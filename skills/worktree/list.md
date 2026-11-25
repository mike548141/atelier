---
action: list
description: Show every worktree with its hygiene flags.
---

# Worktree — list

Drive atelier's worktree tool — the mechanical form of `CONCURRENCY.md`'s "one
worktree per line of work". It is zero-dependency stdlib Python, bundled in this
plugin at `${CLAUDE_PLUGIN_ROOT}/tools/worktree.py` — nothing to install. Run
from inside the target repo.

```
python3 "${CLAUDE_PLUGIN_ROOT}/tools/worktree.py" list
```

Report the tool's output as it is.
