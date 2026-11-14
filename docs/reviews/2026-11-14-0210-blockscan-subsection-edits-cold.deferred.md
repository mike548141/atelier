# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0210-blockscan-subsection-edits-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `99821c6a`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

## The brief-writer's own questions

1. **One edit, two findings.** When a mapped section's own lines and one of its subsections both
   change with the bullet unmoved, the direct rule reports a `violation` and the new check a
   `subsection`. Before the date and with `--warn`, neither blocks; from the date the second blocks
   alone. Is the double report intended, and is it counted honestly? The same question for a heading
   mapped by two bullets: `_subsection_findings` runs once per bullet per source.
2. **The occurrence key.** Subsections are keyed `(heading text, nth under this parent)`. A new
   subsection inserted ahead of an existing one with the same text shifts every later index, and a
   renamed subsection reads as one removed and one added (two findings for one edit). For a removed
   subsection the printed line number is the old file's, shown against the new path. No mapped doc
   held a duplicate heading on 2026-11-14 (measured), so the duplicate case is latent (A2).
3. **The allow marker on a removal.** For a removed subsection the body text is empty, so the
   marker can sit only in a bullet. The README says the marker may sit "in the changed subsection";
   is that true for a removal?
4. **A parent that moves.** If a mapped heading changes level, or an unmapped heading between two
   mapped ones changes level, subsections can change their nearest mapped ancestor between the old
   and new sides. Does that report a change to every migrated subsection, under the wrong bullet?
5. **What "blocking" reaches.** The only wiring is CI's `--against HEAD^ --warn`. `HEAD^` is the
   tip's first parent, so a subsection edit in any commit of a push other than the last, or on the
   second-parent side of a merge, lands green after the date. And with no hook-plane wiring (the
   docstring's WIRING RESIDUAL), blocking means a red CI after the push, never a refused commit.
   Does that match his words *"move to blocking action"* (A4)?
6. **Whose order the date is.** The docstring says the check "was ordered blocking by the principal,
   on a date"; the same text, the README and the CHANGELOG say the date is the run's choice. His
   words order warn-then-block, staggered, and name no date. Is "ordered blocking … on a date" an
   attribution stronger than his words (V1)?
7. **Test count.** The commit body says 53 tests "(+19)"; the `320/810` slice note says "18 new,
   53 total". Measured by counting `def test_` in `tools/test_blockscan.py`: 35 at `6a4eeee2~1`,
   53 at `6a4eeee2`, 58 at the brief's base. So +18; the body's +19 looks off by one (V1).
8. **The CHANGELOG date.** The entry is headed 2026-11-10; the commit is 2026-11-10 02:34 +1300,
   which is 2026-11-09 13:34 UTC, the date the board records. `CONVENTIONS.md` keeps dates at rest
   in UTC. A local date in a record?
9. **The flip's own probe.** `320/810` says each flip needs a fresh fleet probe before its date.
   Nothing the brief-writer found surfaces that probe ahead of 2027-01-11 (no dated item or gate
   reads it). Is the warn period doing its job if nobody is told it is ending?
10. **The 124-commit replay.** No command is recorded for it, so "14 of 124, all real subsection
    edits" cannot be re-run as written. Which 124, and judged real by whom?

## What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC (base `2c1f0296`), foreground, load average about 4
to 5 on 12 cores.

- `git merge-base --is-ancestor 6a4eeee2 HEAD`: exit 0.
- `python3 tools/coldsweep.py --root . --commit 6a4eeee2 --path …` (the brief's four paths):
  exit 0, 607 non-blank lines; the subject and the four-file stat print first.
- `cd tools && python3 -m unittest test_blockscan`: 58 tests, OK, about 34 s.
- `python3 tools/blockscan.py --selftest`: `selftest OK`, exit 0.
- `python3 tools/blockscan.py --root . --check`: exit 0.
- `python3 tools/blockscan.py --root . --against HEAD^ --warn`: clean, coverage 7 files and 4,371
  lines, exit 0. With `--json`: `clean` true, `subsection` `{count 0, blocking false, until
  2027-01-11}`. The base commit touched no mapped doc, so this shows the wiring runs, not that the
  check fires.
- The brief's `coldsweep` sweep line: exit 0 (with a warning that the sibling path matched no file,
  because the sibling was not yet written).
- Duplicate heading text in each mapped doc, by a throwaway script over `tools/blockscan_map.json`:
  none in any of the six mapped docs.
- Not run: the 21-child probe and the 124-commit replay (no recorded commands; left to the pass).
