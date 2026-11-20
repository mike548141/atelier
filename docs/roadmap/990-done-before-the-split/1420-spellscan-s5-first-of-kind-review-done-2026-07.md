- [x] **spellscan (S5) first-of-kind review — DONE 2026-07-23** (queue run 0707,
      cold Opus reviewer; taker rule-4 cleared). Verdict **PASS-WITH-FINDINGS —
      0 MAJOR / 2 minor / 1 Low / 1 nit**, NOT gate-ready. The core spelling-tool
      safety property is *proven*: no confident wrong correction, no both-correct
      word flagged (z→s engine verified across all 46 noun forms). 60 tests +
      selftest green (orchestrator re-verified). Real latent bug found (SS1:
      `hypothesize`/`jeopardize`/`penalize` in `IZE_NOUN_CAPABLE` contradict the
      docstring's stated exclusion). Baseline ~1-in-5 signal — 53 of 68 are
      `artifact` (mostly the legit CI/SBOM term-of-art). Brief:
      [`reviews/2026-07-23-0707-spellscan-s5-cold.md`](../../reviews/2026-07-23-0707-spellscan-s5-cold.md).
