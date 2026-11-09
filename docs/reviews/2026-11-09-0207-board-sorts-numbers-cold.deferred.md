# Sibling to the board-sorts-numbers cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-board-sorts-numbers-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_board.py`: exit 0 (Ran 87 tests).
- `python3 tools/board.py --selftest`: exit 0 (selftest OK — board).
- `python3 tools/board.py --check`: exit 0 (board advisory: 0 finding(s) — reported, not blocking.).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

None found in the sweep.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The docstring's "no existing index changes order" is a statement about the day it was written.
   Section 160 now holds four-digit items. Is the sentence still true, and should it be there?
2. `number_collisions` and the sort: `010-x` and `10-x` are the same number under `int()`. Which
   wins, is it deterministic, and do both planes agree?
3. Who else orders board names as text and now disagrees with the index: `harvestscan`,
   `pointerscan`, `ccclose`'s board ids (`210/370` fixed one), `ROADMAP-DONE`, the plugin's queue
   listing, any child tool?
4. A leading number with a non-ASCII digit (`\d` in `str` patterns matches them), or a very long
   number: does `int()` raise or order them oddly, and does a crash here read as a broken scan?
5. Does a child pinned to an older `board.py` go red on the next rebuild once it holds a four-digit
   item?

## Facts held back from the brief

None.
