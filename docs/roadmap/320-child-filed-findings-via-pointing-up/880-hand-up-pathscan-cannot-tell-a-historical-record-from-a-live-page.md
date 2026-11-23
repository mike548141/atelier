- [~] 🔎 **Hand-up: `pathscan` cannot tell a historical record from a live
      page, so a path that was true when it was written reads as stale, and
      the records it already excludes miss the per-item board store** <!-- wrapscan:allow: a state line carries the whole state in one line so the index reads true -->
      `[M][tools]`. Handed up 2026-11-20 UTC by a private child's session,
      under `PROPAGATION.md` § *Pointing up*, class only.

      **The principal's words, 2026-11-20, verbatim** (answering how the
      child should treat stale paths in its old records):
      > *"If its a path in a historical record (like work that was completed
      > sometime ago. Then it should keep the current path as it stands today
      > because that is a historical record, its not supposed to remain true
      > and I want you to file an issue with atelier that pathscan should
      > understand that. If the path is not a historical record but a part of
      > some content that should be pointing to the current real file then it
      > should be updated"*

      ## Evidence, measured in the child 2026-11-20

      `pathscan --warn` over the child's `docs/`: 1,154 findings. Read by
      where each sits and checked against git history:
      - **About 1,080 are in records the default exclusion does not cover.**
        `RECORDS_GLOBS` names `docs/sessions`, `docs/reviews`,
        `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md` and `CHANGELOG.md`. It
        does not cover: **closed items in the per-item board store** (about
        800 findings; the split store moved done items out of
        `ROADMAP-DONE.md` and into `docs/roadmap/<section>/<item>.md` with a
        `[x]` line, so they are scanned as live); a dated research-notes
        folder (about 200); and the dated rows of a decision register that
        also holds live sections in the same file (about 80).
      - **The records were right when written.** For 813 of them, the path
        existed at the commit that last wrote the line, and git records the
        file moving since (799 by recorded rename, most in one folder
        reorganisation). The finding is "the tree moved after this record",
        which the principal rules is not a defect in a record.
      - **About 70 sat on live pages.** After a proof (the path existed at
        the line's blame commit, and git records the move to a file present
        at `HEAD`), 19 were corrected. Most of the rest name a file in
        another repository, a removed file the text describes as removed, or
        a scratch folder: correct as written. The cross-repo shape is
        already a known class (`320/170`, `320/010`).

      ## What would make the scanner understand it (potential, untested here)

      1. **A closed board item is a record.** The board store already
         knows: a `[x]` checkbox line. Exclude, or scan advisory apart, any
         item file whose state line is done, the same contract
         `RECORDS_GLOBS` gives `ROADMAP-DONE.md`.
      2. **Let a child declare its record folders**, the way
         `.atelier-floor.json` already declares resolution roots (with a
         `why`), so a dated research or handoff folder can be named.
      3. **Mixed files:** a marker that opens a records region (for a
         register whose dated rows sit below live sections), like the
         stamped floor region skip.
      4. **A time axis, which the docstring says the scanner lacks.** git
         has one: blame the line; if the path existed at that commit, report
         it as "true when written" in a separate, non-red tally, and say
         where it went if a recorded rename leads to `HEAD`. The child built
         this as a throwaway check; it took about two minutes over 1,190
         findings, so cost is the question to measure.

      **Owed:** a ruling on which of these, then the build and its cold
      pass. Until then a child's records keep their paths as written and the
      warn-only count stays high.

      **Added 2026-11-20 by session 19378351** (the board-doctrine session,
      on a peer's forwarded finding). The closed-item share needs no folder
      rule and no move: a board item's state is its first line, so
      `pathscan` can treat an item whose state line is `[x]` as a record, the
      same as `RECORDS_GLOBS`, and keep scanning open items. In the reporting
      child that is about 800 of the 1,154 findings. A done/ folder on close
      was put to the principal by that child's session and is ruled out by
      his words to this session the same day: *"I never said the file gets
      moved, my intention is the file stays as you described and it builds
      up git history as its edited etc."* The pre-split archive section
      (`990-done-before-the-split/`, `010/220`) is already in
      `RECORDS_GLOBS`. The remaining classes above (dated research notes, a
      mixed decision register) still need their own answer.
      *(claimed 2026-11-23 UTC, session 608d8123, wt: atelier-qr-608d-pathrec; part 1 only)*
