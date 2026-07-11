"""Stdlib-only tests for signscan (no pytest): `python3 -m unittest`.

Signature machinery is exercised two ways: the embedded fixture (via --selftest,
the real ssh-keygen path) and a throwaway git repo for range/classification —
the latter uses UNSIGNED commits and a forced web-flow committer, so it needs no
key material and runs anywhere git does.
"""

import os
import subprocess
import tempfile
import unittest

import signscan as ss


def _run(cwd, *args, env=None):
    e = dict(os.environ)
    # Deterministic identity + no accidental signing in the throwaway repo.
    e.update({
        "GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": "t@example.test",
        "GIT_COMMITTER_NAME": "T", "GIT_COMMITTER_EMAIL": "t@example.test",
    })
    if env:
        e.update(env)
    return subprocess.run(["git", *args], cwd=cwd, env=e,
                          capture_output=True, text=True, check=True)


class TempRepo:
    def __init__(self):
        self.dir = tempfile.mkdtemp()
        _run(self.dir, "init", "-q", "-b", "main")
        _run(self.dir, "config", "commit.gpgsign", "false")

    def commit(self, msg, committer_email=None):
        # A tree change per commit so rev-list is meaningful.
        fn = os.path.join(self.dir, "f")
        with open(fn, "a") as f:
            f.write(msg + "\n")
        _run(self.dir, "add", "f")
        env = {"GIT_COMMITTER_EMAIL": committer_email} if committer_email else None
        _run(self.dir, "commit", "-q", "-m", msg, env=env)
        return _run(self.dir, "rev-parse", "HEAD").stdout.strip()


class Selftest(unittest.TestCase):
    def test_selftest_passes(self):
        # The fixture verifies and tampering is rejected — the load-bearing guard.
        self.assertEqual(ss.main(["--selftest"]), 0)


class Range(unittest.TestCase):
    def setUp(self):
        self.repo = TempRepo()
        self.c1 = self.repo.commit("one")
        self.c2 = self.repo.commit("two")
        self.c3 = self.repo.commit("three")

    def test_boundary_is_exclusive(self):
        got = ss.commit_range(self.repo.dir, self.c1, None)
        self.assertEqual(got, [self.c3, self.c2])  # rev-list order, c1 excluded

    def test_single_rev(self):
        self.assertEqual(ss.commit_range(self.repo.dir, None, self.c2), [self.c2])

    def test_no_boundary_verifies_all_history(self):
        # Born-signed default: every commit, not just HEAD.
        self.assertEqual(ss.commit_range(self.repo.dir, None, None),
                         [self.c3, self.c2, self.c1])

    def test_committer_email(self):
        self.assertEqual(ss.committer_email(self.repo.dir, self.c1), "t@example.test")


class Planes(unittest.TestCase):
    def _allowed(self):
        # A syntactically valid trust list; content is irrelevant to these cases
        # (unsigned commits fail before any key match; web-flow commits defer).
        fd, path = tempfile.mkstemp()
        os.write(fd, b'x@example.test namespaces="git",valid-after="20260101" '
                     b'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAAAAAAAAAAAAAAAAAAA'
                     b'AAAAAAAAAAAAAAAAAAAAAAAA\n')
        os.close(fd)
        return path

    def test_unsigned_machine_commit_is_bad(self):
        repo = TempRepo()
        sha = repo.commit("unsigned")
        rep = ss.scan(repo.dir, self._allowed(), None, sha, ss.WEB_FLOW_EMAIL)
        self.assertEqual(rep["results"][0]["status"], "bad")
        self.assertEqual(rep["results"][0]["plane"], "machine")

    def test_web_flow_commit_defers(self):
        repo = TempRepo()
        sha = repo.commit("merge", committer_email=ss.WEB_FLOW_EMAIL)
        rep = ss.scan(repo.dir, self._allowed(), None, sha, ss.WEB_FLOW_EMAIL)
        self.assertEqual(rep["results"][0]["status"], "deferred")
        self.assertEqual(rep["results"][0]["plane"], "github")

    def test_missing_allowed_signers_is_environment_error(self):
        repo = TempRepo()
        repo.commit("x")
        with self.assertRaises(ss.SignscanError):
            ss.scan(repo.dir, "/no/such/allowed_signers", None, None, ss.WEB_FLOW_EMAIL)


class Reporting(unittest.TestCase):
    def _report(self, statuses):
        return {"repo": ".", "allowed_signers": "x",
                "results": [{"sha": "a" * 40, "plane": p, "status": s, "detail": ""}
                            for p, s in statuses]}

    def test_bad_blocks_unless_warn(self):
        rep = self._report([("machine", "bad")])
        self.assertEqual(ss.render_human(rep, warn=False)[1], 1)
        self.assertEqual(ss.render_human(rep, warn=True)[1], 0)

    def test_all_good_passes(self):
        rep = self._report([("machine", "good"), ("machine", "good")])
        self.assertEqual(ss.render_human(rep, warn=False)[1], 0)

    def test_deferred_does_not_block(self):
        rep = self._report([("github", "deferred"), ("machine", "good")])
        self.assertEqual(ss.render_human(rep, warn=False)[1], 0)


if __name__ == "__main__":
    unittest.main()
