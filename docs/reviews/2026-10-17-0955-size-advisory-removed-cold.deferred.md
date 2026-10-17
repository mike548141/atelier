# Sibling to the size-advisory-removed cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0955-size-advisory-removed-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board item (title line seen, never read whole): `115/270` (three defects found
  adding finding IDs), part c. Filed at the same merge: `115/330` (RECORD.md's index rotation has
  lost its trigger) — open, and about a passage this delta edits.
- The landing commit's message body (read by the brief-writer): Mike ruled on 115/270
  (2026-10-05) that he does not want arbitrary limits such as a fixed size or line count, and on
  2026-10-16, asked what the advisory was for and what removing it would lose, answered "Remove
  it". It says prose-shaped cold content is now caught at review with nothing in the tool pointing
  at it, "the cost Mike was told about and accepted"; lists the hatches left inert and says each
  is reported, never accepted in silence; says no new exemption is invented; keeps `size-advisory`
  in `FINDING_KINDS` so a stale scoped marker is not read as the unscoped form (which would exempt
  an archive store's integrity check); says the other current-truth files are still walked,
  header only. It claims 26 of 42 tests in the touched classes fail on the old module, and an
  estate blast radius of 29 repos with no exit code changed and 28 size-advisory lines over 12
  repos before, none after.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-14-2048-lean-files-sizescan-cold.md`
- `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`
- `docs/reviews/2026-07-20-2040-size-rebalance-cold.md`
- `docs/reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`
- `docs/reviews/2026-07-26-2215-record-pushed-floor-cold.md` — a RECORD.md pass

## The pointer's own lens hints

None beyond "its dispatched worker's output counts as the run's authorship" and the pass type
"code and doctrine". Refs-only.

## Overlap with sibling passes of this batch

- 160/790 (`f9ccba8`, no hatch silences the cold-content gate) is this delta's direct
  predecessor on the same file and is briefed by this run's other brief-writer. What `f9ccba8`
  decided about the cold-content gate is 790's; what this delta changed in the hatches that
  survived it is this pass's.
- 160/830 (`f4afb7a`) and 160/840 (`e3e8a4f`) share the base; 840 also edits
  `tools/test_report.py` and `tools/README.md`.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The removed advisory was, in `RECORD.md`'s own words, "exactly what surfaces a regression back
   to a flat log". The new text says that regression is "caught at review, not by a number". Which
   review, triggered by what? 115/330 suggests the author's run already saw this gap; is the
   doctrine now describing a detector that does not exist?
2. Mike's 2026-10-05 ruling is about limits; the removed advisory never gated. Was "Remove it"
   given with the trade-off stated in plain words, and does the delta's text claim more of a
   ruling than the quoted words carry (see the board's 420/020 discipline)?
3. The scope narrowed: cold content is now looked for in `ROADMAP.md` only, and the other
   current-truth files are read header-only. Was any of them previously checked for anything a
   gate acted on, so that a cold-content `[x]` in, say, a monolithic `SESSIONS.md` now passes?
4. Keeping `size-advisory` as a retired scope so it is not read as unscoped: is the reverse
   hazard handled — an unknown or misspelt scope on an archive store, and how the shared allow
   grammar treats it?
5. The `pins.py` comment still cites "about 200 lines" for a CLAUDE.md, "the class reference
   sizescan once held". Is a ceiling grounded in a number the house has just ruled arbitrary
   still grounded?
6. Inert hatches are reported but never change an exit code. In a child with many stale markers,
   is that a signal anyone acts on, or new noise on every commit — the cost the removal was meant
   to end?
