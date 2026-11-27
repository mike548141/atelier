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

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import pointerscan  # noqa: E402
import memprobe  # noqa: E402

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


class DeltaBoundTest(unittest.TestCase):
    """PK21 (cold pass on `160/1810`): "the commits citing X" missed three of
    the seven commits on that pointer's own path list. A pointer names its delta
    by path and a bound; a citation alone is advisory-flagged under grammar.
    Every value here is synthetic."""

    CITED = (f"- {Q} **Rule-4 cold pass queued: the widget fixes.** Tier: the\n"
             "      review tier. *Delta, scoped to paths:* `tools/widget.py`,\n"
             "      `docs/widget.md`: the commits citing `210/600`, on `main`,\n"
             "      after `a1cc5f2d`.\n")

    def reasons(self, text):
        return [r for r in reasons(text, "grammar") if "citation" in r]

    def test_a_delta_named_by_citation_alone_is_flagged(self):
        self.assertEqual(dets(self.CITED), ["grammar"])
        self.assertEqual(len(self.reasons(self.CITED)), 1)

    def test_one_start_hash_is_not_a_bound(self):
        """The citation still selects; the start hash only trims."""
        self.assertEqual(len(self.reasons(self.CITED)), 1)

    def test_a_commit_range_is_a_bound(self):
        text = self.CITED.replace("after `a1cc5f2d`", "`a1cc5f2d..9b4a8f8f`")
        self.assertEqual(self.reasons(text), [])
        three = self.CITED.replace("after `a1cc5f2d`",
                                   "`a1cc5f2d...9b4a8f8f`")
        self.assertEqual(self.reasons(three), [])

    def test_two_named_hashes_are_a_bound(self):
        text = self.CITED.replace("after `a1cc5f2d`",
                                  "`a1cc5f2d`, `9b4a8f8f`")
        self.assertEqual(self.reasons(text), [])

    def test_the_citing_family_is_flagged(self):
        """DP19: "commits citing" alone was matched; the same selector in
        other words passed."""
        for phrase in ("commits that cite", "commits which cite",
                       "commits naming", "commits that name",
                       "commits referencing", "commits that mention",
                       "commit citing"):
            text = self.CITED.replace("commits citing", phrase)
            self.assertEqual(len(self.reasons(text)), 1, phrase)

    def test_a_bare_verb_about_commits_is_not_a_selector(self):
        """"commits name their files" says what commits do; it picks none."""
        text = (f"- {Q} **Rule-4 cold pass queued: the scanner, commits name\n"
                "      their files.** *Delta:* `tools/x.py` after `a1cc5f2d`.\n")
        self.assertEqual(self.reasons(text), [])

    def test_two_hashes_not_bound_as_the_delta_do_not_silence_it(self):
        """DP19: any two hashes anywhere silenced the flag, a start hash and a
        pinned verdict, or two session ids, included."""
        pinned = self.CITED + "      Briefed, pinned at `6ddbead2`.\n"
        self.assertEqual(len(self.reasons(pinned)), 1)
        sessions = self.CITED + ("      Barred: sessions `0ee74059`, "
                                 "`14c2530d`.\n")
        self.assertEqual(len(self.reasons(sessions)), 1)

    def test_a_hash_list_named_as_the_delta_is_a_bound(self):
        text = self.CITED + ("      The delta is `a1cc5f2d`, `9b4a8f8f` and\n"
                             "      `c0ffee12`.\n")
        self.assertEqual(self.reasons(text), [])

    def test_a_word_spelled_in_hex_is_not_a_hash(self):
        text = self.CITED.replace("after `a1cc5f2d`",
                                  "after defaced and effaced")
        self.assertEqual(len(self.reasons(text)), 1)

    def test_a_delta_with_no_citation_phrase_is_silent(self):
        text = (f"- {Q} **Rule-4 cold pass queued: the widget fixes.** Tier:\n"
                "      the review tier. *Delta:* `tools/widget.py` after\n"
                "      `a1cc5f2d`. Intent record: the session entry.\n")
        self.assertEqual(dets(text), [])

    def test_the_phrase_in_a_code_span_is_a_mention(self):
        text = (f"- {Q} **Rule-4 cold pass queued: the scanner.** Delta: the\n"
                "      scan of the phrase `commits citing` in `tools/x.py`.\n")
        self.assertEqual(self.reasons(text), [])

    def test_a_scoped_marker_exempts_it(self):
        text = self.CITED.replace(
            "Tier:", "pointerscan:allow:grammar: synthetic. Tier:")
        self.assertEqual(self.reasons(text), [])


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


class QueueStateTest(unittest.TestCase):
    """Detector 3 (130/020) — the queued glyph means a review is queued and its
    pass has not returned a verdict, because that glyph is what a session
    counts to size the review queue. Both miscounts are pinned: a landed pass
    still wearing it (2026-10-03: "20 queued" when none were) and a queued
    review written without it (2026-10-05)."""

    LANDED = (
        f"- {Q} **Rule-4 cold pass queued: the widget rule.** Delta: the\n"
        "      paragraph. Intent record: the session record.\n"
        "      - [ ] **The pass RAN 2026-09-26 and the cycle stays OPEN — a\n"
        "            MAJOR stands.** [verdict](../../reviews/w-cold.md).\n")

    def test_a_landed_pass_still_wearing_the_glyph_is_flagged(self):
        """The 27-item shape: claim in the lead, outcome beneath. The order
        rule reads this as healthy (130/010); this detector does not."""
        self.assertEqual(dets(self.LANDED), ["state"])
        self.assertIn("verdict has landed",
                      " ".join(reasons(self.LANDED, "state")))

    def test_a_stated_cycle_outcome_alone_is_landing_evidence(self):
        text = (f"- {Q} **Rule-4 cold pass queued: x.** Delta: y.\n"
                "      - the cycle CLOSES on this pass (no MAJOR)\n")
        self.assertEqual(dets(text), ["state"])

    def test_a_claimed_pass_still_running_is_not_landed(self):
        """A taken pointer keeps its glyph while the pass runs; a claim stamp
        is not a verdict."""
        text = (f"- [~] {Q} (claimed 2026-10-06-0100, wt: r) **Rule-4 cold "
                "pass queued: x.** Delta: y. CLAIMED for the review run.\n")
        self.assertEqual(dets(text), [])

    def test_the_glyph_off_with_the_owed_work_named_is_silent(self):
        fixed = self.LANDED.replace(f"- {Q} ", "- [ ] 🎯 ", 1)
        self.assertEqual(dets(fixed), [])
        closed = self.LANDED.replace(f"- {Q} ", "- [x] ", 1)
        self.assertEqual(dets(closed), [])

    def test_a_verdict_link_alone_is_not_landing(self):
        """A pointer queuing a further pass cites the verdicts before it."""
        text = (f"- {Q} **Review queued — the application.** Delta: x.\n"
                "  **Verdicts applied:** [prior pass](reviews/p-cold.md),\n"
                "  which returned PASS-WITH-FINDINGS.\n")
        self.assertEqual(dets(text), [])

    def test_a_queued_review_without_the_glyph_is_flagged(self):
        text = ("- [ ] 🛑 **Rule-4 cold pass queued: the hardening.** Tier:\n"
                "      the review tier. Delta: the tool. Intent record: x.\n")
        self.assertEqual(dets(text), ["state"])
        self.assertIn("counting the queue",
                      " ".join(reasons(text, "state")))

    def test_the_same_review_wearing_the_glyph_is_silent(self):
        text = (f"- {Q} **Rule-4 cold pass queued: the hardening.** Tier:\n"
                "      the review tier. Delta: the tool. Intent record: x.\n")
        self.assertEqual(dets(text), [])

    def test_a_title_mentioning_a_queued_review_that_has_run_is_silent(self):
        """The 27 items after conversion: the title keeps its words as record,
        and the RAN stamp says the pass is done."""
        text = ("- [ ] 🎯 **Rule-4 cold pass queued: x.** Delta: y.\n"
                "      - [ ] **The pass RAN 2026-09-26; the cycle CLOSES.**\n")
        self.assertEqual(dets(text), [])

    def test_a_ran_stamp_with_a_time_is_silent(self):
        """115/400: an ISO 8601 stamp with a time has no word boundary
        between the day and the T; the drain writes it that way."""
        text = ("- [ ] 🎯 **Rule-4 cold pass queued: x.** Delta: y.\n"
                "      ✅ PASS RAN 2026-11-15T20:40Z UTC (acts 1 and 2).\n")
        self.assertEqual(dets(text), [])

    def test_a_backticked_glyph_in_a_title_is_a_mention(self):
        """An item ABOUT pointers names the glyph in a code span."""
        text = (f"- [ ] 🔎 **What a `{Q}` review pointer becomes when its "
                "verdict lands.** A missing rule.\n")
        self.assertEqual(dets(text), [])

    def test_ordinary_open_work_is_silent(self):
        self.assertEqual(dets("- [ ] **Build the widget.** Then test it.\n"), [])


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
            # 115/130: the findings path says what it read, as the clean one does.
            self.assertIn("coverage: 1 roadmap file(s) opened \u00b7 1 item(s) "
                          "checked", r.stdout)
            self.assertNotIn("scanned nothing", r.stdout)

    def test_a_clean_tree_says_so(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "ROADMAP.md").write_text(
                "- [ ] **Ordinary work.** Nothing queued here.\n",
                encoding="utf-8")
            r = self._run("--root", td, ".")
            self.assertEqual(r.returncode, 0)
            self.assertIn("clean", r.stdout)
            # 115/130: and it says how much it read.
            self.assertIn("coverage: 1 roadmap file(s) opened \u00b7 1 item(s) "
                          "checked", r.stdout)
            self.assertNotIn("scanned nothing", r.stdout)

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
            # 115/130: a tree with no roadmap is out of scope, and says so
            # rather than looking like a clean read of one.
            self.assertIn("coverage: 0 roadmap file(s) opened \u00b7 0 item(s) "
                          "checked", r.stdout)
            self.assertIn("scanned nothing", r.stdout)

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
            self.assertEqual({"files_opened": 1, "items_checked": 1,
                              "scanned_nothing": False},
                             json.loads(r.stdout)["coverage"])


class LinkedWorktreeSkipped(unittest.TestCase):
    """115/250: a directory argument is enumerated by `filewalk`, so it must
    not read inside a linked worktree (020/160: a directory whose `.git` is a
    regular FILE). Before this, `roadmaps()` was a bare `rglob("*.md")` and a
    hand run counted a sibling session's checkout under `.claude/worktrees/`
    as this tree's own pointers."""

    BAD = f"- [ ] {Q} **Review queued.** Is that right?\n"

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, ignore_errors=True)

    def _write(self, rel, text):
        p = self.tmp / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def _found(self, *paths):
        return {str(p.relative_to(self.tmp))
                for p in pointerscan.roadmaps(list(paths or ["."]), self.tmp)}

    def test_linked_worktree_roadmaps_are_not_read(self):
        self._write("docs/roadmap/010-sec/010-item.md", self.BAD)
        self._write(".claude/worktrees/wt1/.git",
                    "gitdir: /elsewhere/.git/worktrees/wt1\n")
        self._write(".claude/worktrees/wt1/docs/roadmap/010-sec/010-item.md",
                    self.BAD)
        self._write(".claude/worktrees/wt1/ROADMAP.md", self.BAD)
        found = self._found()
        self.assertEqual(found, {"docs/roadmap/010-sec/010-item.md"})

    def test_a_linked_worktree_adds_no_finding_to_a_full_scan(self):
        self._write("docs/roadmap/010-sec/010-item.md", self.BAD)
        before = pointerscan.scan(["."], self.tmp)
        self._write(".claude/worktrees/wt1/.git",
                    "gitdir: /elsewhere/.git/worktrees/wt1\n")
        self._write(".claude/worktrees/wt1/docs/roadmap/010-sec/010-item.md",
                    self.BAD)
        self.assertEqual(len(before), 1)
        self.assertEqual(pointerscan.scan(["."], self.tmp), before)

    def test_an_explicit_file_inside_a_linked_worktree_is_still_read(self):
        """Explicit-file arguments keep working as before: the caller named
        it, so the prune (a directory-walk rule) does not apply."""
        self._write(".claude/worktrees/wt1/.git",
                    "gitdir: /elsewhere/.git/worktrees/wt1\n")
        self._write(".claude/worktrees/wt1/ROADMAP.md", self.BAD)
        self.assertEqual(
            self._found(".claude/worktrees/wt1/ROADMAP.md"),
            {".claude/worktrees/wt1/ROADMAP.md"})

    def test_independent_nested_repos_own_git_dir_still_pruned(self):
        self._write("docs/roadmap/010-sec/010-item.md", self.BAD)
        self._write("nested/.git/objects/pack/ROADMAP.md", self.BAD)
        self.assertEqual(self._found(), {"docs/roadmap/010-sec/010-item.md"})

    def test_skip_dir_names_still_prune(self):
        self._write("node_modules/x/ROADMAP.md", self.BAD)
        self._write("sub/ROADMAP.md", self.BAD)
        self.assertEqual(self._found(), {"sub/ROADMAP.md"})


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
            self.assertIn(f.detector, ("grammar", "cycle", "state"))
            self.assertTrue(f.reason)
            self.assertGreater(f.line, 0)


_MARK = "pointerscan" + ":allow"   # built from parts: no source line is a marker


def _marked(spec: str, marker: str) -> str:
    head, _, rest = spec.partition("\n")
    return f"{head}  {marker}\n{rest}"


class ScopedMarker(unittest.TestCase):
    """115/080: a marker scoped to one detector exempts that detector only
    (AM4); every marker that exempted before still exempts the whole item."""

    LIVE = pointerscan._SPEC_LIVE          # trips grammar and cycle

    def dets(self, text, **kw):
        return sorted({f.detector for f in pointerscan.scan_text(text, **kw)})

    def test_the_fixture_trips_two_detectors(self):
        self.assertEqual(self.dets(self.LIVE), ["cycle", "grammar"])

    def test_a_scope_naming_one_detector_keeps_the_other(self):
        sup = []
        text = _marked(self.LIVE, f"{_MARK}:cycle: ruling recorded elsewhere")
        self.assertEqual(self.dets(text, suppressed=sup), ["grammar"])
        self.assertEqual(len(sup), 1)
        text = _marked(self.LIVE, f"{_MARK}:grammar: quoted on purpose")
        self.assertEqual(self.dets(text), ["cycle"])

    def test_the_unscoped_form_and_an_unknown_scope_still_exempt_the_item(self):
        for marker in (f"{_MARK}: a reason", f"{_MARK}:whole-item: a reason"):
            self.assertEqual(self.dets(_marked(self.LIVE, marker)), [])

    def test_a_file_level_scope_drops_that_detector_across_the_file(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        board = tmp / "docs" / "roadmap"
        board.mkdir(parents=True)
        (board / "a.md").write_text(f"<!-- {_MARK}:grammar: fixture -->\n" + self.LIVE)
        sup = []
        found = pointerscan.scan(["docs"], tmp, sup)
        self.assertEqual(sorted({f.detector for f in found}), ["cycle"])
        self.assertEqual(len(sup), 1)


class Allowances(unittest.TestCase):
    """GUARDS.md rule (c) — a marker with no reason is a mention."""

    def test_bare_marker_without_reason_is_not_an_allowance(self):
        self.assertIsNone(pointerscan.parse_allow("x pointerscan:allow"))
        self.assertIsNone(pointerscan.parse_allow("x pointerscan:allow:"))

    def test_marker_with_reason_allows(self):
        self.assertEqual("", pointerscan.parse_allow("x pointerscan:allow: a reason"))


class BoundedMemory(unittest.TestCase):
    """020/380 — measured, not fixed. `pointerscan` is one of the two tools
    (alongside `board`) the item's own brief names as a legitimate
    exception: it reads every roadmap item in scope by nature, so part of
    its footprint grows with item count, and pretending a growing thing is
    constant would be its own dishonesty.

    What is checked here is that the growth stays LINEAR — a per-item
    constant — never worse. Measured while building this test, subprocess +
    `memprobe` over a synthetic multi-section board:

      500 items    ~19.9 MB peak RSS
      5,000 items  ~37.3 MB peak RSS    (+4,500 items, ~+17.5 MB, ~3.9 KB/item)
      10,000 items ~55.3 MB peak RSS    (+5,000 items, ~+18.0 MB, ~3.6 KB/item)

    The per-item rate holds steady across two doublings rather than growing
    — the signature of a linear design, not a quadratic one — and 10,000
    items finished in ~5s wall-clock with no timeout. The bound below is
    deliberately generous (roughly 2x the measured rate) so this catches a
    future SUPERLINEAR regression without being fitted to today's exact
    figure (`ground-numeric-limits`).
    """

    POINTERSCAN = str(TOOLS_DIR / "pointerscan.py")
    SMALL_ITEMS = 500     # 10 sections x 50 items
    LARGE_ITEMS = 5_000   # 50 sections x 100 items
    MAX_BYTES_PER_ITEM = 8 * 1024

    @staticmethod
    def _build(root: Path, sections: int, items_per_section: int) -> None:
        b = root / "docs" / "roadmap"
        b.mkdir(parents=True, exist_ok=True)
        (b / "README.md").write_text("# board\n\nlegend\n")
        for s in range(sections):
            sec = b / f"{s:03d}-section-{s}"
            sec.mkdir(exist_ok=True)
            (sec / "README.md").write_text(f"# Section {s}\nwhy\n")
            for i in range(items_per_section):
                (sec / f"{i:03d}-item-{i}.md").write_text(
                    f"- [ ] **Item {s}-{i}.** Filler description text, long "
                    f"enough to look like a real work item.\n"
                    f"      A continuation line with a bit more detail.\n")

    def _peak_rss_for(self, sections: int, items_per_section: int) -> int:
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, ignore_errors=True)
        self._build(tmp, sections, items_per_section)
        result = memprobe.run_and_measure(
            [sys.executable, self.POINTERSCAN, "--root", str(tmp), str(tmp)],
            timeout=60, rss_limit_bytes=900 * 1024 * 1024)
        self.assertFalse(result.timed_out, "scan did not finish in time")
        self.assertFalse(result.killed_over_limit,
                         "scan exceeded the 900 MB safety limit")
        return result.peak_rss_bytes

    def test_peak_memory_grows_no_worse_than_linearly_with_item_count(self):
        small_peak = self._peak_rss_for(10, 50)     # 500 items
        large_peak = self._peak_rss_for(50, 100)    # 5,000 items
        item_delta = self.LARGE_ITEMS - self.SMALL_ITEMS
        growth = large_peak - small_peak
        bound = item_delta * self.MAX_BYTES_PER_ITEM
        self.assertLess(
            growth, bound,
            f"peak RSS grew {growth / 1e6:.1f} MB for {item_delta} more "
            f"items (small={small_peak / 1e6:.1f} MB, "
            f"large={large_peak / 1e6:.1f} MB) — that's "
            f"{growth / item_delta:.0f} bytes/item, over the "
            f"{self.MAX_BYTES_PER_ITEM}-byte/item bound. pointerscan's "
            "growth is legitimate (020/380 names it as an exception) but it "
            "must stay LINEAR — this looks like a superlinear regression.")


if __name__ == "__main__":
    unittest.main()


# --- the bar gate (460/030) --------------------------------------------------
# A gate that reads green while it checks nothing is the worst failure here, so
# every "passes" leg below has a "flagged" twin built from the same fixture with
# one thing taken away.

GOOD_RECORD = (
    "# A session record\n\n"
    "- **Commitment:** a gate that blocks every commit touching widget rules\n"
    "- **Worst failure:** the gate reads green while it checks nothing at all\n"
    "- **Why the floor misses it:** the tests only run the cases the author "
    "imagined\n")

BOARD = "docs/roadmap/160-doctrine-review-owed"


def pointer(rec="../../sessions/rec.md", delta="`tools/widget.py`",
            title="the widget", extra="", marker=None):
    marker = Q if marker is None else marker
    return (f"- [ ] {marker} **Rule-4 cold pass queued: {title}.** The authoring "
            "session queues this and does not take it.\n"
            "      *Tier:* Fable, the principal-named review tier.\n"
            f"      *Delta, scoped to paths:* {delta}: the commit that closes "
            "`999/001`.\n"
            f"      *Intent record:*\n      [`rec`]({rec}).\n{extra}")


class _Repo:
    """A throwaway git repo with one base commit."""

    def __init__(self):
        self.root = Path(tempfile.mkdtemp()).resolve()
        self.env = {"GIT_CONFIG_GLOBAL": "/dev/null",
                    "GIT_CONFIG_SYSTEM": "/dev/null",
                    "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin",
                    "HOME": str(self.root)}
        self.git("init", "-q", "-b", "main")
        self.write("README.md", "base\n")
        self.commit()

    def git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.root), "-c", "user.name=t",
             "-c", "user.email=tester", "-c", "commit.gpgsign=false",
             *args], check=True, capture_output=True, env=self.env)

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def commit(self):
        self.git("add", "-A")
        self.git("commit", "-q", "-m", "c")

    def stage(self, *rels):
        self.git("add", "--", *rels)

    def cleanup(self):
        shutil.rmtree(self.root, ignore_errors=True)


class BarGateBase(unittest.TestCase):
    def setUp(self):
        self.repo = _Repo()
        self.addCleanup(self.repo.cleanup)
        # An unrelated existing pointer, committed with NO answers anywhere:
        # existing pointers are never failed retroactively.
        self.repo.write("docs/sessions/old.md", "# an old record\n")
        self.repo.write(f"{BOARD}/001-old.md",
                        pointer("../../sessions/old.md",
                                delta="`tools/legacy.py`", title="legacy"))
        self.repo.commit()

    def run_bar(self, staged=False, **kw):
        return pointerscan.bar_scan(["docs"], self.repo.root, staged=staged,
                                    **kw)

    def add(self, name="010-new.md", rec_text=GOOD_RECORD, **ptr):
        if rec_text is not None:
            self.repo.write("docs/sessions/rec.md", rec_text)
        self.repo.write(f"{BOARD}/{name}", pointer(**ptr))
        return f"{BOARD}/{name}"

    def reasons(self, run):
        return [f.reason for f in run.findings]


class BarAnswersTest(BarGateBase):
    def test_a_new_pointer_whose_record_has_the_answers_passes(self):
        self.add()
        run = self.run_bar()
        self.assertTrue(run.ran, run.note)
        self.assertEqual(run.new_pointers, 1)
        self.assertEqual(run.findings, [])

    def test_the_same_pointer_with_the_answers_removed_is_flagged(self):
        self.add(rec_text="# A session record\n\nNothing was asked here.\n")
        run = self.run_bar()
        self.assertEqual(len(run.findings), 1)
        f = run.findings[0]
        self.assertTrue(f.bar)
        self.assertEqual(f.detector, "grammar")
        self.assertIn("Commitment", f.reason)
        self.assertIn("Why the floor misses it", f.reason)

    def test_one_missing_answer_is_named(self):
        text = GOOD_RECORD.replace("Worst failure", "Something else")
        self.add(rec_text=text)
        (f,) = self.run_bar().findings
        self.assertIn("for: Worst failure", f.reason)
        self.assertNotIn("Commitment,", f.reason)

    def test_not_warranted_with_grounds_passes(self):
        self.add(rec_text="review: not warranted — a wording correction that "
                          "adds no rule\n")
        self.assertEqual(self.run_bar().findings, [])

    def test_not_warranted_with_no_grounds_is_flagged(self):
        self.add(rec_text="review: not warranted —\n")
        self.assertEqual(len(self.run_bar().findings), 1)

    def test_a_placeholder_is_not_an_answer(self):
        text = GOOD_RECORD.replace(
            "a gate that blocks every commit touching widget rules",
            "<what rests on it>")
        self.add(rec_text=text)
        (f,) = self.run_bar().findings
        self.assertIn("Commitment", f.reason)

    def test_a_very_short_answer_is_not_an_answer(self):
        self.add(rec_text=GOOD_RECORD.replace(
            "the tests only run the cases the author imagined", "none"))
        (f,) = self.run_bar().findings
        self.assertIn("Why the floor misses it", f.reason)

    def test_an_answer_may_wrap_onto_the_next_line(self):
        text = GOOD_RECORD.replace(
            "- **Commitment:** a gate that blocks every commit touching widget "
            "rules", "- **Commitment:** a gate\n  that blocks every commit\n")
        self.add(rec_text=text)
        self.assertEqual(self.run_bar().findings, [])

    def test_a_fenced_example_is_not_an_answer(self):
        self.add(rec_text="```\n" + GOOD_RECORD + "```\n")
        self.assertEqual(len(self.run_bar().findings), 1)

    def test_a_label_in_a_code_span_is_a_mention_not_an_answer(self):
        text = GOOD_RECORD.replace("- **Commitment:**", "- `Commitment:`")
        self.add(rec_text=text)
        (f,) = self.run_bar().findings
        self.assertIn("Commitment", f.reason)

    def test_a_plain_unbulleted_label_line_counts(self):
        self.add(rec_text="Commitment: a rule others will follow for years\n"
                          "Worst failure: the rule is wrong and nobody sees it\n"
                          "Why the floor misses it: it fails silent in use\n")
        self.assertEqual(self.run_bar().findings, [])

    def test_a_pointer_naming_no_intent_record_is_flagged(self):
        self.repo.write(f"{BOARD}/010-new.md",
                        pointer().replace("*Intent record:*", "*Record:*"))
        (f,) = self.run_bar().findings
        self.assertIn("names no intent record", f.reason)

    def test_an_intent_record_that_does_not_exist_is_flagged(self):
        self.add(rec_text=None, rec="../../sessions/nope.md")
        (f,) = self.run_bar().findings
        self.assertIn("not found", f.reason)

    def test_a_link_into_reviews_is_a_verdict_not_a_record(self):
        self.repo.write("docs/reviews/v.md", GOOD_RECORD)
        self.add(rec_text=None, rec="../../reviews/v.md")
        (f,) = self.run_bar().findings
        self.assertIn("names no intent record", f.reason)

    def test_any_one_named_record_with_the_answers_is_enough(self):
        self.repo.write("docs/sessions/rec.md", GOOD_RECORD)
        self.repo.write(f"{BOARD}/010-new.md", pointer().replace(
            "[`rec`](../../sessions/rec.md)",
            "[`a`](../../sessions/other.md), [`b`](../../sessions/rec.md)"))
        self.repo.write("docs/sessions/other.md", "# nothing\n")
        self.assertEqual(self.run_bar().findings, [])


class BarNewnessTest(BarGateBase):
    def test_an_existing_pointer_without_answers_is_not_failed(self):
        run = self.run_bar()
        self.assertTrue(run.ran)
        self.assertEqual((run.new_pointers, run.findings), (0, []))

    def test_editing_an_existing_pointer_does_not_make_it_new(self):
        p = self.repo.root / BOARD / "001-old.md"
        p.write_text(p.read_text() + "      🔒 CLAIMED by a session.\n")
        run = self.run_bar()
        self.assertEqual((run.new_pointers, run.findings), (0, []))

    def test_rewording_the_only_pointer_does_not_make_it_new(self):
        p = self.repo.root / BOARD / "001-old.md"
        p.write_text(p.read_text().replace("legacy", "an older name"))
        self.assertEqual(self.run_bar().new_pointers, 0)

    def test_a_renamed_pointer_is_compared_with_its_old_path(self):
        self.repo.git("mv", f"{BOARD}/001-old.md", f"{BOARD}/002-old.md")
        self.assertEqual(self.run_bar(staged=True).new_pointers, 0)

    def test_an_item_that_becomes_a_pointer_is_new(self):
        self.repo.write("docs/roadmap/450-x/010-plain.md",
                        "- [ ] **Plain work.** Nothing queued.\n")
        self.repo.commit()
        self.repo.write("docs/roadmap/450-x/010-plain.md",
                        pointer(rec="../../sessions/missing.md"))
        run = self.run_bar()
        self.assertEqual(run.new_pointers, 1)
        self.assertEqual(len(run.findings), 1)

    def test_a_new_item_in_a_review_owed_section_queues_a_pass(self):
        self.repo.write(f"{BOARD}/010-plain.md",
                        "- [ ] **A cold pass of the thing.** No glyph here.\n")
        run = self.run_bar()
        self.assertEqual(run.new_pointers, 1)
        self.assertEqual(len(run.findings), 1)

    def test_a_completed_item_in_a_review_owed_section_is_not_a_pass(self):
        self.repo.write(f"{BOARD}/010-done.md",
                        "- [x] **A pass that ran.** Verdict landed.\n")
        self.assertEqual(self.run_bar().new_pointers, 0)

    def test_a_new_plain_item_elsewhere_is_not_a_pass(self):
        self.repo.write("docs/roadmap/450-x/010-plain.md",
                        "- [ ] **Plain work.** Nothing queued.\n")
        self.assertEqual(self.run_bar().new_pointers, 0)

    def test_the_allow_marker_exempts_a_bar_finding_and_is_counted(self):
        self.add(rec_text=None, extra="      <!-- pointerscan"
                 ":allow:grammar: the principal ordered this pass, his words "
                 "quoted in the item -->\n")
        tally = []
        run = self.run_bar(suppressed=tally)
        self.assertEqual(run.findings, [])
        self.assertEqual(len(tally), 1)

    def test_an_allow_scoped_to_another_detector_does_not_exempt_it(self):
        self.add(rec_text=None, extra="      <!-- pointerscan"
                 ":allow:cycle: not about the bar -->\n")
        self.assertEqual(len(self.run_bar().findings), 1)


class BarSecondPointerTest(BarGateBase):
    def setUp(self):
        super().setUp()
        self.repo.write("docs/sessions/rec.md", GOOD_RECORD)
        self.repo.write(f"{BOARD}/020-open.md",
                        pointer(delta="`tools/widget.py`, `tools/widget.md`",
                                title="the open one"))
        self.repo.commit()

    def test_a_second_pass_on_the_same_path_is_flagged_naming_the_open_one(self):
        self.repo.write(f"{BOARD}/030-second.md", pointer(title="second"))
        run = self.run_bar()
        (f,) = run.findings
        self.assertIn("`160/020`", f.reason)
        self.assertIn("widen", f.reason)
        self.assertIn("tools/widget.py", f.reason)

    def test_a_directory_prefix_is_the_same_subject(self):
        self.repo.write(f"{BOARD}/021-deep.md",
                        pointer(delta="`tools/area/widget.py`", title="deep"))
        self.repo.commit()
        self.repo.write(f"{BOARD}/030-second.md",
                        pointer(delta="`tools/area/`", title="second"))
        (f,) = self.run_bar().findings
        self.assertIn("`160/021`", f.reason)

    def test_naming_the_open_pointer_is_the_exception(self):
        self.repo.write(
            f"{BOARD}/030-second.md",
            pointer(title="second", extra="      The open pass on this subject "
                    "is `160/020`; the principal ordered this one.\n"))
        self.assertEqual(self.run_bar().findings, [])

    def test_a_briefed_open_pass_is_not_widened(self):
        p = self.repo.root / BOARD / "020-open.md"
        p.write_text(p.read_text() + "      **Brief written 2026-11-27 UTC.**\n")
        self.repo.write(f"{BOARD}/030-second.md", pointer(title="second"))
        self.assertEqual(self.run_bar().findings, [])

    def test_a_landed_open_pass_is_not_widened(self):
        p = self.repo.root / BOARD / "020-open.md"
        p.write_text(p.read_text() + "      **The pass RAN 2026-11-20 and the "
                     "cycle CLOSES.**\n")
        self.repo.write(f"{BOARD}/030-second.md", pointer(title="second"))
        self.assertEqual(self.run_bar().findings, [])

    def test_a_bare_top_level_directory_is_too_broad_to_be_a_subject(self):
        self.repo.write(f"{BOARD}/030-second.md",
                        pointer(delta="`tools`", title="second"))
        self.assertEqual(self.run_bar().findings, [])

    def test_a_section_readme_is_not_a_board_item(self):
        self.repo.write(f"{BOARD}/README.md", pointer(title="readme"))
        self.assertEqual(self.run_bar().new_pointers, 0)

    def test_a_different_subject_is_not_flagged(self):
        self.repo.write(f"{BOARD}/030-second.md",
                        pointer(delta="`tools/other.py`", title="second"))
        self.assertEqual(self.run_bar().findings, [])

    def test_sharing_only_the_changelog_is_not_a_subject(self):
        self.repo.write(f"{BOARD}/020-open.md", pointer(
            delta="`tools/widget.py`, `CHANGELOG.md`", title="the open one"))
        self.repo.commit()
        self.repo.write(f"{BOARD}/030-second.md", pointer(
            delta="`tools/other.py`, `CHANGELOG.md`", title="second"))
        self.assertEqual(self.run_bar().findings, [])

    def test_two_new_pointers_on_one_subject_flag_the_later_one_only(self):
        self.repo.write(f"{BOARD}/040-a.md", pointer(
            delta="`tools/brand_new.py`", title="a"))
        self.repo.write(f"{BOARD}/050-b.md", pointer(
            delta="`tools/brand_new.py`", title="b"))
        run = self.run_bar()
        self.assertEqual([f.path for f in run.findings], [f"{BOARD}/050-b.md"])


class BarPlaneTest(BarGateBase):
    def test_staged_reads_the_index_record_not_the_working_tree_one(self):
        """The commit is what is staged: a record fixed only on disk does not
        rescue a staged pointer, and a record broken only on disk does not
        sink it."""
        rel = self.add(rec_text="# nothing here\n")
        self.repo.stage(rel, "docs/sessions/rec.md")
        self.repo.write("docs/sessions/rec.md", GOOD_RECORD)   # unstaged fix
        self.assertEqual(len(self.run_bar(staged=True).findings), 1)
        self.assertEqual(self.run_bar(staged=False).findings, [])

    def test_staged_ignores_an_unstaged_draft_pointer(self):
        self.add(rec_text="# nothing here\n")                  # never staged
        staged = self.run_bar(staged=True)
        self.assertEqual((staged.new_pointers, staged.findings), (0, []))
        self.assertEqual(len(self.run_bar(staged=False).findings), 1)

    def test_staged_pointer_with_answers_in_the_index_passes(self):
        rel = self.add()
        self.repo.stage(rel, "docs/sessions/rec.md")
        run = self.run_bar(staged=True)
        self.assertEqual((run.new_pointers, run.findings), (1, []))

    def test_an_unreadable_base_says_not_run(self):
        run = pointerscan.bar_scan(["docs"], self.repo.root, base="no-such-ref")
        self.assertFalse(run.ran)
        self.assertIn("not a commit", run.note)
        self.assertIn("NOT RUN", run.line())

    def test_a_tree_that_is_not_a_repo_says_not_run(self):
        with tempfile.TemporaryDirectory() as td:
            run = pointerscan.bar_scan(["."], Path(td))
            self.assertFalse(run.ran)

    def test_a_root_below_the_repo_top_says_not_run(self):
        sub = self.repo.root / "docs"
        run = pointerscan.bar_scan(["."], sub)
        self.assertFalse(run.ran)


class BarInvocationTest(BarGateBase):
    def _run(self, *args):
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "pointerscan.py"),
             "--root", str(self.repo.root), *args],
            capture_output=True, text=True)

    def test_a_bar_finding_alone_does_not_fail_without_block(self):
        self.add(rec_text="# nothing\n")
        r = self._run("docs")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("[bar]", r.stdout)
        self.assertIn("REVIEW BAR", r.stdout)
        self.assertIn("1 review bar", r.stdout)
        self.assertIn("bar check: 1 new queued pass(es)", r.stdout)

    def test_block_fails_a_new_pointer_that_lacks_the_answers(self):
        self.add(rec_text="# nothing\n")
        r = self._run("--block", "docs")
        self.assertEqual(r.returncode, 1, r.stdout + r.stderr)
        self.assertIn("BLOCKING", r.stdout)

    def test_block_passes_a_new_pointer_that_has_them(self):
        self.add()
        r = self._run("--block", "docs")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)

    def test_block_never_fails_on_an_older_kind_of_finding(self):
        """Only the bar blocks: a refs-only breach elsewhere stays advisory."""
        self.repo.write("docs/roadmap/450-x/010-q.md",
                        f"- {Q} **Review queued.** Is that right?\n")
        self.repo.commit()
        r = self._run("--block", "docs")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("[grammar]", r.stdout)

    def test_block_with_no_base_is_a_failure_to_run_not_a_pass(self):
        r = self._run("--block", "--base", "no-such-ref", "docs")
        self.assertEqual(r.returncode, 2, r.stdout + r.stderr)
        self.assertIn("NOT RUN", r.stdout)

    def test_without_block_a_missing_base_is_loud_and_exits_zero(self):
        r = self._run("--base", "no-such-ref", "docs")
        self.assertEqual(r.returncode, 0)
        self.assertIn("NOT RUN", r.stdout)

    def test_staged_block_end_to_end(self):
        rel = self.add(rec_text="# nothing\n")
        self.repo.stage(rel, "docs/sessions/rec.md")
        self.assertEqual(self._run("--staged", "--block", "docs").returncode, 1)
        self.repo.write("docs/sessions/rec.md", GOOD_RECORD)
        self.repo.stage("docs/sessions/rec.md")
        self.assertEqual(self._run("--staged", "--block", "docs").returncode, 0)

    def test_staged_outside_a_work_tree_is_an_error(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "ROADMAP.md").write_text("- [ ] **x.** y\n")
            r = subprocess.run(
                [sys.executable, str(TOOLS_DIR / "pointerscan.py"),
                 "--root", td, "--staged", "."], capture_output=True, text=True)
            self.assertEqual(r.returncode, 2, r.stdout + r.stderr)

    def test_json_carries_the_bar_status_and_the_finding(self):
        import json
        self.add(rec_text="# nothing\n")
        r = self._run("--json", "docs")
        out = json.loads(r.stdout)
        self.assertEqual(out["bar"]["new_pointers"], 1)
        self.assertTrue(out["bar"]["ran"])
        self.assertTrue(out["findings"][0]["bar"])
        self.assertEqual(out["findings"][0]["id"], "pointerscan:grammar")


class BarPartsTest(unittest.TestCase):
    def test_record_gaps_is_empty_only_for_all_three_or_not_warranted(self):
        self.assertEqual(pointerscan.record_gaps(GOOD_RECORD), [])
        self.assertEqual(len(pointerscan.record_gaps("nothing")), 3)

    def test_intent_links_resolve_relative_to_the_pointer(self):
        rel = f"{BOARD}/010-x.md"
        self.assertEqual(
            pointerscan.intent_links(pointer(), rel),
            ["docs/sessions/rec.md"])

    def test_intent_links_refuse_a_path_escaping_the_repo(self):
        self.assertEqual(pointerscan.intent_links(
            pointer(rec="../../../../../etc/passwd.md"), f"{BOARD}/010-x.md"),
            [])

    def test_delta_paths_read_only_the_delta_region(self):
        body = ("**x.** *Delta:* `tools/a.py`, `docs/b/`, `210/630`, "
                "`CHANGELOG.md`. *Intent record:* [`c`](c.md) `tools/z.py`")
        self.assertEqual(pointerscan.delta_paths(body), ["tools/a.py", "docs/b"])

    def test_the_board_ref_is_read_from_the_path(self):
        self.assertEqual(
            pointerscan.board_ref("docs/roadmap/160-x/1880-y.md"), "160/1880")
        self.assertIsNone(pointerscan.board_ref("docs/ROADMAP.md"))
