- [ ] **C4 — make the local bypass visible.** With CI as backstop rather than
      gate, `--no-verify` is the one route that reaches history unscanned, and
      nothing observes it. Idea: CI flags a pushed commit that would not have
      passed the hook, so a bypass is a recorded event rather than a private
      one. Weigh honestly against it also being the legitimate escape hatch —
      making it painful invites worse workarounds.
