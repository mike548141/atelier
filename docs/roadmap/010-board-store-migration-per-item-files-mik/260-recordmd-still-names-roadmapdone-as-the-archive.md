- [x] 🔎 **`docs/method/RECORD.md` still names `ROADMAP-DONE.md` as the
      board's archive, four places, after `010/220` cut it into the store.**
      Found 2026-11-20 by the worker that built `010/240`, which reports it and
      does not patch it (atelier's own rule: a defect quietly patched leaves no
      trace). Lines 60, 424, 451 and 458 read as if the file still exists and a
      done item is moved to it; § *The roadmap* says pre-split detail "stays
      frozen in `ROADMAP-DONE.md`", and the sizescan sentence says a done item
      "belongs in `ROADMAP-DONE.md`". Since `010/220` the detail is the section
      `docs/roadmap/990-done-before-the-split/`, and a done item stays in its own
      file. **Owed:** reword the four places to the store form, then check
      `docs/method/` for the same phrase (`040`'s sweep class). Doctrine edit, so
      it takes the rule-4 route.
      **DONE 2026-11-20** (session 19378351): the four places reworded to the
      store form; no other `docs/method/` file outside the census snapshots
      names the archive. 🚩 Left as it stands: the session-index *rotation*
      rule still names a `SESSIONS-ARCHIVE.md` growth store as where old index
      lines go, while the principal's 2026-11-20 pick cuts existing session
      archives into `docs/sessions/`. They are different things (index lines,
      not detail), but a later rotation would recreate the file the cut
      removed; that question is filed as `010/270`. Rule-4 pass rides on
      `160/1680` (the archivecut cycle), whose delta this joins.
