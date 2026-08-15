# The floor-at-head all-clear has a cancelled-run hole (found 2026-08-09)

`RECORD.md` already requires a close that pushes to carry the **pushed** floor
run's result, not the local scan. This session found the rule has a hole its
grounding case could not have shown: `ci.yml` runs the floor under
`concurrency: cancel-in-progress: true`, so a second session pushing to the same
ref **cancels the in-flight run for the earlier commit**. That run ends
`cancelled` — neither pass nor fail — and no run ever reports on the commit that
was pushed. Observed live: a doctrine push was cancelled ~90 seconds later by a
parallel session's push, and the close cited the *superseding* commit's green
run, which is true but evidences a different tree.

The clause is written at the point of use (a sub-bullet under the existing
all-clear rule) rather than as a new section: read the *conclusion*, never just
"the run finished"; on `cancelled`, re-run against your own SHA and wait. Rule-4
`⏳` queued below.
