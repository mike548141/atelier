- [ ] ⏳ **Rule-4 cold pass queued: the pre-flip gate additions and
      `publishscan --history` (`260/110`).** The run authored this itself
      (its dispatched worker's output counts as the run's authorship). It is
      queued at landing, and the run neither takes it nor spawns a reviewer
      for it. *Tier:* Fable, the principal-named review tier, checked at
      selection. *Pass type:* doctrine and code cold pass, per
      `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `docs/method/AUTONOMY.md`, `tools/publishscan.py`,
      `tools/test_publishscan.py`, `tools/README.md` and `CHANGELOG.md`, from
      `89ff0d8` to the merge that landed it on `main` on 2026-10-05.
      *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
      `[~]` **CLAIMED 2026-10-16-1548 UTC for brief-writing only** by a
      Mike-opened `claude-opus-5-5` session (queue run abe96d8d) that authored
      none of the delta, on Mike's 2026-10-16 answer that a fresh Opus session
      writes these briefs. The brief-writer does not run the review: the pass
      stays queued for a further criterion-passing cold Fable session once the
      brief lands.
