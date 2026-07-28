# Session — the secretscan fragment-match fix's cold pass (cycle closed)

- **Date**: 2026-07-28 12:16 UTC (claim) → 13:05 UTC (close)
- **Tier / spawn**: Fable (the tier the queue asked for on the security
  floor); the Mike-spawned "do any review work" taker session, fourth
  queue item. Author of nothing in this delta; not spawned by its author.
- **Worktree**: `secretscan-fragment-cold-pass`.
- **Subject**: the queued `⏳` on `dd902aa` (#14) — the four fragment-match
  suppression fixes and their three introduced-FP suppressions.

## What happened, and the result

Claim → brief (both aimed questions taken as floor, not fence) → adversarial
probes: all four red legs old-vs-new on synthetic fixtures, FP-neighbour
checks, an independent estate re-scan, and a committed-blob audit of the
test values → verdict committed before the triage record was opened →
reconcile. One file holds the exchange:
[brief and verdict](../reviews/2026-07-28-1220-secretscan-fragment-cold.md).

**PASS-WITH-FINDINGS — 0 MAJOR / 1 minor / 3 notes; cycle CLOSED.**
SF1 (live-proven): the kebab exemption un-flags hyphenated passphrases the
old scanner caught. SF2: the lowercase-hex gap measured at half its stated
size. SF3: the corpus-re-scan question answered — regression floor, not
acceptance test; canary-suite counsel. SF4: resolved at reconcile (the
ruled untrack). One triage-record aside corrected: the ≥32-char entropy
net holds only for mixed-class values. 🎯 SF1–SF4 queued for Mike.

## Owed

Nothing queued by this session (terminal close, no doctrine edited).
