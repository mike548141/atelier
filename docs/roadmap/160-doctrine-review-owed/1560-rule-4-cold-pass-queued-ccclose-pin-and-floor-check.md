- [ ] ⏳ **Rule-4 cold pass queued: `ccclose` check 14, a child's atelier pin
      and floor copy (the `ccclose` half of `020/470`), and its session-open
      twin, the warn-only `SessionStart` hook `tools/floorhook.py`.** The authoring session
      (queue run 78ca9153, Opus 5.5, principal-opened, 2026-11-16 UTC, which
      dispatched the worker that wrote it) queues this and does not take it.
      *Tier:* Fable, the principal-named review tier, checked at selection; the
      pass waits for his explicit permission for Fable work.
      *Pass type:* cold pass on an instrument's new verdict policy, per
      `method/REVIEW.md` rule 4: it reads the principal's "fail noisy" into
      which states fail a close.
      *Delta, scoped to paths:* `instruments/ccclose`,
      `instruments/ccclose.test.js`, `instruments/man/ccclose.1`,
      `instruments/ccclose.design.md`, `instruments/README.md`: the commit that
      lands the `ccclose` half of `020/470`, on `main`; and `tools/floorhook.py`,
      `tools/test_floorhook.py`, `tools/README.md`: the later commit that closes
      `020/470` (built on the principal's answer *"Build the open hook
      (Recommended)"*).
      *What to test hardest:* the orchestrator's reading, applied by the
      worker, that "the safety rules are up to date" means the floor, not the
      pin: the check fails on a drifted copy or a moved floor and only warns on
      pin lag, because failing on lag would fail nearly every child close and
      push reflex bumps the doctrine forbids; "no result" is a warn, not a fail;
      `ccclose` now fetches `origin` in the atelier checkout, so it is no longer
      strictly read-only. For the hook: it must never block a session or read a
      failure to measure as current; it runs at every child session start on
      the principal's machine (measured 1.4–1.6 s), wired at user level.
