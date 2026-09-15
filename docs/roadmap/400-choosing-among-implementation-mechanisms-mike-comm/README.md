# Choosing among implementation mechanisms (Mike commissioned, 2026-09-16)

His words: *"There may be some value in defining in the doctrine when is the
appropriate situation to use code as policy, skills, custom built MCP's, or
other features of Claude."*

Checked before filing: **nothing in atelier answers this today.** `ADR 0006`
governs one narrower boundary — instruments vs estate/infra — and stays
scoped to it through all four addenda; it never generalises to mechanism
choice. `GUARDS.md` governs a guard *after* it exists (response, exemption),
not whether to build one. `ECONOMICS.md` has real criteria for one mechanism
only — when to reach for a sub-agent (§ *Sub-agents — isolation, not
savings*) — and nothing on skills, MCP servers, hooks or slash commands.
`050/010` is the one partial precedent — Mike's own captured idea to handle
one specific class (trust failures) "with a skill... not doctrine" — but it
is scoped to that one class and explicitly undesigned, not a general rule.

In practice the estate already uses four mechanisms — Python scanners wired
to hooks/CI (`tools/`), Claude Code Skills (`queue-run`,
`session-onramp`, `review-brief`, `create-repo`), slash commands
(`worktree`, `scan`, `fleet-pins`, `install-hook`), and Node/MCP-adjacent
instruments (`instruments/`) — with no custom-built MCP server and no custom
subagent definitions anywhere yet. Every choice among these so far is
precedent, made case by case, never written up as a rule a future choice can
be checked against.
