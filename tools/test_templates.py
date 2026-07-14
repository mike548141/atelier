"""Tests for docs/build/templates/ — the template↔canonical sync, kept honest.

The 2026-07-10 create-repo review (C3) closed a stated hope with a mechanism:
the CLAUDE.md template carries a *stamped copy* of the standard doctrine block
whose canonical text is docs/method/PROPAGATION.md, and its header said a pin
bump "reviews this wording too" — but nothing mechanical diffed the copy
against the canonical. The MODEL-ECONOMICS template drift (found in the same
rewire) proves this class of second-copy drift happens. These tests are the
diff, run on every suite run.
"""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROPAGATION = ROOT / "docs" / "method" / "PROPAGATION.md"
TEMPLATE = ROOT / "docs" / "build" / "templates" / "CLAUDE.md"

BLOCK_HEADING = "## Doctrine — inherited from atelier (pinned"
PLACEHOLDERS = {"<atelier-path>", "<SHA>", "<owner/repo>", "<visibility fact>"}


def canonical_block() -> str:
    """The fenced block PROPAGATION.md declares as the standard child block."""
    m = re.search(r"```markdown\n(.*?)\n```", PROPAGATION.read_text(), re.S)
    if not m:
        raise AssertionError("PROPAGATION.md has no ```markdown fenced block")
    return m.group(1).rstrip()


def template_block() -> str:
    """The stamped copy: from the block heading to the first --- divider."""
    text = TEMPLATE.read_text()
    start = text.index(BLOCK_HEADING)
    end = text.index("\n---", start)
    return text[start:end].rstrip()


class TemplateBlockSyncTest(unittest.TestCase):
    def test_stamped_block_matches_canonical(self):
        """Character-for-character: a copy that drifts is a second source."""
        self.assertEqual(
            canonical_block(),
            template_block(),
            "templates/CLAUDE.md doctrine block has drifted from "
            "PROPAGATION.md's canonical text — sync them (canonical wins, "
            "or change PROPAGATION deliberately and re-stamp)",
        )

    def test_block_carries_exactly_the_four_placeholders(self):
        """create-repo fills exactly these; a fifth (or a lost one) means the
        skill's stamp step and the block have drifted apart."""
        found = set(re.findall(r"<[a-z/ A-Z-]+>", canonical_block()))
        self.assertEqual(found, PLACEHOLDERS)

    def test_prose_placeholder_count_matches_block(self):
        """PROPAGATION's prose said 'three' while its own block carried four
        (review C4) — pin the sentence to the block's reality."""
        self.assertRegex(PROPAGATION.read_text(), r"fill the four\s+placeholders")


FLOOR = ROOT / "docs" / "build" / "templates" / "workflows" / "floor.yml"


class ChildFloorWorkflowTest(unittest.TestCase):
    """docs/build/templates/workflows/floor.yml — the child-CI scanner floor.

    Its safety rests on invariants that are easy to break with an innocent
    edit: it must fetch the *one source* of scanners, scope the scan to the
    repo's own tree (not the whole workspace, which holds atelier's fake-secret
    fixtures), and keep leakscan structural-only (its term list is machine-local
    and must never be demanded in CI). Pin them.
    """

    def setUp(self):
        self.text = FLOOR.read_text()

    def test_fetches_atelier_scanners_one_source(self):
        """No vendored copy: the tools come from a checkout of atelier."""
        self.assertIn("repository: mike548141/atelier", self.text)
        for tool in ("secretscan.py", "leakscan.py", "linkscan.py"):
            self.assertIn(f"atelier/tools/{tool}", self.text)

    def test_scan_scoped_to_repo_not_workspace(self):
        """Every active scan targets `repo` (its own tree), never `.` — a
        whole-workspace scan would false-positive on atelier's fixtures.
        Selftest lines scan nothing, so they are exempt."""
        runs = re.findall(r"tools/(?:secret|leak|link)scan\.py [^\n]*", self.text)
        runs = [ln for ln in runs if "--selftest" not in ln]
        self.assertTrue(runs, "no scanner run lines found in floor.yml")
        for line in runs:
            self.assertRegex(
                line,
                r"--root repo repo$",
                f"scan not scoped to the repo tree: {line!r}",
            )

    def test_selftests_run_before_the_scans(self):
        """2026-07-11 review N5 (mirrors atelier's own ci.yml): prove the
        fetched instruments before trusting their pass — a scanner that cannot
        detect its own fixtures must go red here, not pass green below."""
        for tool in ("secretscan.py", "leakscan.py", "linkscan.py"):
            self.assertIn(f"atelier/tools/{tool} --selftest", self.text)
        self.assertLess(self.text.find("--selftest"),
                        self.text.find("--root repo repo"),
                        "selftests must run before the scans they vouch for")

    def test_push_trigger_covers_every_branch(self):
        """2026-07-11 review N4: a push to ANY branch is publication (the
        commit is on the remote whether or not it's ever PR'd); restricting
        push to main left a never-PR'd feature branch scanned by nothing."""
        on_block = self.text[self.text.find("\non:"):self.text.find("permissions:")]
        self.assertNotIn("branches:", on_block)

    def test_false_positive_hatches_documented(self):
        """2026-07-11 review N6: a child whose own tree legitimately trips a
        scanner (its own fake-secret fixtures, a committed build-output dir)
        must find the hatch in this file, not in atelier's internals."""
        for hatch in (".secretscanignore", ".leakscanignore", ".linkscanignore"):
            self.assertIn(hatch, self.text)

    def test_leakscan_structural_only(self):
        """--require-terms would demand the machine-local term list CI can't
        (and must not) hold — the same honest scope as atelier's own ci.yml.
        Assert on the active run line, not the file: the header prose names the
        flag to explain why it's absent."""
        run_lines = [
            ln for ln in self.text.splitlines()
            if "run:" in ln and "leakscan.py" in ln
        ]
        self.assertTrue(run_lines, "no leakscan run line found in floor.yml")
        for ln in run_lines:
            self.assertNotIn("--require-terms", ln)

    def test_licenscan_is_a_commented_publish_gate(self):
        """No LICENSE hard-fails licenscan; a private/pre-licence child must
        not red on it. It stays commented until the repo opts in."""
        for line in self.text.splitlines():
            if "licenscan.py" in line:
                self.assertTrue(
                    line.lstrip().startswith("#"),
                    f"licenscan must be commented (publish gate): {line!r}",
                )

    def test_least_privilege(self):
        """The floor only reads trees."""
        self.assertIn("contents: read", self.text)

    def test_sizescan_wired_as_a_check_scoped_to_repo(self):
        """2026-07-14 review: sizescan gates current-truth file size in --check
        mode, scoped to the repo's own tree, with its selftest run first — the
        same contract as the other scanners."""
        self.assertIn("atelier/tools/sizescan.py --selftest", self.text)
        run_lines = [ln for ln in self.text.splitlines()
                     if "run:" in ln and "sizescan.py" in ln and "--selftest" not in ln]
        self.assertTrue(run_lines, "no sizescan run line found in floor.yml")
        for ln in run_lines:
            self.assertIn("--check", ln)          # a gate, not advisory
            self.assertRegex(ln, r"--root repo repo$")   # its own tree only


if __name__ == "__main__":
    unittest.main()
