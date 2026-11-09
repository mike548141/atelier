# Sibling to the orchestrator-writes-the-pointer cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-orchestrator-writes-the-pointer-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 tools/pointerscan.py --selftest`: exit 0 (pointerscan selftest: ok (0 failure(s))).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

None found in the sweep.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. "A hash it cites must already be the one on `main`": the landing commit cannot name its own hash.
   Is the rule followable for the pointer's most natural citation, and does the path-and-item form
   then carry the whole load?
2. `REVIEW.md` rule 4 makes "the author" queue the pointer and says the author runs `pointerscan` on
   it, "the one reader who can act on the warning for free". When the orchestrator writes it, who
   runs pointerscan, and does rule 4's text still read true (V3, V5)?
3. Does the rule reach a worker that lands its own work, a single-session build, and a child that
   has no orchestrator? Is "the worker" scoped?
4. Mirror sites (V3): `skills/queue-run/`, the plugin's commands, and any child template that tells
   a worker to queue its own `⏳`.
5. "By the item it closes" fails if a commit closes several items, or if an item is reopened. Does
   the form name one commit?

## Facts held back from the brief

- Live instance of the class, same repo: board item `160/990` cites `29021b9`, a pre-rebase hash
  that is not on `main`; the landed commit is `2ba261b`. That pointer predates this rule by hours.
