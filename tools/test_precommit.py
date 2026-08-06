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
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
SAMPLE = TOOLS_DIR / "pre-commit.sample"
TRACKED_HOOK = TOOLS_DIR.parent / ".githooks" / "pre-commit"

# Structural-match AWS access-key-ID shape — secretscan flags it as
# [high/named]. (Do NOT use AWS's published example SECRET key wJalr…: the
# scanner correctly ignores known documentation dummies, which made the first
# live proof look like a miss.)
PLANTED_SECRET = 'aws_key = "AKIAIOSFODNN7EXAMPLE"\n'  # secretscan:allow: test fixture / leakscan:allow: test fixture


def _registry_scanners() -> list[str]:
    """The scanners floor.py actually runs, read from the registry itself."""
    sys.path.insert(0, str(TOOLS_DIR))
    import floor  # noqa: E402  (deliberately late — TOOLS_DIR must be on the path)

    return [s.name for s in floor.SCANNERS]


# The hook plane runs leakscan with --require-terms, so these tests need a term
# list or every "clean commit passes" case blocks. Pin one INSIDE the fixture
# rather than inheriting the machine's: without this the suite passes on a
# developer laptop (which has ~/.claude/leakscan-terms.txt) and fails on every
# CI runner (which must never have one) — an env-gated split where the local run
# is the misleading half. Deliberately nonsense so it matches no fixture here.
#
# Built in setUpModule, not at import (TA6): at module scope this wrote a temp
# file on EVERY import — including test selections that run none of these tests
# — and never removed it. The fixture-pinning is the part that matters and is
# unchanged; only its lifetime is.
_TERMS: Path | None = None
_TERMS_DIR: str | None = None


def setUpModule() -> None:
    global _TERMS, _TERMS_DIR
    _TERMS_DIR = tempfile.mkdtemp(prefix="precommit-terms-")
    _TERMS = Path(_TERMS_DIR) / "leakscan-terms.txt"
    _TERMS.write_text("zzz-term-that-appears-in-no-fixture\n", encoding="utf-8")


def tearDownModule() -> None:
    if _TERMS_DIR:
        shutil.rmtree(_TERMS_DIR, ignore_errors=True)


def _git(repo: Path, *args: str, env: dict | None = None) -> subprocess.CompletedProcess:
    e = os.environ.copy()
    e["ATELIER_LEAKSCAN_TERMS"] = str(_TERMS)
    if env:
        e.update(env)
    return subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True, text=True, env=e,
    )


class TrackedHookTest(unittest.TestCase):
    """.githooks/pre-commit — the hook that survives a fresh clone.

    `.git/hooks/` is untracked, so a hook installed there exists on exactly one
    machine and no clone inherits it. That is not a theoretical gap: on
    2026-07-25 every guard in every child repo in the estate was machine-local,
    and a fresh clone (or a new laptop) would have started with none. A tracked
    `.githooks/` plus `core.hooksPath` makes the hook FILE travel and stay
    current; one `git config` per clone is still needed, and `floorfleet` is
    what catches a clone that never ran it.

    The tracked copy is a stamped copy of tools/pre-commit.sample, so it needs
    the same treatment every other stamped copy in this repo gets: a test that
    diffs it. A drifted hook is worse than no hook, because it looks installed.
    """

    def test_tracked_hook_matches_the_canonical_sample(self):
        self.assertTrue(TRACKED_HOOK.is_file(),
                        ".githooks/pre-commit is missing — the tracked hook is "
                        "how a fresh clone gets guarded at all")
        self.assertEqual(
            SAMPLE.read_text(), TRACKED_HOOK.read_text(),
            ".githooks/pre-commit has drifted from tools/pre-commit.sample — "
            "sync them (the sample is canonical)",
        )

    def test_tracked_hook_is_executable(self):
        """A non-executable hook is silently skipped by git: no error, no scan,
        green commits. Exactly the fail-open shape this repo keeps closing."""
        self.assertTrue(TRACKED_HOOK.stat().st_mode & 0o111,
                        ".githooks/pre-commit is not executable — git will skip "
                        "it silently and every commit goes unscanned")

    def test_tracked_hook_blocks_a_real_commit_via_hookspath(self):
        """Drive a real commit through `core.hooksPath`, not `.git/hooks/`.

        Every other test here installs the hook the legacy way. That would leave
        the tracked-hooks route — the whole point of the transport fix, and the
        route every repo is about to be moved onto — proven by nothing but
        resemblance. So: plant a secret in a repo whose hook lives in a TRACKED
        directory, and require the commit to be refused.
        """
        tmp = tempfile.mkdtemp(prefix="hookspath-test-")
        try:
            repo = Path(tmp) / "child"
            (repo / ".githooks").mkdir(parents=True)
            _git(repo, "init", "-q")
            _git(repo, "config", "user.name", "Test")
            _git(repo, "config", "user.email", "test@example.com")  # leakscan:allow: RFC-2606 fixture identity
            _git(repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
            hook = repo / ".githooks" / "pre-commit"
            shutil.copy(TRACKED_HOOK, hook)
            hook.chmod(0o755)
            _git(repo, "config", "core.hooksPath", ".githooks")

            (repo / "leaky.py").write_text(PLANTED_SECRET)
            _git(repo, "add", "-A")
            r = _git(repo, "commit", "-m", "x", env={"ATELIER_TOOLS": ""})

            self.assertNotEqual(r.returncode, 0,
                                "the tracked hook must block a planted secret")
            self.assertNotIn("fail closed", r.stderr.lower(),
                             "must block on the FINDING, not on a missing scanner")
            count = _git(repo, "rev-list", "--count", "HEAD")
            landed = int(count.stdout) if count.returncode == 0 else 0
            self.assertEqual(landed, 0, "nothing may enter history")
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_tracked_hook_names_no_scanner(self):
        """Same invariant as the child CI floor: the hook is transport, the
        registry is policy."""
        body = "\n".join(ln for ln in TRACKED_HOOK.read_text().splitlines()
                         if not ln.lstrip().startswith("#"))
        self.assertNotRegex(
            body, r"\b(?!floor)\w+scan\.py",
            "the hook must name no individual scanner — add it to the registry",
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

    def test_a_clone_with_no_term_list_blocks_rather_than_half_scanning(self):
        """ADR 0008 cold pass, EP3. "The full cover lives on the hook" was the
        design's stated asymmetry with CI, and nothing enforced it: with no
        machine-local term list leakscan degraded to a structural-only scan, and
        the floor printed `✅ leakscan enforced` ten lines under leakscan's own
        warning. A clone got CI-grade cover from the plane that is supposed to
        carry the personal-data boundary, with no signal anywhere.

        The block is the point: this is the boundary the public-repo rule
        depends on, so a partial scan must not be reportable as a pass."""
        _git(self.repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
        (self.repo / "README.md").write_text("clean content\n")
        r = self._commit(env={"ATELIER_TOOLS": "",
                              "ATELIER_LEAKSCAN_TERMS": "/nonexistent/terms.txt",
                              "HOME": self._tmp})
        self.assertNotEqual(r.returncode, 0,
                            "a structural-only hook scan must not pass as full cover")
        self.assertEqual(self._commit_count(), 0)
        # The remedy has to travel with the block, or a fresh clone reads this
        # as broken tooling and reaches for --no-verify.
        self.assertIn("--require-terms", r.stderr)

    def test_a_missing_python3_blocks_with_a_remedy_that_is_not_the_bypass(self):
        """ADR 0008 cold pass, EP9. Fail-closed was never in doubt here — a bare
        `python3: command not found` still exits non-zero. What was missing is
        that the ONLY actionable line a contributor saw was the `--no-verify`
        bypass at the bottom, so the one machine that cannot scan was also the
        one told how to skip scanning. The interpreter now gets the same guard
        the registry above it has had all along."""
        _git(self.repo, "config", "hooks.atelierTools", str(TOOLS_DIR))
        (self.repo / "README.md").write_text("clean content\n")
        # A PATH carrying git and nothing else this hook needs. Symlinked rather
        # than emptied: git must still resolve, or the failure under test is
        # never reached.
        bindir = Path(self._tmp) / "bin"
        bindir.mkdir()
        git_path = shutil.which("git")
        self.assertIsNotNone(git_path, "no git on PATH — cannot drive this test")
        (bindir / "git").symlink_to(git_path)
        self.assertIsNone(shutil.which("python3", path=str(bindir)),
                          "fixture PATH must not resolve python3")

        r = self._commit(env={"ATELIER_TOOLS": "", "PATH": str(bindir)})
        self.assertNotEqual(r.returncode, 0, "no interpreter must block, not skip")
        self.assertEqual(self._commit_count(), 0)
        self.assertIn("python3 not found", r.stderr)
        self.assertIn("fail closed", r.stderr.lower())
        # The remedy, and the shape of it: a way to FIX the machine, offered
        # before the way to skip the check.
        self.assertIn("Install it", r.stderr)
        self.assertLess(r.stderr.find("Install it"),
                        r.stderr.find("--no-verify") if "--no-verify" in r.stderr
                        else len(r.stderr),
                        "the fix must be printed above the bypass, not below it")

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
        # Carry the registry AND every scanner it runs, so the block is the
        # secretscan finding — not a fail-closed on a scanner floor.py invokes.
        # Read the list from floor.py rather than hard-coding it: a hard-coded
        # list here would be a fourth copy of the policy, which is the exact bug
        # ADR 0008 removed.
        shutil.copy(TOOLS_DIR / "floor.py", tools / "floor.py")
        for name in _registry_scanners():
            shutil.copy(TOOLS_DIR / f"{name}.py", tools / f"{name}.py")
        (self.repo / "leaky.py").write_text(PLANTED_SECRET)
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertNotEqual(r.returncode, 0)
        self.assertEqual(self._commit_count(), 0)
        self.assertNotIn("fail closed", r.stderr.lower())

    # -- 4b. the shim's NEW fail-closed surface (ADR 0008) ---------------------

    def test_missing_individual_scanner_still_blocks(self):
        """floor.py present, one scanner absent → BLOCK.

        The 2026-07-10 defect was the hook failing open on a missing scanner.
        Routing every scanner through floor.py moved that surface rather than
        removing it: now a tools dir can hold the registry but not the check it
        names. Pinned here because a fail-OPEN in this spot would be the original
        defect wearing new clothes — and it would look green.
        """
        tools = self.repo / "tools"
        tools.mkdir()
        shutil.copy(TOOLS_DIR / "floor.py", tools / "floor.py")
        names = _registry_scanners()
        for name in names[1:]:  # deliberately omit the first registered scanner
            shutil.copy(TOOLS_DIR / f"{name}.py", tools / f"{name}.py")
        (self.repo / "README.md").write_text("entirely clean content\n")
        r = self._commit(env={"ATELIER_TOOLS": ""})
        self.assertNotEqual(r.returncode, 0,
                            "a missing scanner must block, not silently skip")
        self.assertIn("fail closed", r.stderr.lower())
        self.assertIn(names[0], r.stderr)
        self.assertEqual(self._commit_count(), 0,
                         "nothing may enter history with a check unrun")

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
