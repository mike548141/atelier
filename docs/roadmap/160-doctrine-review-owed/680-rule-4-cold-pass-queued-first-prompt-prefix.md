- [ ] ⏳ **Rule-4 cold pass queued: cctranscript's first-prompt prefix read
      (`210/180`).** The run authored this itself (its dispatched worker's
      output counts as the run's authorship). It is queued at landing, and the
      run neither takes it nor spawns a reviewer for it. *Tier:* Fable, the
      principal-named review tier, checked at selection. *Pass type:* code
      cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to paths:*
      `instruments/cctranscript` and `instruments/cctranscript.test.js`,
      merge `89a7539` and the commit after it. It landed on `main` on
      2026-10-05. *Intent record:*
      [`../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md`](../../sessions/2026-10-05-1120-queue-run-closes-and-builds.md).
