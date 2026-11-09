"""Tests for namescan (no pytest needed): `python3 -m unittest`.

Board `160/360` finding NP2, slice 5 of `320/810`. Term lists are synthetic and
written to a temp file, so no real name ever enters the repo. Exit codes and
the date flip are tested through `main` with `_utc_today` patched."""

import contextlib
import datetime
import io
import json
import os
import subprocess
import tempfile
import unittest
import unittest.mock
from pathlib import Path

import namescan as n

FAKE_TERM = "zephyrquill"


def _git(root, *args, env=None):
    return subprocess.run(["git", "-C", str(root), *args], capture_output=True,
                          text=True, env=env, check=False)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.terms = self.root / "terms.txt"
        self.terms.write_text(f"{FAKE_TERM}\n", encoding="utf-8")
        for args in (["init", "-q", "-b", "main"], ["config", "user.name", "t"],
                     ["config", "user.email", "t@example.invalid"],  # leakscan:allow: RFC-2606 fixture identity
                     ["config", "commit.gpgsign", "false"]):
            _git(self.root, *args)
        (self.root / ".atelier-floor.json").write_text(
            json.dumps({"visibility": "public"}), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def _msg(self, text):
        p = self.root / "msg.txt"
        p.write_text(text, encoding="utf-8")
        return str(p)

    def run_main(self, *argv, today=None):
        out = io.StringIO()
        today = today or datetime.date(2026, 11, 10)
        with unittest.mock.patch.object(n, "_utc_today", return_value=today):
            with contextlib.redirect_stdout(out):
                rc = n.main([*argv, "--root", str(self.root), "--terms", str(self.terms)])
        return rc, out.getvalue()


class ScopeTest(Base):
    def test_a_repo_not_declared_public_is_out_of_scope(self):
        (self.root / ".atelier-floor.json").write_text("{}", encoding="utf-8")
        rc, out = self.run_main("--message-file", self._msg(f"tools: {FAKE_TERM}\n"))
        self.assertEqual(rc, 0)
        self.assertIn("out of scope", out)


class MessagePlaneTest(Base):
    def test_a_clean_title_passes(self):
        rc, out = self.run_main("--message-file", self._msg("tools: add a check\n"))
        self.assertEqual(rc, 0, out)
        self.assertIn("clean", out)
        import floor
        self.assertEqual(floor._read_advisory_count(out, "namescan"), 0,
                         "the known zero the board reads")

    def test_a_term_in_the_title_warns_before_the_date(self):
        rc, out = self.run_main("--message-file", self._msg(f"tools: {FAKE_TERM} fix\n"))
        self.assertEqual(rc, 0)
        self.assertIn("warning; blocking from 2027-05-03", out)
        self.assertNotIn(FAKE_TERM, out, "a finding never prints the term")

    def test_a_term_in_the_branch_warns(self):
        _git(self.root, "checkout", "-q", "-b", f"report-{FAKE_TERM}-1")
        rc, out = self.run_main("--message-file", self._msg("tools: clean title\n"))
        self.assertEqual(rc, 0)
        self.assertIn("branch", out)

    def test_it_blocks_on_the_flip_date(self):
        rc, out = self.run_main("--message-file", self._msg(f"tools: {FAKE_TERM}\n"),
                                today=datetime.date(2027, 5, 3))
        self.assertEqual(rc, 1, out)
        self.assertIn("commit blocked", out)

    def test_it_does_not_block_the_day_before(self):
        rc, _ = self.run_main("--message-file", self._msg(f"tools: {FAKE_TERM}\n"),
                              today=datetime.date(2027, 5, 2))
        self.assertEqual(rc, 0)

    def test_warn_never_blocks(self):
        rc, _ = self.run_main("--message-file", self._msg(f"tools: {FAKE_TERM}\n"),
                              "--warn", today=datetime.date(2027, 5, 3))
        self.assertEqual(rc, 0)

    def test_a_reasoned_marker_in_the_body_exempts(self):
        text = f"tools: {FAKE_TERM}\n\nnamescan:allow: a synthetic name, test fixture\n"
        rc, out = self.run_main("--message-file", self._msg(text),
                                today=datetime.date(2027, 5, 3))
        self.assertEqual(rc, 0, out)

    def test_a_bare_marker_exempts_nothing(self):
        text = f"tools: {FAKE_TERM}\n\nnamescan:allow\n"
        rc, _ = self.run_main("--message-file", self._msg(text),
                              today=datetime.date(2027, 5, 3))
        self.assertEqual(rc, 1)

    def test_require_terms_with_no_list_is_broken(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = n.main(["--message-file", self._msg("x\n"), "--root", str(self.root),
                         "--require-terms", "--terms", str(self.root / "no-such-list")])
        self.assertEqual(rc, 2)

    def test_one_source_exactly(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            self.assertEqual(n.main(["--root", str(self.root)]), 2)
            self.assertEqual(n.main(["--message-file", "a", "--range", "b",
                                     "--root", str(self.root)]), 2)


class RangePlaneTest(Base):
    def _commit(self, msg):
        (self.root / "f").write_text(msg, encoding="utf-8")
        _git(self.root, "add", "f")
        _git(self.root, "commit", "-q", "-m", msg)

    def test_range_reports_and_never_blocks(self):
        self._commit("area: first\n")
        self._commit(f"area: {FAKE_TERM} second\n")
        rc, out = self.run_main("--range", "HEAD^..HEAD", "--warn",
                                today=datetime.date(2028, 1, 1))
        self.assertEqual(rc, 0, out)
        self.assertIn("private name", out)

    def test_range_exits_zero_even_without_warn_after_the_date(self):
        self._commit("area: first\n")
        self._commit(f"area: {FAKE_TERM} second\n")
        rc, _ = self.run_main("--range", "HEAD^..HEAD",
                              today=datetime.date(2028, 1, 1))
        self.assertEqual(rc, 0)

    def test_a_broken_range_is_broken_not_clean(self):
        self._commit("area: first\n")
        out = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(out):
            rc = n.main(["--range", "nosuch..HEAD", "--warn", "--root", str(self.root),
                         "--terms", str(self.terms)])
        self.assertEqual(rc, 2, out.getvalue())


if __name__ == "__main__":
    unittest.main()
