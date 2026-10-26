# Sibling to the paragraph-projection and grace cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-26 UTC by the Opus 5.5 brief-writer named in the brief's
provenance; it forms no finding and writes no severity. Fold this file in below the reconcile
and delete it at phase 2.

Holds: one intent-record pointer, three locations of the author's account and one of other
held-back framing, ten hypotheses and twelve re-run results.

## Intent record

- `docs/roadmap/010-board-store-migration-per-item-files-mik/170-the-index-projects-the-logical-first-paragraph-with-a-grace.md`
  — read in full by the brief-writer. Filed at `e1ce2a1` (2026-10-18 08:36 UTC), closed at
  `63720eb`. Lines 11–14 (to the end of the quoted answer) are the acceptance test. The
  principal's own words are only the two-word answer on line 14; the longer quote on lines
  11–13 is the queue run's recommendation that he answered.

## The author's account, by location

- Intent record lines 1–10: the author's statement of the problem and the planned fix, written
  at filing, before the build. Line 14 after the quote, through line 16: what the author took
  to be owed.
- Intent record lines 17–33: the author's closing account — the paragraph rule as built, which
  field reads what and why, counts of changed index lines by class, two classes that got worse
  (filed at `010/180`), how the grace works, that the 30-day span was the queue run's choice
  and not a ruling, one probe of the old index from `main` either side of the date, the
  CHANGELOG entry as the notice to children, and test counts at the time.
- `docs/roadmap/010-board-store-migration-per-item-files-mik/180-the-paragraph-projection-loses-two-small-signals.md`
  whole: the author's own residual list, filed in the pointer-landing commit, with shapes to
  weigh. The comments and docstrings in `tools/board.py` also carry the author's reasons, but
  they are the delta and were readable in phase 1.
- Not the author, but framing held back for the same reason: `320/730` lines 25–32 (a child
  session's remediation options and its review note), and line 10 of the same item, which
  calls the line-two claim reaching the index "as intended". The bodies of `28ef94a` and
  `63720eb` were not read by the brief-writer.

## Hypotheses (the brief-writer's suspicions, a floor not a fence)

1. **The end date is a UTC day.** `_today_utc()` reads the UTC date, so the old form is refused
   from 2026-11-18 00:00 UTC, which is 13:00 on 18 November in New Zealand daylight time. The
   CHANGELOG entry says "before 2026-11-18" with no timezone. Does a child reading it locally
   get the same day the code uses?
2. **Two planes, two versions.** A child's CI floats at `floor.yml@main` and runs the new
   projection; its commit hook runs its pinned copy. Before a pin bump, a rebuild with the
   pinned copy writes the old form, which CI accepts only until the end date. After it, does
   every child that has not bumped its pin red in CI on any commit that changes its board,
   with the hook still green? The child counts in the re-run results suggest how many
   children that touches.
3. **The pointer did not land in the landing commit.** The work landed at `28ef94a` and its
   pointer at `63720eb`, 59 seconds later. Rule 4 asks for the pointer in the commit that lands
   the work, or in the last commit of a series. Does a close-and-queue commit after the code
   commit meet that, or is it the gap the rule closes?
4. **This pass's own pointer is a live specimen of `010/180`'s third class.** Its claim was
   inserted on line two, inside the wrapped bold title. Its index line now shows a truncated
   title ending in "…" and about 180 columns of claim fragment before the link. Which part of
   the projection produces each, and is either the behaviour the delta meant?
5. **The block-start pattern stops too early on prose.** `_BLOCK_START_RE` matches `#` and `|`
   with no following space, so a wrapped line that begins `#122` or a pipe in prose ends the
   paragraph, which CommonMark would not. Does any real item lose title or claim text that way?
6. **The paragraph rule is narrower than the renderer's.** CommonMark keeps an unindented
   line in the paragraph (lazy continuation); the code stops at the first unindented line. Do
   any real items wrap with no indent?
7. **"One release" became 30 days.** The acceptance words ask for a one-release grace. This
   repo keeps everything under _Unreleased_ and children float at `main`, so there is no
   release to count. The code says the span was the orchestrator's choice. Is the mapping
   grounded anywhere, and did the principal see it?
8. **A flag wrapped onto line two is dropped.** Flags read the state line alone. A long title
   can push a real flag past the wrap. Is that loss measured, or only the opposite case (a
   glyph mentioned in prose)?
9. **The grace path with problems.** When the index matches the old form and the board also
   has problems, the grace prints its notice and returns 1. Is the stale-versus-problem message
   clear to a child, and do the problem lines print first?
10. **Mirror sites.** `docs/roadmap/README.md` describes state lines and what the index lifts.
    Does any README, template or skill still say the index reads the first line, or say where a
    claim goes when a title wraps?

## Re-run results held back from the brief

Run once by the brief-writer, 2026-10-26 UTC, from its worktree root at `6f78d85`, in the
foreground, on this machine:

1. `coldsweep --commit 28ef94a`: exit 0; four files; nothing left out as barred; closing line
   present.
2. `test_board.py`: 59 tests, OK, exit 0 (also with `-v`).
3. `board.py --selftest`: OK, exit 0.
4. `board.py --check` on both planes: exit 0, index current.
5. `wrapscan` over `tools/board.py` and `tools/test_board.py`: clean, exit 0.
6. `git log 28ef94a..HEAD`: nothing on `tools/board.py` or `tools/test_board.py`; two later
   commits on `CHANGELOG.md`, both for another tool's items.
7. Full Python suite under `nice`: 2032 tests, OK, exit 0, about 566 s. The intent record's
   count is from 2026-10-18; later commits added tests.
8. Floor, ci plane, under `nice`: exit 0. leakscan shows 🟡 (the ci plane does not pass
   `--require-terms`); four guards are warn-only by wiring.
9. Legacy byte-identity, on a copy of this repo's board: the pre-delta `board.py` (extracted
   from `28ef94a^`) and `_index_entry_v1` render identical indexes; the new and old forms
   differ on 300 lines today (the intent record counted 297 on 2026-10-18).
10. Boundary probe, worktree plane only, on a copy of this board with an old-form index:
    `today=2026-11-17` exit 0 with the notice; `today=2026-11-18` exit 1, stale; no date
    injected (run date 2026-10-26) exit 0 with the notice. The staged plane was exercised only
    by the delta's own unit test.
11. Child probe, read-only, check mode, worktree plane of each primary checkout (which may
    carry uncommitted edits), by count: 30 other repos in the machine's repo directory; 11
    with a split board; 5 current today and on the end date; 6 pass today only under the grace
    and red stale on 2026-11-18.
12. Claimed lines over the same 11 children, new projection: 55 claimed index lines; 1 whose
    text before the title link exceeds 100 columns, in 1 repo. Rough measure: it splits at the
    last ` [` before the link and ignores each child's own wrap width and exemptions.
