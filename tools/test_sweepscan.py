"""Stdlib-only tests for sweepscan (no pytest needed): `python3 -m unittest`.

Board `320/060`, the fourth slice of `320/810`. The signal is git's own, so
every case drives a real commit through a hook in a throwaway repo."""

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path

import sweepscan as s

TOOLS = Path(__file__).resolve().parent


def _git(cwd: Path, *args: str, env: dict | None = None) -> subprocess.CompletedProcess:
    full = {**os.environ, **(env or {})}
    # Never inherit a parent commit's hook environment into a fixture repo.
    for key in ("GIT_DIR", "GIT_INDEX_FILE", "GIT_WORK_TREE", "ATELIER_WHOLE_INDEX"):
        full.pop(key, None)
    full.update(env or {})
    return subprocess.run(["git", *args], cwd=cwd, env=full, capture_output=True,
                          text=True, check=False)


HOOK = """#!/bin/sh
"$SWEEP_PYTHON" "$SWEEP_TOOL" --root "$(git rev-parse --show-toplevel)" >&2
"""


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="sweepscan-test-"))
        self.repo = self.tmp / "r"
        self.repo.mkdir()
        _git(self.repo, "init", "-q", "-b", "main")
        for args in (("user.name", "t"),
                     ("user.email", "t@example.invalid"),  # leakscan:allow: RFC-2606 fixture identity
                     ("commit.gpgsign", "false"), ("core.hooksPath", ".githooks")):
            _git(self.repo, "config", *args)
        (self.repo / ".githooks").mkdir()
        hook = self.repo / ".githooks" / "pre-commit"
        hook.write_text(HOOK, encoding="utf-8")
        hook.chmod(0o755)
        (self.repo / "a").write_text("1\n", encoding="utf-8")
        (self.repo / "b").write_text("1\n", encoding="utf-8")
        _git(self.repo, "add", "-A")
        _git(self.repo, "commit", "-q", "-m", "init", env=self._env())

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _env(self, **extra) -> dict:
        return {"SWEEP_PYTHON": sys.executable,
                "SWEEP_TOOL": str(TOOLS / "sweepscan.py"), **extra}

    def add_sibling(self):
        _git(self.repo, "worktree", "add", "-q", str(self.tmp / "w2"), "-b", "w2")

    def commit(self, *args: str, env: dict | None = None,
               stage: bool = True) -> subprocess.CompletedProcess:
        (self.repo / "a").write_text("2\n", encoding="utf-8")
        (self.repo / "b").write_text("2\n", encoding="utf-8")
        if stage:
            _git(self.repo, "add", "-A")
        return _git(self.repo, *args, env=self._env(**(env or {})))


class CommitFormTest(Base):
    def test_one_worktree_is_out_of_scope(self):
        r = self.commit("commit", "-m", "x")
        self.assertEqual(r.returncode, 0)
        self.assertIn("one worktree", r.stderr)

    def test_a_plain_commit_with_a_sibling_warns_and_lands(self):
        self.add_sibling()
        r = self.commit("commit", "-m", "x")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("takes the whole index", r.stderr)
        self.assertIn("advisory: 1 finding(s)", r.stderr)

    def test_a_path_scoped_commit_is_clean(self):
        self.add_sibling()
        r = self.commit("commit", "-m", "x", "--", "a")
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("names its files", r.stderr)
        self.assertNotIn("takes the whole index", r.stderr)

    def test_commit_dash_a_warns(self):
        self.add_sibling()
        r = self.commit("commit", "-am", "x", stage=False)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("takes the whole index", r.stderr)

    def test_the_marker_clears_a_whole_index_commit(self):
        self.add_sibling()
        r = self.commit("commit", "-m", "x", env={"ATELIER_WHOLE_INDEX": "1"})
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertNotIn("takes the whole index", r.stderr)

    def test_a_merge_is_exempt(self):
        self.add_sibling()
        (self.tmp / "w2" / "c").write_text("1\n", encoding="utf-8")
        _git(self.tmp / "w2", "add", "c")
        _git(self.tmp / "w2", "commit", "-q", "-m", "side", env=self._env())
        # a resolved conflict is a real commit made under MERGE_HEAD
        (self.repo / "a").write_text("main\n", encoding="utf-8")
        _git(self.repo, "add", "a")
        _git(self.repo, "commit", "-q", "-m", "main", "--no-verify")
        m = _git(self.repo, "merge", "--no-commit", "--no-ff", "w2", env=self._env())
        self.assertEqual(m.returncode, 0, m.stderr)
        r = _git(self.repo, "commit", "-m", "merge", env=self._env())
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("replaying", r.stderr)

    def test_a_prunable_worktree_does_not_count(self):
        self.add_sibling()
        shutil.rmtree(self.tmp / "w2")
        self.assertEqual(s.live_worktrees(self.repo), 1)


class CliTest(Base):
    def _run(self, *argv, env=None):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            with unittest.mock.patch.dict(os.environ, env or {}, clear=False):
                rc = s.main(list(argv))
        return rc, out.getvalue()

    def test_no_commit_in_progress_is_clean(self):
        env = {k: "" for k in ("GIT_INDEX_FILE",)}
        env["GIT_INDEX_FILE"] = ""
        rc, out = self._run("--root", str(self.repo), env=env)
        self.assertEqual(rc, 0)
        self.assertIn("no commit in progress", out)

    def test_json(self):
        rc, out = self._run("--root", str(self.repo), "--json",
                            env={"GIT_INDEX_FILE": ""})
        self.assertEqual(rc, 0)
        self.assertFalse(json.loads(out)["finding"])

    def test_a_missing_root_is_broken_not_clean(self):
        rc, _ = self._run("--root", str(self.tmp / "nope"))
        self.assertEqual(rc, 2)

    def test_exits_zero_on_a_finding(self):
        self.add_sibling()
        rc, out = self._run("--root", str(self.repo),
                            env={"GIT_INDEX_FILE": ".git/index"})
        self.assertEqual(rc, 0)
        self.assertIn("advisory: 1 finding(s)", out)


if __name__ == "__main__":
    unittest.main()
