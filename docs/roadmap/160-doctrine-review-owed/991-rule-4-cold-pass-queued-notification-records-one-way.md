- [ ] ⏳ **Rule-4 cold pass queued: `cctranscript` reads a task notification
      the same way as an attachment record and as a user record, with no
      exchange number for the attachment (`210/260`).** `cctranscript`'s turn numbering and harness
      classification are what `ccclose` and the session records quote as
      refs. So the authoring session (a principal-opened Opus 5.5 queue run,
      session 4c65083c, 2026-11-03, which dispatched the Sonnet worker that
      wrote the code) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/cctranscript`,
      `instruments/cctranscript.test.js`, `instruments/ccclose.test.js`,
      `instruments/man/cctranscript.1`, `instruments/README.md`,
      `CHANGELOG.md` (the commit that closes `210/260`, on `main`,
      2026-11-03).
      *Intent record:*
      [`../210-instruments-open-features/260-notification-records-read-two-ways.md`](../210-instruments-open-features/260-notification-records-read-two-ways.md).
