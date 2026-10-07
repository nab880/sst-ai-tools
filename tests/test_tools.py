import importlib.util
import json
import tempfile
import unittest
from types import SimpleNamespace
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "sst_tools", Path(__file__).resolve().parents[1] / "tools/sst_tools.py"
)
tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tools)


class KnowledgeChecks(unittest.TestCase):
    def test_inspection_does_not_attribute_parent_repository_to_snapshot(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            copied_source = root / "sst-core"
            copied_source.mkdir()
            with patch.object(
                tools.subprocess,
                "run",
                return_value=SimpleNamespace(returncode=0, stdout=str(root)),
            ):
                result = tools.inspect({"sst-core": copied_source})
            self.assertIsNone(result["repositories"]["sst-core"]["commit"])
            self.assertIsNone(result["repositories"]["sst-core"]["dirty"])

    def test_source_change_missing_source_and_broken_link(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "bundle"
            source_root = root / "sst-core"
            bundle.mkdir()
            source_root.mkdir()
            source = source_root / "api.h"
            source.write_text("original")
            metadata = {
                "type": "SST Guide",
                "sources": [
                    {
                        "resource": "https://example.org/api.h",
                        "x-repository": "sst-core",
                        "x-path": "api.h",
                        "x-commit": "a" * 40,
                        "x-sha256": tools.digest(source),
                    }
                ],
            }
            document = bundle / "guide.md"
            document.write_text("---\n" + json.dumps(metadata) + "\n---\n[Self](/guide.md)\n")
            roots = {"sst-core": source_root}
            self.assertEqual(tools.check(bundle, roots)["issues"], [])
            source.write_text("changed")
            self.assertIn("review needed", tools.check(bundle, roots)["issues"][0])
            source.unlink()
            self.assertIn("missing source", tools.check(bundle, roots)["issues"][0])
            document.write_text(document.read_text() + "[Missing](missing.md)\n")
            self.assertTrue(
                any("broken bundle link" in issue for issue in tools.check(bundle, roots)["issues"])
            )

    def test_source_path_case_must_match_checkout(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "bundle"
            source_root = root / "sst-core"
            bundle.mkdir()
            source_root.mkdir()
            source = source_root / "Api.h"
            source.write_text("original")
            metadata = {
                "type": "SST Guide",
                "sources": [
                    {
                        "resource": "https://example.org/api.h",
                        "x-repository": "sst-core",
                        "x-path": "api.h",
                        "x-commit": "a" * 40,
                        "x-sha256": tools.digest(source),
                    }
                ],
            }
            (bundle / "guide.md").write_text("---\n" + json.dumps(metadata) + "\n---\nBody\n")
            issues = tools.check(bundle, {"sst-core": source_root})["issues"]
            self.assertEqual(len(issues), 1)
            self.assertRegex(issues[0], "missing source|case mismatch")
            self.assertFalse(tools.exact_case(source_root / "api.h", source_root))
            self.assertTrue(tools.exact_case(source, source_root))

    def test_source_cannot_escape_checkout(self):
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(ValueError):
                tools.source_path(
                    {"x-repository": "sst-core", "x-path": "../outside"},
                    {"sst-core": Path(directory)},
                )

    def test_test_plan_preserves_paths_and_parallel_options(self):
        with tempfile.TemporaryDirectory(prefix="sst workspace ") as directory:
            root = Path(directory)
            suite = root / "src/sst/elements/merlin/tests"
            suite.mkdir(parents=True)
            (suite / "testsuite_default_merlin.py").write_text("pass\n")
            result = tools.plan_tests("merlin", {"sst-elements": root}, 2, 3)
            self.assertEqual(
                result["command"],
                [
                    "sst-test-elements",
                    "-p",
                    str(suite / "testsuite_default_merlin.py"),
                    "-r",
                    "2",
                    "-t",
                    "3",
                ],
            )
            self.assertEqual(result["discovery_command"][-1], "-l")

    def test_standalone_configs_are_not_reported_as_runner_coverage(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            suite = root / "src/sst/elements/carcosa/tests"
            suite.mkdir(parents=True)
            model = suite / "testFault.py"
            model.write_text("import sst\n")
            (suite / "helper.py").write_text("import os\n")
            result = tools.plan_tests("carcosa", {"sst-elements": root})
            self.assertIsNone(result["command"])
            self.assertIsNone(result["discovery_command"])
            self.assertEqual(result["standalone_configurations"], [str(model)])

    def test_mercury_hg_suite_names_are_discovered_by_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            suite = root / "src/sst/elements/mercury/tests"
            suite.mkdir(parents=True)
            hg = suite / "testsuite_default_hg.py"
            hg.write_text("pass\n")
            result = tools.plan_tests("mercury", {"sst-elements": root})
            self.assertEqual(result["suite_files"], [str(hg)])
            self.assertEqual(result["command"][2], str(hg))

    def test_test_plan_includes_nested_and_nondefault_suites(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            suite = root / "src/sst/elements/example/tests/nested"
            suite.mkdir(parents=True)
            weekly = suite / "testsuite_weekly_example.py"
            weekly.write_text("pass\n")
            plan = tools.plan_tests("example", {"sst-elements": root})
            self.assertEqual(plan["command"][2], str(weekly))
            self.assertEqual(plan["discovery_command"][2], str(weekly))

    def test_invalid_metadata_is_reported(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory)
            (bundle / "bad.md").write_text("No frontmatter")
            self.assertIn("invalid metadata", tools.check(bundle, {})["issues"][0])

    def test_malformed_metadata_shapes_and_missing_hash_are_reported(self):
        cases = [
            [],
            None,
            {"type": "Guide", "sources": "bad"},
            {"type": "Guide", "sources": [None]},
            {
                "type": "Guide",
                "sources": [{"resource": "url", "x-repository": "sst-core", "x-path": "a.h"}],
            },
        ]
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory)
            for metadata in cases:
                with self.subTest(metadata=metadata):
                    (bundle / "guide.md").write_text("---\n" + json.dumps(metadata) + "\n---\nBody")
                    self.assertIn("invalid metadata", tools.check(bundle)["issues"][0])

    def test_frontmatter_delimiter_inside_a_string_and_offline_check(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory)
            resource = "https://example.org/a.h"
            metadata = {
                "type": "Guide---Example",
                "sources": [
                    {
                        "resource": resource,
                        "x-repository": "sst-core",
                        "x-path": "a.h",
                        "x-commit": "a" * 40,
                        "x-sha256": "b" * 64,
                    }
                ],
            }
            (bundle / "guide.md").write_text("---\n" + json.dumps(metadata) + "\n---\nBody")
            result = tools.check(bundle)
            self.assertEqual(result["issues"], [])
            self.assertEqual(result["local_sources_not_checked"], [resource])

    def test_external_provenance_is_preserved_without_claiming_freshness(self):
        with tempfile.TemporaryDirectory() as directory:
            bundle = Path(directory)
            resource = "https://example.org/toolchain/commit/guide.md"
            metadata = {"type": "SST Guide", "sources": [{"resource": resource}]}
            (bundle / "guide.md").write_text("---\n" + json.dumps(metadata) + "\n---\nGuide\n")
            result = tools.check(bundle, {})
            self.assertEqual(result["issues"], [])
            self.assertEqual(result["external_sources_not_checked"], [resource])
            metadata["sources"][0]["x-path"] = "local.h"
            (bundle / "guide.md").write_text("---\n" + json.dumps(metadata) + "\n---\nGuide\n")
            self.assertIn("requires x-repository", tools.check(bundle, {})["issues"][0])

    def test_test_directory_and_library_without_suites(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            elements = root / "src/sst/elements"
            suite = elements / "zodiac/test"
            suite.mkdir(parents=True)
            (suite / "testsuite_default_SiriusZodiacTrace.py").write_text("pass\n")
            (elements / "hermes").mkdir()
            zodiac = tools.plan_tests("zodiac", {"sst-elements": root})
            self.assertEqual(
                zodiac["command"][2], str(suite / "testsuite_default_SiriusZodiacTrace.py")
            )
            hermes = tools.plan_tests("hermes", {"sst-elements": root})
            self.assertIsNone(hermes["command"])
            self.assertTrue(hermes["integration_required"])

    def test_catalog_detects_new_element_without_profile(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            elements = root / "src/sst/elements"
            new = elements / "newElement"
            new.mkdir(parents=True)
            (new / "Makefile.am").write_text("\n")
            catalog = tools.element_catalog({"sst-elements": root}, root / "bundle")
            self.assertEqual(catalog["source_elements"], 1)
            self.assertEqual(catalog["missing_profiles"], ["newElement"])

    def test_catalog_rejects_mismatched_and_orphan_profiles(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            element = root / "src/sst/elements/example"
            element.mkdir(parents=True)
            (element / "Makefile.am").touch()
            bundle = root / "bundle"
            for name in ("example", "removed"):
                profile = bundle / "elements" / name / "use-cases.md"
                profile.parent.mkdir(parents=True)
                profile.write_text('---\n{"type":"Guide","x-element":"wrong"}\n---\nBody')
            result = tools.element_catalog({"sst-elements": root}, bundle)
            self.assertEqual(result["orphan_profiles"], ["removed"])
            self.assertTrue(any("x-element" in issue for issue in result["issues"]))

    def test_planner_rejects_escape_and_invalid_parallelism(self):
        with tempfile.TemporaryDirectory() as directory:
            roots = {"sst-elements": Path(directory)}
            with self.assertRaises(ValueError):
                tools.plan_tests("../outside", roots)
            with self.assertRaises(ValueError):
                tools.plan_tests("merlin", roots, ranks=0)


if __name__ == "__main__":
    unittest.main()
