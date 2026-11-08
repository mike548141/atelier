"""Stdlib-only tests for filewalk (`110`: guards walk untracked trees).

Git mode (streamed `git ls-files`), the `os.walk` fallback, files deleted from
the tree but still in the index, gitignored files, and `skip_dir_names` under
git mode. Fixtures are synthetic.
"""

import os
import shutil
import subprocess
import tempfile
import unittest
from unittest import mock
from pathlib import Path

import filewalk

SKIP = {".git", "node_modules"}


def git(cwd, *args):
    subprocess.run(["git", *args], cwd=cwd, check=True, capture_output=True)


def walk(root, skip=SKIP):
    return sorted(str(p.relative_to(root)) for p in filewalk.walk_files(root, skip))


class GitTreeCase(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)
        git(self.tmp, "init", "-q")
        git(self.tmp, "config", "user.email", "t" + chr(64) + "x.invalid")
        git(self.tmp, "config", "user.name", "t")

    def put(self, rel, text="x\n"):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p


class TestGitMode(GitTreeCase):
    def test_tracked_and_untracked_unignored_yielded(self):
        self.put("tracked.txt"); self.put("sub/also.txt")
        git(self.tmp, "add", "."); git(self.tmp, "commit", "-qm", "i")
        self.put("new.txt")
        self.assertEqual(walk(self.tmp), ["new.txt", "sub/also.txt", "tracked.txt"])
        self.assertEqual(filewalk.LAST_MODE, "git")

    def test_ignored_files_and_dirs_not_read(self):
        self.put(".gitignore", "junk/\n*.log\n")
        self.put("keep.txt"); self.put("junk/a.bin"); self.put("junk/deep/b.bin"); self.put("x.log")
        self.assertEqual(walk(self.tmp), [".gitignore", "keep.txt"])

    def test_walk_does_not_touch_ignored_tree(self):
        self.put(".gitignore", "junk/\n"); self.put("junk/a.bin"); self.put("keep.txt")
        with mock.patch("os.walk", side_effect=AssertionError("os.walk used")):
            self.assertEqual(walk(self.tmp), [".gitignore", "keep.txt"])

    def test_deleted_but_cached_file_skipped(self):
        gone = self.put("gone.txt"); self.put("here.txt")
        git(self.tmp, "add", "."); git(self.tmp, "commit", "-qm", "i")
        gone.unlink()
        self.assertEqual(walk(self.tmp), ["here.txt"])

    def test_skip_dir_names_hold_in_git_mode(self):
        self.put("node_modules/m.js"); self.put("a/node_modules/n.js"); self.put("ok.txt")
        self.put("a/build/b.txt")
        git(self.tmp, "add", "-f", ".")
        self.assertEqual(walk(self.tmp), ["a/build/b.txt", "ok.txt"])
        # the skip set is a per-guard parameter
        self.assertEqual(walk(self.tmp, SKIP | {"build"}), ["ok.txt"])

    def test_symlinks_match_os_walk(self):
        self.put("t.txt"); (self.tmp / "d").mkdir()
        os.symlink("t.txt", self.tmp / "to-file")
        os.symlink("d", self.tmp / "to-dir")
        os.symlink("nowhere", self.tmp / "broken")
        got = walk(self.tmp)
        self.assertEqual(got, ["t.txt", "to-file"])
        self.assertEqual(got, sorted(str(p.relative_to(self.tmp))
                                     for p in filewalk._os_walk(self.tmp, SKIP)
                                     if ".git" not in p.parts))

    def test_nested_plain_clone_still_read(self):
        n = self.tmp / "nested"; n.mkdir()
        git(n, "init", "-q")
        self.put("nested/n.txt"); self.put("nested/node_modules/skipped.js")
        self.put("top.txt")
        self.assertEqual(walk(self.tmp), ["nested/n.txt", "top.txt"])

    def test_linked_worktree_pruned(self):
        self.put("a.txt"); git(self.tmp, "add", "."); git(self.tmp, "commit", "-qm", "i")
        git(self.tmp, "worktree", "add", "-q", str(self.tmp / "wt"), "-b", "w")
        self.assertEqual(walk(self.tmp), ["a.txt"])

    def test_unicode_and_odd_names_unquoted(self):
        self.put("tōhutō kōrero.txt"); self.put("sp ace/\"q\".txt")
        self.assertEqual(walk(self.tmp), sorted(["tōhutō kōrero.txt", "sp ace/\"q\".txt"]))

    def test_subdirectory_root_lists_only_that_subtree(self):
        self.put("sub/in.txt"); self.put("out.txt")
        self.assertEqual(walk(self.tmp / "sub"), ["in.txt"])

    def test_ignored_root_falls_back_visibly(self):
        self.put(".gitignore", "junk/\n"); self.put("junk/a.txt")
        self.assertEqual(walk(self.tmp / "junk"), ["a.txt"])
        self.assertEqual(filewalk.LAST_MODE, "os.walk:root-ignored")

    def test_git_failure_mid_stream_raises(self):
        self.put("a.txt")
        real = filewalk.subprocess.Popen

        def bad(cmd, **kw):
            return real(["sh", "-c", "printf 'a.txt\\0'; echo boom >&2; exit 3"],
                        **{k: v for k, v in kw.items() if k != "env"})
        with mock.patch.object(filewalk.subprocess, "Popen", bad), \
                mock.patch.object(filewalk, "_git_unusable", return_value=""):
            with self.assertRaises(RuntimeError):
                list(filewalk.walk_files(self.tmp, SKIP))


class TestTrackedUnderSkipNames(GitTreeCase):
    """GW1 (160/600): the three boundary guards must read a TRACKED file even
    under a skip-named directory; every other guard keeps the skip."""

    NAMES = ["node_modules/m.js", "a/node_modules/n.js", ".vscode/settings.json",
             "venv/lib/x.py", "a/.idea/w.xml"]

    def _commit_forced(self):
        for n in self.NAMES:
            self.put(n)
        self.put("ok.txt")
        git(self.tmp, "add", "-f", ".")

    def test_default_still_skips_tracked_files_under_skip_names(self):
        self._commit_forced()
        skip = SKIP | {".vscode", "venv", ".idea"}
        self.assertEqual(walk(self.tmp, skip), ["ok.txt"])

    def test_flag_yields_tracked_files_under_every_skip_name(self):
        self._commit_forced()
        skip = SKIP | {".vscode", "venv", ".idea"}
        got = sorted(str(p.relative_to(self.tmp)) for p in
                     filewalk.walk_files(self.tmp, skip, read_tracked_under_skip=True))
        self.assertEqual(got, sorted(self.NAMES + ["ok.txt"]))

    def test_flag_leaves_untracked_files_under_skip_names_skipped(self):
        self.put("tracked.txt"); git(self.tmp, "add", "tracked.txt")
        self.put("node_modules/untracked.js"); self.put(".vscode/u.json")
        got = sorted(str(p.relative_to(self.tmp)) for p in
                     filewalk.walk_files(self.tmp, SKIP | {".vscode"},
                                         read_tracked_under_skip=True))
        self.assertEqual(got, ["tracked.txt"])

    def test_flag_does_not_widen_a_nested_walk(self):
        n = self.tmp / "nested"; n.mkdir(); git(n, "init", "-q")
        self.put("nested/n.txt"); self.put("nested/node_modules/skipped.js")
        got = sorted(str(p.relative_to(self.tmp)) for p in
                     filewalk.walk_files(self.tmp, SKIP, read_tracked_under_skip=True))
        self.assertEqual(got, ["nested/n.txt"])

    def test_boundary_guards_pass_the_flag_and_the_rest_do_not(self):
        """The decision is per guard: pin which ones."""
        import importlib
        for name, want in (("secretscan", True), ("leakscan", True),
                           ("conflictscan", True), ("datescan", False),
                           ("pathscan", False), ("licenscan", False)):
            mod = importlib.import_module(name)
            seen = {}

            def fake(base, skip, read_tracked_under_skip=False, _s=seen):
                _s["flag"] = read_tracked_under_skip
                return iter(())
            with mock.patch.object(filewalk, "walk_files", fake):
                list(mod._walk_files(self.tmp))
            self.assertIs(seen["flag"], want, name)

    def test_secretscan_whole_tree_reads_a_secret_under_a_skip_name(self):
        """The end-to-end shape of GW1: synthetic credential, tracked under
        `.vscode`, whole-tree plane."""
        import secretscan
        key = "AKIA" + "ABCDEFGHIJKLMNOP"
        self.put(".vscode/settings.json", '{"aws": "%s"}\n' % key)
        self.put("plain/settings.json", '{"aws": "%s"}\n' % key)
        git(self.tmp, "add", "-f", ".")
        found = sorted(p.relative_to(self.tmp).as_posix()
                       for p in secretscan._walk_files(self.tmp))
        self.assertIn(".vscode/settings.json", found)


class TestWalkContract(GitTreeCase):
    """GW3: the three behaviours the module relied on with no test, and the
    property the design rests on."""

    def test_force_added_past_an_ignore_rule_is_yielded(self):
        self.put(".gitignore", "secret.env\n")
        self.put("secret.env", "k=v\n")
        git(self.tmp, "add", "-f", "secret.env", ".gitignore")
        self.assertEqual(walk(self.tmp), [".gitignore", "secret.env"])

    def test_environment_scrub_ignores_an_inherited_git_dir(self):
        other = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, other, True)
        git(other, "init", "-q")
        self.put("here.txt")
        env = {"GIT_DIR": str(other / ".git"), "GIT_WORK_TREE": str(other),
               "GIT_INDEX_FILE": str(other / ".git" / "index")}
        with mock.patch.dict(os.environ, env):
            self.assertEqual(walk(self.tmp), ["here.txt"])
        self.assertEqual(filewalk.LAST_MODE, "git")

    def test_unmerged_paths_are_yielded_once(self):
        self.put("c.txt", "base\n"); git(self.tmp, "add", "."); git(self.tmp, "commit", "-qm", "b")
        git(self.tmp, "checkout", "-qb", "side")
        self.put("c.txt", "side\n"); git(self.tmp, "commit", "-qam", "s")
        git(self.tmp, "checkout", "-q", "-")
        self.put("c.txt", "main\n"); git(self.tmp, "commit", "-qam", "m")
        subprocess.run(["git", "merge", "side"], cwd=self.tmp, capture_output=True)
        out = subprocess.run(["git", "ls-files", "-u"], cwd=self.tmp,
                             capture_output=True, text=True).stdout
        self.assertGreaterEqual(len(out.splitlines()), 2, "fixture must be unmerged")
        got = [p.name for p in filewalk.walk_files(self.tmp, SKIP)]
        self.assertEqual(got.count("c.txt"), 1)

    def test_tracked_directory_whose_dot_git_is_a_file_is_pruned(self):
        self.put("sub/a.txt"); self.put("ok.txt")
        git(self.tmp, "add", "."); git(self.tmp, "commit", "-qm", "i")
        (self.tmp / "sub/.git").write_text("gitdir: /elsewhere\n")
        self.assertEqual(walk(self.tmp), ["ok.txt"])
        got = sorted(str(p.relative_to(self.tmp)) for p in
                     filewalk.walk_files(self.tmp, SKIP, read_tracked_under_skip=True))
        self.assertEqual(got, ["ok.txt"])


class TestSymlinkedParent(GitTreeCase):
    """GW4: git indexes `d/f.txt`; the worktree swaps `d` for a link out."""

    def test_a_path_through_a_symlinked_parent_is_not_yielded(self):
        outside = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, outside, True)
        (outside / "f.txt").write_text("outside\n")
        self.put("d/f.txt"); self.put("ok.txt")
        git(self.tmp, "add", "."); git(self.tmp, "commit", "-qm", "i")
        shutil.rmtree(self.tmp / "d")
        os.symlink(outside, self.tmp / "d")
        self.assertEqual(walk(self.tmp), ["ok.txt"])
        for flag in (False, True):
            got = [p for p in filewalk.walk_files(self.tmp, SKIP, read_tracked_under_skip=flag)]
            self.assertNotIn(outside / "f.txt", got)
            self.assertFalse(any("d" in p.relative_to(self.tmp).parts for p in got))

    def test_a_symlink_leaf_to_a_file_is_still_yielded(self):
        self.put("t.txt"); os.symlink("t.txt", self.tmp / "to-file")
        self.assertEqual(walk(self.tmp), ["t.txt", "to-file"])

    def test_a_symlinked_root_is_still_walked(self):
        self.put("r.txt")
        link = self.tmp.parent / (self.tmp.name + "-link")
        os.symlink(self.tmp, link)
        self.addCleanup(link.unlink)
        self.assertEqual(sorted(p.name for p in filewalk.walk_files(link, SKIP)), ["r.txt"])


class TestTreeConfiguredCommands(GitTreeCase):
    """GW5: scanning a tree must not execute a command its config names."""

    def test_core_fsmonitor_in_the_trees_config_is_not_run(self):
        proof = self.tmp.parent / (self.tmp.name + "-ran")
        hook = self.tmp.parent / (self.tmp.name + "-hook.sh")
        hook.write_text("#!/bin/sh\ntouch '%s'\nexit 0\n" % proof)
        hook.chmod(0o755)
        self.addCleanup(lambda: [x.unlink() for x in (hook, proof) if x.exists()])
        git(self.tmp, "config", "core.fsmonitor", str(hook))
        self.put("a.txt")
        # the control: git itself runs the command for an ordinary call
        subprocess.run(["git", "ls-files", "--others"], cwd=self.tmp,
                       capture_output=True)
        if not proof.exists():
            self.skipTest("this git does not run core.fsmonitor for ls-files")
        proof.unlink()
        self.assertEqual(walk(self.tmp), ["a.txt"])
        self.assertFalse(proof.exists(), "the walk ran the tree's fsmonitor")


class TestFallbackVoice(GitTreeCase):
    """GW2: "git says no repository" is silent; "git failed" speaks."""

    def setUp(self):
        super().setUp()
        filewalk._WARNED.discard("failed")

    def test_plain_non_repository_is_silent(self):
        plain = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, plain, True)
        (plain / "f.txt").write_text("x")
        with mock.patch("sys.stderr") as err:
            self.assertEqual(walk(plain), ["f.txt"])
        self.assertEqual(filewalk.LAST_MODE, "os.walk:not-in-git-tree")
        self.assertFalse(err.write.called)

    def test_a_corrupt_head_is_a_voiced_failure_not_no_repository(self):
        self.put("f.txt")
        (self.tmp / ".git" / "HEAD").write_text("garbage\n")
        import io
        buf = io.StringIO()
        with mock.patch("sys.stderr", buf):
            self.assertEqual(walk(self.tmp), ["f.txt"])
            self.assertEqual(walk(self.tmp), ["f.txt"])
        self.assertEqual(filewalk.LAST_MODE, "os.walk:git-failed")
        self.assertEqual(buf.getvalue().count("could not enumerate"), 1, "once")
        self.assertIn("walking the whole directory tree", buf.getvalue())

    def test_a_refused_repository_is_a_voiced_failure(self):
        """Dubious ownership, simulated: git exits non-zero for a tree that
        carries a `.git` entry."""
        self.put("f.txt")
        real = filewalk.subprocess.run

        def refuse(cmd, **kw):
            if "rev-parse" in cmd:
                return subprocess.CompletedProcess(
                    cmd, 128, b"", b"fatal: detected dubious ownership in repository\n")
            return real(cmd, **kw)
        import io
        buf = io.StringIO()
        with mock.patch.object(filewalk.subprocess, "run", refuse), \
                mock.patch("sys.stderr", buf):
            self.assertEqual(walk(self.tmp), ["f.txt"])
        self.assertEqual(filewalk.LAST_MODE, "os.walk:git-failed")
        self.assertIn("dubious ownership", buf.getvalue())


class TestShapeMatrix(GitTreeCase):
    """Seeded question 1 (160/600): "the set is right", not only "smaller".
    One repository holding every shape the parent and git modes could
    differ on; the expected set is written out, not derived."""

    def test_the_yielded_set_over_every_shape(self):
        self.put(".gitignore", "ignored/\n*.log\n")
        self.put("tracked.txt"); self.put("sub/tracked2.txt")
        self.put("node_modules/tracked-skip.js")
        git(self.tmp, "add", "-f", "tracked.txt", "sub/tracked2.txt",
            "node_modules/tracked-skip.js", ".gitignore")
        git(self.tmp, "commit", "-qm", "i")
        self.put("untracked.txt"); self.put("sub/untracked2.txt")
        self.put("ignored/a.bin"); self.put("x.log")
        self.put("node_modules/untracked-skip.js")
        self.put("forced.log"); git(self.tmp, "add", "-f", "forced.log")
        gone = self.put("gone.txt"); git(self.tmp, "add", "gone.txt"); gone.unlink()
        os.symlink("tracked.txt", self.tmp / "link-to-file")
        os.symlink("sub", self.tmp / "link-to-dir")
        os.symlink("nowhere", self.tmp / "broken")
        n = self.tmp / "nested"; n.mkdir(); git(n, "init", "-q")
        self.put("nested/n.txt"); self.put("nested/ignored-in-nested.txt")
        (self.tmp / "wt").mkdir(); (self.tmp / "wt/.git").write_text("gitdir: x\n")
        self.put("wt/w.txt")
        base = [".gitignore", "forced.log", "link-to-file", "nested/ignored-in-nested.txt",
                "nested/n.txt", "sub/tracked2.txt", "sub/untracked2.txt", "tracked.txt",
                "untracked.txt"]
        self.assertEqual(walk(self.tmp), base)
        got = sorted(str(p.relative_to(self.tmp)) for p in
                     filewalk.walk_files(self.tmp, SKIP, read_tracked_under_skip=True))
        self.assertEqual(got, sorted(base + ["node_modules/tracked-skip.js"]))


class TestFallback(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def test_non_git_tree_uses_os_walk(self):
        (self.tmp / "a").mkdir(); (self.tmp / "a/f.txt").write_text("x")
        (self.tmp / "node_modules").mkdir(); (self.tmp / "node_modules/n.js").write_text("x")
        self.assertEqual(walk(self.tmp), ["a/f.txt"])
        self.assertEqual(filewalk.LAST_MODE, "os.walk:not-in-git-tree")

    def test_git_missing_falls_back_and_says_so(self):
        (self.tmp / "f.txt").write_text("x")
        filewalk._WARNED.discard("unavailable")
        with mock.patch.object(filewalk.subprocess, "run", side_effect=FileNotFoundError("git")):
            with mock.patch("sys.stderr") as err:
                self.assertEqual(walk(self.tmp), ["f.txt"])
        self.assertEqual(filewalk.LAST_MODE, "os.walk:git-unavailable")
        self.assertTrue(err.write.called)

    def test_linked_worktree_dir_pruned_in_fallback(self):
        (self.tmp / "wt").mkdir(); (self.tmp / "wt/.git").write_text("gitdir: x\n")
        (self.tmp / "wt/f.txt").write_text("x"); (self.tmp / "ok.txt").write_text("x")
        self.assertEqual(walk(self.tmp), ["ok.txt"])


if __name__ == "__main__":
    unittest.main()
