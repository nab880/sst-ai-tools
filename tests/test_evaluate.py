import csv
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "evaluate", Path(__file__).resolve().parents[1] / "tools/evaluate.py"
)
evaluate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(evaluate)


class ResultsAccounting(unittest.TestCase):
    def write_rows(self, path, rows):
        with path.open("w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=evaluate.FIELDS)
            writer.writeheader()
            writer.writerows(rows)

    def test_invalid_measurements_and_duplicate_pairs_are_rejected(self):
        valid = {"run_id": "a", "task": "network-config", "repeat": "1", "arm": "baseline"}
        changes = [
            {"arm": "other"},
            {"verdict": "success"},
            {"repeat": "0"},
            {"input_tokens": "-1"},
            {"output_tokens": "1.5"},
            {"elapsed_seconds": "NaN"},
            {"elapsed_seconds": "-1"},
            {"input_tokens": "10", "cached_input_tokens": "11"},
        ]
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.csv"
            for change in changes:
                with self.subTest(change=change):
                    self.write_rows(path, [{**valid, **change}])
                    with self.assertRaises(ValueError):
                        evaluate.summarize(path)
            self.write_rows(path, [valid, {**valid, "run_id": "b", "repeat": "01"}])
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                evaluate.summarize(path)

    def test_unpaired_runs_remain_visible(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.csv"
            self.write_rows(path, [{"run_id": "a", "task": "task", "repeat": "1", "arm": "pilot"}])
            result = evaluate.summarize(path)
            self.assertEqual(result["unpaired_runs"], ["a"])
            self.assertEqual(result["paired_token_comparisons"], [])

    def test_unknown_usage_is_not_zero_and_failures_count(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "results.csv"
            rows = [
                {
                    "run_id": "a",
                    "task": "network-config",
                    "repeat": "1",
                    "arm": "baseline",
                    "verdict": "fail",
                    "input_tokens": "100",
                    "cached_input_tokens": "50",
                    "output_tokens": "20",
                },
                {
                    "run_id": "b",
                    "task": "network-config",
                    "repeat": "1",
                    "arm": "pilot",
                    "verdict": "pass",
                    "input_tokens": "70",
                    "output_tokens": "20",
                },
                {
                    "run_id": "c",
                    "task": "network-config",
                    "repeat": "2",
                    "arm": "baseline",
                    "verdict": "blocked",
                },
                {"run_id": "d", "task": "network-config", "repeat": "2", "arm": "pilot"},
            ]
            with path.open("w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=evaluate.FIELDS)
                writer.writeheader()
                writer.writerows(rows)
            result = evaluate.summarize(path)
            self.assertEqual(result["arms"]["baseline"]["fail"], 1)
            self.assertEqual(result["arms"]["baseline"]["blocked"], 1)
            self.assertEqual(result["arms"]["pilot"]["unscored"], 1)
            self.assertEqual(len(result["paired_token_comparisons"]), 1)
            pair = result["paired_token_comparisons"][0]
            self.assertEqual(pair["saved_tokens"], 30)
            self.assertEqual(pair["baseline_total"], 120)
            self.assertFalse(pair["both_pass"])


class ExperimentPreparation(unittest.TestCase):
    def test_dangling_tracked_symlink_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source"
            source.mkdir()
            (source / "broken").symlink_to("missing")
            with patch.object(
                evaluate.subprocess, "check_output", side_effect=[str(source), "broken\0", "a" * 40]
            ):
                with self.assertRaisesRegex(ValueError, "symlink"):
                    evaluate.snapshot(source, root / "snapshot")

    def test_nested_source_does_not_inherit_parent_repository(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(evaluate.subprocess, "check_output", return_value=str(root)):
                with self.assertRaisesRegex(ValueError, "checkout root"):
                    evaluate.snapshot(root / "nested-source", root / "snapshot")

    def test_freezes_working_tree_prompt_knowledge_and_private_rubric(self):
        with tempfile.TemporaryDirectory() as directory:
            workspace = Path(directory)
            for name in ("sst-core", "sst-elements"):
                source = workspace / name
                source.mkdir()
                subprocess.run(["git", "init", "-q", str(source)], check=True)
                (source / "api.h").write_text("committed\n")
                subprocess.run(["git", "-C", str(source), "add", "api.h"], check=True)
                subprocess.run(
                    [
                        "git",
                        "-C",
                        str(source),
                        "-c",
                        "user.name=Test",
                        "-c",
                        "user.email=test@example.org",
                        "-c",
                        "commit.gpgsign=false",
                        "commit",
                        "-qm",
                        "Fixture",
                    ],
                    check=True,
                )
                (source / "api.h").write_text("local edit\n")
                (source / "notes.md").write_text("excluded\n")
            pilot = workspace / "pilot"
            for part in ("ofk", "skills", "tools", "evaluation/prompts", "evaluation/rubrics"):
                (pilot / part).mkdir(parents=True)
            (pilot / "ofk/index.md").write_text("Frozen guide\n")
            prompt = pilot / "evaluation/prompts/network-config.txt"
            prompt.write_text("Frozen task\n")
            rubric = pilot / "evaluation/rubrics/network-config.json"
            rubric.write_text('{"task":"network-config","criteria":["Original"]}\n')
            output = workspace / "experiment"
            with patch.object(evaluate, "ROOT", pilot):
                evaluate.prepare(workspace, output, "network-config", 1, 42)
                with self.assertRaisesRegex(ValueError, "outside input"):
                    evaluate.prepare(workspace, pilot / "ofk/nested", "network-config", 1, 42)
            prompt.write_text("Changed task\n")
            rubric.write_text("Changed rubric\n")
            for arm in ("baseline", "pilot"):
                run = output / "runs" / f"network-config-1-{arm}"
                self.assertEqual((run / "sst-core/api.h").read_text(), "local edit\n")
                self.assertFalse((run / "sst-core/notes.md").exists())
                self.assertFalse((run / "sst-core/.git").exists())
                self.assertFalse((run / "evaluator").exists())
                self.assertEqual((run / "TASK.txt").read_text(), "Frozen task\n")
            manifest = json.loads((output / "experiment.json").read_text())
            self.assertIn("Original", (output / manifest["evaluator_rubric"]).read_text())
            for name, expected in manifest["frozen_artifact_sha256"].items():
                self.assertEqual(evaluate.sha(output / name), expected)


if __name__ == "__main__":
    unittest.main()
