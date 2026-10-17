- [ ] 🛑 **Rule-4 cold pass queued: "harvest" scoped to monolithic boards
      across the close lists (`200/100` C3).** The run authored this itself.
      It was queued at landing, and the run neither takes it nor spawns a
      reviewer for it. *Tier:* Fable, the principal-named review tier,
      checked at selection. *Pass type:* doctrine cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `docs/method/RECORD.md` (the harvest trigger),
      `docs/method/CONCURRENCY.md` (the closing-litany bullet),
      `docs/method/session-open/session-open-prompt.md` (ending the
      session) and `skills/queue-run/SKILL.md` (step 6). It landed on
      `main` on 2026-10-03.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
      **Brief WRITTEN 2026-10-16, review NOT run** —
      `docs/reviews/2026-10-16-1510-harvest-monolithic-board-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (queue run abe96d8d), on Mike's 2026-10-16 answer that
      a fresh Opus session writes these briefs; its exposure is disclosed in
      the brief. The pass stays queued for a further criterion-passing cold
      Fable session.
      `[~]` **CLAIMED 2026-10-17 0900 UTC for the review run** (wt:
      atelier-review-1017; brief
      `2026-10-16-1510-harvest-monolithic-board-cold.md`, written 2026-10-16 by
      a non-author Opus brief-writer under a different session) by a Mike-opened
      `claude-fable-5-1` session ("I want you to do all reviews and fable
      dependent work") that authored none of the delta and none of the brief,
      and was not started or instructed by either. Shape, disclosed per rule 4:
      reviewer-plus-orchestrator, both seats Fable — this session holds the
      `.deferred.md` sibling outside the worktree and outside the harness
      scratchpad, and commits the records; a fresh Fable subagent it spawns
      forms every finding and severity. The sibling, the intent record and prior
      verdicts stay unopened by the reviewer until its phase-1 findings are
      committed. Provenance and exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-10-17 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR · 2 MODERATE ·
            2 minor · 5 note →
            [`2026-10-16-1510-harvest-monolithic-board-cold.md`](../../reviews/2026-10-16-1510-harvest-monolithic-board-cold.md)
            (sibling folded in and deleted). HM1 (MAJOR): the session-open
            prompt's delta site is reverted at HEAD by a stale-base restore
            (6a0ac93 after the backdated 4d80321), and board item 320/670
            under-reads it as possibly intended; HM10 (note) formed at
            reconcile. Findings are the principal's to decide (rule 3); nothing
            was applied.
