"""Local inspection, validation, test planning, and reviewed provenance updates."""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "ofk"


def read_document(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?=\n|\Z)(.*)\Z", text, re.DOTALL)
    if not match:
        raise ValueError("Missing or unterminated frontmatter")
    metadata = json.loads(match[1])
    if not isinstance(metadata, dict):
        raise ValueError("Frontmatter must be a JSON object")
    return metadata, match[2]


def source_roots(args):
    workspace = args.workspace.resolve()
    return {
        "sst-core": (args.core or workspace / "sst-core").resolve(),
        "sst-elements": (args.elements or workspace / "sst-elements").resolve(),
    }


def source_path(source, roots):
    relative = source["x-path"]
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError("Source x-path must be a nonempty relative path")
    root = roots[source["x-repository"]].resolve()
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError("Source path escapes repository")
    return path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def exact_case(path, root):
    # Case-insensitive filesystems accept paths that break on Linux and GitHub.
    current = root
    for part in path.relative_to(root).parts:
        try:
            entries = os.listdir(current)
        except OSError:
            return False
        if part not in entries:
            return False
        current = current / part
    return True


def document_sources(metadata, require_recorded=True):
    sources = metadata.get("sources", [])
    if not isinstance(sources, list):
        raise ValueError("Sources must be a list")
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError("Each source must be an object")
        if not isinstance(source.get("resource"), str) or not source["resource"].strip():
            raise ValueError("Source has no resource")
        if "x-repository" not in source:
            if "x-path" in source:
                raise ValueError("Local source path requires x-repository")
            continue
        if source["x-repository"] not in ("sst-core", "sst-elements"):
            raise ValueError("Unknown source x-repository")
        relative = source.get("x-path")
        if (
            not isinstance(relative, str)
            or not relative
            or Path(relative).is_absolute()
            or ".." in Path(relative).parts
        ):
            raise ValueError("Source x-path must stay inside its repository")
        if not require_recorded:
            continue
        for key, pattern in (
            ("x-sha256", r"[a-f0-9]{64}"),
            ("x-commit", r"(?:[a-f0-9]{40}|[a-f0-9]{64})"),
        ):
            if not isinstance(source.get(key), str) or not re.fullmatch(pattern, source[key]):
                raise ValueError(f"Missing or invalid source {key}")
    return sources


def check(bundle, roots=None):
    issues = []
    count = 0
    external_sources = []
    unchecked_local_sources = []
    for path in sorted(bundle.rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        if path.name not in ("index.md", "log.md"):
            count += 1
            try:
                metadata, _ = read_document(path)
                if not isinstance(metadata.get("type"), str) or not metadata["type"].strip():
                    raise ValueError("Missing concept type")
                for source in document_sources(metadata):
                    if "x-repository" not in source:
                        external_sources.append(source["resource"])
                        continue
                    if roots is None:
                        unchecked_local_sources.append(source["resource"])
                        continue
                    local = source_path(source, roots)
                    if not local.is_file():
                        issues.append(f"{path.relative_to(bundle)}: missing source {local}")
                    elif not exact_case(local, roots[source["x-repository"]].resolve()):
                        issues.append(
                            f"{path.relative_to(bundle)}: source path case mismatch {local}"
                        )
                    elif digest(local) != source["x-sha256"]:
                        issues.append(f"{path.relative_to(bundle)}: review needed: {local}")
            except (ValueError, KeyError, TypeError) as error:
                issues.append(f"{path.relative_to(bundle)}: invalid metadata: {error}")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            linked = (
                bundle / target.lstrip("/") if target.startswith("/") else path.parent / target
            ).resolve()
            if not linked.is_relative_to(bundle.resolve()) or not linked.exists():
                issues.append(f"{path.relative_to(bundle)}: broken bundle link {target}")
    return {
        "concepts": count,
        "issues": issues,
        "external_sources_not_checked": sorted(set(external_sources)),
        "local_sources_not_checked": sorted(set(unchecked_local_sources)),
    }


def plan_tests(target, roots, ranks=1, threads=1):
    if not re.fullmatch(r"[A-Za-z0-9_-]+", target):
        raise ValueError("Target must be core or an element directory name")
    if ranks < 1 or threads < 1:
        raise ValueError("Ranks and threads must be positive")
    if target == "core":
        runner = "sst-test-core"
        element = roots["sst-core"]
    else:
        runner = "sst-test-elements"
        element = roots["sst-elements"] / "src/sst/elements" / target
    if not element.is_dir():
        raise ValueError(f"Missing source directory: {element}")
    directories = [element / name for name in ("tests", "test") if (element / name).is_dir()]
    suites = sorted(path for directory in directories for path in directory.rglob("testsuite_*.py"))
    if not suites:
        configurations = [
            str(path)
            for directory in directories + [element / "examples"]
            for path in sorted(directory.glob("*.py"))
            if re.search(r"^import sst\s*$", path.read_text(encoding="utf-8"), re.MULTILINE)
        ]
        return {
            "command": None,
            "discovery_command": None,
            "runner_available": shutil.which(runner) is not None,
            "standalone_configurations": configurations,
            "integration_required": not configurations,
            "scope": "No native runner suites found. Inspect standalone configurations or validate through consuming elements, including prerequisites and a behavioral oracle.",
        }
    # Explicit files include non-default suites and nested non-package directories.
    paths = [str(path) for path in suites]
    return {
        "suite_files": [str(path) for path in suites],
        "command": [runner, "-p", *paths, "-r", str(ranks), "-t", str(threads)],
        "discovery_command": [runner, "-p", *paths, "-l"],
        "runner_available": shutil.which(runner) is not None,
        "scope": "All discovered suite files, including non-default types. Narrow by changed behavior and prerequisites before executing; runner category filters still apply.",
    }


def element_catalog(roots, bundle=BUNDLE):
    source = roots["sst-elements"] / "src/sst/elements"
    if not source.is_dir():
        raise ValueError(f"Missing elements directory: {source}")
    entries = []
    issues = []
    for directory in sorted(source.iterdir()):
        if not directory.is_dir() or not (directory / "Makefile.am").is_file():
            continue
        profile = bundle / "elements" / directory.name / "use-cases.md"
        metadata = {}
        if profile.is_file():
            try:
                metadata = read_document(profile)[0]
                if metadata.get("x-element") != directory.name:
                    issues.append(f"{profile}: x-element does not match source directory")
                for key in ("x-role", "x-coverage"):
                    if not isinstance(metadata.get(key), str) or not metadata[key].strip():
                        issues.append(f"{profile}: missing {key}")
            except ValueError as error:
                issues.append(f"{profile}: invalid metadata: {error}")
        entries.append(
            {
                "element": directory.name,
                "role": metadata.get("x-role"),
                "description": metadata.get("description"),
                "profile": str(profile) if profile.is_file() else None,
                "coverage": metadata.get("x-coverage", "missing"),
                "runner_suites": [
                    str(path.relative_to(directory))
                    for folder in ("tests", "test")
                    for path in sorted((directory / folder).rglob("testsuite_*.py"))
                ],
            }
        )
    names = {entry["element"] for entry in entries}
    orphan_profiles = sorted(
        path.parent.name
        for path in (bundle / "elements").glob("*/use-cases.md")
        if path.parent.name not in names
    )
    return {
        "source_elements": len(entries),
        "documented_elements": sum(entry["profile"] is not None for entry in entries),
        "missing_profiles": [entry["element"] for entry in entries if entry["profile"] is None],
        "orphan_profiles": orphan_profiles,
        "issues": issues + [f"Profile has no source element: {name}" for name in orphan_profiles],
        "elements": entries,
    }


def inspect(roots):
    result = {"repositories": {}, "executables": {}}
    for name, root in roots.items():
        item = {"path": str(root), "exists": root.is_dir()}
        if root.is_dir():
            proc = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "--show-toplevel"],
                capture_output=True,
                text=True,
            )
            if proc.returncode != 0 or Path(proc.stdout.strip()).resolve() != root.resolve():
                item.update(commit=None, dirty=None)
                result["repositories"][name] = item
                continue
            proc = subprocess.run(
                ["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True
            )
            item["commit"] = proc.stdout.strip() if proc.returncode == 0 else None
            proc = subprocess.run(
                ["git", "-C", str(root), "status", "--porcelain"], capture_output=True, text=True
            )
            item["dirty"] = bool(proc.stdout.strip()) if proc.returncode == 0 else None
        result["repositories"][name] = item
    for name in (
        "sst",
        "sst-info",
        "sst-config",
        "sst-test-core",
        "sst-test-elements",
        "clang-format",
        "mpicxx",
        "make",
    ):
        result["executables"][name] = shutil.which(name)
    return result


def record_source(document, roots):
    path = document.resolve()
    if not path.is_relative_to(BUNDLE.resolve()):
        raise ValueError("Document must be inside this repository's OFK bundle")
    metadata, body = read_document(path)
    for source in document_sources(metadata, require_recorded=False):
        if "x-repository" not in source:
            continue
        local = source_path(source, roots)
        repo = source["x-repository"]
        if not exact_case(local, roots[repo].resolve()):
            raise ValueError(f"Source path case mismatch: {source['x-path']}")
        commit = subprocess.check_output(
            ["git", "-C", str(roots[repo]), "rev-parse", "HEAD"], text=True
        ).strip()
        source["x-sha256"] = digest(local)
        source["x-commit"] = commit
        source["resource"] = (
            f"https://github.com/sstsimulator/{repo}/blob/{commit}/{source['x-path']}"
        )
    path.write_text("---\n" + json.dumps(metadata, indent=2) + "\n---" + body, encoding="utf-8")
    return {
        "document": str(path),
        "provenance_updated": True,
        "semantic_verification": False,
        "external_sources_not_refreshed": [
            source["resource"]
            for source in metadata.get("sources", [])
            if "x-repository" not in source
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("inspect", "check", "catalog", "plan-tests", "record-source"):
        command = commands.add_parser(name)
        command.add_argument("--workspace", type=Path, default=ROOT.parent)
        command.add_argument("--core", type=Path)
        command.add_argument("--elements", type=Path)
        if name == "plan-tests":
            command.add_argument(
                "--target", required=True, help="core or an element source-directory name"
            )
            command.add_argument("--ranks", type=int, default=1)
            command.add_argument("--threads", type=int, default=1)
        if name == "record-source":
            command.add_argument(
                "--document",
                type=Path,
                required=True,
                help="Use only after reviewing source changes and reconciling claims",
            )
    args = parser.parse_args()
    roots = source_roots(args)
    try:
        if args.command == "inspect":
            result = inspect(roots)
        elif args.command == "check":
            result = check(BUNDLE, roots)
            catalog = element_catalog(roots)
            result["coverage"] = {key: value for key, value in catalog.items() if key != "elements"}
            result["issues"].extend(
                f"Missing use-case profile: {name}" for name in catalog["missing_profiles"]
            )
            result["issues"].extend(catalog["issues"])
        elif args.command == "catalog":
            result = element_catalog(roots)
        elif args.command == "plan-tests":
            if args.ranks < 1 or args.threads < 1:
                raise ValueError("Ranks and threads must be positive")
            result = plan_tests(args.target, roots, args.ranks, args.threads)
        else:
            result = record_source(args.document, roots)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(2, f"{error}\n")
    print(json.dumps(result, indent=2))
    return 1 if result.get("issues") else 0


if __name__ == "__main__":
    raise SystemExit(main())
