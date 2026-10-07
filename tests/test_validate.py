import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1] / "tools"
sys.path.insert(0, str(TOOLS))
spec = importlib.util.spec_from_file_location("validate", TOOLS / "validate.py")
validate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate)


class RepositoryValidation(unittest.TestCase):
    def test_skill_metadata_and_shared_reference(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            skill = root / "skills/example"
            skill.mkdir(parents=True)
            (root / "guide.md").write_text("# Guide\n")
            path = skill / "SKILL.md"
            path.write_text(
                "---\nname: example\ndescription: Example skill\n---\n[Guide](../../guide.md)\n"
            )
            self.assertEqual(validate.validate_repository(root)["issues"], [])
            path.write_text(path.read_text().replace("name: example", "name: different"))
            self.assertTrue(
                any("name" in issue for issue in validate.validate_repository(root)["issues"])
            )
            (root / "guide.md").unlink()
            self.assertTrue(
                any(
                    "broken local link" in issue
                    for issue in validate.validate_repository(root)["issues"]
                )
            )

    def test_evaluation_pair_is_required(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            prompts = root / "evaluation/prompts"
            prompts.mkdir(parents=True)
            (prompts / "task.txt").write_text("Do the task\n")
            self.assertIn(
                "Missing evaluator rubric: task", validate.validate_repository(root)["issues"]
            )

    def test_unterminated_skill_frontmatter_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = root / "skills/example"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: example\ndescription: Example\n")
            self.assertTrue(
                any(
                    "unterminated" in issue
                    for issue in validate.validate_repository(root)["issues"]
                )
            )

    def test_runtime_source_copies_are_not_repository_documentation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            copied = root / ".runtime/src"
            copied.mkdir(parents=True)
            (copied / "README.md").write_text("[Missing](missing.md)\n")
            self.assertEqual(validate.validate_repository(root)["issues"], [])
            (root / "README.md").write_text("[Missing](missing.md)\n")
            self.assertEqual(len(validate.validate_repository(root)["issues"]), 1)


if __name__ == "__main__":
    unittest.main()
