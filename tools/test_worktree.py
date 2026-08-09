"""Stdlib-only tests for worktree (no pytest needed): `python3 -m unittest`.

The command tests build real throwaway git repos under a tmp dir (never iCloud)
and drive worktree.py end-to-end, so the guards are proven against real git, not
mocks. The pure-logic guards (iCloud detection, feature validation) are unit-tested
directly and need no git."""

import contextlib
import io
import json
import os
import subprocess
import tempfile
import types
import unittest
from pathlib import Path

import worktree as wt


def git(args, cwd):
    subprocess.run(["git", *args], cwd=str(cwd), check=True,
                   capture_output=True, text=True)


def git_out(args, cwd):
    return subprocess.run(["git", *args], cwd=str(cwd), check=True,
                          capture_output=True, text=True).stdout.strip()


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


class _LocalRepoFixture:
    """A throwaway repo with no remote, cwd set to it. Mixed into TestCases so the
    fixture is shared without one class inheriting another's tests."""

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

    def cli_out(self, argv):
        """Run the CLI and return (rc, stdout) — for asserting on what it printed."""
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = self.cli(argv)
        return rc, buf.getvalue()


class CommandsOnRealRepo(_LocalRepoFixture, unittest.TestCase):
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


class CwdIndependence(_LocalRepoFixture, unittest.TestCase):
    """Every answer must be the same from the main checkout and from inside a
    linked worktree — the cwd a session is normally in when it lands work.

    Regression cover: `rev-parse --show-toplevel` was used as "the repo", so from
    inside a worktree `list` labelled it main and hid its ahead/behind counts, and
    land/remove/start built <repo>-<feature> from the worktree's own name.
    """

    def setUp(self):
        super().setUp()
        self.assertEqual(self.cli(["start", "featx"]), 0)
        self.linked = self.base / "acme-featx"
        for n in ("a", "b"):
            (self.linked / f"{n}.txt").write_text(f"{n}\n")
            git(["add", "-A"], self.linked)
            git(["commit", "-qm", f"work {n}"], self.linked)

    def json_list(self):
        rc, out = self.cli_out(["--json", "list"])
        self.assertEqual(rc, 0)
        return json.loads(out)

    def test_list_identical_from_both_cwds(self):
        from_main = self.json_list()
        os.chdir(self.linked)
        from_linked = self.json_list()
        self.assertEqual(from_main, from_linked)

    def test_list_from_linked_worktree_names_the_right_main(self):
        os.chdir(self.linked)
        rows = {Path(r["path"]).name: r for r in self.json_list()["worktrees"]}
        self.assertTrue(rows["acme"]["is_main"])
        self.assertFalse(rows["acme-featx"]["is_main"])
        self.assertEqual(rows["acme-featx"]["branch"], "featx")
        # the counts the bug dropped
        self.assertEqual((rows["acme-featx"]["ahead"], rows["acme-featx"]["behind"]),
                         (2, 0))

    def test_list_from_main_checkout_still_correct(self):
        rows = {Path(r["path"]).name: r for r in self.json_list()["worktrees"]}
        self.assertTrue(rows["acme"]["is_main"])
        self.assertFalse(rows["acme-featx"]["is_main"])
        self.assertEqual((rows["acme-featx"]["ahead"], rows["acme-featx"]["behind"]),
                         (2, 0))

    def test_render_shows_counts_for_linked_worktree(self):
        os.chdir(self.linked)
        rc, out = self.cli_out(["list"])
        self.assertEqual(rc, 0)
        self.assertIn("featx", out)
        self.assertIn("↑2 ↓0", out)

    def test_feature_lookup_from_both_cwds(self):
        args = types.SimpleNamespace(feature="featx")
        for cwd in (self.repo, self.linked):
            os.chdir(cwd)
            found = wt._feature_worktree(wt.toplevel(Path.cwd()), args)
            self.assertIsNotNone(found, f"not found from {cwd}")
            self.assertEqual(Path(found["path"]).name, "acme-featx")
            self.assertEqual(found["branch"], "featx")

    def test_start_from_linked_worktree_uses_the_repo_name(self):
        os.chdir(self.linked)
        self.assertEqual(self.cli(["start", "second"]), 0)
        self.assertTrue((self.base / "acme-second").exists())
        self.assertFalse((self.base / "acme-featx-second").exists())
        # and the slug it printed actually resolves afterwards
        self.assertIsNotNone(
            wt._feature_worktree(wt.toplevel(Path.cwd()),
                                 types.SimpleNamespace(feature="second")))

    def test_land_resolves_feature_from_linked_worktree(self):
        # No remote in this fixture, so a resolved worktree takes the
        # reconcile-locally path (rc 0). The bug returned 1, "no worktree found".
        os.chdir(self.linked)
        rc, out = self.cli_out(["land", "featx"])
        self.assertEqual(rc, 0)
        self.assertIn("no remote configured", out)
        # the local-merge hint must name the main checkout, not the worktree
        self.assertIn(str(wt.toplevel(self.repo)), out)

    def test_land_still_resolves_feature_from_main_checkout(self):
        rc, out = self.cli_out(["land", "featx"])
        self.assertEqual(rc, 0)
        self.assertIn("no remote configured", out)

    def test_remove_refuses_unmerged_from_linked_worktree(self):
        os.chdir(self.linked)
        self.assertEqual(self.cli(["remove", "featx"]), 1)
        self.assertTrue(self.linked.exists())


class MergedGuardReferent(unittest.TestCase):
    """`remove`'s unmerged guard must measure against the *remote* integration
    branch too: `git push <branch>:main` moves origin/main and leaves local main
    where it was, and the guard called that landed work unmerged.

    The guard must not get weaker — genuinely unlanded work is still refused, and
    a repo with no integration ref at all refuses rather than assumes.
    """

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix="wt-test-")
        self.remote = Path(self.tmp) / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", "-b", "main", str(self.remote)],
                       check=True, capture_output=True)
        self.repo = Path(self.tmp) / "acme"
        subprocess.run(["git", "clone", "-q", str(self.remote), str(self.repo)],
                       check=True, capture_output=True)
        git(["config", "user.email", "t@example.com"], self.repo)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], self.repo)
        (self.repo / "README.md").write_text("seed\n")
        git(["add", "-A"], self.repo)
        git(["commit", "-qm", "seed"], self.repo)
        git(["push", "-q", "-u", "origin", "main"], self.repo)
        self.base = Path(self.tmp) / "worktrees"
        self._cwd = os.getcwd()
        os.chdir(self.repo)

    def tearDown(self):
        os.chdir(self._cwd)
        subprocess.run(["rm", "-rf", self.tmp])

    def cli(self, argv):
        return wt.main(["--base", str(self.base)] + argv)

    def _branch_with_a_commit(self, feature):
        self.assertEqual(self.cli(["start", feature]), 0)
        path = self.base / f"acme-{feature}"
        (path / f"{feature}.txt").write_text("work\n")
        git(["add", "-A"], path)
        git(["commit", "-qm", f"{feature} work"], path)
        return path

    def test_integration_refs_prefer_the_remote_branch(self):
        # remote first, local second — both count as landed
        self.assertEqual(wt.integration_refs(self.repo, "main"), ["origin/main", "main"])
        # a name with no ref either side contributes nothing
        self.assertEqual(wt.integration_refs(self.repo, "nope"), [])

    def test_is_merged_with_no_refs_is_false(self):
        # fail safe, not fail open: nothing to compare against => not merged
        self.assertFalse(wt.is_merged(self.repo, "HEAD", []))

    def test_remove_allows_branch_landed_only_on_origin_main(self):
        path = self._branch_with_a_commit("pushed")
        git(["push", "-q", "origin", "HEAD:main"], path)
        # local main has NOT moved — that is the whole condition
        self.assertNotEqual(git_out(["rev-parse", "main"], self.repo),
                            git_out(["rev-parse", "origin/main"], self.repo))
        self.assertEqual(self.cli(["remove", "pushed"]), 0)
        self.assertFalse(path.exists())

    def test_remove_still_refuses_genuinely_unmerged(self):
        path = self._branch_with_a_commit("unlanded")
        self.assertEqual(self.cli(["remove", "unlanded"]), 1)
        self.assertTrue(path.exists())

    def test_remove_allows_branch_merged_into_local_main_only(self):
        # a local merge that has not been pushed has still landed
        path = self._branch_with_a_commit("localmerge")
        git(["merge", "-q", "--no-edit", "localmerge"], self.repo)
        self.assertEqual(self.cli(["remove", "localmerge"]), 0)
        self.assertFalse(path.exists())

    def test_remove_refuses_when_no_integration_ref_exists(self):
        # Fresh repo whose default branch is neither main nor master, and no
        # remote: nothing to measure containment against, so refuse.
        solo = Path(self.tmp) / "solo"
        subprocess.run(["git", "init", "-q", "-b", "trunk", str(solo)],
                       check=True, capture_output=True)
        git(["config", "user.email", "t@example.com"], solo)  # leakscan:allow: fictional test fixture
        git(["config", "user.name", "Test"], solo)
        (solo / "f.txt").write_text("x\n")
        git(["add", "-A"], solo)
        git(["commit", "-qm", "seed"], solo)
        linked = self.base / "solo-featx"
        git(["worktree", "add", "-q", "-b", "featx", str(linked), "trunk"], solo)
        self.assertEqual(wt.integration_branch(solo), "main")
        self.assertEqual(wt.integration_refs(solo, "main"), [])
        os.chdir(solo)
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            rc = self.cli(["remove", "featx"])
        self.assertEqual(rc, 1)
        self.assertIn("cannot be verified as merged", buf.getvalue())
        self.assertTrue(linked.exists())


if __name__ == "__main__":
    unittest.main()
