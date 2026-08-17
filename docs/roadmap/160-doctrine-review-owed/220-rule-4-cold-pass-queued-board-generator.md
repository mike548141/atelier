- [ ] 🎯 **The board-generator cycle CLOSED 2026-08-17 (0 MAJOR); BG1–BG14
      await Mike's ruling round.** The rule-4 Fable code cold pass (taker: a
      cold session Mike opened 2026-08-17 0955 UTC on the Fable tier, running
      the brief a *different* cold session wrote at 0730 UTC, under a
      Fable-orchestrator-held context partition — reviewer and orchestrator
      both on the named tier) returned PASS-WITH-FINDINGS — 0 MAJOR /
      4 MODERATE / 4 minor / 6 note after reconcile (no severity amendments;
      BG13–BG14 added post-reconcile) →
      [`reviews/2026-08-17-0730-board-generator-child-truth-cold.md`](../../reviews/2026-08-17-0730-board-generator-child-truth-cold.md).
      Every re-run reproduced in kind: selftest OK, Python 1,344 / node 235,
      both floor planes green, pathscan 29 → 1 before/after the delta, the
      public child's index 49 / 16 → 0 / 0 and byte-identical to its committed
      copy, the emitted command run live under env / config / neither. The
      MODERATEs, all one class (*a string true from one place, asserted true
      from every place*): BG1 — the index text and so the enforced check's
      verdict depend on where the generator ran from (flip-flop across
      geometries; no test covers the in-tree branch); BG2 — the child spelling
      names two of the hook's three resolution branches, so a symlinked-tools
      child or a fresh unconfigured clone gets `python3 /board.py`; BG3 —
      "passes wrapscan in any repo" is a property of the current data, not the
      renderer (a long state line with an allow-marker renders to a flagged
      187-column line), so the withdrawn `070` policy question is **not**
      closed by the code; BG4 — the corrections did not reach `tools/README.md`,
      `CHANGELOG.md` or the module docstring, which still carry the superseded
      spelling and the withdrawn residual. Reconcile: BS1 (MAJOR, open) and
      BG1/BG2 sit on the same `check` path in sequence — rule together.
      *Delta:* the generator commit on wt: board-generator-child-truth
      (`tools/board.py`, `tools/pointerscan.py`, `tools/README.md`,
      `CHANGELOG.md`) plus the board commits `e2551da` and the `080`/`070`
      updates that landed with it, and `a3a64aa`. *Intent record:*
      `docs/sessions/2026-08-17-0530-board-generator-child-truth.md`. Brief
      written 2026-08-17 by a non-author Opus cold session (its disclosures
      stand in the verdict, judged acceptable by the reviewer with grounds);
      sibling folded in and deleted; wt: cold-run-0817-0955.
