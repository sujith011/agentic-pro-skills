"""Exercise installer effects only inside temporary directories."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "install_skills.py"
spec = importlib.util.spec_from_file_location("install_skills", SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "source"
        self.destination = self.root / "destination"
        self.make_skill("first", "First")
        self.make_skill("second", "Second")

    def make_skill(self, name, content):
        folder = self.source / name
        folder.mkdir(parents=True)
        (folder / "SKILL.md").write_text(content, encoding="utf-8")

    def test_dry_run_creates_nothing(self):
        installer.install(self.source, self.destination, ["first"], apply=False)
        self.assertFalse(self.destination.exists())

    def test_apply_copies_only_selected_skill(self):
        installer.install(self.source, self.destination, ["first"], apply=True)
        self.assertEqual("First", (self.destination / "first/SKILL.md").read_text())
        self.assertFalse((self.destination / "second").exists())

    def test_repeat_install_skips_identical_files(self):
        installer.install(self.source, self.destination, ["first"], apply=True)
        installer.install(self.source, self.destination, ["first"], apply=True)
        self.assertEqual("First", (self.destination / "first/SKILL.md").read_text())

    def test_collision_aborts_before_other_copies(self):
        installer.install(self.source, self.destination, ["second"], apply=True)
        (self.destination / "second/SKILL.md").write_text("User content")
        with self.assertRaises(ValueError):
            installer.install(self.source, self.destination, ["first", "second"], apply=True)
        self.assertFalse((self.destination / "first").exists())
        self.assertEqual("User content", (self.destination / "second/SKILL.md").read_text())

    def test_unknown_skill_creates_nothing(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.destination, ["missing"], apply=True)
        self.assertFalse(self.destination.exists())

    def test_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.destination, ["../escape"], apply=True)
        self.assertFalse(self.destination.exists())

    def test_destination_inside_source_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.source / "first" / "nested", ["first"], apply=True)

    def test_extra_existing_resource_counts_as_collision(self):
        installer.install(self.source, self.destination, ["first"], apply=True)
        (self.destination / "first/custom.txt").write_text("Keep me")
        with self.assertRaises(ValueError):
            installer.install(self.source, self.destination, ["first"], apply=True)
        self.assertTrue((self.destination / "first/custom.txt").exists())


if __name__ == "__main__":
    unittest.main()
