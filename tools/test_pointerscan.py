"""Tests for tools/pointerscan.py — the queued-review pointer's two guards.

The tests are shaped by what actually goes wrong, and every fixture below is a
real pointer from this repo's history rather than an invented one. Two things
carry the weight:

  * THE SCOPE. A guard scoped to the marker glyph alone misses the one specimen
    still standing, so most of these tests are about which items are IN and,
    just as hard, which are OUT. Getting scope wrong makes a check that runs,
    exits 0 and covers nothing — this programme's organising defect.
  * THE FALSE POSITIVES. A pointer citing the verdicts of a prior cycle while
    queuing a further pass is CORRECT, and so is an archived item narrating a
    cycle that closed. Both were reported by earlier cuts of these rules and
    both are pinned here, because a guard that fires on healthy edits gets
    exempted into silence.

Zero third-party deps, same as the rest of the suite.
"""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import pointerscan  # noqa: E402

Q = pointerscan.QUEUED


def dets(text):
    return sorted({f.detector for f in pointerscan.scan_text(text)})


def reasons(text, detector):
    return [f.reason for f in pointerscan.scan_text(text)
            if f.detector == detector]


class ScopeTest(unittest.TestCase):
    """What makes an item a queued-review pointer — the prior question, and the
    one this whole build turns on."""

    def test_the_marker_glyph_scopes_an_item_in(self):
        self.assertTrue(pointerscan.is_pointer(Q, "anything at all"))

    def test_the_glyph_in_the_state_prefix_scopes_an_item_in(self):
        """Shape (b): a claimed pointer carries its checkbox AND the glyph."""
        body = (f"{Q} (claimed 2026-07-26-2210, wt: a-take) **ADR 0008 review "
                "owed** — self-authored.")
        self.assertTrue(pointerscan.is_pointer("[~]", body))

    def test_an_obligation_in_an_emphasis_run_scopes_an_item_in(self):
        """Shape (c) — the LIVE specimen. No glyph anywhere; the obligation is
        stated mid-body. A marker-scoped guard misses exactly this."""
        body = ("REVIEWED 2026-07-26: PASS-WITH-FINDINGS. **ADR 0008 review "
                "owed** — self-authored, so this session may not review it.")
        self.assertTrue(pointerscan.is_pointer("[ ]", body))

    def test_an_item_with_no_checkbox_at_all_scopes_in(self):
        """Shape (d): the five residues open with a verdict stamp."""
        text = ("- REVIEWED 2026-07-26: PASS-WITH-FINDINGS 0M/3m/3n\n"
                f"  — [verdict](reviews/x-cold.md). **{Q} review queued for a\n"
                "  non-author** (self-authored doctrine, rule 4).\n")
        items = pointerscan.parse_items(text)
        self.assertEqual(len(items), 1)
        self.assertTrue(pointerscan.is_pointer(items[0].marker, items[0].body))

    def test_prose_about_pointers_is_out_of_scope(self):
        """The discriminating case, and why the rule reads EMPHASIS rather than
        the whole body: this build's own funding entry quotes the residues'
        wording and asks its own open questions. An author asserting an
        obligation about their item bolds it; an author writing prose about
        obligations does not."""
        body = ("**Mechanise the pointer grammar.** All five said \"review "
                "queued\" when the review had run. Is this the same rung the "
                "0820 record rejected?")
        self.assertFalse(pointerscan.is_pointer("[ ]", body))
        self.assertEqual(dets(f"- [ ] {body}\n"), [])

    def test_a_backticked_marker_is_documentation_not_a_claim(self):
        """stampscan's context-blindness lesson at the point it bites hardest:
        the doctrine describing this convention must not trip it."""
        body = f"**Legend.** `{Q}` means review queued for a non-author."
        self.assertFalse(pointerscan.is_pointer("", body))

    def test_a_completed_item_is_never_a_pointer(self):
        """The checkbox is a work-owed tri-state (Mike, 2026-07-22): `[x]`
        means no more work is owed, so an obligation phrase inside one is
        narration of a closed cycle. Measured — without this the guard reported
        an archived 2026-07-13 item closing with a pass-owed cross-reference."""
        body = ("**Cold review of CONCURRENCY.** RAN 2026-07-13: "
                "**PASS-WITH-FINDINGS**, verdict in reviews/x.md. "
                "**Applied-batch cold pass owed** (above).")
        self.assertFalse(pointerscan.is_pointer("[x]", body))


class GrammarTest(unittest.TestCase):
    """Detector 1 — what a pointer may say."""

    def test_the_live_specimen_is_flagged(self):
        """The must-flag case the build exists for: instance 1, still standing
        when this shipped. It trips BOTH legs — the seeded question and the
        instruction — which is the shape the finding described."""
        text = ("- [ ] REVIEWED 2026-07-26: PASS-WITH-FINDINGS 3M/5m/1L/1n —\n"
                "      [verdict](reviews/adr0008-cold.md). **ADR 0008 review\n"
                "      owed** — self-authored (rule 4). Aim a reviewer at the\n"
                "      one real trade: moving every repo onto a floating\n"
                "      caller swaps a slow silent failure for a fast loud\n"
                "      estate-wide one. Is that right for a security floor?\n")
        self.assertIn("grammar", dets(text))
        self.assertEqual(len(reasons(text, "grammar")), 2)

    def test_instance_three_is_flagged(self):
        """Written at ff8080b: the author seeded the pass's first question and
        volunteered his own doubt about his verdict."""
        text = (f"- {Q} **B4 — the roadmap-deletion guard.** Delta: the tool\n"
                "  and its tests. Intent record: the Track B session entry.\n"
                "  **The pass's first question is whether a 26.9% firing rate\n"
                "  is the right ground for the verdict.**\n")
        self.assertIn("first question", " ".join(reasons(text, "grammar")))

    def test_instance_three_stripped_is_silent(self):
        """Stripped at 7ca1f1d — the must-stay-silent half of the same pointer,
        and the corpus's own model of a compliant one. It still carries a tier
        AND a pass type, which is the point of the FG6 ruling below."""
        text = (f"- {Q} **B4 — the roadmap-deletion guard: the item, and the\n"
                "  work addressing it.** Delta: the tool, its tests, the B4\n"
                "  entry carrying the measurement and the verdict. Intent\n"
                "  record: the Track B session record. Cold pass owed per rule\n"
                "  4; the tier bar applies (cold review passes run on Fable).\n")
        self.assertEqual(dets(text), [])

    def test_pass_type_is_a_lawful_field(self):
        """FG6, settled on the corpus: pass type sits beside {delta, intent
        record, tier}. Tier is already lawful and is the same class of fact —
        both route the review; neither says anything about the delta's merits.
        The ceiling forbids an evaluative ACCOUNT, not routing."""
        text = (f"- [ ] **F1 — rebuild the model from base.** **{Q} Review\n"
                "      queued for a non-author.** Cold passes run on **Fable**.\n"
                "      *Delta:* this item. *Intent record:* [the record](x.md).\n"
                "      Design/intent pass per REVIEW.md section *Review the\n"
                "      design, not only the build*.\n")
        self.assertEqual(dets(text), [])

    def test_a_question_anywhere_in_a_pointer_fires(self):
        text = f"- {Q} **Review queued.** Delta: x. Is the tier right?\n"
        self.assertIn("question", " ".join(reasons(text, "grammar")))

    def test_a_backticked_question_mark_does_not_fire(self):
        text = (f"- {Q} **Review queued.** Delta: the `--help?` flag handling "
                "in the parser. Intent record: the session entry.\n")
        self.assertEqual(dets(text), [])


class CycleStateTest(unittest.TestCase):
    """Detector 2 — whether the pointer is still true."""

    RESIDUE = (
        "- REVIEWED 2026-07-26: PASS-WITH-FINDINGS 0M/3m/3n —\n"
        "  [verdict](reviews/evidence-escalation-cold.md); EE1-EE6 await\n"
        "  Mike's ruling (rule 3). **Capture to doctrine** — APPLIED\n"
        f"  2026-07-26. **{Q} review queued for a non-author**\n"
        "  (self-authored doctrine, rule 4). Rides the normal review cycle\n"
        "  when a qualifying session takes it.\n")

    def test_a_stale_residue_is_flagged(self):
        self.assertIn("cycle", dets(self.RESIDUE))

    def test_the_state_is_named_not_just_the_contradiction(self):
        """The sharper defect the record names: all five said the review was
        queued when what was owed was the principal's RULING. A guard that only
        knows a verdict exists cannot say that."""
        self.assertIn("ruling is what is owed",
                      " ".join(reasons(self.RESIDUE, "cycle")))

    def test_the_cleaned_form_is_silent(self):
        """As 49f1a8f left it. Note it still carries the words "Review queued"
        — so the guard cannot key on the phrase alone; the resolution is what
        clears it."""
        cleaned = (
            "- REVIEWED 2026-07-26: PASS-WITH-FINDINGS 0M/3m/3n —\n"
            "  [verdict](reviews/evidence-escalation-cold.md); EE1-EE6 await\n"
            "  Mike's ruling (rule 3). **Capture to doctrine** — APPLIED\n"
            "  2026-07-26. **Review queued at landing** (self-authored\n"
            "  doctrine, rule 4) — **taken**; the verdict is above.\n")
        self.assertEqual(dets(cleaned), [])

    def test_a_pointer_queuing_a_further_pass_is_not_stale(self):
        """The false-positive class that would have earned this an exemption.
        This repo's cycles routinely queue the NEXT pass while citing the
        verdicts of the one before; order is what tells them apart. Here the
        claim leads and the verdicts follow as provenance."""
        text = (f"- {Q} **Review queued — the Track A application (A1-A5b).**\n"
                "  Rule 4: each application earns a further cold pass while a\n"
                "  MAJOR stood, and two did. **Delta:** the floor and its\n"
                "  tests. **Verdicts applied:** [ADR 0008 cold\n"
                "  pass](reviews/adr0008-cold.md).\n")
        self.assertEqual(dets(text), [])

    def test_a_genuinely_owed_pointer_is_silent(self):
        text = (f"- {Q} **Review queued for a non-author.** *Delta:* the\n"
                "  PROPAGATION.md paragraph. *Intent record:* [the session\n"
                "  record](sessions/x.md). Cold passes run on Fable.\n")
        self.assertEqual(dets(text), [])


class ParseTest(unittest.TestCase):
    def test_fenced_examples_are_not_work_items(self):
        text = f"```\n- {Q} **Review queued.** Is this right?\n```\n"
        self.assertEqual(pointerscan.parse_items(text), [])
        self.assertEqual(dets(text), [])

    def test_sub_bullets_fold_into_their_item(self):
        text = "- [ ] the head\n  - a sub-bullet\n  - and another\n"
        items = pointerscan.parse_items(text)
        self.assertEqual(len(items), 1)
        self.assertIn("another", items[0].body)

    def test_a_blockquoted_item_is_not_a_work_item(self):
        """Same rationale as sizescan's: the `>` breaks the bullet anchor, and
        quoted material is not this repo's claim about its own work."""
        text = f"> - {Q} **Review queued.** Is this right?\n"
        self.assertEqual(pointerscan.parse_items(text), [])


class HatchTest(unittest.TestCase):
    def test_the_allow_marker_exempts_an_item(self):
        text = (f"- {Q} **Review queued.** Is that right? "
                f"<!-- {pointerscan.ALLOW_MARKER} quoting a prior finding -->\n")
        self.assertEqual(dets(text), [])


class InvocationTest(unittest.TestCase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "pointerscan.py"), *args],
            capture_output=True, text=True)

    def test_selftest_passes(self):
        self.assertEqual(self._run("--selftest").returncode, 0)

    def test_it_never_fails_a_build(self):
        """Advisory by construction, and this is the contract it is wired in
        under. A finding must still exit 0."""
        with tempfile.TemporaryDirectory() as td:
            roadmap = Path(td) / "ROADMAP.md"
            roadmap.write_text(f"- {Q} **Review queued.** Is that right?\n",
                               encoding="utf-8")
            r = self._run("--root", td, ".")
            self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
            self.assertIn("pointerscan:", r.stdout)
            self.assertIn("ADVISORY ONLY", r.stdout)

    def test_a_clean_tree_says_so(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "ROADMAP.md").write_text(
                "- [ ] **Ordinary work.** Nothing queued here.\n",
                encoding="utf-8")
            r = self._run("--root", td, ".")
            self.assertEqual(r.returncode, 0)
            self.assertIn("clean", r.stdout)

    def test_only_roadmaps_are_read(self):
        """Pointing this at prose is the fires-on-every-author failure the 0820
        record rejected. The grammar is a ROADMAP convention and nothing else
        in a tree carries it."""
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "NOTES.md").write_text(
                f"- {Q} **Review queued.** Is that right?\n", encoding="utf-8")
            r = self._run("--root", td, ".")
            self.assertEqual(r.returncode, 0)
            self.assertIn("clean", r.stdout)

    def test_a_missing_root_is_an_error_not_a_silent_pass(self):
        self.assertEqual(self._run("--root", "/no/such/dir").returncode, 2)

    def test_a_missing_path_is_an_error_not_a_silent_pass(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(self._run("--root", td, "nope").returncode, 2)

    def test_json_mode_is_parseable(self):
        import json
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "ROADMAP.md").write_text(
                f"- {Q} **Review queued.** Is that right?\n", encoding="utf-8")
            r = self._run("--root", td, "--json", ".")
            self.assertEqual(r.returncode, 0)
            self.assertEqual(len(json.loads(r.stdout)["findings"]), 1)


class LiveSpecimenTest(unittest.TestCase):
    """The day-one proof, run against this repo's real roadmap. Written to
    survive the fix: once the live specimens are cleaned this asserts only that
    the scan runs and reports honestly, which is the durable claim."""

    def test_the_repo_roadmap_scans_without_error(self):
        roadmap = TOOLS_DIR.parent / "docs" / "ROADMAP.md"
        if not roadmap.is_file():
            self.skipTest("no docs/ROADMAP.md in this checkout")
        findings = pointerscan.scan(["docs"], TOOLS_DIR.parent)
        for f in findings:
            self.assertIn(f.detector, ("grammar", "cycle"))
            self.assertTrue(f.reason)
            self.assertGreater(f.line, 0)


if __name__ == "__main__":
    unittest.main()


class Allowances(unittest.TestCase):
    """GUARDS.md rule (c) — a marker with no reason is a mention."""

    def test_bare_marker_without_reason_is_not_an_allowance(self):
        self.assertIsNone(pointerscan.parse_allow("x pointerscan:allow"))
        self.assertIsNone(pointerscan.parse_allow("x pointerscan:allow:"))

    def test_marker_with_reason_allows(self):
        self.assertEqual("", pointerscan.parse_allow("x pointerscan:allow: a reason"))
