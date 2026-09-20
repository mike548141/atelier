"""Stdlib-only tests for blockscan (no pytest needed): `python3 -m unittest`.

Builds a tiny real git repo per test (blockscan's --staged mode reads
`git show HEAD:` and `git show :`, so a fixture must be an actual repo, not
just files on disk) with a stripped-down map: one bullet ("apex"), one
source doc with a mapped heading, a region file, and a template file — the
same four-file shape as `blockscan.py`'s own `--selftest`, factored here so
each case is a separate, named test rather than one long script."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import blockscan as bs


def _git(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), *args], check=True,
                   capture_output=True, text=True)


class BlockscanFixture(unittest.TestCase):
    """One repo per test: an APEX.md with a mapped heading, a PROPAGATION.md
    floor region, and a template CLAUDE.md stamped copy — each starting
    identical and committed, so a test only has to write the ONE change it's
    about."""

    ANCHOR = "**The apex:**"
    HEADING = "## Honesty is absolute"

    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory(prefix="blockscan-test-")
        self.root = Path(self._tmpdir.name)
        (self.root / "docs" / "method").mkdir(parents=True)
        (self.root / "docs" / "build" / "templates").mkdir(parents=True)
        (self.root / "tools").mkdir()

        self.write_source("Original honesty text.")
        self.write_region("- **The apex:** Original block wording.\n")
        self.write_template("- **The apex:** Original block wording.\n")
        (self.root / "tools" / "blockscan_map.json").write_text(json.dumps({
            "region": {"path": "docs/method/PROPAGATION.md",
                      "begin_marker": "floor:begin", "end_marker": "floor:end"},
            "template": {"path": "docs/build/templates/CLAUDE.md",
                        "begin_marker": "stamp:begin", "end_marker": "stamp:end"},
            "bullets": {
                "apex": {
                    "anchor": self.ANCHOR,
                    "sources": [{"path": "docs/method/APEX.md",
                                "heading": self.HEADING}],
                }
            },
        }))

        _git(self.root, "init", "-q", "-b", "main")
        _git(self.root, "config", "user.email", "test@example.com")  # leakscan:allow: RFC-2606 fixture identity for a throwaway test repo
        _git(self.root, "config", "user.name", "Test")
        _git(self.root, "add", "-A")
        _git(self.root, "commit", "-q", "-m", "init")

    def tearDown(self):
        self._tmpdir.cleanup()

    def write_source(self, body: str) -> None:
        (self.root / "docs" / "method" / "APEX.md").write_text(
            f"# Apex\n\n{self.HEADING}\n\n{body}\n"
            "## Adaptation is continuous\n\nOther text.\n")

    def write_region(self, bullet: str) -> None:
        (self.root / "docs" / "method" / "PROPAGATION.md").write_text(
            "# Propagation\n\n<!-- floor:begin -->\n"
            "## Doctrine\n\n" + bullet +
            "- **Concurrency:** other bullet text.\n"
            "<!-- floor:end -->\n")

    def write_template(self, bullet: str) -> None:
        (self.root / "docs" / "build" / "templates" / "CLAUDE.md").write_text(
            "<!-- stamp:begin source=docs/method/PROPAGATION.md region=floor -->\n"
            "## Doctrine\n\n" + bullet +
            "- **Concurrency:** other bullet text.\n"
            "<!-- stamp:end -->\n")

    def stage_all(self) -> None:
        _git(self.root, "add", "-A")

    def run_staged(self) -> "subprocess.CompletedProcess[str]":
        return subprocess.run(
            [sys.executable, bs.__file__, "--staged", "--root", str(self.root)],
            capture_output=True, text=True)

    def run_check(self) -> "subprocess.CompletedProcess[str]":
        return subprocess.run(
            [sys.executable, bs.__file__, "--check", "--root", str(self.root)],
            capture_output=True, text=True)

    def run_against(self, rev: str) -> "subprocess.CompletedProcess[str]":
        return subprocess.run(
            [sys.executable, bs.__file__, "--against", rev, "--root", str(self.root)],
            capture_output=True, text=True)


class UnchangedTree(BlockscanFixture):
    def test_nothing_staged_is_clean(self):
        r = self.run_staged()
        self.assertEqual(0, r.returncode, r.stdout + r.stderr)

    def test_whole_tree_check_is_clean(self):
        r = self.run_check()
        self.assertEqual(0, r.returncode, r.stdout + r.stderr)


class SectionChangedNoBlockMove(BlockscanFixture):
    """The core rule: a mapped section changed, neither copy of its block
    bullet moved -> a violation, exit 1."""

    def test_reds_with_both_files_unmoved(self):
        self.write_source("Reworded honesty text.")
        self.stage_all()
        r = self.run_staged()
        self.assertEqual(1, r.returncode, r.stdout + r.stderr)
        self.assertIn("violation", r.stdout)
        self.assertIn("docs/method/PROPAGATION.md", r.stdout)
        self.assertIn("docs/build/templates/CLAUDE.md", r.stdout)


class SectionChangedBothBlocksMove(BlockscanFixture):
    """Both the region's and the template's bullet text changed alongside
    the source section -> clean."""

    def test_passes_when_both_copies_move(self):
        self.write_source("Reworded honesty text.")
        self.write_region("- **The apex:** Updated block wording.\n")
        self.write_template("- **The apex:** Updated block wording.\n")
        self.stage_all()
        r = self.run_staged()
        self.assertEqual(0, r.returncode, r.stdout + r.stderr)
        self.assertIn("moved", r.stdout)


class SectionChangedOnlyOneBlockMoves(BlockscanFixture):
    """Only ONE of the two copies moved -> still a violation, and it names
    the file that did not move."""

    def test_reds_and_names_the_unmoved_file(self):
        self.write_source("Reworded honesty text.")
        self.write_region("- **The apex:** Updated block wording.\n")
        # template left unmoved
        self.stage_all()
        r = self.run_staged()
        self.assertEqual(1, r.returncode, r.stdout + r.stderr)
        self.assertIn("docs/build/templates/CLAUDE.md", r.stdout)


class AgainstModeCIBackstop(BlockscanFixture):
    """`--against <rev>` asks the same question `--staged` asks, between two
    committed revisions instead of HEAD-vs-index — the CI plane's stand-in
    for a staged diff (matching harvestscan's own `--against HEAD^`)."""

    def test_committed_violation_reds_against_previous_commit(self):
        self.write_source("Reworded honesty text.")
        self.stage_all()
        _git(self.root, "commit", "-q", "-m", "reword, block not moved")
        r = self.run_against("HEAD^")
        self.assertEqual(1, r.returncode, r.stdout + r.stderr)
        self.assertIn("violation", r.stdout)

    def test_committed_and_moved_passes_against_previous_commit(self):
        self.write_source("Reworded honesty text.")
        self.write_region("- **The apex:** Updated block wording.\n")
        self.write_template("- **The apex:** Updated block wording.\n")
        self.stage_all()
        _git(self.root, "commit", "-q", "-m", "reword and move both")
        r = self.run_against("HEAD^")
        self.assertEqual(0, r.returncode, r.stdout + r.stderr)


class AllowMarkerWithReason(BlockscanFixture):
    """A `blockscan:allow: <reason>` in the changed section suppresses the
    violation that would otherwise fire."""

    def test_passes_with_a_stated_reason(self):
        self.write_source(
            "Reworded honesty text. "
            "<!-- blockscan:allow: deliberate, template pending -->")
        self.stage_all()
        r = self.run_staged()
        self.assertEqual(0, r.returncode, r.stdout + r.stderr)
        self.assertIn("suppressed: 1", r.stdout)


class AllowMarkerWithoutReason(BlockscanFixture):
    """A bare mention of the marker text, with no reason, exempts nothing —
    the same tightened contract every sibling scanner's allow marker uses."""

    def test_bare_mention_does_not_exempt(self):
        self.write_source(
            "Reworded honesty text. Mentions blockscan:allow in passing.")
        self.stage_all()
        r = self.run_staged()
        self.assertEqual(1, r.returncode, r.stdout + r.stderr)
        self.assertIn("violation", r.stdout)

    def test_empty_reason_does_not_exempt(self):
        self.write_source(
            "Reworded honesty text. <!-- blockscan:allow: -->")
        self.stage_all()
        r = self.run_staged()
        self.assertEqual(1, r.returncode, r.stdout + r.stderr)


class RenamedHeadingReds(BlockscanFixture):
    """A mapped heading that no longer resolves in its source doc — renamed,
    removed, or duplicated — is a config error (the map going stale), never
    a silent pass and never suppressible by an allow marker."""

    def test_renamed_heading_is_a_config_error(self):
        (self.root / "docs" / "method" / "APEX.md").write_text(
            "# Apex\n\n## Honesty absolutely\n\nRenamed heading body.\n"
            "## Adaptation is continuous\n\nOther text.\n")
        self.stage_all()
        r = self.run_staged()
        self.assertEqual(2, r.returncode, r.stdout + r.stderr)
        self.assertIn("stale-heading", r.stdout)

    def test_renamed_heading_also_reds_whole_tree_check(self):
        (self.root / "docs" / "method" / "APEX.md").write_text(
            "# Apex\n\n## Honesty absolutely\n\nRenamed heading body.\n"
            "## Adaptation is continuous\n\nOther text.\n")
        r = self.run_check()
        self.assertEqual(2, r.returncode, r.stdout + r.stderr)
        self.assertIn("stale-heading", r.stdout)

    def test_duplicated_heading_is_ambiguous_and_reds(self):
        (self.root / "docs" / "method" / "APEX.md").write_text(
            f"# Apex\n\n{self.HEADING}\n\nFirst copy.\n"
            f"{self.HEADING}\n\nSecond copy — a genuine duplicate.\n"
            "## Adaptation is continuous\n\nOther text.\n")
        r = self.run_check()
        self.assertEqual(2, r.returncode, r.stdout + r.stderr)
        self.assertIn("stale-heading", r.stdout)


class UnknownBulletIdReds(BlockscanFixture):
    """A map entry whose anchor does not resolve to exactly one bullet in
    the region or the template — a hand-edited map drifting from the prose
    it points at — is a config error, not a silent skip."""

    def test_anchor_missing_from_region_and_template(self):
        bad_map = json.loads(
            (self.root / "tools" / "blockscan_map.json").read_text())
        bad_map["bullets"]["ghost"] = {
            "anchor": "**Does not exist anywhere:**",
            "sources": [{"path": "docs/method/APEX.md",
                        "heading": "## Adaptation is continuous"}],
        }
        (self.root / "tools" / "blockscan_map.json").write_text(json.dumps(bad_map))
        r = self.run_check()
        self.assertEqual(2, r.returncode, r.stdout + r.stderr)
        self.assertIn("missing-bullet", r.stdout)

    def test_duplicated_anchor_is_ambiguous_and_reds(self):
        # Two bullets sharing one anchor text makes it unresolvable, the
        # same "ambiguous is not a free pick" rule as a duplicated heading.
        self.write_region(
            "- **The apex:** Original block wording.\n"
            "- **The apex:** A second, unrelated bullet with the same lead-in.\n")
        r = self.run_check()
        self.assertEqual(2, r.returncode, r.stdout + r.stderr)
        self.assertIn("missing-bullet", r.stdout)


class ExtractionHelpers(unittest.TestCase):
    """Unit-level coverage of the text-extraction primitives, independent of
    git or the CLI."""

    def test_extract_section_is_non_recursive(self):
        text = ("## Honesty is absolute\n\nTop text.\n\n"
               "### A nested subsection\n\nNested text.\n\n"
               "## Adaptation is continuous\n\nOther.\n")
        section = bs.extract_section(text, "## Honesty is absolute")
        self.assertNotIn("Nested text.", section)
        self.assertIn("Top text.", section)

    def test_extract_bullet_stops_at_next_top_bullet(self):
        region = ("## Doctrine\n\n"
                 "- **First:** some prose spanning\n  two lines.\n"
                 "- **Second:** other bullet.\n")
        found = bs.extract_bullet(region, "**First:**")
        self.assertIsNotNone(found)
        text, _ = found
        self.assertIn("two lines.", text)
        self.assertNotIn("Second", text)

    def test_extract_bullet_ambiguous_anchor_returns_none(self):
        region = "- **X:** one.\n- **X:** two.\n"
        self.assertIsNone(bs.extract_bullet(region, "**X:**"))


if __name__ == "__main__":
    unittest.main()
