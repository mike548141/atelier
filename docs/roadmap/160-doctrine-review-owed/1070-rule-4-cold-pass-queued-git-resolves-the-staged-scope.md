- [ ] ⏳ **Rule-4 cold pass queued: git resolves a staged scan's positional
      scope, and an unknown one is refused (`160/950`, QS1 applied).** The
      staged-positional reader every staged guard shares now asks git what a
      scope names. The authoring session (a principal-opened Opus 5.5 queue
      run, session 722ac2e2, 2026-11-09, in its ruling round, which
      dispatched the Sonnet worker that wrote it) queues this and does not
      take it.
      *Tier:* Fable, the principal-named review tier, checked at selection;
      the pass waits for his explicit permission for Fable work.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/report.py` (`resolve_staged_scope`),
      `tools/secretscan.py`, `tools/leakscan.py`, `tools/conflictscan.py`,
      `tools/floor.py` (comments), their tests and the five other scanners'
      scope tests, `tools/test_pins.py`, `tools/README.md`, `CHANGELOG.md` —
      the commit that applies `160/950`'s QS1, on `main`, 2026-11-09.
      *Questions worth the pass's time:* whether any spelling still lets a
      staged secret past (symlinks, submodules, a scope naming a removed
      directory); whether refusing an unknown scope can strand a child.
      *Intent record:*
      [`950-rule-4-cold-pass-queued-staged-positional-reader.md`](950-rule-4-cold-pass-queued-staged-positional-reader.md).
