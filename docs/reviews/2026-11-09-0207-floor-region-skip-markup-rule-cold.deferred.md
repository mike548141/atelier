# Sibling to the floor-region-skip-markup-rule cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-floor-region-skip-markup-rule-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_pathscan.py`: exit 0 (Ran 154 tests).
- `python3 -m unittest discover -s tools -p test_conflictscan.py`: exit 0 (Ran 84 tests).
- `python3 tools/pathscan.py --selftest`: exit 0 (selftest OK — pathscan).
- `python3 tools/conflictscan.py --selftest`: exit 0 (selftest OK — conflictscan).
- `python3 tools/conflictscan.py --root . . --json`: exit 0 (}).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-16-1510-expected-toolbox-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The skip keys on the file's absence: a child that holds a `docs/method/PROPAGATION.md` of its
   own, or a parent that deletes it. Does the test then flip for reasons nothing states?
2. Who checks the skipped block if `stampscan` is warn-only or disabled in a child? The docstring
   says "not silent": is that true on every plane and for a child that disables it?
3. A child's own text placed inside the stamp markers, with a bad path: skipped silently. An
   unterminated `stamp:begin` near the top of a long file skips the rest. Does stampscan run on
   every file pathscan does?
4. `clean: not findings and not blocking_total and not advisory_total`: the docstring says `clean`
   keeps its meaning. Did it? A consumer gating on `clean` sees a new false.
5. The `.conflictscanignore` entries exempt two frozen records from conflict-marker checks too,
   which the comment names. Is that hole proportionate, given the rule is advisory and an
   allow-marker cannot be added?
6. `TOOL_CLOSE_RX` needs the whole line; an indented or fenced quote of the markup? `TOOL_OPEN_RX`
   has no end anchor: prose or docs that start a line with `<parameter name=`? The doctrine about
   this tool does that.
7. The cap accounting (`advisory_over_cap`): can a flood of advisory findings consume the shared
   materialisation budget, so a real conflict marker is counted but never listed?

## Facts held back from the brief

None.
