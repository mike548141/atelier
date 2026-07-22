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


REVIEWS_TEMPLATE = ROOT / "docs" / "build" / "templates" / "docs" / "reviews" / "README.md"
REVIEW_SKILL = ROOT / "skills" / "review-brief" / "SKILL.md"


class ReviewsTemplateTest(unittest.TestCase):
    """docs/build/templates/docs/reviews/README.md — the stamped pointer.

    2026-07-19 cold-pass F7: this file drifted once as an unmarked fork (it
    carried a diff-shaped trigger its parent had retired), and after the
    fork→pointer conversion nothing mechanical pinned the conversion's
    load-bearing lines. Pin the invariants, not the prose — the file may be
    edited deliberately, but it must stay a marked, narrowing-free pointer
    keyed on the commitment trigger.
    """

    def setUp(self):
        self.text = REVIEWS_TEMPLATE.read_text()
        # Wrap- and emphasis-insensitive view: assertions pin wording, not
        # where a line happens to break.
        self.flat = " ".join(self.text.replace("*", "").split())

    def test_carries_the_stamped_pointer_header(self):
        """An unmarked local copy is how it drifted; the marker is the fix."""
        self.assertIn("STAMPED POINTER, NOT A SECOND SOURCE", self.text)
        self.assertIn("docs/method/REVIEW.md", self.text)
        self.assertIn("Narrowing-free", self.text)

    def test_trigger_is_commitment_not_artefact(self):
        """The one trigger question, stated in the parent's grammar."""
        self.assertIn("The trigger is commitment, not artefact", self.flat)
        self.assertIn("what will come to rest on it once it is trusted",
                      self.flat)

    def test_prose_is_not_exempted(self):
        """The old fork affirmatively exempted "a doc line"; the conversion
        replaced that with its opposite — keep the opposite."""
        self.assertIn("not routine by virtue of being prose", self.flat)

    def test_placeholder_is_exactly_atelier_path(self):
        """create-repo's stamp step fills <atelier-path> here (its prove-the-
        stamp grep covers the whole tree since cold-pass F1); of the stamp
        vocabulary, exactly that one may appear. (The Format section's
        <YYYY-MM-DD>-style filename patterns are not stamp placeholders.)"""
        found = set(re.findall(r"<[a-z/ A-Z-]+>", self.text)) & PLACEHOLDERS
        self.assertEqual(found, {"<atelier-path>"})
        self.assertIn("<atelier-path>", self.text)


TEMPLATES_DIR = ROOT / "docs" / "build" / "templates"

# The whole-set inventory: stamp placeholders may appear in the template set
# ONLY where create-repo's stamp step fills them. Adding a token to a new
# file means updating the skill's fill step AND this inventory, together.
STAMP_INVENTORY = {
    ("CLAUDE.md", "<atelier-path>"),
    ("CLAUDE.md", "<SHA>"),
    ("CLAUDE.md", "<owner/repo>"),
    ("CLAUDE.md", "<visibility fact>"),
    ("CONTRIBUTING.md", "<atelier-path>"),
    ("docs/reviews/README.md", "<atelier-path>"),
}


class TemplateSetPlaceholderInventoryTest(unittest.TestCase):
    """2026-07-19 applied-batch cold-pass G2: floor.yml carried a stamp-shaped
    `<SHA>` slot the stamp step never fills, making the whole-tree
    prove-the-stamp grep unsatisfiable on every full scaffold (G1) — and no
    test saw it, because each pin was per-file. This is the set-wide pin: the
    exact (file, token) pairs the stamp step fills, nothing else, anywhere."""

    def test_stamp_tokens_only_where_the_stamp_step_fills_them(self):
        found = set()
        for path in TEMPLATES_DIR.rglob("*"):
            if not path.is_file():
                continue
            text = path.read_text()
            rel = path.relative_to(TEMPLATES_DIR).as_posix()
            for token in PLACEHOLDERS:
                if token in text:
                    found.add((rel, token))
        self.assertEqual(
            found,
            STAMP_INVENTORY,
            "stamp-placeholder inventory drifted: a token appeared in a "
            "template the stamp step doesn't fill (it would make the "
            "prove-the-stamp grep permanently red — G1), or a filled "
            "surface lost its token. Change create-repo's fill step and "
            "this inventory together.",
        )


class ReviewBriefSkillTest(unittest.TestCase):
    """skills/review-brief/SKILL.md — the plugin copy of the same doctrine.

    2026-07-19 cold-pass F3: the consolidation sweep missed skills/, leaving
    the old artefact-grammar trigger live on the widest propagation surface.
    Same pin, same reason.
    """

    def setUp(self):
        self.text = REVIEW_SKILL.read_text()

    def test_marked_as_stamped_copy(self):
        self.assertIn("STAMPED COPY, NOT A SECOND SOURCE", self.text)

    def test_trigger_is_commitment_not_artefact(self):
        self.assertIn("The trigger is commitment, not artefact",
                      self.text.replace("*", ""))

    def test_old_artefact_grammar_evicted(self):
        """The exact phrases F3 anchored on must not return."""
        for phrase in ("a change earns a review",
                       "does this change even earn a review",
                       "The build makes the claim"):
            self.assertNotIn(phrase, self.text)


REVIEW_DOCTRINE = ROOT / "docs" / "method" / "REVIEW.md"


def canonical_lenses() -> list:
    """Lens names from REVIEW.md's numbered list — the one source.

    Bounded to the 'What a review actually checks' section so the
    independence rules (1–4) and the lifecycle steps, also numbered+bold
    lists, are never mistaken for lenses."""
    text = REVIEW_DOCTRINE.read_text()
    start = text.index("## What a review actually checks")
    end = text.index("\n## ", start + 1)
    return re.findall(r"^\d+\. \*\*(.+?)\*\*", text[start:end], re.M)


class LensRosterParityTest(unittest.TestCase):
    """2026-07-21 cold-pass SL1: lens 4 landed in REVIEW.md while the
    review-brief skill still taught three lenses — the second shipping of the
    F3 drift class, this time on the roster itself. The skill may compress
    the parent's prose; the lens ROSTER it may never shrink. Same rule for
    the child reviews template, which compresses the lenses into its
    house-practice sentence."""

    def test_canonical_roster_parses(self):
        lenses = canonical_lenses()
        self.assertGreaterEqual(
            len(lenses), 4,
            "REVIEW.md's lens list no longer parses — the parity tests "
            "below are checking against nothing",
        )

    def test_skill_names_every_canonical_lens(self):
        skill = REVIEW_SKILL.read_text()
        for lens in canonical_lenses():
            self.assertIn(
                lens, skill,
                f"skills/review-brief/SKILL.md is missing lens {lens!r} — "
                "the skill must name every lens REVIEW.md enumerates "
                "(add one there, add it here, same commit)",
            )

    def test_skill_lens_count_words_match_roster(self):
        """'run all three' outlived lens 4 in prose; pin the count words."""
        n = len(canonical_lenses())
        words = {3: "three", 4: "four", 5: "five", 6: "six"}
        skill_flat = " ".join(REVIEW_SKILL.read_text().split()).lower()
        for count, word in words.items():
            if count != n:
                self.assertNotIn(
                    f"{word} lenses", skill_flat,
                    f"the skill still says '{word} lenses' while REVIEW.md "
                    f"enumerates {n}",
                )

    def test_reviews_template_carries_the_security_lens(self):
        """The child floor compresses the roster; security & privacy is the
        lens whose omission SL1's cycle existed to catch — pin it."""
        flat = " ".join(REVIEWS_TEMPLATE.read_text().split()).lower()
        self.assertIn("security & privacy is a must on every review", flat)


if __name__ == "__main__":
    unittest.main()
