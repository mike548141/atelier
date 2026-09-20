- [x] **E9 — every scanner walks gitignored nested worktrees, and counts the
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
      ---
      ✅ **FIXED 2026-09-20 across all eleven `_walk_files` copies.** A linked
      worktree's `.git` is a **file** (`gitdir: <path>`), not a directory, so
      `SKIP_DIR_NAMES`' name match never fired. Each copy's pruning line now
      also drops a directory containing a `.git` **file**. Checked by
      file-ness alone, not by parsing `gitdir:` — a bare file named exactly
      `.git` is never anything else, and this is the same name/type check
      `SKIP_DIR_NAMES` already makes rather than a new content decision. The
      accepted cost is documented and **tested** in all eleven: an ordinary
      file called `.git` prunes its parent too.
      📈 **Measured on atelier itself, which is the evidence this item never
      had.** Scanning the main checkout root while one harness worktree was
      live, same tree, same command, only the fix between:
      | | `pathscan --root . .` |
      |---|---|
      | before | **333 findings** |
      | after | **49 findings** |
      **284 of 333 were phantom — 85% noise**, every one of them a path inside
      `.claude/worktrees/<agent>/`. The child's report (`plainscan` 2000 vs
      623; `pathscan` 4 vs 2) is reproduced in the parent at larger scale.
      ⚠️ *Read the 49 correctly:* that is an **unscoped hand run**, wider than
      the surface `.atelier-floor.json` gates `pathscan` to. It measures the
      double-count removal, not atelier's real defect count — the floor
      answers that differently, and conflating the two is the error this
      session made once already tonight.
      🔎 **The brief this ran under carried a false premise, and the worker
      caught it.** The dispatch prompt asserted atelier's worktrees live
      outside the tree at `/Users/mike/worktrees`, so no difference should be
      expected here. Harness worktrees nest at `.claude/worktrees/`
      (`.gitignore`), which is a fact this estate already had written down.
      Had the worker accepted the premise it would have reported "no
      difference on atelier, as expected" — correct for its own leaf
      worktree, which has nothing nested *inside* it, and wrong about the
      repo. It flagged the contradiction as evidence rather than acting on
      it, and the orchestrator ran the main-root scan above. **A dispatch
      prompt's premises are inputs to verify, not givens.**
      **Verified:** independent nested repos (`.git` a directory) still
      pruned as before; hook plane (`--staged`, a git-diff path) and floor
      plane (explicit file arguments never reach `_walk_files`) both
      unaffected; all eleven scanners byte-identical on a tree with nothing
      nested. Full suite **1,564 tests OK** on the interpreter `115/210`
      names, with `gh` on `PATH`.
      🚩 **Out of scope and still open — the principal's, per this item's own
      text:** whether scanners should skip *all* gitignored paths. Records
      legitimately name gitignored paths (`pathscan`'s docstring), and a child
      has a gitignored `intake/` that `wrapscan` flags with findings nobody
      can act on. Deliberately untouched.
      🔑 *And this item is `115/080`'s fourth piece of evidence:* a one-line
      correction cost **eleven edits plus eleven test files**, which is
      exactly the signature Mike's own upstream test names.
      Rule-4 `⏳` at `160/410`; this run may not take it.
