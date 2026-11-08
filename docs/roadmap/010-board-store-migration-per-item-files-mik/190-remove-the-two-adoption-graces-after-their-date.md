- [ ] **Remove the two adoption graces once 2026-11-18 has passed.**
      Two grace periods were landed on 2026-10-18, both on Mike's answers
      that day, and both end on 2026-11-18. In `tools/board.py` it is the
      LEGACY block (`LEGACY_INDEX_ACCEPTED_UNTIL`, `_item_state_v1`,
      `_index_entry_v1`, `_legacy_accepted`) and its one branch in
      `run_check` (`010/170`). In `tools/leakscan.py` it is
      `BINARY_GRACE_UNTIL` and its warn-only path (`020/150`). After the
      date both are dead code that a reader must still reason about.
      Before removing them, check which children have not yet rebuilt their
      index or listed their binaries (`atelier:fleet-pins` and each child's
      latest floor run). That list goes to Mike, so the cut-off reds are
      expected, not a surprise.
      🔎 **Added 2026-11-09 from the cold pass of `010/170` (`160/970`):**
      - **The removal list in the code was short.** Following it verbatim left
        `today`, `_today_utc`, the `_entry` seam, the `escape` parameter and
        the `date` / `Callable` imports behind, and `test_board.py` failed to
        import (the `LegacyGrace` class reads the constant). The full list is
        now the `LEGACY` comment in `tools/board.py`; use that, not the line
        above. The new `board advisory:` count line stays when the grace goes.
      - **The "which children have not rebuilt" list comes from `board` on
        each checkout, not from CI (PQ1).** Run `board --check` (both planes)
        in each child's checkout. A child with no running CI is the one a
        fleet-pins or latest-floor-run list would miss: its CI never showed
        the notice, and on 2026-11-18 its hook reds from a plane that never
        warned it.
      - **Put "one release" to the principal before the cut-off (PP11).** His
        words were "a one-release grace period"; this repo tags no release, and
        the 2026-11-18 end (UTC, 31 days) was the queue run's reading, which
        reached him in the closing account. Raise it with the child counts at
        the "list goes to Mike" step, as a briefing question.
