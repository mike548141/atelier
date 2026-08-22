- [ ] **`pins.py` enumerates CWD-relative and reports a wrong denominator
      from a worktree, silently** (PU-5, ruled to the board 2026-08-22) —
      run from `/Users/mike/worktrees/<wt>`, it printed "1 of 1 not
      current" (`wt-cite`), having enumerated the worktrees directory
      instead of the fleet, with no hint the denominator was wrong.
      `floorfleet.py` run from the same directory found the fleet
      correctly, so the two instruments disagree on discovery and the
      quieter one is the liar. Bit a live review pass 2026-08-22
      (the pointing-up cold pass's claim-4 grounding, which item
      `310/030` tells readers to re-derive "from the pins list"). Fix
      shape: discover from the repo the tool ships in (or its configured
      root), never from the caller's CWD — and when discovery finds
      nothing that looks like a fleet, say so instead of reporting the
      denominator it found.
