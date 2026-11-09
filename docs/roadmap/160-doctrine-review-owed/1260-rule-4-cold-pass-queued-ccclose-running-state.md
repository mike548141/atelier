- [ ] ⏳ **Rule-4 cold pass queued: ccclose's fourth agent state, still running (`210/380`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/man/ccclose.1`, `instruments/ccclose.design.md` — the commit that closes `210/380`, on `main`.
      *Questions worth the pass's time:* whether the two freshness tests can read a dead agent as running past the stated bound; whether a run of the check under live workers stays honest.
      *Intent record:* `210/380`.
