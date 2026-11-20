- [x] **Capture the subagent `.meta.json` sidecar (Mike ruled 2026-07-28 — a new
  capture class, not covered by the 2026-07-23 metadata ruling).** Each
  `<uuid>/subagents/agent-<id>.jsonl` has a `.meta.json` beside it that ccarchive
  does **not** take: `captureClass()` is an allowlist of `.jsonl` at any depth,
  `tool-results/*`, `toolu_*` and `memory/*.md`, and a `.meta.json` matches none
  of them.
