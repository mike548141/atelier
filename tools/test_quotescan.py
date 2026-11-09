"""Tests for quotescan (no pytest needed): `python3 -m unittest`.

Board `160/900` QK1's second counsel, slice 6 of `320/810`. The paths a commit
carries are git's, so the message plane is driven by real commits through a
hook; the date flip is patched in process."""

import contextlib
import datetime
import io
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

import quotescan as q

PROMPT = q.GUARDED[0]
TOOLS = Path(__file__).resolve().parent


def _git(root, *args, env=None):
    full = {**os.environ, **(env or {})}
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, env=full, check=False)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="quotescan-test-"))
        self.root = self.tmp / "r"
        self.root.mkdir()
        for args in (["init", "-q", "-b", "main"], ["config", "user.name", "t"],
                     ["config", "user.email", "t@example.invalid"],  # leakscan:allow: RFC-2606 fixture identity
                     ["config", "commit.gpgsign", "false"]):
            _git(self.root, *args)
        (self.root / PROMPT).parent.mkdir(parents=True)
        (self.root / PROMPT).write_text("prompt text\n", encoding="utf-8")
        (self.root / "other.txt").write_text("1\n", encoding="utf-8")
        _git(self.root, "add", "-A")
        _git(self.root, "commit", "-q", "-m", "init")

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _msg(self, text):
        p = self.root.parent / "msg.txt"
        p.write_text(text, encoding="utf-8")
        return str(p)

    def run_main(self, *argv, today=None):
        out = io.StringIO()
        today = today or datetime.date(2026, 11, 10)
        with unittest.mock.patch.object(q, "_utc_today", return_value=today):
            with contextlib.redirect_stdout(out):
                rc = q.main([*argv, "--root", str(self.root)])
        return rc, out.getvalue()

    def _stage_prompt(self):
        (self.root / PROMPT).write_text("prompt changed\n", encoding="utf-8")
        _git(self.root, "add", PROMPT)


class QuoteFormTest(unittest.TestCase):
    def test_what_counts(self):
        for text in ('t\n\n"yes, add it"\n', 't\n\n“yes, add it”\n',
                     't\n\n> yes, add it\n'):
            with self.subTest(text=text):
                self.assertTrue(q.carries_quote(text))

    def test_what_does_not(self):
        for text in ('area: "word" edit\n', 'area: x\n\n`"in code here"`\n', 'area: x\n'):
            with self.subTest(text=text):
                self.assertFalse(q.carries_quote(text))


class MessagePlaneTest(Base):
    def test_a_commit_not_touching_the_prompt_is_clean(self):
        (self.root / "other.txt").write_text("2\n", encoding="utf-8")
        _git(self.root, "add", "other.txt")
        rc, out = self.run_main("--message-file", self._msg("area: unrelated\n"))
        self.assertEqual(rc, 0, out)
        self.assertIn("clean", out)
        import floor
        self.assertEqual(floor._read_advisory_count(out, "quotescan"), 0,
                         "the known zero the board reads")

    def test_touching_the_prompt_without_a_quote_warns(self):
        self._stage_prompt()
        rc, out = self.run_main("--message-file", self._msg("docs: tidy the prompt\n"))
        self.assertEqual(rc, 0)
        self.assertIn("warning; blocking from 2027-05-31", out)

    def test_a_quote_clears_it(self):
        self._stage_prompt()
        rc, out = self.run_main(
            "--message-file", self._msg('docs: prompt\n\nHe said: "add that rule"\n'))
        self.assertEqual(rc, 0, out)
        self.assertIn("clean", out)

    def test_it_blocks_on_the_flip_date(self):
        self._stage_prompt()
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"),
                                today=datetime.date(2027, 5, 31))
        self.assertEqual(rc, 1, out)
        self.assertIn("commit blocked", out)

    def test_not_the_day_before(self):
        self._stage_prompt()
        rc, _ = self.run_main("--message-file", self._msg("docs: tidy\n"),
                              today=datetime.date(2027, 5, 30))
        self.assertEqual(rc, 0)

    def test_a_reasoned_marker_exempts_a_bare_one_does_not(self):
        self._stage_prompt()
        rc, _ = self.run_main("--message-file",
                              self._msg("docs: t\n\nquotescan:allow: a link rename\n"),
                              today=datetime.date(2027, 6, 1))
        self.assertEqual(rc, 0)
        rc, _ = self.run_main("--message-file",
                              self._msg("docs: t\n\nquotescan:allow\n"),
                              today=datetime.date(2027, 6, 1))
        self.assertEqual(rc, 1)

    def test_warn_never_blocks(self):
        self._stage_prompt()
        rc, _ = self.run_main("--message-file", self._msg("docs: tidy\n"), "--warn",
                              today=datetime.date(2027, 6, 1))
        self.assertEqual(rc, 0)


class RealCommitTest(Base):
    """Driven through a real commit-msg hook: the staged paths are git's."""

    def setUp(self):
        super().setUp()
        hooks = self.root / ".githooks"
        hooks.mkdir()
        hook = hooks / "commit-msg"
        hook.write_text(f"""#!/bin/sh
"{sys.executable}" "{TOOLS / 'quotescan.py'}" --message-file "$1" --root "$(git rev-parse --show-toplevel)" >&2
""", encoding="utf-8")
        hook.chmod(0o755)
        _git(self.root, "config", "core.hooksPath", ".githooks")

    def test_a_path_scoped_commit_reads_only_what_it_named(self):
        self._stage_prompt()
        (self.root / "other.txt").write_text("2\n", encoding="utf-8")
        _git(self.root, "add", "other.txt")
        r = _git(self.root, "commit", "-m", "docs: other only", "--", "other.txt")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("clean", r.stderr)

    def test_a_commit_carrying_the_prompt_warns(self):
        self._stage_prompt()
        r = _git(self.root, "commit", "-m", "docs: tidy")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("warning; blocking from 2027-05-31", r.stderr)


class RangePlaneTest(Base):
    def test_a_range_commit_without_a_quote_reports_and_exits_zero(self):
        self._stage_prompt()
        _git(self.root, "commit", "-q", "-m", "docs: tidy the prompt")
        rc, out = self.run_main("--range", "HEAD^..HEAD", "--warn",
                                today=datetime.date(2028, 1, 1))
        self.assertEqual(rc, 0, out)
        self.assertIn("1 unquoted change", out)

    def test_a_range_commit_with_a_quote_is_clean(self):
        self._stage_prompt()
        _git(self.root, "commit", "-q", "-m", 'docs: prompt\n\n"please add it"')
        rc, out = self.run_main("--range", "HEAD^..HEAD", "--warn")
        self.assertEqual(rc, 0, out)
        self.assertIn("clean", out)

    def test_a_broken_range_is_broken_not_clean(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = q.main(["--range", "nosuch..HEAD", "--warn", "--root", str(self.root)])
        self.assertEqual(rc, 2)


if __name__ == "__main__":
    unittest.main()
