"""Tests for tools/pre-commit.sample — the scan hook's contract, kept honest.

The 2026-07-10 create-repo exercise found this hook FAILING OPEN: it pointed at
$repo_root/tools/ and silently skipped both scanners in a scaffolded child repo
(which has none — the scanners live only in atelier), committing a planted
secret with a green exit. These tests pin the fixed contract so a regression
can't ship silently again (EVIDENCE §14: a live proof that doesn't persist is a
claim; the known-failure-test is the enforcement):

  1. FAIL CLOSED — no resolvable scanners → the commit is BLOCKED, not skipped.
  2. Resolution via `git config hooks.atelierTools` → a staged real-shaped
     secret is blocked; a clean commit passes.
  3. Resolution via ATELIER_TOOLS env (wins over config).
  4. In-repo fallback ($repo_root/tools) — atelier's own case — still blocks.
  5. linkscan is wired WHOLE-TREE, not staged: a broken internal link blocks,
     and — the crux — a rename that breaks a link in a file NOT in the diff
     still blocks (the staged boundary scanners structurally cannot see this,
     which is why linkscan runs over the tree). A valid link passes.

Each test builds a throwaway git repo in a temp dir and drives `git commit`
for real: the hook's behaviour is only meaningful on the actual commit path.
Zero third-party deps, same as the rest of the suite.
"""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
SAMPLE = TOOLS_DIR / "pre-commit.sample"

# Structural-match AWS access-key-ID shape — secretscan flags it as
# [high/named]. (Do NOT use AWS's published example SECRET key wJalr…: the
# scanner correctly ignores known documentation dummies, which made the first
# live proof look like a miss.)
PLANTED_SECRET = 'aws_key = "AKIAIOSFODNN7EXAMPLE"\n'  # secretscan:allow / leakscan:allow: test fixture


def _git(repo: Path, *args: str, env: dict | None = None) -> subprocess.CompletedProcess:
    e = os.environ.copy()
    if env:
        e.update(env)
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, env=e,
    )


class PreCommitHookTest(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.mkdtemp(prefix="precommit-test-")
        self.repo = Path(self._tmp) / "child"
        self.repo.mkdir()
        _git(self.repo, "init", "-q")
        _git(self.repo, "config", "user.name", "Test")
        _git(self.repo, "config", "user.email", "test@example.com")  # leakscan:allow: RFC-2606 fixture identity for throwaway test repos
        hook = self.repo / ".git" / "hooks" / "pre-commit"
        shutil.copy(SAMPLE, hook)
        hook.chmod(0o755)

    def tearDown(self):
        shutil.rmtree(self._tmp, ignore_errors=True)

    def _commit(self, msg: str = "x", env: dict | None = None) -> subprocess.CompletedProcess:
        _git(self.repo, "add", "-A")
        return _git(self.repo, "commit", "-m", msg, env=env)

    def _commit_count(self) -> int:
        r = _git(self.repo, "rev-list", "--count", "HEAD")
        return int(r.stdout) if r.returncode == 0 else 0

    # -- 1. the defect class itself ------------------------------------------

    def test_fails_closed_when_scanners_unresolvable(self):
        """No config, no env, no in-repo tools/ → BLOCK, never a silent pass."""
        (self.repo / "README.md").write_text("hello\n")
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertNotEqual(r.returncode, 0, "hook must fail closed, not skip")
        self.assertIn("fail closed", r.stderr.lower())
        self.assertEqual(self._commit_count(), 0, "nothing may enter history unscanned")

    # -- 2. resolution via baked git config (the create-repo path) ------------

    def test_config_resolution_blocks_planted_secret(self):
        _git(self.repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
        (self.repo / "leaky.py").write_text(PLANTED_SECRET)
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertNotEqual(r.returncode, 0, "a staged secret must block the commit")
        self.assertEqual(self._commit_count(), 0)

    def test_config_resolution_passes_clean_commit(self):
        _git(self.repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
        (self.repo / "README.md").write_text("clean content\n")
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertEqual(r.returncode, 0, f"clean commit must pass; stderr: {r.stderr}")
        self.assertEqual(self._commit_count(), 1)

    # -- 3. env resolution wins over config ------------------------------------

    def test_env_resolution_wins_over_config(self):
        # Config deliberately points nowhere; env points at the real tools.
        _git(self.repo, "config", "hooks.atelierTools", "/nonexistent")
        (self.repo / "leaky.py").write_text(PLANTED_SECRET)
        r = self._commit(env={"ATELIER_TOOLS": str(TOOLS_DIR)})
        self.assertNotEqual(r.returncode, 0, "env-resolved scanner must run and block")
        self.assertEqual(self._commit_count(), 0)
        # ...and the block must be a scan finding, not the fail-closed path.
        self.assertNotIn("fail closed", r.stderr.lower())

    # -- 4. in-repo fallback (atelier's own hook) -------------------------------

    def test_in_repo_fallback_blocks(self):
        """A repo carrying the scanners itself (atelier) needs no config."""
        tools = self.repo / "tools"
        tools.mkdir()
        # Carry every scanner the hook runs, so the block is the secretscan
        # finding — not a fail-closed on a scanner the hook also invokes.
        for name in ("secretscan.py", "leakscan.py", "linkscan.py",
                     "reviewscan.py"):
            shutil.copy(TOOLS_DIR / name, tools / name)
        (self.repo / "leaky.py").write_text(PLANTED_SECRET)
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(self._commit_count(), 0)
        self.assertNotIn("fail closed", r.stderr.lower())

    # -- 5. linkscan wired whole-tree (not staged) -----------------------------

    def test_broken_link_blocks_commit(self):
        """A staged Markdown file with a broken internal link is blocked."""
        _git(self.repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
        (self.repo / "doc.md").write_text("# Doc\n\nsee [the plan](nope.md)\n")
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertNotEqual(r.returncode, 0, "a broken internal link must block")
        self.assertEqual(self._commit_count(), 0)
        self.assertNotIn("fail closed", r.stderr.lower())

    def test_valid_link_passes(self):
        """A Markdown file whose internal link resolves commits cleanly."""
        _git(self.repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
        (self.repo / "target.md").write_text("# Target\n\nbody\n")
        (self.repo / "doc.md").write_text("# Doc\n\nsee [target](target.md)\n")
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertEqual(r.returncode, 0, f"clean links must pass; stderr: {r.stderr}")
        self.assertEqual(self._commit_count(), 1)

    def test_rename_breaking_unstaged_link_blocks(self):
        """The crux of whole-tree scanning: deleting target.md breaks doc.md's
        link even though doc.md is NOT in this commit's diff. A staged-only scan
        would wave this through; linkscan over the tree catches it."""
        _git(self.repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
        (self.repo / "target.md").write_text("# Target\n\nbody\n")
        (self.repo / "doc.md").write_text("# Doc\n\nsee [target](target.md)\n")
        first = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertEqual(first.returncode, 0, f"setup commit must pass; stderr: {first.stderr}")
        # Remove the target only — doc.md is untouched, so it is not in the diff.
        _git(self.repo, "rm", "-q", "target.md")
        r = _git(self.repo, "commit", "-m", "drop target", env={"ATELIER_TOOLS": ""})
        self.assertNotEqual(r.returncode, 0,
                            "a rename/delete breaking an unstaged link must block")
        self.assertEqual(self._commit_count(), 1, "the breaking commit must not land")


if __name__ == "__main__":
    unittest.main()
