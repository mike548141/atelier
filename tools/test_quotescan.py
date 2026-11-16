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

    def test_a_path_scoped_commit_changing_a_floor_stamp_warns_and_lands(self):
        """115/110: the floor is compared through the index git built for the
        hook, so a `git commit -- <path>` reads the side it is committing."""
        stamp = ("<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n"
                 "- confirm first\n<!-- stamp:end -->\n")
        (self.root / "CLAUDE.md").write_text(stamp, encoding="utf-8")
        _git(self.root, "add", "CLAUDE.md")
        _git(self.root, "commit", "-q", "-m", "add")
        (self.root / "CLAUDE.md").write_text(stamp.replace("confirm first", "proceed"),
                                             encoding="utf-8")
        r = _git(self.root, "commit", "-m", "docs: tidy", "--", "CLAUDE.md")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("🟡 quotescan: CLAUDE.md changes the always-confirm floor", r.stderr)


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


FLOOR_TEXT = ("intro\n<!-- floor:begin -->\n- confirm before a public flip\n"
              "<!-- floor:end -->\noutro\n")
STAMPED = ("# repo\n\n<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n"
           "- confirm before a public flip\n<!-- stamp:end -->\n\nnotes\n")
SETTINGS = '{"model": "a", "permissions": {"allow": ["Read"]}}\n'


class AuthoritySurfaceTest(Base):
    """115/110: an edit to the agent's grant of authority, with no quotation of
    the principal, gets a 🟡 line and never blocks, on any date."""

    def setUp(self):
        super().setUp()
        files = {q.AUTONOMY_PATH: "grant\n", q.FLOOR_SOURCE: FLOOR_TEXT,
                 "CLAUDE.md": STAMPED, ".claude/settings.json": SETTINGS}
        for rel, text in files.items():
            (self.root / rel).parent.mkdir(parents=True, exist_ok=True)
            (self.root / rel).write_text(text, encoding="utf-8")
        _git(self.root, "add", "-A")
        _git(self.root, "commit", "-q", "-m", "surfaces")

    def _stage(self, rel, text):
        (self.root / rel).write_text(text, encoding="utf-8")
        _git(self.root, "add", rel)

    def _advisory(self, out):
        import floor
        return floor._read_advisory_count(out, "quotescan")

    def test_an_autonomy_edit_warns_and_never_blocks(self):
        self._stage(q.AUTONOMY_PATH, "grant widened\n")
        for today in (datetime.date(2026, 11, 16), datetime.date(2030, 1, 1)):
            with self.subTest(today=today):
                rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"),
                                        today=today)
                self.assertEqual(rc, 0, out)
                self.assertIn(f"🟡 quotescan: {q.AUTONOMY_PATH} changes the autonomy grant", out)
                self.assertIn("quote them in the commit body", out)
                self.assertEqual(self._advisory(out), 1)

    def test_a_quote_or_a_reasoned_marker_clears_it(self):
        self._stage(q.AUTONOMY_PATH, "grant widened\n")
        for msg in ('docs: grant\n\nHe said: "yes, widen it"\n',
                    "docs: grant\n\n> yes, widen it\n",
                    "docs: grant\n\nquotescan:allow: a link rename\n"):
            with self.subTest(msg=msg):
                rc, out = self.run_main("--message-file", self._msg(msg))
                self.assertEqual(rc, 0, out)
                self.assertIn("clean", out)

    def test_the_floor_region_is_a_surface_the_rest_of_the_file_is_not(self):
        self._stage(q.FLOOR_SOURCE, FLOOR_TEXT.replace("outro", "after"))
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"))
        self.assertEqual(rc, 0, out)
        self.assertIn("clean", out)
        self._stage(q.FLOOR_SOURCE, FLOOR_TEXT.replace("confirm before", "proceed on"))
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"))
        self.assertEqual(rc, 0, out)
        self.assertIn("changes the always-confirm floor", out)

    def test_a_stamped_copy_in_claude_md_is_a_surface(self):
        self._stage("CLAUDE.md", STAMPED.replace("notes", "more notes"))
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"))
        self.assertIn("clean", out)
        self._stage("CLAUDE.md", STAMPED.replace("confirm before", "proceed on"))
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"))
        self.assertEqual(rc, 0, out)
        self.assertIn("CLAUDE.md changes the always-confirm floor", out)

    def test_removing_the_stamp_reads_as_a_change(self):
        self._stage("CLAUDE.md", "# repo\n\nnotes\n")
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"))
        self.assertIn("changes the always-confirm floor", out)

    def test_the_permissions_key_is_a_surface_other_keys_are_not(self):
        sp = ".claude/settings.json"
        self._stage(sp, SETTINGS.replace('"a"', '"b"'))
        rc, out = self.run_main("--message-file", self._msg("chore: model\n"))
        self.assertIn("clean", out)
        self._stage(sp, SETTINGS.replace('["Read"]', '["Read", "Bash"]'))
        rc, out = self.run_main("--message-file", self._msg("chore: allow\n"))
        self.assertEqual(rc, 0, out)
        self.assertIn(f"{sp} changes a permission allowlist", out)

    def test_a_new_settings_file_with_permissions_and_a_deleted_grant(self):
        nested = "sub/.claude/settings.local.json"
        (self.root / nested).parent.mkdir(parents=True)
        (self.root / nested).write_text(SETTINGS, encoding="utf-8")
        _git(self.root, "add", "-f", nested)  # a global ignore may name it
        rc, out = self.run_main("--message-file", self._msg("chore: add\n"))
        self.assertIn(f"{nested} changes a permission allowlist", out)
        _git(self.root, "reset", "-q")
        _git(self.root, "rm", "-q", q.AUTONOMY_PATH)
        rc, out = self.run_main("--message-file", self._msg("chore: drop\n"))
        self.assertEqual(rc, 0, out)
        self.assertIn("changes the autonomy grant", out)

    def test_a_prompt_finding_still_blocks_beside_an_advisory_one(self):
        self._stage_prompt()
        self._stage(q.AUTONOMY_PATH, "grant widened\n")
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"),
                                today=datetime.date(2027, 6, 1))
        self.assertEqual(rc, 1, out)
        self.assertIn("commit blocked", out)
        self.assertIn("🟡 quotescan", out)
        self.assertEqual(self._advisory(out), 1, "the authority line is the advisory")

    def test_the_ci_plane_names_the_commit_and_reports_only(self):
        self._stage(q.AUTONOMY_PATH, "grant widened\n")
        _git(self.root, "commit", "-q", "-m", "docs: tidy")
        rc, out = self.run_main("--range", "HEAD^..HEAD", "--warn")
        self.assertEqual(rc, 0, out)
        sha = _git(self.root, "rev-parse", "--short=12", "HEAD").stdout.strip()
        self.assertIn(f"🟡 quotescan: {sha} {q.AUTONOMY_PATH}", out)
        self.assertIn("A pushed message cannot be changed now", out)

    def test_a_repo_with_none_of_the_surfaces_is_clean(self):
        """A child that carries none of these files: no error, no finding."""
        (self.root / "other.txt").write_text("2\n", encoding="utf-8")
        _git(self.root, "add", "other.txt")
        _git(self.root, "commit", "-q", "-m", "x")
        rc, out = self.run_main("--range", "HEAD^..HEAD", "--warn")
        self.assertEqual(rc, 0, out)
        self.assertIn("clean", out)

    def test_json_states_kind_and_surface(self):
        self._stage(q.AUTONOMY_PATH, "grant widened\n")
        rc, out = self.run_main("--message-file", self._msg("docs: tidy\n"), "--json")
        import json
        doc = json.loads(out)
        self.assertFalse(doc["blocking"])
        self.assertEqual(doc["advisory"], 1)
        self.assertEqual(doc["findings"], [{"where": "this commit",
                                            "paths": [q.AUTONOMY_PATH],
                                            "kind": "authority",
                                            "surface": "the autonomy grant"}])


if __name__ == "__main__":
    unittest.main()
