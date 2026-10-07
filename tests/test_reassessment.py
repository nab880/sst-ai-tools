import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

REVIEW = Path(__file__).resolve().parents[1] / "reviews/core/2026-10-06"
spec = importlib.util.spec_from_file_location("reassessment", REVIEW / "summarize_reassessment.py")
reassessment = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reassessment)


class ReassessmentEvidence(unittest.TestCase):
    def test_archived_findings_still_reproduce_with_stronger_oracle(self):
        result = reassessment.analyze(REVIEW / "evidence")
        self.assertEqual(len(result["findings"]), 11)
        self.assertTrue(all(f["status"] == "reproduced" for f in result["findings"].values()))
        self.assertTrue(result["raw_controls_passed"])

    def test_element_outputs_are_required_for_histogram_claims(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "evidence"
            shutil.copytree(REVIEW / "evidence", folder)
            integer = folder / "element_stats_integer.out"
            integer.write_text(
                integer.read_text().replace("Bin0:5-54.u64 = 0", "Bin0:5-54.u64 = 1")
            )
            floating = folder / "element_stats_floating.out"
            floating.write_text(
                floating.read_text().replace("NumItemsBinned.u64 = 0", "NumItemsBinned.u64 = 4")
            )
            result = reassessment.analyze(folder)
            for identifier in ("F08", "F09"):
                self.assertEqual(result["findings"][identifier]["status"], "requires-investigation")

    def test_failed_build_cannot_reuse_stale_run_output(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "evidence"
            shutil.copytree(REVIEW / "evidence", folder)
            path = folder / "results.json"
            results = json.loads(path.read_text())
            results["build"]["exit_code"] = 1
            path.write_text(json.dumps(results))
            with self.assertRaisesRegex(ValueError, "compilation"):
                reassessment.analyze(folder)

    def test_workspace_revision_is_not_an_installed_runtime_revision(self):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "evidence"
            shutil.copytree(REVIEW / "evidence", folder)
            path = folder / "results.json"
            results = json.loads(path.read_text())
            results["workspace_revisions"] = results.pop("revisions")
            results["runtime_identity"] = {"source_revision_binding": "not verified"}
            path.write_text(json.dumps(results))
            analysis = reassessment.analyze(folder)
            self.assertNotIn("revisions", analysis)
            self.assertEqual(analysis["runtime_identity"], results["runtime_identity"])


if __name__ == "__main__":
    unittest.main()
