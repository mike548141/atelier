"""Tests for instruments/atelier-menu/menu.py (board 450/010 row 14)."""
import os
import re
import subprocess
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
MENU = os.path.join(HERE, "atelier-menu", "menu.py")
ROOT = os.path.dirname(HERE)


class Menu(unittest.TestCase):
    def run_menu(self, *args):
        return subprocess.run([sys.executable, MENU, *args], capture_output=True, text=True, timeout=30)

    def test_selftest(self):
        r = self.run_menu("--selftest")
        self.assertEqual(r.returncode, 0, r.stderr)

    def test_lists_every_plugin_command(self):
        # The menu is built from the tree, so every subject's every action
        # must appear: the property that makes it never stale (450/020).
        out = self.run_menu("--root", ROOT).stdout
        skills = os.path.join(ROOT, "skills")
        names = []
        for d in os.listdir(skills):
            if not os.path.isfile(os.path.join(skills, d, "SKILL.md")):
                continue
            for f in os.listdir(os.path.join(skills, d)):
                if f.endswith(".md") and f != "SKILL.md":
                    with open(os.path.join(skills, d, f), encoding="utf-8") as fh:
                        m = re.search(r"^action:\s*(\S+)", fh.read().split("\n---", 1)[0], re.M)
                    if m:
                        names.append(f"{d} {m.group(1)}")
        self.assertGreaterEqual(len(names), 15)
        for n in names:
            self.assertIn(f"`/atelier:{n}`", out)

    def test_a_subject_shows_only_its_own_actions(self):
        out = self.run_menu("--root", ROOT, "review").stdout
        for a in ("plan", "run", "brief"):
            self.assertIn(f"`/atelier:review {a}`", out)
        self.assertNotIn("/atelier:work ", out)
        self.assertIn("on its own only shows this menu", out)

    def test_skill_is_named_atelier(self):
        with open(os.path.join(HERE, "atelier-menu", "SKILL.md"), encoding="utf-8") as f:
            head = f.read().split("\n---", 1)[0]
        self.assertIn("\nname: atelier\n", head + "\n")


if __name__ == "__main__":
    unittest.main()
