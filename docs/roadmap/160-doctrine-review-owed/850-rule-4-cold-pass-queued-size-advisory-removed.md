- [ ] 🎯 **Rule-4 cold pass queued: sizescan's size advisory removed
      (`115/270` c).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code and doctrine cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `tools/sizescan.py`, `tools/test_sizescan.py`,
      `tools/test_report.py`, `tools/README.md`, `docs/method/RECORD.md`, and
      comments in `tools/pins.py` and `tools/blockscan.py`, commit `72a68cc`
      and its merge, landed on
      `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`](../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md).
      **Brief WRITTEN 2026-10-17, review NOT run** —
      `docs/reviews/2026-10-17-0955-size-advisory-removed-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored none
      of the delta (dispatched by the Mike-opened Fable review session, wt
      atelier-review-1017), on Mike's 2026-10-16 answer that a fresh Opus
      session writes these briefs; its exposure is disclosed in the brief. The
      pass stays queued for a further criterion-passing cold Fable session.
      `[~]` **CLAIMED 2026-10-17 2319 UTC for the review run** (a cloud
      session with no worktree: the container's one checkout, branch
      `claude/review-work-briefs-adj6ad`, landed on `main` by PR before any
      pass runs; brief `2026-10-17-0955-size-advisory-removed-cold.md`,
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
      - [ ] 🎯 **The pass RAN 2026-10-18 UTC; the cycle CLOSES on this pass (no
            MAJOR) — what remains is decided into the backlog.** The rule-4
            Fable cold pass (taker: a fresh `claude-fable-5-1` subagent under a
            `claude-fable-5-1` cloud orchestrator — the shape disclosed in the
            claim above; the sibling, the intent record and prior verdicts
            opened only after the phase-1 findings were committed, `5de15d6`)
            returned PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 4 minor ·
            7 note →
            [`2026-10-17-0955-size-advisory-removed-cold.md`](../../reviews/2026-10-17-0955-size-advisory-removed-cold.md)
            (sibling folded in and deleted). SZ1 (MODERATE): the docstring,
            README, CHANGELOG and commit body all say the only hatches that
            still exempt anything are an unscoped or `harvest-integrity`-scoped
            marker on an archive store, but a marker with any unrecognised
            scope also exempts the store's integrity check — silently, counted
            as an ordinary allow, at the delta's parent and at HEAD alike. SZ2
            (MODERATE): `RECORD.md` now names "review" as the detector for a
            flat-log regression where nothing reads the index for shape — a
            phrase the record shows came from the briefing the principal was
            given, so a one-line re-brief is owed alongside the rewording.
            SZ12 (note) and SZ13 (minor) formed at reconcile. Findings are the
            principal's to decide (rule 3); nothing was applied.
