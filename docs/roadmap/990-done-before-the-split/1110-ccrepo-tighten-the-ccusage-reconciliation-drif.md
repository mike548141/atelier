- [x] **ccrepo: tighten the ccusage reconciliation drift** — done 2026-07-22
  (wave-2 queue run, `75bba4c`). Root cause found and fixed: the
  `(message.id, requestId)` dedup kept the **last** log line, and the logs
  re-emit messages with a trailing partial/zeroed usage line — last-wins
  silently dropped tokens. Now keeps the **richest** record (max-total),
  which matches ccusage **exactly** on a frozen matched-session set;
  sonnet-5 (the ~1.5% outlier) → 0.00%, total drift → ~0.00% with only
  in-flight current-session variance left, reported plainly.
  `server_tool_use` measured live: present on many messages but every
  counter zero — per-call pricing not built, the v1 "named contributor"
  hypothesis retracted in the design doc as measured-false. Per-model
  reconcile also scoped to matched sessions (one-sided window-edge sessions
  no longer smear into phantom per-model deltas). Suite 92→94 green (111
  instruments-wide, re-proven post-merge).
