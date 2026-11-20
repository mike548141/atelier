- [x] **wrapscan (S1) first-of-kind review — DONE 2026-07-23** (queue run 0707,
      cold Opus reviewer; taker rule-4 cleared). Verdict **PASS-WITH-FINDINGS —
      1 MAJOR / 3 minor / 2 Low**, NOT gate-ready. Tool is correct, honestly
      documented, correctly wired advisory; 40 tests + selftest green (orchestrator
      re-verified). The MAJOR (WS1) is a **gate-scope** finding, not a detection
      bug: default `docs/**` buries the real signal (~15% doctrine-prose
      over-wraps) under 154 deliberate single-line SESSIONS index rows (54% of the
      287 baseline). Brief:
      [`reviews/2026-07-23-0707-wrapscan-s1-cold.md`](../../reviews/2026-07-23-0707-wrapscan-s1-cold.md).
