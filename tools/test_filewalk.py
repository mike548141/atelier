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
