# Sibling to the close-loose-ends-refusals cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-close-loose-ends-refusals-cold.md`, held under
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

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. "Open work recorded on the board is not one." Does that let a session park a real loose end as a
   board item and declare ready (the very failure)? Does the invariant cover it?
2. The refusal wording is a regex over harness text, from a census of one machine. If it changes,
   the flag goes silent. Is that failure mode stated, and is there a canary?
3. `DELETE_ROUTES` as a re-route test: `rm` refused then `git clean`, `mv` to trash, `:>`
   truncation, `shred`. `rm` is a substring case in `rm -rf`, and a heredoc Python script is not
   read. Does the flag's name overclaim?
4. The 73 and 9 figures are recorded proofs over private transcripts. They can be re-run by count.
   Do they hold at HEAD, and what fraction of the 9 are true positives?
5. Check 13 says "every entry is the session's own". A background task's output or the harness's own
   files in that folder (for example task outputs): does the check then warn on what the session
   cannot clear?
6. `AUTONOMY.md`'s rule and the auto-approve posture: where every permission is granted, what still
   counts as a refusal? Does the rule collapse to the classifier?
7. Is "put to the principal through the decision device" workable in a headless session with no
   device? `CONCURRENCY.md` has a prose fallback; `AUTONOMY.md` does not say.

## Facts held back from the brief

- The principal's sentence in `180/170` includes `askuserquestion`; the delta's doctrine names the
  device, not the tool.
