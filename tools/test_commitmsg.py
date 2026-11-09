"""Tests for commitmsg, the helper the commit-message checks share."""

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import commitmsg as c


class CleanTest(unittest.TestCase):
    def test_comment_lines_go(self):
        self.assertEqual(c.clean("title\n\nbody\n# On branch x\n"), "title\n\nbody")

    def test_a_scissors_section_is_dropped(self):
        text = "title\n# ------------------------ >8 ------------------------\ndiff --git\n"
        self.assertEqual(c.clean(text), "title")

    def test_a_custom_comment_char(self):
        self.assertEqual(c.clean("title\n; note\n", ";"), "title")

    def test_subject_skips_blank_lines(self):
        self.assertEqual(c.subject("\n\n  title \n\nbody\n"), "title")
        self.assertEqual(c.subject(""), "")


class RepoTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for args in (["init", "-q", "-b", "main"], ["config", "user.name", "t"],
                     ["config", "user.email", "t@example.invalid"],  # leakscan:allow: RFC-2606 fixture identity
                     ["config", "commit.gpgsign", "false"]):
            subprocess.run(["git", "-C", str(self.root), *args], check=True,
                           capture_output=True)

    def tearDown(self):
        self.tmp.cleanup()

    def _commit(self, name, text):
        (self.root / name).write_text(text, encoding="utf-8")
        subprocess.run(["git", "-C", str(self.root), "add", name], check=True,
                       capture_output=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-q", "-m",
                        f"add {name}\n\nbody of {name}"], check=True,
                       capture_output=True)

    def test_commits_reads_a_range_newest_first(self):
        self._commit("a", "1\n")
        self._commit("b", "2\n")
        got = c.commits(self.root, "HEAD~1..HEAD")
        self.assertEqual(len(got), 1)
        self.assertEqual(c.subject(got[0].message), "add b")

    def test_commits_refuses_a_range_git_cannot_read(self):
        self._commit("a", "1\n")
        with self.assertRaises(RuntimeError):
            c.commits(self.root, "nosuch..HEAD")

    def test_commit_files_includes_a_deletion(self):
        self._commit("a", "1\n")
        subprocess.run(["git", "-C", str(self.root), "rm", "-q", "a"], check=True)
        subprocess.run(["git", "-C", str(self.root), "commit", "-q", "-m", "rm a"],
                       check=True, capture_output=True)
        sha = c.commits(self.root, "HEAD~1..HEAD")[0].sha
        self.assertEqual(c.commit_files(self.root, sha), ["a"])

    def test_branch_uses_the_ref_name_in_ci(self):
        self._commit("a", "1\n")
        self.assertEqual(c.branch(self.root, {"GITHUB_REF_NAME": "feature"}), "feature")
        self.assertEqual(c.branch(self.root, {"GITHUB_HEAD_REF": "pr-branch",
                                              "GITHUB_REF_NAME": "1/merge"}), "pr-branch")

    def test_pushed_range_from_the_event(self):
        self._commit("a", "1\n")
        self._commit("b", "2\n")
        base = c.commits(self.root, "HEAD~1..HEAD")[0].sha  # stand-in sha, resolvable
        with tempfile.NamedTemporaryFile("w", suffix=".json") as ev:
            json.dump({"before": base}, ev)
            ev.flush()
            spec, note = c.pushed_range(self.root, {"GITHUB_EVENT_PATH": ev.name})
        self.assertEqual(spec, f"{base}..HEAD")
        self.assertEqual(note, "")

    def test_pushed_range_for_a_new_branch_reads_head(self):
        self._commit("a", "1\n")
        self._commit("b", "2\n")
        with tempfile.NamedTemporaryFile("w", suffix=".json") as ev:
            json.dump({"before": "0" * 40}, ev)
            ev.flush()
            spec, note = c.pushed_range(self.root, {"GITHUB_EVENT_PATH": ev.name})
        self.assertEqual(spec, "HEAD^..HEAD")
        self.assertIn("HEAD only", note)

    def test_pushed_range_with_no_commits_reads_nothing_and_does_not_fail(self):
        spec, note = c.pushed_range(self.root, {})
        self.assertEqual(spec, "")
        self.assertIn("no commits", note)
        self.assertEqual(c.commits(self.root, spec), [])

    def test_pushed_range_with_no_event(self):
        self._commit("a", "1\n")
        self.assertEqual(c.pushed_range(self.root, {})[0], "HEAD")


if __name__ == "__main__":
    unittest.main()
