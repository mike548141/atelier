# Cold pass — the 2026-09-19 tier ruling — orchestration is no longer reserved for the top model, and the run-open stop is gone

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/330-rule-4-cold-pass-queued-the-tier-ruling.md`.
**Why it earns a review:** this rewording decides which model takes every seat
in every orchestrated run in the fleet, and removes a stop that used to halt
runs; if it leaves a route by which a session still asks the principal for a
tier, or removes a stop that was load-bearing, every future run inherits it.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `c38b7da` (2026-09-20) — the landing commit

Delta paths:

- `docs/method/ECONOMICS.md` — the ruling paragraph in § *Match the model to the
  job*; the capable-seat definition and the role-check sentence in § *The
  orchestrated-run tier split*
- `docs/method/CONCURRENCY.md` § *Orchestrated queue runs* — the
  orchestrator/worker seat sentence, and *Tier at open — state it, don't ask*
  (formerly *Role check at open*)
- `skills/queue-run/SKILL.md` step 1
- `docs/method/session-open/session-open-prompt.md` — the anchor paragraph
- `docs/method/AUTONOMY.md` — the first-of-kind bullet
- `docs/method/REVIEW.md` — the reviewer-capability parenthesis
- `docs/method/README.md` — the `REVIEW.md` line

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Every surface that once said, or implied, that the most capable available model
takes the orchestrator seat, or that a session asks the principal which tier to
use — sweep for the old grammar at HEAD (`coldsweep` with the phrases the delta
removed, lifted from the diff), and say whether any survives. Whether the two
surviving stops are stated where a session meets them (at open; at `⏳`
selection) and read as stops rather than advice. Whether the rewording keeps
REVIEW.md rule 4's tier bar *for cold passes* intact and unambiguous — this
batch is itself running under that bar, and the reviewer may treat its own
session as a test case. **Non-goal:** the ruling — only its wording.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   ruling rests on "the cheapest model that can do a good job" being a judgement
   a session can make about *itself* at open — attack whether the wording gives
   a model any test for "good job" beyond its own confidence, and whether
   removing the run-open stop removed the only external check on that judgement.
2. **Correctness & quality.** Diff `c38b7da`. Check every cross-reference
   between the seven surfaces resolves and that they agree; check the renamed
   heading is not still linked by its old name anywhere.
3. **Completeness / harvest.** Search `skills/`, `docs/build/`, `CLAUDE.md`, the
   templates, and the session-open material for any surviving instance of the
   old rule or the old ranking language.
4. **Security & privacy** — mandatory. Doctrine prose; no code surface. The
   residual risk is a smaller model taking an irreversible seat under the new
   wording — check whether AUTONOMY's always-confirm floor still binds
   regardless of tier, and say so. Discharge the house scanner by grounds in one
   line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `coldsweep` at HEAD for the removed phrases (lift them from the diff), with
  `--also-exclude` on this brief and the board item
- `linkscan`, `pathscan`, `spellscan`, `wrapscan` over `docs/method` at HEAD;
  the floor on both planes

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/330-rule-4-cold-pass-queued-the-tier-ruling.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`
- the board item `docs/roadmap/320-*/320-*.md` (the hand-up that carried the
  ruling ask) and any `docs/roadmap/*/…tier-question-back-to-the-principal.md`
  item

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/330-rule-4-cold-pass-queued-the-tier-ruling.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `TR`: `TR1`, `TR2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.

---

# Verdict — phase 1, written 2026-09-25 (run opened 2026-09-25T07:09Z, closed 07:18Z)

## Provenance, repeated

- **Spawn.** A fresh subagent spawned by the batch orchestrator with this brief as
  its only framing. Not the author's session; not started or instructed by the
  author of `c38b7da`. Shape: reviewer-plus-orchestrator, as the brief discloses;
  the orchestrator forms no finding here.
- **Tier.** `claude-fable-5-1` — the principal-named review tier (rule 4). Checked
  at the model identity this session runs under, not inferred from the brief.
- **Read, in scope.** This brief; `docs/method/REVIEW.md` and `00-APEX.md` at
  HEAD; the seven delta paths in full at HEAD `c4b9cd0`; `git show c38b7da`
  restricted to those seven paths (the diff *and the commit message* — the
  message carries the author's "four-link chain" narrative, disclosed here as
  rule-2-adjacent exposure); `.githooks/pre-commit`, `tools/floor.py` (first
  half, the registry), `.github/workflows/ci.yml`, `.atelier-floor.json`,
  `tools/blockscan_map.json`, `tools/test_templates.py::QueueRunSkillTest`,
  `docs/build/templates/CONTRIBUTING.md` lines 108–122, `CHANGELOG.md` lines
  1–25 and 41–52 (the ruling's changelog line — author-worded, one sentence),
  and grep-hit lines only from `PROPAGATION.md`, `DATA-PROTECTION.md`,
  `skills/*/SKILL.md`, `README.md`.
- ⚠️ **Barred-material exposure, disclosed.** My `coldsweep` runs passed
  `--also-exclude` for the 330 pointer and this brief only — not for the 320
  hand-up item the brief lists under *Deferred reading*. Roughly twelve single
  lines of `docs/roadmap/320-…/320-the-run-open-role-check-sends-the-tier-question-back-to-the-principal.md`
  surfaced as hits (its title, its quote of the old CONCURRENCY sentence, the
  labels of its options (a) and (b), and a line naming the heading rename). I
  did not open the file. Every finding below was formed from the delta and the
  doctrine at HEAD; none cites or depends on those lines, but the reader now
  knows the exposure existed rather than discovering it.
- **Not opened.** The `.deferred.md` sibling (not in the tree); the 330 pointer;
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`; every prior
  verdict; every other `2026-09-25-0715-*` brief.

## Per-lens answers

### Lens 1 — approach & assumptions

Load-bearing assumptions, named by me:

1. *A session can judge "the cheapest model that does this job well" about
   itself at open.* The wording gives one test beyond confidence, and it lives
   in ECONOMICS § *One doctrine, tiered authority*: "genuinely does" is a
   **verifiability** test — cheap-model work is safe where failure is
   *catchable* by a floor. That is a test on the **work class**, not on the
   model, and it is complete for builds (scanners, tests, verify-at-merge). For
   the **orchestrator seat** — selection, dispatch, merge endorsement — there is
   no floor, and the wording names no evidence test and no observable trigger
   for "outruns" (TR3). The executor seat *does* have one: the third-seat trial
   paragraph keeps a tier "only when the floor's evidence shows the tier
   genuinely does that class of work". The asymmetry is the gap.
2. *Removing the run-open stop removed the only external check.* False as
   stated, and worth saying plainly: the stop removed was a **rank** check
   ("are you the top model?") — external only in that the roster is external —
   not a check on the session's judgement. The external checks that remain are
   downstream and unchanged: the mechanical floor on every build, the
   orchestrator's read-before-merge, the rule-4 cold pass on any doctrine the
   run authors (this pass is one), and the principal reading the stated tier in
   the opening report. So nothing external was lost at open; nothing was put in
   its place either (TR3 again). The residual is the well-known one — a model
   past its depth is a poor judge of being past its depth — and the doctrine's
   honest answer to that is the downstream net, which the wording should say.
3. *"Cheapest that does the job well, for every job" and "cold passes on the
   principal-named tier" are compatible.* Yes: ECONOMICS § *Match the model*
   states the named tier as the principal's judgement of what doing that job
   well takes, and rule 4's tier sentence is untouched. This batch is the test
   case — Fable orchestrator, Fable reviewers — and the wording admitted it.
4. *The brief's account of the delta is accurate.* Checked against the
   `--stat` and the diff: seven live paths plus the board index and two items;
   the brief's list matches. `CHANGELOG.md` carries a one-line entry (lines
   41–44), which the brief did not list; it agrees with the delta.

### Lens 2 — correctness & quality

Diffed `c38b7da` over the seven paths. The quote of the ruling is verbatim and
identical on ECONOMICS, CONCURRENCY and the skill; AUTONOMY paraphrases it and
says so. Cross-references: CONCURRENCY → `ECONOMICS.md` and → `REVIEW.md` rule 4
resolve and agree; ECONOMICS → `REVIEW.md` agrees; the skill → both canonical
homes, pinned by `QueueRunSkillTest` (8 tests, OK at HEAD). Two defects:
ECONOMICS still names "the **role check** `CONCURRENCY.md` describes" though
CONCURRENCY no longer uses the term anywhere (TR4), and REVIEW's rewritten intro
parenthesis attributes to rule 4 a category rule 4 does not state (TR5). The
two run-open surfaces state the ⏳ stop more strictly than rule 4 does (TR1);
the principal's own prompt states one stop where doctrine states two (TR2).

### Lens 3 — completeness / harvest

Swept at HEAD with `coldsweep` (13 patterns, ledger below) and, for contrast, at
`c38b7da^` in a scratch clone. **No instance of the old ranking grammar survives
on a live surface**: the four pre-landing "most capable (available) model" sites
(AUTONOMY, ECONOMICS, REVIEW, method README) are all rewritten; "capable tier
orchestrates and reviews" is gone from CONCURRENCY and the skill; "wrong tier
for", "Confirm you're on the capable tier" and "Role check" are gone from the
live docs. `skills/`, `docs/build/`, `CLAUDE.md`, both READMEs, the templates and
the session-open material carry only compatible language ("a more capable model
where stakes are highest", "capable tier reviews", "a more capable tier is a
multiplier"). The PROPAGATION floor region and the scaffold `CLAUDE.md` stamp
contain no tier sentence, and `blockscan_map.json` maps none of the delta's
sections, so no floor-bullet co-change was owed. Residue that *does* survive:
the reinterpretation clause at ECONOMICS line 47 now reinterprets nothing (TR8);
"the expensive tier … pay capability for" sits eight lines under the sentence
that retires ranking (TR7); and the **tier half of rule 4's selection check is
absent from both "Taking a ⏳ review item" paragraphs** — CONCURRENCY's and the
skill's name the authorship criterion only (TR6).

### Lens 4 — security & privacy

Doctrine prose; no code surface, no input path, no credential handling.
`/security-review` is **discharged by grounds**: it reads the session's pending
diff, which in this shared worktree is other passes' unstaged briefs, and this
is a landed-delta review of markdown its exclusions bar anyway — its clean pass
would be definitionally empty. Design altitude: the residual the brief names —
a smaller model taking an irreversible seat — is answered. AUTONOMY's
always-confirm floor is untouched by the delta and binds "everywhere, standing
grants notwithstanding" on "every model the same way"; the delta's edit is in
the *Who acts* section, which AUTONOMY itself calls "a second axis, orthogonal
to the floor above". CONCURRENCY keeps the merge and "everything on the
always-confirm floor" with the orchestrator, so a cheaper orchestrator holds
the merge seat but still stops at the floor. The new AUTONOMY bullet keeps the
"dig itself out afterwards" test for live-blast-radius work. Nothing in the
delta quotes a secret, an address or a person; leakscan is clean on both
planes. Threat enumeration for a doctrine change is the lens-1 attack above.

## Findings

**TR1 — MODERATE.** The ⏳ stop at run-open is stated more strictly than rule 4.
CONCURRENCY *Tier at open* says "an off-tier session leaves the ⏳ for one that
qualifies"; skill step 1 says "leave it and take the next open item". Rule 4's
2026-08-17 clause lets an off-tier **orchestrator** run the pass with an on-tier
**reviewer**, disclosed — which under the ruling is the intended cheap shape for
review batches. A workhorse orchestrator reading either surface will skip every
⏳ item it could legitimately run. Not a contradiction (rule 4 wins), an
under-statement at the surface where the choice is made.
*Counsel:* one clause on both surfaces — "or runs it in rule 4's
reviewer-plus-orchestrator shape with an on-tier reviewer, disclosed".

**TR2 — MODERATE.** `session-open-prompt.md` says "Stop only if the work
outruns you" — *only*, in the principal's voice — where CONCURRENCY says "two
things still stop a run". The second (a ⏳ whose named tier the session cannot
honour) is missing. The prompt defers to doctrine ("follow them rather than
re-deriving"), so doctrine wins on a careful read; a session that takes the
prompt's "only" at its word has one stop, not two.
*Counsel:* "Stop only if the work outruns you, or a review item's named tier
isn't yours — and say so either way."

**TR3 — MODERATE.** The orchestrator seat's "does the job well" has no evidence
test and no named trigger. ECONOMICS gives builds the verifiability test and the
executor seat the third-seat-trial evidence rule; *Tier at open* and skill
step 1 point to neither, and the surviving stop names the action ("hand up,
noisily") without an observable for an orchestrator to hand up *on*. Lens 1
above: the removed stop was a rank check, so nothing external was lost — but
the wording now rests the seat on self-assessment without saying what the
downstream net is.
*Counsel:* point *Tier at open* at the verifiability test, and name two or
three observables for the orchestrator seat — a worker defect reaching head
that the merge read missed; a rule-4 pass returning MAJOR on the run's own
doctrine; a hand-up the orchestrator cannot resolve — with the trial rule
applied to this seat as it already is to the executor's.

**TR4 — minor.** ECONOMICS line 308: "the **role check** `CONCURRENCY.md`
describes at run-open" — CONCURRENCY has zero occurrences of "role check" at
HEAD; the heading is *Tier at open — state it, don't ask*. The renamed section
is still referenced by its old name, which lens 2 asked about by name.
*Counsel:* "the *Tier at open* check `CONCURRENCY.md` describes".

**TR5 — minor.** REVIEW.md intro: the named tier applies "for irreversible or
structural work — rule 4 below"; rule 4 binds **self-authored doctrine**. The
categories overlap without either containing the other, so the intro cites
rule 4 for a category rule 4 does not state. Rule 4's own tier sentence is
unchanged, so the bar this batch runs under is intact; the ambiguity is in the
pointer to it.
*Counsel:* match the intro's category to rule 4's, or to "any cold pass" if
that was the 2026-08-04 ruling's scope — the principal knows which.

**TR6 — minor.** Rule 4 says "tier is checked at selection, alongside the
criterion", but at the two surfaces where a run selects a ⏳ item —
CONCURRENCY *Taking a ⏳ review item* and the skill's section of the same
name — only the authorship criterion is stated. The tier stop is placed at
open (step 1, *Tier at open*) and in rule 4, not where the item is met.
*Counsel:* one sentence in each ⏳ paragraph: "and the tier check of rule 4".

**TR7 — minor.** ECONOMICS § *The orchestrated-run tier split*, lines 291–299:
"the run spends the **expensive tier** where its marginal value is highest …
pay capability for" survives eight lines under the sentence that retires the
ranking grammar. Reconcilable (relative cost between the two seats is still
real), but it is the residue of the chain the commit says it cut.
*Counsel:* "the dearer of the two seats" — cost relative to the workhorse,
not to the roster.

**TR8 — minor.** ECONOMICS line 47: "Read 'most capable available' anywhere in
this house as shorthand for …". At HEAD the sweep finds no such phrase on any
live surface outside this clause, so it reinterprets nothing, and it licences
the old phrase to return by declaring it acceptable shorthand. The house rule
(PRINCIPLES §6, stale claims swept in the same commit) prefers the sweep,
which this delta actually completed.
*Counsel:* drop the clause, or scope it explicitly to records and to children
reading an older pin.

**TR9 — note.** ECONOMICS line 54 (added by the delta) is 90 columns; wrapscan
passes it under its single-unbreakable-token exemption (the overflow is the
one word "guard"). Within the floor as enforced; ragged against the ~80-column
target. Rewrap when next touched.

**TR10 — note, not the delta's.** pathscan (warn-only) flags
`session-open-prompt.md` line 15 — a deliberate cross-repo path
`../atelier/docs/method/CONCURRENCY.md` from 2026-09-16 (`411e96a`), outside
the delta's hunk. A `pathscan:allow` marker with the cross-repo reason would
quiet it.

## Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 3 MODERATE (TR1–TR3) · 5 minor (TR4–TR8) ·
2 notes (TR9–TR10). The delta does what it claims: no live surface still
reserves the orchestrator seat for the top model or sends the tier question
to the principal; rule 4's tier bar is intact and this batch ran under it.
The MODERATEs are all placement-and-wording of the two surviving stops.

## Re-run ledger (all at HEAD `c4b9cd0` unless stated; worktree root as `--root`)

| Check | Invocation | Result |
| --- | --- | --- |
| Floor, CI plane | `python3 tools/floor.py --plane ci --root <wt>` | exit 0; secretscan 22 advisory (entropy, none in delta); leakscan 🟡 partial by design (no `--require-terms` on CI); sizescan 2 size-advisory (ROADMAP, SESSIONS); pointerscan 1 grammar on the 380 pointer (another pass's item); pathscan 1 warn-only (TR10) |
| Floor, hook plane | `python3 tools/floor.py --plane hook --root <wt>` | exit 0; staged set empty so the boundary scanners read 0 staged paths; whole-tree checks as CI |
| linkscan | `python3 tools/linkscan.py --root <wt> docs/method` | exit 0, clean |
| pathscan | `python3 tools/pathscan.py --root <wt> docs/method` | exit 1, the one pre-existing finding (TR10); warn-only in the registry |
| spellscan | `python3 tools/spellscan.py --root <wt> docs/method` | exit 0, clean |
| wrapscan | `python3 tools/wrapscan.py --root <wt> docs/method` | exit 0, clean (85-col limit; TR9 passes by exemption) |
| coldsweep at HEAD | `python3 tools/coldsweep.py "<p>" -i --root <wt> --also-exclude <330> --also-exclude <this brief>` for 13 patterns | "most capable (available) model": 0; "capable tier orchestrates": 0; "capable tier for review": 0; "confirm…tier": 0; "role check": 1 live hit (ECONOMICS:308, TR4) + CHANGELOG/board-index/320 item; "wrong tier for": only the 320 item; "on the capable tier": ECONOMICS:134 only; "top model": the two new sentences + skill + a JS test comment; "most capable available": the clause itself (TR8) + 320 item |
| coldsweep at `c38b7da^` | same, in the scratch clone at `21cc384` | old grammar at AUTONOMY:141, ECONOMICS:271/293/294, README:95, REVIEW:19, CONCURRENCY:733/743/745, skill:41–43, prompt:22 — every site rewritten at HEAD |
| blockscan | `--check --warn` at HEAD in the clone | clean; `--against HEAD^` at `c38b7da` not runnable — `tools/blockscan.py` did not exist at that commit; the map at HEAD covers none of the delta's sections |
| QueueRunSkillTest | `python3 -m unittest tools.test_templates.QueueRunSkillTest` | 8 tests OK |
| Full Python suite | not run | grounds: prose-only delta, no tool or test touched; the one class pinning the edited skill was run |
| `/security-review` | discharged by grounds (lens 4) | — |
| Scratch clone | `git clone <wt> <scratchpad>/TR/probe` | ok; no git write in the worktree |

## Follow-up checklist

- [ ] TR1 — principal's decision; if accepted, one clause on CONCURRENCY *Tier at
  open* and skill step 1 (same commit; `QueueRunSkillTest` pins the skill).
- [ ] TR2 — principal's decision; the prompt is in his voice.
- [ ] TR3 — principal's decision; if accepted, ECONOMICS § tier split +
  CONCURRENCY *Tier at open*, one paragraph.
- [ ] TR4 — one-word fix in ECONOMICS:308.
- [ ] TR5 — principal to say which category the 2026-08-04 ruling meant.
- [ ] TR6 — one sentence in each ⏳ paragraph (CONCURRENCY + skill, same commit).
- [ ] TR7, TR8 — wording; principal's call.
- [ ] TR9 — rewrap on next touch. TR10 — `pathscan:allow` marker, any session.
- [ ] Phase 2: reconcile against the sibling once released; restate the overall
  line.

### Reconcile

Written 2026-09-26 (UTC), after phase 1 was committed unrevised (`60225c1`, merged
`1109d49`) and the sibling's text was released by the orchestrator. Phase-1 text
above is unchanged. Opened at this step: the 320 hand-up item, the 330 pointer,
`docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md` in full, and —
because rule 2 says reconcile against prior verdicts and the sibling named none —
a grep across `docs/reviews/` for the surfaces, which found four earlier passes
on them; I read the relevant passages of the 2026-08-17 ruling-round application
verdict (RR5 and its provenance section) and its board item `160/230`, and
grep-hit lines only of the other three. The other `2026-09-25-0715-*` brief the
grep listed stayed closed (house rule for this batch).

**The pointer's lens hint** — *any route by which a session still asks the
principal which tier to use; do the two surviving stops read as clearly as the
rule they replaced?* First half: **no route found** (lens 3 sweep; the intent
record's own run stated its tier and did not ask, under the 2026-09-16 default,
before the delta landed). Second half: **no — less clearly, in three places**,
and that is what TR1, TR2 and TR6 are. The old rule was one sentence at one
place plus the prompt; the new one is two stops spread over four surfaces with
uneven coverage (both stops at CONCURRENCY *Tier at open* and skill step 1; one
in the prompt; the tier half absent from the two ⏳ paragraphs). The hint
anticipated the *class* as a lens; neither record tests placement, and the
record's summary line ("two stops survive") asserts it.

**Seeded question 1 — the two verbatim fragments.** *"the cheapest model that
can do a good job is the one that should be used for every job including
orchestration"*: quoted verbatim on ECONOMICS, CONCURRENCY and the skill;
paraphrased on AUTONOMY as "cheapest that does a good job, for every job"
(drops "including orchestration" — fair, AUTONOMY's context is authority, not
seats). ECONOMICS line 40 expands "every job" to "building, orchestrating a
queue run, fan-out, and the judgement calls in between" — an enumeration, not a
widening. Line 47's gloss adds "at this job's stakes" — a gloss, not a
narrowing. *"fable reviews remain fable reviews"*: applied as "a cold review
pass runs on the tier the principal names, currently Fable" — *remain* maps to
the pre-existing 2026-08-04 bar, so the scope is preserved, not widened to all
reviews and not narrowed. The one place the mapping wobbles is TR5: REVIEW's
intro kept its pre-existing category ("irreversible or structural work") and
newly cited rule 4 for it — a conflation of two categories that both predate
the ruling, not a change to what "remains" Fable. **Neither fragment is
narrowed or widened by the applied wording.**

**Per finding:**

- **TR1 (MODERATE) — anticipated twice, ruled never; stands, heavier.** The
  320 item's option (b) is exactly this shape — *state and proceed* "when the
  orchestrator sends every review and structural call to a capable-tier
  sub-agent" — and the ruling "goes under" the options rather than rejecting
  it. Earlier still, RR5 (2026-08-17 application pass, minor) named the same
  overload: ECONOMICS's orchestrator, the skill's "do not proceed off-tier",
  and rule 4's "may be off-tier" orchestrator, with a batched run of cold
  passes meeting all three; it counselled one clause naming which orchestrator
  the permission is for. RR5 is listed unruled on `160/230`. The delta rewrote
  both surfaces RR5 named and carried the omission forward. So TR1 re-raises
  an open point with new evidence, and its severity is right: the ruling
  makes the cheap shape the default, and the two run-open surfaces still
  steer a cheaper orchestrator away from it.
- **TR2 (MODERATE) — not anticipated; stands.** The record is explicit that
  the prompt "carried the defect too" and that a sweep confined to
  `docs/method/` "would have read clean" — the author knew the prompt was a
  live surface. The record then claims two stops survive; the prompt states
  one, with *only*. The gap is between the record's claim and the prompt's
  text. Not ruled.
- **TR3 (MODERATE) — not anticipated; stands, and the record grounds it.** The
  ruling was applied with no test attached to "can do a good job". The record
  is itself the evidence for the downstream net doing the work the wording
  does not name: the run's orchestrator-seat misjudgements were caught after
  the fact and outside the seat — the pushed floor red three times on a
  harness the orchestrator had declared sound; a worker refused a dispatch
  instruction on evidence; blockscan's blind spot was found by probing. Every
  one is an observable of the kind TR3's counsel asks the wording to name.
  Not ruled.
- **TR4 (minor) — not anticipated; stands.** The 320 item's applied list says
  "the role-check sentence" in ECONOMICS was edited; it was, and kept the term
  CONCURRENCY dropped. Not ruled.
- **TR5 (minor) — not anticipated; stands.** The 320 item's intent for
  REVIEW.md was a one-for-one substitution ("review reads as the *named* tier,
  not 'most capable available'"); the citation to rule 4 for the intro's
  category is the extra. Not ruled; the principal's call on which category the
  2026-08-04 ruling meant is still the ask.
- **TR6 (minor) — anticipated as a lens; stands at its weight.** Checked
  whether the tier check lives at the item instead: the 330 pointer carries
  "*Tier:* Fable … checked at selection", and the record's run read Fable off
  the pointers at open. But `tools/pointerscan.py` *permits* a tier line as a
  lawful field; it does not require one. So the tier stop reaches the
  selection point only where a pointer's author wrote it. TR6's counsel is
  unchanged.
- **TR7 (minor) — not anticipated; stands.** No record touches the "expensive
  tier" residue.
- **TR8 (minor) — reframed by the intent record; weight drops to a wording
  note.** The 320 item names the fourth link of the chain as "the estate's own
  records naming which model is above which" and calls it "an inference, and
  no single text says it"; the record says all four links are cut. That link
  is person-local and outside atelier, so the reinterpretation clause at
  ECONOMICS line 47 is the only treatment atelier *can* give it — my phase-1
  reading that it "reinterprets nothing" is true of this tree and misses its
  intended target. Revised counsel: keep the clause but name its target —
  records outside this repo and children reading an older pin — instead of
  "anywhere in this house", which reads as licence for the phrase to return.
- **TR9, TR10 (notes) — untouched by any record.**

**Compliance confirmed at reconcile:** the 330 pointer landed in `c38b7da`
itself (landing = queuing, rule 4); the pointer is refs-only plus a lens hint,
which pointerscan treats as lawful routing; the 320 item carries its review
line; the record says the author may not take the pass, and did not.

**Formed at reconcile:**

**TR11 — minor.** The session record (§ *320/320*) states "All four are cut
(`c38b7da`)" for a chain whose fourth link the 320 item itself describes as an
inference held in person-local records, not a text — `c38b7da` touches
atelier only. The record rounds a three-link sweep plus a reinterpretation
clause into a four-link cut, and does not say the clause is the fourth link's
treatment. Records are append-only, so the remedy is a dated correction line
at the record's tail, not an edit.
*Counsel:* one line — "the fourth link is outside this repo; ECONOMICS line 47
is its treatment" — appended to the record, stamped from `date -u`.

**Overall, restated:** **PASS-WITH-FINDINGS** — 0 MAJOR · 3 MODERATE (TR1–TR3)
· 6 minor (TR4–TR8, TR11) · 2 notes (TR9–TR10). Phase-1 severities stand;
TR8's counsel is revised above and TR1 gains RR5 as a prior unruled instance.

## Deferred material — folded in at reconcile

# Deferred material — tier-ruling (open only after your findings are durably written)

Sibling of `docs/reviews/2026-09-25-0715-tier-ruling-cold.md` under REVIEW.md
rule 1's split; held by the orchestrator outside the worktree. Folded into the
brief below the verdict when the verdict lands.

## Intent records

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md` — the run's
  account of the ruling and its application. **Not opened by the brief-writer**;
  its `docs/SESSIONS.md` index entry was read at onramp.
- `docs/roadmap/320-*/320-*.md` — the hand-up item that carried the principal's
  verbatim ruling. **Not opened.**

## Prior verdicts and barred items on the same surfaces

- `docs/sessions/2026-09-19-0038-queue-run-the-morning-rulings.md`
- the board item `docs/roadmap/320-*/320-*.md` (the hand-up that carried the
  ruling ask) and any `docs/roadmap/*/…tier-question-back-to-the-principal.md`
  item

## The queue pointer's own lens hints — the author's seeded questions, verbatim

**The lens that matters most here:** whether the rewording left any
route by which a session still asks the principal which tier to use, and
whether the two surviving stops (work outruns the model; a `⏳` pass's
named tier) read as clearly as the rule they replaced.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

1. The brief-writer holds a machine-local note of the principal's ruling in two
   verbatim fragments: *"the cheapest model that can do a good job is the one
   that should be used for every job including orchestration"* and *"fable
   reviews remain fable reviews"*. At reconcile, compare the applied wording
   against those fragments for narrowing or widening.
