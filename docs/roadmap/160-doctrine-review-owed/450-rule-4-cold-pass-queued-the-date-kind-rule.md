- [ ] 🛑 **Rule-4 cold pass queued: the mandate-versus-default date rule
      (`040/010`).** The run authored the wording itself. The rule is Mike's
      and is quoted, and the placement and surrounding prose are the run's.
      It was queued at landing, and the run neither takes it nor spawns a
      reviewer for it. *Tier:* Fable, the principal-named review tier,
      checked at selection. *Pass type:* doctrine cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `docs/method/GUARDS.md` (the new subsection under § *Acceptance and
      deferment are different things*). It landed on `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-03 0357 UTC for the review run** (wt:
      `atelier-review-430`, branch `review-430-1003`; brief
      `docs/reviews/2026-10-03-0357-date-kind-rule-cold.md`)
      by a Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any
      other work dependent on fable") that authored none of the delta and was
      not started or instructed by the authoring run. Shape, disclosed per rule
      4: reviewer-plus-orchestrator, both seats Fable — this session writes the
      refs-only brief and holds the `.deferred.md` sibling outside the worktree
      and outside the harness scratchpad; a fresh Fable subagent it spawns forms
      every finding and severity. Disclosed exposure: the authoring run told
      this session, over the cross-session channel, that the pointer existed
      and named its subject in a phrase; nothing else from it was read. The
      sibling, the intent record and prior verdicts stay unopened by the
      reviewer until its phase-1 findings are committed. Provenance and
      exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-10-03 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR · 3 MODERATE ·
            7 minor · 0 note →
            [`2026-10-03-0357-date-kind-rule-cold.md`](../../reviews/2026-10-03-0357-date-kind-rule-cold.md)
            (sibling folded in). DK1 (MAJOR): the rule asks for a kind a child
            can read beside the date, but `floor.py`'s parser refuses any key
            beside `why` and `review-by` (probed), so the kind can only travel
            as free text nothing reads — by GUARDS.md's own homing test it is
            not yet a rule. DK2 (MODERATE): a child that mis-classes a mandate
            and sets a later date trips nothing on either plane. DK3
            (MODERATE): self-set dates and event-expiring deferments fall
            outside both kinds. The principal's words are quoted verbatim
            against the board capture; two glosses are the run's own (DK4,
            DK10). The review worktree lacked the delta at spawn (DK8) and the
            brief's sweep bar named a directory that never existed (DK9); both
            recovered and disclosed. The phase-1 verdict landed inside commit
            `4ff5f81` (titled for the CP pass) because a blocked commit had left
            that pass's files staged; the text is unrevised. Findings are the
            principal's to decide (rule 3); nothing was applied.
