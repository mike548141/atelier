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
