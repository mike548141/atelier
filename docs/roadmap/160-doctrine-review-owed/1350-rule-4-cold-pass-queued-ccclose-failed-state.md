- [ ] ⏳ **Rule-4 cold pass queued: `ccclose` names a `failed` agent as its own state (`210/400`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`, `instruments/man/ccclose.1` — the commit that closes `210/400`, on `main`.
      *Questions worth the pass's time:* whether a failed foreground agent is judged correctly before its tool result; whether the count of *failed* can mix agents with background commands.
      *Intent record:* `210/400`.
