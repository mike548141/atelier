- [x] **cctranscript — per-reply response IDs (`N.M`)** — DONE 2026-07-11.
      Both open decisions taken and stated in the code: a "reply" is a **text
      reply only** (the unit a human cites; thinking/tool turns stay
      unnumbered even under `--full` — clutter loses), and `--json` carries a
      `ref` field on every turn (`"1"` on prompts, `"1.2"` on replies, null on
      think/tool/result) so citations are machine-addressable. Header shows
      `◂ Claude 1.1 (Opus 4.8)`; a reply before any prompt (resumed session)
      numbers under exchange 0, honestly marking its prompt isn't in the log.
      `numberTurns()` pure + unit-tested; `--json` contract test asserts the
      ref scheme; driven live.
