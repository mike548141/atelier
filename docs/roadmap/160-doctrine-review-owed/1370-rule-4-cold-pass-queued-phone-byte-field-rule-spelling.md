- [ ] ⏳ **Rule-4 cold pass queued: `nz-phone` passes a bracketed byte field (`320/850`), and `secretscan`'s assigned rule takes both spellings (`320/840`).** The authoring session (a
      principal-opened Opus 5.5 queue run, session d0ca5d24, 2026-11-09 UTC,
      which dispatched the worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/leakscan.py`, `tools/secretscan.py`, their tests, `tools/README.md`, `CHANGELOG.md` — the commit that closes `320/850`, on `main`.
      *Questions worth the pass's time:* whether a real number can pass as a byte field; whether the second spelling can exempt a line it should not.
      *Intent record:* `320/850`, `320/840`.
