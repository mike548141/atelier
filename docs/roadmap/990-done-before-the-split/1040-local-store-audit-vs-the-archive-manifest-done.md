- [x] **Local-store audit vs the archive manifest — DONE 2026-07-17.**
      `ccarchive --audit` hashes every live `.jsonl` and buckets it against the
      manifest: **synced** · **grown** (archived bytes a strict prefix — a plain
      append, kept out of the drift signal so an active session isn't a false
      alarm) · **mutated** (rewritten/truncated) · **renamed** (content matched
      an archived path now gone from live) · **new** · **pruned**. Only mutated +
      renamed are drift (listed, non-zero exit); the rest are counted. Read-only
      over both trees (no write path ⇒ no git-worktree guard). Pure core
      (`auditCategorize` + `classifyDivergence`) unit-tested; +11 tests (35→46
      ccarchive, 86 instrument), man AUDIT section (mandoc clean), README +
      `--help`. Driven live: 435 archived · 432 synced · 3 grown · 19 new · 0
      drift → exit 0.
