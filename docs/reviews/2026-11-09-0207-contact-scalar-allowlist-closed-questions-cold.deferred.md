# Sibling to the contact-scalar-allowlist-closed-questions cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-contact-scalar-allowlist-closed-questions-cold.md`, held
under `docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief
are committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in
the brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 tools/pathscan.py --root . docs/method/REVIEW.md docs/method/SECRETS.md
  docs/method/PROPAGATION.md docs/method/CONCURRENCY.md`: exit 0 (suppressed: 0 by allow-marker · 0
  file(s) by .pathscanignore · 0 rec).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-08-17-1000-channel-doctrine-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. Disclosed contact: nothing obliges the sender to say it was the author. A receiver who does not
   know the message came from the author cannot record it. Is the rule enforceable from the
   receiving end, as it claims?
2. "Permitted only as disclosed contact" against rule 4's "a session the author neither started nor
   instructed". Does disclosed contact that changes the brief still meet the criterion? The
   grounding is a message that changed nothing.
3. Who else counts: the orchestrator, a batch scheduler, a mid-turn relayed by the principal? Is
   "review chain" defined?
4. "Non-scalar": a JSON string holding a serialised object is a scalar. A base64 string? A very long
   string? Is "scalar" the wrong line?
5. "Recurse the allowlist into it": for a child that does, an empty allowlist at the depth where the
   secret sits passes it whole.
6. "The second shape is the worse one": does a three-item grounding carry the comparative, or is it
   asserted?
7. `310/090`'s check says a house question is closed by the house. How does a child tell a house
   question from its own before it closes one? Is that the same test as *whose rule is it*?

## Facts held back from the brief

- The three commits landed in one queue run, and no pass has read them since.
