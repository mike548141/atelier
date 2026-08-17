# Deferred material — the board generator's child-facing strings (open only after your findings are durably written)

Sibling of `2026-08-17-0730-board-generator-child-truth-cold.md` under
REVIEW.md rule 1's split. Fold into the brief below the verdict and delete this
file when the verdict lands.

## Intent records

- `docs/sessions/2026-08-17-0530-board-generator-child-truth.md` — the
  authoring session's account. **Not opened by the brief-writer.**
- The board items the delta writes: `060` (the generated banner names a path
  only atelier has), `070` (the index fails two scanners it generates into),
  `080` (the action word is the only bare positional), and the two handed up by
  a second child, `100` and `110`. **None opened by the brief-writer** — their
  content is known here only from the commit messages that filed them.
- The `docs/SESSIONS.md` index entry for the same session. ⚠️ **This one WAS
  read by the brief-writer**, at onramp and before this brief was commissioned
  — see the disclosure in the brief. It is the reason the intent record above
  was left closed.

## Prior verdicts on the same surfaces

- `docs/reviews/2026-08-15-1030-board-store-migration-cold.md` — the pass on
  the migration that created this generator. BS1 (MAJOR) concerns the hook
  plane's stale-index guarantee, which is the same `--check` path this delta
  edits the remedy string of; BS1–BS14 await the principal's ruling round.
  Reconcile against it.
- `docs/reviews/2026-08-09-0823-floor-render-batch-cold.md` — the pass on the
  floor's render states, if your findings reach how `board`'s check reports
  through the floor rather than what it prints.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these. Treat a question you did not think of
as a prompt to re-read the surface, not as an agenda — and note that the
brief-writer read the author's commit messages in full, so these questions
inherit some of the author's framing.

1. `board.py` now defines both `GENERATED_MARK` and a `GENERATED_MARKS` tuple,
   and its docstring says the marker is matched as a prefix against both
   spellings *"here and in pointerscan"*. `pointerscan.py` visibly does so.
   Trace every read of the marker in `board.py` itself and say which constant
   each one uses. If a comparison in this file honours only one spelling, what
   does that do to an index generated under the other — and is that the
   behaviour the docstring promises?
2. The `wrapscan` exemption is restored by making every item line end in its
   path. Allow-comments still render *after* the link, so a line carrying one
   does not end in a path. The commit says such a line "exempts itself anyway".
   Is that true of every allow-comment shape the board's grammar admits, or of
   the ones currently in the tree? What happens to a long item line whose
   allow-comment is short?
3. `rebuild_cmd()` branches on `Path(__file__).resolve().relative_to(root)`
   raising `ValueError`. Enumerate the geometries this can meet: a symlinked
   `tools/` directory, a symlinked repo root, a child that vendors the tool
   after all, a checkout reached through `/private/var` versus `/var` on this
   platform. In which of them does the branch pick the spelling the reader
   needs — and in which does a *true* condition produce a *false* string?
4. `build_index()` derives its root as `board.parent.parent`; `run_check()`
   passes its own `root`. Are these the same path in every invocation the floor
   makes, including when the tool is called with `--root` and a relative path?
   The estate has a live finding (board item `110`) that `--root` is honoured
   for rules and not for targets in at least four tools. Does `board` share it?
5. Two defects of one class shipped an hour apart, both found by a child rather
   than by this repo's own floor. Is there a check that would have caught
   either before the push — and if the answer is "the selftest, had it asserted
   the emitted command *runs*", does anything now assert that? Distinguish an
   assertion that the string has the right shape from evidence that the command
   works.
6. Item `070` recorded a conclusion — that only a floor-policy ruling could fix
   the wrapscan half — that the next commit withdrew. Follow the withdrawal:
   does any surface still carry the retracted claim, and did the correction
   reach the principal's decision queue as clearly as the original would have?
   A wrong finding that nearly cost a ruling is worth a note either way.
7. The delta's own frame is that a generator must not assume the repo it lives
   in. Apply that frame outward: do the other tools in `tools/` that write text
   into committed files (or into a child's terminal at the moment a check
   fails) make the same assumption anywhere? Name what you checked, including
   what you checked and cleared.
8. The rollout item `e2551da` states that the rollout shipped with this item's
   own gate still shut, and that every previous figure in it was low. Is the
   *current* set of figures reproducible at HEAD, and does the item now say
   what it counted — the failure mode the wrapscan arithmetic in `363a846`
   diagnosed one commit later?
