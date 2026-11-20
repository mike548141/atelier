- [x] (2026-08-03: applied, pointer queued) 🎯 **B4 — REVIEWED 2026-07-29 (rule-4 Fable cold pass):
  PASS-WITH-FINDINGS — 1 MAJOR / 2 minor / 2 notes; every recorded
  figure reproduced exactly. HV1–HV5 RULED 2026-07-29 (Mike): the shelf
  verdict is OVERTURNED on the pass's measurement — WIRE `harvestscan`,
  scoped and advisory:** registry entry firing only on net-bulk-delete
  roadmap commits (≥50 net lines removed), warn-only, never blocking.
  Evidence: 6 in-scope commits in the 391-commit history, 3 warns, all
  justified, the `dd7fcb74` incident caught; strict delete-only rejected
  (it misses the incident, +48/−184). HV2 — the pointer exclusion's
  dependency on the FUNDED `reviewscan` ⏳-grammar check is named and
  they build together. HV3 — survivor search widened to
  `docs/sessions/` + `docs/reviews/`, effect measured by the replay
  harness before landing. HV4 — usage wording + the staged-vs-working
  seam handled in the wiring build. HV5 lapsed under HV1. Rulings
  verbatim + counsel:
  [B4 cold pass](../../reviews/2026-07-29-1306-b4-harvestscan-cold.md).
  **Application owed as one wiring build item (scope + tests + registry
  + HV2–HV4 folds); it queues its rule-4 pointer at landing.**
