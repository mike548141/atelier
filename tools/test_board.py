"""Tests for tools/board.py — the per-item roadmap store and its generated index.

What carries the weight here, shaped by the defects the split exists to end:

  * THE INDEX NEVER LIES. A committed derived file drifting from its source is
    the estate's most-recorded defect class, so staleness detection is the
    contract: any item edit must flip `check` red until `rebuild` runs.
  * `[x]` NEVER REACHES THE INDEX. `sizescan`'s cold-content gate fires on a
    `[x]` item on the hot path; the index renders done items as ✅ precisely so
    a generated line can never trip a gate meant for hand-written content.
  * GRACEFUL OUT-OF-SCOPE IS NOT FAIL-OPEN. A repo with no `docs/roadmap/` is
    not using the split board; exiting 0 there is the scoped-scanner posture,
    and the test pins that it *says so* rather than passing silently.

Zero third-party deps, same as the rest of the suite.
"""

import contextlib
import io
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest import mock

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import board  # noqa: E402
import memprobe  # noqa: E402


def make_board(root: Path) -> Path:
    sec = root / board.BOARD_DIR / "10-track-a"
    sec.mkdir(parents=True)
    (root / board.BOARD_DIR / "README.md").write_text(
        "# board\n\nCheckbox legend lives here.\n", encoding="utf-8")
    (sec / "README.md").write_text(
        "# Track A — live exposure\n\nWhy this track exists.\n",
        encoding="utf-8")
    (sec / "10-open-item.md").write_text(
        "- [ ] 🎯 **Fix the fail-open gate** — it exits 0 and covers nothing\n"
        "      continuation detail with a [link](../../method/REVIEW.md)\n",
        encoding="utf-8")
    return sec


class Index(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        self.sec = make_board(self.root)

    def tearDown(self):
        self._td.cleanup()

    def rebuild(self) -> str:
        board.run_check(self.root, fix=True)
        return (self.root / board.INDEX_REL).read_text(encoding="utf-8")

    def test_missing_index_is_stale_and_rebuild_heals(self):
        self.assertEqual(board.run_check(self.root, fix=False), 1)
        self.assertEqual(board.run_check(self.root, fix=True), 0)
        self.assertEqual(board.run_check(self.root, fix=False), 0)

    def test_item_edit_flips_check_red(self):
        self.rebuild()
        (self.sec / "10-open-item.md").write_text(
            "- [x] **Fix the fail-open gate** — done\n", encoding="utf-8")
        self.assertEqual(board.run_check(self.root, fix=False), 1)

    def test_done_renders_check_emoji_never_bracket_x(self):
        (self.sec / "20-done.md").write_text(
            "- [x] **Shipped** — landed and verified\n", encoding="utf-8")
        text = self.rebuild()
        self.assertIn("- ✅ [Shipped]", text)
        self.assertNotIn("- [x]", text)

    def test_numbers_sort_as_numbers_not_text(self):
        """010/200: a `1000-` item sorted before `130-` as text. Items and
        sections now sort by their leading number."""
        for n in ("130", "990", "1000"):
            (self.sec / f"{n}-item.md").write_text(
                f"- [ ] **Item {n}** — numbered\n", encoding="utf-8")
        sec9 = self.root / board.BOARD_DIR / "9-track-early"
        sec9.mkdir()
        (sec9 / "README.md").write_text("# Track early\n\nWhy.\n",
                                        encoding="utf-8")
        text = self.rebuild()
        order = [text.index(f"Item {n}") for n in ("130", "990", "1000")]
        self.assertEqual(order, sorted(order))
        self.assertLess(text.index("Track early"), text.index("Track A"))

    def test_board_order_puts_unnumbered_names_last(self):
        names = ["notes.md", "1000-b.md", "20-a.md", "130-c.md"]
        self.assertEqual(sorted(names, key=board.board_order),
                         ["20-a.md", "130-c.md", "1000-b.md", "notes.md"])

    def test_claim_fragment_surfaces_in_index(self):
        (self.sec / "30-claimed.md").write_text(
            "- [~] **Mid-flight** work (claimed 2026-08-15-0610, wt: b)\n",
            encoding="utf-8")
        self.assertIn("(claimed 2026-08-15-0610, wt: b)", self.rebuild())

    def test_pointer_item_keeps_its_glyph(self):
        (self.sec / "40-pointer.md").write_text(
            "- ⏳ Rule-4 review queued — delta aaa..bbb, intent record x\n",
            encoding="utf-8")
        self.assertIn("- ⏳ [", self.rebuild())

    def test_generated_marker_opens_the_index(self):
        self.assertTrue(self.rebuild().startswith(board.GENERATED_MARK))

    def test_rebuild_is_deterministic(self):
        self.assertEqual(self.rebuild(), self.rebuild())

    def test_stateless_item_file_is_a_defect(self):
        (self.sec / "50-broken.md").write_text("prose only\n", encoding="utf-8")
        self.assertEqual(board.run_check(self.root, fix=True), 1)

    def test_leading_comment_before_state_line_is_tolerated(self):
        (self.sec / "60-marked.md").write_text(
            "<!-- datescan:allow: historical dates quoted verbatim -->\n"
            "- [ ] **Marker-led item** — body\n", encoding="utf-8")
        self.assertIn("[Marker-led item]", self.rebuild())

    def test_index_links_resolve_relative_to_docs(self):
        text = self.rebuild()
        self.assertIn("(roadmap/10-track-a/10-open-item.md)", text)

    def test_flags_lift_but_title_stays_clean(self):
        text = self.rebuild()
        self.assertIn("🎯", text)
        self.assertIn("[Fix the fail-open gate]", text)

    def test_a_backticked_glyph_is_a_mention_not_a_flag(self):
        """130/020: an item ABOUT the queued-review glyph names it in a code
        span, and lifting it from there put that glyph on the item's index
        line — where a session counting the review queue counted it. The
        same glyph outside a code span still lifts."""
        (self.sec / "80-about-pointers.md").write_text(
            "- [ ] 🔎 **What a `⏳` pointer becomes when its verdict lands**\n",
            encoding="utf-8")
        (self.sec / "90-flagged.md").write_text(
            "- [ ] ⏳ **A child's own sense of the glyph** — waiting\n",
            encoding="utf-8")
        text = self.rebuild()
        about = next(l for l in text.splitlines() if "80-about" in l)
        self.assertTrue(about.startswith("- [ ] 🔎 ["), about)
        flagged = next(l for l in text.splitlines() if "90-flagged" in l)
        self.assertTrue(flagged.startswith("- [ ] ⏳ ["), flagged)

    def test_source_line_allow_markers_travel_to_the_index(self):
        """A projection reproduces exempted text, so it inherits the
        exemption — day-one live finding: the index re-flagged a verbatim
        date its item file had already scoped-allowed."""
        (self.sec / "70-dated.md").write_text(
            "- [ ] **Verbatim (15/7/26) title** "
            "<!-- datescan:allow: verbatim --> — body\n", encoding="utf-8")
        self.assertIn("<!-- datescan:allow: verbatim -->", self.rebuild())


class FloorArgv(unittest.TestCase):
    """The argv floor.py actually renders must RUN, not abort the process.

    `board` is registered enforced with no advisory form, so a parser that
    exits 2 on the floor's own template does not degrade — it blocks the
    commit, in every repo, on an argument the floor itself supplied. It did:
    the registry used to render `check --root <root> {scope}` with `action` a
    positional-with-`choices` ahead of `paths` — the only bare positional
    action word anywhere in the registry — so a bare invocation (no leading
    `check`/`rebuild`) bound the first remaining positional to `action` and
    failed its choices check (roadmap 010/090). `--check`/`--rebuild` flags
    remove the collision entirely: `paths` is the only positional left, so
    nothing competes with it for a slot regardless of where `{scope}` falls.

    floor.py's registry now renders `--check`/`--rebuild` (tools/floor.py's
    `board` entry). The bare `check`/`rebuild` word is kept working —
    unconditionally, not just for the floor — because every invocation on
    record before this change (child repos, docs, hooks) spells it that way,
    and nothing pinned to that spelling gets a flag day.
    """

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        make_board(self.root)

    def tearDown(self):
        self._td.cleanup()

    def test_scope_after_root_is_absorbed_not_fatal(self):
        # exactly floor.py's CURRENT rendered hook/ci argv for this scanner
        argv = ["--rebuild", "--root", str(self.root), str(self.root)]
        self.assertEqual(board.main(argv), 0)
        self.assertEqual(board.main(["--check", "--root", str(self.root),
                                     str(self.root)]), 0)

    def test_the_scope_does_not_displace_the_action(self):
        # a stale index must still be REPORTED through the floor's argv —
        # absorbing the scope must not quietly turn `--check` into `--rebuild`.
        self.assertEqual(
            board.main(["--check", "--root", str(self.root), str(self.root)]),
            1)

    def test_an_unknown_option_is_still_an_error(self):
        with self.assertRaises(SystemExit) as ctx:
            board.main(["--check", "--root", str(self.root), "--bogus"])
        self.assertEqual(ctx.exception.code, 2)

    def test_legacy_bare_word_argv_still_runs(self):
        # the PRE-flags spelling, pinned everywhere outside this repo too —
        # it must go on working exactly as before this change.
        argv = ["rebuild", "--root", str(self.root), str(self.root)]
        self.assertEqual(board.main(argv), 0)
        self.assertEqual(board.main(["check", "--root", str(self.root),
                                     str(self.root)]), 0)

    def test_legacy_word_does_not_displace_the_action_either(self):
        self.assertEqual(
            board.main(["check", "--root", str(self.root), str(self.root)]),
            1)

    def test_legacy_unknown_option_is_still_an_error(self):
        with self.assertRaises(SystemExit) as ctx:
            board.main(["check", "--root", str(self.root), "--bogus"])
        self.assertEqual(ctx.exception.code, 2)

    def test_check_and_rebuild_flags_are_mutually_exclusive(self):
        with self.assertRaises(SystemExit) as ctx:
            board.main(["--check", "--rebuild", "--root", str(self.root)])
        self.assertEqual(ctx.exception.code, 2)

    def test_legacy_word_cannot_combine_with_the_opposite_flag(self):
        with self.assertRaises(SystemExit) as ctx:
            board.main(["check", "--rebuild", "--root", str(self.root)])
        self.assertEqual(ctx.exception.code, 2)


class OutOfScope(unittest.TestCase):
    def test_bare_tree_exits_zero_and_says_why(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(board.run_check(Path(td), fix=False), 0)

    def test_selftest_passes(self):
        self.assertEqual(board.selftest(), 0)


class DuplicateNumbers(unittest.TestCase):
    """A duplicate section or item number is invisible to git (roadmap 010/120).

    Two sessions allocating the next N from stale views mint the same number,
    and two NEW files are not a shared line — so no conflict fires, the rebuilt
    index is well-formed, and the pair sorts adjacently and reads as
    intentional. One such pair sat on atelier's own board for six days. The
    contract these pin: the collision reds `check` AND `rebuild`, and the
    message names the colliding files rather than only the number.
    """

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        self.sec = make_board(self.root)
        board.run_check(self.root, fix=True)

    def tearDown(self):
        self._td.cleanup()

    def _second_section(self, name):
        d = self.root / board.BOARD_DIR / name
        d.mkdir()
        (d / "README.md").write_text("# Another\n", encoding="utf-8")
        return d

    def test_clean_board_has_no_collision(self):
        self.assertEqual(0, board.run_check(self.root, fix=False))

    def test_duplicate_section_number_is_caught(self):
        # Rebuild FIRST, so the index cannot be stale: without that step this
        # passes on an unfixed tool for the wrong reason — staleness, not the
        # collision — which is the vacuous-test shape 370/030 exists to catch.
        self._second_section("10-track-a-again")
        board.run_check(self.root, fix=True)
        self.assertEqual(1, board.run_check(self.root, fix=False))

    def test_a_rebuild_cannot_paper_over_a_section_collision(self):
        # The failure mode that let the real one survive: `rebuild` produced a
        # perfectly well-formed index and returned success.
        self._second_section("10-track-a-again")
        self.assertEqual(1, board.run_check(self.root, fix=True))

    def test_duplicate_item_number_is_caught(self):
        (self.sec / "10-also-ten.md").write_text(
            "- [ ] **Also ten**\n", encoding="utf-8")
        board.run_check(self.root, fix=True)   # not stale — only colliding
        self.assertEqual(1, board.run_check(self.root, fix=False))

    def test_message_names_the_colliding_files(self):
        (self.sec / "10-also-ten.md").write_text(
            "- [ ] **Also ten**\n", encoding="utf-8")
        _, problems = board.build_index(self.root / board.BOARD_DIR)
        joined = " ".join(problems)
        self.assertIn("10-open-item.md", joined)
        self.assertIn("10-also-ten.md", joined)

    def test_different_sections_may_reuse_a_number(self):
        # Numbering is per-directory: `10` in two different sections is normal
        # and must not fire, or the check is unusable.
        other = self._second_section("20-track-b")
        (other / "10-its-own-ten.md").write_text(
            "- [ ] **Track B's ten**\n", encoding="utf-8")
        self.assertEqual(0, board.run_check(self.root, fix=True))

    def test_readme_is_not_an_item(self):
        # Every section has a README.md with no leading number; it must never
        # be counted as an item, at any grain.
        self.assertEqual([], board.number_collisions(
            ["README.md", "10-a.md", "20-b.md"], "x", "item"))


class ClaimInTheFallbackTitle(unittest.TestCase):
    """A wrapped bold title sends index_title down its fallback path, and the
    fallback used to start at the claim (roadmap 010/140).

    `index_line` already surfaces the claim separately, so the fallback taking
    the head of `rest` rendered it twice on one line.
    """

    def test_wrapped_title_does_not_repeat_the_claim(self):
        rest = ("🔥 (claimed 2026-08-23-1259, wt: x) **A title that keeps\n"
                "      going onto a second line** — and then some body")
        self.assertNotIn("claimed", board.index_title(rest))

    def test_closed_bold_span_is_unaffected(self):
        rest = "**A closed title** (claimed 2026-08-23-1259, wt: x) — body"
        self.assertEqual("A closed title", board.index_title(rest))

    def test_the_claim_still_reaches_the_index_line(self):
        # Stripping it from the TITLE must not strip it from the LINE — the
        # claim is what tells another session the item is taken.
        line = board.index_line(
            "[~]", "🔥 (claimed 2026-08-23-1259, wt: x) **Wrapped\n      title**",
            "roadmap/10-a/10-b.md")
        self.assertIn("(claimed 2026-08-23-1259, wt: x)", line)


class LogicalFirstParagraph(unittest.TestCase):
    """010/170 (from 320/450 §1) — the index projects an item's LOGICAL first
    paragraph, not its first physical line, so a bold title or a claim that
    wraps onto line two still reaches the index. Synthetic fixtures only."""

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        self.sec = make_board(self.root)

    def tearDown(self):
        self._td.cleanup()

    def line_for(self, name: str, body: str) -> str:
        (self.sec / name).write_text(body, encoding="utf-8")
        board.run_check(self.root, fix=True)
        text = (self.root / board.INDEX_REL).read_text(encoding="utf-8")
        return next(l for l in text.splitlines() if name in l)

    def test_a_wrapped_title_projects_whole(self):
        line = self.line_for(
            "20-wrapped.md",
            "- [ ] 🎯 **A synthetic title long enough that it\n"
            "      wraps onto a second line** — and then the body\n")
        self.assertIn("[A synthetic title long enough that it wraps onto a "
                      "second line]", line)

    def test_a_wrapped_claim_projects(self):
        line = self.line_for(
            "30-claimed.md",
            "- [~] **A claimed item whose title fills the first\n"
            "      line** (claimed 2026-01-02-0304, wt: example-wt)\n"
            "      and more prose after it.\n")
        # The whole claim stays; the title is squeezed to the room it leaves
        # (320/730), so the wrapped title ends at a word boundary with `…`.
        self.assertTrue(line.startswith(
            "- [~] (claimed 2026-01-02-0304, wt: example-wt) [A claimed item "
            "whose title fills the…]("), line)

    def test_the_allow_marker_still_propagates(self):
        # On the state line, as before, and from the continuation line the
        # wrapped title ends on — the text it exempts now reaches the index.
        line = self.line_for(
            "40-marked.md",
            "- [ ] **Verbatim (15/7/26) title** "
            "<!-- datescan:allow: verbatim --> — body\n")
        self.assertIn("<!-- datescan:allow: verbatim -->", line)
        line = self.line_for(
            "50-wrapped-marked.md",
            "- [ ] **A wrapped title that ends on line two with a\n"
            "      date (15/7/26)** <!-- datescan:allow: quoted -->\n")
        self.assertIn("<!-- datescan:allow: quoted -->", line)

    def test_a_marker_deep_in_the_paragraph_does_not_travel(self):
        line = self.line_for(
            "60-deep.md",
            "- [ ] **A one-line title** — body\n"
            "      more body\n"
            "      a far line <!-- pathscan:allow: about the prose -->\n")
        self.assertNotIn("pathscan:allow", line)

    def test_the_paragraph_ends_at_a_blank_line_or_a_new_block(self):
        line = self.line_for(
            "70-stops.md",
            "- [~] **Title**\n"
            "      - (claimed 2026-01-02-0304, wt: in-a-sub-bullet)\n")
        self.assertNotIn("claimed", line)
        line = self.line_for(
            "80-blank.md",
            "- [~] **Title**\n\n"
            "      (claimed 2026-01-02-0304, wt: after-a-blank)\n")
        self.assertNotIn("claimed", line)

    def test_a_marker_on_the_line_a_plain_title_reaches_into_travels(self):
        """160/970 PP2. With no bold span, the title is the first 70 characters
        of the PARAGRAPH, so a line-two fragment is reproduced into the index
        line; its allow-marker has to travel with it, or the index line fails
        the very scanner the item file had already exempted."""
        line = self.line_for(
            "21-plain.md",
            "- [ ] a plain-text title that wraps onto its second line\n"
            "      (15/7/26) <!-- datescan:allow: synthetic fixture --> and on\n")
        self.assertIn("(15/7/26)", line)
        self.assertTrue(line.endswith("<!-- datescan:allow: synthetic fixture -->"),
                        line)

    def test_a_marker_beyond_the_plain_titles_reach_does_not_travel(self):
        """The other direction: once line one alone fills the title, a marker on
        line two exempts prose the index never shows, and must not travel."""
        line = self.line_for(
            "22-plain.md",
            "- [ ] a plain-text title long enough that the first line alone fills the cap and more\n"
            "      later words <!-- datescan:allow: synthetic fixture -->\n")
        self.assertNotIn("datescan:allow", line)

    def test_a_code_span_that_wraps_from_line_one_masks_what_it_spans(self):
        """160/970 PP6, pinned as the documented shape (see `_mask_code`): the
        span is read across the joined paragraph, as the renderer reads it, so a
        marker between an odd backtick and the next one is masked."""
        line = self.line_for(
            "23-span.md",
            "- [ ] **A title** with a stray ` backtick\n"
            "      then <!-- datescan:allow: synthetic fixture --> a closing ` here\n")
        self.assertNotIn("datescan:allow", line)

    def test_a_flag_in_continuation_prose_is_a_mention(self):
        line = self.line_for(
            "90-mention.md",
            "- [ ] **A plain item**\n"
            "      whose prose talks about the 🎯 glyph\n")
        self.assertTrue(line.startswith("- [ ] [A plain item]("), line)

    def test_a_backticked_claim_is_a_mention(self):
        line = self.line_for(
            "95-about-claims.md",
            "- [~] **About the `(claimed …)` fragment**\n")
        # Nothing between the glyph and the link: no claim was surfaced.
        self.assertTrue(line.startswith("- [~] [About the"), line)


class LegacyGrace(unittest.TestCase):
    """010/170's grace period: `--check` accepts an index rendered by the
    PREVIOUS projection until `LEGACY_INDEX_ACCEPTED_UNTIL`, says so when it
    does, and refuses it from that date. Synthetic fixtures only."""

    BEFORE = board.LEGACY_INDEX_ACCEPTED_UNTIL.fromordinal(
        board.LEGACY_INDEX_ACCEPTED_UNTIL.toordinal() - 1)
    ON = board.LEGACY_INDEX_ACCEPTED_UNTIL

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        self.sec = make_board(self.root)
        # An item the two projections render differently: a wrapped claim.
        (self.sec / "20-wrapped.md").write_text(
            "- [~] **A claimed item whose title fills the first\n"
            "      line** (claimed 2026-01-02-0304, wt: example-wt)\n",
            encoding="utf-8")
        self.board = self.root / board.BOARD_DIR
        self.index = self.root / board.INDEX_REL
        self.new, _ = board.build_index(self.board)
        self.old, _ = board.build_index(self.board,
                                        _entry=board._index_entry_v1)
        self.assertNotEqual(self.new, self.old, "fixture must discriminate")

    def tearDown(self):
        self._td.cleanup()

    def check(self, today) -> tuple[int, str]:
        import contextlib
        import io
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = board.run_check(self.root, fix=False, today=today)
        return rc, buf.getvalue()

    def test_check_passes_on_a_new_form_index(self):
        self.index.write_text(self.new, encoding="utf-8")
        for today in (self.BEFORE, self.ON):
            rc, out = self.check(today)
            self.assertEqual(rc, 0, out)
            self.assertNotIn("PREVIOUS projection", out)

    def test_check_passes_on_an_old_form_index_before_the_date(self):
        self.index.write_text(self.old, encoding="utf-8")
        rc, out = self.check(self.BEFORE)
        self.assertEqual(rc, 0, out)
        self.assertIn("PREVIOUS projection", out)
        self.assertIn("rebuild", out)
        self.assertIn(self.ON.isoformat(), out)

    def test_check_fails_on_an_old_form_index_from_the_date(self):
        self.index.write_text(self.old, encoding="utf-8")
        rc, out = self.check(self.ON)
        self.assertEqual(rc, 1, out)
        self.assertIn("stale", out)
        self.assertNotIn("PREVIOUS projection", out)

    def test_check_fails_on_an_index_that_matches_neither(self):
        self.index.write_text(self.new.replace("example-wt", "other-wt"),
                              encoding="utf-8")
        rc, out = self.check(self.BEFORE)
        self.assertEqual(rc, 1, out)
        self.assertIn("stale", out)

    def test_rebuild_always_writes_the_new_form(self):
        self.index.write_text(self.old, encoding="utf-8")
        board.run_check(self.root, fix=True, today=self.BEFORE)
        self.assertEqual(self.index.read_text(encoding="utf-8"), self.new)

    def test_the_legacy_renderer_reads_the_first_line_only(self):
        self.assertIn("- [~] [A claimed item whose title fills the first](",
                      self.old)

    def test_the_end_date_is_pinned(self):
        """160/970 PP3. Every other test here derives from the constant, so
        moving it left them green. Mike made 2026-11-18 firm, UTC, no flag."""
        self.assertEqual(date(2026, 11, 18), board.LEGACY_INDEX_ACCEPTED_UNTIL)

    def test_the_default_date_is_todays_utc_date(self):
        """160/970 PP3. `_today_utc` was reached by no test: they all inject
        `today`. Here it is the clock that decides."""
        self.index.write_text(self.old, encoding="utf-8")
        for fake, want_rc in ((self.BEFORE, 0), (self.ON, 1)):
            buf = io.StringIO()
            with mock.patch.object(board, "_today_utc", return_value=fake), \
                    contextlib.redirect_stdout(buf):
                rc = board.run_check(self.root, fix=False)
            self.assertEqual(want_rc, rc, buf.getvalue())

    def test_the_notice_says_utc_and_points_a_wrapscan_child_at_the_readme(self):
        """160/970 PP8 and PP1: the zone, and the standing advice that the
        projected index is not rewrappable by hand."""
        self.index.write_text(self.old, encoding="utf-8")
        _, out = self.check(self.BEFORE)
        self.assertIn("(UTC)", out)
        self.assertIn("wrapscan", out)
        self.assertIn("tools/README.md", out)

    def test_a_notice_beside_a_real_failure_says_which_one_fails(self):
        """160/970 PP8: the grace notice used to print as an 'accepted' line
        directly beside exit 1, which read as if the index were the failure."""
        self.index.write_text(self.old, encoding="utf-8")
        (self.sec / "30-no-state.md").write_text("prose first\n", encoding="utf-8")
        rc, out = self.check(self.BEFORE)
        self.assertEqual(1, rc, out)
        self.assertIn("a notice, not the failure", out)

    def test_the_legacy_renderer_reproduces_the_pre_delta_tool_byte_for_byte(self):
        """160/970 PP3. `_index_entry_v1` was pinned by nothing but a reviewer's
        probe. These strings are what the tool printed before 010/170 landed,
        for the shapes children's committed indexes hold; if the grace's
        renderer drifts, a child's old-form index stops being accepted."""
        cases = [
            ("- [ ] 🎯 **Fix the fail-open gate** — it exits 0\n      continuation\n",
             "- [ ] 🎯 [Fix the fail-open gate](roadmap/a/b.md)"),
            ("- [~] (claimed 2026-01-02-0304, wt: example-wt) **A claimed item**\n",
             "- [~] (claimed 2026-01-02-0304, wt: example-wt) [A claimed item](roadmap/a/b.md)"),
            ("- [ ] a plain title with no bold at all, carried on a single line of text well past the cap of seventy chars\n",
             "- [ ] [a plain title with no bold at all, carried on a single line of text…](roadmap/a/b.md)"),
            ("- [x] **Done thing** <!-- datescan:allow: synthetic -->\n",
             "- ✅ [Done thing](roadmap/a/b.md) <!-- datescan:allow: synthetic -->"),
            ("- [ ] **About the `⏳` glyph** and `(claimed x)` mention\n",
             "- [ ] [About the glyph](roadmap/a/b.md)"),
            ("- ⏳ 🔎 **Queued review pointer** thing\n",
             "- ⏳ 🔎 [Queued review pointer](roadmap/a/b.md)"),
        ]
        for text, want in cases:
            self.assertEqual(want, board._index_entry_v1(text, "roadmap/a/b.md"), text)

    def test_a_continuation_must_be_indented_to_join_the_paragraph(self):
        """160/970 PP3: the indented-only rule. An unindented line after the
        state line is not part of the state line's paragraph."""
        text = "- [ ] **A title that\ncontinues unindented** (claimed 2026-01-02, wt: x)\n"
        state = board.item_state(text)
        self.assertEqual(("**A title that",), state.lines)


class AdvisoryCount(unittest.TestCase):
    """160/970 PP5: every `--check` prints one `board advisory: N finding(s)`
    line, which `floor.py` reads into the floor's board. N is 1 on a run that
    used the grace, else 0. A missing line would read as -1 (a drifted
    contract), so it prints on the not-in-scope path too."""

    def run_main(self, root: Path, *args: str) -> tuple[int, str]:
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = board.main(["--check", "--root", str(root), *args])
        return rc, buf.getvalue()

    def test_a_tree_with_no_board_prints_a_zero(self):
        with tempfile.TemporaryDirectory() as td:
            rc, out = self.run_main(Path(td))
        self.assertEqual(0, rc)
        self.assertIn("board advisory: 0 finding(s) — reported, not blocking.", out)

    def test_a_current_index_prints_a_zero(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            make_board(root)
            board.run_check(root, fix=True)
            rc, out = self.run_main(root)
        self.assertEqual(0, rc, out)
        self.assertIn("board advisory: 0 finding(s)", out)

    def test_a_grace_run_prints_a_one(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            sec = make_board(root)
            (sec / "20-wrapped.md").write_text(
                "- [~] **A claimed item whose title fills the first\n"
                "      line** (claimed 2026-01-02-0304, wt: example-wt)\n",
                encoding="utf-8")
            old, _ = board.build_index(root / board.BOARD_DIR,
                                       _entry=board._index_entry_v1)
            (root / board.INDEX_REL).write_text(old, encoding="utf-8")
            until = board.LEGACY_INDEX_ACCEPTED_UNTIL
            with mock.patch.object(board, "_today_utc",
                                   return_value=until.fromordinal(until.toordinal() - 1)):
                rc, out = self.run_main(root)
        self.assertEqual(0, rc, out)
        self.assertIn("board advisory: 1 finding(s) — reported, not blocking.", out)

    def test_a_stale_index_prints_a_zero_and_still_fails(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            make_board(root)
            rc, out = self.run_main(root)
        self.assertEqual(1, rc, out)
        self.assertIn("board advisory: 0 finding(s)", out)

    def test_rebuild_does_not_print_it(self):
        """`floor.py` only ever runs `--check`; a rebuild's output is not a check's."""
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            make_board(root)
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = board.main(["--rebuild", "--root", str(root)])
        self.assertEqual(0, rc)
        self.assertNotIn("advisory", buf.getvalue())


class BoundedMemory(unittest.TestCase):
    """020/380 — measured, not fixed. `board` is one of the two tools
    (alongside `pointerscan`) the item's own brief names as a legitimate
    exception: it IS the whole board's generated index, so part of its
    footprint grows with the number of items by nature, and pretending a
    growing thing is constant would be dishonest in the other direction.

    What was actually checked here is that the growth is LINEAR in item
    count (a per-item constant), never worse — a quadratic regression would
    still be a genuine defect this class of tool could hide. Measured while
    building this test, subprocess + `memprobe` (`--check` and `--rebuild`
    both walk every item file):

      500 items    ~17.6-17.8 MB peak RSS
      5,000 items  ~19.4-20.0 MB peak RSS   (+4,500 items, ~+1.8-2.2 MB)
      10,000 items measured separately (elapsed only) at ~3.5s — no timeout,
                   no superlinear blow-up

    ~0.4-0.5 KB held per item, and time stays in the single-digit seconds at
    10,000 items — both consistent with a linear design. This is the
    documented growth, not an inert one: the bound below is deliberately
    generous (an order of magnitude over the measured per-item rate) so the
    test catches a future SUPERLINEAR regression without being fitted to
    today's exact number (`ground-numeric-limits`).
    """

    BOARD = str(TOOLS_DIR / "board.py")
    SMALL_ITEMS = 500     # 10 sections x 50 items
    LARGE_ITEMS = 5_000   # 50 sections x 100 items
    # Generous: measured growth was ~2 MB for a 4,500-item delta (~0.45
    # KB/item). Bounding at 2 KB/item leaves headroom for allocator noise
    # while still catching an accidental switch to an O(n^2) or
    # whole-tree-cached shape, which would blow well past this on 4,500 more
    # items.
    MAX_BYTES_PER_ITEM = 2 * 1024

    @staticmethod
    def _build(root: Path, sections: int, items_per_section: int) -> None:
        b = root / board.BOARD_DIR
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
            [sys.executable, self.BOARD, "--check", "--root", str(tmp), str(tmp)],
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
            f"{self.MAX_BYTES_PER_ITEM}-byte/item bound. board.py's index "
            "growth is legitimate (020/380 names it as an exception) but it "
            "must stay LINEAR — this looks like a superlinear regression.")


def _git(root: Path, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "-C", str(root), *args],
                          capture_output=True, text=True, check=True)


class StagedPlane(unittest.TestCase):
    """010/020 (BS1's fund) — `--staged`/`--from-index` read the git INDEX,
    not the worktree, closing the two live slips that made the hook's
    guarantee weaker than it looked: an index rebuilt but never staged, and a
    rebuild that absorbed a SIBLING's dirty, unstaged item line into the
    index this commit is about to make true. Both need a real git repo — the
    plane they read does not exist without one — so unlike the rest of this
    file these tests actually run `git`, and are skipped (not soft-passed) if
    `git` is not on PATH.
    """

    def setUp(self):
        if shutil.which("git") is None:
            self.skipTest("git not on PATH")
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        self.sec = make_board(self.root)
        _git(self.root, "init", "-q")
        _git(self.root, "config", "user.email",
             "test@example.invalid")  # leakscan:allow: RFC 2606 reserved domain, throwaway git identity
        _git(self.root, "config", "user.name", "test")
        # A host whose global config signs commits with a key the test cannot
        # reach would otherwise ERROR all twelve tests here (160/970, PP9).
        _git(self.root, "config", "commit.gpgsign", "false")
        board.run_check(self.root, fix=True)          # write a current index
        _git(self.root, "add", "-A")
        _git(self.root, "commit", "-q", "-m", "seed")

    def tearDown(self):
        self._td.cleanup()

    def test_clean_committed_board_passes_staged_check(self):
        self.assertEqual(
            board.run_check(self.root, fix=False, source=board.INDEX), 0)

    def test_rebuild_from_index_matches_rebuild_from_worktree_when_clean(self):
        # No dirt anywhere: the two planes must agree, or the new plane is
        # answering a different question rather than the same one differently.
        self.assertEqual(
            board.run_check(self.root, fix=True, source=board.INDEX), 0)

    def test_quoted_paths_are_read_on_the_staged_plane(self):
        """115/260. `git ls-files` C-quotes a path holding a non-ASCII byte,
        tab, double quote or backslash when it writes lines, so a section
        directory or item file spelt that way was split into the wrong parts
        and dropped from the staged index. `-z` hands over the raw path: the
        staged plane must agree with the worktree plane, item and all."""
        sec = self.root / board.BOARD_DIR / "20-café track"
        sec.mkdir()
        (sec / "README.md").write_text("# Café\n\nWhy.\n", encoding="utf-8")
        (sec / '10-say "hi".md').write_text(
            "- [ ] 🎯 **Quoted item** — still read\n", encoding="utf-8")
        (sec / "20-tab\tname.md").write_text(
            "- [ ] 🎯 **Tabbed item** — still read\n", encoding="utf-8")
        _git(self.root, "add", "-A")
        staged, _ = board.build_index(self.root / board.BOARD_DIR, board.INDEX)
        disk, _ = board.build_index(self.root / board.BOARD_DIR, board.WORKTREE)
        self.assertEqual(staged, disk)
        self.assertIn("Quoted item", staged)
        self.assertIn("Tabbed item", staged)

    def test_staged_plane_sorts_numbers_as_numbers(self):
        """010/200 on the INDEX plane: both planes order a four-digit item
        after a three-digit one, so they still agree."""
        for n in ("130", "1000"):
            (self.sec / f"{n}-item.md").write_text(
                f"- [ ] **Item {n}** — numbered\n", encoding="utf-8")
        _git(self.root, "add", "-A")
        staged, _ = board.build_index(self.root / board.BOARD_DIR, board.INDEX)
        disk, _ = board.build_index(self.root / board.BOARD_DIR, board.WORKTREE)
        self.assertEqual(staged, disk)
        self.assertLess(staged.index("Item 130"), staged.index("Item 1000"))

    def test_environment_error_outside_a_git_repo(self):
        with tempfile.TemporaryDirectory() as bare:
            self.assertEqual(
                board.run_check(Path(bare), fix=False, source=board.INDEX), 2)

    def test_not_in_scope_when_index_has_no_board_dir(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            _git(root, "init", "-q")
            _git(root, "config", "user.email",
                 "test@example.invalid")  # leakscan:allow: RFC 2606 reserved domain, throwaway git identity
            _git(root, "config", "user.name", "test")
            (root / "placeholder.txt").write_text("x\n")
            _git(root, "add", "-A")
            _git(root, "commit", "-q", "-m", "init")
            self.assertEqual(
                board.run_check(root, fix=False, source=board.INDEX), 0)

    # --- SLIP (a): rebuilt but not staged --------------------------------

    def test_slip_a_rebuilt_but_unstaged_index_passes_worktree_check(self):
        """The BUG as it shipped, pinned so it can never come back silently.
        Stage an item edit, rebuild the index ON DISK, but never `git add`
        the rebuilt index. The worktree plane (the check's old, and still
        default, behaviour) reads disk for BOTH sides and finds them
        agreeing with each other — a clean verdict that says nothing about
        what is actually staged."""
        (self.sec / "10-open-item.md").write_text(
            "- [x] **Fix the fail-open gate** — done\n", encoding="utf-8")
        _git(self.root, "add", str(self.sec / "10-open-item.md"))
        board.run_check(self.root, fix=True)     # rebuild ON DISK, don't add it
        self.assertEqual(
            board.run_check(self.root, fix=False), 0,
            "worktree plane is blind to this slip by construction — pinning "
            "that so a future change to the default plane is a deliberate "
            "decision, not a silent regression")

    def test_slip_a_is_caught_on_the_staged_plane(self):
        """The FIX: `--staged` compares the staged item files against the
        staged ROADMAP.md — both via `git show :path` — so the still-old
        staged blob of ROADMAP.md (never `git add`ed after the rebuild) is
        caught even though the worktree agrees with itself."""
        (self.sec / "10-open-item.md").write_text(
            "- [x] **Fix the fail-open gate** — done\n", encoding="utf-8")
        _git(self.root, "add", str(self.sec / "10-open-item.md"))
        board.run_check(self.root, fix=True)     # rebuild ON DISK, don't add it
        rc = board.run_check(self.root, fix=False, source=board.INDEX)
        self.assertEqual(rc, 1, "the staged plane must catch the unstaged "
                                "rebuild that the worktree plane missed")

    def test_slip_a_is_healed_by_rebuild_from_index_then_staging(self):
        (self.sec / "10-open-item.md").write_text(
            "- [x] **Fix the fail-open gate** — done\n", encoding="utf-8")
        _git(self.root, "add", str(self.sec / "10-open-item.md"))
        board.run_check(self.root, fix=True, source=board.INDEX)
        _git(self.root, "add", str(self.root / board.INDEX_REL))
        self.assertEqual(
            board.run_check(self.root, fix=False, source=board.INDEX), 0)

    # --- SLIP (b): a sibling's dirty item line gets absorbed --------------

    def test_slip_b_plain_rebuild_absorbs_a_dirty_siblings_line(self):
        """The BUG as it shipped. A second, unrelated item exists, committed
        clean. A "sibling session" then dirties it on disk WITHOUT staging
        it — exactly the shape of a shared, dirty primary checkout. A
        claimer editing a DIFFERENT item runs the plain (worktree) `rebuild`
        and it bakes the sibling's unstaged text into the generated index."""
        (self.sec / "20-sibling.md").write_text(
            "- [ ] **A sibling's item** — untouched\n", encoding="utf-8")
        _git(self.root, "add", "-A")
        board.run_check(self.root, fix=True)
        _git(self.root, "add", "-A")
        _git(self.root, "commit", "-q", "-m", "add sibling item")

        # The sibling dirties their OWN item, on disk, unstaged.
        (self.sec / "20-sibling.md").write_text(
            "- [ ] **A sibling's item — WIP, uncommitted** — do not ship this\n",
            encoding="utf-8")

        # The claimer stages an edit to a DIFFERENT item, then runs the
        # plain worktree rebuild — the tool has no way to tell "my staged
        # edit" from "someone else's dirty file sitting in the same tree".
        (self.sec / "10-open-item.md").write_text(
            "- [x] **Fix the fail-open gate** — done\n", encoding="utf-8")
        _git(self.root, "add", str(self.sec / "10-open-item.md"))
        board.run_check(self.root, fix=True)
        rebuilt = (self.root / board.INDEX_REL).read_text(encoding="utf-8")
        self.assertIn("WIP, uncommitted", rebuilt,
                       "pins the bug: the plain rebuild reads the dirty "
                       "sibling line straight off disk")

    def test_slip_b_is_avoided_by_rebuild_from_index(self):
        """The FIX. Same setup as the slip-b bug test, but the claimer runs
        `rebuild --from-index`: it reads every item via `git show :path`, so
        the sibling's item — never staged — reads back as its last
        COMMITTED content, not the dirty text sitting unstaged on disk."""
        (self.sec / "20-sibling.md").write_text(
            "- [ ] **A sibling's item** — untouched\n", encoding="utf-8")
        _git(self.root, "add", "-A")
        board.run_check(self.root, fix=True)
        _git(self.root, "add", "-A")
        _git(self.root, "commit", "-q", "-m", "add sibling item")

        (self.sec / "20-sibling.md").write_text(
            "- [ ] **A sibling's item — WIP, uncommitted** — do not ship this\n",
            encoding="utf-8")

        (self.sec / "10-open-item.md").write_text(
            "- [x] **Fix the fail-open gate** — done\n", encoding="utf-8")
        _git(self.root, "add", str(self.sec / "10-open-item.md"))

        board.run_check(self.root, fix=True, source=board.INDEX)
        rebuilt = (self.root / board.INDEX_REL).read_text(encoding="utf-8")
        self.assertNotIn("WIP, uncommitted", rebuilt,
                         "the fix: --from-index never reads the sibling's "
                         "unstaged line")
        self.assertIn("A sibling's item", rebuilt,
                      "the sibling's last COMMITTED content is still there — "
                      "this is a plane fix, not a data-loss fix")
        # And the claimer's OWN staged edit is fully reflected.
        self.assertIn("✅ [Fix the fail-open gate]", rebuilt)

    def test_argv_wires_staged_and_from_index_flags(self):
        argv_check = ["--check", "--staged", "--root", str(self.root)]
        argv_rebuild = ["--rebuild", "--from-index", "--root", str(self.root)]
        self.assertEqual(board.main(argv_check),
                         board.run_check(self.root, fix=False,
                                         source=board.INDEX))
        self.assertEqual(board.main(argv_rebuild), 0)


    def test_the_grace_holds_on_the_staged_plane(self):
        """010/170: `--staged` reads the same comparison, so an old-form
        STAGED index passes with the notice before the date, and fails from
        it, exactly as the worktree plane does."""
        import contextlib
        import io
        (self.sec / "20-wrapped.md").write_text(
            "- [~] **A claimed item whose title fills the first\n"
            "      line** (claimed 2026-01-02-0304, wt: example-wt)\n",
            encoding="utf-8")
        old, _ = board.build_index(self.root / board.BOARD_DIR,
                                   _entry=board._index_entry_v1)
        (self.root / board.INDEX_REL).write_text(old, encoding="utf-8")
        _git(self.root, "add", "-A")
        until = board.LEGACY_INDEX_ACCEPTED_UNTIL
        before = until.fromordinal(until.toordinal() - 1)
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = board.run_check(self.root, fix=False, source=board.INDEX,
                                 today=before)
        self.assertEqual(rc, 0, buf.getvalue())
        self.assertIn("PREVIOUS projection", buf.getvalue())
        self.assertIn("--from-index", buf.getvalue())
        with contextlib.redirect_stdout(io.StringIO()):
            rc = board.run_check(self.root, fix=False, source=board.INDEX,
                                 today=until)
        self.assertEqual(rc, 1)


LONG_PATH = ("roadmap/320-child-filed-findings-via-pointing-up/"
             "730-an-item-whose-slug-runs-on-and-on-for-a-long-while-yes.md")


class ClaimedLineFitsWrapscan(unittest.TestCase):
    """320/730 (and 750) — a claimed item's index line must pass `wrapscan`,
    which reads a line over 85 columns as prose unless its overflow is one
    unbreakable token. Every index line ends in a store path, so the line
    passes while no space of it sits past column 85. The real scanner judges
    here, not a re-statement of its rule."""

    TITLE = ("**Hand-up: the paragraph projection joins a wrapped claim into "
             "one index line which a child refuses**")

    def scan(self, line: str):
        import wrapscan
        return wrapscan.scan_text("x.md", line + "\n")

    def test_the_hand_up_case_passes_wrapscan(self):
        # 750's measured case: the shortest one-line claim, a long path.
        rest = f"🔎 {self.TITLE} (claimed 2026-10-26-1010, wt: doctrine-0a2b7a7)"
        line = board.index_line("[~]", rest, LONG_PATH, head=rest)
        self.assertGreater(len(line), 85, "fixture should overrun the width")
        self.assertEqual([], self.scan(line), line)
        self.assertIn("wt: doctrine-0a2b7a7", line)

    def test_a_long_worktree_name_is_cut_not_the_title_alone(self):
        rest = (f"🔎 {self.TITLE} (claimed 2026-11-03-0638, "
                "wt: atelier-qr-4c65-a-worktree-with-a-very-long-name)")
        line = board.index_line("[~]", rest, LONG_PATH, head=rest)
        self.assertEqual([], self.scan(line), line)
        self.assertIn("(claimed 2026-11-03, wt: atelier-qr-4c65-a-", line)
        self.assertIn("…)", line)

    def test_the_claim_drops_its_time_before_it_drops_the_title(self):
        rest = (f"🔎 {self.TITLE} "
                "(claimed 2026-11-03-0638, wt: atelier-qr-4c65-board)")
        line = board.index_line("[~]", rest, LONG_PATH, head=rest)
        self.assertTrue(line.startswith(
            "- [~] 🔎 (claimed 2026-11-03, wt: atelier-qr-4c65-board) [Hand-up"),
            line)
        self.assertEqual([], self.scan(line), line)

    def test_a_short_claim_is_untouched(self):
        rest = "**Short title here** (claimed 2026-08-15-0610, wt: b)"
        line = board.index_line("[~]", rest, "roadmap/a/b.md", head=rest)
        self.assertEqual("- [~] (claimed 2026-08-15-0610, wt: b) "
                         "[Short title here](roadmap/a/b.md)", line)

    def test_an_unclaimed_line_is_unchanged_at_the_longest_title(self):
        title = "word " * 30
        rest = f"🎯🔥🛑🔎🤔 **{title.strip()}**"
        line = board.index_line("[ ]", rest, LONG_PATH, head=rest)
        self.assertTrue(line.startswith("- [ ] 🎯🔥🛑🔎🤔 [word word"), line)
        self.assertEqual([], self.scan(line), line)

    def test_no_claim_fragment_cannot_reach_the_wrapscan_wall_on_a_real_board(self):
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        sec = make_board(root)
        (sec / "30-claimed.md").write_text(
            f"- [~] {self.TITLE}\n      (claimed 2026-10-26-1010, wt: x-y)\n",
            encoding="utf-8")
        board.run_check(root, fix=True)
        text = (root / board.INDEX_REL).read_text(encoding="utf-8")
        self.assertEqual([], self.scan(next(
            l for l in text.splitlines() if "30-claimed" in l)))


class BracketsInATitle(unittest.TestCase):
    """320/450 §2 — `index_title` never escaped `]`, so a bracket in a bold
    title closed the generated link early or opened another one."""

    def test_a_bare_bracket_pair_is_neutralised(self):
        t = board.index_title("**Fix the [~] marker**")
        self.assertNotIn("[", t)
        self.assertNotIn("]", t)
        self.assertEqual("Fix the &#91;~&#93; marker", t)

    def test_a_close_bracket_then_paren_is_not_a_link(self):
        # The probe shape, built here rather than written out in this file's
        # records: a `]` directly followed by `(`.
        t = board.index_title("**Bad " + "]" + "(elsewhere) title**")
        self.assertNotIn("](", t)
        line = board.index_line("[ ]", "**Bad " + "]" + "(elsewhere) title**",
                                "roadmap/a/b.md")
        self.assertEqual("- [ ] [Bad &#93;(elsewhere) title](roadmap/a/b.md)",
                         line)

    def test_the_generated_line_has_exactly_one_link(self):
        import re
        line = board.index_line("[ ]", "**A [x] and [y](z) title**",
                                "roadmap/a/b.md")
        self.assertEqual(1, len(re.findall(r"\]\(", line)), line)
        self.assertIn("[A &#91;x&#93; and y title](roadmap/a/b.md)", line)

    def test_linkscan_sees_one_link_only(self):
        import linkscan
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        (root / "roadmap" / "a").mkdir(parents=True)
        (root / "roadmap" / "a" / "b.md").write_text("x\n", encoding="utf-8")
        line = board.index_line("[ ]", "**Bad " + "]" + "(nowhere.md) [t]**",
                                "roadmap/a/b.md")
        (root / "ROADMAP.md").write_text(line + "\n", encoding="utf-8")
        self.assertEqual([], linkscan.scan_paths([root / "ROADMAP.md"], root))

    def test_the_legacy_projection_is_byte_identical(self):
        # The grace accepts a child's committed old-form index exactly; escaping
        # must not reach it.
        self.assertEqual(
            "- [ ] [Fix the [~] marker](roadmap/a/b.md)",
            board._index_entry_v1("- [ ] **Fix the [~] marker**\n",
                                  "roadmap/a/b.md"))


class IndexLineWidthOnRealOutput(unittest.TestCase):
    """160/220, BG3 — "the generated index passes `wrapscan` in any repo" was a
    claim about the CURRENT DATA, not the renderer: it was never tested on the
    generator's real output. These run the real `wrapscan` over a whole
    generated index built from items shaped to stress the renderer (flags, long
    claims, long titles, a wrapped title, a long slug), so a renderer change
    that breaks the promise fails here, where the scanner's own rule is read,
    not restated."""

    LONG_TITLE = ("**A title that runs on and on well past what a reader needs "
                  "in an index line, so it must be cut**")

    def build(self, files: dict[str, str]) -> str:
        td = tempfile.TemporaryDirectory()
        self.addCleanup(td.cleanup)
        root = Path(td.name)
        sec = make_board(root)
        for name, body in files.items():
            (sec / name).write_text(body, encoding="utf-8")
        board.run_check(root, fix=True)
        return (root / board.INDEX_REL).read_text(encoding="utf-8")

    def scan(self, text: str):
        import wrapscan
        return wrapscan.scan_text("ROADMAP.md", text)

    def test_a_board_of_stressing_items_passes_wrapscan(self):
        text = self.build({
            "20-" + "a-very-long-slug-" * 4 + "x.md":
                f"- [ ] 🎯🔥 {self.LONG_TITLE}\n",
            "30-claimed.md":
                f"- [~] 🔎 {self.LONG_TITLE}\n"
                "      (claimed 2026-11-03-0638, "
                "wt: atelier-qr-4c65-a-worktree-with-a-very-long-name)\n",
            "40-wrapped.md":
                "- [~] **A title that wraps\n      onto line two and keeps "
                "going for a good while longer** "
                "(claimed 2026-11-03-0638, wt: x)\n",
            "50-done.md": f"- [x] {self.LONG_TITLE}\n",
            "60-pointer.md": "- ⏳ Rule-4 review queued — delta abc..def\n",
            "70-reasoned.md":
                "- [ ] **Short** <!-- datescan:allow: verbatim date; "
                "wrapscan:allow: the marker pads the line --> body\n",
        })
        self.assertGreater(max(len(l) for l in text.splitlines()), 85,
                           "fixture must overrun the width, or it proves nothing")
        self.assertEqual([], self.scan(text), text)

    def test_a_sibling_marker_with_a_wrapscan_allow_travels_and_passes(self):
        text = self.build({
            "20-m.md": "- [ ] **Verbatim (15/7/26) title** <!-- datescan:allow:"
                       " verbatim; wrapscan:allow: marker pads --> body\n"})
        line = next(l for l in text.splitlines() if "20-m.md" in l)
        self.assertIn("wrapscan:allow: marker pads", line)
        self.assertEqual([], self.scan(line + "\n"), line)

    def test_STATED_RESIDUAL_a_sibling_only_marker_can_be_flagged(self):
        """The case the promise does NOT cover, pinned so the module docstring
        and `tools/README.md` stay true to it. `wrapscan` exempts marker padding
        only when the text before the marker fits in 85 columns, and an index
        line's path seldom lets it. If this starts passing, the renderer or
        `wrapscan` closed the gap: update both statements, then this test."""
        text = self.build({
            "20-" + "a-long-slug-" * 4 + "x.md":
                "- [ ] **Verbatim (15/7/26) title** "
                "<!-- datescan:allow: verbatim --> body\n"})
        line = next(l for l in text.splitlines() if "20-a-long-slug" in l)
        self.assertEqual(1, len(self.scan(line + "\n")), line)


class SelftestNeedsNoHomeDirectory(unittest.TestCase):
    """160/220, BG7 — the selftest asserted `str(Path.home()) not in text`, which
    matches EVERY index when HOME is `/` (a minimal container), so the CI
    selftest step failed on a machine with nothing wrong."""

    def test_selftest_passes_with_home_at_the_filesystem_root(self):
        import os
        with mock.patch.dict(os.environ, {"HOME": "/"}):
            self.assertEqual(Path.home(), Path("/"))
            self.assertEqual(
                0, board.selftest(), "selftest depends on the home directory")


class DefaultRootIsTheGitToplevel(unittest.TestCase):
    """160/220, BG8 — run from a subdirectory with no `--root`, the check looked
    for `docs/roadmap/` under the subdirectory, found none, and printed "not in
    scope" with exit 0: a silent pass for a check the floor enforces."""

    def setUp(self):
        if shutil.which("git") is None:
            self.skipTest("git not on PATH")
        import os
        self._td = tempfile.TemporaryDirectory()
        self.addCleanup(self._td.cleanup)
        self.root = Path(self._td.name).resolve()
        make_board(self.root)
        _git(self.root, "init", "-q")
        self.sub = self.root / "docs" / "method"
        self.sub.mkdir(parents=True)
        cwd = os.getcwd()
        self.addCleanup(os.chdir, cwd)
        os.chdir(self.sub)

    def run_main(self, *argv):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            rc = board.main(list(argv))
        return rc, out.getvalue() + err.getvalue()

    def test_a_subdirectory_run_finds_the_board(self):
        rc, out = self.run_main("--check")
        self.assertNotIn("not in scope", out)
        self.assertEqual(1, rc, out)           # no index yet: stale, not skipped
        self.assertIn("stale", out)

    def test_rebuild_from_a_subdirectory_writes_the_roots_index(self):
        rc, out = self.run_main("--rebuild")
        self.assertEqual(0, rc, out)
        self.assertTrue((self.root / board.INDEX_REL).is_file())
        self.assertFalse((self.sub / board.INDEX_REL).exists())

    def test_an_explicit_root_still_wins(self):
        with tempfile.TemporaryDirectory() as bare:
            rc, out = self.run_main("--check", "--root", bare)
        self.assertEqual(0, rc, out)
        self.assertIn("not in scope", out)

    def test_outside_a_repo_the_default_is_the_current_directory(self):
        import os
        with tempfile.TemporaryDirectory() as bare:
            os.chdir(bare)
            rc, out = self.run_main("--check")
        self.assertEqual(0, rc, out)
        self.assertIn("not in scope", out)


if __name__ == "__main__":
    unittest.main()
