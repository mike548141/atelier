# Session — B4 harvestscan cold pass, PASS-WITH-FINDINGS — HV1–HV5 to Mike

- **Date:** 2026-07-29, 1306 UTC
- **Model:** Fable 5 (1M context), wt: b4-harvestscan-cold-pass
- **Ask:** third queue item for the Mike-spawned "do review work" taker
  session (after the E6 intent pass and the B2+B3 pass).

## Provenance (rule 4) — and a named exposure

Taker session authored nothing in the Track B chain; claim on `main`
(`3cad1a9`) before the worktree. **Deferral exposure disclosed in the
brief:** B4 shares its intent record with B2+B3, which this same taker
opened at the B2+B3 reconcile — so the author's do-not-wire counsel was
seen before this brief was written. Handled as seeded questions (a floor,
never a fence); the residual is on the record for Mike to weigh.

## What ran

Code + measurement + **verdict** pass on `ff8080b`. Claims re-run, not
read: selftest + 16 tests green (two must-fire legs); the replay harness
rebuilt from the tool's pure functions (it did not ship) and the full
measurement re-run — 105/391 commits (26.9%), 158 items, `dd7fcb74` = 2:
**every recorded figure reproduced exactly.** Then the measurement the
verdict lacked: the bulk-delete-scoped variant, over the same history.

## Verdict

**PASS-WITH-FINDINGS — 1 MAJOR / 2 minor / 2 notes.** HV1 (MAJOR, on the
verdict): "do not wire, not even advisory" rests on the unscoped rate
alone; the measured net-bulk-delete scope yields 6 in-scope commits in
the repo's whole history, 3 warns, all justified, incident caught — and
the entry's first-ranked strict delete-only shape would have missed the
incident (+48/−184). Wire-scoped vs shelved re-put to Mike with numbers.
HV2: the pointer exclusion assumes the refs-only ceiling the record shows
breached three times (pairs with the FUNDED reviewscan ⏳-grammar item).
HV3: survivor search is two files, narrower than the docstring's
"anywhere". HV4/HV5: plane wording; the hand-run shelf has no carrier.
All rulings Mike's; nothing applied. Verdict:
[`2026-07-29-1306-b4-harvestscan-cold.md`](../reviews/2026-07-29-1306-b4-harvestscan-cold.md).
