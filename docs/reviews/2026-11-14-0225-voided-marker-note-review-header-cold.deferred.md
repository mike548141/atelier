# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0225-voided-marker-note-review-header-cold.md` (`REVIEW.md`
rule 1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `64377cac`),
which authored none of the delta. Open this only after act 1 is committed. Everything here is a
floor, never a fence, and none of it is a finding: the brief-writer read the code once and probed
none of these past what the brief's re-run list records.

## What the barred intent records say, in brief

- `110/010` carries the author's landing note (2026-11-09, queue run `d0ca5d24`): the note covers
  15 reader call sites with no scanner file changed; an old-against-new probe of `leakscan` and
  `secretscan` in each of 30 local repositories, one at a time under `nice`, found exit code and
  stdout length identical everywhere. After a tightening (the word must end at a colon, a space or
  the line's end) the note fired in 2 repos: twice per scanner in atelier's own tooling source and
  once in one child's `secretscan` run, every one a mention, none a genuinely voided marker. Its
  conclusion: the estate held no voided marker of that shape on that date. It states the same
  limits the brief extracts (stderr, not the finding line; fires on any line a reader is asked
  about; a prose mention outside a code span is noted, the residual `160/480` AM3 names).
- `320/440` carries the author's landing note: proposal items 1 and 2 built warn-only, 3 and 4 not
  built by design; the same 30-repo probe found exit code and stdout length identical (no review
  file was dated on or after the boundary then). With the boundary pushed back for a count only,
  736 of 738 review files across 17 repos had no `board:` line and 480 had no dated `Status:` line.
  The item stays open on purpose for blocking, which "needs its own date and a fleet probe at that
  date"; if the warning is not read or catches nothing by then, it closes as warn-only.
- Earlier on `320/440`, the child's own measurement of the drift ("one in five") was corrected by
  the filer the same day to **unmeasured**; the class survived the correction.

## The brief-writer's own questions

1. **A scoped marker read by an unscoped pattern.** `conflictscan` and `wrapscan` build their
   pattern with no scope. A line carrying `conflictscan:allow:<kind>: <reason>` allows nothing
   there and is noted, correctly. But is there any scanner that reads the same line with two
   patterns for one word (scoped and unscoped), so that the one that does not match notes a line
   the other honoured?
2. **The note in CI.** The note goes to stderr. Does `tools/floor.py` (and the pre-commit hook)
   pass a scanner's stderr through, or keep only its exit code and stdout? If stderr is dropped,
   the note is invisible exactly where `110/010` said the reader already is.
3. **Today's briefs are the first in scope.** Every brief named for 2026-11-10 or later is under
   check 3. On 2026-11-14 at `d3293d93` the scanner printed no `⚠` stanza over this repo, so every
   such brief carried both lines. Is that the check working, or the template doing the work and
   the check untested on real misses?
4. **Any `.md` passes `Board:`.** `_BOARD_PATH` is `\S\.md\b`, so `**Board:** see README.md`
   passes, as does a path to an item file that does not exist. The docstring says "naming its item
   file". Is existence worth checking, given the proposal's aim is a pointer a reader can follow?
5. **The boundary is a filename.** A brief-writer or reviewer that names a file for the day the
   work was done rather than the day it was written produces a backdated name in good faith. How
   common is that shape in the house's own naming rule (HHMM from `date -u`), and does anything
   catch it?
