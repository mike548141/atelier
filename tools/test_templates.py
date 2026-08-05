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


# stampscan's marker lines bracket the stamped block but are not part of it:
# they are HTML comments, invisible in rendered Markdown, and PROPAGATION's
# canonical region does not carry them. Dropping them here is what let the
# template's `stamp:end` move off the `---` divider onto its own line
# (2026-07-26 cold pass ST7) — that placement compromise existed only to keep
# this slice verbatim, and it was the reason stampscan had to match its end
# marker anywhere on a line instead of anchoring it.
_STAMP_MARKER_LINE = re.compile(r"^\s*<!--\s*stamp:(?:begin|end)\b.*-->\s*$")


def template_block() -> str:
    """The stamped copy: from the block heading to the first --- divider,
    with stampscan's marker lines removed."""
    text = TEMPLATE.read_text()
    start = text.index(BLOCK_HEADING)
    end = text.index("\n---", start)
    body = "\n".join(ln for ln in text[start:end].splitlines()
                     if not _STAMP_MARKER_LINE.match(ln))
    return body.rstrip()


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

    def test_stamp_markers_sit_on_their_own_lines(self):
        """2026-07-26 cold pass ST7. The end marker used to hide inline on the
        `---` divider (`---<!-- stamp:end -->`) purely to keep the slice above
        verbatim — and that placement forced stampscan to match its end marker
        ANYWHERE on a line, which made an inline-code mention of the marker
        read as a stray end and reddened the floor on ordinary documentation.
        Both markers now sit on their own lines so the scanner stays anchored;
        pin that, or the compromise silently returns."""
        marker_lines = [ln for ln in TEMPLATE.read_text().splitlines()
                        if "stamp:begin" in ln or "stamp:end" in ln]
        self.assertEqual(
            2, len(marker_lines),
            "the template must carry exactly one stamp:begin/stamp:end pair")
        for ln in marker_lines:
            self.assertRegex(
                ln, r"^<!--\s*stamp:(?:begin|end)\b.*-->$",
                "a stamp marker must be alone on its line — sharing one with "
                "other content is what forced stampscan's unanchored end "
                "regex (ST7)")

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
REUSABLE_FLOOR = ROOT / ".github" / "workflows" / "floor.yml"


class ChildFloorWorkflowTest(unittest.TestCase):
    """docs/build/templates/workflows/floor.yml — what a CHILD repo holds.

    Until 2026-07-25 this was a 247-line copy naming every scanner, and that
    copy was the defect: 12 of 13 children were still running their
    scaffold-time list and had never executed five of atelier's checks (ADR
    0008). The template is now a thin caller, and the invariants worth pinning
    inverted with it — the sharpest one being that this file names NO scanner
    at all. The scanner-level invariants moved to ReusableFloorWorkflowTest
    (transport) and test_floor.py (policy).
    """

    def setUp(self):
        self.text = FLOOR.read_text()
        self.body = "\n".join(ln for ln in self.text.splitlines()
                              if not ln.lstrip().startswith("#"))

    def test_names_no_scanner(self):
        """THE invariant. A scanner named here is a scanner this repo has to
        remember to update — which is the whole failure this design removed.
        The header prose may discuss scanners; the executable body may not."""
        self.assertNotRegex(
            self.body, r"\w+scan\.py",
            "the child floor must name no scanner — add it to atelier's "
            "registry (tools/floor.py) so every repo gets it, not just this one",
        )

    def test_calls_ateliers_reusable_floor(self):
        """One source, and not a copy of it."""
        self.assertRegex(
            self.body,
            r"uses:\s*mike548141/atelier/\.github/workflows/floor\.yml@",
            "the child floor must call atelier's reusable workflow",
        )

    def test_calls_main_not_a_pinned_sha(self):
        """Newest scanner = safest for a security floor, and a pinned caller
        would re-introduce exactly the staleness ADR 0008 removed. A child may
        pin deliberately; the shipped default must not."""
        self.assertIn("floor.yml@main", self.body)

    def test_push_trigger_covers_every_branch(self):
        """2026-07-11 review N4: a push to ANY branch is publication (the
        commit is on the remote whether or not it's ever PR'd); restricting
        push to main left a never-PR'd feature branch scanned by nothing."""
        on_block = self.text[self.text.find("\non:"):self.text.find("permissions:")]
        self.assertNotIn("branches:", on_block)

    def test_least_privilege(self):
        """The floor only reads trees."""
        self.assertIn("contents: read", self.text)

    def test_points_at_the_declaration_file_for_opt_outs(self):
        """A child WILL need to opt out of something. It must be told where
        that is declared — because the old answer ('delete the scanner line')
        is now both impossible and invisible, and an undirected maintainer
        will otherwise reach for --no-verify."""
        self.assertIn(".atelier-floor.json", self.text)

    def test_false_positive_hatches_documented(self):
        """2026-07-11 review N6: a child whose own tree legitimately trips a
        scanner (its own fake-secret fixtures, a committed build-output dir)
        must find the hatch here, not in atelier's internals. Still true when
        the file is thin — arguably more so, since there is now no scanner line
        nearby to hint at it."""
        for hatch in (".secretscanignore", ".leakscanignore", ".linkscanignore"):
            self.assertIn(hatch, self.text)


class ReusableFloorWorkflowTest(unittest.TestCase):
    """.github/workflows/floor.yml — atelier's hosted floor, called by everyone.

    This is the transport half of ADR 0008. Because every repo in the estate
    calls THIS file, a mistake here is a mistake everywhere at once — so the
    invariants that used to be pinned per-child are pinned once, here.
    """

    def setUp(self):
        self.text = REUSABLE_FLOOR.read_text()
        self.runs = [ln for ln in self.text.splitlines()
                     if "run:" in ln or "python3" in ln]

    def test_is_callable_by_children(self):
        self.assertIn("workflow_call:", self.text)

    def test_fetches_atelier_one_source(self):
        self.assertIn("repository: mike548141/atelier", self.text)

    def test_floor_scoped_to_the_calling_repo_not_the_workspace(self):
        """A whole-workspace scan would read atelier's own tree, which carries
        deliberate fake-secret fixtures. `--root repo` is load-bearing."""
        # `--selftest` and `--list` read no tree, so they need no scoping.
        floor_runs = [ln for ln in self.runs
                      if "floor.py" in ln
                      and "--selftest" not in ln and "--list" not in ln]
        self.assertTrue(floor_runs, "no floor.py run line found")
        for ln in floor_runs:
            self.assertIn("--root repo", ln)
            self.assertNotRegex(ln, r"--root\s+\.\s")

    def test_selftests_run_before_the_floor(self):
        """2026-07-11 review N5: prove the fetched instruments before trusting
        their pass. A scanner that cannot detect its own fixtures goes red
        here, not green below."""
        self.assertIn("--selftest", self.text)
        self.assertLess(self.text.find("--selftest"),
                        self.text.find("--plane ci"),
                        "selftests must run before the floor they vouch for")

    def test_selftests_are_driven_by_the_registry(self):
        """A hard-coded selftest list would be a second copy of the scanner
        list living one directory from the first — the same bug, smaller."""
        self.assertIn("floor.py --list", self.text)

    def test_least_privilege(self):
        self.assertIn("contents: read", self.text)

    def test_signature_verification_kept_out_of_the_registry(self):
        """signscan needs a trust list resolved from the CALLER's pin, never
        floating main (2026-07-12 review G7). It is not a tree scanner, so it
        stays here as explicit steps rather than being forced into floor.py."""
        self.assertIn("signscan.py", self.text)
        self.assertIn("allowed_signers", self.text)


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


QUEUE_RUN_SKILL = ROOT / "skills" / "queue-run" / "SKILL.md"
CONCURRENCY = ROOT / "docs" / "method" / "CONCURRENCY.md"


def queue_run_section() -> str:
    """CONCURRENCY.md § Orchestrated queue runs — the skill's one source."""
    text = CONCURRENCY.read_text()
    start = text.index("## Orchestrated queue runs")
    end = text.find("\n## ", start + 1)
    return text[start:] if end == -1 else text[start:end]


def canonical_stop_conditions() -> list:
    """The bold stop names from the section's own bullet list, bounded to
    the stop-conditions block so other bold bullets are never mistaken
    for stops."""
    section = queue_run_section()
    start = section.index("A run stops on one")
    end = section.index("It ends with a", start)
    return re.findall(r"^- \*\*(.+?)\*\*", section[start:end], re.M)


class QueueRunSkillTest(unittest.TestCase):
    """skills/queue-run/SKILL.md — third stamped-copy skill, same pin as
    review-brief (2026-07-19 F3, 2026-07-21 SL1: this drift class has
    shipped twice; 2026-07-23 QR6 ruled the pin mandatory at birth)."""

    def setUp(self):
        self.text = QUEUE_RUN_SKILL.read_text()
        self.flat = " ".join(self.text.split())

    def test_marked_as_stamped_copy(self):
        self.assertIn("STAMPED COPY, NOT A SECOND SOURCE", self.text)

    def test_points_at_both_canonical_homes(self):
        for pointer in ("CONCURRENCY.md` § Orchestrated queue runs",
                        "ECONOMICS.md` § The orchestrated-run tier split"):
            self.assertIn(
                pointer, self.flat,
                f"the skill lost its canonical pointer {pointer!r} — it is "
                "a delivery vehicle, not a second source",
            )

    def test_canonical_stop_roster_parses(self):
        self.assertEqual(
            len(canonical_stop_conditions()), 4,
            "CONCURRENCY.md's stop-condition list no longer parses as four "
            "bold bullets — the parity test below is checking nothing",
        )

    def test_skill_names_every_stop_condition(self):
        for stop in canonical_stop_conditions():
            self.assertIn(
                stop, self.flat,
                f"skills/queue-run/SKILL.md is missing stop condition "
                f"{stop!r} — the skill must name every stop CONCURRENCY.md "
                "enumerates (change one, change both, same commit)",
            )

    def test_rule4_criterion_phrase_in_both(self):
        """The criterion is quoted, not paraphrased, on both surfaces —
        paraphrase is where the authorship-vs-spawn drift (QR1) hid."""
        phrase = "neither started nor instructed"
        self.assertIn(phrase, self.flat)
        self.assertIn(phrase, " ".join(queue_run_section().split()))

    def test_chain_pin_in_both(self):
        """QR1's fix: a run never extends itself. Pin the sentence on both
        surfaces so a future rewording can't quietly drop it."""
        phrase = "starts or instructs its own successor"
        self.assertIn(phrase, self.flat)
        self.assertIn(phrase, " ".join(queue_run_section().split()))

    def test_item_text_never_overrides_in_both(self):
        """QR4's injection guard (QA1): the run's trust boundary is pinned
        on both surfaces, same treatment as the chain pin."""
        phrase = "never overrides"
        self.assertIn(phrase, self.flat)
        self.assertIn(phrase, " ".join(queue_run_section().split()))

    def test_loses_nothing_overclaim_evicted(self):
        """QR7: the honest form is 'at most the item in flight' — held on
        both ruled surfaces (QA2: the README bullet had no pin)."""
        self.assertNotIn("loses nothing", self.flat.lower())
        readme = " ".join((ROOT / "README.md").read_text().split()).lower()
        self.assertNotIn("loses nothing", readme)


if __name__ == "__main__":
    unittest.main()
