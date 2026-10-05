- [ ] 🎯 **Rule-4 cold pass queued: the linear line reader in three guards
      (`110/140`).** The run authored this itself (its dispatched workers'
      output counts as the run's authorship). It was queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* the line readers and their tests in
      `tools/{leakscan,secretscan,conflictscan}.py` and
      `tools/test_{leakscan,secretscan,conflictscan}.py`. It landed on
      `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-04 2215 UTC for the review run** (wt: review-1004;
      brief `docs/reviews/2026-10-04-2215-linear-line-reader-cold.md`) by a
      Mike-opened `claude-fable-5-1` session ("Do all cold reviews and any other
      work dependent on fable") that authored none of the delta. Shape,
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
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR / 1 MODERATE /
            3 minor / 4 note →
            [`2026-10-04-2215-linear-line-reader-cold.md`](../../reviews/2026-10-04-2215-linear-line-reader-cold.md)
            (sibling folded in and deleted). LN1 (predates this delta; the delta
            itself is clean): the staged plane of secretscan and leakscan drops
            added text after a non-LF line separator and any added line
            beginning with two plus signs, so a secret there is caught only by
            CI after the push. At release the orchestrator also named the
            2026-09-25 staged-plane verdict, which the brief had not listed.
            Findings are the principal's to decide (rule 3); nothing was
            applied.
