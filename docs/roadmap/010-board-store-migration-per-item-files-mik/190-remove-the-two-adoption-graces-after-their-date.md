- [x] **Remove the two adoption graces once 2026-11-18 has passed.**
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
      📎 **Added 2026-11-09 UTC:** land `010/180`'s held `board.py` fix (branch
      `hold-010-180-index-title`) in the same step, since it also needs every
      child's index rebuilt.
      ✅ **Done 2026-11-12 UTC:** `010/180` landed on its own, with the six
      children's indexes rebuilt the same hour; it no longer waits on this item.
      Probe the same day: with the clock at 2026-11-18, every child passes the
      board check, so removing the board grace reds none.
      🔒 CLAIMED 2026-11-20T07:40Z (claimed 2026-11-20-0740, wt: atelier-qr-08cd-graces) by queue-run
      session 08cd3b95 (Opus 5.5, principal-opened). Scope: both graces removed, children probed first.
      ✅ **Done 2026-11-20 UTC (queue run 08cd, worker):** both graces removed
      by the `LEGACY` comment's full list. `tools/board.py`: the LEGACY block,
      `LEGACY_INDEX_ACCEPTED_UNTIL`, `today`, `_today_utc`, `_run_check`'s
      tuple (it returns the exit code; `main` prints `board advisory: 0`),
      `_entry`, `escape`, `legacy` and the `date`/`datetime`/`timezone`/
      `Callable` imports. `_EDGE_LEAD_RE` and `_EDGE_TRAIL_RE` STAY: the
      comment's list names them, but the current strip reads them. In
      `tools/leakscan.py`: `BINARY_GRACE_UNTIL`, `in_binary_grace`,
      `render_grace`, the `grace` argument of `render_human`, the
      `binary_grace` key in `--json` and the summary's G3 field. Tests: the
      `LegacyGrace` class, the byte-identity, staged-plane and advisory-one
      tests, `test_floor.py`'s `_graced_board_repo` helper and its grace test,
      and `BinaryGrace` (now `BinaryGate`: the post-date blocking tests kept).
      Docs updated: `tools/README.md`, `docs/method/SECRETS.md`, comments that
      cited `BINARY_GRACE_UNTIL`; records untouched.
      Probe before removing (read-only, counts only): 17 children with a
      board, 0 red on `board --check`; 29 sibling repos leak-scanned, 2 red
      on the binary rules (33 findings, the same before and after). The
      per-repo list is in the run's scratch only.
