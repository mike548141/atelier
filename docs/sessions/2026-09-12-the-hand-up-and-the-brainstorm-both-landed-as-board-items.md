# 2026-09-12 · The hand-up and the brainstorm, both landed as board items

**Session:** Sonnet 5 (VS Code) · `main`, in place · four commits, nothing
implemented, nothing claimed. Continued 2026-09-14 after Mike's weekly
budget reset mid-sitting; the two commits below arrived before the reset and
were left off this entry's first pass — closed out properly now rather than
left as a silent gap in the record.

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

## A twelfth thread: exceptions narrower than the line, `110/100`

Mike returned the same sitting with a distinct concern: guard exceptions
(`secretscan`/`leakscan`) may be scoped wider than they need to be — down to
"just the specific characters in a text file, not the file, not the
line/row," and the same question for non-text files. Checked against the
2026-08-09 exception audit (`110/`) first, which swept ~120 markers and 11
globs for reason and effectiveness and then flagged its own blind spot at
close: *"an exception review that reads the reasons has checked rule (c) and
nothing else."* Narrowness itself was never audited. Two findings, read from
the guard code rather than assumed: `GUARDS.md`'s granularity table has no
rung finer than **Line**, so a line carrying a real secret plus other
content — or two matches of the same rule on one line — cannot be split.
And `secretscan.py`/`leakscan.py` both skip binary file **contents**
outright (`_looks_binary()` → `continue`) — no exception exists to narrow
for binaries, because neither guard scans them at all, which is a wider,
undeclared gap rather than the milder one Mike assumed. Filed at `110/100`.

## A thirteenth thread: a model router, checked against its own source

Mike widened the earlier cheap-model-subagent idea into a general question —
*"would we be able to create a model router as code that is both effective
and efficient"* — pointed at
[Anthropic's own model-selection guidance](https://academy.claude.com/tutorials/choosing-the-right-claude-model),
then asked to make that guidance policy as code. Fetched and read rather
than assumed: the source names two decision axes (task complexity,
rate-limit cost) with genuinely codable task-type→model examples, but its
complexity axis resists coding by its own admission — *"if you're not sure,
start with Sonnet [and test]."* Answered as **half yes**: a static
task-type→tier table is real policy-as-code; the complexity judgement is
not. What closes the other half is already `ECONOMICS.md`'s own doctrine,
just not run as code — a smaller model that hits structural work *"logs and
hands up rather than improvising past its depth"* — made mechanical instead
of left to inference is what would make a cheap-default router effective,
not merely efficient. Dispatch already exists (a model parameter on
subagent launch); only the policy layer is missing. Widened into `020/180`
beside the close-out and subagent-tiering threads it extends, not filed
separately.

## State at close

Floor green (`ci` plane, exit 0) before every commit; board index rebuilt
each time; no worktree, no PR — direct commits to `main` under the
standing autonomy grant throughout. Nothing claimed, nothing queued for
review (no doctrine text was written, only board items, across all four
commits). Session ends here, budget-driven rather than work-driven both
times it paused.
