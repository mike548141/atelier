# 2026-10-03 · 0144 UTC — Queue run: the hand-up backlog and the tool defects

**Tier:** Opus 5.5 orchestrating, stated at open per `ECONOMICS.md`
§ *The orchestrated-run tier split*. Sonnet 5.5 workers in isolation
worktrees, and Sonnet 5.5 read-only triage agents.

**The brief.** Mike: *"Try not to stop and ask me questions until you have
done all the work. I won't be here to answer for several hours."* The standard
queue-run prompt (loose ends and unblockers first, claim before work, workers
do the building). He added one steer before the run: *"A parallel session is
doing the review work."*

**Onramp.** Synced at `94d5cc6` with a clean tree. Peers on the channel:
`atelier-39` held nothing. `atelier-d0`, a Fable session, holds every review
surface (each `⏳`, the rule-4 briefs, `docs/reviews/`, section `160`), and
will run Mike's ruling round after this. So it asked that the 🎯
"awaits-ruling" items and the verdict files be left alone. This run touches
none of them, apart from adding its own `⏳` pointer, which was announced
first.

**Selection, by triage rather than by reading order.** Four read-only Sonnet
agents classified the 131 open non-🎯 items. Two more classified the 81 🎯
items, looking for any ruled work not yet applied. The non-🎯 buckets came out
at about a dozen DO-NOW, with the rest RULING, IDEA, OTHER-REPO, BLOCKED or
REVIEW. Of the 🎯 items, none was cleanly ruled-and-unapplied. `290/060`
looks applied in code already, and that went to the ruling-round session
instead of being edited here.

## Hand-up PRs: eleven waiting, ten landed, one held

The review session pointed at eleven open hand-up PRs. `PROPAGATION.md`
§ *Pointing up* gives the parent's half: land a filed finding on the floor's
own evidence and say it is the child's, unreviewed. **Ten landed** on `main`
as `--no-ff` merges, reporter branches merged as-is and never rebased. Each
PR carries a comment saying what landed and where.

**Seven of the filings collided on numbers.** Five filed as `320/410`, and
`360`, `370` and `400` were already taken on `main`. `board.py` refuses a
duplicate item number, so each was renumbered inside its own merge commit,
which says so. New slots: `320/410`–`490` and `180/020`. One filing
appended to the existing `320/160`.

**PR #92 is held, not landed.** Its evidence lists which tools one machine
has on and off `PATH`. The item's own option D argues that a public list of
this kind is reconnaissance material. Trimming it before it reaches `main`
is Mike's call, so the PR carries a comment and nothing else.

The merged filing's worktree (`atelier-report`) was put away, since the
branch was on `main`. `atelier-report-tool-locator-0353` (PR #92) was left
alone.

## `320/130`: stampscan's cover switch

The item names the remedy as a copy rather than a design: `leakscan
--require-terms`. The worker built `--require-stamps`, which makes a run that
verified no stamped block exit `2` with the cause named. With the switch off,
the output is byte-identical (stdout, stderr and exit; plain, `--warn` and
`--json`; atelier's tree). That meets `020/110`'s stated precondition. The
wiring decision stays there.

## `320/340`: blockscan names what its map cannot see

This is the third of the item's three candidates, the one it says stops the
gap being rediscovered. `--check` reports headings in mapped docs that no
entry names. Subsections under a mapped heading are listed in full, and
uncited top-level headings are collapsed to a count. The first output was
about 60 lines on the real tree. The orchestrator asked for the collapse, and
it is now 16. It is advisory only, with the exit code unchanged. Today it shows
12 subsections in the blind spot, including the two this item was found on.
The map-design choice itself (explicit subsections or `recursive: true`) is
still open.

## `320/010` class C and `320/170`: built, then held as draft PR #96

🛑 **An orchestrator error, caught before push.** The triage read class C as
a cheap mechanical fix. The item says in so many words that *"Classes B and C
remain unruled"*, and that the fix candidates were *"deliberately not chosen
here"*. The worker chose **expand-and-check** over the item's
**exclude-like-`*`**, and the orchestrator merged it locally before reading
that line. The unpushed merge was reset. The branch went up as draft PR #96,
framed as a ready option for the ruling. **The lesson is the board's own
lesson, not a new one: a triage summary is not the item.** The orchestrator
reads an item's ruling state in the item before dispatch. Afterwards it is
too late.

## `210/150`: why the source is smaller — answered

A read-only investigation. `--force` was never run, and the manifest mtime
was unchanged afterwards. The result is recorded in the item as classes, not
content. The sources really were edited: both refusals are memory `.md`
files rewritten or trimmed since their last archive, and neither is
mis-paired or corrupt. So the guard's append-only premise is wrong for
whole-document classes, and that supports `210/010`'s option (a). Mike
decides whether superseded revisions are kept.

Found on the way and filed as `210/170`: **the manifest lags the mirror in 14
files**. That makes the guard's comparand too low, so a truncation could pass
silently. The cause is not diagnosed.

## `210/050`: the archive pool, roughly halved

Both causes the item named are fixed. The dataless check is one batched
`stat` per 400 paths, and the cwd sniff inflates only a gzip prefix. The
listing went from about 15 s to about 7 s, with byte-identical output in
three paired runs and flag-for-flag agreement across all 960 mirrors. The
remaining cost is a third path, filed as `210/180`. ⚠️ The worker's first
profiling script hydrated evicted iCloud mirrors by reading them. That is
harmless and temporary, but it is the hazard the tool exists to avoid, so
it is disclosed. The cold pass is queued at `160/440`.

## `115/210`: claimed, then put back

This is the same mistake as class C, caught one step earlier this time,
before any work. The item lists three candidates, *"not chosen here"*, with
a stated trade-off. The run had claimed it on a triage summary that called
it a documentation fix. The claim was released untouched. From here on, the
run reads each item's own ruling state before claiming it.

## `040/010`: the date-kind rule, written down

Mike's rule from 2026-08-09, captured near-verbatim on the board ever since,
now lives in `GUARDS.md` beside the acceptance/deferment split, which is the
home the item named. A **mandate** date binds the class: a child may only
tighten it or argue an exemption. A **default** date seeds the value: a
child may set it earlier, the same, or later. A date-setting ruling names
its kind. The run added one clause of its own, saying so in the item: an
older date with no kind on record is asked about, not inferred. The
doctrine pass is queued at `160/450`.

## `200/010`: the census, and atelier's own drift fixed

The ruling bound the generic index-keeper to a census first. A read-only
sweep of all 31 estate repos found **22 hand-maintained indexes of 7 kinds in
14 repos**. Drift is firm in 4 and probable in 3. Nothing guards the
unlisted direction anywhere, so the class has many members and the ruled
build stands. The census also found that **catalogues and session indexes
drift, while decisions indexes mostly do not**, and that moves the design's
first target. The item records only classes and counts, with no private repo
named. atelier's own four firm drifts were fixed in the same commit, except
`filewalk.py`. Its missing entry is FW2, which is in the ruling round, so it
was left alone.

## `210/170`: the manifest stops falling behind

The orchestrator read the code before claiming. `archive()` writes mirrors
inside its loop and saves the manifest once, after it. So a run that dies
part-way strands every mirror it wrote, and the mtime check makes the gap
permanent. The fix checkpoints the manifest every 50 mirrors and on any
throw, re-signing each time so the signature always matches the saved
bytes. It also heals an entry whose size disagrees with a fresh-by-mtime
source. The real archive's 14 lagging entries heal on the next ordinary
run. Locking against overlapping runs is the open half. The code pass is
queued at `160/460`.

## `200/040`: R2 surveyed, and eleven contradictions filed

A claim-keyed pass over `method/`, `build/`, the templates and the skills
found **68 multi-stated claims: 41 independent restatements, 20 pointers and
7 stamped**. Only the floor block is mechanically stamped. **Eleven sets of
copies already disagree.** They are filed as `200/100` with file:line
evidence and six re-read first-hand, and none was fixed in passing (the
report-don't-patch rule). The sharpest is C1: the queue-run skill tells a
run to `pull --rebase --autostash` with no status-first gate, which is the
step `CONCURRENCY.md` warns against, on a recorded near-miss. Four of the
eleven are a skill or template contradicting the parent it claims to
compress.

## `260/040`: publishscan's second round

The tracked-file half of P2a ran as a names-only survey of every sibling's
tracked set. It found few never-publish shapes, all in private repos. Round
2 adds those and about 55 standard-practice shapes. The reasons for each
exclusion are written in the source. Measured blast radius: 3 private repos
newly red (23 files) at their next pin bump, and 0 public. 🛑 **Before
merge the orchestrator rewrote the worker's unpushed commit.** The worker
had written measured counts for the secret-carrier shapes, plus an
appliance backup's vendor-specific filename, into the public source. That
describes a private repo's security posture even with no name attached, so
those entries now say "standard practice" and the vendor pattern is gone.
The measured instance it covered is left to its own repo. The code pass is
queued at `160/470`.

## `115/080` part 2: one allow-marker grammar, fourteen parameters

The item's binding constraint was carried into the dispatch verbatim:
share the mechanism, never the behaviour. `tools/allowmarker.py` now builds
every scanner's marker regex and loads every reason-required ignore file.
Fourteen scanners are converted, and each keeps its own acceptance rules as
parameters. The proof is the item's own standard. Patterns are
string-identical (one benign backslash aside), and output is byte-identical
on the real tree and on 170 fixture comparisons. A pin test now fails if a
shared edit changes any scanner's pattern. That turns the 2026-08-09 class
(nine markers silently voided) into a red test. The extraction surfaced four
divergences, filed as `115/230` rather than unified. One widens: a scope with
no reason exempts every kind on the line. Part 3 is still owed. The code pass
is queued at `160/480`.
