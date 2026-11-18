"""Tests for instruments/atelier-menu/menu.py (board 450/010 row 14)."""
import os
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
        # The menu is built from the tree, so every skill and command the
        # plugin ships must appear: the property that makes it never stale.
        out = self.run_menu("--root", ROOT).stdout
        names = [d for d in os.listdir(os.path.join(ROOT, "skills"))
                 if os.path.isfile(os.path.join(ROOT, "skills", d, "SKILL.md"))]
        names += [f[:-3] for f in os.listdir(os.path.join(ROOT, "commands")) if f.endswith(".md")]
        self.assertTrue(names)
        for n in names:
            self.assertIn(f"`/atelier:{n}`", out)

    def test_skill_is_named_atelier(self):
        with open(os.path.join(HERE, "atelier-menu", "SKILL.md"), encoding="utf-8") as f:
            head = f.read().split("\n---", 1)[0]
        self.assertIn("\nname: atelier\n", head + "\n")


if __name__ == "__main__":
    unittest.main()
