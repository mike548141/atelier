- ⏳ **Rule-4 cold pass queued: the concurrency cue count (`200/100`
      C5).** The run authored this itself. It was queued at landing, and the
      run neither takes it nor spawns a reviewer for it. *Tier:* Fable, the
      principal-named review tier, checked at selection. *Pass type:*
      doctrine cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `docs/method/CONCURRENCY.md` (§ *The trigger*, the cue
      count). It landed on `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      **Brief WRITTEN 2026-10-16, review NOT run** —
      `docs/reviews/2026-10-16-1510-three-cues-cold.md` with a `.deferred.md`
      sibling. Written by an Opus brief-writer that authored none of the delta
      (queue run abe96d8d), on Mike's 2026-10-16 answer that a fresh Opus
      session writes these briefs; its exposure is disclosed in the brief. The
      pass stays queued for a further criterion-passing cold Fable session.
      `[~]` **CLAIMED 2026-10-17 0900 UTC for the review run** (wt:
      atelier-review-1017; brief `2026-10-16-1510-three-cues-cold.md`, written
      2026-10-16 by a non-author Opus brief-writer under a different session) by
      a Mike-opened `claude-fable-5-1` session ("I want you to do all reviews
      and fable dependent work") that authored none of the delta and none of the
      brief, and was not started or instructed by either. Shape, disclosed per
      rule 4: reviewer-plus-orchestrator, both seats Fable — this session holds
      the `.deferred.md` sibling outside the worktree and outside the harness
      scratchpad, and commits the records; a fresh Fable subagent it spawns
      forms every finding and severity. The sibling, the intent record and prior
      verdicts stay unopened by the reviewer until its phase-1 findings are
      committed. Provenance and exposure go in the verdict.
