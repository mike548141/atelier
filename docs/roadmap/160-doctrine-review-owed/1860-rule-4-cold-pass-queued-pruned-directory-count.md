- [ ] ⏳ **Rule-4 cold pass queued: the plain-tree walk counts what it prunes, and two
      scanners warn on it (`320/900`).** The authoring session (f8dd3843, `atelier-31`,
      Opus 5.5, principal-opened by `/atelier:work run`, whose Opus worker wrote it) queues this
      and neither briefs nor takes it.
      *Tier:* Fable, the principal-named review tier, checked at selection; it runs only on
      his approval (the general Fable hold).
      *Pass type:* code, per `method/REVIEW.md` rule 4: a change to the walk every scanner
      shares. Can the count be wrong in the direction that hides files (a floor reported as
      exact, a git-mode zero passed off as measured), and is git mode's yielded set truly
      unchanged?
      *Delta, scoped to paths:* `tools/filewalk.py`, `tools/report.py`, `tools/secretscan.py`,
      `tools/leakscan.py`, their tests, `tools/README.md`, `CHANGELOG.md`: every commit on
      `main` after `ddba7cde` up to and including the commit that lands this pointer.
      *Intent record:*
      [`../320-child-filed-findings-via-pointing-up/900-hand-up-scanner-walk-prunes-directories-uncounted.md`](../320-child-filed-findings-via-pointing-up/900-hand-up-scanner-walk-prunes-directories-uncounted.md).
