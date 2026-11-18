- [ ] ⏳ **Rule-4 cold pass queued: `secretguard`, `deadhook`, `stashscan`,
      `treeline` and `pins.py --floor` (`450/010` rows 6–10).** A hook that
      denies Bash commands, a line every child's floor run now prints, and a
      new verdict mode on the pin tool, built by workers of session
      84b7932e (Opus 5.5, principal-opened, 2026-11-18), which queues this
      and does not take it or brief it.
      *Tier:* the principal-named review tier, checked at selection.
      *Pass type:* code cold pass, per `method/REVIEW.md` rule 4.
      *Delta, scoped to paths:* `tools/secretguard.py`,
      `tools/test_secretguard.py`, `tools/deadhook.py`,
      `tools/test_deadhook.py`, `commands/install-hook.md`,
      `tools/stashscan.py`, `tools/test_stashscan.py`, `tools/treeline.py`,
      `tools/test_treeline.py`, `tools/floor.py`, `tools/pins.py`,
      `tools/test_pins.py`, `docs/method/CONCURRENCY.md`,
      `docs/method/GUARDS.md`, `tools/README.md`, `CHANGELOG.md` (commits
      `262658e0`, `cdfadc75`, `ef4972e6`, `603378f4`, on `main`,
      2026-11-18).
      *Intent record:*
      [`../450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md`](../450-one-home-and-one-command-prefix-mike-commissioned/010-one-command-prefix-and-the-homing-sweep.md).
      No brief yet: a brief-writer that is not session 84b7932e writes it.
      **Drain priority: low (principal, 2026-11-18).**
