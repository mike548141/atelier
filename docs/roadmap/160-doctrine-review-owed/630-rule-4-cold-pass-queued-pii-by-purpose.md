- [~] (claimed 2026-11-09-0120, wt: atelier-rr-722a-630)
      🎯 **Rule-4 cold pass queued: personal data held by purpose, with
      recorded exceptions (`200/100` C11).** The run authored this itself.
      The rule is in Mike's own words, and the placement and wording around
      it are the run's. It was queued at landing, and the run neither takes
      it nor spawns a reviewer for it. *Tier:* Fable, the principal-named
      review tier, checked at selection. *Pass type:* doctrine cold pass,
      per `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `docs/build/REPO-STANDARD.md`, `docs/build/templates/CLAUDE.md`,
      `docs/build/templates/CONTRIBUTING.md` and `CLAUDE.md` (the
      personal-data constraint in each). It landed on `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      `[~]` **CLAIMED 2026-10-04 2215 UTC for the review run** (wt: review-1004;
      brief `docs/reviews/2026-10-04-2215-pii-by-purpose-cold.md`) by a
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
            were committed) returned PASS-WITH-FINDINGS — 2 MAJOR / 6 MODERATE /
            2 minor / 1 note →
            [`2026-10-04-2215-pii-by-purpose-cold.md`](../../reviews/2026-10-04-2215-pii-by-purpose-cold.md)
            (sibling folded in and deleted). PI1: the public repo's hard
            constraint says each personal-data exception is declared where it
            appears, but the account name stands on 27 lines with no inline
            declaration and the leak guard passes it unmarked. Findings are the
            principal's to decide (rule 3); nothing was applied.
      💬 **Mike's answer, 2026-11-09 (to options queue run 722ac2e2 offered,
      re-put with their impacts after he said he did not understand them; an
      answer, not a ruling):** *"Honest claim + only you grant"* — the offered
      option read: reword the claim to "listed in one place" (true today),
      add a test that keeps that list matching the files, and add a rule that
      in a public repo only he grants a personal-data exception, in his own
      words, so the scanner refuses any other excuse (PI1, PI2 on the
      reviewer's counsel); the other findings take the reviewer's counsel.
