# Sibling to the leakscan-off-rules cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_leakscan.py`: exit 0 (Ran 395 tests).
- `python3 tools/leakscan.py --selftest`: exit 0 (selftest OK).
- `cd tools && python3 -m unittest test_floor`: 187 tests, OK, exit 0 (Python 3.14.6).
- `python3 tools/floor.py --plane ci --root .`: exit 0 (Python 3.14.6), `leakscan advisory: 3
  finding(s)`.
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-07-29-1243-e6-intent-cold.md`
- `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. EI6 said no advisory form because a leak cannot be rotated. An off rule that now reports prints
   the matched personal data into CI logs and a board count: a public repo's log, for a rule the
   repo chose to turn off. Does "report" create the exposure EI6 was protecting against? What does
   the output print: value, redacted, or none?
2. The withdrawn `diagnosis-key` rule reports across repositories. At 11 and 2,652 findings, is a
   count nobody acts on "cover, not coverage" (EI1), and is the board's count the consumer EI1 asked
   for?
3. `BlockingSetPinned` lists fifteen rules. Is the list derived, or hand-kept so a new rule escapes
   it?
4. `blocks(rule, disabled)` is "the single decision". Is it the only path, or can a finding
   constructed elsewhere reach the report with no response?
5. `--disable` is a flag in `.atelier-floor.json`: can a child now disable a blocking rule more
   cheaply because it "still reports", so the tier makes a narrowing feel safe?
6. The MAC duplicate in § 5 is named. What other double-counts does the shadow asymmetry make?
7. The ruling's authority chain: the first answer was given before EI6 was shown. Read the question
   text at phase 2 against `00-APEX.md`'s informed-ruling test.

## Facts held back from the brief

- At this HEAD the ci plane prints `leakscan advisory: 3 finding(s)` on this repo, all
  `diagnosis-key` shape.
- `tools/test_floor.py` fails to import on the system Python 3.9.6 here; passes on 3.14.
