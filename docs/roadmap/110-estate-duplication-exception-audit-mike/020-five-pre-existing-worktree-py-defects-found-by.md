- [x] 🔎 **Five pre-existing `worktree.py` defects, found by that fix and
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

  - [x] ✅ **(b)–(e) FIXED 2026-09-18** (`3635fc1`, merged from
        `worktree-defects-0918`): `land` refuses a detached worktree and points
        at `git switch -c`; the no-remote hint names the real feature slug;
        `_feature_worktree()` also resolves harness worktrees
        (`.claude/worktrees/<feature>/`), prefixed form checked first; the
        101-column line wrapped. One test per defect.
  - [ ] 🎯→✅ **(a) RULED 2026-09-18 by Mike, via the question device:**
        *"Compare to origin/main"* — the ahead/behind arrows measure against
        what is published, not a possibly stale local `main`. Build owed;
        claimed below with this ruling as its spec.

  - [x] ✅ **(a) BUILT 2026-09-18 on Mike's ruling** (`50fef74`, merged from
        `worktree-referent-0918`): `worktree list` measures ahead/behind
        against `origin/<main>`, prints the referent and how old the last
        fetch is, falls back to local `main` with a ⚠ saying so when there is
        no remote-tracking ref, and takes `--fetch` to refresh first (off by
        default, keeping `list` offline-safe). All five defects now closed.
