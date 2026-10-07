"""Prepare paired SST tasks and summarize manually recorded measurements."""

import argparse
import csv
import hashlib
import json
import math
import random
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASKS = (
    "network-config",
    "network-extension",
    "memory-extension",
    "ember-workload",
    "mercury-runtime",
    "vanadis-program",
    "carcosa-fault",
    "balar-vector",
)
FIELDS = (
    "run_id",
    "task",
    "arm",
    "repeat",
    "verdict",
    "input_tokens",
    "cached_input_tokens",
    "output_tokens",
    "elapsed_seconds",
    "source_files_read",
    "exploratory_calls",
    "human_interventions",
    "usage_source",
    "evidence",
    "notes",
)
AGREEMENTS = """# Evaluation working agreements

Implement the supplied request in this workspace. Source roots are sst-core and sst-elements. Keep changes focused and preserve existing conventions. Do not add dependencies, pull source, push, or create pull requests. Do not access other evaluation runs, the original workspace, evaluator rubrics, or transcript/results files. Do not delegate. Record commands, validation outcomes, and limitations in your final response. Do not claim runtime success without executing relevant checks. Place deliverables under this workspace and keep working notes untracked.
"""


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(source, destination):
    git_root = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "--show-toplevel"], text=True
    ).strip()
    if Path(git_root).resolve() != source.resolve():
        raise ValueError(f"Source must be a Git checkout root: {source}")
    files = subprocess.check_output(["git", "-C", str(source), "ls-files", "-z"], text=True).split(
        "\0"
    )
    commit = subprocess.check_output(
        ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
    ).strip()
    hashes = {}
    for name in files:
        if not name:
            continue
        path = source / name
        if path.is_symlink() or any(
            parent.is_symlink()
            for parent in path.parents
            if parent != source and parent.is_relative_to(source)
        ):
            raise ValueError(f"Snapshot requires reviewing symlink: {path}")
        if not path.exists():
            continue
        if not path.is_file():
            raise ValueError(f"Unsupported tracked entry: {path}")
        target = destination / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        hashes[name] = sha(target)
    return {
        "commit": commit,
        "tracked_working_tree_hashes": hashes,
        "untracked_files": "excluded",
        "git_metadata": "excluded",
    }


def prepare(workspace, output, task, repeats, seed):
    workspace, output = workspace.resolve(), output.resolve()
    if repeats < 1 or task not in TASKS:
        raise ValueError("Choose a supported task and a positive repeat count")
    if output.exists():
        raise ValueError("Output already exists; choose a new directory")
    sources = {name: workspace / name for name in ("sst-core", "sst-elements")}
    for source in sources.values():
        if not source.is_dir():
            raise ValueError(f"Missing source: {source}")
    for source in [
        *sources.values(),
        ROOT / "ofk",
        ROOT / "skills",
        ROOT / "tools",
        ROOT / "evaluation",
    ]:
        if output.is_relative_to(source.resolve()):
            raise ValueError(f"Output must be outside input directory: {source}")
    output.mkdir(parents=True)
    snapshots = output / "snapshots"
    manifests = {name: snapshot(source, snapshots / name) for name, source in sources.items()}
    # Freeze the pilot once so all treatment runs receive identical knowledge.
    shutil.copytree(ROOT / "ofk", snapshots / "pilot/ofk")
    shutil.copytree(ROOT / "skills", snapshots / "pilot/skills")
    shutil.copytree(
        ROOT / "tools", snapshots / "pilot/tools", ignore=shutil.ignore_patterns("__pycache__")
    )
    shutil.copy2(ROOT / "evaluation/prompts" / f"{task}.txt", snapshots / "TASK.txt")
    evaluator = output / "evaluator"
    evaluator.mkdir()
    shutil.copy2(ROOT / "evaluation/rubrics" / f"{task}.json", evaluator / "rubric.json")
    artifacts = {
        str(path.relative_to(output)): sha(path)
        for directory in (snapshots / "pilot", evaluator)
        for path in sorted(directory.rglob("*"))
        if path.is_file()
    }
    artifacts["snapshots/TASK.txt"] = sha(snapshots / "TASK.txt")
    (output / "source-manifest.json").write_text(json.dumps(manifests, indent=2) + "\n")
    rows = []
    for repeat in range(1, repeats + 1):
        for arm in ("baseline", "pilot"):
            run_id = f"{task}-{repeat}-{arm}"
            run = output / "runs" / run_id
            run.mkdir(parents=True)
            for name in sources:
                shutil.copytree(snapshots / name, run / name)
            instructions = AGREEMENTS
            if arm == "pilot":
                shutil.copytree(snapshots / "pilot", run / "sst-ai-tools")
                instructions += "\nUse sst-ai-tools/ofk/index.md and task-relevant skills under sst-ai-tools/skills. Load references selectively.\n"
            (run / "AGENTS.md").write_text(instructions)
            shutil.copy2(snapshots / "TASK.txt", run / "TASK.txt")
            rows.append(
                {
                    **dict.fromkeys(FIELDS, ""),
                    "run_id": run_id,
                    "task": task,
                    "arm": arm,
                    "repeat": repeat,
                }
            )
    random.Random(seed).shuffle(rows)
    with (output / "results.csv").open("w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "task": task,
        "repeats": repeats,
        "seed": seed,
        "frozen_artifact_sha256": artifacts,
        "evaluator_rubric": "evaluator/rubric.json",
        "run_order": [r["run_id"] for r in rows],
        "runtime": {
            name: shutil.which(name) for name in ("sst", "sst-test-core", "sst-test-elements")
        },
        "configuration_to_record": [
            "model",
            "reasoning effort",
            "agent version",
            "tool permissions",
            "budget",
            "isolated installation prefixes",
            "cache accounting",
        ],
    }
    (output / "experiment.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return {
        "output": str(output),
        "run_order": manifest["run_order"],
        "runtime": manifest["runtime"],
    }


def summarize(path):
    with path.open(newline="") as file:
        reader = csv.DictReader(file)
        if reader.fieldnames is None or not set(FIELDS).issubset(reader.fieldnames):
            raise ValueError("Results CSV is missing required columns")
        rows = list(reader)
    identities = set()
    run_ids = set()
    integer_fields = (
        "input_tokens",
        "cached_input_tokens",
        "output_tokens",
        "source_files_read",
        "exploratory_calls",
        "human_interventions",
    )
    for line, row in enumerate(rows, start=2):
        if None in row or any(value is None for value in row.values()):
            raise ValueError(f"Results row {line} has the wrong number of columns")
        for key in FIELDS:
            row[key] = row[key].strip()
        if row["arm"] not in ("baseline", "pilot") or row["verdict"] not in (
            "",
            "pass",
            "fail",
            "blocked",
        ):
            raise ValueError(f"Results row {line} has an invalid arm or verdict")
        if (
            not row["run_id"]
            or not row["task"]
            or not row["repeat"].isdigit()
            or int(row["repeat"]) < 1
        ):
            raise ValueError(f"Results row {line} requires run_id, task and a positive repeat")
        row["repeat"] = str(int(row["repeat"]))
        identity = (row["task"], row["repeat"], row["arm"])
        if identity in identities or row["run_id"] in run_ids:
            raise ValueError(f"Duplicate run or task/repeat/arm at results row {line}")
        identities.add(identity)
        run_ids.add(row["run_id"])
        for key in integer_fields:
            if row[key] and not row[key].isdigit():
                raise ValueError(
                    f"Results row {line}: {key} must be a nonnegative integer or blank"
                )
        if row["elapsed_seconds"]:
            elapsed = float(row["elapsed_seconds"])
            if not math.isfinite(elapsed) or elapsed < 0:
                raise ValueError(
                    f"Results row {line}: elapsed_seconds must be finite and nonnegative"
                )
        if (
            row["cached_input_tokens"]
            and row["input_tokens"]
            and int(row["cached_input_tokens"]) > int(row["input_tokens"])
        ):
            raise ValueError(f"Results row {line}: cached input exceeds total input")
    result = {"arms": {}, "paired_token_comparisons": [], "unpaired_runs": []}
    for arm in ("baseline", "pilot"):
        group = [r for r in rows if r["arm"] == arm]
        result["arms"][arm] = {
            "runs": len(group),
            "pass": sum(r["verdict"] == "pass" for r in group),
            "fail": sum(r["verdict"] == "fail" for r in group),
            "blocked": sum(r["verdict"] == "blocked" for r in group),
            "unscored": sum(not r["verdict"] for r in group),
        }
    pairs = {}
    for row in rows:
        pairs.setdefault((row["task"], row["repeat"]), {})[row["arm"]] = row
    for (task, repeat), pair in pairs.items():
        if set(pair) != {"baseline", "pilot"}:
            result["unpaired_runs"].extend(row["run_id"] for row in pair.values())
            continue
        totals = {}
        for arm, row in pair.items():
            if row["input_tokens"] and row["output_tokens"]:
                totals[arm] = int(row["input_tokens"]) + int(row["output_tokens"])
        if len(totals) == 2:
            result["paired_token_comparisons"].append(
                {
                    "task": task,
                    "repeat": repeat,
                    "baseline_total": totals["baseline"],
                    "pilot_total": totals["pilot"],
                    "saved_tokens": totals["baseline"] - totals["pilot"],
                    "both_pass": all(r["verdict"] == "pass" for r in pair.values()),
                }
            )
    result["accounting"] = (
        "Input includes cached input; do not add cached_input_tokens again. Blank usage is unknown, never zero. Failed and blocked runs remain in arm counts."
    )
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("prepare")
    command.add_argument("--workspace", type=Path, default=ROOT.parent)
    command.add_argument("--output", type=Path, required=True)
    command.add_argument("--task", choices=TASKS, default=TASKS[0])
    command.add_argument("--repeats", type=int, default=1)
    command.add_argument("--seed", type=int, default=42)
    command = commands.add_parser("summarize")
    command.add_argument("--results", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            if args.repeats < 1:
                raise ValueError("Repeats must be positive")
            result = prepare(
                args.workspace.resolve(), args.output.resolve(), args.task, args.repeats, args.seed
            )
        else:
            result = summarize(args.results)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        parser.exit(2, f"{error}\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
