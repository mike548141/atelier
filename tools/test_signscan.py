"""Stdlib-only tests for signscan (no pytest): `python3 -m unittest`.

Signature machinery is exercised two ways: the embedded fixture (via --selftest,
the real ssh-keygen path) and a throwaway git repo for range/classification —
the latter uses UNSIGNED commits and a forced web-flow committer, so it needs no
key material and runs anywhere git does.
"""

import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import signscan as ss
import memprobe

TOOLS_DIR = Path(__file__).resolve().parent


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

    def test_an_option_shaped_boundary_is_refused_not_obeyed(self):
        """AR6b. The boundary is a caller's workflow input. `--branches=*` plus
        `..HEAD` was read by git as an option and listed NO commits with exit 0,
        so nothing was verified and nothing said so. `--end-of-options` makes it
        a (bad) revision, which is the error it should be."""
        with self.assertRaises(ss.SignscanError):
            ss.commit_range(self.repo.dir, "--branches=*", None)
        with self.assertRaises(ss.SignscanError):
            ss.commit_range(self.repo.dir, None, "--branches=*")

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


class CoverageLine(unittest.TestCase):
    """115/130: the verdict line is followed by what was examined and verified,
    on the failing path as on the passing one; exit codes are unchanged."""

    def _report(self, statuses):
        return {"repo": ".", "allowed_signers": "x",
                "results": [{"sha": "a" * 40, "plane": p, "status": s, "detail": ""}
                            for p, s in statuses]}

    def test_a_passing_range_counts_commits_and_signatures(self):
        rep = self._report([("github", "deferred"), ("machine", "good")])
        out, code = ss.render_human(rep, warn=False)
        self.assertEqual(code, 0)
        self.assertIn("  coverage: 2 commit(s) examined \u00b7 1 signature(s) "
                      "checked (1 good \u00b7 0 bad \u00b7 0 accepted)", out)
        self.assertNotIn("scanned nothing", out)

    def test_a_failing_range_prints_it_too(self):
        out, code = ss.render_human(self._report([("machine", "bad")]),
                                    warn=False)
        self.assertEqual(code, 1)
        self.assertIn("coverage: 1 commit(s) examined \u00b7 1 signature(s) "
                      "checked (0 good \u00b7 1 bad \u00b7 0 accepted)", out)

    def test_an_empty_range_says_scanned_nothing_and_still_passes(self):
        out, code = ss.render_human(self._report([]), warn=False)
        self.assertEqual(code, 0)
        self.assertIn("coverage: 0 commit(s) examined \u00b7 0 signature(s) "
                      "checked (0 good \u00b7 0 bad \u00b7 0 accepted)", out)
        self.assertIn("scanned nothing: no commits were evaluated", out)

    def test_only_server_commits_verify_nothing_here_and_say_so(self):
        out, code = ss.render_human(self._report([("github", "deferred")]),
                                    warn=False)
        self.assertEqual(code, 0)
        self.assertIn("scanned nothing: no signatures were evaluated", out)

    def test_json_carries_the_same_coverage(self):
        rep = self._report([("github", "deferred"), ("machine", "good")])
        self.assertEqual({"files_opened": 2, "signatures_verified": 1,
                          "scanned_nothing": False, "signatures_checked": 1,
                          "signatures_good": 1, "signatures_bad": 0,
                          "signatures_accepted": 0},
                         ss.coverage_dict(rep))

    def test_a_bad_signature_is_checked_not_verified(self):
        """115/510 item 3: the line once counted a failed signature as
        verified. The old key keeps its value; the new keys tell the truth."""
        rep = self._report([("machine", "good"), ("machine", "bad"),
                            ("github", "deferred")])
        out, _ = ss.render_human(rep, warn=True)
        self.assertNotIn("signature(s) verified", out)
        self.assertIn("2 signature(s) checked (1 good \u00b7 1 bad "
                      "\u00b7 0 accepted)", out)
        d = ss.coverage_dict(rep)
        self.assertEqual((2, 1, 1), (d["signatures_checked"],
                                     d["signatures_good"],
                                     d["signatures_bad"]))
        self.assertEqual(2, d["signatures_verified"])


class AcceptedExceptions(unittest.TestCase):
    """115/520: history that can never be re-signed is accepted by exact full
    commit id, each entry reasoned. The list is narrow by construction: a new
    unsigned commit by the same committer still fails, and a malformed list
    is an environment error (exit 2), never a warning."""

    def setUp(self):
        self.repo = TempRepo()
        self.old = self.repo.commit("old unsigned")
        self.new = self.repo.commit("new unsigned")  # same committer identity
        self.trust = Planes._allowed(self)
        self.addCleanup(os.unlink, self.trust)

    def _list(self, text):
        fd, path = tempfile.mkstemp()
        os.write(fd, text.encode())
        os.close(fd)
        self.addCleanup(os.unlink, path)
        return path

    def _main(self, *extra):
        out = io.StringIO()
        err = io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = ss.main(["--repo", self.repo.dir,
                            "--allowed-signers", self.trust, *extra])
        return code, out.getvalue(), err.getvalue()

    def test_a_listed_commit_is_accepted_and_does_not_block(self):
        acc = self._list(f"# accepted history, reason stated here\n{self.old}\n")
        rep = ss.scan(self.repo.dir, self.trust, None, self.old,
                      ss.WEB_FLOW_EMAIL, acc)
        self.assertEqual("accepted", rep["results"][0]["status"])
        self.assertEqual("machine", rep["results"][0]["plane"])
        code, out, _ = self._main("--rev", self.old, "--accepted", acc)
        self.assertEqual(0, code)  # blocking mode, no --warn
        self.assertIn("0 good, 0 bad, 1 accepted", out)
        self.assertIn("(0 good \u00b7 0 bad \u00b7 1 accepted)", out)

    def test_a_trailing_reason_is_a_reason_too(self):
        acc = self._list(f"{self.old}  # accepted: the reason on its line\n")
        rep = ss.scan(self.repo.dir, self.trust, None, self.old,
                      ss.WEB_FLOW_EMAIL, acc)
        self.assertEqual("accepted", rep["results"][0]["status"])

    def test_an_unlisted_commit_by_the_same_identity_still_fails(self):
        acc = self._list(f"# only the old one\n{self.old}\n")
        self.assertEqual(ss.committer_email(self.repo.dir, self.old),
                         ss.committer_email(self.repo.dir, self.new))
        rep = ss.scan(self.repo.dir, self.trust, None, None,
                      ss.WEB_FLOW_EMAIL, acc)
        by = {r["sha"]: r["status"] for r in rep["results"]}
        self.assertEqual({self.old: "accepted", self.new: "bad"}, by)
        code, out, _ = self._main("--accepted", acc)
        self.assertEqual(1, code)
        self.assertIn("0 good, 1 bad, 1 accepted", out)
        d = ss.coverage_dict(rep)
        self.assertEqual((2, 0, 1, 1), (d["signatures_checked"],
                                        d["signatures_good"],
                                        d["signatures_bad"],
                                        d["signatures_accepted"]))

    def test_json_exit_ignores_accepted_but_not_bad(self):
        acc = self._list(f"# both\n{self.old}\n{self.new}\n")
        code, out, _ = self._main("--accepted", acc, "--json")
        self.assertEqual(0, code)
        self.assertEqual(2, json.loads(out)["coverage"]["signatures_accepted"])

    def test_malformed_lists_red_loudly_even_under_warn(self):
        short = self.old[:12]
        cases = {
            "unreasoned": f"{self.old}\n",
            "abbreviated id": f"# reason\n{short}\n",
            "uppercase id": f"# reason\n{self.old.upper()}\n",
            "second field": f"# reason\n{self.old} someone@example.test\n",
            "a range": f"# reason\n{self.old}..{self.new}\n",
            "duplicate": f"# reason\n{self.old}\n{self.old}\n",
        }
        for name, text in cases.items():
            with self.subTest(name):
                acc = self._list(text)
                with self.assertRaises(ss.SignscanError):
                    ss.load_accepted(acc)
                code, _, err = self._main("--warn", "--accepted", acc)
                self.assertEqual(2, code)
                self.assertIn("malformed accepted-exception file", err)

    def test_a_named_but_missing_list_is_an_environment_error(self):
        code, _, err = self._main("--warn", "--accepted", "/no/such/accepted")
        self.assertEqual(2, code)
        self.assertIn("accepted-exception file not found", err)

    def test_a_listed_commit_that_verifies_is_just_good(self):
        rep = {"repo": ".", "allowed_signers": "x",
               "results": [{"sha": "a" * 40, "plane": "machine",
                            "status": "good", "detail": ""}]}
        out, code = ss.render_human(rep, warn=False)
        self.assertEqual(0, code)
        self.assertIn("1 good, 0 bad, 0 accepted", out)

    def test_the_repo_list_is_well_formed(self):
        """atelier's own list parses: every entry is a full id with a reason."""
        root = TOOLS_DIR.parent / ".signscanaccept"
        entries = ss.load_accepted(str(root))
        self.assertEqual(29, len(entries))


class BoundedMemory(unittest.TestCase):
    """020/380 — extending 020/370's ruling to signscan. UNLIKE the tree-
    walking guards, signscan never reads a file's content at all: it holds
    one small `dict` per commit in the verified range (sha, plane, status, a
    short detail string) — a shape that already scales with the NUMBER of
    commits scanned, never with the size of any file or the tree. Measured
    while building this fix (see below): peak RSS grew well under a
    megabyte for a 10x larger commit range, on a REAL checkout (atelier's
    own history, 1324 commits) as well as a synthetic one — so this test is
    measurement-and-pin, not a rewrite, per the board item's own "already
    bounded needs no rewrite" close condition.

    Runs the real CLI as a SUBPROCESS via `memprobe.run_and_measure` and
    reads peak RSS back from the kernel — see `tools/memprobe.py`. Commits
    are UNSIGNED (git verify-commit fails fast, no ssh-keygen key material
    needed) so the measurement stays about memory, not signature-verify
    latency."""

    SIGNSCAN = str(TOOLS_DIR / "signscan.py")
    SMALL_COMMITS = 30
    LARGE_COMMITS = 300
    # Grounded in the shape, not fitted to a measurement: each held result is
    # a handful of short strings in a dict — call it generously 1 KiB each
    # (secretscan's own `Finding` was measured at ~700 B/object for a
    # similarly-shaped record) — so even 10,000 EXTRA commits would be under
    # 10 MB. 270 extra commits here should show growth close to zero; this
    # bound leaves two-plus orders of magnitude of headroom over that.
    GROWTH_BOUND_BYTES = 20 * 1024 * 1024

    @staticmethod
    def _run(cwd, *args, env=None):
        e = dict(os.environ)
        e.update({"GIT_AUTHOR_NAME": "T", "GIT_AUTHOR_EMAIL": "t@example.test",
                 "GIT_COMMITTER_NAME": "T", "GIT_COMMITTER_EMAIL": "t@example.test"})
        if env:
            e.update(env)
        return subprocess.run(["git", *args], cwd=cwd, env=e,
                              capture_output=True, text=True, check=True)

    def _build_repo(self, n_commits: int) -> str:
        d = tempfile.mkdtemp(prefix="signscan-mem-")
        self.addCleanup(lambda: __import__("shutil").rmtree(d, ignore_errors=True))
        self._run(d, "init", "-q", "-b", "main")
        self._run(d, "config", "commit.gpgsign", "false")
        fn = os.path.join(d, "f")
        for i in range(n_commits):
            with open(fn, "a") as f:
                f.write(f"line {i}\n")
            self._run(d, "add", "f")
            self._run(d, "commit", "-q", "-m", f"c{i}")
        return d

    def _allowed_signers(self) -> str:
        fd, path = tempfile.mkstemp()
        self.addCleanup(lambda: os.unlink(path))
        os.write(fd, b'x@example.test namespaces="git",valid-after="20260101" '
                     b'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAAAAAAAAAAAAAAAAAAA'
                     b'AAAAAAAAAAAAAAAAAAAAAAAA\n')
        os.close(fd)
        return path

    def _peak_rss_for(self, n_commits: int) -> int:
        repo = self._build_repo(n_commits)
        trust = self._allowed_signers()
        result = memprobe.run_and_measure(
            [sys.executable, self.SIGNSCAN, "--repo", repo,
             "--allowed-signers", trust, "--warn", "--json"],
            timeout=120, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        self.assertEqual(0, result.returncode)
        return result.peak_rss_bytes

    def test_peak_memory_does_not_scale_with_commit_count(self):
        small_peak = self._peak_rss_for(self.SMALL_COMMITS)
        large_peak = self._peak_rss_for(self.LARGE_COMMITS)
        growth = large_peak - small_peak
        self.assertLess(
            growth, self.GROWTH_BOUND_BYTES,
            f"peak RSS grew {growth / 1e6:.1f} MB for "
            f"{self.LARGE_COMMITS - self.SMALL_COMMITS} more commits "
            f"(small={small_peak / 1e6:.1f} MB, large={large_peak / 1e6:.1f} MB) "
            "— memory is scaling with the size of what's scanned (020/370's "
            "class), which signscan's per-commit-dict shape should never do.")


if __name__ == "__main__":
    unittest.main()
