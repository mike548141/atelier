- [x] **ccrepo context-size column — DELIVERED 2026-07-26** (`c94f75e`, inline
  Opus; `ccrepo.design.md` § "Context size"). Mike asked for a reading of when
  window sizes get large and named the three candidate shapes himself (sum /
  average / max). **The answer was measured before it was chosen** — a throwaway
  probe over the live logs (419 sessions, 107,902 assistant messages) killed two
  of the three: **sum is meaningless** (every message carries the whole cached
  prefix, so it counts one window repeatedly — context is the only metric that
  must never go through `addTo`), **mean is skewed** by exactly the outliers the
  column exists to catch. Shipped as **one column, two numbers** (`110k/578k` —
  median beside max), which also answers the column-count concern. One repo
  settled it: median 108k, max 578k — scariest on the board by max, calmest by
  median. Grain is the **per-session peak**, not per-message (message-grain
  understates: 122k vs 168k across the set), matching what `cctranscript` already
  headlines. **A `% of window` column was designed and abandoned as unbuildable**
  — the logs carry no `[1m]` marker, so 200k and 1M variants are
  indistinguishable; the 934k observed peak proves 1M sessions exist but not
  which. Recorded so it isn't re-derived. `--json`/`--csv` deliberately go
  **wider than the table** (Mike's follow-on: a data file isn't width-bound) —
  full distribution incl. `p90`, plus the covered/uncovered split behind
  `Actual`; grand total in `meta.total` because peaks can't be re-aggregated from
  leaves. **`ROLLUP_SCHEMA` → /2 was load-bearing, not housekeeping:** the
  `(mtime,size)` fingerprint only proves the *source* unchanged, so v1-cached
  events lacking the new field would have reported a confident **zero** context
  on every warm archive run forever — caught at design time, with a test that
  rewinds a ledger and proves it's re-read. 180/180 tests, floor 9/9.
