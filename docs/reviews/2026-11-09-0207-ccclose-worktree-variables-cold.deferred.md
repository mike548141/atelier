# Sibling to the ccclose-worktree-variables cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-ccclose-worktree-variables-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `node --test instruments/ccclose.test.js`: exit 0 (ℹ duration_ms 214628.846232).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`
- `docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. A dropped add leaves the close check blind to a real worktree. Later `03d8503` counts the
   unresolved. At these two commits, does anything say an add was dropped? A guess is prevented, a
   silence is not.
2. The transcript-wide variable map: a variable assigned in one shell command and reused in a later
   one that ran in a fresh shell (the Bash tool does not persist env). Is the map then stale, so a
   path is confidently wrong?
3. `a.at < m.index` and the `[;&|\n]` test: an assignment inside a subshell, an `if`, a `for`, or a
   pipeline; one reassigned after use; `export`; quoting. Does any give a path that was not the one
   used?
4. `$HOME`, `~` and `${VAR:-default}` in `expandVars`: which are literal, and which guess?
5. The window: the committer date of a rebase is the rebase's. A session that only rebases others'
   commits is credited with them. Is that named beside the heuristic?

## Facts held back from the brief

- Later commits touch the same file (`1569e64`, `3de818b`, `03d8503`, `5f7c2b0`, `457f374`,
  `4e3b398`); three are under their own passes.
