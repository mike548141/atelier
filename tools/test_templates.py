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


if __name__ == "__main__":
    unittest.main()
