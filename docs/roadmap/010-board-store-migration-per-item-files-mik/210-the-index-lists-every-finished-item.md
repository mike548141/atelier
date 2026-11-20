- [x] **The index lists every finished item, so finished work is read at
      every session start.** Filed 2026-11-20 by session 19378351. The
      generated `ROADMAP.md` carries one line per item whatever its state,
      and nothing in `tools/board.py` collapses a finished section. Measured
      here the same day: 814 lines, 46 sections, 17 of them with no open
      item; a dropped-done index would be about 400 lines, and the five
      largest boards in the estate fall by a quarter to five-sixths each.
      **Agreed** (Mike, 2026-11-20, to "Should finished themes drop out of
      what sessions read?"): *"yes I agree"*. That approves the collapse of
      an all-done section to one line; item files stay untouched.
      **🎯 Shape still being discussed** (his words, same message):
      *"I am considering if ROADMAP.md should be a synopsis and state of only
      the themes of work (the folders basically). And then in each folder the
      README.md or some other dedciated file that runs the board for that
      theme of work, in the same way ROADMAP.md runs the baord for each theme.
      The detail still sits in individual work item files"*. The weighing put
      to him: about ten tools across the estate read the index's state lines
      (`pointerscan`, `harvestscan`, `coldsweep`, `cclive`, `ccclose`, a
      review-queue reader and others), and sections are uneven (one board
      holds 290 open items in six sections), so a sections-only index does
      not bound what a session reads there. Build waits for his pick.
      **Shape picked 2026-11-20** (Mike's pick from offered options, an
      answer, not a ruling in his words): *"Summary + open only
      (Recommended)"*: a table of sections at the top (open, claimed,
      waiting on him, review-queued counts per section), then only the
      unfinished items; an all-done section takes one line. The sections-only
      index he floated is not taken now. **Owed:** the generator, its tests,
      the legend in `roadmap/README.md` and RECORD.md § *The roadmap*, and a
      rollout that does not turn every child's `board` check red the day the
      generator changes (children run atelier's tools from `main`).
      ✅ **DONE 2026-11-20 UTC** (a worker of an orchestrated run, Opus 5.5).
      `tools/board.py` writes the picked shape: a summary table, one row per
      section, counting open `[ ]`, claimed `[~]`, `🎯` and `⏳` items (the
      two glyphs read off the state line, code spans excluded), with a
      total row; then only the unfinished items under each section that has
      any. Unfinished is a marker other than `[x]`, or a `⏳` on the state
      line, so the review-queue count stays the count of `⏳` state lines. A
      section with nothing owed keeps its table row alone, marked `✅`; it
      gets no "finished sections" list, since that would give it two lines.
      Item files are untouched. This board's index went from 816 lines to
      470: 17 of 46 sections collapse to their row. **Grace:** `--check`
      accepts the previous full form of the same board until 2026-12-04 (the
      first day it is refused), prints ⚠️ with the date and the rebuild
      command, and passes; `--rebuild` writes the new form. Probed read-only
      the same day: all twenty children with a split board pass on both
      planes under the grace, and the five largest fail on the end date, as
      they should. Small boards grow by about a dozen lines (the table and
      its three lines of prose); the largest shrink by up to three-quarters.
      Readers of the index checked: `cclive`, `ccclose` and the estate's
      review-queue reader read item files, not index lines; `pointerscan`
      skips the generated file; `sizescan` sees no `[x]`; `harvestscan`
      (warn-only) matches no `- ✅` line as an item. Removal of the grace is
      `010/250`; cold pass queued at `160/1670`. Legend in
      `roadmap/README.md`, RECORD.md § *The roadmap* and `tools/README.md`
      updated; `test_board.py` gained the summary and grace classes.
