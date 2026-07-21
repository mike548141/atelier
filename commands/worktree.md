---
description: One worktree per line of work — start / list / land / remove worktrees (CONCURRENCY.md as a command).
argument-hint: "start <branch> | list | land <branch> | remove <branch>"
allowed-tools: Bash(python3:*), Bash(git:*)
---

Drive atelier's worktree tool — the mechanical form of `CONCURRENCY.md`'s "one
worktree per line of work". It is zero-dependency stdlib Python, bundled in this
plugin at `${CLAUDE_PLUGIN_ROOT}/tools/worktree.py` — nothing to install.

**Why worktrees** (say it back when a session starts write-heavy or multi-commit
work, or finds an uncommitted change it didn't make): a clean tree is *not* proof
you are alone; a disciplined parallel session commits small and leaves the tree
clean between commits. Take a worktree by default for write-heavy / multi-commit
work; reading needs no ceremony.

Run from inside the target repo. Pass `$ARGUMENTS` through to the subcommand:

- **start `<branch>`** — fork a new line of work into its own worktree (default base
  `~/worktrees`, which must be outside any cloud-synced folder):
  `python3 "${CLAUDE_PLUGIN_ROOT}/tools/worktree.py" start <branch>`
- **list** (`ls`) — show worktrees + hygiene flags:
  `python3 "${CLAUDE_PLUGIN_ROOT}/tools/worktree.py" list`
- **land `<branch>`** — push the branch + open a PR back to main:
  `python3 "${CLAUDE_PLUGIN_ROOT}/tools/worktree.py" land <branch>`
- **remove `<branch>`** (`clean`) — remove a worktree (guarded against unmerged
  work): `python3 "${CLAUDE_PLUGIN_ROOT}/tools/worktree.py" remove <branch>`

If `$ARGUMENTS` is empty, run `list` and show the current state. Report the tool's
output honestly — a guarded `remove` that refuses is protecting unmerged work, not
failing; say so and stop rather than forcing it.
