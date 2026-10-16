# Sibling to the queue-run sync-gate cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-16-1510-queue-run-sync-gate-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-16 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` —
  **not opened by the brief-writer**.
- Commissioning item: `200/100` C1, in
  `docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`
  — **not opened by the brief-writer**.
- The landing commit's message body (read by the brief-writer): it says the skill contradicted
  CONCURRENCY, that the skill's header forbids that, and that the fix was made on its own per a
  principal answer quoted there.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-22-1149-queue-run-doctrine-cold.md`
- `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md`
- `docs/reviews/2026-09-25-0715-0918-hand-up-fixes-cold.md`

## The pointer's own lens hints

None. The pointer is refs-only; its last sub-bullet is the brief-writer's orchestrator's claim.

## Overlap with sibling passes of this batch

`skills/queue-run/SKILL.md` is also the subject of the harvest pass
(`2026-10-16-1510-harvest-monolithic-board-cold.md`, step 6). Different steps; a runner taking
both should run them in sequence and say so, since one reading of the file serves both.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The skill's header forbids restating standing rules, and step 2 now restates CONCURRENCY's two
   gates in full rather than pointing at them. Has the fix re-created the drift class the header
   names, one level down?
2. A queue run claims items on `main` from the primary checkout before it moves anywhere. If the
   primary is dirty with a peer's work, step 2 says stop and move — where does the claim happen?
3. "Only your own work": at a run's start, what dirty work can be its own? A run resumed after a
   context cut, or a worker's output left in the primary, are the live cases.
4. "A repo with no upstream skips the pull", where CONCURRENCY says "no remote, no bookend".
   Upstream and remote are different facts; which is meant, and do the two texts agree?
5. Step 2 then loads the onramp, and atelier's own read order (its `CLAUDE.md` step 1) runs the
   same status-then-pull again. Does a run now sync twice, and is the second pass's "yours"
   still well defined once the run has started work?
