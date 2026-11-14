# Sibling to the ccclose-failed-state cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-14-0242-ccclose-failed-state-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-14 UTC by the brief-writer, session `6321275c` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-14 UTC, from the worktree root at `461fdf92`, Node v24.18.0,
machine load averages about 7 on 12 cores:

- `nice -n 10 node --test instruments/ccclose.test.js`: 111 tests, 111 pass, exit 0
  (ℹ duration_ms 122301.906914).
- `mandoc -T lint -W style instruments/man/ccclose.1`: no output, exit 0.
- The census and the live proof: not run (the brief-writer forms no finding, and re-deriving the
  census is the reviewer's measurement to make).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md`
- `docs/reviews/2026-10-18-0506-close-covers-subagents-cold.md`
- `docs/reviews/2026-11-14-0154-ccclose-running-state-cold.md` (the neighbouring pass, `160/1260`)

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **A resume after a failure.** An agent resumed by `SendMessage` after its `failed` notification,
   whose transcript is growing again and has no new notification yet: the `failed` test runs before
   the running test, so does a working agent read as *failed*? The design note's running paragraph
   says the check "never calls a live agent dead". The only supersession test is a later
   `completed` notification; the `completed` branch has a resume path, the `failed` branch has none.
2. **Severity.** A failed agent is no longer running, so the teardown hazard the check guards does
   not apply to it. As a fail it blocks the close for every session that ever had one, even one that
   saw the failure and redid the work; *stopped on purpose* is a pass for a comparable reason. Is
   fail the right level, and does any doctrine around close say what a session does on *failed*?
3. **The foreground claim.** The test gives the failed foreground agent a `failed` notification in
   the queue-operation shape and a clean `tool_result`. Does the harness actually write a
   `task-notification` for a foreground agent? If not, a failed foreground agent reaches
   `hasResult` and reads as *reported*; the code never looks at the launch `tool_result`'s
   `is_error`. Probe with a fixture of a foreground agent whose launch result is an error and which
   has no notification.
4. **Background commands.** Notes are keyed by task id, and only ids with a file under `subagents/`
   are judged, so a background command's `failed` notification seems unable to enter the count.
   Confirm by fixture, including an id collision, and check that the changelog's reason for leaving
   `cctranscript` alone does not quietly concede the same mixing for `ccclose`.
5. **A mirror site.** The design note's *cut mid-flight* row still reads "no completed, killed or
   stopped notification", while the manual's matching sentence was changed to "completed, killed,
   stopped or failed". Is that a V3/V5 contradiction, and are there others (the design note's line
   about "a status the tool does not know", the `unconsumed` row)?
6. **The census.** "None ending on `end_turn`" is the delta's evidence, yet the code and one test
   make `failed` override an `end_turn`. If no real case was observed, on what is "whatever the
   agent's own transcript says" grounded? Nothing in the delta names the script, the corpus or its
   date, so can anyone re-derive 3,587 and 50 (V1, V2)?
7. **The status spelling.** The match is exact and case-sensitive on `failed`. Does the harness ever
   write another word for the same end (`error`, `failure`, a capitalised form)? Those fall to the
   unknown warn. A status census of the local store, counts only, would settle it.
8. **Which notification governs.** "The latest per agent governs" is implemented as the last one in
   file order, not by timestamp, and the same notification arrives in up to three carrier shapes.
   Can a `failed` and a `completed` for one agent land out of time order, or within one record as
   two blocks, so the wrong one governs?

## Facts held back from the brief

- The intent record's DONE note states the census figures and the `cctranscript` grounds in the same
  words as the delta's changelog and comments. It records no run on a real failed agent; the
  finding that opened the item came from measuring a different item (`210/070`).
- The neighbouring pass `160/1260` (the running state, `1bc89816`) names this delta a non-goal; its
  sibling notes that this delta places the `failed` test before the launch's `tool_result` and
  before the running test.
- At brief time no commit after `50547442` touched the four delta paths; HEAD was `461fdf92`.
