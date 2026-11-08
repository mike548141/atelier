"""A relative target that climbs out of `--root` is refused (`160/730`, RT7).

`resolve_targets` promised "never the caller's cwd"; nothing promised "never
outside the root", so `scanner --root R ../elsewhere` scanned another tree under
R's ignore file and anchors, in silence. One CLI check per guard that takes
positional paths, plus the controls that must still work.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent

GUARDS = ("secretscan", "leakscan", "conflictscan", "datescan", "spellscan",
          "wrapscan", "linkscan", "pathscan", "sizescan", "indexscan")


class EscapingTargets(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.base, True)
        self.root = self.base / "repo"
        (self.root / "docs").mkdir(parents=True)
        (self.root / "docs" / "a.md").write_text("nothing here\n")
        (self.base / "elsewhere").mkdir()
        (self.base / "elsewhere" / "b.md").write_text("nothing here\n")
        empty = self.base / "terms.txt"
        empty.write_text("")
        self.env = {**os.environ, "ATELIER_LEAKSCAN_TERMS": str(empty)}

    def run_guard(self, name, *paths):
        r = subprocess.run(
            [sys.executable, str(TOOLS / f"{name}.py"), "--root", str(self.root),
             *paths], capture_output=True, text=True, env=self.env, cwd=self.base)
        return r.returncode, r.stdout, r.stderr

    def test_every_guard_refuses_a_target_climbing_out_of_root(self):
        for name in GUARDS:
            for path in ("../elsewhere", "docs/../../elsewhere"):
                with self.subTest(guard=name, path=path):
                    rc, out, err = self.run_guard(name, path)
                    self.assertEqual(2, rc, out + err)
                    self.assertIn("climb out of --root", err)
                    self.assertNotIn("clean", out)

    def test_a_target_inside_root_still_scans(self):
        for name in GUARDS:
            for path in ("docs", "./docs", "docs/../docs"):
                with self.subTest(guard=name, path=path):
                    rc, out, err = self.run_guard(name, path)
                    self.assertNotEqual(2, rc, out + err)

    def test_an_absolute_target_is_the_callers_explicit_choice(self):
        for name in ("secretscan", "conflictscan", "datescan"):
            with self.subTest(guard=name):
                rc, out, err = self.run_guard(name, str(self.base / "elsewhere"))
                self.assertNotEqual(2, rc, out + err)


if __name__ == "__main__":
    unittest.main()
