- [ ] 🛑 **Rule-4 cold pass queued: `indexscan`, the generic index-integrity
      guard (`200/010`).** The run authored this itself (its dispatched
      worker's output counts as the run's authorship). It is queued at
      landing, and the run neither takes it nor spawns a reviewer for it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4. *Delta,
      scoped to paths:* `tools/indexscan.py`, `tools/test_indexscan.py`,
      `tools/floor.py`, `tools/README.md`, `tools/test_allowmarker.py`,
      `tools/test_mixed_root.py`, and the declaration and allow-marker lines
      in `docs/decisions/README.md`, `instruments/README.md` and
      `docs/SESSIONS.md`, from `8d10487` to the merge that landed it on
      `main` on 2026-10-05. *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
      **Brief WRITTEN 2026-10-16, review NOT run** —
      `docs/reviews/2026-10-16-1551-indexscan-guard-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (queue run abe96d8d), on Mike's 2026-10-16 answer that
      a fresh Opus session writes these briefs; its exposure is disclosed in
      the brief. The pass stays queued for a further criterion-passing cold
      Fable session.
      `[~]` **CLAIMED 2026-10-17 0900 UTC for the review run** (wt:
      atelier-review-1017; brief `2026-10-16-1551-indexscan-guard-cold.md`,
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
            were committed) returned PASS-WITH-FINDINGS — 1 MAJOR · 1 MODERATE ·
            5 minor · 3 note →
            [`2026-10-16-1551-indexscan-guard-cold.md`](../../reviews/2026-10-16-1551-indexscan-guard-cold.md)
            (sibling folded in and deleted). IX1 (MAJOR): the delta's
            "listed-but-missing is already guarded" claim is false for code-span
            catalogues, so the tools and instruments indexes have no guard when
            an entry's file is deleted; IX10 (minor) formed at reconcile.
            Findings are the principal's to decide (rule 3); nothing was
            applied.
