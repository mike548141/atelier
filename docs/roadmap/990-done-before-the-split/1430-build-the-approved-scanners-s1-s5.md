- [x] **Build the approved scanners S1–S5** — ALL FIVE BUILT + wired advisory.
      S2+S4 landed 2026-07-23 (queue run 0959): **S2 `pathscan`** (`b738f21`,
      merged) — bare-prose/backtick repo-path resolution, the half linkscan's
      markdown-link resolution can't see (triple-anchor: root / own-dir /
      outermost-`docs`-ancestor; 53 tests; 174-finding heuristic-noise baseline
      by design); **S4 `stampscan`** (`2fe97f3`, merged) — a new mechanism
      comparing an inlined-floor stamped block to its pinned canonical parent
      region (`stamp:begin source=… region=…` HTML-comment markers, wired to the
      real templates/CLAUDE.md↔PROPAGATION.md floor pair, byte-identical → CLEAN;
      46 tests; `narrow=<reason>` distinguishes a declared narrowing from a silent
      drop). Both Sonnet-built, Opus-verified, ship ADVISORY (`--warn` in
      `ci.yml`, absent from hook + `floor.yml` per don't-stack). Combined suite
      601 green. S1/S3/S5 built earlier (`72e8ecb`/`6077972`/`760260473`). Each
      of S2/S4 earns a queued ⏳ first-of-kind rule-4 review (live in ROADMAP.md)
      before any gate.
