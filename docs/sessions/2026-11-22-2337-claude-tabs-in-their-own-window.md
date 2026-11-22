# 2026-11-22 23:37 UTC — Claude's browser tabs go in Claude's own window

Session 8abe2db0 (`atelier-6a`), primary checkout, inline. One ask.

**Ask.** A ruling for every session and repo, the principal, verbatim:
*"Unless I specify otherwise, when you open a web browser tab up you should do
it in a browser window that you are using, not the same window that I use for
my own tabs. To be clear you can have multiple tabs and tab groups in your
single window (we dont want too many windows)"*. He called it *"not a hard
rule"*, *"a tweak to help us better work together"*.

**Done.** Recorded in his user-level instructions (outside this repo, which is
where his working-style rulings live), in his words, beside his walk-through
rule. Mechanics checked against the Chrome extension's tools: each session gets
its own tab group, the first `tabs_context_mcp` with `createIfEmpty` makes it in
a new window, and no tool picks or moves a window. So the rule says: one shared
Claude window; if a group lands elsewhere, say so in one line and ask him to drag
it, never work around it. Sessions already live pick it up only on restart.

**Open.** Nothing.
