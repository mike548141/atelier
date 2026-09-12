# 2026-09-12 · The hand-up and the brainstorm, both landed as board items

**Session:** Sonnet 5 (VS Code) · `main`, in place · two commits, nothing
implemented, nothing claimed.

Two unrelated inputs arrived the same sitting, both handled the same way:
recorded on the board, not acted on.

## The hand-up: `320/150`

A private child, deliberately unnamed, handed up a concurrency finding over
the cross-session channel (`PROPAGATION.md` § *Pointing up*, filing shape 2):
`git pull --rebase --autostash` — the floor's own session-open command — can
fail with `Cannot rebase onto multiple branches` while config is provably
correct (checked independently by two sessions), then clear on a bare retry.
A `FETCH_HEAD`-race is offered as the cause, explicitly labelled a hypothesis
— no capture was taken at the moment of failure, and the child said plainly
what would settle it. Checked against `CONCURRENCY.md` §§ 78–99 first, per
the route's own requirement: this is neither of the two blind spots already
named there (shared index, shared repo state) — filed as a candidate third,
distinguished because the error names a wrong cause rather than staying
silent. Landed as filed; nothing enacted into doctrine.

## The brainstorm: eleven threads, filed not built

Mike then dropped eleven strategic ideas across three mid-turn messages, and
closed with the instruction that mattered most: *record it all, don't spend
what's left of this week's budget building any of it.* Two research passes
(read-only, no state changed) checked each thread against existing doctrine
and roadmap before filing anything, so nothing here duplicates standing work:

**Already covered — pointed at, not re-filed:** using cheap models
(`ECONOMICS.md` § tiered authority); the policy-as-code programme itself
(`020/`, already carries his near-identical words); common-vs-repo-specific
doctrine (`PROPAGATION.md`, mature); roadmap/session-log correctness
(`010/` board-store migration, `370/`).

**Existing items widened with his verbatim asks, dated 2026-09-12:**
`020/180` (mechanical close-out) gained his exact checklist — worktrees,
PRs, docs, no work-arounds, evidence recorded — plus the cheap-model-tier
question as a design constraint on the same tool, not a separate one.
`200/030` (recurrence mining) gained the corpus gap: the one sweep run so
far covers review findings only, never raw transcripts, which is narrower
than what he actually asked for.

**New items, genuine gaps found by the research:** `360/020` — parallel
sessions and claim/work visibility have no shared view *across* repos, only
within one. `310/120` — § *Pointing up* only names atelier as a parent; a
child of `shed` wanting to hand something back to `shed` has no route.
`390/` (new section) — two further shapes with no home at all: `010`
consumer-of-asset and subject-domain-cluster relationships (his own
tentative, hedged names for a home-automation group carried as hedged, not
corrected); `020` — `shed` and client-data repos currently rely on an
*always-confirm* floor rule, not an enforced control, for the one failure
that isn't reversible.

Every new/widened item is explicit that no mechanism was chosen — filing
records the gap and the evidence for it, not a design.

## State at close

Floor green (`ci` plane, exit 0) before both commits; board index rebuilt
both times; no worktree, no PR — direct commits to `main` under the
standing autonomy grant. Nothing claimed, nothing queued for review (no
doctrine text was written, only board items). Session ends here on Mike's
own instruction, budget-driven rather than work-driven.
