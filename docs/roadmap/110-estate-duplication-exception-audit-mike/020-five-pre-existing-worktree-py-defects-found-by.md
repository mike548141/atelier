- [ ] 🔎 **Five pre-existing `worktree.py` defects, found by that fix and
      deliberately left** (2026-08-09). Queued rather than taken because each is
      outside the two claimed items and one of them changes a documented meaning:
      (a) **`list`'s ↑/↓ carries the same stale-local-`main` referent** `remove`
      just lost, so a landed branch shows `↑N` forever — fixing it changes what
      "behind" *means* on this board, which is its own call;
      (b) **`cmd_land` breaks on a detached worktree** exactly as `remove` would
      have, sending the literal `"HEAD"` to `git push -u origin HEAD` and
      `gh pr create --head HEAD`;
      (c) **`land`'s no-remote hint derives the feature slug as
      `branch.split('-')[-1]`** — for `queue-batch-0809-0813` it prints
      `worktree remove 0813`, a command that resolves nothing, when the slug is
      knowable from the directory name;
      (d) **harness worktrees under `.claude/worktrees/` cannot be addressed by
      slug at all** — they are named `<feature>`, not `atelier-<feature>`, so
      `land`/`remove` can never resolve one, while `list` shows it fine. This is
      the same nesting that makes `git add -A` unsafe here;
      (e) **`worktree.py` carries pre-existing 101-column lines** that nothing
      flags, because `wrapscan` is scoped away from `tools/` — a live instance
      of the cover the scope declaration in `.atelier-floor.json` now states it
      gives up.
