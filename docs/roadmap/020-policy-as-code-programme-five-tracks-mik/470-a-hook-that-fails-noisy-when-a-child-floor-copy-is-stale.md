- [x] **A hook that checks, without the model having to remember, that a
      child's floor copy and pin are current, and fails noisy when they are
      not.** A hand-up from a private child, 2026-11-14, on the principal's
      instruction. Work to pick up under `020/460`; nothing here is designed
      or ruled beyond his words.

      **The principal's words, verbatim.** Asked whether the inlined floor
      breaks DRY, and given `PROPAGATION.md`'s reason (it binds even where
      atelier is never read; `pins.py` diffs every copy against the source),
      he said:

      > no that is fine but we might want a hook to confirm the safety rules
      > are up to date and fail noisy if not. Perhaps in a hook at session open
      > or build it into ccclose as a post tidy up

      **Why it is needed (evidence).** Today the drift check is a line in each
      child's `CLAUDE.md` that the model runs by hand at session start. An
      estate-wide sweep on 2026-11-13 found one child whose floor copy had
      drifted from atelier's text, caught only by a fleet run of `pins.py`.
      The floor-copy comparison is report-only until 2026-12-09 and runs at
      fleet level, not in a child's own CI (`PROPAGATION.md`).

      **Proposed (Claude's, not ruled).**

      - Mechanism: `pins.py --atelier <checkout> --child <repo>` already
        answers both questions (pin current, copy identical). Measured on the
        principal's machine: about 1.2 s including the fetch, exit 0 when
        current.
      - Two attachment points he named:
        - a `SessionStart` hook: cannot block, but its stdout reaches the
          model, so a stale result is impossible to miss; it costs about a
          second on every session, and a failed fetch must print "no result",
          never "current";
        - `ccclose`, as a step after the put-away: no cost at open, but the
          session has already worked on a stale floor by then.
      - Both, or the hook with `ccclose` as the backstop, are possible.
        `020/460`'s gaps apply: a hook fails open, can be switched off, and does
        not exist in a cloud session.
      **Progress, 2026-11-16 (UTC), queue run 78ca.** The `ccclose` half is
      built: check 14, "Atelier pin and floor copy current"
      (`instruments/ccclose`, tests in `instruments/ccclose.test.js`, man page
      and design note updated). In a child it runs `tools/pins.py --json --log
      --atelier <checkout> --child <repo>`: a current pin with an identical
      floor copy passes; a floor copy that differs, or a pin behind while the
      safety floor has changed since the pin, fails and `ccclose` exits 1 (a pin
      merely behind with the floor unchanged only warns: atelier moves daily and
      a bump is a deliberate read of the delta, not a reflex); ahead, diverged
      and unknown pins fail as integrity problems; any
      failure to get an answer (no checkout, failed fetch, 20 s timeout,
      unreadable output) is a warn that says "no result" with the reason, never
      "current". Atelier itself and non-children read "not a child". Still
      open, and the principal's to decide: the `SessionStart` hook half (it
      changes every session on his machine, and a hook fails open and does not
      exist in a cloud session, `020/460`).
      🔒 CLAIMED 2026-11-16T11:22Z (claimed 2026-11-16-1122, wt: qr-78ca-ccclose) by queue-run
      session 78ca9153 (Opus 5.5, principal-opened).
      💬 2026-11-16 UTC, the principal's answer to options offered (an answer,
      not a ruling), asked whether a hook should check the pin and floor copy
      at each session open as well as at close: *"Build the open hook
      (Recommended)"*. The option read: a warn-only SessionStart hook printing a
      loud line when the floor is out of date, about 1 s per child session.
      🔒 CLAIMED 2026-11-16T19:21Z (claimed 2026-11-16-1921, wt: qr-78ca-openhook) by
      queue-run session 78ca9153 (Opus 5.5, principal-opened).
      **Done, 2026-11-16 (UTC), queue run 78ca: the hook half.** `tools/floorhook.py`
      is a warn-only `SessionStart` hook that runs `pins.py` (still the only
      judge) and reaches the same verdicts as check 14: a loud line when the floor
      copy differs, or the pin is behind and the floor moved since it, or the pin
      is ahead, diverged, unknown or missing; one quiet line for a pin behind with
      the floor unchanged; one user-only line when current; silence for a repo that
      is not a child; and `no result: <reason>` for any failure to measure (no
      checkout, failed fetch, 10 s timeout, unreadable output), never "current". It
      always exits 0. Tests: `tools/test_floorhook.py` (20, synthetic fixtures);
      wiring and limits: `tools/README.md` section `floorhook.py`. Not wired: the
      orchestrator adds the user-level `hooks.SessionStart` entry, since a settings
      edit is the principal's machine, not a worker's.
