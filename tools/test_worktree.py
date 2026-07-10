"""Stdlib-only tests for worktree (no pytest needed): `python3 -m unittest`.

The command tests build real throwaway git repos under a tmp dir (never iCloud)
and drive worktree.py end-to-end, so the guards are proven against real git, not
mocks. The pure-logic guards (iCloud detection, feature validation) are unit-tested
directly and need no git."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

import worktree as wt


def git(args, cwd):
    subprocess.run(["git", *args], cwd=str(cwd), check=True,
                   capture_output=True, text=True)


class Guards(unittest.TestCase):
    def test_icloud_paths_detected(self):
        for p in ("~/Library/Mobile Documents/com~apple~CloudDocs/x",
                  "/Users/x/Library/CloudStorage/Dropbox/repo"):
            self.assertTrue(wt.is_icloud(Path(p)), p)

    def test_plain_path_not_icloud(self):
        self.assertFalse(wt.is_icloud(Path("~/worktrees/repo-feat")))

    def test_feature_validation(self):
        for good in ("perf-harness", "v2.1_fix", "a"):
            self.assertRegex(good, wt.FEATURE_RE)
        for bad in ("feature/foo", "bad name", "", "-lead"):
            self.assertIsNone(wt.FEATURE_RE.match(bad))

    def test_selftest_passes(self):
        self.assertEqual(wt._selftest(), 0)


class CommandsOnRealRepo(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="wt-test-")
        self.repo = Path(self.tmp) / "acme"
        self.repo.mkdir()
        git(["init", "-q", "-b", "main"], self.repo)
        git(["config", "user.email", "t@example.com"], self.repo)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], self.repo)
        (self.repo / "README.md").write_text("seed\n")
        git(["add", "-A"], self.repo)
        git(["commit", "-qm", "seed"], self.repo)
        self.base = Path(self.tmp) / "worktrees"
        self._cwd = os.getcwd()
        os.chdir(self.repo)

    def tearDown(self):
        os.chdir(self._cwd)
        subprocess.run(["rm", "-rf", self.tmp])

    def cli(self, argv):
        return wt.main(["--base", str(self.base)] + argv)

    def test_start_creates_worktree_and_branch(self):
        rc = self.cli(["start", "featx"])
        self.assertEqual(rc, 0)
        path = self.base / "acme-featx"
        self.assertTrue((path / ".git").exists())
        head = subprocess.run(["git", "-C", str(path), "rev-parse", "--abbrev-ref", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
        self.assertEqual(head, "featx")

    def test_start_refuses_icloud_base(self):
        rc = wt.main(["--base", "~/Library/Mobile Documents/com~apple~CloudDocs/wt",
                      "start", "featx"])
        self.assertEqual(rc, 2)

    def test_start_rejects_bad_feature(self):
        self.assertEqual(self.cli(["start", "bad/name"]), 2)

    def test_start_off_main_not_current_branch(self):
        # A dirty/other branch must not leak into the new line of work.
        git(["checkout", "-q", "-b", "wip"], self.repo)
        (self.repo / "wip.txt").write_text("junk\n")
        git(["add", "-A"], self.repo)
        git(["commit", "-qm", "wip-only"], self.repo)
        self.cli(["start", "clean"])
        path = self.base / "acme-clean"
        self.assertFalse((path / "wip.txt").exists())  # branched off main, not wip

    def test_list_reports_worktree(self):
        self.cli(["start", "featx"])
        rc = wt.main(["--base", str(self.base), "--json", "list"])
        self.assertEqual(rc, 0)

    def test_remove_guards_unmerged(self):
        self.cli(["start", "featx"])
        path = self.base / "acme-featx"
        (path / "new.txt").write_text("work\n")
        git(["add", "-A"], path)
        git(["commit", "-qm", "unmerged work"], path)
        # unmerged commit present -> refuse without --force
        self.assertEqual(self.cli(["remove", "featx"]), 1)
        self.assertTrue(path.exists())
        # --force discards it
        self.assertEqual(self.cli(["remove", "featx", "--force"]), 0)
        self.assertFalse(path.exists())

    def test_remove_clean_merged_ok(self):
        self.cli(["start", "featx"])
        # nothing committed on the branch -> merged into main -> removable
        self.assertEqual(self.cli(["remove", "featx"]), 0)

    def test_land_refuses_from_main(self):
        # standing in the main tree, no feature arg -> refuse
        self.assertEqual(self.cli(["land"]), 1)


if __name__ == "__main__":
    unittest.main()
