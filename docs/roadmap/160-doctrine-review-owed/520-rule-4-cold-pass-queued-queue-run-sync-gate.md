- [ ] 🎯 **Rule-4 cold pass queued: the queue-run skill's sync step gains the
      status-first gate (`200/100` C1).** The run authored this itself. It
      was queued at landing, and the run neither takes it nor spawns a
      reviewer for it. *Tier:* Fable, the principal-named review tier,
      checked at selection. *Pass type:* doctrine cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `skills/queue-run/SKILL.md` (step 2). It landed on `main` on
      2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      **Brief WRITTEN 2026-10-16, review NOT run** —
      `docs/reviews/2026-10-16-1510-queue-run-sync-gate-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (queue run abe96d8d), on Mike's 2026-10-16 answer that
      a fresh Opus session writes these briefs; its exposure is disclosed in
      the brief. The pass stays queued for a further criterion-passing cold
      Fable session.
      `[~]` **CLAIMED 2026-10-17 0900 UTC for the review run** (wt:
      atelier-review-1017; brief `2026-10-16-1510-queue-run-sync-gate-cold.md`,
      written 2026-10-16 by a non-author Opus brief-writer under a different
      session) by a Mike-opened `claude-fable-5-1` session ("I want you to do
      all reviews and fable dependent work") that authored none of the delta and
      none of the brief, and was not started or instructed by either. Shape,
      disclosed per rule 4: reviewer-plus-orchestrator, both seats Fable — this
      session holds the `.deferred.md` sibling outside the worktree and outside
      the harness scratchpad, and commits the records; a fresh Fable subagent it
      spawns forms every finding and severity. The sibling, the intent record
      and prior verdicts stay unopened by the reviewer until its phase-1
      findings are committed. Provenance and exposure go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-10-17; the cycle CLOSES on this pass (no
            MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 3 minor · 1 note →
            [`2026-10-16-1510-queue-run-sync-gate-cold.md`](../../reviews/2026-10-16-1510-queue-run-sync-gate-cold.md)
            (sibling folded in and deleted). SY1 (MODERATE): step 2's
            stop-and-move-to-a-worktree leaves the run no sync path, so step 4's
            claim on main from the dirty primary cannot land; SY7 (note) formed
            at reconcile. Findings are the principal's to decide (rule 3);
            nothing was applied.
