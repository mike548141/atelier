# Sibling to the merge-hook-staged-scanners cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-merge-hook-staged-scanners-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `cd tools && python3 -m unittest test_precommit`: 23 tests, OK, exit 0 (Python 3.14.6).
- `python3 -m unittest discover -s tools -p test_spellscan.py`: exit 0 (Ran 87 tests).
- `python3 -m unittest discover -s tools -p test_wrapscan.py`: exit 0 (Ran 67 tests).
- `python3 -m unittest discover -s tools -p test_datescan.py`: exit 0 (Ran 96 tests).
- `python3 -m unittest discover -s tools -p test_reviewscan.py`: exit 0 (Ran 49 tests).
- `python3 -m unittest discover -s tools -p test_sizescan.py`: exit 0 (Ran 106 tests).
- `python3 tools/floor.py --plane hook --root .`: exit 0 (✅ licenscan enforced).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md`
- `docs/reviews/2026-10-28-1255-staged-positional-reader-topup-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `exec sh "$hook_dir/pre-commit"`: `$0` when a hook is invoked through a symlink, a worktree's
   `core.hooksPath` or a relative path. Does `dirname "$0"` find the sibling? Does the shipped
   `.githooks/pre-merge-commit` have its mode set?
2. Installation reach: `commands/install-hook.md` copies it, but a child whose `.githooks` is
   already stamped? `floorfleet` or `create-repo`'s stamp: what is the population that has it, and
   does anything report a child without it?
3. `git merge` when the merge is fast-forward, or with `--no-commit`, or an octopus: what runs? The
   table measured one git version.
4. Added-line filter plus whole-file context for fences: does `spellscan` read the fence state from
   the index copy or the disk? Partial staging with `git add -p`: which lines are "added" and do the
   numbers map to the index copy?
5. `reviewscan` and `sizescan` whole-file on the index: `staged_paths` filter is `ACMR`. A rename
   with no content change, a mode-only change, a deletion of a file whose absence is the defect (a
   deleted ADR's review line)? `D` is excluded.
6. Hook plane runtime: five more `git cat-file` readers per commit. On a big child's hook, the
   hook-time growth?
7. A blocking scan that used to read the disk and now reads only added lines: a defect already in a
   touched file no longer blocks. Is that a narrowing, was it ruled, and does CI cover it on every
   push in every child?
8. `staged_blob`'s `finally`: `proc.stdout.close()` before `proc.wait()` on a large blob; a consumer
   that stops reading early gets a SIGPIPE rc from git, and raises for a clean read?

## Facts held back from the brief

- `tools/test_precommit.py` fails to import on the system Python 3.9.6 here; passes on 3.14.
- `staged_blob` is the reader `secretscan`'s `--staged` body exemption later reuses (pass
  `160/1030`, whose verdict the brief-writer read).
