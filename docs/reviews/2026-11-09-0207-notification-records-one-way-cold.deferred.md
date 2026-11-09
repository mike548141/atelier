# Sibling to the notification-records-one-way cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-notification-records-one-way-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `node --test instruments/cctranscript.test.js`: exit 0 (ℹ duration_ms 18487.354076).
- `node --test instruments/ccclose.test.js`: exit 0 (ℹ duration_ms 214628.846232).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-17-1010-harness-classification-cold.md`
- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. Order of the branches: the notification test runs before `isHumanQueuedCommand`, which returns
   true on an absent origin. Is there a shape a human typed that also has `commandMode` set? The
   census is the only evidence.
2. Is the census re-runnable, and did it look at the subagent logs, the older formats and resumed
   sessions?
3. `extractText(o.attachment.prompt)` on a non-string prompt returns what? A turn with empty text is
   dropped: can a real notification disappear silently?
4. `ccclose` numbers the same log "the same way": does `ccclose` read this attachment channel, or
   does it now disagree with `cctranscript` about what exists? `instruments/ccclose.test.js` gained
   a test here.
5. Header chips and counts: does "N prompts" or any total change for a session that has these
   records?

## Facts held back from the brief

None.
