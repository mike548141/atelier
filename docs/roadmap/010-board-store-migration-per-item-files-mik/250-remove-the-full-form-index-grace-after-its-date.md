- [ ] **Remove the full-form index grace once 2026-12-04 has passed.**
      Filed 2026-11-20 with `010/210`, which changed the generated index to a
      summary table and the unfinished items only. Children run `board.py`
      from atelier `main` against their own committed index, so `--check`
      accepts the previous full form (every item listed) until
      `FULL_FORM_ACCEPTED_UNTIL = 2026-12-04`, the first day it is refused,
      and prints ⚠️ with the rebuild command meanwhile. The 14-day span was
      the building run's pick, not a ruling. After the date the grace is dead
      code that a reader must still reason about.
      **Owed, in order:**
      1. Before the date, run `board --check` (both planes, read-only) in
         every child checkout that has `docs/roadmap/`, and list which still
         hold the full form. On 2026-11-20 all twenty passed under the grace
         and none was yet rebuilt. A child whose index is still full on the
         date goes red at its next commit or CI run; that list goes to the
         principal before the cut-off, so the reds are expected.
      2. Remove everything the `LEGACY` comment in `tools/board.py` lists
         (the comment is the full list, as `010/190` learned): the block, the
         `today` parameter and grace branch of `run_check`, the `full`
         parameter of `build_index` and its two branches, the date imports,
         `test_board.py`'s `FullFormGrace` class, and the grace sentences in
         `tools/README.md` and `docs/roadmap/README.md`.
