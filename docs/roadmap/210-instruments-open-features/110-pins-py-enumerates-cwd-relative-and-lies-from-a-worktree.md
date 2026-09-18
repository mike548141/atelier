- [x] **`pins.py` enumerates CWD-relative and reports a wrong denominator
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

      ✅ **FIXED 2026-09-18** (`8f1b5ca`, merged from `pins-cwd-0918`):
      `resolve_atelier()` now resolves to the MAIN checkout via
      `git rev-parse --git-common-dir` (a twin of `floorfleet.main_checkout`,
      not an import — floorfleet imports pins, so importing back would cycle),
      and every run names the search root and its funnel (entries → git repos
      → pinned children) instead of guessing at an "implausible" threshold.
      Verified live from inside a worktree: resolves to the primary checkout
      and reports the real fleet. `signfleet.py` shared the bug through the
      same calls and is fixed with it. Test builds a real `git worktree add`
      layout.
