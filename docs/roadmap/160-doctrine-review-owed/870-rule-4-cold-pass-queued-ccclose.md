- [ ] ⏳ **Rule-4 cold pass queued: `ccclose`, the close-out checker
      (`020/180`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and
      the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
      the principal-named review tier, checked at selection. *Pass type:*
      code and design cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
      paths:* `instruments/ccclose`, `instruments/ccclose.test.js`,
      `instruments/ccclose.design.md`, `instruments/man/ccclose.1` and
      `instruments/README.md`, commits `ef3673a` and `4eda680` and their merge,
      and the `TOOLBOX.md` expected-toolbox row that names it (the close
      commit), landed on
      `main` on 2026-10-16.
      *Intent record:*
      [`../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md`](../../sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md).
      **Brief WRITTEN 2026-10-17, review NOT run** —
      `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored none
      of the delta (dispatched by the Mike-opened Fable review session, wt
      atelier-review-1017), on Mike's 2026-10-16 answer that a fresh Opus
      session writes these briefs; its exposure is disclosed in the brief. The
      pass stays queued for a further criterion-passing cold Fable session.
      `[~]` **CLAIMED 2026-10-17 2319 UTC for the review run** (a cloud
      session with no worktree: the container's one checkout, branch
      `claude/review-work-briefs-adj6ad`, landed on `main` by PR before any
      pass runs; brief `2026-10-17-1010-ccclose-close-checker-cold.md`,
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
