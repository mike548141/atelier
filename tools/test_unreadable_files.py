"""An unreadable file is a broken scan, not a clean one (`160/730`, RT1).

`report.py` documents "an unreadable file" as an exit-2 line of the shared
contract. Five guards swallowed the error inside their per-file read and
printed `clean`; this pins all nine that read files to the contract, one
`chmod 000` fixture each. A file that VANISHES between the walk and the open is
a race and stays silent.

Skipped when the process can read a mode-000 file (running as root).
"""

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import report

TOOLS = Path(__file__).resolve().parent

# scanner -> (file name the scanner reads, readable content that is clean)
GUARDS = {
    "secretscan": ("notes.txt", "nothing here\n"),
    "leakscan": ("notes.txt", "nothing here\n"),
    "datescan": ("notes.md", "nothing here\n"),
    "spellscan": ("notes.md", "nothing here\n"),
    "wrapscan": ("notes.md", "nothing here\n"),
    "conflictscan": ("notes.txt", "nothing here\n"),
    "linkscan": ("notes.md", "nothing here\n"),
    "pathscan": ("notes.md", "nothing here\n"),
    "sizescan": ("ROADMAP.md", "nothing here\n"),
}


def _can_read_mode_000(tmp: Path) -> bool:
    probe = tmp / "probe"
    probe.write_text("x")
    probe.chmod(0)
    try:
        probe.read_text()
        return True
    except OSError:
        return False
    finally:
        probe.chmod(0o644)


class UnreadableFile(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        if _can_read_mode_000(self.tmp):
            self.skipTest("this process can read a mode-000 file")
        empty = self.tmp.parent / (self.tmp.name + "-terms.txt")
        empty.write_text("")
        self.addCleanup(empty.unlink)
        self.env = {**os.environ, "ATELIER_LEAKSCAN_TERMS": str(empty)}

    def run_guard(self, name, *extra):
        r = subprocess.run(
            [sys.executable, str(TOOLS / f"{name}.py"), "--root", str(self.tmp),
             *extra, str(self.tmp)],
            capture_output=True, text=True, env=self.env, cwd=self.tmp.parent)
        return r.returncode, r.stdout, r.stderr

    def test_every_guard_exits_two_on_an_unreadable_file(self):
        for name, (fname, text) in GUARDS.items():
            with self.subTest(name):
                f = self.tmp / fname
                f.write_text(text)
                rc, out, err = self.run_guard(name)
                self.assertEqual(0, rc, f"control (readable) {name}: {out}{err}")
                f.chmod(0)
                try:
                    rc, out, err = self.run_guard(name)
                finally:
                    f.chmod(0o644)
                self.assertEqual(2, rc, f"{name}: {out}{err}")
                self.assertIn("cannot read", err)
                self.assertNotIn("clean", out)
                f.unlink()

    def test_the_other_findings_are_not_the_only_signal(self):
        """An unreadable file next to a finding: still 2, never 1 or 0."""
        (self.tmp / "bad.txt").write_text("<" * 7 + " HEAD\n")
        (self.tmp / "locked.txt").write_text("x\n")
        (self.tmp / "locked.txt").chmod(0)
        try:
            rc, out, err = self.run_guard("conflictscan")
        finally:
            (self.tmp / "locked.txt").chmod(0o644)
        self.assertEqual(2, rc, out + err)


class VanishedFile(unittest.TestCase):
    """The race stays a silent skip: only ENOENT-class errors."""

    def test_the_vanished_classes(self):
        self.assertTrue(report.is_vanished(FileNotFoundError()))
        self.assertFalse(report.is_vanished(PermissionError()))

    def test_scan_file_skips_a_file_that_vanishes(self):
        import datescan
        import spellscan
        import wrapscan
        gone = self.tmp / "gone.md"
        for mod in (datescan, spellscan, wrapscan):
            with self.subTest(mod.__name__):
                self.assertEqual([], mod.scan_file(gone, "gone.md"))

    def test_scan_file_raises_on_a_permission_error(self):
        import datescan
        import spellscan
        import wrapscan
        for mod in (datescan, spellscan, wrapscan):
            with self.subTest(mod.__name__):
                with mock.patch.object(
                        mod, "_content_lines_from_file",
                        side_effect=PermissionError(13, "denied", "x.md")):
                    with self.assertRaises(PermissionError):
                        mod.scan_file(Path("x.md"), "x.md")

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)


if __name__ == "__main__":
    unittest.main()
