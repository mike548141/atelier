- [x] **`tools/worktree.py` resolves the branch from the cwd, not per-worktree.**
      Reproduced 2026-08-09, and the condition is the whole finding: run **from
      inside a linked worktree**, `list` labels that worktree's branch as `main`
      and drops its ahead/behind counts, and `land <feature>` fails
      `no worktree found`; run from the main checkout, both are correct. The
      branch itself is never wrong — `git branch --show-current` agrees
      throughout. *Superseded in its diagnosis on close: the cwd-dependent value
      was repo identity, not the branch.*
