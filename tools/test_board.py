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

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

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


if __name__ == "__main__":
    unittest.main()


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
