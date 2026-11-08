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
      💬 **Mike, 2026-11-08, in his own words** (asked by queue run 722ac2e2
      whether to redraft, walk the findings first, or drop the register; the
      recommended option was a redraft fixing every finding, with a period
      where old and new exemption forms both work): *"So your recommendation
      is to improve the design based on the the fable review advice - if
      thats correct then I approve"*. It is correct, so the redraft is
      approved: the design is reworked on the reviewer's counsel for XR1–XR14
      (both forms honoured through a transition, so no child goes red at the
      switch). The redraft's re-review is Fable work and waits for his
      approval then.
      📝 **REDRAFTED 2026-11-09** by queue run 722ac2e2 (an Opus worker, read by
      the orchestrator before landing), per Mike's approval above: the ADR
      `docs/decisions/2026-10-03-0641-the-exception-register.md` is reworked
      on the reviewer's counsel for every finding, still a draft. Today's
      markers and ignore files stay; each gains who granted it
      (`principal-ruled`, `principal-answer`, `agent`), session, date and a
      pointer to his words, the same tokens `160/980` put on manifest lines;
      old and new forms both work, and the old one retires only on a later
      dated ruling of his, so no child goes red (XR1). **Four questions for
      him** sit in the ADR's open-questions section: Q1 small design or one
      central file; Q2 whether a public repo may show session ids and
      pointers to his words; Q3 old exceptions marked "unrecorded" with a
      review-by date, or re-granted; Q4 binary contents scanned in a
      separate investigation or the gap accepted. The redraft's re-review is
      queued as `160/1130` and waits for his Fable approval.
      💬 **Mike's answers to the redraft's four questions, 2026-11-09 (to
      options queue run 722ac2e2 offered; answers, not rulings):** Q1 —
      *"Large: one central file"* (not the recommended option, which was the
      small in-place design): one central register file per repo replaces the
      scattered notes, so the redraft is reworked to that shape, keeping the
      both-forms transition so no child goes red during migration. Q2 —
      *"Yes, short ID + pointer"*: each exemption shows the 8-character
      session id and points to the record holding his words. Q3 — *"Mark
      'unrecorded' + review date"*. Q4 — *"Separate investigation"*: scanning
      inside binary files is filed as `115/390`, outside this design.
      📝 **REWORKED 2026-11-09** by queue run 722ac2e2 (an Opus worker, read by
      the orchestrator before landing) to the central shape he chose: one
      file per repo, `.atelier-exceptions.jsonl`, append-only under a union
      merge. Scanners read both forms from the start, and the old form
      retires only on a later dated ruling of his, at zero unmigrated. Q2 and
      Q3 are in; binary contents are out (`115/390`). The costs of the
      central choice are stated in the ADR's § 8, the largest being the
      build and migration. **Left for him:** approve the re-review
      (`160/1130`), then accept the design. Two readings of the writer's, both
      stated in the ADR: `.leakscanbinaries` moves in; floor softening stays
      in `.atelier-floor.json`.
