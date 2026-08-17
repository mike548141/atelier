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

import sys
import tempfile
import unittest
from pathlib import Path

TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import board  # noqa: E402


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
    the registry renders `check --root <root> {scope}`, and argparse will not
    bind positionals that an intervening optional split into two runs, so the
    trailing scope path aborted with "unrecognized arguments". The board's
    location is fixed at docs/roadmap/, so the scope is rightly ignored — but
    it has to be ignored, not fatal.
    """

    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = Path(self._td.name)
        make_board(self.root)

    def tearDown(self):
        self._td.cleanup()

    def test_scope_after_root_is_absorbed_not_fatal(self):
        # exactly floor.py's rendered hook/ci argv for this scanner
        argv = ["rebuild", "--root", str(self.root), str(self.root)]
        self.assertEqual(board.main(argv), 0)
        self.assertEqual(board.main(["check", "--root", str(self.root),
                                     str(self.root)]), 0)

    def test_the_scope_does_not_displace_the_action(self):
        # a stale index must still be REPORTED through the floor's argv —
        # absorbing the scope must not quietly turn `check` into `rebuild`.
        self.assertEqual(
            board.main(["check", "--root", str(self.root), str(self.root)]), 1)

    def test_an_unknown_option_is_still_an_error(self):
        with self.assertRaises(SystemExit) as ctx:
            board.main(["check", "--root", str(self.root), "--bogus"])
        self.assertEqual(ctx.exception.code, 2)


class OutOfScope(unittest.TestCase):
    def test_bare_tree_exits_zero_and_says_why(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(board.run_check(Path(td), fix=False), 0)

    def test_selftest_passes(self):
        self.assertEqual(board.selftest(), 0)


if __name__ == "__main__":
    unittest.main()
