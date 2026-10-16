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
      **Brief WRITTEN 2026-10-16, review NOT run** —
      `docs/reviews/2026-10-16-1551-pre-flip-gate-history-cold.md` with a
      `.deferred.md` sibling. Written by an Opus brief-writer that authored
      none of the delta (queue run abe96d8d), on Mike's 2026-10-16 answer that
      a fresh Opus session writes these briefs; its exposure is disclosed in
      the brief. The pass stays queued for a further criterion-passing cold
      Fable session.
