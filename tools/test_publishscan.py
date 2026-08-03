"""Tests for publishscan — the never-publish tracked-path lint.

The tool's job: a path whose publication weakens the repo must not be TRACKED,
whatever it contains. The tests bite-prove the grounded pattern (the finding
that produced the tool), the deliberate green list (guard declarations that
must travel), the two planes, and the hatch.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import publishscan

TOOLS = Path(__file__).resolve().parent


def git_repo(td: Path) -> Path:
    """A real git repo — this scanner's unit is git's tracked set."""
    for cmd in (["init", "-q", "-b", "main"],
                ["config", "user.email", "t@example.invalid"],  # leakscan:allow: git fixture identity
                ["config", "user.name", "T"]):
        subprocess.run(["git", "-C", str(td), *cmd], check=True,
                       capture_output=True)
    return td


def add(root: Path, rel: str, text: str = "x\n") -> None:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    subprocess.run(["git", "-C", str(root), "add", "-f", rel], check=True,
                   capture_output=True)


class PatternTest(unittest.TestCase):
    def test_the_grounded_pattern_reds(self):
        """rpi F1 — the finding the tool exists for."""
        self.assertIsNotNone(publishscan.matches(".claude/settings.json"))
        self.assertIn("unprompted",
                      publishscan.matches(".claude/settings.json"))

    def test_standard_practice_patterns_red(self):
        for p in (".mcp.json", ".env", ".env.production", "sub/.env",
                  ".envrc", ".netrc", ".npmrc", ".pypirc",
                  ".vscode/settings.json", ".idea/workspace.xml"):
            with self.subTest(path=p):
                self.assertIsNotNone(publishscan.matches(p))

    def test_patterns_match_at_any_depth(self):
        """PB1 (2026-08-02 cold pass): the first cut matched most entries at
        the repo root only — fnmatch globs are not path-aware, so the listed
        files passed green one directory down. Machine-local is machine-local
        wherever it sits."""
        for p in ("packages/api/.npmrc", "sub/.env.production",
                  "docs/.envrc", "services/x/.claude/settings.json",
                  "sub/.mcp.json", "a/b/c/.netrc", "x/.pypirc",
                  "apps/web/.vscode/settings.json", "x/.idea/workspace.xml",
                  "y/.claude/settings.local.json"):
            with self.subTest(path=p):
                self.assertIsNotNone(publishscan.matches(p))

    def test_depth_matching_does_not_overreach(self):
        """Names that merely contain the letters stay green at any depth."""
        for p in ("src/env.py", "environments/prod/main.tf",
                  "docs/build/templates/claude/settings.json",
                  "docs/envrc-notes.md", "conf/renv.lock"):
            with self.subTest(path=p):
                self.assertIsNone(publishscan.matches(p))

    def test_guard_declarations_are_deliberately_allowed(self):
        """They map where the defences are weak AND must travel to work.

        Untracking them would break the floor and hide the weakening at the
        same time — the accepted exposure named in the module docstring.
        """
        for p in (".atelier-floor.json", ".leakscanignore",
                  ".secretscanignore", ".sizescanignore", ".gitignore",
                  ".githooks/pre-commit", ".github/workflows/floor.yml"):
            with self.subTest(path=p):
                self.assertIsNone(publishscan.matches(p))

    def test_the_template_seed_is_not_the_live_file(self):
        """atelier ships the allowlist as a TEMPLATE; that must stay tracked."""
        self.assertIsNone(
            publishscan.matches("docs/build/templates/claude/settings.json"))

    def test_ordinary_content_passes(self):
        for p in ("src/env.py", "docs/method/REVIEW.md", "tools/floor.py",
                  "environments/prod/main.tf"):
            with self.subTest(path=p):
                self.assertIsNone(publishscan.matches(p))


class PlaneTest(unittest.TestCase):
    def run_tool(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS / "publishscan.py"), *args],
            capture_output=True, text=True)

    def test_ci_plane_sees_a_file_that_slipped_in_earlier(self):
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".claude/settings.json", '{"permissions":{}}\n')
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", s)
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertIn(".claude/settings.json", r.stdout)

    def test_hook_plane_judges_only_what_this_commit_adds(self):
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, "README.md")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            # Nothing staged → the hook plane has nothing to judge.
            self.assertEqual(self.run_tool("--root", s, "--staged").returncode,
                             0)
            add(root, ".mcp.json")
            self.assertEqual(self.run_tool("--root", s, "--staged").returncode,
                             1)

    def test_clean_repo_is_green_on_both_planes(self):
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, "README.md")
            add(root, ".atelier-floor.json", "{}\n")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            self.assertEqual(self.run_tool("--root", s).returncode, 0)
            self.assertEqual(self.run_tool("--root", s, "--staged").returncode,
                             0)


class HatchAndModeTest(unittest.TestCase):
    def run_tool(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS / "publishscan.py"), *args],
            capture_output=True, text=True)

    def test_ignore_file_exempts_with_a_reason(self):
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".mcp.json")
            add(root, ".publishscanignore",
                ".mcp.json  # deliberate: fixture endpoint list, no live data\n")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            self.assertEqual(self.run_tool("--root", s).returncode, 0)

    def test_bare_ignore_glob_is_a_config_error(self):
        """PB2: the stated mitigation — every exemption carries its reason —
        is enforced, not claimed. A broken scan is not a pass: exit 2."""
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".mcp.json")
            add(root, ".publishscanignore", "# deliberate\n.mcp.json\n")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", s)
            self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
            self.assertIn("reason", r.stderr)

    def test_glued_hash_glob_is_a_config_error(self):
        """PA3 (ruled 2026-08-03): a '#' glued to the glob used to silently
        truncate it into an exemption for a different path than written."""
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".mcp.json")
            add(root, ".publishscanignore", "foo#bar.md # deliberate\n")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", s)
            self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
            self.assertIn("space before", r.stderr)

    def test_json_parses_under_subdir_root_and_names_the_rebase(self):
        """PA1 (ruled 2026-08-03): the rebase notice went to stdout and broke
        --json consumers; it now goes to stderr and the JSON carries
        rebased_to (always present; null when --root was already the top)."""
        import json as _json
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".claude/settings.json", '{"permissions":{}}\n')
            add(root, "docs/README.md")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", str(Path(s) / "docs"), "--json")
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            doc = _json.loads(r.stdout)  # would raise before the fix
            self.assertTrue(doc["rebased_to"])
            self.assertIn("--root is inside the repo", r.stderr)
            top = self.run_tool("--root", s, "--json")
            self.assertIsNone(_json.loads(top.stdout)["rebased_to"])
            self.assertNotIn("--root is inside the repo", top.stderr)

    def test_subdir_root_rebases_to_the_repo_top(self):
        """PB3: --root inside the repo must not silently scan a subtree that
        the root-anchored patterns can never match."""
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".claude/settings.json", '{"permissions":{}}\n')
            add(root, "docs/README.md")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", str(Path(s) / "docs"))
            self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
            self.assertIn(".claude/settings.json", r.stdout)

    def test_warn_never_blocks_but_still_reports(self):
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".env")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", s, "--warn")
            self.assertEqual(r.returncode, 0, r.stdout)
            self.assertIn(".env", r.stdout)
            self.assertIn("advisory", r.stdout)

    def test_json_shape(self):
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".claude/settings.json")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", s, "--json")
            self.assertEqual(r.returncode, 1)
            data = json.loads(r.stdout)
            self.assertEqual([f["path"] for f in data["findings"]],
                             [".claude/settings.json"])

    def test_non_repo_root_is_a_usage_error_not_a_pass(self):
        r = self.run_tool("--root", "/nonexistent-publishscan-test")
        self.assertEqual(r.returncode, 2)

    def test_a_non_repo_tree_skips_visibly_rather_than_blocking(self):
        """Not a fail-open: with no git there is no tracked set to miss.

        The first cut hard-failed here on fail-closed instinct, and floor.py's
        own suite caught it — its fixture trees are plain directories, so a
        hard failure would have made this scanner unrunnable in every child's
        fixtures. A tree with no git cannot publish anything through git, so
        the check's claim is true rather than unverified. Every other git
        failure stays exit 2.
        """
        with tempfile.TemporaryDirectory() as s:
            r = self.run_tool("--root", s)
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("not a git repository", r.stdout)

    def test_selftest_passes(self):
        self.assertEqual(self.run_tool("--selftest").returncode, 0)


class ControlCharacterTest(unittest.TestCase):
    """Nothing this tool ingests can repaint the terminal it reports to.

    Both output surfaces echo strings the tool did not write: the
    `BadIgnoreFile` message embeds the offending glob verbatim, and a finding
    line prints a tracked path (three times over, counting the two
    remediation commands under it). A hostile or careless child could put ANSI
    escapes in either and clear the screen, or paint a clean-scan line over a
    red one. PA4 (ruled 2026-08-03) folded both into C1F3's strip-at-parse
    scope — one class, closed in both tools at the seam where text enters.
    """

    def run_tool(self, *args: str) -> subprocess.CompletedProcess:
        return subprocess.run(
            [sys.executable, str(TOOLS / "publishscan.py"), *args],
            capture_output=True, text=True)

    def test_the_strip_drops_controls_and_keeps_everything_else(self):
        self.assertEqual(
            publishscan._strip_controls("\x1b[2K.mcp\x07.json\x7f\x00"),
            "[2K.mcp.json")
        self.assertEqual(publishscan._strip_controls(".claude/settings.json"),
                         ".claude/settings.json")

    def test_a_hostile_glob_cannot_repaint_the_error_message(self):
        """The surface PA4 named: a bare glob is echoed back verbatim at
        exit 2, so the escape sequence rode out on the error the tool prints
        when it refuses the file."""
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".mcp.json")
            add(root, ".publishscanignore", "\x1b[2J\x1b[H.mcp.json\n")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            r = self.run_tool("--root", s)
        # Still a config error, still loud — the strip must not turn a refusal
        # into a pass.
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertNotIn("\x1b", r.stderr)
        self.assertIn(".mcp.json", r.stderr)

    def test_a_stripped_glob_still_exempts_what_it_names(self):
        """The other direction: stripping must not quietly rewrite an honest
        exemption into one that matches nothing — which would red a repo that
        had done everything right."""
        with tempfile.TemporaryDirectory() as s:
            root = git_repo(Path(s))
            add(root, ".mcp.json")
            add(root, ".publishscanignore",
                ".mcp.json  # deliberate: fixture endpoints, no live data\n")
            subprocess.run(["git", "-C", s, "commit", "-qm", "x"], check=True,
                           capture_output=True)
            self.assertEqual(self.run_tool("--root", s).returncode, 0)

    def test_a_git_error_cannot_repaint_the_error_message(self):
        """The second ingest seam. git's own stderr is echoed at exit 2 and
        can carry a repo-supplied path; the paths it lists on stdout are
        echoed in every finding line. Both come through `_git`, so both are
        stripped there."""
        with tempfile.TemporaryDirectory() as s:
            fake = Path(s) / "git"
            fake.write_text(
                "#!/bin/sh\nprintf '\\033[2J.env\\n' >&2\nexit 128\n")
            fake.chmod(0o755)
            r = subprocess.run(
                [sys.executable, str(TOOLS / "publishscan.py"), "--root", s],
                capture_output=True, text=True,
                env={**os.environ, "PATH": f"{s}:{os.environ['PATH']}"})
        # A broken scan is not a pass, and the message it fails with is clean.
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertNotIn("\x1b", r.stderr)

    def test_a_control_bearing_path_is_reported_clean(self):
        """The finding line itself. Whatever git hands over, what reaches the
        terminal carries no controls — the guarantee is this tool's, not a
        default of git's quoting that a child could switch off."""
        for line in publishscan._git(Path(TOOLS).parent, "ls-files"):
            self.assertNotIn("\x1b", line)
        self.assertEqual(
            [publishscan._strip_controls(".env\x1b[2K")], [".env[2K"])


if __name__ == "__main__":
    unittest.main()
