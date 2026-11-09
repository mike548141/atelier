# Sibling to the quiet-selftests cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-quiet-selftests-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_selftest_quiet.py`: exit 0 (Ran 11 tests).
- `python3 tools/board.py --selftest`: exit 0 (selftest OK — board).
- `python3 tools/conflictscan.py --selftest`: exit 0 (selftest OK — conflictscan).
- `python3 tools/datescan.py --selftest`: exit 0 (selftest OK — datescan).
- `python3 tools/pathscan.py --selftest`: exit 0 (selftest OK — pathscan).
- `python3 tools/sizescan.py --selftest`: exit 0 (selftest OK — sizescan).
- `python3 tools/spellscan.py --selftest`: exit 0 (selftest OK — spellscan).
- `python3 tools/stampscan.py --selftest`: exit 0 (selftest OK — stampscan).
- `python3 tools/wrapscan.py --selftest`: exit 0 (selftest OK — wrapscan).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

None found in the sweep.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `except BaseException` catches `SystemExit`. Does any selftest body call `sys.exit(0)` on
   success, so a pass prints `FAILED — <name> raised`? The eight here return an int, but is that
   pinned?
2. `redirect_stdout` captures Python-level writes only. A selftest that spawns a child process, or
   writes to `sys.__stdout__` or fd 1, still prints. Do any do so, in which case "nothing else"
   fails?
3. "Every scanner": the README sentence is universal. Run every tool's `--selftest` and count. The
   eight converted use `selftest OK — X`; others print `selftest OK` or `X selftest: OK`. Is the
   contract the sentence or the eight?
4. Does anything parse the old selftest output, in `floor.py`, a child's workflow or a fleet tool?
5. A failing selftest's output is now on stdout with a prefix. Could a fixture's secret-shaped
   sample reach a public CI log, and is that different from before?

## Facts held back from the brief

- The brief-writer ran every `tools/*.py --selftest` (Python 3.9): 25 printed one verdict line and
  `report.py` printed nothing. `coldsweep --selftest` printed 8 lines (exit 0; it is not a scanner
  in the floor's registry).
