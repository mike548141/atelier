- [~] 🔎 **`ccclose` counts a resumed session's own MCP server as live launched work, so
      🔒 Claimed by session 4c77ea94 (`atelier-73`, Opus 5.5), principal-opened by
      `/atelier:work run`.
      (claimed 2026-11-28-1439, wt: atelier-qr-4c77-ccclose-mcp)
      the close reads ❌ over a process the session did not start** `[S][tool]`. Found
      2026-11-27 by session a2097e54 (`atelier-b2`) at its close. *Launched work finished*
      reported `live process: pid … · Python …/instruments/browser-fetch/server.py`, "carries
      this session's id; stop it by its pid". It is a direct child of the session's own
      `claude` process: the harness started it as an MCP server. Two conditions in the
      helper exclusion (`instruments/ccclose`, the `helper` set) both miss it:
      1. *Started before the first prompt*: the session was resumed after an editor crash,
         so its harness process and helpers started ~11 h after the transcript's first
         prompt, which is the time the test compares against.
      2. *Named as MCP* (`MCP_CMD`): the server's command line is `Python …/server.py`, with
         no `mcp` word in its first four argv words.
      **Owed:** judge "early" against the current harness process's own start, not the
      transcript's first prompt (a resumed session has a new harness), or read the
      harness's MCP config for its server commands; a test with a resumed session's
      timings. Until then the line is named at close, not fixed by killing the server.
      **Not fixed in passing:** filed under `CLAUDE.md`'s rule that a tool defect is
      reported first.
