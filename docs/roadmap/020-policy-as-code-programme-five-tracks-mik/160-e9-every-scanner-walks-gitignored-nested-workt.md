- [ ] **E9 — every scanner walks gitignored nested worktrees, and counts the
      repo twice.** Reported by `faves` 2026-08-15 under Track F
      (queue-never-deliver); **no fix, test or marker was written here**.
      A repo whose sessions take worktrees *inside* the tree —
      `.claude/worktrees/<name>/`, gitignored — gets a full second checkout of
      itself on disk. The scanners walk it, so an ad-hoc whole-repo run counts
      every finding once per live worktree. Measured in `faves` on 2026-08-15:
      `plainscan .` reported **2000** findings where the real tree had **623**;
      `pathscan .` reported 4 where 2 were real.
      **Why this is a Track E item and not cosmetic.** Two of the three effects
      are precision failures of exactly the kind this track exists for.
      **(1)** The inflated number is what a session quotes into a roadmap or a
      session log, so a wrong count enters the record as fact. This nearly
      produced a fabricated upstream defect report on 2026-08-15 — the reporter
      caught it only by re-running the way the floor invokes the scanner.
      **(2)** Root-relative `.<name>ignore` globs cannot match inside the nested
      copy, so a repo's own carefully-scoped allowances silently do not apply
      there. In `faves` this turned an **enforced** scanner loud: `leakscan .`
      reported **101 findings — commit blocked**, every one a venue address or
      phone already covered by `site/data/*` in `.leakscanignore`, and every one
      inside a sibling session's worktree. The tree itself is clean.
      **(3)** `sizescan` double-reports the same files in the hook's own output,
      which is where an adopter actually reads it.
      **What saves it today is accidental**: the pre-commit hook scans *staged*
      files, and the floor passes explicit paths — so neither plane sees this.
      Only the whole-repo run a session does at close sees it, which is the run
      most likely to be believed and least likely to be double-checked.
      **Suggested shape, not a prescription:** skip paths git itself ignores, or
      at minimum skip a directory containing a `.git` file (the worktree
      marker). `SKIP_DIR_NAMES` already carries `.git`, `node_modules` and
      `__pycache__` — this is the same class. Whether to skip *all* gitignored
      paths is a real decision: `pathscan`'s own docstring notes records
      legitimately name gitignored paths, and `faves` has `intake/` (gitignored
      owner source) that `wrapscan` flags today with 9 findings nobody can act
      on.
