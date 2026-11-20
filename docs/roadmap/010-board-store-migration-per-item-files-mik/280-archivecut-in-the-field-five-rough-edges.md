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
