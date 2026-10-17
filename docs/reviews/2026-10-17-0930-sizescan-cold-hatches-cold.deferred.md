# Sibling to the sizescan cold-content hatches cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0930-sizescan-cold-hatches-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md` —
  **not opened by the brief-writer**.
- Commissioning board item (head line seen, never read whole): `115/270` (three defects found
  while adding finding IDs, found 2026-10-05 by the `080` finding-ID worker). The pointer scopes
  this pass to its parts (a) and (b); part (c) is 160/850's subject.
- A neighbouring board commit, subject only: `fd63df8` (2026-10-06 03:49 UTC) — "board: Mike's
  ruling on sizescan, verbatim, on 115/270 — three builds owed".
- The landing commit's message body (read by the brief-writer): it restates the ruling as
  "nothing may exempt the cold-content gate, since no repo should keep a flat running log" and
  "a check which finds done work must report the specific items"; describes (a) and (b) as the
  brief's *What the work is* lists them; reports a side effect found on the way (`files_by_glob`
  always printed 0 because `iter_candidates` never appended to the list it was handed); and
  gives a blast radius: `sizescan --check` run old and new over every git repo on the authoring
  machine, one at a time, with no repo changing exit code and one already failing under both.
- The merge's message body: the orchestrator read the diff and re-ran the targeted tests before
  merging; the work was rebuilt fresh after a 07:35 UTC crash.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-14-2048-lean-files-sizescan-cold.md` — sizescan's origin
- `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`
- `docs/reviews/2026-07-20-2040-size-rebalance-cold.md`
- `docs/reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md` — the marker grammar
- `docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.md` — an unrun 2026-10-16 brief on
  the scoped kinds this delta changes (another pass's framing)

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/850 (size advisory removed, `72a68cc`) rewrote this delta's surface the same day. Findings
  on code that 160/850 replaced belong to the landed delta here, and to 160/850 only if they
  survive its change; say which.
- 160/750 (marker kinds and finding IDs, `115/080`) introduced the scoped kinds, including the
  `cold-content` scope this delta makes inert.
- 160/730 (the shared report contract) owns `report.over_cap_line` and `report.cap_part`, which
  this delta calls.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. This repo's own `.sizescanignore` matches the harness worktrees nested under `.claude/`, with
   a comment saying their roadmap copies must not gate this repo's commit. With
   `evaluate_ignored`, a glob no longer skips a hot-path file. Does a nested worktree's
   `ROADMAP.md` (or another metered file) now get read and gated from this repo's root, unless
   the file walk excludes it on its own? Probe it with a fixture.
2. In `scan_paths`, slots are spent and `cold_over_cap` is charged before the checks that drop a
   file (a blanket-marked archive store, a file with no reference). Can the over-cap count and
   the spent slots include items of files that produce no finding?
3. `files_by_glob` now counts ignored hot-path files that are still gated. Does "N file(s) by
   .sizescanignore" on the suppressed line now claim a suppression that did not happen?
4. The docstring dates the ruling 2026-10-05; the board commit that recorded it verbatim is
   timestamped 2026-10-06 03:49 UTC. Is the docstring's date a local date stored at rest
   (CONVENTIONS: UTC at rest)?
5. The README paraphrase ("no repo keeps a flat running log; the board is a list of work and its
   state, and the detail lives in a standalone file") sits beside the verbatim quote in the
   module. Does either narrow or widen the quote?
6. The blast radius was measured on exit codes only. `EVIDENCE.md` §13 says a scanner delta
   compares per-finding output, never totals. Does an exit-code-only comparison meet that?
7. Item text is printed raw into hook output and CI logs. A completed item carrying a terminal
   escape sequence, or a bidirectional-control character, would reach the log unaltered. Is that
   the house's concern for a tool whose input is the repo's own tracked text?
8. Does any template, onboarding skill or child-facing doc still tell a repo it may keep a flat
   log behind `sizescan:allow`, now that the hatch exempts nothing from the gate?
