- [x] **`--no-verify` is the real hole, and nothing sees it.** With CI as a
      backstop rather than a gate (see the ranked residual, item 2), a local
      bypass is the one route that reaches history unscanned. I used it twice in
      one night. Idea: make it *visible* rather than impossible — e.g. CI flags a
      pushed commit that would not have passed the hook, so a bypass is a
      recorded event rather than a private one. Worth weighing against the
      obvious counter: it is also the legitimate escape hatch, and making it
      painful invites worse workarounds.
      ✅ CLOSED 2026-11-16 UTC as a duplicate of `020/100` (C4 — make the
      local bypass visible), which states the same hole and the same idea;
      the work stays open there. Closed by queue run 78ca9153.
