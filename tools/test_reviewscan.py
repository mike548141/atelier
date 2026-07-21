"""Tests for reviewscan — the decision-record review-line lint.

The tool's job: a post-boundary decision record without a review line is a
finding; frozen (pre-boundary) and retired-scheme records are never touched.
The tests bite-prove both legs and the boundary edges.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import reviewscan

TOOLS = Path(__file__).resolve().parent


def make_tree(td: Path) -> Path:
    d = td / "docs" / "decisions"
    d.mkdir(parents=True)
    return d


class ScopeTest(unittest.TestCase):
    def test_post_boundary_dated_records_are_in_scope(self):
        with tempfile.TemporaryDirectory() as s:
            d = make_tree(Path(s))
            (d / "2026-07-22-1200-a.md").write_text("x")
            (d / "2026-08-01-b.md").write_text("x")  # no HHMM — still a record
            names = [r.name for r in reviewscan.find_records([Path(s)])]
            self.assertEqual(names, ["2026-07-22-1200-a.md", "2026-08-01-b.md"])

    def test_pre_boundary_and_retired_scheme_and_readme_are_skipped(self):
        with tempfile.TemporaryDirectory() as s:
            d = make_tree(Path(s))
            (d / "2026-07-20-2359-frozen.md").write_text("x")
            (d / "0007-ssh-commit-signing.md").write_text("x")
            (d / "README.md").write_text("x")
            (d / "template.md").write_text("x")
            self.assertEqual(reviewscan.find_records([Path(s)]), [])

    def test_boundary_day_itself_is_in_scope(self):
        with tempfile.TemporaryDirectory() as s:
            d = make_tree(Path(s))
            (d / f"{reviewscan.BOUNDARY}-0001-first.md").write_text("x")
            self.assertEqual(len(reviewscan.find_records([Path(s)])), 1)

    def test_templates_tree_is_skipped(self):
        with tempfile.TemporaryDirectory() as s:
            t = Path(s) / "build" / "templates" / "docs" / "decisions"
            t.mkdir(parents=True)
            (t / "2026-07-22-1200-example.md").write_text("x")
            self.assertEqual(reviewscan.find_records([Path(s)]), [])

    def test_decisions_dir_passed_directly_is_scanned(self):
        # RS1: the natural hand-run — the decisions dir itself as the path
        # arg must scan its records, never silently match nothing and green.
        with tempfile.TemporaryDirectory() as s:
            d = make_tree(Path(s))
            (d / "2026-07-22-1200-a.md").write_text("x")
            self.assertEqual(len(reviewscan.find_records([d])), 1)

    def test_record_file_passed_directly_is_scanned(self):
        # RS1, second leg: a single record file as the path arg.
        with tempfile.TemporaryDirectory() as s:
            d = make_tree(Path(s))
            f = d / "2026-07-22-1200-a.md"
            f.write_text("x")
            self.assertEqual(reviewscan.find_records([f]), [f])
            # A pre-boundary file named directly stays out of scope (frozen).
            g = d / "2026-07-19-1200-frozen.md"
            g.write_text("x")
            self.assertEqual(reviewscan.find_records([g]), [])

    def test_overlapping_bases_do_not_duplicate(self):
        with tempfile.TemporaryDirectory() as s:
            d = make_tree(Path(s))
            (d / "2026-07-22-1200-a.md").write_text("x")
            self.assertEqual(len(reviewscan.find_records([Path(s), d])), 1)


class LineTest(unittest.TestCase):
    def check(self, body: str) -> bool:
        with tempfile.TemporaryDirectory() as s:
            f = Path(s) / "r.md"
            f.write_text(body)
            return reviewscan.scan_record(f)

    def test_typographies_that_count(self):
        for line in ("**Review**: queued — docs/reviews/x.md",
                     "review: not warranted — records-only edit",
                     "- Review: queued",
                     "> **review**: not warranted — trivial",
                     "REVIEW: queued — docs/reviews/x.md"):  # RS4: caps count
            self.assertTrue(self.check(f"# t\n{line}\n"), line)

    def test_absence_and_lookalikes_fail(self):
        for body in ("# t\nno field at all\n",
                     "# t\nthe review of this work was thorough\n",
                     "# t\nPreview: something\n"):
            self.assertFalse(self.check(body), body)

    def test_empty_value_fails(self):
        # RS3: the field with nothing after the colon is a blank in the
        # field's clothes — presence means presence of a JUDGEMENT.
        for body in ("# t\n**Review**:\n", "# t\nreview:   \n"):
            self.assertFalse(self.check(body), body)

    def test_fenced_review_does_not_count(self):
        # RS2: a record QUOTING the convention in a code fence has not
        # stated its own judgement.
        self.assertFalse(self.check(
            "# t\n```\nreview: not warranted — a quoted example\n```\n"))
        # …but a real field outside the fence still counts.
        self.assertTrue(self.check(
            "# t\n```\nreview: quoted\n```\n**Review**: not warranted — t\n"))

    def test_allow_marker_exempts(self):
        self.assertTrue(self.check(
            "# t\n<!-- reviewscan:allow: a stated exception -->\n"))


class ExitCodeTest(unittest.TestCase):
    def run_tool(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS / "reviewscan.py"), *args],
            capture_output=True, text=True)

    def test_red_green_and_usage(self):
        with tempfile.TemporaryDirectory() as s:
            d = make_tree(Path(s))
            bad = d / "2026-07-22-1200-bad.md"
            bad.write_text("# no line\n")
            r = self.run_tool("--root", s, s)
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertIn("2026-07-22-1200-bad.md", r.stdout)
            bad.write_text("# ok\n**Review**: not warranted — test\n")
            r = self.run_tool("--root", s, s)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        r = self.run_tool("--root", "/nonexistent-reviewscan-test")
        self.assertEqual(r.returncode, 2)

    def test_selftest_passes(self):
        r = self.run_tool("--selftest")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
