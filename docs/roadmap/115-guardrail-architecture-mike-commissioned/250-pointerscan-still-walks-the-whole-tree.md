- [x] 🔎 **pointerscan still walks the whole tree, harness worktrees included**
      `[S][tools]`. Found 2026-10-05 by a queue run's hand run of
      `pointerscan --root . .` at the primary checkout. It reported four
      findings, every one from a sibling session's linked worktree under
      `.claude/worktrees/`: that worktree's copy of an item, not this tree's.
      Its file discovery is a bare `rglob("*.md")` with a short skip list,
      so it never got `110/110`'s fix (guards walk only what git could
      commit) or `020/160`'s linked-worktree skip. `reviewscan`,
      `blockscan` and `harvestscan` were checked the same way and showed no
      worktree paths. CI is unaffected, because a CI checkout has no nested
      worktrees. The hook plane reads staged files. So the harm is a hand
      run or a session's own check counting other sessions' items, which is
      the miscount `130/020` exists to prevent.
      **The work:** route pointerscan's directory walk through the shared
      `tools/filewalk.py` (or the tracked-file listing the other guards
      use), with a test that a linked worktree nested in the root is not
      read.

      ✅ **Fixed and merged 2026-10-05** (queue run, a Sonnet 5.5 worker;
      `602e95a`). `roadmaps()` now walks a directory argument through the
      shared `filewalk.walk_files` with pointerscan's own skip set, as
      `datescan` and `linkscan` do. It inherits `110/110`'s git-could-commit
      rule and `020/160`'s linked-worktree prune, with no variant of its own.
      Explicit file arguments are unchanged. **Evidence:** output was
      byte-identical, old against new, on a git-initialised copy and a non-git
      copy (text, `--json` and `--root . .`). A nested linked worktree added
      one finding under the old code and none under the new. Five regression
      tests mirror the other guards' linked-worktree tests, and the two that
      matter fail against the old code. The full Python suite passed: 1,714
      tests OK. The orchestrator re-ran `test_pointerscan` on the merged tree,
      and a hand run at the primary checkout no longer reports sibling
      worktrees' items. One judged difference: skip names are now matched
      below the scanned directory only, as in every other guard, and this
      changes nothing on a normal tree. No rule-4 pass is queued: this is a
      one-guard application of an already-reviewed shared walk, and
      `160/690`'s pass covers pointerscan's current code.
