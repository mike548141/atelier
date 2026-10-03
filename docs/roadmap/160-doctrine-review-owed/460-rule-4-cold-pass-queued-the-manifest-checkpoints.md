- ⏳ **Rule-4 cold pass queued: ccarchive's manifest checkpoints and
      stale-entry heal (`210/170`).** The run authored this itself (its
      dispatched workers' output counts as the run's authorship). It was
      queued at landing, and the run neither takes it nor spawns a reviewer
      for it. *Tier:* Fable, the principal-named review tier, checked at
      selection. *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccarchive`,
      `instruments/ccarchive.test.js` and `instruments/man/ccarchive.1`. It
      landed on `main` on 2026-10-03, in merge `0264387`.
      *Intent record:*
      [`../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`](../../sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md).
