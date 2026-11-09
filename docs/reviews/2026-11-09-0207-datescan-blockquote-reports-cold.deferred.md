# Sibling to the datescan-blockquote-reports cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-datescan-blockquote-reports-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_datescan.py`: exit 0 (Ran 96 tests).
- `python3 tools/datescan.py --selftest`: exit 0 (selftest OK — datescan).
- `cd tools && python3 -m unittest test_floor`: 187 tests, OK, exit 0 (Python 3.14.6).
- `python3 tools/datescan.py --root . docs --json`: exit 0 (}).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md`
- `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. A line both blockquoted and something else that blocks: can a `>` line have been blocking before,
   for instance a lazy continuation, a `>` inside a list, or a `>` after a fence closes? Design note
   § 5 says no.
2. Design note § 6 says a fence inside a blockquote now reports. Does a quoted code sample's content
   land on the board as the repo's own dating, and how often in the fleet?
3. `--warn` softens the whole check and "already prints every finding": does a `--warn` run
   double-print, and does `advisory_count` read the right line in that form?
4. `BlockingSetPinned`: seventeen terms, four cues, four shapes. Is that the whole blocking set, or
   a sample that a change outside it would pass?
5. The hook plane reports only added lines. Does a blockquote edit that reflows a line count as
   added?
6. The sampling in § 3 is 40 hits from one repository of 30. Is "about 95% correct prose" stronger
   than that?
7. Does the authority reach datescan's case? The answers were about leakscan first; the "carry on"
   label is a short pick. Read the full question text at phase 2.

## Facts held back from the brief

- `tools/test_floor.py` and `tools/test_precommit.py` fail to import on the system Python 3.9.6
  here: a module-level `str | None` annotation with no `from __future__ import annotations`. They
  pass on 3.14.
- At this HEAD datescan reports 0 advisory findings on this repo's `docs/`, so the tier has no live
  hit here to re-drive.
