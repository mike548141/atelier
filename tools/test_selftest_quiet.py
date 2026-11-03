"""A scanner's `--selftest` prints its verdict and nothing in the floor's own
shape (roadmap 320/690).

A selftest runs the engine over deliberate fixtures, so the engine's honest
report about them is a list of findings. Printed, those lines sat in a CI log
beside the floor's real findings, with the same glyph and wording, and a red
run was diagnosed from them. Each scanner below is run as a real subprocess
(its own stdout and stderr, as CI sees them) and its passing output must be
exactly one verdict line.
"""

import re
import subprocess
import sys
import unittest
from pathlib import Path

import report

TOOLS_DIR = Path(__file__).resolve().parent

# The six the finding named, plus the two with the same mechanism and the same
# shared helper (sizescan's `⚠ sizescan: N file(s) flagged`, stampscan's
# `✗ stampscan: N drift finding(s)`).
SCANNERS = ("board", "datescan", "pathscan", "spellscan", "wrapscan",
            "conflictscan", "sizescan", "stampscan")

# What the floor prints for a finding or a broken scan, and what a usage error
# looks like. None of it may appear in a passing selftest.
FINDING_SHAPED = re.compile(
    r"✗|⚠|\bfinding\(s\)|commit blocked|\[[a-z-]+\] |:\d+ +\[|^usage:|error:")


def _selftest(name):
    return subprocess.run(
        [sys.executable, str(TOOLS_DIR / f"{name}.py"), "--selftest"],
        capture_output=True, text=True, timeout=300)


class SelftestIsQuiet(unittest.TestCase):
    pass


def _make(name):
    def test(self):
        r = _selftest(name)
        self.assertEqual(0, r.returncode, r.stdout + r.stderr)
        self.assertEqual("", r.stderr)
        lines = r.stdout.splitlines()
        self.assertEqual([f"selftest OK — {name}"], lines)
        for line in lines:
            self.assertIsNone(FINDING_SHAPED.search(line), line)
    return test


for _name in SCANNERS:
    setattr(SelftestIsQuiet, f"test_{_name}_selftest_prints_only_its_verdict",
            _make(_name))


class QuietSelftestHelper(unittest.TestCase):
    def _run(self, fn):
        import contextlib
        import io
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            try:
                rc = report.quiet_selftest("demo", fn)
            except RuntimeError as e:
                return "raised", out.getvalue(), e
        return rc, out.getvalue(), None

    def test_a_pass_prints_one_line_and_swallows_fixture_findings(self):
        import sys as _sys

        def body():
            print("✗ demo: 3 finding(s) — commit blocked.")
            print("  docs/broken.md:4  [opener] '<<<<<<< HEAD'")
            print("usage: demo [-h]", file=_sys.stderr)
            return 0
        rc, out, _ = self._run(body)
        self.assertEqual(0, rc)
        self.assertEqual("selftest OK — demo\n", out)

    def test_a_failure_prints_the_verdict_then_prefixed_evidence(self):
        def body():
            print("FAIL: got [] expected ['x']")
            return 1
        rc, out, _ = self._run(body)
        self.assertEqual(1, rc)
        self.assertEqual("selftest FAILED — demo\n"
                         "selftest (demo): FAIL: got [] expected ['x']\n", out)

    def test_an_exception_is_reported_then_reraised(self):
        def body():
            print("half way")
            raise RuntimeError("boom")
        rc, out, exc = self._run(body)
        self.assertEqual("raised", rc)
        self.assertIsInstance(exc, RuntimeError)
        self.assertIn("selftest FAILED — demo raised", out)
        self.assertIn("selftest (demo): half way", out)


if __name__ == "__main__":
    unittest.main()
