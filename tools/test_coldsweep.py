#!/usr/bin/env python3
"""Tests for coldsweep — the cold-sweep exclusion guard.

The corpus is the defect's own history: three recorded instances where an
exclusion silently did not apply because a path was compared as TEXT and the
prefix did not match. Every test below is that shape, or the boundary next to it
(a sibling directory that must NOT be swept up by the same bar).
"""

import contextlib
import io
import os
import shutil
import stat as statmod
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

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


class CommitFixture(unittest.TestCase):
    """`--commit` prints subject, stat and diff — and never the message body.

    The defect: a cold brief bars the landing commit's body, but `git show`
    prints it, so reviewers leaked it by the obvious command. Every test builds
    a throwaway repo with a body carrying a distinctive string.
    """

    BODY = "BODYMARKER-the-authors-account-of-why"

    def git(self, *args, env_extra=None):
        who = "t" + chr(64) + "fixture.invalid"   # built, not a literal address
        env = {"GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": who,
               "GIT_COMMITTER_NAME": "T", "GIT_COMMITTER_EMAIL": who,
               "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin",
               "HOME": str(self.tmp), "GIT_CONFIG_NOSYSTEM": "1"}
        env.update(env_extra or {})
        out = subprocess.run(["git", "-C", str(self.tmp), *args], env=env,
                             capture_output=True, text=True, check=True)
        return out.stdout.strip()

    def commit(self, subject, body=None):
        msg = [subject] + ([body] if body else [])
        args = ["commit", "-q"]
        for m in msg:
            args += ["-m", m]
        self.git(*args)
        return self.git("rev-parse", "HEAD")

    def run_cmd(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = coldsweep.main(["--root", str(self.tmp), *argv])
        return code, out.getvalue(), err.getvalue()

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.git("init", "-q")
        (self.tmp / "docs").mkdir()
        (self.tmp / "src").mkdir()
        (self.tmp / "src" / "a.py").write_text("print('one')\n")
        (self.tmp / "docs" / "SESSIONS.md").write_text("log\n")
        self.git("add", "src/a.py", "docs/SESSIONS.md")
        self.root_sha = self.commit("root: first commit", self.BODY + "-root")
        (self.tmp / "src" / "a.py").write_text("print('two')\n")
        (self.tmp / "src" / "b.py").write_text("print('bee')\n")
        (self.tmp / "docs" / "SESSIONS.md").write_text("log\nSESSIONTEXT\n")
        self.git("add", "src/a.py", "src/b.py", "docs/SESSIONS.md")
        self.sha = self.commit("area: change things", self.BODY)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)



class TestCommitView(CommitFixture):
    """The `--commit` view: the original contract."""

    def test_plain_git_show_would_leak_the_body(self):
        # The control: the fixture's body really is what `git show` prints, so
        # the absence assertions below are not vacuous.
        self.assertIn(self.BODY, self.git("show", "--stat", self.sha))
        self.assertIn(self.BODY, self.git("show", self.sha, "--", "src"))

    def test_body_never_appears(self):
        for argv in (("--commit", self.sha), ("--commit", "HEAD"),
                     ("--commit", self.sha[:7]),
                     ("--commit", self.sha, "--include-barred"),
                     ("--commit", self.sha, "--path", "src")):
            with self.subTest(argv=argv):
                code, out, err = self.run_cmd(*argv)
                self.assertEqual(code, 0)
                self.assertNotIn(self.BODY, out + err)

    def test_subject_stat_and_diff_are_present(self):
        code, out, _ = self.run_cmd("--commit", self.sha)
        self.assertEqual(code, 0)
        # The subject, not the abbreviated hash: a global core.abbrev on the
        # machine running the test changes the hash's length (160/930 BF7).
        self.assertIn(" area: change things", out.splitlines()[0])
        self.assertIn("src/a.py", out)       # stat and diff headers
        self.assertIn("2 files changed", out)
        self.assertIn("+print('two')", out)
        self.assertIn("-print('one')", out)

    def test_barred_paths_are_left_out_and_named(self):
        _, out, _ = self.run_cmd("--commit", self.sha)
        self.assertNotIn("SESSIONTEXT", out)
        self.assertIn("1 file(s) left out as rule-2 barred", out)
        self.assertIn("docs/SESSIONS.md", out.splitlines()[-1])

    def test_include_barred_restores_them_with_a_banner(self):
        _, out, _ = self.run_cmd("--commit", self.sha, "--include-barred")
        self.assertIn("+SESSIONTEXT", out)
        self.assertIn("--include-barred", out)

    def test_also_exclude_applies_to_the_diff(self):
        _, out, _ = self.run_cmd("--commit", self.sha, "--also-exclude",
                                 "./src/b.py")
        self.assertNotIn("bee", out)
        self.assertIn("+print('two')", out)

    def test_path_scoping(self):
        code, out, _ = self.run_cmd("--commit", self.sha, "--path", "src/b.py")
        self.assertEqual(code, 0)
        self.assertIn("+print('bee')", out)
        self.assertNotIn("print('two')", out)
        self.assertIn("1 file changed", out)

    def test_path_with_no_changes_says_so_and_exits_one(self):
        # BF3: a typo'd --path used to print the proof line and exit 0, which a
        # brief's own re-run criterion ("exit 0, closing line present") read as
        # a clean read of nothing.
        code, out, err = self.run_cmd("--commit", self.sha, "--path", "nope")
        self.assertEqual(code, 1)
        self.assertIn("(no changes in scope)", out)
        self.assertIn("--path nope matched no changed file", err)
        self.assertIn("nothing in scope", err)

    def test_one_bad_path_among_good_ones_is_named_not_fatal(self):
        code, out, err = self.run_cmd("--commit", self.sha, "--path",
                                      "src/b.py", "--path", "src/typo.py")
        self.assertEqual(code, 0)
        self.assertIn("+print('bee')", out)
        self.assertIn("--path src/typo.py matched no changed file", err)
        self.assertNotIn("--path src/b.py matched", err)

    def test_a_barred_path_named_with_path_is_not_a_way_in(self):
        code, out, err = self.run_cmd("--commit", self.sha, "--path",
                                      "docs/SESSIONS.md")
        self.assertEqual(code, 1)
        self.assertNotIn("SESSIONTEXT", out)
        self.assertIn("--path docs/SESSIONS.md matched no changed file", err)

    def test_root_commit_diffs_against_the_empty_tree(self):
        code, out, err = self.run_cmd("--commit", self.root_sha)
        self.assertEqual(code, 0, err)
        self.assertIn("root: first commit", out)
        self.assertIn("+print('one')", out)
        self.assertIn("root commit", out)
        self.assertNotIn(self.BODY, out)

    def test_merge_commit_diffs_against_first_parent(self):
        self.git("checkout", "-q", "-b", "side", self.root_sha)
        (self.tmp / "src" / "c.py").write_text("print('sea')\n")
        self.git("add", "src/c.py")
        self.commit("side: add c", self.BODY + "-side")
        self.git("checkout", "-q", "-")
        self.git("merge", "-q", "--no-ff", "side", "-m", "merge: side",
                 "-m", self.BODY + "-merge")
        code, out, _ = self.run_cmd("--commit", "HEAD")
        self.assertEqual(code, 0)
        self.assertIn("merge: side", out)
        self.assertIn("+print('sea')", out)       # what the merge brought in
        self.assertNotIn("print('bee')", out)     # already on the first parent
        self.assertNotIn(self.BODY, out)

    def test_unknown_sha_exits_two_with_a_clear_error(self):
        code, out, err = self.run_cmd("--commit", "deadbeef0000")
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("not a commit in this repository", err)

    def test_not_a_repository_exits_two(self):
        plain = Path(tempfile.mkdtemp())
        try:
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                code = coldsweep.main(["--root", str(plain), "--commit", "HEAD"])
            self.assertEqual(code, 2)
            self.assertIn("git repository", err.getvalue())
        finally:
            shutil.rmtree(plain, ignore_errors=True)

    def test_a_pattern_with_commit_is_a_usage_error(self):
        self.assertEqual(self.run_cmd("--commit", self.sha, "PAT")[0], 2)

    def test_path_without_commit_is_a_usage_error(self):
        self.assertEqual(self.run_cmd("--path", "src", "PAT")[0], 2)


class TestCommitViewGuards(CommitFixture):
    """The same fixture, for the findings of the 160/930 cold pass."""

    def board_commit(self):
        """A landing commit that, like a rule-4 one, also edits the board."""
        item = self.tmp / "docs" / "roadmap" / "160-owed"
        item.mkdir(parents=True)
        (item / "910-pointer.md").write_text("AUTHORACCOUNT the pointer\n")
        (self.tmp / "docs" / "ROADMAP.md").write_text("INDEXLINE\n")
        (self.tmp / "src" / "a.py").write_text("print('three')\n")
        self.git("add", "docs/roadmap/160-owed/910-pointer.md",
                 "docs/ROADMAP.md", "src/a.py")
        return self.commit("area: land it", self.BODY + "-board")

    # BF1 -- the safe view by default when a commit touches the board
    def test_board_store_is_left_out_by_default_and_named(self):
        sha = self.board_commit()
        code, out, _ = self.run_cmd("--commit", sha)
        self.assertEqual(code, 0)
        self.assertNotIn("AUTHORACCOUNT", out)
        self.assertNotIn("INDEXLINE", out)
        self.assertIn("+print('three')", out)           # the code delta stays
        self.assertIn("2 board-store file(s) left out by default", out)
        self.assertIn("docs/roadmap/160-owed/910-pointer.md", out)

    def test_naming_a_board_file_shows_it_and_says_so(self):
        sha = self.board_commit()
        code, out, _ = self.run_cmd(
            "--commit", sha, "--path", "docs/roadmap/160-owed/910-pointer.md")
        self.assertEqual(code, 0)
        self.assertIn("+AUTHORACCOUNT the pointer", out)
        self.assertIn("1 board-store file(s) SHOWN", out)

    def test_include_barred_lifts_the_board_default_with_the_banner(self):
        sha = self.board_commit()
        _, out, _ = self.run_cmd("--commit", sha, "--include-barred")
        self.assertIn("+AUTHORACCOUNT the pointer", out)
        self.assertIn("nor the board store", out)

    def test_a_commit_that_touches_no_board_prints_a_stable_zero_line(self):
        _, out, _ = self.run_cmd("--commit", self.sha)
        self.assertIn("0 board-store file(s) left out or shown: none touched",
                      out)

    # BF2 -- only the first LINE of the message is ever printed
    def test_a_message_with_no_blank_line_after_its_subject_prints_one_line(self):
        (self.tmp / "src" / "d.py").write_text("print('dee')\n")
        self.git("add", "src/d.py")
        self.git("commit", "-q", "-m",
                 "area: glued\n" + self.BODY + "-glued\nmore body")
        for argv in (("--commit", "HEAD"), ("--commit", "HEAD", "--path",
                                            "src")):
            with self.subTest(argv=argv):
                _, out, err = self.run_cmd(*argv)
                self.assertIn("area: glued", out.splitlines()[0])
                self.assertNotIn(self.BODY, out + err)
                self.assertNotIn("more body", out + err)

    def test_a_crlf_message_prints_a_clean_first_line(self):
        (self.tmp / "src" / "e.py").write_text("print('eee')\n")
        self.git("add", "src/e.py")
        msg = self.tmp / "crlf.txt"
        msg.write_bytes(("area: crlf\r\n\r\n" + self.BODY +
                         "-crlf\r\n").encode())
        self.git("commit", "-q", "-F", str(msg), "--cleanup=verbatim")
        _, out, err = self.run_cmd("--commit", "HEAD")
        self.assertTrue(out.splitlines()[0].endswith("area: crlf"))
        self.assertNotIn("\r", out.splitlines()[0])
        self.assertNotIn(self.BODY, out + err)

    # BF4 -- an absolute --also-exclude is applied, or refused; never reported
    # as applied while doing nothing
    def test_an_absolute_also_exclude_is_applied_in_both_modes(self):
        absolute = str((self.tmp / "src" / "b.py").resolve())
        _, out, _ = self.run_cmd("--commit", self.sha, "--also-exclude",
                                 absolute)
        self.assertNotIn("bee", out)
        self.assertIn("+print('two')", out)
        (self.tmp / "docs" / "method").mkdir()
        (self.tmp / "docs" / "method" / "D.md").write_text("NEEDLE\n")
        absolute = str((self.tmp / "docs" / "method").resolve())
        code, out, err = self.run_cmd("--also-exclude", absolute, "NEEDLE")
        self.assertEqual(code, 1)           # excluded, so nothing matched
        self.assertEqual(err, "")
        self.assertNotIn("D.md:", out)

    def test_an_also_exclude_outside_the_root_exits_two(self):
        outside = tempfile.mkdtemp()
        try:
            for entry in (outside, "../elsewhere"):
                with self.subTest(entry=entry):
                    code, _, err = self.run_cmd("--commit", self.sha,
                                                "--also-exclude", entry)
                    self.assertEqual(code, 2)
                    self.assertIn("lies outside --root", err)
        finally:
            shutil.rmtree(outside, ignore_errors=True)

    # BF9 -- one meaning for --root
    def test_a_root_below_the_repository_top_is_refused(self):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = coldsweep.main(["--root", str(self.tmp / "src"),
                                   "--commit", self.sha])
        self.assertEqual(code, 2)
        self.assertIn("must be the repository's top", err.getvalue())
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            self.assertEqual(
                coldsweep.main(["--root", str(self.tmp / "docs"), "log"]), 2)

    # BF10 -- a shallow clone's boundary commit is not a root commit
    def test_a_shallow_boundary_commit_is_refused(self):
        clone = Path(tempfile.mkdtemp())
        try:
            subprocess.run(["git", "clone", "-q", "--depth", "1",
                            "file://" + str(self.tmp), str(clone / "c")],
                           check=True, capture_output=True)
            out, err = io.StringIO(), io.StringIO()
            with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
                code = coldsweep.main(["--root", str(clone / "c"),
                                       "--commit", "HEAD"])
            self.assertEqual(code, 2)
            self.assertIn("shallow clone", err.getvalue())
            self.assertNotIn("print('two')", out.getvalue())
        finally:
            shutil.rmtree(clone, ignore_errors=True)

    # BF6 -- the guards that had no test
    def test_the_barred_bar_is_anchored_at_the_repo_top(self):
        # Called from below the top (main refuses that now, but the guard is
        # kept for any caller): `top` is what stops the exclusion being
        # measured from the subdirectory and barring nothing.
        self.assertIn(":(top,exclude)docs/SESSIONS.md",
                      coldsweep._pathspec([], coldsweep.BARRED))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            code = coldsweep.show_commit(self.tmp / "src", self.sha, [],
                                         coldsweep.BARRED)
        self.assertEqual(code, 0)
        self.assertNotIn("SESSIONTEXT", buf.getvalue())

    def test_an_external_diff_driver_is_never_run(self):
        marker = self.tmp / "ext-ran"
        script = self.tmp / "extdiff.sh"
        script.write_text("#!/bin/sh\necho EXTDIFFLEAK; touch '%s'\n" % marker)
        script.chmod(script.stat().st_mode | statmod.S_IXUSR)
        self.git("config", "diff.external", str(script))
        code, out, err = self.run_cmd("--commit", self.sha)
        self.assertEqual(code, 0, err)
        self.assertNotIn("EXTDIFFLEAK", out)
        self.assertFalse(marker.exists())

    def test_a_textconv_filter_is_never_run(self):
        (self.tmp / ".gitattributes").write_text("*.py diff=leaky\n")
        self.git("config", "diff.leaky.textconv", "echo TEXTCONVLEAK #")
        code, out, err = self.run_cmd("--commit", self.sha)
        self.assertEqual(code, 0, err)
        self.assertNotIn("TEXTCONVLEAK", out)
        self.assertIn("+print('two')", out)

    def test_colour_config_does_not_put_escapes_in_the_output(self):
        self.git("config", "color.ui", "always")
        self.git("config", "color.diff", "always")
        _, out, _ = self.run_cmd("--commit", self.sha)
        self.assertNotIn("\x1b[", out)

    def test_a_notes_ref_never_reaches_the_output(self):
        self.git("notes", "add", "-m", "NOTELEAK", self.sha)
        self.git("config", "notes.displayRef", "refs/notes/commits")
        _, out, err = self.run_cmd("--commit", self.sha)
        self.assertNotIn("NOTELEAK", out + err)

    def test_a_rev_spelled_like_an_option_is_a_rev_not_a_flag(self):
        for rev in ("--all", "-h", "--output=" + str(self.tmp / "o.txt")):
            with self.subTest(rev=rev):
                # `=` form: argparse would take a bare "--all" for a flag.
                code, out, err = self.run_cmd("--commit=" + rev)
                self.assertEqual(code, 2)
                self.assertEqual(out, "")
                self.assertIn("not a commit", err)
        self.assertFalse((self.tmp / "o.txt").exists())

    def test_a_failed_git_diff_is_an_error_never_a_clean_read(self):
        real = coldsweep._git

        def failing(root, *args):
            if args and args[0] == "diff":
                return subprocess.CompletedProcess(
                    args, 128, stdout="", stderr="fatal: simulated failure")
            return real(root, *args)

        out, err = io.StringIO(), io.StringIO()
        with mock.patch.object(coldsweep, "_git", side_effect=failing), \
                contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = coldsweep.show_commit(self.tmp, self.sha, [],
                                         coldsweep.BARRED)
        self.assertEqual(code, 2)
        self.assertIn("git failed", err.getvalue())
        self.assertNotIn("message body not printed", out.getvalue())
        self.assertNotIn("(no changes in scope)", out.getvalue())


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


class TestEmptyAlsoExclude(unittest.TestCase):
    """160/450 DK9: an --also-exclude that matches nothing bars nothing, and
    a brief once named a path that never existed. The sweep warns on stderr,
    still runs, and keeps its exit code."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        (self.tmp / "docs").mkdir()
        (self.tmp / "docs" / "a.md").write_text("FINDME\n")
        (self.tmp / "docs" / "b.md").write_text("FINDME\n")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = coldsweep.main(["--root", str(self.tmp), *argv])
        return code, out.getvalue(), err.getvalue()

    def test_a_path_that_matches_nothing_is_warned_about(self):
        code, _, err = self._run("--also-exclude", "docs/typo-dir", "FINDME")
        self.assertEqual(code, 0)          # the sweep ran; exit unchanged
        self.assertIn("--also-exclude docs/typo-dir matches no file", err)

    def test_a_path_that_matches_is_silent_in_any_spelling(self):
        for spelling in ("docs/a.md", "./docs/a.md", "docs//a.md"):
            with self.subTest(spelling=spelling):
                code, out, err = self._run("--also-exclude", spelling,
                                           "FINDME")
                self.assertEqual(err, "")
                self.assertNotIn("docs/a.md:", out)

    def test_include_barred_has_no_bar_to_warn_about(self):
        _, _, err = self._run("--include-barred", "--also-exclude", "nope",
                              "FINDME")
        self.assertEqual(err, "")


if __name__ == "__main__":
    unittest.main()
