# Sibling to the licenscan advisory-tier cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0955-licenscan-advisory-tier-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board item (title line seen, never read whole): `115/290` (three guard
  descriptions disagree with their own code). Filed at the same merge: `115/320` (three small
  gaps in the floor's tests and count contract), which `dc0ed0e` then addressed.
- The landing commit's message body (read by the brief-writer): the docstring and README called
  a permissive-into-permissive mix or an unknown declaration a "warn: friction, never a silent
  pass" while the code made every one count toward exit 1; it quotes Mike's 2026-10-16 answer on
  115/290, "make the warning real"; it says a severity not named advisory blocks so the tier is
  opt-in; floor gains licenscan as a count-carrying check with `advisory=None` kept; pathscan's
  docstring said it was not in the registry though it has been since 2026-08-05; `Scanner`'s
  docstring said boundary checks have no advisory form "by design" while publishscan carries one
  as an adoption aid. It claims nine new licenscan tests (eight fail on the old code), three floor
  contract tests, and an estate blast radius of 29 repos: six red to green, none the other way,
  two still red on high findings.
- `dc0ed0e`'s message body (read by the brief-writer, another pass's subject): the count pattern
  was unanchored and a file named like the count line made the board read a count off a blocking
  finding, reproduced against secretscan; the pattern is now built per scanner and must be the
  whole line.
- The merge `6acefc9` changed "2026-10-17" to "2026-10-16" in two places in the delta (the
  README's section heading and the "Until …" sentences).

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-08-06-0903-licenscan-e1e2-cold.md`
- `docs/reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md` — secretscan's advisory
  tier, the model this delta cites
- `docs/reviews/2026-07-28-1204-c1-advisory-cold.md`

## The pointer's own lens hints

None beyond "its dispatched worker's output counts as the run's authorship". Refs-only.

## Overlap with sibling passes of this batch

- 160/860 (`dc0ed0e`) rewrites the floor's count reader this delta first used, and pins
  licenscan as unsoftenable in tests. A defect in the count reader at HEAD is 860's; a defect in
  the count line licenscan prints, or in the contract as `e3e8a4f` landed it, is this pass's.
- 160/830 (`f4afb7a`) and 160/850 (`72a68cc`) share the base and edit `tools/README.md`;
  160/850 also edits `tools/test_report.py`.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. An unrecognised LICENSE body and an unrecognised declaration are now advisory. Could a repo
   carry a copyleft licence the scan cannot name (a `LicenseRef-`, a dual expression, an
   unfamiliar SPDX id) and pass a publish gate at exit 0? Was that class moved knowingly?
2. The fix chose to make the code match the prose. The prose said "never a silent pass"; is an
   exit-0 advisory in CI output a silent pass in practice for an unattended run?
3. `advisory=None` (a child may not soften) and `advisory_count=True` (the check reports some
   findings without blocking) now sit side by side on two scanners. Does any surface a person
   reads tell those apart, or does "unsoftenable" now mean less than it did?
4. As landed at `e3e8a4f`, was the count line forgeable by a file path in the same output (the
   defect `dc0ed0e` later fixed for secretscan)? If so, the delta shipped a known-shape hole that
   a later commit closed; say which commit carries it.
5. The publishscan sentence added to `floor.py` describes a boundary check that IS softenable.
   Is that a correction of a docstring, or a change to doctrine about what boundary checks may
   do, landed inside a licenscan commit?
6. The blast-radius claim (six repos red to green) is a statement that six repos had findings
   that previously blocked and now do not. Were those findings looked at, or only the exit codes?
