# Cold pass — the applied batch of the G1–G3 rulings (delta `578d84d`)

- **Date/time**: 2026-07-19 0629 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike spawned with "do any review work". This session authored **none** of:
  the doctrine under the chain (REVIEW.md and the review-trigger/sizescan
  deltas), the 0407 combined pass, the batch that applied its F1–F9 rulings,
  the 0544 applied-batch pass that produced G1–G3, or the application of
  Mike's G1–G3 rulings now under review. The author/applier queued the `⏳`
  pointer and stopped; this brief is taker-written.
- **Named exposure**: the taker read the `⏳` ROADMAP item and the one-line
  `SESSIONS.md` entry tails before claiming — both carry the applier's
  evaluative summary (e.g. "re-proven both legs"). That is framing leak
  beyond bare refs; it is named here, and every such claim is treated as a
  claim to re-run, not a fact. Additionally, an application review cannot
  fully honour rule 2: the delta itself contains hunks to the prior verdict
  files. Sequence per REVIEW.md: review the non-verdict files at HEAD and
  commit findings first; open the verdict-file hunks and applier's log after.

## What the work is (refs only)

Commit `578d84d` — the application of Mike's 2026-07-19 ruling ("yes take all
three") on the 0544 pass's G1–G3 findings. In-scope files at HEAD:

- `docs/build/templates/workflows/floor.yml` (G1 — pin-slot rewording)
- `tools/test_templates.py` (G2 — placeholder-inventory test)
- `docs/sessions/2026-07-18-0820-review-the-design-not-only-the-build.md`
  (G3 — dated one-liner)
- `CHANGELOG.md`, `docs/ROADMAP.md`, `docs/SESSIONS.md` (records of the batch)

**Deferred below the divider** (opened only after this reviewer's findings are
committed): the delta's hunks to
`reviews/2026-07-19-0544-combined-applied-batch-cold.md` and
`reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md` (decision
stamps + correction addenda), and the applier's session-log addenda
(`sessions/2026-07-19-0407-…` and `…-0544-…`).

## Ask

Run all three lenses on the applied delta:

1. **Approach & assumptions** — name the load-bearing assumptions first, then
   attack them. Does each applied fix actually discharge the finding it claims
   to? Is the rewording/test the right mechanism, or a patch over the class?
2. **Correctness & quality** — re-run every live proof in scope rather than
   reading it: the 275-test suite; the prove-the-stamp grep **both legs on a
   full scaffold** (red without the fix, green with); G2's bite proof
   (re-introducing a stamp token must turn the suite red). Honest-labelling
   check on the addenda: corrections dated, originals standing.
3. **Completeness / harvest** — anything the rulings required that the batch
   skipped; anything the new test should cover and doesn't; record hygiene
   (CHANGELOG/ROADMAP/SESSIONS consistent with the delta).

Cycle context: this pass is terminal if it returns no MAJOR (close rule) —
report findings either way; decisions are Mike's (rule 3: the chain is
self-authored doctrine).

---

## Deferred material (open only after findings are committed)

- `git show 578d84d -- docs/reviews/2026-07-19-0544-combined-applied-batch-cold.md`
- `git show 578d84d -- docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`
- `git show 578d84d -- docs/SESSIONS.md docs/sessions/2026-07-19-0407-combined-cold-pass-taken.md docs/sessions/2026-07-19-0544-applied-batch-cold-pass-taken.md`
- The authors seeded no questions; there is no author-written ask anywhere in
  this file. Everything above the divider is taker-written.
