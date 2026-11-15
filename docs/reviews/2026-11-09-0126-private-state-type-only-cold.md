# Cold pass — a private repo's state goes by type in public records (`260/080`, posture C)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** VERDICT WRITTEN 2026-11-15 UTC, both acts — PASS-WITH-FINDINGS (0 MAJOR · 2 MODERATE
· 6 minor · 2 note after reconcile), by a Fable 5.1 reviewer under the principal's drain order of
2026-11-16 NZDT; the ten findings await the principal's decisions (rule 3).
**Sizing:** **small** — one commit, 130 changed lines of an ADR plus a ten-line doctrine paragraph;
no code.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1090-rule-4-cold-pass-queued-private-state-type-only.md`.
**Why it earns a review:** This binds every public record every session writes from now on, and
pushed history cannot be recalled. Worst failure: a line a session cannot draw at write time, so the
rule is either ignored or over-applied, with the exposure accumulating in a public repo either way.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched, which wrote it (per the
  queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `84e3aa7f` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). Neither authored any of this delta,
  and neither was started or instructed by the author. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing its briefs. It ran
  no review and used no Fable model. The principal's rule: whoever writes a brief does not run it.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  list of board items, the run constraints, and the principal's request verbatim, "Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done". It carried no framing of the
  work. The brief-writer had no contact with the author or its workers.
- **Who reviews:** a fresh Fable 5.1 session or subagent started for this pass alone, from a spawner
  that passes rule 4's criterion. **Barred from reviewing:** session `722ac2e2` and everything it
  started; session `84e3aa7f` (this brief-writer); session `74f2b8cd`. Whoever takes the pass states
  the spawn in the verdict (V7).
- **The principal's approval:** none yet for the pass. His request above covers this brief only. The
  pass waits for his explicit permission for Fable work.

⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):

- its dispatch text; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` whole; the
  house-form brief `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` through
  line 728, including its verdict (read for shape, another surface); the top of one sibling brief;
- the queue pointer whole; the intent record whole;
- the delta body-free through `tools/coldsweep.py --commit 38536e4c` (subject, stat, diff, never the
  message body), `--help` of `coldsweep`, `board`, `leakscan` and `reviewscan`, commit subjects
  through `git log`, and file names under `docs/reviews/` and
  `docs/roadmap/160-doctrine-review-owed/`;
- the last three index lines of `docs/SESSIONS.md` and one earlier session record, read for the
  format of its own closing record; and the results of the re-run lines below, held in the sibling.

It did **not** open `docs/ROADMAP-DONE.md`, any other session record, any other prior verdict, or
any delta commit's message body. Its harness also loaded user-level and repo instruction files and a
memory index, which hold private context this brief does not carry. Everything evaluative it formed
is in the sibling.

## The acceptance test

The principal's pick of 2026-11-08, as the ADR records it: *"Type-only for private state"*, whose
offered option read: a private repo's internal state is described by its type only in a public
record, naming a repo in any other context stays allowed. An answer to options offered, not a ruling
in his own words; the ADR says where his words differ, his words win.

## What the work is

One commit on `main`, `38536e4c` (first confirm your tree has it: `git merge-base --is-ancestor
38536e4c HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 38536e4c \
  --path docs/decisions/2026-08-05-1233-estate-internal-context-in-public-records.md \
  --path docs/method/RECORD.md \
  --path docs/decisions/README.md \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 38536e4c..HEAD -- docs/decisions/2026-08-05-1233-estate-internal-context-in-public-records.md docs/method/RECORD.md docs/decisions/README.md CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- The Decision states posture C and binds forward only.
- What must be type-only is a sentence saying what *condition* a particular private repo was in;
  naming it in any other context, including an *act* done to it, stays allowed.
- The ADR marks two judgements as the drafter's readings (a type only one repo fits is a name; act
  versus condition).
- `docs/method/RECORD.md` § *The record is public* gains the rule, stated once and pointing at the
  ADR.
- No scanner enforces it; a narrow advisory aid is possible.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** The ADR's Context measurements except as they ground a claim in the Decision or
Rejected sections.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. This delta is a privacy rule on a PUBLIC repo. Attack it as a
rule: what it still leaves readable, what a reader can join across sentences. Do not quote any
private repo name or state you meet in the tree; refer to it by type, as the rule says.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane hook --root .` and `--plane ci`

## House rules for this run

**Live systems:** read-only reads of live systems as needed, no live writes. A check that would need
a write is marked **NOT RUN**, with what it would have checked. No push and no `gh` call that
writes, except committing this one file as the process below says.

- Never print a secret, and quote no key body, fixture bytes, personal data, private repo name or
  private path. This repo is PUBLIC; a child is referred to by type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Scratch
  repos, mutated copies and fixtures go under your session scratchpad and are deleted when you
  finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/` or
  `instruments/`.
- One heavy process at a time, foreground, long timeout, `uptime` first. Never run an installed tool
  by bare name from `PATH`: run it from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it only from a clean tree
  at a scratch clone of the code, or discharge it by grounds; never with this brief or its sibling
  dirty. A clean pass over markdown is weighed as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-09-0126-private-state-type-only-cold.deferred.md`, every delta commit's
message body, and the intent record
`docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/080-p6-rpi-f5-estate-internal-context-accumulating.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1090-rule-4-cold-pass-queued-private-state-type-only.md \
  --also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/080-p6-rpi-f5-estate-internal-context-accumulating.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`38536e4c`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `TY`: `TY1`, `TY2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling
is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (cold, Fable 5.1, 2026-11-15 UTC)

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, tier checked at
  selection. Ran on 2026-11-15 UTC, 22:11–22:25, in a drain worktree of atelier at `ce0e1cc2`.
- **Spawn:** a headless rule-4 orchestrator, session `6dd1e8d3` (Opus 5.5), itself started by
  the drain session `21a271a5` (Opus 5.5) under the principal's weekly drain order of
  2026-11-16 06:53 NZDT (`/fable-drain`), which is the explicit permission for Fable work this
  brief waits for. Both are off-tier orchestrators disclosed under rule 4: they hold the context
  partition, form no finding and write no severity. `21a271a5` wrote no brief and no delta for
  this pass. Neither was started or instructed by the barred set (`722ac2e2` and what it started,
  `84e3aa7f`, `74f2b8cd`), and I had no contact with any of them.
- **The orchestrator's direction, as process only** (the substance of its spawn prompt): the
  worktree path and the brief path; read the brief and `REVIEW.md` first; the sibling
  `.deferred.md` is held out of the worktree (it shows as a deleted file in `git status`) and
  must not be sought elsewhere; sweep with `coldsweep`; keep a work log outside the tree with
  commands and evidence only; write nothing but that log and this file; no git write, no live
  write, no mutation of `tools/` or `instruments/`; `uptime` before heavy commands, `nice -n 10`,
  one suite at a time; refer to private repos by type; act 1 then stop, act 2 on release. It
  carried no question about the delta and no pointer to where the risk lives.
- **What I read before writing:** this brief whole; `docs/method/REVIEW.md` whole; the delta
  body-free through `tools/coldsweep.py --commit 38536e4c --path …` (four paths); the four delta
  paths at HEAD; three later commits that touched them, body-free the same way (`7ad98503`,
  `9c8cb7e7`, `e76250cf`); `RECORD.md` §§ *The why lives at the site*, *The session log*
  (identifier block), *The record is public*; `PROPAGATION.md` § *The route* rules 1–2 and the
  `320/330` and `020/050` paragraphs, the floor block (lines 205–225); the child template
  `docs/build/templates/CLAUDE.md` 85–130; `AUTONOMY.md` 50–64; `PRINCIPLES.md` § 6;
  `docs/decisions/README.md` 1–44; the board item `030/070` (the scanner item; not touched by the
  delta, so not barred) and the names in the `200` section; `commands/fleet-pins.md`;
  `tools/README.md` § namescan; `tools/reviewscan.py` 138–150 and 618; `namescan.py --help`;
  the `private` lines of every skill and `docs/build` file. The session log step of the onramp
  was skipped (rule 2). Not opened: `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`,
  any prior verdict, the queue pointer, the intent record beyond its title, any commit body,
  the sibling.
- **Exposure, disclosed:** `tools/floor.py --plane ci` printed pointerscan's two queue-state
  findings, which named two other `160/` pointer files (`1420`, `994`) by path only; I read no
  content of them. My harness loaded user-level instruction and memory files that carry private
  context this verdict does not use.
- **Work log:** kept outside the tree during the run, to be opened into this repo at the fold
  by the orchestrator. It lists every command and file range above with what each showed.

### The acceptance test, read cold

The pick, as the ADR quotes it, is *"Type-only for private state"*, from options a session
offered on 2026-11-08. I cannot verify the option's wording in act 1: the record of the ruling
round is barred until phase 2. So in act 1 the ADR's quotation is the author's claim, and I test
the Decision against it as quoted. Reconcile owes a check of the option text.

### Load-bearing assumptions, named first

1. **The harm sits in the state sentence, not the name** (Rejected B's grounds). *Damaged*, not
   falsified: the probe is the ADR's own example table, whose rows pair an allowed act sentence
   naming the repo with a type-only state sentence that is the same fact (TY2).
2. **A writer can tell an act from a condition at write time.** *Confirmed as followable, with a
   gap*: the one-question test is sharp for the examples given; it is silent where the act names
   the repo and the condition sits beside it (TY2), and where a type fits one repo (TY8).
3. **The rule reaches the writer where the sentence is written.** *Damaged*: the point of use in
   `RECORD.md` says the opposite posture (TY1), the plugin prompts say a third (TY3), and the
   instrument that produces the fleet-state table carries no pointer (TY5).
4. **No scanner can hold the rule, so it binds by discipline.** *Confirmed for the whole rule,
   over-stated for the band*: a scratch probe joining the leak scanner's local term list to
   state vocabulary ran over every non-barred prose surface and returned 0 lines in 0 files, so
   the advisory aid the ADR calls plausible has a measured false-positive floor of zero on
   those surfaces. Records are barred in act 1; the same probe runs over them at reconcile.
5. **"Naming in any other context stays allowed" holds on every record surface.** *Falsified at
   HEAD* by later work the delta's text does not acknowledge (TY3).
6. **Forward only is the only honest scope.** *Confirmed*: `RECORD.md` § *The record is public*
   says a scrub of HEAD is not remediation; the ADR's Context measured ~270 mentions; the
   accepted Consequences claim nothing retrospective.

### The four lenses

**1. Approach & assumptions.** Right problem, right altitude: the band between the narrow join
rule and general reticence is real, the measurement grounds the choice of C over A and B, and
the ADR is candid that the pick is an answer to options and marks two drafter's readings. The
altitude slip is the unit of analysis: the rule is drawn per sentence while the exposure it
names in Rejected A ("which sibling repos exist and roughly what state each was in on a given
date") is assembled per record. See TY2.

**2. Correctness & quality.** The Decision states what the quoted option says and marks its two
additions. One addition is unmarked (TY7). One claim is stale against the tree: the scanner
item's location (TY4). One scope-cut from the draft's own plan is silent (TY5). The
review line is a promise rather than a pointer (TY6). The CHANGELOG entry and the README index
line agree with the ADR. `RECORD.md`'s paragraph is a faithful compression that points at the
ADR (V4 satisfied for the pair).

**3. Completeness / harvest.** The delta swept `RECORD.md` § *The record is public*, the ADR,
its index line and the CHANGELOG. It did not sweep `RECORD.md`'s own closing-entry spec
(TY1), the review-brief and session-close surfaces the draft named (TY5), or the scanner item
(TY4). No test can see a prose rule; `reviewscan` sees only that a review line is non-blank
and passed on a line that points nowhere (TY6). Later work added surfaces that state a
different posture (TY3) and a correction placed outside the ADR lifecycle's form (TY9).

**4. Security & privacy.** Attacked as a rule on a public repo. What stays readable: every
private repo's name, its acts, its sessions and items, by design. What a reader can join: an
act sentence to the type-only condition in the same entry (TY2); an item or PR title that
carries a condition word to the named repo it concerns (TY2); a unique type to the repo it
names (TY8). What the rule closes: the direct name × condition sentence, and the probe says
the non-record surfaces hold to it today. `/security-review`: **not run**, discharged on
grounds: the delta is markdown, which the scanner's exclusions bar, so its clean pass would
weigh as nothing; and the tree is dirty with this brief for the whole act.

### Standing checklist

- **V1** No claim stronger than its evidence: one over-claim, TY7; the "~15 lines" and "~270"
  figures are the Context's own measurements and are cited as such.
- **V2** Re-run: see the ledger below; both planes exit 0.
- **V3** Swept to every mirror site: not fully; TY1, TY5, and at HEAD TY3 (skills are on
  `PRINCIPLES.md` § 6's surface list).
- **V4** One fact, one home: the ADR is the home, `RECORD.md` the stamped copy with a link;
  `CHANGELOG` is the index. Satisfied.
- **V5** No internal contradiction: TY1 (within `RECORD.md`), TY3 (doctrine vs enforced check
  and plugin prompts), TY4 (a cross-reference that reaches no item), TY8 (the drafter's
  reading vs the ADR's own example). Cross-references checked for the rule reached:
  `RECORD.md` → ADR reaches the Decision; ADR → `RECORD.md` § *The record is public* reaches
  the paragraph; ADR Consequences → "the 200 section" reaches no scanner item.
- **V6** Security & privacy: lens 4 above; the scanner discharged with grounds.
- **V7** Provenance: stated above, in the brief and here.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `38536e4c` (the delta) | yes, `coldsweep --commit` with four `--path` | TY1, TY2, TY4, TY5, TY6, TY7, TY8 |
| `7ad98503` (pointer, +51 s) | yes, `--path docs/method/RECORD.md` only | TY6 (timing noted) |
| `9c8cb7e7` (`320/330`) | yes, `--path docs/method/RECORD.md` | none; resolves a would-be V5 |
| `e76250cf` (`020/050`) | yes, `--path` RECORD and the ADR | TY9 |
| later `namescan`, `210/440` skills | read at HEAD, not as commits | TY3 |

### Findings

**TY1 — MODERATE.** `docs/method/RECORD.md` § *The session log*, the closing-entry identifier
block (lines 123–124 at HEAD): *"A private repo is named generically in a public record
(§ The record is public)"*. That is posture B's wording, written 2026-10-18 (`180/080`), and it
cites the section that since the delta says the name is allowed and only the condition goes by
type. The two statements sit 400 lines apart in the same file, and the first is the one a
session reads while writing its close, which the ADR's Context identifies as the surface
carrying ~96% of the mentions. The delta did not sweep it. Evidence: `sed -n 112,132p`;
`git blame -L123,124`. Breaks: V3, V5; `PRINCIPLES.md` § 6 (sweep in the same commit).
*Counsel:* reword the clause to the accepted posture and let it point at the paragraph.

**TY2 — MODERATE.** The rule's unit is the sentence; the exposure it exists to close is
assembled from the record. The Decision's own table pairs *"Bumped the pin in `widget-api`"*
(allowed) with *"A private child's pin was three bumps behind"* (type-only); read as one entry,
which is how a session close is written, those are one fact with the name restored. The same
join runs through *"a PR or item that concerns it"* (allowed by name) when the title carries
the condition, which item titles do by convention here. The one-question test in Consequences
asks about "any sentence" and says nothing about what stands beside it. Severity reasoning: the
rule still removes the direct join and is followable, so the work is not mis-built; but on the
common shape of a close entry that touches one or two repos it closes less than Rejected A says
it closes. Not MAJOR because the residual is narrower than A's and the fix is a clause, not a
re-ruling. Breaks: lens 4 (join across sentences), V1 against Rejected A's account of what C
buys. *Counsel:* add one sentence to the paragraph and the ADR's one-question test: a type-only
condition is written where no sentence in the same entry names the repo it describes; where the
act must be named, the condition is left to the private repo's own record.

**TY3 — MODERATE (HEAD state; formed against work landed after the delta).** The ADR and
`RECORD.md` say naming a private repo "in any other context stays allowed", unqualified by
surface. At HEAD two surfaces apply the stricter posture: `tools/namescan.py` (in a public
repo, no private name in a branch name or commit title, using the leak scanner's term list,
warning until 2027-05-03, then exit 1), and the `fleet-sweep` and `review-drain` skill prompts
(*"Never name or point at a private repo, the estate root …"*, landed 2026-11-14). `RECORD.md`
§ *The why lives at the site* makes the commit message the smallest unit of the record, so a
title is a record surface the ADR's allowance reaches. `PROPAGATION.md` § *The route* rule 2
gives a filing's surfaces precedence, but `namescan` runs on every title, not only filings.
Neither the paragraph nor the ADR names the split; a writer following `RECORD.md` writes
"pins: bump <private child>" and the hook warns. Breaks: V5; `PRINCIPLES.md` § 6 (skills are a
sweep surface). *Counsel:* one clause in the `RECORD.md` paragraph naming the surfaces where the
name itself is barred (branch, commit title, hand-up filings, fleet prompts) and why: those
surfaces publish before anyone reads them.

**TY4 — minor.** ADR Consequences: *"Registry scanner item (the name x posture item in the 200
section of the board). Re-specify against this line."* The item is
`docs/roadmap/030-…/070-mechanise-the-private-repo-posture-join.md`; the `200` section holds
one item, about where the registry lives. The item is still specified on the join and has not
been re-specified; the CHANGELOG says it "can now be". A cross-reference that reaches no item
is dangling under V5's own wording. *Counsel:* name the item by number and queue the
re-specification, or state that it is deferred.

**TY5 — minor.** Silent scope-cut from the draft's own plan. The draft's Consequences for B or C
read: the rule is stated *"at the point of use — the session-record and review-brief templates,
where the sentence is actually written — rather than only in the doctrine chapter, per this
repo's own rule-grammar finding"*. The accepted Consequences read *"stated once and pointing
here"*, with no reason for the change. The point-of-use surfaces today: the closing-entry spec
says B (TY1); `skills/review-brief/SKILL.md` has no private-repo line; `commands/fleet-pins.md`,
whose purpose line is *"who is stale, by how much"* per named child, has no pointer to the
record rule, and item `030/070` records that all three prior breaches happened at exactly the
moment of *"summarising fleet-wide scan state into an atelier record"*. Breaks: lens 2 (silent
scope-cut); `PROPAGATION.md` § *When a rule keeps breaking* rung 1 (framing before
enforcement). *Counsel:* one line at each of the three points of use, pointing at the paragraph.

**TY6 — minor.** The ADR's review line: *"queued — a rule-4 cold pass is owed … the ⏳ pointer is
written when that edit lands, by the landing session"*. It names no pointer and no brief, and
passes `reviewscan` because the check asks only that the value be non-empty; the tool's own
grammar example is `**Review**: queued — docs/reviews/<brief>.md`. The pointer landed in the next
commit, `7ad98503`, 51 seconds after `38536e4c`; rule 4 wants it in the landing commit, and the
TA9 precedent (a series, pointer in the commit that completes it) covers the intent. At HEAD
the brief exists and the line still points at nothing. *Counsel:* point the line at this file
and the `160/1090` pointer when the verdict is folded.

**TY7 — minor.** The ADR promises that *"the places where this statement makes a judgement the
pick did not spell out are marked (drafter's reading)"*, and marks two. A third is unmarked:
*"Part (b), published workflow. Answered by the same line"*. The quoted option concerns a
private repo's internal state; it says nothing about the method-versus-operations boundary the
Context drew for part (b), so applying the pick to it is the drafter's judgement. The reading
is reasonable; the mark is owed by the ADR's own rule. V1.

**TY8 — note.** The drafter's reading *"a type that only one repo fits is a name"* is sound and
is not carried through. The ADR's own type-only example is *"An infra repo had two open scan
findings"*; whether more than one repo in this estate answers to "an infra repo" is not stated
in any public surface I may read, and should not be. `RECORD.md`'s later paragraph says the
estate-root repo's *"condition go[es] by type only"* while "the estate-root repo" is a type one
repo fits, so a writer reading that paragraph alone may write "the estate-root repo was failing
a check" and believe it compliant. Breaks: V5 (the reading against the example). *Counsel:*
one worked example of a type that is a name, beside the table.

**TY9 — note (HEAD state).** `e76250cf` placed the 2026-11-09 correction inside the Decision
section, under the example table, as a blockquote. `docs/decisions/README.md` says everything
after acceptance is appended as a dated **Addendum**, never edited in place. The content is
right and dated; the form is the lifecycle's one mutable-after-acceptance shape not used.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 4 minor · 2 note.** The decision is grounded,
candid about its provenance and correctly scoped forward-only; its rule is followable. The
findings are about reach and seams: the posture is contradicted at its own point of use (TY1),
its per-sentence unit leaves the per-entry join it was meant to close (TY2), and later surfaces
apply a stricter posture without either text naming the other (TY3). No MAJOR, so under
`REVIEW.md`'s close rule the application of these rulings closes without a further pass.

### Re-run ledger

| Line | Where | Result |
|---|---|---|
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | worktree root | exit 0; 13 enforced pass, 5 warn-only report 0 |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | worktree root | exit 0; pointerscan advisory 2 (two other pointers' queue state) |
| `git merge-base --is-ancestor 38536e4c HEAD` | worktree root | exit 0 |
| `coldsweep --commit 38536e4c --path ×4` | worktree root | exit 0, body not printed, 0 board files touched |
| scratch probe: leak-scanner terms × state vocabulary, non-barred prose | scratchpad | 0 lines / 0 files over ~840 files |
| `/security-review` | — | NOT RUN (markdown-only delta; dirty tree) |

### Follow-up checklist

- [ ] TY1 reword `RECORD.md` lines 123–124 to the accepted posture.
- [ ] TY2 add the same-entry clause to the paragraph and the ADR's one-question test.
- [ ] TY3 name the name-barred surfaces in the paragraph; cross-reference `namescan`.
- [ ] TY4 fix the item reference; re-specify or defer `030/070` explicitly.
- [ ] TY5 one pointer line at each point of use (closing-entry spec, review-brief skill,
  fleet-pins command).
- [ ] TY6 point the ADR's review line at this file and `160/1090`.
- [ ] TY7 mark part (b)'s answer as a drafter's reading.
- [ ] TY8 one example of a type that is a name.
- [ ] TY9 move the correction into a dated Addendum, or record why not.
- [ ] Reconcile (act 2): verify the option text; re-run the term × state probe over the
  record surfaces, counts only.

### Reconcile (act 2, 2026-11-15 UTC, resumed after the weekly reset)

Opened after act 1 was committed (`b5353ca4`): the held sibling (one file, outside the tree,
released by the orchestrator's message naming its path), the delta's commit body, the queue pointer
`160/1090`, the intent record `260/080`, the ruling-round session record of 2026-11-08 (69 lines),
the brief-writer's session record's board line, `docs/ROADMAP-DONE.md` by grep. The release
message was process only: the path, the barred list, the deliverable's shape. A usage limit cut
the session at about 22:30 UTC with the sibling read and two probes run; it resumed at 23:55 UTC
on the principal's order to finish in-progress work, from the review log.

**The acceptance test, verified as far as the record allows.** The ruling-round record lists
`260/080` among items answered through the device and quotes no option text. The one record of the
option is the intent record's 💬 bullet, written by the authoring run: *"a private repo's
internal state is described by its type only in a public record ('a private child was failing a
check'); naming a repo in any other context stays allowed"*. The ADR's quotation matches it. So the
Decision is faithful to the option as recorded; the option as shown on the device is not in the
repo and cannot be checked from here.

**The author's account (commit body, intent record).** It claims what the delta does and no more:
posture C stated precisely, A and B rejected with reasons, two judgements marked as the drafter's,
`RECORD.md` gains a pointer paragraph, forward only, a cold pass owed at landing. The body does not
claim the pointer landed in the same commit, and the intent record's DONE bullet says the registry
item "can be re-specified", which is the honest form the ADR's Consequences over-stated (TY4). No
finding changes on the author's account.

**Per finding, against the sibling.**

- **TY1** — not among the sibling's questions. Stands.
- **TY2** — the sibling's Q2 (*"Landed a fix for X" discloses a prior condition*) and Q3 (a type
  beside a roster in the same record; does the one-repo reading reach the join across sentences)
  are the same mechanism from two sides. The ADR allows "a fix landed" as an act by design, so the
  inference it invites is accepted exposure, not a defect; the same-entry join is the defect.
  Stands at MODERATE.
- **TY3** — **revised at reconcile, severity lowered to minor.** My act-1 statement that
  `namescan` bars a private repo's name in a commit title was too strong. A probe at reconcile
  compared the leak scanner's local term list (the scanner's and `namescan`'s only term source)
  with the names of the estate's repos: 0 of 31 names are on the list. So today `namescan` cannot
  flag a sibling's name in a title; the contradiction on that surface is latent, becoming live
  only if a name is ever added to the list. The skill-prompt leg stands as written: the
  `fleet-sweep` and `review-drain` prompts (landed 2026-11-14) tell a public-repo session
  *"Never name or point at a private repo, the estate root …"*, which is posture B on a plugin
  surface `PRINCIPLES.md` § 6 names for sweeps, with no cross-reference either way. The ccfleet
  guard those skills cite ("refuses to launch one that contains a configured private name") rests
  on the same term list and so bars no repo name today. Reasoning for the downgrade: the live
  contradiction is between two texts, not between a text and an enforced check, and the stricter
  text is the safe side.
- **TY4** — not among the sibling's questions. Stands.
- **TY5** — the sibling's Q4 asks the same question (silent scope-cut or decision; check the
  templates). Found independently in act 1; the templates checked are listed there. Stands.
- **TY6** — the sibling's Q7 notes the separate commits. Stands at minor; the 51-second series
  meets the rule's intent, and the review line still points nowhere.
- **TY7** — not among the sibling's questions. Stands.
- **TY8** — the sibling's Q3 reaches it (the one-repo reading against the roster). Stands.
- **TY9** — not among the sibling's questions. Stands.
- **Sibling Q5** (*"Ruled 2026-11-08"* beside *"not his own words"*): already answered in the
  tree; `7ad98503` changed the word to "Decided" 51 seconds after the delta, and `PROPAGATION.md`
  uses the "an answer, not a ruling" form eight times. No finding.
- **Sibling Q6** (worked examples keep their names vs `9c8cb7e7`): resolved at HEAD by
  `e76250cf`'s correction, as act 1 recorded; TY9 is about its form only.

**TY10 — minor, formed at reconcile, prompted by the sibling's Q1.** The Decision's type-only
list includes *"the work in flight inside it"*; the Decision's table allows *"Session ran in
`widget-api` to land item X"*. An item under way in a named repo is work in flight inside it, so
the two clauses of the same section disagree on the one example the ADR offers for it. The
resolution the drafter probably intended (a session's presence is an act; the item's content is
the condition) is not written. Breaks: V5, within the Decision. *Counsel:* strike "the work in
flight inside it" from the type-only list or qualify it to the item's content and findings.

**Correction to act 1's assumption 4 and lens 4.** The act-1 probe that returned 0 lines on the
non-barred surfaces used the leak scanner's term list, which holds no repo name, so its zero
measured nothing about this rule; the "false-positive floor of zero" sentence is withdrawn. The
reconcile probe used the estate's repo directory names instead (31 names, public ones included,
none printed; a crude state vocabulary of 20 words), counts only: records, 1,158 files, 1,051
lines name a sibling, 139 put a name beside a state word, **0 of those in any file dated
2026-11-09 or later**; non-barred surfaces, 82 files, 97 name lines, 6 name-beside-state, 0 dated
2026-11-09 or later. Read with care: the 139 is an upper bound over history and includes public
repos and words like "finding" in review ids; what it shows is that the band exists in the
archive at a width the ADR's "~15 lines" under-counts by its narrower probe, and that in the
week since the rule landed no record surface has added to it. The advisory aid the ADR calls
plausible is feasible on this evidence, keyed on a discovered repo list (as item `030/070`
sketched with `pins.discover`), not on the leak scanner's terms.

**The brief-writer's re-run.** Its floor at `c132cc1c` reported pathscan 3 warn-only findings;
at `ce0e1cc2` pathscan is clean on both planes. Resolved since.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 6 minor · 2 note** (TY3
lowered to minor at reconcile; TY10 added at reconcile). No MAJOR, so the application of these
rulings closes without a further pass.
