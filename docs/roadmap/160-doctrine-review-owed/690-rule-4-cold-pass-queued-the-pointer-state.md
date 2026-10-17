- [ ] 🛑 **Rule-4 cold pass queued: one unambiguous review-pointer state
      (`130/020`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and the
      run neither takes it nor spawns a reviewer for it. *Tier:* Fable, the
      principal-named review tier, checked at selection. *Pass type:* doctrine
      and code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `docs/roadmap/README.md`, `tools/pointerscan.py`,
      `tools/test_pointerscan.py`, `tools/board.py`, `tools/test_board.py`,
      and the state lines of the sixteen `160` items it converted, from
      `b02c56d` to `952f78a` and the merge that landed them on `main` on
      2026-10-05. *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
      **Brief WRITTEN 2026-10-16, review NOT run** —
      `docs/reviews/2026-10-16-1550-queued-glyph-state-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (queue run abe96d8d), on Mike's 2026-10-16 answer that
      a fresh Opus session writes these briefs; its exposure is disclosed in
      the brief. The pass stays queued for a further criterion-passing cold
      Fable session.
      `[~]` **CLAIMED 2026-10-17 0900 UTC for the review run** (wt:
      atelier-review-1017; brief `2026-10-16-1550-queued-glyph-state-cold.md`,
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
      - [ ] 🛑 **The pass RAN 2026-10-17 and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` orchestrator
            — the shape disclosed in the claim above; the sibling, the intent
            record and prior verdicts opened only after the phase-1 findings
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR · 3 MODERATE ·
            7 minor · 2 note →
            [`2026-10-16-1550-queued-glyph-state-cold.md`](../../reviews/2026-10-16-1550-queued-glyph-state-cold.md)
            (sibling folded in and deleted). PO1 (MAJOR): the legend admits
            three queue counts and every live pointer wears the unnamed `- [ ]
            ⏳` shape its own author wrote, so a session following the legend's
            words miscounts the queue; PO13 (minor) formed at reconcile.
            Findings are the principal's to decide (rule 3); nothing was
            applied.
