- [ ] ⏳ **Rule-4 cold pass queued: one unambiguous review-pointer state
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
      `[~]` **CLAIMED 2026-10-16-1548 UTC for brief-writing only** by a
      Mike-opened `claude-opus-5-5` session (queue run abe96d8d) that authored
      none of the delta, on Mike's 2026-10-16 answer that a fresh Opus session
      writes these briefs. The brief-writer does not run the review: the pass
      stays queued for a further criterion-passing cold Fable session once the
      brief lands.
