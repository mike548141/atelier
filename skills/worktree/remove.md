---
action: remove
description: Remove a worktree, guarded against unmerged work.
argument-hint: "<branch>"
allowed-tools: Bash(python3:*), Bash(git:*)
---

# Worktree — remove

Drive atelier's worktree tool — the mechanical form of `CONCURRENCY.md`'s "one
worktree per line of work". It is zero-dependency stdlib Python, bundled in this
plugin at `${CLAUDE_PLUGIN_ROOT}/tools/worktree.py` — nothing to install. Run
from inside the target repo.

```
python3 "${CLAUDE_PLUGIN_ROOT}/tools/worktree.py" remove $ARGUMENTS
```

A guarded `remove` that refuses is protecting unmerged work, not failing; say
so and stop rather than forcing it.
