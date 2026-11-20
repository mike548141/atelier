- [ ] 🔎 **`docs/method/RECORD.md` still names `ROADMAP-DONE.md` as the
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
