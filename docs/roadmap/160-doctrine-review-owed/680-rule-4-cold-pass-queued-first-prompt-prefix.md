- [ ] 🎯 **Rule-4 cold pass queued: cctranscript's first-prompt prefix read
      (`210/180`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and the
      run neither takes it nor spawns a reviewer for it. *Tier:* Fable, the
      principal-named review tier, checked at selection. *Pass type:* code
      cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `instruments/cctranscript` and `instruments/cctranscript.test.js`,
      merge `89a7539` and the commit after it. It landed on `main` on
      2026-10-05. *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
      **Brief WRITTEN 2026-10-16, review NOT run** —
      `docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (queue run abe96d8d), on Mike's 2026-10-16 answer that
      a fresh Opus session writes these briefs; its exposure is disclosed in
      the brief. The pass stays queued for a further criterion-passing cold
      Fable session.
      `[~]` **CLAIMED 2026-10-17 0900 UTC for the review run** (wt:
      atelier-review-1017; brief `2026-10-16-1550-first-prompt-prefix-cold.md`,
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
            PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 3 minor · 5 note →
            [`2026-10-16-1550-first-prompt-prefix-cold.md`](../../reviews/2026-10-16-1550-first-prompt-prefix-cold.md)
            (sibling folded in and deleted). FP1 (MODERATE): the "prefix can
            never change an answer" claim fails on a damaged mirror, where a
            corrupt-but-decodable prefix lists silently wrong text where the old
            read threw; FP9 (note, privacy) formed at reconcile. Findings are
            the principal's to decide (rule 3); nothing was applied.
