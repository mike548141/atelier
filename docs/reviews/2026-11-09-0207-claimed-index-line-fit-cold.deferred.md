# Sibling to the claimed-index-line-fit cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-claimed-index-line-fit-cold.md`, held under
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
- `python3 tools/wrapscan.py --root . docs/ROADMAP.md`: exit 0 (suppressed: 4 by allow-marker · 0
  file(s) by .wrapscanignore · 0 ove).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-26-0941-paragraph-projection-grace-cold.md`
- `docs/reviews/2026-10-28-1255-paragraph-projection-grace-topup-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `_claim_for_index` matches only `(claimed <date>[-HHMM], wt: <name>)`. A claim of any other shape
   returns whole. How many real claim shapes on this board and in the children fall outside it? This
   repo's own 2026-11-09 claims read `wt: under ~/worktrees/briefs, brief only, session …` and were
   cut to `bri…` in the index: is what is left of "who has it" still true?
2. `_fit_title` runs on every line, claimed or not. Is "a no-op for an unclaimed line" true for a
   long prefix (a `DONE` state, or an icon run)?
3. `WRAP_COLS` restates wrapscan's `LINE_LIMIT` by hand. Does a test pin the two (V4)? `pathscan`
   keeps a test for its copy of stampscan's regexes; this delta may not have one.
4. The widths use `len()`, in code points. Does wrapscan count the same way for the icons the state
   line carries?
5. `TITLE_MAX` cuts before the brackets are escaped, and `&#91;` is five columns. Can escaping push
   a line past the limit `_fit_title` thought it had met, and can `_fit_title` cut inside a
   reference?
6. A literal `&#91;` already in a title: does it survive, and does a round trip through `linkscan`,
   `board --check` and a child's pinned older `board.py` agree on the bytes?
7. The hand-up says the line still exceeds 85 and passes only by wrapscan's single-token exemption.
   Is a child that scopes wrapscan over its index actually green at HEAD?

## Facts held back from the brief

- The intent record `320/730` states, in its landing account, what the delta does not reach. The
  brief does not pass that on.
