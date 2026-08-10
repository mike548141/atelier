"""Tests for tools/plainscan.py — the plain-language gate's four rules.

Every fixture below is a real specimen, lifted from this estate's own session
transcripts or its own doctrine files, never invented. That matters more here
than in most of the suite: this scanner reads prose written by the same author
it is meant to correct, so a fixture invented to make a rule look good would
prove nothing about whether the rule fires on the writing that caused it.

Two things carry the weight:

  * THE FALSE POSITIVES. This scanner reads judgement-adjacent text, and the
    ways it can be wrong are the ways it gets exempted into silence — a shouted
    word read as jargon, a code fence read as a sentence, a table row read as
    prose, a sentence-final aside read as a buried one. Most of what is pinned
    below is what must NOT fire.
  * THE TWO PLANES. `scan_text` is the whole engine, and the Stop hook calls it
    with different limits from the repo plane. A test that only exercised the
    CLI would leave the surface the rules were measured on untested.

Zero third-party deps, same as the rest of the suite.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import plainscan  # noqa: E402

HOOK = TOOLS_DIR / "hooks" / "plain-reply.py"


def rules_hit(text, **kw):
    return {f.rule for f in plainscan.scan_text(text, **kw)}


class ReferenceIds(unittest.TestCase):
    """P1 — a short code used before anything says what it points at."""

    def test_bare_reference_is_a_finding(self):
        # Real: 2026-08 atelier session, a ruling summary.
        t = "Your ruling closes F1 and the cycle with it. Nothing else is open."
        self.assertIn("P1", rules_hit(t))

    def test_inline_gloss_clears_it(self):
        t = "Your ruling closes F1 — the missing UTC stamp — and the cycle with it."
        self.assertNotIn("P1", rules_hit(t))

    def test_table_definition_anywhere_clears_it(self):
        # A findings table below the summary is a legitimate layout: the reader
        # scrolls and finds it, so first-use-before-definition is not the test.
        t = ("Your ruling closes F1 and the cycle with it.\n\n"
             "| # | Sev | What |\n|---|---|---|\n| F1 | LOW | the missing stamp |\n")
        self.assertNotIn("P1", rules_hit(t))

    def test_bold_definition_clears_it(self):
        t = "Rule per finding: **F1** — stamp UTC at the six minting sites."
        self.assertNotIn("P1", rules_hit(t))

    def test_first_use_only(self):
        """One finding per code, not one per mention — noise is the enemy."""
        t = "F1 is open. F1 is still open. F1 will stay open until you rule."
        self.assertEqual(1, len([f for f in plainscan.scan_text(t) if f.rule == "P1"]))

    def test_version_numbers_are_not_references(self):
        for t in ("We pinned it at v2 in the lockfile there.",
                  "The ADR 0005 ruling made the repo public last month."):
            with self.subTest(t=t):
                self.assertNotIn("P1", rules_hit(t))

    def test_heading_levels_collide_and_that_is_the_right_trade(self):
        """'H2' as a heading level reads as a reference code, deliberately.

        The obvious fix — exempt H1 through H6 — was checked against the corpus
        and rejected: 'H1' appears 45 times across the transcripts and every one
        of them is a finding ID, not a heading level. Exempting the shape would
        blind the rule to real bare references to spare a rare collision, and
        the collision costs one em-dash to clear.
        """
        self.assertIn("P1", rules_hit("Check the H2 heading level in that doc."))


class Acronyms(unittest.TestCase):
    """P2 — grounded in digital.govt.nz: expand on first use."""

    def test_unexpanded_acronym_is_a_finding(self):
        self.assertIn("P2", rules_hit("We rely on MNDP for neighbour discovery."))

    def test_expansion_clears_it(self):
        t = "MikroTik Neighbor Discovery Protocol (MNDP) finds the switches."
        self.assertNotIn("P2", rules_hit(t))

    def test_reverse_expansion_clears_it(self):
        t = "We rely on MNDP (the neighbour discovery protocol) to find them."
        self.assertNotIn("P2", rules_hit(t))

    def test_glossary_entry_clears_it(self):
        t = "We rely on MNDP for neighbour discovery."
        self.assertNotIn("P2", rules_hit(t, glossary={"MNDP"}))

    def test_common_acronyms_never_fire(self):
        t = "The CLI writes JSON over HTTPS to the API and logs a UTC timestamp."
        self.assertNotIn("P2", rules_hit(t))

    def test_shouted_prose_is_not_jargon(self):
        """The false positive that showed up on the first real run, 00-APEX.md.

        'It sits ABOVE every design principle' is emphasis, not an acronym. The
        general test is the lowercase twin in the same text; the built-in list
        is the fallback for a shout with no twin.
        """
        t = "The rule sits ABOVE every principle. Everything above it is fixed."
        self.assertNotIn("P2", rules_hit(t))
        self.assertNotIn("P2", rules_hit("This is NEVER acceptable in any form."))


class SentenceLength(unittest.TestCase):
    """P3 — the house number, and the structures that are not sentences."""

    def test_long_sentence_is_a_finding(self):
        self.assertIn("P3", rules_hit("word " * 40 + "end."))

    def test_short_sentence_passes(self):
        self.assertNotIn("P3", rules_hit("The floor is green. I re-ran it twice."))

    def test_limit_is_honoured(self):
        t = "word " * 40 + "end."
        self.assertNotIn("P3", rules_hit(t, sentence_limit=60))
        self.assertIn("P3", rules_hit(t, sentence_limit=20))

    def test_headings_are_not_sentences(self):
        self.assertNotIn("P3", rules_hit("# " + "word " * 60))

    def test_table_rows_are_not_sentences(self):
        self.assertNotIn("P3", rules_hit("| " + "word " * 60 + " |"))

    def test_wrapped_paragraphs_are_joined(self):
        """A markdown-wrapped sentence must be measured whole, not per line."""
        wrapped = "\n".join(["word word word word word word word"] * 8) + " end."
        self.assertIn("P3", rules_hit(wrapped))

    def test_list_items_are_separate_sentences(self):
        items = "\n".join(f"- item {i} is short and readable." for i in range(8))
        self.assertNotIn("P3", rules_hit(items))


class BuriedAsides(unittest.TestCase):
    """P4 — COMMUNICATION.md, 2026-07-15: brackets hold droppable glosses only."""

    def test_mid_sentence_aside_is_a_finding(self):
        t = ("The scanner runs on the hook (which reads only the staged diff, so "
             "the commit path stays fast) and blocks the commit outright.")
        self.assertIn("P4", rules_hit(t))

    def test_sentence_final_aside_passes(self):
        """The reader has landed the sentence before the bracket opens."""
        t = ("The scanner runs on the hook and blocks the commit (it reads only "
             "the staged diff, so the commit path stays fast).")
        self.assertNotIn("P4", rules_hit(t))

    def test_short_gloss_passes(self):
        self.assertNotIn("P4", rules_hit("The hook (staged only) blocks it here."))

    def test_limit_is_honoured(self):
        t = ("The hook (which reads only the staged diff and nothing else at all) "
             "blocks the commit.")
        self.assertIn("P4", rules_hit(t))
        self.assertNotIn("P4", rules_hit(t, aside_limit=200))


class Structure(unittest.TestCase):
    """What is not prose must not be read as prose."""

    def test_code_fences_are_skipped(self):
        t = "```\nF1 MNDP " + "word " * 60 + "\n```\n"
        self.assertEqual(set(), rules_hit(t))

    def test_indented_code_is_skipped(self):
        self.assertEqual(set(), rules_hit("    F1 MNDP " + "word " * 60))

    def test_inline_code_is_skipped(self):
        self.assertEqual(set(), rules_hit("Run `plainscan --rules P1` to check it."))

    def test_link_targets_are_skipped_but_text_is_kept(self):
        t = "See [the F1 ruling](docs/reviews/2026-08-09-MNDP-C5.md) for detail."
        hits = rules_hit(t)
        self.assertIn("P1", hits)          # 'F1' is visible text, still bare
        self.assertNotIn("P2", hits)       # 'MNDP' is only in the URL

    def test_blockquote_content_is_still_prose(self):
        """A quoted ruling is prose the reader still has to read."""
        self.assertIn("P1", rules_hit("> Your ruling closes F1 and the cycle."))

    def test_rule_subsetting(self):
        t = "Your ruling closes F1 and we rely on MNDP throughout."
        self.assertEqual({"P1"}, rules_hit(t, rules={"P1"}))


class Cli(unittest.TestCase):
    """The repo plane: exit codes, scoping, and the ignore file."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "docs").mkdir()
        self.addCleanup(self.tmp.cleanup)

    def write(self, rel, body):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(body, encoding="utf-8")
        return p

    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(TOOLS_DIR / "plainscan.py"), "--root",
             str(self.root), *args],
            capture_output=True, text=True)

    def test_findings_block_without_warn(self):
        self.write("docs/a.md", "Your ruling closes F1 and the cycle with it.\n")
        self.assertEqual(1, self.run_cli().returncode)

    def test_warn_always_exits_zero(self):
        self.write("docs/a.md", "Your ruling closes F1 and the cycle with it.\n")
        self.assertEqual(0, self.run_cli("--warn").returncode)

    def test_clean_tree_exits_zero(self):
        self.write("docs/a.md", "The floor is green. I re-ran it twice.\n")
        self.assertEqual(0, self.run_cli().returncode)

    def test_missing_root_exits_two(self):
        r = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "plainscan.py"), "--root",
             str(self.root / "nope")], capture_output=True, text=True)
        self.assertEqual(2, r.returncode)

    def test_unknown_rule_exits_two(self):
        self.assertEqual(2, self.run_cli("--rules", "P9").returncode)

    def test_ignore_file_is_honoured(self):
        self.write("docs/a.md", "Your ruling closes F1 and the cycle with it.\n")
        self.write(".plainscanignore", "docs/a.md\n")
        self.assertEqual(0, self.run_cli().returncode)

    def test_records_are_excluded_by_default(self):
        # Ruled 2026-08-10: records are append-only history for the next
        # session's agent, not prose the principal reads — the repo plane
        # skips them rather than warning forever about unrewritable archives.
        bad = "Your ruling closes F1 and the cycle with it.\n"
        self.write("docs/SESSIONS.md", bad)
        self.write("docs/sessions/2026-08-10-0900-example.md", bad)
        self.write("docs/ROADMAP-DONE.md", bad)
        self.assertEqual(0, self.run_cli().returncode)

    def test_include_records_selects_the_records(self):
        self.write("docs/SESSIONS.md",
                   "Your ruling closes F1 and the cycle with it.\n")
        self.assertEqual(1, self.run_cli("--include-records").returncode)

    def test_an_explicit_records_path_is_still_scanned(self):
        # Explicit selection beats the default exclusion: a named file is a
        # question deserving an answer.
        p = self.write("docs/SESSIONS.md",
                       "Your ruling closes F1 and the cycle with it.\n")
        self.assertEqual(1, self.run_cli(str(p)).returncode)

    def test_roadmap_itself_is_not_a_record(self):
        # The exclusion names ROADMAP-DONE.md; the live roadmap is exactly the
        # ruling-ask prose the principal reads, and must never be swept up.
        self.write("docs/ROADMAP.md",
                   "Your ruling closes F1 and the cycle with it.\n")
        self.assertEqual(1, self.run_cli().returncode)

    def test_json_shape(self):
        self.write("docs/a.md", "Your ruling closes F1 and the cycle with it.\n")
        out = json.loads(self.run_cli("--warn", "--json").stdout)
        self.assertEqual("plainscan", out["scanner"])
        self.assertEqual(1, out["counts"]["P1"])
        self.assertEqual("docs/a.md", out["findings"][0]["path"])

    def test_glossary_is_read_from_the_repo(self):
        self.write("docs/method/GLOSSARY.md", "- **MNDP** — neighbour discovery.\n")
        self.write("docs/a.md", "We rely on MNDP to find the switches.\n")
        self.assertEqual(0, self.run_cli("--rules", "P2").returncode)

    def test_selftest_passes(self):
        r = subprocess.run(
            [sys.executable, str(TOOLS_DIR / "plainscan.py"), "--selftest"],
            capture_output=True, text=True)
        self.assertEqual(0, r.returncode, r.stdout)
        self.assertIn("selftest OK", r.stdout)


class StopHook(unittest.TestCase):
    """The reply plane: the surface every measured defect was counted on."""

    def setUp(self):
        """Isolate the block counter.

        These tests used to share one state file with the live install and with
        each other, so a session id reused across runs carried its block count
        forward and tripped the give-up path early — the suite failed about one
        run in three. A flaky gate gets re-run, not read.
        """
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.env = dict(os.environ,
                        PLAIN_REPLY_STATE=str(Path(self.tmp.name) / "state.json"))

    def fire(self, session, message):
        payload = {"session_id": session, "hook_event_name": "Stop",
                   "last_assistant_message": message}
        r = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(payload),
                           capture_output=True, text=True, env=self.env)
        self.assertEqual(0, r.returncode, r.stderr)
        return json.loads(r.stdout) if r.stdout.strip() else {}

    # Long enough to clear the 200-char floor, and bad in three ways at once.
    BAD = ("Your ruling closes F1 and the cycle with it, and the remaining work "
           "is what the queue already carries. " + "word " * 50 + "end. "
           "The flip is gated (signscan does not even run on two of the children "
           "because secretscan fails first) and that ordering is load-bearing.")
    GOOD = ("The floor is green. I re-ran the whole suite twice to be sure of it. "
            "Nothing is outstanding, and nothing needs your ruling right now. "
            "You can close this session whenever you like. " * 2)

    def test_bad_reply_is_blocked(self):
        out = self.fire("t-block", self.BAD)
        self.assertEqual("block", out.get("decision"))
        self.assertIn("Rewrite it", out["reason"])

    def test_reason_names_the_rule_and_the_remedy(self):
        reason = self.fire("t-reason", self.BAD)["reason"]
        self.assertIn("[P1]", reason)
        self.assertIn("one idea per sentence", reason)

    def test_good_reply_passes(self):
        self.assertEqual({}, self.fire("t-good", self.GOOD))

    def test_short_replies_are_never_blocked(self):
        self.assertEqual({}, self.fire("t-short", "Done. F1 is closed."))

    def test_gives_up_rather_than_wedging_the_session(self):
        """A Stop hook that can never be satisfied is worse than no hook."""
        self.assertEqual("block", self.fire("t-loop", self.BAD).get("decision"))
        self.assertEqual("block", self.fire("t-loop", self.BAD).get("decision"))
        out = self.fire("t-loop", self.BAD)
        self.assertNotIn("decision", out)
        self.assertIn("plain-reply", out["hookSpecificOutput"]["additionalContext"])

    def test_a_clean_reply_resets_the_streak(self):
        self.fire("t-reset", self.BAD)
        self.fire("t-reset", self.GOOD)
        self.assertEqual("block", self.fire("t-reset", self.BAD).get("decision"))

    def test_malformed_input_fails_open(self):
        r = subprocess.run([sys.executable, str(HOOK)], input="not json",
                           capture_output=True, text=True)
        self.assertEqual(0, r.returncode)
        self.assertEqual("", r.stdout.strip())


class Registry(unittest.TestCase):
    """The wiring, not the rules: plainscan must reach the estate warn-first."""

    def test_registered_and_warn_only_on_both_planes(self):
        import floor
        s = floor.BY_NAME["plainscan"]
        self.assertTrue(s.warns_only("hook"))
        self.assertTrue(s.warns_only("ci"))
        self.assertEqual("docs", s.default_scope)


if __name__ == "__main__":
    unittest.main()
