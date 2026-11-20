- [x] **ccrepo rollup precompute ledger — DELIVERED 2026-07-23** (`8a31b95`,
  0441 run, Opus worker; `ccrepo.design.md` §8). Machine-local ledger at
  `~/.claude/ccrepo-rollup.json` (mirrors the pricing/billing config convention;
  `CCREPO_ROLLUP` override), so a warm `--from-archive` run reads the ledger
  instead of re-gunzipping every file. **Live smoke: 3.1× faster warm, numbers
  byte-identical cold vs warm** (the rollup==recompute floor, proven in a fixture
  test AND on the real archive; invalidation tested; ccrepo 48/48, instruments
  167/167). **One endorsed design deviation:** keyed **per-file, not per-period**
  — a month can't be fingerprinted without first reading files for message
  timestamps (chicken-and-egg; file mtime ≠ message timestamp), so period-keying
  would misfile boundary-straddling sessions and break the floor. Per-file
  `(mtime,size)` is provably exact. Known tradeoff: ~46 MB ledger; compaction is
  a safe future optimisation. No review gate (design §9 self-verification).
