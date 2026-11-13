- [ ] **A hook that checks, without the model having to remember, that a
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
