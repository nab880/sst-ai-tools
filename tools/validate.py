"""Validate repository links, skills, knowledge provenance, and element coverage."""

import argparse
import json
import os
import re
import sys
from pathlib import Path

import yaml

from sst_tools import BUNDLE, ROOT, check, element_catalog, source_roots


def validate_repository(root):
    issues = []
    skill_count = 0
    paths = []
    for directory, folders, files in os.walk(root):
        folders[:] = sorted(
            folder
            for folder in folders
            if folder not in {".git", ".venv", ".runtime", ".ruff_cache", "__pycache__"}
        )
        paths.extend(Path(directory) / name for name in sorted(files) if name.endswith(".md"))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            bundle = root / "ofk"
            base = bundle if path.is_relative_to(bundle) and target.startswith("/") else path.parent
            destination = (base / target.lstrip("/")).resolve()
            if not destination.exists() or not destination.is_relative_to(root.resolve()):
                issues.append(f"{path.relative_to(root)}: broken local link {target}")
        if path.name == "SKILL.md" and path.parent.parent == root / "skills":
            skill_count += 1
            try:
                frontmatter = re.match(r"\A---\n(.*?)\n---(?=\n|\Z)", text, re.DOTALL)
                if not frontmatter:
                    raise ValueError("Missing or unterminated frontmatter")
                metadata = yaml.safe_load(frontmatter[1])
                name = metadata.get("name", "")
                if name != path.parent.name or not re.fullmatch(r"[a-z0-9-]{1,63}", name):
                    raise ValueError("Skill name does not match its directory")
                if (
                    not isinstance(metadata.get("description"), str)
                    or not metadata["description"].strip()
                ):
                    raise ValueError("Missing skill description")
            except (ValueError, TypeError, AttributeError, yaml.YAMLError) as error:
                issues.append(f"{path.relative_to(root)}: {error}")
    prompts = root / "evaluation/prompts"
    rubrics = root / "evaluation/rubrics"
    for prompt in sorted(prompts.glob("*.txt")):
        rubric = rubrics / (prompt.stem + ".json")
        if not rubric.is_file():
            issues.append(f"Missing evaluator rubric: {prompt.stem}")
            continue
        try:
            metadata = json.loads(rubric.read_text(encoding="utf-8"))
            if metadata.get("task") != prompt.stem or not metadata.get("criteria"):
                issues.append(f"Invalid evaluator rubric: {prompt.stem}")
        except (ValueError, AttributeError) as error:
            issues.append(f"Invalid evaluator rubric {prompt.stem}: {error}")
    for rubric in sorted(rubrics.glob("*.json")):
        if not (prompts / (rubric.stem + ".txt")).is_file():
            issues.append(f"Missing task prompt: {rubric.stem}")
    return {"skills": skill_count, "issues": issues}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace", type=Path, default=ROOT.parent)
    parser.add_argument("--core", type=Path)
    parser.add_argument("--elements", type=Path)
    parser.add_argument(
        "--repository-only", action="store_true", help="Skip checks requiring SST sources"
    )
    args = parser.parse_args()
    result = validate_repository(ROOT)
    try:
        roots = None if args.repository_only else source_roots(args)
        knowledge = check(BUNDLE, roots)
        result["concepts"] = knowledge["concepts"]
        result["external_sources_not_checked"] = knowledge["external_sources_not_checked"]
        result["local_sources_not_checked"] = knowledge["local_sources_not_checked"]
        result["issues"].extend(knowledge["issues"])
        if roots is not None:
            catalog = element_catalog(roots)
            result["elements"] = catalog["source_elements"]
            result["documented_elements"] = catalog["documented_elements"]
            result["issues"].extend(
                f"Missing use-case profile: {name}" for name in catalog["missing_profiles"]
            )
            result["issues"].extend(catalog["issues"])
    except (OSError, ValueError, KeyError) as error:
        result["issues"].append(str(error))
    print(json.dumps(result, indent=2))
    return bool(result["issues"])


if __name__ == "__main__":
    sys.exit(main())
