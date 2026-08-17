#!/usr/bin/env python3
"""Tests for coldsweep — the cold-sweep exclusion guard.

The corpus is the defect's own history: three recorded instances where an
exclusion silently did not apply because a path was compared as TEXT and the
prefix did not match. Every test below is that shape, or the boundary next to it
(a sibling directory that must NOT be swept up by the same bar).
"""

import shutil
import tempfile
import unittest
from pathlib import Path

import coldsweep


class TestPathBarring(unittest.TestCase):
    """is_barred() is the whole fix — it must not care how a path is spelled."""

    def test_every_spelling_of_a_barred_dir_bars_it(self):
        target = Path("docs/sessions/2026-08-17-x.md")
        for spelling in ("docs/sessions", "./docs/sessions", "docs/sessions/",
                         "docs//sessions", "./docs/sessions/"):
            with self.subTest(spelling=spelling):
                self.assertIsNotNone(coldsweep.is_barred(target, (spelling,)))

    def test_barred_file_matches_itself(self):
        self.assertEqual(
            coldsweep.is_barred(Path("docs/SESSIONS.md"), coldsweep.BARRED),
            "docs/SESSIONS.md")

    def test_sibling_directory_is_not_barred(self):
        # `docs/sessions-archive/` shares a text prefix with `docs/sessions`.
        # A string-prefix bar would swallow it; a parts bar must not.
        self.assertIsNone(
            coldsweep.is_barred(Path("docs/sessions-archive/x.md"),
                                ("docs/sessions",)))

    def test_sibling_file_is_not_barred(self):
        self.assertIsNone(
            coldsweep.is_barred(Path("docs/SESSIONS.md.bak"),
                                ("docs/SESSIONS.md",)))

    def test_nested_file_under_barred_dir_is_barred(self):
        self.assertIsNotNone(
            coldsweep.is_barred(Path("docs/reviews/withdrawn/old.md"),
                                coldsweep.BARRED))

    def test_unbarred_doctrine_path_is_free(self):
        self.assertIsNone(
            coldsweep.is_barred(Path("docs/method/REVIEW.md"),
                                coldsweep.BARRED))

    def test_empty_entry_is_ignored_not_a_wildcard(self):
        # A stray empty string in the barred set must bar NOTHING. Failing open
        # here would be bad; failing CLOSED (barring the tree) would be worse —
        # it would look like a clean sweep of nothing.
        self.assertIsNone(coldsweep.is_barred(Path("docs/method/X.md"), ("",)))


class TestSweep(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "docs" / "sessions").mkdir(parents=True)
        (self.tmp / "docs" / "reviews").mkdir(parents=True)
        (self.tmp / "docs" / "method").mkdir(parents=True)
        (self.tmp / "docs" / "SESSIONS.md").write_text("author account NEEDLE\n")
        (self.tmp / "docs" / "ROADMAP-DONE.md").write_text("harvest NEEDLE\n")
        (self.tmp / "docs" / "sessions" / "r.md").write_text("record NEEDLE\n")
        (self.tmp / "docs" / "reviews" / "v.md").write_text("verdict NEEDLE\n")
        (self.tmp / "docs" / "method" / "D.md").write_text("doctrine NEEDLE\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_default_sweep_reaches_only_unbarred_files(self):
        kept, skipped = coldsweep.walk(self.tmp, coldsweep.BARRED)
        hits = coldsweep.search(self.tmp, "NEEDLE", kept, False)
        self.assertEqual([str(r) for r, _, _ in hits], ["docs/method/D.md"])
        self.assertEqual(len(skipped), 4)

    def test_include_barred_reaches_everything(self):
        kept, _ = coldsweep.walk(self.tmp, ())
        hits = coldsweep.search(self.tmp, "NEEDLE", kept, False)
        self.assertEqual(len(hits), 5)

    def test_also_exclude_bars_an_extra_path(self):
        barred = coldsweep.BARRED + ("docs/method",)
        kept, _ = coldsweep.walk(self.tmp, barred)
        self.assertEqual(coldsweep.search(self.tmp, "NEEDLE", kept, False), [])

    def test_case_insensitive_flag(self):
        kept, _ = coldsweep.walk(self.tmp, coldsweep.BARRED)
        self.assertEqual(coldsweep.search(self.tmp, "needle", kept, False), [])
        self.assertEqual(len(coldsweep.search(self.tmp, "needle", kept, True)), 1)

    def test_binary_files_are_skipped_not_decoded(self):
        (self.tmp / "docs" / "blob.bin").write_bytes(b"NEEDLE\x00NEEDLE")
        kept, _ = coldsweep.walk(self.tmp, coldsweep.BARRED)
        hits = coldsweep.search(self.tmp, "NEEDLE", kept, False)
        self.assertEqual([str(r) for r, _, _ in hits], ["docs/method/D.md"])

    def test_git_dir_is_never_searched(self):
        (self.tmp / ".git").mkdir()
        (self.tmp / ".git" / "COMMIT_EDITMSG").write_text("NEEDLE\n")
        kept, _ = coldsweep.walk(self.tmp, coldsweep.BARRED)
        self.assertNotIn(".git", {r.parts[0] for r in kept})


class TestExitCodes(unittest.TestCase):
    """grep's contract: 0 matched, 1 no match, 2 the search itself failed."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "docs").mkdir()
        (self.tmp / "docs" / "a.md").write_text("FINDME\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_match_exits_zero(self):
        self.assertEqual(coldsweep.main(["--root", str(self.tmp), "FINDME"]), 0)

    def test_no_match_exits_one(self):
        self.assertEqual(coldsweep.main(["--root", str(self.tmp), "NOPE"]), 1)

    def test_bad_pattern_exits_two(self):
        self.assertEqual(coldsweep.main(["--root", str(self.tmp), "("]), 2)

    def test_missing_pattern_exits_two(self):
        self.assertEqual(coldsweep.main(["--root", str(self.tmp)]), 2)

    def test_missing_root_exits_two(self):
        self.assertEqual(
            coldsweep.main(["--root", str(self.tmp / "nope"), "X"]), 2)

    def test_list_barred_exits_zero_without_a_pattern(self):
        self.assertEqual(
            coldsweep.main(["--root", str(self.tmp), "--list-barred"]), 0)

    def test_selftest_passes(self):
        self.assertEqual(coldsweep.selftest(), 0)


if __name__ == "__main__":
    unittest.main()
