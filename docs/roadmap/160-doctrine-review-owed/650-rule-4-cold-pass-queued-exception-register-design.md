- [ ] 🎯 **Rule-4 cold pass queued: the exception-register design, before it is
      accepted or built (`110/100` part 2).** The run authored this itself.
      It was queued at drafting, and the run neither takes it nor spawns a
      reviewer for it. *Tier:* Fable, the principal-named review tier,
      checked at selection. *Pass type:* design cold pass, per
      `method/REVIEW.md` § *Review the design*. *Delta, scoped to paths:*
      `docs/decisions/2026-10-03-0641-the-exception-register.md` (draft). It
      landed on `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-04 2215 UTC for the review run** (wt: review-1004;
      brief `docs/reviews/2026-10-04-2215-exception-register-design-cold.md`) by
      a Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any
      other work dependent on fable") that authored none of the delta. Shape,
      disclosed per rule 4: reviewer-plus-orchestrator, both seats Fable — this
      session writes the refs-only brief and holds the `.deferred.md` sibling
      outside the worktree; a fresh Fable subagent it spawns forms every finding
      and severity. The sibling, the intent record and prior verdicts stay
      unopened by the reviewer until its phase-1 findings are committed.
      Provenance and exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-10-04 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned FAIL as a design to accept as drafted — 3
            MAJOR / 7 MODERATE / 3 minor / 3 note →
            [`2026-10-04-2215-exception-register-design-cold.md`](../../reviews/2026-10-04-2215-exception-register-design-cold.md)
            (sibling folded in and deleted). XR1: retiring the inline markers
            and ignore files would red every child at its next CI run, not at a
            pin bump — children call the floor at the main branch and the draft
            has no both-forms transition. Findings are the principal's to decide
            (rule 3); nothing was applied.
