"""Regression tests for the repository validator (standard library only)."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate.py"
spec = importlib.util.spec_from_file_location("validate", SCRIPT)
validate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.write("skills/demo/SKILL.md", '---\nname: demo\ndescription: "Check a meaningful behavior."\n---\n\n# Demo\n')
        self.write("README.md", "**1 engineering skill**\n\n[demo](skills/demo/SKILL.md)\n")

    def write(self, path, content):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    def errors(self):
        return validate.validate_repository(self.root)

    def assertError(self, text):
        self.assertTrue(any(text in error for error in self.errors()), self.errors())

    def test_valid_repository(self):
        self.assertEqual([], self.errors())

    def test_missing_frontmatter(self):
        self.write("skills/demo/SKILL.md", "# Missing\n")
        self.assertError("frontmatter")

    def test_missing_description(self):
        self.write("skills/demo/SKILL.md", "---\nname: demo\n---\n# Demo\n")
        self.assertError("description")

    def test_duplicate_key(self):
        self.write("skills/demo/SKILL.md", '---\nname: demo\nname: demo\ndescription: "Valid"\n---\n# Demo\n')
        self.assertError("duplicate")

    def test_name_must_match_folder(self):
        self.write("skills/demo/SKILL.md", '---\nname: other\ndescription: "Valid"\n---\n# Demo\n')
        self.assertError("folder")

    def test_invalid_description_quoting(self):
        self.write("skills/demo/SKILL.md", '---\nname: demo\ndescription: "Unclosed\n---\n# Demo\n')
        self.assertError("description")

    def test_empty_body(self):
        self.write("skills/demo/SKILL.md", '---\nname: demo\ndescription: "Valid"\n---\n')
        self.assertError("body")

    def test_missing_entrypoint(self):
        (self.root / "skills" / "empty").mkdir()
        self.assertError("entrypoint")

    def test_count_drift(self):
        self.write("README.md", "**2 engineering skills**\n[demo](skills/demo/SKILL.md)\n")
        self.assertError("count")

    def test_missing_catalog_skill(self):
        self.write("README.md", "**1 engineering skill**\n")
        self.assertError("catalog")

    def test_broken_relative_link(self):
        self.write("docs/guide.md", "[missing](../missing.md)\n")
        self.assertError("missing.md")

    def test_existing_relative_link_and_anchor(self):
        self.write("docs/guide.md", "[demo](../skills/demo/SKILL.md#demo)\n")
        self.assertEqual([], self.errors())

    def test_missing_anchor(self):
        self.write("docs/guide.md", "[demo](../skills/demo/SKILL.md#absent)\n")
        self.assertError("anchor")

    def test_code_fences_are_not_links(self):
        fence = chr(96) * 3
        self.write("docs/guide.md", fence + "md\n[example](missing.md)\n" + fence + "\n")
        self.assertEqual([], self.errors())

    def test_external_links_are_not_network_checked(self):
        self.write("docs/guide.md", "[source](https://example.com/no-network-check)\n")
        self.assertEqual([], self.errors())

    def test_link_cannot_escape_repository(self):
        self.write("docs/guide.md", "[escape](../../outside.md)\n")
        self.assertError("escapes")

    def test_percent_encoded_local_link(self):
        self.write("docs/a file.md", "# Space\n")
        self.write("docs/guide.md", "[space](a%20file.md#space)\n")
        self.assertEqual([], self.errors())

    def test_symlink_skill_rejected(self):
        try:
            (self.root / "skills" / "linked").symlink_to(self.root / "skills" / "demo", target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable on this platform")
        self.assertError("symlink")

    def test_markdown_heading_duplicate_anchor(self):
        self.write("docs/guide.md", "# Same\n# Same\n[second](#same-1)\n")
        self.assertEqual([], self.errors())

    def test_version_drift_detected(self):
        self.write("VERSION", "0.1.0\n")
        self.write("CHANGELOG.md", "# Changelog\n## 0.1.0 - 2026-10-12\n")
        self.assertError("release version")

    def test_version_consistency(self):
        self.write("VERSION", "0.1.0\n")
        self.write("README.md", "**1 engineering skill**\nVersion: **0.1.0**\n[demo](skills/demo/SKILL.md)\n")
        self.write("CHANGELOG.md", "# Changelog\n## 0.1.0 - 2026-10-12\n")
        self.assertEqual([], self.errors())

    def test_unknown_evaluation_skill(self):
        case = {"id": "case", "prompt": "Task", "setup": "Fixture", "skills": ["missing"], "checks": ["Check"], "hard_fail": ["Failure"]}
        self.write("evals/scenarios.json", json.dumps([case]))
        self.assertError("unknown evaluation skill")

    def test_duplicate_evaluation_case(self):
        case = {"id": "case", "prompt": "Task", "setup": "Fixture", "skills": ["demo"], "checks": ["Check"], "hard_fail": ["Failure"]}
        self.write("evals/scenarios.json", json.dumps([case, case]))
        self.assertError("unique")

    def test_invalid_evaluation_json(self):
        self.write("evals/scenarios.json", "{")
        self.assertError("scenarios.json")

    def test_valid_evaluation_case(self):
        case = {"id": "case", "prompt": "Task", "setup": "Fixture", "skills": ["demo"], "checks": ["Check"], "hard_fail": ["Failure"]}
        self.write("evals/scenarios.json", json.dumps([case]))
        self.assertEqual([], self.errors())


if __name__ == "__main__":
    unittest.main()
