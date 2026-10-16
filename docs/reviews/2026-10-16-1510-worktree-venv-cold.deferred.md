# Sibling to the worktree-venv cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-16-1510-worktree-venv-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-16 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` —
  **not opened by the brief-writer**.
- Commissioning item: `200/100` C4, in
  `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`
  — **not opened by the brief-writer**.
- The landing commit's message body (read by the brief-writer): it says the bullet described the
  iCloud-era layout, that STORAGE made in-repo `.venv` the norm when the estate left iCloud, and
  that the new text adds the consequence a session meets in practice.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

No verdict carries the old "external venv" phrase. Nearest CONCURRENCY substrate passes by name:
`docs/reviews/2026-07-11-concurrency-put-away.md`,
`docs/reviews/2026-07-20-1355-concurrency-flip-cold.md`.

## The pointer's own lens hints

None. The pointer is refs-only; its last sub-bullet is the brief-writer's orchestrator's claim.

## Overlap with sibling passes of this batch

`docs/method/CONCURRENCY.md` is also the subject of the three-cues pass (§ *The trigger*) and the
harvest pass (the closing-litany bullet). Different sections; sequence them if one runner takes
several.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. "Or points at the primary's explicitly" re-admits the sharing the old text recommended. With
   an editable install, the primary's venv imports the primary's source, so a worktree's tests
   could run the wrong tree and pass. Should the bullet name that, or drop the option?
2. STORAGE's rule is conditional on a synced working copy; the bullet states "the norm is an
   in-repo `.venv`" unconditionally, with an estate-history date, in a doctrine file adopters
   read. Is that an estate fact presented as house doctrine?
3. The retained first sentence still gives iCloud sync churn as the reason worktrees live in
   `~/worktrees/`, after the estate left iCloud, while harness-native worktrees land in a
   worktrees folder under the repo's own `.claude` directory (per this repo's `.gitignore`). Did
   the fix leave the bullet's other half stale?
