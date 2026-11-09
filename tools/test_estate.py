"""`estate.py`, and the three tools that take their answer from it.

The worktree cases use a real `git worktree add` on a fixture, because the
finding they pin (`320/180`) is exactly the gap between a real linked worktree
and the main checkout: same scanner, byte-identical files, opposite verdict.
The layout cases pin `320/660`: repos in group folders, one setting.
"""

import contextlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import estate
import pins

TOOLS = Path(__file__).resolve().parent


def _hermetic_env(**extra):
    env = {k: v for k, v in os.environ.items()
           if not k.startswith("GIT_") and k != estate.ENV_VAR}
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1", **extra)
    return env


def _git(cwd, *args):
    subprocess.run(
        ["git", "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",  # leakscan:allow:email: RFC-2606 fixture identity for a throwaway test repo
         "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null", *args],
        cwd=cwd, check=True, capture_output=True, env=_hermetic_env())


class Fixture(unittest.TestCase):
    """`<base>/parent/{main,sibling}` with a real worktree of `main` at
    `<base>/elsewhere/wt`, nowhere near the sibling."""

    def setUp(self):
        self.base = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.base, True)
        self.addCleanup(estate.forget)
        estate.forget()
        self.parent = self.base / "parent"
        self.sibling = self.parent / "sibling"
        (self.sibling / "docs").mkdir(parents=True)
        (self.sibling / "docs" / "target.md").write_text("# Target\n\nbody\n")
        self.main = self.parent / "main"
        (self.main / "docs").mkdir(parents=True)
        self.env = _hermetic_env()
        patcher = mock.patch.dict(os.environ, self.env, clear=True)
        patcher.start()
        self.addCleanup(patcher.stop)

    def commit_and_worktree(self):
        _git(self.main, "init", "-q")
        _git(self.main, "add", "-A")
        _git(self.main, "commit", "-q", "--allow-empty", "-m", "fixture")
        (self.base / "elsewhere").mkdir()
        self.wt = self.base / "elsewhere" / "wt"
        _git(self.main, "worktree", "add", "-q", "--detach", str(self.wt))

    def scan(self, tool, root):
        r = subprocess.run(
            [sys.executable, str(TOOLS / f"{tool}.py"), "--json",
             "--root", str(root), "docs"],
            capture_output=True, text=True, env=self.env, cwd=self.base)
        self.assertIn(r.returncode, (0, 1), r.stdout + r.stderr)
        return r.returncode, json.loads(r.stdout)

    @staticmethod
    def kinds(payload):
        return sorted(f.get("kind") or f.get("rule") for f in payload["findings"])


class MainCheckout(Fixture):
    def test_worktree_and_main_name_the_same_checkout(self):
        self.commit_and_worktree()
        self.assertEqual(estate.main_checkout(self.wt).resolve(), self.main)
        self.assertEqual(estate.main_checkout(self.main).resolve(), self.main)
        self.assertEqual(estate.parent(self.wt).resolve(), self.parent)

    def test_not_a_repo_falls_back_to_the_path_given(self):
        self.assertEqual(estate.main_checkout(self.base), self.base)

    def test_a_bare_repos_worktree_has_no_main_checkout_to_name(self):
        bare = self.base / "bare.git"
        _git(self.base, "init", "-q", "--bare", str(bare))
        self.assertEqual(estate.main_checkout(bare), bare)

    def test_a_hook_exporting_git_dir_does_not_redirect_the_answer(self):
        self.commit_and_worktree()
        other = self.base / "other"
        other.mkdir()
        _git(other, "init", "-q")
        with mock.patch.dict(os.environ, {"GIT_DIR": str(other / ".git")}):
            self.assertEqual(estate.main_checkout(self.wt).resolve(), self.main)


class TheSetting(Fixture):
    def test_unset_means_direct_siblings(self):
        self.commit_and_worktree()
        self.assertIsNone(estate.root_setting(self.main))

    def test_the_environment_names_the_root(self):
        with mock.patch.dict(os.environ, {estate.ENV_VAR: str(self.parent)}):
            self.assertEqual(estate.root_setting(self.main), self.parent)
            self.assertEqual(estate.parent(self.main), self.parent)

    def test_the_git_config_carries_it_where_the_environment_does_not_reach(self):
        self.commit_and_worktree()
        _git(self.main, "config", estate.GIT_CONFIG_KEY, str(self.parent))
        self.assertEqual(estate.root_setting(self.wt), self.parent)

    def test_a_value_that_is_not_an_absolute_directory_warns_and_is_ignored(self):
        err = io.StringIO()
        with mock.patch.dict(os.environ, {estate.ENV_VAR: "not/absolute"}), \
                contextlib.redirect_stderr(err):
            self.assertIsNone(estate.root_setting(self.main))
        self.assertIn("not an absolute directory", err.getvalue())


class ScannersFromAWorktree(Fixture):
    """Same content, same verdict, from the main checkout and from a worktree."""

    def test_pathscan_resolves_a_sibling_from_a_real_worktree(self):
        (self.main / "docs" / "a.md").write_text(
            "See `../sibling/docs/target.md` for the rule.\n")
        self.commit_and_worktree()
        self.assertEqual(
            (self.main / "docs" / "a.md").read_bytes(),
            (self.wt / "docs" / "a.md").read_bytes())

        main_rc, main_out = self.scan("pathscan", self.main)
        self.assertEqual((main_rc, main_out["findings"]), (0, []))
        wt_rc, wt_out = self.scan("pathscan", self.wt)
        self.assertEqual((wt_rc, wt_out["findings"]), (0, []),
                         "the worktree must agree with the main checkout")

    def test_pathscan_still_reports_a_real_miss_from_a_worktree(self):
        (self.main / "docs" / "a.md").write_text(
            "See `../sibling/docs/gone.md` for the rule.\n")
        self.commit_and_worktree()
        _, main_out = self.scan("pathscan", self.main)
        _, wt_out = self.scan("pathscan", self.wt)
        self.assertEqual(len(main_out["findings"]), 1)
        self.assertEqual(len(wt_out["findings"]), 1)

    def test_linkscan_gives_a_worktree_the_main_checkouts_verdict(self):
        (self.main / "docs" / "a.md").write_text(
            "A [link](../../sibling/docs/target.md).\n")
        self.commit_and_worktree()
        _, main_out = self.scan("linkscan", self.main)
        _, wt_out = self.scan("linkscan", self.wt)
        self.assertEqual(self.kinds(main_out), ["outside-root"])
        self.assertEqual(self.kinds(wt_out), ["outside-root"])

    def test_linkscan_allow_marker_for_outside_root_holds_in_a_worktree(self):
        (self.main / "docs" / "a.md").write_text(
            "A [link](../../sibling/docs/target.md). "
            "<!-- linkscan:allow:outside-root: a stated reason -->\n")
        self.commit_and_worktree()
        self.assertEqual(self.scan("linkscan", self.main)[0], 0)
        self.assertEqual(self.scan("linkscan", self.wt)[0], 0)

    def test_linkscan_still_reports_a_real_miss_from_a_worktree(self):
        (self.main / "docs" / "a.md").write_text(
            "A [link](../../sibling/docs/gone.md).\n")
        self.commit_and_worktree()
        self.assertEqual(self.kinds(self.scan("linkscan", self.wt)[1]),
                         ["missing-file"])

    def test_a_scan_root_below_the_repo_top_measures_from_the_repo_top(self):
        (self.main / "docs" / "a.md").write_text("nothing\n")
        (self.main / "sub" / "docs").mkdir(parents=True)
        (self.main / "sub" / "docs" / "b.md").write_text(
            "See `../../sibling/docs/target.md` for the rule.\n")
        self.commit_and_worktree()
        self.assertEqual(self.scan("pathscan", self.wt / "sub")[1]["findings"], [])


class GroupedLayout(Fixture):
    """`<root>/themeA/child` naming `../sibling`, with the sibling at the root
    or in another group: the physical path no longer exists, the setting finds it."""

    def setUp(self):
        super().setUp()
        self.child = self.parent / "themeA" / "child"
        (self.child / "docs").mkdir(parents=True)
        (self.child / ".git").mkdir()
        (self.child / "docs" / "a.md").write_text(
            "See `../sibling/docs/target.md` for the rule.\n")

    def test_without_the_setting_it_is_a_finding(self):
        self.assertEqual(len(self.scan("pathscan", self.child)[1]["findings"]), 1)

    def test_with_the_setting_the_sibling_is_found_at_the_root(self):
        self.env[estate.ENV_VAR] = str(self.parent)
        self.assertEqual(self.scan("pathscan", self.child)[1]["findings"], [])

    def test_with_the_setting_the_sibling_is_found_in_another_group(self):
        other = self.parent / "themeB"
        other.mkdir()
        self.sibling.rename(other / "sibling")
        self.env[estate.ENV_VAR] = str(self.parent)
        self.assertEqual(self.scan("pathscan", self.child)[1]["findings"], [])

    def test_a_sibling_inside_another_repo_is_not_a_landing(self):
        host = self.parent / "host"
        host.mkdir()
        (host / ".git").mkdir()
        self.sibling.rename(host / "sibling")
        self.env[estate.ENV_VAR] = str(self.parent)
        self.assertEqual(len(self.scan("pathscan", self.child)[1]["findings"]), 1)

    def test_linkscan_in_a_group_reports_outside_root_not_missing(self):
        (self.child / "docs" / "a.md").write_text(
            "A [link](../../sibling/docs/target.md).\n")
        self.env[estate.ENV_VAR] = str(self.parent)
        self.assertEqual(self.kinds(self.scan("linkscan", self.child)[1]),
                         ["outside-root"])


class DiscoverWalksGroups(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.base, True)
        self.addCleanup(estate.forget)
        patcher = mock.patch.dict(os.environ, _hermetic_env(), clear=True)
        patcher.start()
        self.addCleanup(patcher.stop)
        self.atelier = self.make_repo(self.base / "atelier", pin=False)
        self.make_repo(self.base / "standalone")
        self.make_repo(self.base / "themeA" / "grouped")
        self.make_repo(self.base / "themeA" / "unpinned", pin=False)
        (self.base / "themeA" / "notes").mkdir()
        (self.base / "themeB").mkdir()
        self.make_repo(self.base / "themeB" / "alpha")
        self.make_repo(self.base / ".cache" / "hidden")
        # A repo nested in a repo is not a child: repos are never descended.
        self.make_repo(self.base / "standalone" / "vendored")
        self.make_repo(self.base / "themeA" / "deep" / "toodeep")
        (self.base / "linked").symlink_to(self.base / "themeB")

    @staticmethod
    def make_repo(path, pin=True):
        (path / ".git").mkdir(parents=True)
        if pin:
            (path / "CLAUDE.md").write_text(
                "Pinned to atelier@deadbeef, see the floor.\n")
        return path

    def discover(self, **kwargs):
        err = io.StringIO()
        with contextlib.redirect_stderr(err):
            found = pins.discover([self.base], self.atelier, **kwargs)
        return {p.name for p in found}, err.getvalue()

    def test_pin_fixture_is_read_as_a_pin(self):
        self.assertIsNotNone(pins.read_pin(self.base / "standalone" / "CLAUDE.md"))

    def test_unset_stays_one_level_with_the_same_line(self):
        names, err = self.discover()
        self.assertEqual(names, {"standalone"})
        self.assertNotIn("grouped layout", err)
        self.assertRegex(err, r"searched .* — \d+ entries, 1 are git repos, "
                              r"1 carry an atelier pin")

    def test_set_walks_group_folders_one_level_deeper(self):
        with mock.patch.dict(os.environ, {estate.ENV_VAR: str(self.base)}):
            names, err = self.discover()
        self.assertEqual(names, {"standalone", "grouped", "alpha"})
        self.assertIn("walked 2 group folder(s)", err)
        self.assertIn("themeA (2)", err)
        self.assertIn("themeB (1)", err)
        # The funnel counts what it reached, and says what it did not.
        self.assertIn("4 are git repos, 3 carry an atelier pin", err)
        self.assertIn("skipped 2 hidden, symlinked or unreadable: .cache, linked",
                      err)
        self.assertIn("2 folder(s) inside a group are not repos", err)

    def test_explicit_grouped_flag_wins_over_the_setting(self):
        names, _ = self.discover(grouped=True)
        self.assertIn("grouped", names)
        with mock.patch.dict(os.environ, {estate.ENV_VAR: str(self.base)}):
            names, _ = self.discover(grouped=False)
        self.assertEqual(names, {"standalone"})

    def test_atelier_in_a_group_is_not_its_own_child(self):
        moved = self.base / "themeB" / "atelier"
        self.atelier.rename(moved)
        (moved / "CLAUDE.md").write_text("Pinned to atelier@deadbeef.\n")
        found = pins.discover([self.base], moved, quiet=True, grouped=True)
        self.assertNotIn(moved.resolve(), [p.resolve() for p in found])
        self.assertIn("alpha", {p.name for p in found})


if __name__ == "__main__":
    unittest.main()
