---
action: start
description: Fork a new line of work into its own worktree.
argument-hint: "<branch>"
---

# Worktree — start

Drive atelier's worktree tool — the mechanical form of `CONCURRENCY.md`'s "one
worktree per line of work". It is zero-dependency stdlib Python, bundled in this
plugin at `${CLAUDE_PLUGIN_ROOT}/tools/worktree.py` — nothing to install. Run
from inside the target repo.

Fork `$ARGUMENTS` (a branch name) into its own worktree (default base
`~/worktrees`, which must be outside any cloud-synced folder):

```
python3 "${CLAUDE_PLUGIN_ROOT}/tools/worktree.py" start $ARGUMENTS
```

**Why worktrees** (say it back when a session starts write-heavy or multi-commit
work, or finds an uncommitted change it didn't make): a clean tree is *not* proof
you are alone; a disciplined parallel session commits small and leaves the tree
clean between commits. Take a worktree by default for write-heavy / multi-commit
work; reading needs no ceremony.
