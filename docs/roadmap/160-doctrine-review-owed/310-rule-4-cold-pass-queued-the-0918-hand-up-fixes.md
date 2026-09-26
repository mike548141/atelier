- ⏳ **Rule-4 cold pass queued — the 2026-09-18 hand-up fixes to the
      session-start sync, the act-verification clause and the drift command.**
      Self-authored doctrine, queued at landing by its author, who may not take
      it. *Tier:* Fable, the principal-named review tier — checked at
      selection; a session that cannot honour the bar stops rather than takes.
      *Pass type:* doctrine cold pass, per `method/REVIEW.md` rule 4.
      *Delta — scoped to paths, deliberately not to the commit:*
      `docs/method/CONCURRENCY.md` § *Integration hygiene* (the **Sync
      bookends** bullet's two gates, and the new **Verify the act** bullet) ·
      `docs/method/PROPAGATION.md` § *The mechanism* point 4, and in § *The
      standard child doctrine block* the **Concurrency** and **Source &
      drift** bullets · `docs/build/templates/CLAUDE.md` (the same two
      bullets) · `CLAUDE.md` (onramp step 1) · `docs/method/COMMUNICATION.md`
      (the enforceable-split bullet and the reply-plane paragraph — plainscan
      removed, `020/360`). Landed on `main`.
      *Intent record:*
      [`../../sessions/2026-09-18-0114-queue-run-hand-up-fixes.md`](../../sessions/2026-09-18-0114-queue-run-hand-up-fixes.md).
      `[~]` **CLAIMED 2026-09-25 0705 UTC for the review run** (wt:
      review-batch-0925; brief
      `docs/reviews/2026-09-25-0715-0918-hand-up-fixes-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Please deliver all fable
      dependent work, and work that would be best delivered using fable") that
      authored none of the delta. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree;
      a fresh Fable subagent it spawns forms every finding and severity. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and exposure
      go in the verdict.
      - [ ] 🎯 **The pass RAN 2026-09-26; the cycle CLOSES on this pass (no
            MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` orchestrator — the shape disclosed in the claim
            above; the sibling, the intent record and prior verdicts opened only
            after the phase-1 findings were committed) returned
            PASS-WITH-FINDINGS — 0 MAJOR · 4 MODERATE · 6 minor · 2 note →
            [`2026-09-25-0715-0918-hand-up-fixes-cold.md`](../../reviews/2026-09-25-0715-0918-hand-up-fixes-cold.md)
            (sibling folded in and deleted). HF2 (MODERATE): the corrected drift
            check reads current when its fetch fails offline — the
            absence-of-an-error class the same commit's verify-the-act bullet
            names; HF1 (MODERATE): the autostash mechanism prose is wrong about
            the real harm; HF3/HF4 (MODERATE): the class was not harvested
            across skills and pins.py, and COMMUNICATION still describes a live
            reply plane; HF11/HF12 (minor) formed at reconcile. Findings are the
            principal's to decide (rule 3); nothing was applied.
