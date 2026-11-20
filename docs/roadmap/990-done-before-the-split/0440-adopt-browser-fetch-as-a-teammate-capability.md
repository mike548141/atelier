- [x] **Adopt browser-fetch as a teammate capability** — DONE 2026-07-12 (Opus,
      session 41). The first **capability** instrument: a Chrome-driving MCP
      server (fresh headless, or the operator's own Chrome over CDP for
      captcha/Cloudflare) for when `WebFetch`/curl are blocked. ADR 0006 got an
      addendum — `instruments/` widens to admit tools that **extend the
      teammate's reach**, not only observe; the zero-dep ethos flexes for a
      capability tool whose value needs deps (pinned `requirements`/`constraints`,
      a regenerable venv OUTSIDE the repo/iCloud, code versioned in-repo).
      `instruments/browser-fetch/` holds the **scrubbed** `server.py` (every
      "Mike" → operator, pre-SDK/machine history removed before this public repo),
      pinned deps, a reproducible `setup`, and a README. Proven end-to-end after
      setup (`browser_fetch` returned a rendered page; both tools register); MCP
      registration repointed to the atelier location. Not CI-unit-tested (a
      browser is disproportionate in CI); floor scanners cover `server.py`, live
      use verifies. **Confirmed + cleaned up 2026-07-12:** a fresh parallel
      session ran `browser_fetch` end-to-end against the re-registered server
      (example.com → 200; httpbin User-Agent showed `HeadlessChrome/149` — real
      Chrome), so the old `~/.claude/mcp-servers/browser-fetch` was deleted.
