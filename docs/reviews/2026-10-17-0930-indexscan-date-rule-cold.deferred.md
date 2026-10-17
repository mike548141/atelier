# Sibling to the indexscan date-rule cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-17-0930-indexscan-date-rule-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-17 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-16-0703-queue-run-after-the-sizescan-ruling.md` —
  **not opened by the brief-writer**.
- Commissioning board item (head line seen, never read whole): `320/430` (a hand-up from a public
  child: nothing catches an orphaned session-detail file once the session log is an index). Its
  unlisted-file half shipped earlier as `indexscan` (`200/010`, 160/700); this delta is its
  second residual.
- The landing commit's message body (read by the brief-writer): it says "the brief asked for
  agreement; the real index says otherwise", and grounds "not earlier" in a count over the
  session index — 254 dated lines linking a dated file, 16 of them later than their file (9 by
  date, 7 by same-day time), all called legitimate (addenda and close stamps); it measured and
  rejected a first-line-must-equal rule (0 of 204 first links differ in date, 1 in time) because
  a session spanning midnight would make it a heuristic; it lists the blind spots as the README
  does; it says the existing unscoped marker still exempts `unlisted` only "so no legacy marker is
  silently widened"; it reports 252 dated lines compared here with 0 findings, one sibling repo
  declaring an index (10 lines, 0 findings) and a probe over every sibling repo's dated leading
  links (109 lines, 0 mismatches), and calls the rule "a tripwire, not a find"; and it says 13
  of the 18 new tests fail or error on the previous module, the other five passing on both by
  design.
- The merge's message body: the orchestrator re-ran the live scan and the four affected test
  files; one load-only test failure passed once the machine was quieter; rebuilt fresh after a
  07:35 UTC crash.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-10-16-1551-indexscan-guard-cold.md` — an unrun 2026-10-16 brief on the
  guard's first landing (160/700; another pass's framing)
- `docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md` — the shared grammar whose
  `scope="one"` branch this delta adopts
- `docs/reviews/2026-10-16-1551-marker-kinds-finding-ids-cold.md` — an unrun 2026-10-16 brief on
  scoped marker kinds (another pass's framing)

## The pointer's own lens hints

None. The pointer is refs-only.

## Overlap with sibling passes of this batch

- 160/700 (indexscan, the base guard) shares every code path except the date rule; a finding
  on `discover`'s marker handling may belong to either.
- 160/750 (marker kinds and finding IDs) owns the scoped-kind grammar this delta adopts.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. The commission asked for agreement between a line and its file; the delta built "not
   earlier" instead, on the author's own measurement. Is that departure from the commissioned
   rule recorded as a ruling, an answer, or the author's call, and does rule 3 reach it?
2. With `scope="one"`, any kind word is captured. In `discover`, every marker whose scope is not
   `date-mismatch` is filed as an `unlisted` exemption. Does a marker with a misspelt scope, or
   any other scope word, now exempt an unlisted entry — a widening the commit says did not
   happen?
3. `LEAD_LINK_RX` allows at most three spaces of indent. Are nested addendum bullets (indented
   four or more) silently out of the rule, and is that in the documented blind spots?
4. The counts disagree with each other (254 dated lines in the measurement, 252 compared in the
   live run, 204 first links). Which population is which, and do they re-drive?
5. Link text that opens with a glyph, emphasis or a status icon before its date is not a dated
   line. How many index lines in the tree have that shape (count only, not text)?
6. Does the file name's `HHMM` mean the same clock as the line's `HHMM UTC` everywhere the rule
   is reachable, including children whose session files may be stamped in local time?
7. The rule is warn-only on every plane, and the author found no true defect in any repo. Who
   reads a warn-only `date-mismatch`, and is "a tripwire" honest about whether anyone would see
   it trip?
