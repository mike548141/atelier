# Sibling to the dispatch-brief-shared-surfaces cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-dispatch-brief-shared-surfaces-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 tools/pathscan.py --root . docs/method/session-open/dispatch-brief.md`: exit 0
  (suppressed: 0 by allow-marker · 0 file(s) by .pathscanignore · 0 rec).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

None found in the sweep.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `git commit -- <paths>` with a partially staged path: does it commit the staged or the working
   content (it commits working-tree content for named paths), and does the rule warn? Does the
   pre-commit hook then read the right index? `GIT_INDEX_FILE` is a temporary index in this mode.
2. The skeleton says "never edit the shared primary checkout" and "commit by pathspec", while the
   rule says a claim must still be committed in the shared checkout. Is the skeleton's bound true
   for an orchestrator-side worker?
3. `dispatch-brief.md` "holds no rule of its own". Is every bound actually in `CONCURRENCY.md`, and
   did any line strengthen its grounding (V4, V5)? Walk the table.
4. A worker told to use a scratch path "unique to this worker": the rule that held-back notes never
   live in the scratchpad (`d7abac1`). Reconcile.
5. "Reads every brief in full before it lands": a review brief's deferred sibling is held from the
   reviewer, but does the orchestrator reading it break a partition rule 1 relies on?
6. The triage's categories: are they exhaustive and disjoint, and who judges "progressable"? Does it
   interact with "a stopped run reports its count" elsewhere?
7. `lsof -p <pid> -d cwd` for the kill scope: is that what the rule means, and does it work for a
   process whose cwd was deleted?

## Facts held back from the brief

- Nine items landed in one commit; each intent record's landing note says the commit closes it.
