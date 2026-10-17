# Sibling to the advisory-count-per-scanner cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the
brief are committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the
brief's provenance; it forms no finding. Fold this file in below the reconcile and
delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-1501-queue-run-briefs-and-guard-builds.md` —
  **not opened by the brief-writer**.
- Commissioning board items (single grep lines seen, never read whole):
  `115/320` (three small floor test and contract gaps; one line seen says the old
  pattern matches any `advisory: N finding(s)` text) and `115/290` (three guards
  describe a response tier their code lacks; lines seen name the four-name selftest pin
  and floor.py's "no advisory form by design" wording naming publishscan's exception).
- The landing commit's message body (read by the brief-writer), in summary: three gaps
  "from the 115/290 worker, checked before changing anything" — (1) `test_floor.py`'s
  head comment still said only prose-hygiene checks may re-baseline, rewritten to
  mirror `floor.py`'s docstring with the registry as authority; (2) conflictscan and
  board were pinned nowhere and licenscan only inside the count tests, now all three in
  both pinned sets plus a config-error test, "mutation-checked: giving conflictscan an
  advisory form fails both"; (3) cross-scanner attribution "cannot happen" because each
  scanner's output is captured separately, but a file named like the count line made
  the board read 77 off a blocking finding, "reproduced against the real secretscan".
  Trailer: a Sonnet model.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-08-09-0825-e6b-advisory-e3-fingerprint-cold.md` — the only verdict
  whose text names the count contract (`AdvisoryCountContract` or the old pattern)
- `docs/reviews/2026-07-28-1204-c1-advisory-cold.md`
- `docs/reviews/2026-08-06-0903-licenscan-e1e2-cold.md`
- `docs/reviews/2026-07-26-2215-floor-local-seam-cold.md`
- `docs/reviews/2026-08-09-0823-floor-render-batch-cold.md`

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/840 (licenscan's advisory tier) and 160/850 (sizescan's size advisory removed)
  have briefs written this batch by another brief-writer; both touch the advisory
  vocabulary and licenscan or sizescan's softenability. Their briefs were seen only as
  filenames (and the first 50 lines of the 160/850 brief). A runner should not charge
  this delta with what those commits changed.
- The publishscan exception named in `floor.py`'s docstring is outside this delta's
  hunks but inside the claim the test docstring now makes.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The body says cross-scanner attribution "cannot happen" because output is captured
   per scanner. Is every `advisory_count=True` scanner run through the capturing branch
   in `run`, on both planes, or does any path print straight to the child's stdout and
   then read nothing?
2. The last-match rule rests on "the count is printed after every finding line". The
   two writers each call `advisory_count_line` at two sites. Does anything print after
   either site (a stale-marker summary, an over-cap note, a remedy line), and can that
   later text carry a path?
3. A file name containing a newline followed by a full contract-shaped line: printed
   after the real count (for example in a trailing section), would it now win under the
   last-match rule where the old first-match rule would have read the real one?
4. The two unsoftenable lists are hand-written on purpose ("so making one of them
   softenable fails a test instead of quietly redefining the list"). Does anything stop
   a new boundary scanner being added to the registry with an advisory form and to
   neither list?
5. ADR 0008 still says only the prose-hygiene checks may re-baseline, and the new test
   docstring says the registry, not prose, is the authority. Is an ADR a record that
   stays, or a live statement that is now wrong?
6. The whole-line pattern hard-codes the em dash and "reported, not blocking." in a
   third file. The comment calls it the scanners' own wording; is there one source for
   that wording, or three copies kept equal by tests?
