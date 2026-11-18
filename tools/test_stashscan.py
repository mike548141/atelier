"""Tests for tools/stashscan.py (board 450/010 row 7). Throwaway repos only:
nothing here pushes onto, or reads, a real repository's stash stack."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = str(Path(__file__).resolve().parent / "stashscan.py")
NOW = "2026-09-21T09:00:00"
OLD = "2026-08-17T19:57:00"
IDENT = ["-c", "user.name=T", "-c", "user.email=t" + chr(64) + "example.invalid",
         "-c", "commit.gpgsign=false"]


class StashScan(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix="stashscan-test-"))
        self.addCleanup(shutil.rmtree, self.base, True)
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env.update(GIT_CONFIG_NOSYSTEM="1", HOME=str(self.base))

    def git(self, repo, *args, when=None, check=True):
        env = dict(self.env)
        if when:
            env.update(GIT_AUTHOR_DATE=when, GIT_COMMITTER_DATE=when)
        r = subprocess.run(["git", *IDENT, "-C", str(repo), *args],
                           capture_output=True, text=True, env=env)
        if check:
            self.assertEqual(r.returncode, 0, r.stderr)
        return r

    def repo(self, name="r"):
        repo = self.base / name
        repo.mkdir()
        self.git(repo, "init", "-q", "-b", "main")
        (repo / "f.txt").write_text("base\n")
        (repo / "g.txt").write_text("other\n")
        self.git(repo, "add", "-A")
        self.git(repo, "commit", "-qm", "base")
        return repo

    def stash(self, repo, msg, when):
        (repo / "f.txt").write_text(f"dirty for {msg}\n")
        self.git(repo, "stash", "push", "-q", "-m", msg, when=when)

    def run_tool(self, repo, *extra, tz=None, now=NOW):
        env = dict(self.env)
        if tz:
            env["TZ"] = tz
        argv = [sys.executable, TOOL, "--repo", str(repo), *extra]
        if now:
            argv += ["--now", now]
        r = subprocess.run(argv, capture_output=True, text=True, env=env, timeout=60)
        return r.returncode, r.stdout + r.stderr

    def stack(self, repo):
        return self.git(repo, "stash", "list", "--format=%gd %H").stdout

    def test_selftest(self):
        r = subprocess.run([sys.executable, TOOL, "--selftest"], capture_output=True,
                           text=True, env=self.env, timeout=120)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertEqual(r.stdout.strip(), "selftest OK — stashscan")

    def test_empty_stack_is_quiet_and_counts_zero(self):
        rc, out = self.run_tool(self.repo())
        self.assertEqual(rc, 0, out)
        self.assertIn("0 entries on the shared stash stack", out)

    def test_same_day_entries_are_quiet_and_counted(self):
        repo = self.repo()
        self.stash(repo, "made this morning", "2026-09-21T08:10:00")
        self.stash(repo, "made just now", NOW)
        rc, out = self.run_tool(repo)
        self.assertEqual(rc, 0, out)
        self.assertIn("2 entries", out)

    def test_old_entry_fires_naming_selector_and_age(self):
        repo = self.repo()
        self.stash(repo, "three weeks ago", OLD)
        self.stash(repo, "this morning", "2026-09-21T08:10:00")
        rc, out = self.run_tool(repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("1 of 2 entries", out)
        self.assertIn("stash@{1}", out)
        self.assertIn("35d old", out)
        self.assertIn("this morning", out)

    def test_boundary_is_the_calendar_day(self):
        a, b = self.repo("a"), self.repo("b")
        self.stash(a, "one second before midnight", "2026-09-20T23:59:59")
        self.stash(b, "midnight exactly", "2026-09-21T00:00:00")
        self.assertEqual(self.run_tool(a)[0], 1)
        self.assertEqual(self.run_tool(b)[0], 0)

    def test_local_zone_is_load_bearing(self):
        repo = self.repo()
        self.stash(repo, "a fixed instant", "2026-09-20T13:30:00+00:00")
        self.assertEqual(self.run_tool(repo, tz="Pacific/Auckland")[0], 0)
        self.assertEqual(self.run_tool(repo, tz="UTC")[0], 1)

    def test_a_worktree_sees_the_primary_stack(self):
        repo = self.repo()
        wt = self.base / "wt"
        self.git(repo, "worktree", "add", "-q", "-b", "wt", str(wt))
        self.stash(repo, "pushed from the primary", OLD)
        rc, out = self.run_tool(wt)
        self.assertEqual(rc, 1, out)
        self.assertIn("pushed from the primary", out)
        self.assertIn(str((repo / ".git").resolve()), out)

    def test_a_firing_run_never_mutates_the_stack(self):
        repo = self.repo()
        self.stash(repo, "old", OLD)
        before = self.stack(repo)
        self.run_tool(repo)
        self.run_tool(repo, "-v")
        self.assertEqual(before, self.stack(repo))
        self.assertTrue(before)

    def test_a_real_autostash_is_named(self):
        repo = self.repo()
        self.git(repo, "checkout", "-q", "-b", "feat")
        (repo / "g.txt").write_text("feat only\n")
        self.git(repo, "commit", "-qam", "feat")
        self.git(repo, "checkout", "-q", "main")
        (repo / "f.txt").write_text("main moved\n")
        self.git(repo, "commit", "-qam", "main2")
        self.git(repo, "checkout", "-q", "feat")
        (repo / "f.txt").write_text("uncommitted and conflicting\n")
        self.git(repo, "rebase", "--autostash", "main", when=OLD, check=False)
        if not self.stack(repo):
            self.skipTest("this git kept the conflicting autostash off refs/stash")
        rc, out = self.run_tool(repo)
        self.assertEqual(rc, 1, out)
        self.assertIn("autostash", out)

    def test_cannot_check_is_exit_2(self):
        (self.base / "nogit").mkdir()
        self.assertEqual(self.run_tool(self.base / "nogit")[0], 2)
        rc, out = self.run_tool(self.repo(), now="the day before yesterday")
        self.assertEqual(rc, 2, out)
        self.assertIn("not ISO 8601", out)

    def test_the_cli_prints_the_tree_line_of_the_repo_read(self):
        repo = self.repo()
        rc, out = self.run_tool(repo)
        self.assertTrue(any(ln.startswith("  tree ") and str(repo.resolve()) in ln
                            for ln in out.splitlines()), out)

    def hook(self, cwd):
        r = subprocess.run([sys.executable, TOOL, "--hook"],
                           input=json.dumps({"cwd": str(cwd)}),
                           capture_output=True, text=True, env=self.env, timeout=60)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout.strip()

    def test_hook_is_silent_when_clean_or_not_a_checkout(self):
        repo = self.repo()
        self.stash(repo, "set aside today", None)    # dated now: today
        self.assertEqual(self.hook(repo), "")
        (self.base / "nogit").mkdir()
        self.assertEqual(self.hook(self.base / "nogit"), "")

    def test_hook_warns_on_residue_and_forbids_touching_it(self):
        repo = self.repo()
        self.stash(repo, "prices work", OLD)
        out = json.loads(self.hook(repo))
        ctx = out["hookSpecificOutput"]["additionalContext"]
        self.assertEqual(out["hookSpecificOutput"]["hookEventName"], "SessionStart")
        self.assertIn("stash@{0}", ctx)
        self.assertIn("prices work", ctx)
        self.assertIn("do not pop", ctx)
        self.assertIn("older than today", out["systemMessage"])

    def test_hook_survives_bad_stdin(self):
        r = subprocess.run([sys.executable, TOOL, "--hook"], input="not json",
                           capture_output=True, text=True, env=self.env,
                           cwd=str(self.base), timeout=60)
        self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()
