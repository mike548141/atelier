- [x] **DONE 2026-10-18** (wt: atelier-qr-010-170)
      **Project an item's logical first paragraph into the index, with a
      grace period for children** — part 1 of `320/450`, split out to build.
      `board.py` reads only an item's first physical line, so a title or
      `(claimed …)` fragment wrapped onto line two never reaches the index.
      A queue run's own claims hit it on 2026-10-18. The fix joins the
      indented continuation lines of the first paragraph before `TITLE_RE`
      and `CLAIM_RE` run. But `board` blocks in every child's CI from
      `floor.yml@main` and has no advisory form, so a changed projection
      would make each child's committed `ROADMAP.md` read stale at its next
      run. The queue run recommended: *"build it with a one-release grace
      period, where the check accepts both the old and the new index, and
      tell the children"*. Mike, 2026-10-18, answering that recommendation:
      *"I agree"*. Owed: the new projection; `--check` accepting the old
      one until a stated end, saying so when it does; a test for each; and
      the notice children read at their pin bump.
      ✅ **Built 2026-10-18, `28ef94a`.** The index now reads an item's
      logical first paragraph: the state line plus indented continuations,
      stopping at a blank line or a line that opens a new block. Titles and
      claims read the paragraph. Flags read line one only, because 45 items
      carry a flag glyph only in their prose. Allow-markers travel only from
      the lines the title and claim came from. Of the 297 changed index
      lines: 274 truncated titles are now whole, 8 silent cut-offs now end
      in "…", 2 junk fallbacks were replaced, and claims wrapped to line two
      now show. 🚩 Two classes got worse, filed at `010/180`. **Grace:**
      `--check` also accepts an index matching the old renderer, kept
      verbatim in a marked LEGACY block, and prints ⚠️ with the rebuild
      command and the date. `LEGACY_INDEX_ACCEPTED_UNTIL = 2026-11-18` is
      the first day the old form is refused. The 30-day span was the queue
      run's choice, not a ruling. Probed: the old index from `main` passes
      with the notice, and fails on the end date. The CHANGELOG entry is the
      notice children read at their pin bump. 59 board tests, 1963 Python
      tests green. Cold pass queued at `160/970`.
