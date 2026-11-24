"""Tests for deadhook.py (board 450/010 row 8): the dead-hook check and the
"are hooks on?" status, answered from the primary checkout and from a worktree.

Every repo is a fresh `git init` under a scratch directory, and every subprocess
runs with a scrubbed environment (no global or system git config, HOME inside
the scratch, no inherited GIT_*), so nothing here reads or touches a real
clone's config. ATELIER_TOOLS points at a fake directory holding an empty
floor.py. Carried over from the first-built copy's selftest: every case but its
negative control, which ran that copy's own pre-fix revision from its own
history and has no equivalent here."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOL = Path(__file__).resolve().parent / "deadhook.py"
FAKE_EMAIL = "selftest" + chr(64) + "example.invalid"
HOOK = "#!/bin/sh\n# the primary checkout's copy\nexit 0\n"
FLOOR = ("pre-commit", "pre-merge-commit", "commit-msg")


class Fix:
    """A scratch repo `main/` with tracked floor hooks, and a linked worktree
    `wt/`. `core.hooksPath` is armed ABSOLUTE on main's `.githooks`, the shape
    that makes the worktree case differ from the primary."""

    def __init__(self, base: Path, name: str):
        self.dir = (base / name).resolve()
        self.main = self.dir / "main"
        self.wt = self.dir / "wt"
        self.tools = self.dir / "atelier-tools"
        env = {k: v for k, v in os.environ.items()
               if not k.startswith("GIT_") and k not in ("ATELIER_TOOLS", "HOME")}
        env.update(HOME=str(self.dir), GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_NOSYSTEM="1",
                   GIT_AUTHOR_NAME="selftest", GIT_AUTHOR_EMAIL=FAKE_EMAIL,
                   GIT_COMMITTER_NAME="selftest", GIT_COMMITTER_EMAIL=FAKE_EMAIL,
                   ATELIER_TOOLS=str(self.tools))
        self.env = env
        self.tools.mkdir(parents=True)
        (self.tools / "floor.py").write_text("")
        self.main.mkdir()
        self.git(self.main, "init", "-q", "-b", "main")
        hooks = self.main / ".githooks"
        hooks.mkdir()
        for name in FLOOR:
            (hooks / name).write_text(HOOK)
            (hooks / name).chmod(0o755)
        self.git(self.main, "add", ".githooks")
        self.git(self.main, "commit", "-q", "-m", "init")
        self.git(self.main, "worktree", "add", "-q", "-b", "wt", str(self.wt))
        self.git(self.main, "config", "core.hooksPath", str(hooks))

    def git(self, cwd: Path, *args: str) -> str:
        r = subprocess.run(["git", *args], cwd=cwd, env=self.env, capture_output=True, text=True)
        assert r.returncode == 0, f"git {args} in {cwd}: {r.stderr}"
        return r.stdout.strip()

    def run(self, cwd: Path, *args: str, env: dict | None = None):
        r = subprocess.run([sys.executable, str(TOOL), *args], cwd=cwd, env=env or self.env,
                           capture_output=True, text=True, timeout=60)
        return r.returncode, r.stdout, r.stderr

    def status(self, cwd: Path, **kw):
        return self.run(cwd, "--status", **kw)


class Base(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix="deadhook-test-")).resolve()

    def tearDown(self):
        shutil.rmtree(self.base, ignore_errors=True)

    def fix(self, name="f"):
        return Fix(self.base, name)


class Worktrees(Base):
    def test_primary_answers_and_says_nothing_about_another_tree(self):
        f = self.fix()
        rc, out, err = f.status(f.main)
        self.assertEqual((rc, err), (0, ""), out)
        self.assertIn("is executable", out)
        self.assertIn("all set: commits here are scanned", out)
        self.assertNotIn("⚠️", out)
        self.assertNotIn("PRIMARY", out)
        self.assertNotIn("another work tree", out)

    def test_worktree_names_the_primary_as_the_armed_hook(self):
        f = self.fix()
        rc, out, err = f.status(f.wt)
        self.assertEqual((rc, err), (0, ""), out)
        self.assertIn(f"the PRIMARY checkout's copy ({f.main}/.githooks/pre-commit), not this tree's", out)
        self.assertIn("byte-identical", out)
        self.assertNotIn("⚠️", out)

    def test_worktree_with_an_edited_hook_is_warned_not_failed(self):
        f = self.fix()
        (f.wt / ".githooks" / "pre-commit").write_text(HOOK + "# edited in the worktree\n")
        rc, out, _ = f.status(f.wt)
        self.assertEqual(rc, 0, out)
        self.assertIn("⚠️ this tree's .githooks/pre-commit DIFFERS from the armed hook", out)
        self.assertIn("NOT what runs when you commit here", out)
        self.assertIn(f"diff {f.main}/.githooks/pre-commit {f.wt}/.githooks/pre-commit", out)
        self.assertIn("but see ⚠️ above", out)

    def test_the_difference_is_only_reported_from_the_tree_that_differs(self):
        f = self.fix()
        (f.wt / ".githooks" / "pre-commit").write_text(HOOK + "# edited\n")
        rc, out, _ = f.status(f.main)
        self.assertEqual(rc, 0)
        self.assertNotIn("DIFFERS", out)
        self.assertNotIn("⚠️", out)

    def test_a_one_byte_difference_is_caught(self):
        f = self.fix()
        (f.wt / ".githooks" / "pre-commit").write_text(HOOK.rstrip("\n"))
        rc, out, _ = f.status(f.wt)
        self.assertEqual(rc, 0)
        self.assertIn("DIFFERS", out)

    def test_worktree_without_the_hook_file_is_warned(self):
        f = self.fix()
        (f.wt / ".githooks" / "pre-commit").unlink()
        rc, out, _ = f.status(f.wt)
        self.assertEqual(rc, 0)
        self.assertIn("has no .githooks/pre-commit to compare", out)

    def test_a_real_commit_in_the_worktree_runs_the_primarys_hook(self):
        # The claim the warning rests on, proved with git rather than assumed.
        f = self.fix()
        mark = f.dir / "which-hook-ran"
        for tree, label in ((f.main, "PRIMARY-COPY"), (f.wt, "WORKTREE-EDIT")):
            p = tree / ".githooks" / "pre-commit"
            p.write_text(f'#!/bin/sh\necho {label} > "{mark}"\nexit 0\n')
            p.chmod(0o755)
        (f.wt / "change.txt").write_text("x\n")
        f.git(f.wt, "add", "change.txt")
        f.git(f.wt, "commit", "-q", "-m", "change")
        self.assertEqual(mark.read_text().strip(), "PRIMARY-COPY")
        rc, out, _ = f.status(f.wt)
        self.assertEqual(rc, 0)
        self.assertIn("DIFFERS", out)

    def test_relative_hooks_path_means_each_tree_runs_its_own_copy(self):
        f = self.fix()
        f.git(f.main, "config", "core.hooksPath", ".githooks")
        (f.wt / ".githooks" / "pre-commit").write_text(HOOK + "# edited\n")
        for tree in (f.main, f.wt):
            rc, out, err = f.status(tree)
            self.assertEqual((rc, err), (0, ""), out)
            self.assertIn("(.githooks/pre-commit is executable)", out)
            for absent in ("PRIMARY", "DIFFERS", "⚠️"):
                self.assertNotIn(absent, out)

    def test_hook_armed_in_a_third_tree_is_named_as_another_work_tree(self):
        f = self.fix()
        third = f.dir / "third"
        f.git(f.main, "worktree", "add", "-q", "-b", "third", str(third))
        f.git(f.main, "config", "core.hooksPath", str(third / ".githooks"))
        rc, out, _ = f.status(f.wt)
        self.assertEqual(rc, 0)
        self.assertIn(f"another work tree's copy ({third}/.githooks/pre-commit)", out)
        self.assertNotIn("PRIMARY", out)
        rc, out, _ = f.status(third)
        self.assertNotIn("another work tree", out)
        self.assertNotIn("PRIMARY", out)

    def test_hook_armed_outside_every_tree_is_said_plainly(self):
        f = self.fix()
        elsewhere = f.dir / "elsewhere"
        elsewhere.mkdir()
        for name in FLOOR:
            (elsewhere / name).write_text(HOOK)
            (elsewhere / name).chmod(0o755)
        f.git(f.main, "config", "core.hooksPath", str(elsewhere))
        rc, out, _ = f.status(f.wt)
        self.assertEqual(rc, 0)
        self.assertIn("outside every work tree of this repo", out)
        self.assertIn("byte-identical", out)

    def test_a_symlinked_hooks_path_is_still_this_trees_own(self):
        f = self.fix()
        link = f.dir / "alias"
        link.symlink_to(f.dir)
        f.git(f.main, "config", "core.hooksPath", str(link / "main" / ".githooks"))
        rc, out, err = f.status(f.main)
        self.assertEqual((rc, err), (0, ""))
        self.assertNotIn("ℹ️", out)
        self.assertNotIn("⚠️", out)
        rc, out, _ = f.status(f.wt)
        self.assertIn("the PRIMARY checkout's copy", out)
        self.assertNotIn("outside every", out)

    def test_tilde_in_hooks_path_is_expanded_as_git_does(self):
        f = self.fix()  # HOME is f.dir, so ~/main is the primary checkout
        f.git(f.main, "config", "core.hooksPath", "~/main/.githooks")
        rc, out, _ = f.status(f.wt)
        self.assertEqual(rc, 0, out)
        self.assertIn("is executable", out)
        self.assertIn("PRIMARY checkout's copy", out)

    def test_status_works_from_a_subdirectory_of_the_worktree(self):
        f = self.fix()
        sub = f.wt / "nested" / "deeper"
        sub.mkdir(parents=True)
        rc, out, err = f.status(sub)
        self.assertEqual((rc, err), (0, ""))
        self.assertIn("PRIMARY checkout's copy", out)


class Verdicts(Base):
    def test_unset_hooks_path_with_no_hook_fails_from_both_trees(self):
        f = self.fix()
        f.git(f.main, "config", "--unset", "core.hooksPath")
        for tree in (f.main, f.wt):
            rc, out, err = f.status(tree)
            self.assertEqual(rc, 1, out)
            self.assertIn("core.hooksPath unset", out)
            self.assertIn("NOT scanned", out)
            self.assertIn("NOT all set", out)
            self.assertIn("arms it", out)          # the tracked .githooks/ is named
            self.assertNotIn("Traceback", err)

    def test_legacy_install_with_hooks_path_unset_is_live_not_dead(self):
        # /atelier:repo hook writes into `git rev-parse --git-path hooks`, which
        # is .git/hooks when core.hooksPath is unset: that copy is the live one.
        f = self.fix()
        f.git(f.main, "config", "--unset", "core.hooksPath")
        legacy = f.main / ".git" / "hooks"
        for name in FLOOR:
            (legacy / name).write_text(HOOK)
            (legacy / name).chmod(0o755)
        for tree in (f.main, f.wt):
            rc, out, _ = f.status(tree)
            self.assertEqual(rc, 0, out)
            self.assertIn("all set: commits here are scanned", out)
            self.assertIn("no dead floor hook", out)
            self.assertEqual(f.run(tree)[0], 0)

    def test_hooks_path_set_to_the_default_dir_is_not_dead(self):
        f = self.fix()
        legacy = f.main / ".git" / "hooks"
        (legacy / "pre-commit").write_text(HOOK)
        (legacy / "pre-commit").chmod(0o755)
        f.git(f.main, "config", "core.hooksPath", str(legacy))
        self.assertEqual(f.run(f.main)[0], 0)

    def test_non_executable_hook_fails_from_both_trees(self):
        f = self.fix()
        (f.main / ".githooks" / "pre-commit").chmod(0o644)
        for tree in (f.main, f.wt):
            rc, out, _ = f.status(tree)
            self.assertEqual(rc, 1, out)
            self.assertIn("NOT scanned", out)

    def test_missing_scanners_fail_and_config_alone_satisfies(self):
        f = self.fix()
        env = {k: v for k, v in f.env.items() if k != "ATELIER_TOOLS"}
        for tree in (f.main, f.wt):
            rc, out, _ = f.status(tree, env=env)
            self.assertEqual(rc, 1, out)
            self.assertIn("from in-repo tools/", out)
            self.assertIn("BLOCK every commit", out)
        f.git(f.main, "config", "hooks.atelierTools", str(f.tools))
        for tree in (f.main, f.wt):
            rc, out, _ = f.status(tree, env=env)
            self.assertEqual(rc, 0, out)
            self.assertIn(f"scanners at {f.tools}  (from hooks.atelierTools", out)

    def test_dead_hook_is_a_fault_in_both_modes_from_both_trees(self):
        f = self.fix()
        dead = f.main / ".git" / "hooks" / "pre-commit"
        dead.write_text("#!/bin/sh\nexit 0\n")
        for tree in (f.main, f.wt):
            rc, out, _ = f.status(tree)
            self.assertEqual(rc, 1, out)
            self.assertIn(f"dead pre-commit hook at {dead}", out)
            rc, out, err = f.run(tree)
            self.assertEqual(rc, 1)
            self.assertIn(f"a DEAD pre-commit hook exists at {dead}", err)
            self.assertIn(f"rm {dead}", err)
        dead.unlink()
        for tree in (f.main, f.wt):
            rc, out, _ = f.run(tree)
            self.assertEqual(rc, 0)
            self.assertIn("no dead floor hook", out)

    def test_every_floor_hook_name_counts(self):
        for name in ("pre-merge-commit", "commit-msg"):
            with self.subTest(name=name):
                f = self.fix(name)
                (f.main / ".git" / "hooks" / name).write_text("#!/bin/sh\n")
                rc, _, err = f.run(f.wt)
                self.assertEqual(rc, 1)
                self.assertIn(f"a DEAD {name} hook", err)

    def test_a_dead_non_floor_hook_is_named_not_failed(self):
        f = self.fix()
        (f.main / ".git" / "hooks" / "post-checkout").write_text("#!/bin/sh\n")
        self.assertEqual(f.run(f.main)[0], 0)
        rc, out, _ = f.status(f.main)
        self.assertEqual(rc, 0, out)
        self.assertIn("post-checkout at", out)
        self.assertIn("never runs either", out)

    def test_stock_sample_hooks_are_not_dead_hooks(self):
        f = self.fix()
        (f.main / ".git" / "hooks" / "pre-commit.sample").write_text("#!/bin/sh\n")
        for tree in (f.main, f.wt):
            self.assertEqual(f.run(tree)[0], 0)

    def test_a_missing_plane_hook_warns(self):
        f = self.fix()
        (f.main / ".githooks" / "commit-msg").unlink()
        rc, out, _ = f.status(f.main)
        self.assertEqual(rc, 0, out)
        self.assertIn("⚠️ no commit-msg hook", out)
        self.assertIn("but see ⚠️ above", out)

    def test_warn_turns_1_into_0(self):
        f = self.fix()
        (f.main / ".git" / "hooks" / "pre-commit").write_text("#!/bin/sh\n")
        rc, _, err = f.run(f.main, "--warn")
        self.assertEqual(rc, 0)
        self.assertIn("DEAD", err)

    def test_dash_c_reads_another_clone(self):
        f = self.fix()
        (f.main / ".git" / "hooks" / "pre-commit").write_text("#!/bin/sh\n")
        rc, _, err = f.run(f.dir, "-C", str(f.wt))
        self.assertEqual(rc, 1)
        self.assertIn("DEAD", err)

    def test_outside_a_repo_exits_2_with_a_message(self):
        f = self.fix()
        nowhere = f.dir / "not-a-repo"
        nowhere.mkdir()
        for args in ((), ("--status",), ("--warn",)):
            rc, _, err = f.run(nowhere, *args)
            self.assertEqual(rc, 2)
            self.assertIn("not inside a git work tree", err)
            self.assertNotIn("Traceback", err)


if __name__ == "__main__":
    unittest.main()
