# 2026-09-16 · Which mechanism a new need should take

**Session:** Sonnet 5 (VS Code) · `main`, in place · two commits, nothing
implemented, nothing claimed.

## Onramp

Synced clean. `git log` showed one commit since the last sitting that this
record didn't yet know about — `fc75cf5`, a separate session's own filing
(`180/010`, 2026-09-14): the atelier plugin's `queue-run` skill shipped and
was declared done, but was never actually **installed** anywhere on the
machine, so the hand-carried session-opening prompt it was built to retire
never stopped. Checked rather than assumed live: no dirty tree, the commit
already merged and pushed, no `[~]` claim on the item — a completed filing
from a prior sitting, not a concurrency hazard. Four pre-existing report
worktrees (`at-handup-320-140`, `at-handup-actcompleted`,
`at-handup-autostash`, `at-handup-conflictscan`) are still present and their
branches unmerged — not touched, not created this sitting, flagged to Mike
rather than acted on.

## The question: which mechanism, and doctrine says nothing

Mike: *"There may be some value in defining in the doctrine when is the
appropriate situation to use code as policy, skills, custom built MCP's, or
other features of Claude."* Checked before filing: `ADR 0006` stays scoped
to the narrower instruments-vs-estate/infra boundary across all four of its
addenda; `ECONOMICS.md` has real criteria for exactly one mechanism
(sub-agents); `050/010` is the one existing gesture at "skill, not
doctrine" and stays scoped to a single incident class, undesigned. Nothing
answers the general question. Filed `400/010` plus a section `README.md`,
naming six mechanisms already in use by precedent alone (guards, skills,
slash commands, hooks, instruments, one adopted MCP server) and four
candidate axes pulled from existing fragments rather than invented:
enforce-vs-judgement (`GUARDS.md`'s own premise), automatic-intercept vs
deliberate-invoke (the `COMMUNICATION.md` Stop-hook lesson), per-repo vs
estate-wide reach, and standing cost to carry (`ECONOMICS.md`'s
episodic-skill-cost framing). No decision tree composed, no home chosen.

**The connection worth keeping:** `180/010`, read at the onramp for
unrelated reasons, turned out to be live evidence for this same item — a
skill was built, declared done, and then never installed, so it delivered
nothing for two months. Named in the reply to Mike rather than left as a
coincidence: the estate already shows a bias toward building a mechanism
over verifying it gets used, which whatever this item becomes should
account for.

## One more before close: `ccarchive` counts files, not sessions

Mike: *"ccarchive currently talks about how many files are archived but does
not mention how many session transcripts which will make more sense to the
user... we should be able to show both files and transcripts."* Checked
against `instruments/ccarchive` rather than assumed: `captureClass()`
already classifies every captured path into named classes (`transcript`,
`tool-result`, `subagent-meta`, `memory`) — the classification exists — but
the printed and `--json` summaries both collapse everything into one
undifferentiated file count. Flagged before it gets built wrong: the
`transcript` class matches any `.jsonl` at any depth, so it already
conflates one real session with however many subagent transcripts that
session spawned — a raw count of that class is not a *session* count, and
"will make more sense to the user" specifically wants the number a person
recognises. Filed `210/160` naming the ambiguity explicitly rather than
leaving it for the build to discover. Nothing built.

## State at close

Floor green (`ci` plane, exit 0) before each commit; board index rebuilt
each time. Direct commits to `main` under the standing autonomy grant; no
worktree, no PR opened this sitting. Nothing claimed, nothing queued for
review — two roadmap items filed, no doctrine text written, no code
changed.
