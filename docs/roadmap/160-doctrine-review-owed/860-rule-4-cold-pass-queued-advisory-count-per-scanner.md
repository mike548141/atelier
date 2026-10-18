- [ ] 🛑 **Rule-4 cold pass queued: the floor's advisory count scoped to its
      scanner, and three more unsoftenable pins (`115/320`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/floor.py`, `tools/test_floor.py` and a comment in
      `tools/licenscan.py`, commit `dc0ed0e` (cherry-picked from the worker's
      `fe4f20d`), landed on
      `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`](../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md).
      **Brief WRITTEN 2026-10-17, review NOT run** —
      `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored none
      of the delta (dispatched by the Mike-opened Fable review session, wt
      atelier-review-1017), on Mike's 2026-10-16 answer that a fresh Opus
      session writes these briefs; its exposure is disclosed in the brief. The
      pass stays queued for a further criterion-passing cold Fable session.
      `[~]` **CLAIMED 2026-10-17 2319 UTC for the review run** (a cloud
      session with no worktree: the container's one checkout, branch
      `claude/review-work-briefs-adj6ad`, landed on `main` by PR before any
      pass runs; brief `2026-10-17-1010-advisory-count-per-scanner-cold.md`,
      written 2026-10-17 by a non-author Opus brief-writer under a different
      session) by a Mike-opened `claude-fable-5-1` cloud session ("As a cold
      session please do any review work, any work that is fable dependent, and
      write briefs for any reviews that need them") that authored none of the
      delta and none of the brief, and was not started or instructed by
      either; it opened on `claude-opus-5` and Mike switched it to
      `claude-fable-5-1` before any claim or pass. Shape, disclosed per rule
      4: reviewer-plus-orchestrator, both seats Fable — this session holds the
      `.deferred.md` sibling outside the checkout and outside the harness
      scratchpad, and commits the records; a fresh Fable subagent it spawns
      forms every finding and severity. The sibling, the intent record and
      prior verdicts stay unopened by the reviewer until its phase-1 findings
      are committed. Provenance and exposure go in the verdict.
      - [ ] 🛑 **The pass RAN 2026-10-18 UTC and the cycle stays OPEN — a MAJOR
            stands.** The rule-4 Fable cold pass (taker: a fresh
            `claude-fable-5-1` subagent under a `claude-fable-5-1` cloud
            orchestrator — the shape disclosed in the claim above; the sibling,
            the intent record and prior verdicts opened only after the phase-1
            findings were committed, `51679e6`) returned PASS-WITH-FINDINGS —
            1 MAJOR · 0 MODERATE · 4 minor · 3 note →
            [`2026-10-17-1010-advisory-count-per-scanner-cold.md`](../../reviews/2026-10-17-1010-advisory-count-per-scanner-cold.md)
            (sibling folded in and deleted). AV1 (MAJOR): the reader's
            last-match rule rests on an ordering the writers do not keep — both
            count-carriers print their advisory finding lines, which carry the
            flagged path, after the count line — so a committed root-level file
            or directory whose name is a forged zero count line followed by a
            newline makes the board read a silent zero (`✅ … enforced`, JSON
            `advisory: 0`) while the scanner printed a count of 2, on both
            planes and for both writers; the delta closes the brief's
            no-newline case and leaves this narrower, worse-in-kind hole, the
            2026-08-09 AB5 residue made live by the switch from first to last
            match. AV8 (note) formed at reconcile. Findings are the principal's
            to decide (rule 3); nothing was applied.
