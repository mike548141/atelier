# Sibling to the staged-real-line-numbers cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0955-staged-real-line-numbers-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board item (title line seen, never read whole): `115/300` (conflictscan and
  leakscan report the wrong line number). Filed at the same merge: `115/310` (conflictscan's
  open-conflict state runs across staged hunks).
- The landing commit's message body (read by the brief-writer): on the staged plane both guards
  joined a file's added lines into one blob numbered from 1, so a finding pointed at the wrong
  line, though it still blocked; "secretscan already numbered by hunk"; `report.staged_added`
  already yielded the real number and both guards discarded it; "Only the number a finding is
  reported at changes: no output format, rule, exit code or JSON field moves"; conflictscan's
  open-conflict state "still runs through the added lines in order, as before"; two new tests
  per guard fail on the old code; whole-tree output byte-identical on the repo and on a fixture.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-08-09-0826-e7-leakscan-build-cold.md`
- `docs/reviews/2026-09-25-0715-staged-plane-check-cold.md`
- `docs/reviews/2026-10-16-1551-git-quoted-paths-cold.md` — the staged path reader, 160/760
- `docs/reviews/2026-10-16-1551-scanner-rule-gates-cold.md` — leakscan's gates, 160/720 (its
  brief was one of this brief-writer's templates)

## The pointer's own lens hints

None beyond "its dispatched worker's output counts as the run's authorship". Refs-only.

## Overlap with sibling passes of this batch

- 160/800 (`39a74b9`, the shared staged-diff reader in `tools/report.py`) is this delta's
  foundation and is briefed by this run's other brief-writer. A defect in the number the reader
  yields belongs there; how this delta consumes it belongs here.
- 160/840 (`e3e8a4f`) and 160/850 (`72a68cc`) branched from the same base and also edit
  `tools/README.md`; the merges were sequential.
- 160/720 (scanner gates) reviews leakscan's `scan_lines` gate checks at HEAD, the same function
  this delta now feeds from the staged plane.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. "Only the number changes": conflictscan's open-conflict state used to run across a joined
   blob and now runs across numbered pairs from several hunks, unchanged. 115/310, filed at the
   same merge, suggests that state crossing hunks is itself a defect. Did the delta knowingly
   carry it forward, and is a finding's line now right while its cause is a line in another hunk?
2. Does any leakscan rule or marker check look at line 1, line adjacency, or "the previous line"
   (a preceding-line allow, a header-only scope)? With real numbers, line 1 of the staged input
   may no longer be line 1 of the file.
3. The README paragraph now says "all three guards" report at the real line. Is secretscan's
   per-hunk numbering the same number as `report.staged_added`'s, on every diff shape?
4. Do the new tests build the numbered pairs by hand, or stage a real diff through git? If by
   hand, they test the plumbing, not the claim.
5. leakscan's staged path also runs the path-name scan through `scan_text`, numbered from 1 —
   is that line number meaningful to a reader, and is it consistent with the body findings now?
6. The whole-tree "byte-identical" evidence was taken by the author on one repo and one fixture.
   Is the whole-tree plane provably untouched by construction, making that evidence unnecessary,
   or does it rest on the fixture?
