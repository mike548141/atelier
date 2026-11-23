- [ ] 🔎 **`archivecut` in the field: five rough edges from its first fleet
      run.** Filed 2026-11-20 by session 19378351 from the reports of the
      workers it ran in sixteen children (class only; every cut that ran
      proved byte for byte and landed with green CI). None lost data; each
      cost a worker a refused commit or left a warning behind.
      1. **A re-pointed link can push a line past the wrap limit**, so the
         first commit is refused by `wrapscan` (seen in four children; lines
         of 113 and 118 columns). The tool re-points paths but never re-wraps
         prose; it should report each lengthened line so the worker wraps it
         before committing, or wrap where the line is ordinary prose.
      2. **The session-index line it writes can be wider than the limit**,
         and `--verify` forbids wrapping or marking it, so a child that scans
         its session index has to exempt the whole file.
      3. **It looks for the archive in `docs/` only.** A child that kept its
         pre-split board at the repo root reads "nothing to do".
      4. **Archived items keep their old `⏳` marks**, and the new index
         counts an `[x]` line carrying `⏳` as review-queued (`010/210`'s
         rule), so a "Done before the split" row can show a non-zero review
         count for history. The archive section should count zero, or the
         rule should skip it.
      5. **`attribscan` warns on moved text** that says "Mike's ruling"
         without his words (it reads the move as new prose); it starts
         blocking 2027-02-08. Moved records should be read as records.
      **Owed:** fix 1–4 in the tool and `board.py`; decide 5 with `attribscan`'s
      record-path rule. Rides on the `160/1680` pass's delta when built.
      *Note 2026-11-20:* item 2 is moot since `010/270` retired the session
      index; the tool writes no index line now.
      *Note 2026-11-20, from the session-log retirement run (23 children):*
      item 2 came back in a new form. The label line the tool writes above
      each placed entry ("**From the retired session log**, word for word;
      …") is 101 columns, so `wrapscan` refused the first commit in about
      ten children. Each exempted its session folder in `.wrapscanignore`
      (atelier already exempts `docs/sessions/`), some the whole folder and
      some `docs/sessions/2*.md`. No proof was weakened, but the line should
      fit the limit for any repo cut later, and the exemptions now differ
      from child to child. Item 5 also recurred (one child: a copied title).
      ✅ **Items 1, 3, 4 and item 2's new form done 2026-11-23** (queue run
      c7a1e36e; a Sonnet worker, read by the run before landing). 1: the plan
      prints `WRAP n line(s)` with file, line and width for each line a
      re-point lengthens past the limit (not one already over, not in an
      exempt file); prose is never re-wrapped. 3: the board archive is found
      at the repo root when `docs/` has none; with both, `docs/` wins and the
      other is named and left. 4: in `board.py`, a `[x]` item in
      `990-done-before-the-split` is neither listed nor counted
      (`ARCHIVE_SECTION`); atelier's own row went to zero (the one case,
      `990/1170`, a review delivered 2026-07-22). 2: the label line is 76
      columns; the old wording is still read, so repos already cut still
      pass `--verify`. Tests in `tools/test_archivecut.py` and
      `tools/test_board.py`. Covered by `160/1680`, whose delta now includes
      this commit.
      **Still open:** the `archivecut:retired` comment the tool writes into
      `docs/sessions/README.md` is 92 columns, the same class as item 2;
      session-log sources at the repo root are not looked for (the item named
      only the board); and item 5, the `attribscan` record-path decision.
