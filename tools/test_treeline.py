"""Tests for tools/treeline.py and its adoption in the floor's summary (board
450/010 row 9). Real throwaway git trees, so each case is the state git leaves."""
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import treeline  # noqa: E402

IDENT = ["-c", "user.name=T", "-c", "user.email=t" + chr(64) + "example.invalid",
         "-c", "commit.gpgsign=false"]


class TreeLine(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix="treeline-test-")).resolve()
        self.addCleanup(shutil.rmtree, self.base, True)
        self.env = {k: v for k, v in os.environ.items()
                    if not k.startswith("GIT_") and k != treeline.ENV_OFF}
        self.env.update(GIT_CONFIG_NOSYSTEM="1", HOME=str(self.base))
        self._saved = dict(os.environ)
        os.environ.clear()
        os.environ.update(self.env)
        self.addCleanup(self._restore)

    def _restore(self):
        os.environ.clear()
        os.environ.update(self._saved)

    def git(self, repo, *args, check=True):
        r = subprocess.run(["git", *IDENT, "-C", str(repo), *args],
                           capture_output=True, text=True)
        if check:
            self.assertEqual(r.returncode, 0, r.stderr)
        return r

    def tree(self, name, branch="main"):
        root = self.base / name
        root.mkdir()
        self.git(root, "init", "-q", "-b", branch)
        (root / "f.txt").write_text("base\n")
        self.git(root, "add", "-A")
        self.git(root, "commit", "-qm", "base")
        return root

    def test_a_tree_names_itself_and_two_trees_differ(self):
        a, b = self.tree("alpha", "branch-a"), self.tree("beta", "branch-b")
        la, lb = treeline.line(a), treeline.line(b)
        self.assertTrue(la.startswith(f"  tree {a} · branch-a@"), la)
        self.assertNotEqual(la, lb)
        self.assertNotIn(str(a), lb)
        self.assertEqual(la, treeline.line(a))      # control: stable

    def test_cwd_does_not_move_the_answer(self):
        a, b = self.tree("alpha"), self.tree("beta")
        r = subprocess.run([sys.executable, str(TOOLS / "treeline.py"), str(a)],
                           cwd=str(b), capture_output=True, text=True, env=self.env)
        self.assertEqual(r.stdout.rstrip("\n"), treeline.line(a))

    def test_detached_head_says_so(self):
        a = self.tree("alpha")
        sha = self.git(a, "rev-parse", "HEAD").stdout.strip()
        self.git(a, "checkout", "-q", "--detach", sha)
        line = treeline.line(a)
        self.assertIn("detached@", line)
        self.assertNotIn("main@", line)

    def test_a_stopped_rebase_is_named(self):
        a = self.tree("alpha")
        self.git(a, "checkout", "-q", "-b", "side")
        (a / "c.txt").write_text("side\n")
        self.git(a, "add", "-A")
        self.git(a, "commit", "-qm", "side")
        self.git(a, "checkout", "-q", "main")
        (a / "c.txt").write_text("main\n")
        self.git(a, "add", "-A")
        self.git(a, "commit", "-qm", "main side")
        self.git(a, "checkout", "-q", "side")
        self.git(a, "rebase", "main", check=False)
        self.assertIn("REBASE IN PROGRESS", treeline.line(a))

    def test_a_worktree_is_marked_and_differs_from_its_parent(self):
        a = self.tree("alpha")
        wt = self.base / "alpha-wt"
        self.git(a, "worktree", "add", "-q", "-b", "wt-branch", str(wt))
        line = treeline.line(wt)
        self.assertIn(f"tree {wt} · wt-branch@", line)
        self.assertIn("· worktree", line)
        self.assertNotIn("worktree", treeline.line(a).replace(str(a), ""))

    def test_no_git_and_a_subdirectory_say_so(self):
        bare = self.base / "nogit"
        bare.mkdir()
        self.assertEqual(treeline.line(bare), f"  tree {bare} · not a git checkout")
        a = self.tree("alpha")
        (a / "sub").mkdir()
        self.assertIn(f"⚠ not the git root: {a}", treeline.line(a / "sub"))

    def test_tools_in_tree_or_named_with_their_own_head(self):
        a, b = self.tree("alpha"), self.tree("beta", "tools-branch")
        (a / "tools").mkdir()
        self.assertTrue(treeline.line(a, a / "tools").endswith("· tools in-tree"))
        line = treeline.line(a, b)
        self.assertIn(f"· tools {b} · tools-branch@", line)

    def test_the_switch_turns_it_off(self):
        os.environ[treeline.ENV_OFF] = "1"
        self.assertIsNone(treeline.line(self.tree("alpha")))

    def floor(self, *args, cwd):
        return subprocess.run([sys.executable, str(TOOLS / "floor.py"), "--plane", "ci",
                               *args], cwd=str(cwd), capture_output=True, text=True,
                              env=self.env, timeout=600)

    def test_the_floor_names_the_tree_it_read_after_its_coverage_line(self):
        a, b = self.tree("alpha"), self.tree("beta")
        (a / "docs").mkdir()
        r = self.floor("--root", str(a), "--tools", str(TOOLS), cwd=b)
        lines = r.stderr.splitlines()
        cov = next(i for i, ln in enumerate(lines) if ln.startswith("  coverage:"))
        self.assertTrue(lines[cov + 1].startswith(f"  tree {a} · main@"), r.stderr)
        self.assertIn(f"· tools {TOOLS}", lines[cov + 1])
        self.assertNotIn(str(b), r.stderr)

    def test_the_floor_line_changes_nothing_about_the_exit(self):
        a = self.tree("alpha")
        (a / "docs").mkdir()
        on = self.floor("--root", str(a), cwd=a)
        off_env = dict(self.env, **{treeline.ENV_OFF: "1"})
        off = subprocess.run([sys.executable, str(TOOLS / "floor.py"), "--plane", "ci",
                              "--root", str(a)], cwd=str(a), capture_output=True,
                             text=True, env=off_env, timeout=600)
        self.assertEqual(on.returncode, off.returncode)
        self.assertIn("  tree ", on.stderr)
        self.assertNotIn("  tree ", off.stderr)


if __name__ == "__main__":
    unittest.main()
