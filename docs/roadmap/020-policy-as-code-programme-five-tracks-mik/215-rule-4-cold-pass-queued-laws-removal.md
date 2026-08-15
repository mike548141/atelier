- [ ] 🎯 **The Laws-removal cycle CLOSED 2026-08-15 (0 MAJOR); LR1–LR9 await
      Mike's ruling round.** The rule-4 Fable cold pass (taker: a cold session
      Mike opened 2026-08-15 ~1120 UTC, running the brief a *different* cold
      session wrote at 1024 UTC, under an orchestrator-held context partition)
      returned PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE / 2 minor / 4 note
      after reconcile (LR5 amended note → minor; LR8–LR9 added post-reconcile)
      → [`reviews/2026-08-15-1031-laws-removal-apex-cold.md`](../../reviews/2026-08-15-1031-laws-removal-apex-cold.md).
      Every re-run reproduced: byte-identity of the PROPAGATION floor block and
      the template stamp, stampscan clean, floor green both planes, suites
      green. The MODERATEs: LR1 — a live board instruction the delta itself
      edited still tells children to adopt a "three-element floor"; LR3 — a
      principal-authored open item was *deleted* from the board rather than
      closed with a disposition (`1b46d05`, landed after this pass's claim,
      appears to restore-and-close it — principal to confirm); LR4 — "children
      shed the Laws sentence at their next pin bump" is stated as behaviour
      but is an unenforced convention, and 13 of 17 pinned children still
      carry a Laws sentence. LR2 (minor: the "surface a genuine dilemma" line
      left with the section) appears resolved on its face by `c782e14`, also
      after the claim. *Delta:* the removal commit `71b3e8f` on wt:
      laws-removal-0815 (claim `4ea0a8f`, merge `b5da9e5`). *Intent record:*
      `docs/sessions/2026-08-15-0809-laws-removal.md`.
