- [x] **Migrate the board to per-item files + generate the index** — ADR, item
      format, `tools/board.py` (index generator + validator + tests), migration
      of all open items, scanner-compatibility pass, hook wiring, doctrine
      updates (RECORD/CONCURRENCY/CLAUDE read order). Review queued at landing
      per REVIEW rule 4. (claimed 2026-08-15-0610, wt: board-per-item-0815)
      **Done 2026-08-15** (`8ce1bb7` toolchain · `a9abc26` migration ·
      `15d3de2` doctrine): 4,063 lines to 27 sections / 118 item files, index
      generated at 253 lines, `board` enforced on both floor planes,
      harvestscan/pointerscan adapted with tests (suite +20), linkscan and
      harvestscan clean across the move. Follow-ups queued as their own items
      in this section; the review pointer is `050-…` beside this file.
