- [ ] ⏳ **Rule-4 cold pass queued: `ccclose` counts a subagent's background shells, and
      the dispatch rules say a worker's wait must be able to end (`210/690`).** The
      authoring session (a2097e54, `atelier-b2`, Opus 5.5, principal-opened by
      `/atelier:work run`, whose Sonnet worker wrote it) queues this and neither briefs nor
      takes it.
      *Tier:* Fable, the principal-named review tier, checked at selection; it runs only on
      his approval (the general Fable hold), at the next drain by default (`460/060`).
      *Pass type:* code and doctrine, per `method/REVIEW.md` rule 4: a close check every
      session trusts to say nothing it launched is still running, and a bound every
      dispatch carries.
      *Delta, scoped to paths:* `instruments/ccclose`, `instruments/ccclose.test.js`,
      `instruments/ccclose.design.md`, `instruments/man/ccclose.1`,
      `docs/method/CONCURRENCY.md`, `docs/method/session-open/dispatch-brief.md`,
      `CHANGELOG.md`: every commit on `main` after `6051b8a8` up to and including the
      commit that lands this pointer.
      *Intent record:*
      [`../210-instruments-open-features/690-worker-background-waits-never-end-and-ccclose-misses-them.md`](../210-instruments-open-features/690-worker-background-waits-never-end-and-ccclose-misses-them.md).
