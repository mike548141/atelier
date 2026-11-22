# Cold pass — the evidence-window rule, the check declaration standard, the pre-flip settings gate, and the pinned review bound

**Board:** `docs/roadmap/160-doctrine-review-owed/1300-rule-4-cold-pass-queued-evidence-window-declaration-settings-gate.md`
**Status:** RUN 2026-11-22 UTC, both acts, sibling folded (PASS-WITH-FINDINGS, 0 MAJOR,
3 MODERATE, 8 minor, 3 notes); findings await the principal's rulings. Brief written 2026-11-14
UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as session `fef270f6`); run 2026-11-22
UTC by a Fable 5.1 reviewer under the 2026-11-23 drain order.

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (self-authored doctrine and a
design every check will be built to).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** medium: one commit, 7 files outside the board store, 366 lines added and 3
removed. About 100 are new `GUARDS.md` doctrine (two sections), 223 a new design note, 19 a new
`AUTONOMY.md` gate, 4 a `REVIEW.md` rule-4 sentence; the rest are pointers and the changelog. No
code.
**Why it earns a review:** four commitments at once, each one others build to. The evidence-window
rule can refuse a check before it is built, and it applies to existing checks too; a wrong rule
either bars sound guards or licenses ones that enforce what they cannot see. The declaration
standard and its schema will sit on every check in the estate, and its census sets how much build
work is owed; a census that is wrong both ways misdirects that work. The pre-flip gate is the last
thing between a private repo and publication; a setting it does not read is published unexamined,
and publication cannot be retracted. The rule-4 sentence governs which commits a cold pass reviews;
a bound that still drifts lets a pass review commits nobody queued, or its own. The worst failure is
a reader trusting any of the four as complete when it is not.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched, which wrote the commit (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `fef270f6`; `$CLAUDE_SESSION_ID` was unset), started 2026-11-14 UTC by an estate health sweep,
  orchestrator session `58027096` (Opus), on the principal's instruction that a brief is written for
  every review known to be owed (Mike, 2026-11-14, verbatim: *"include all briefs are written where
  we know a fable review is required"*). Neither wrote any of this delta. **Off-tier for review,
  disclosed: the brief-writer forms no finding and writes no severity**, and stops after writing.
  It ran no review and used no Fable model.
- **Barred from running this pass:** session `fef270f6` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **all four intent
  records whole**, including the author's landing notes (the line ranges barred below); the first
  three lines of `160/1430` and `160/1440` (to set the non-goals); the unrun brief for `160/1270`
  and its sibling (read for house form). It read the delta and three later `GUARDS.md` hunks
  body-free through `coldsweep`, and **no commit message body**. It opened **no prior verdict
  file**. Its harness also loaded user-level and repo instruction files and a memory index, which
  hold private context this brief does not carry. Everything evaluative it formed is in the
  sibling.

## The acceptance test

The principal's word on all four is a pick from options a session offered, an answer and not a
ruling in his own words. Print it, and the problem each change answers as it was filed before the
work, from the worktree root:

```
sed -n '1,33p'  docs/roadmap/115-guardrail-architecture-mike-commissioned/010-mint-the-evidence-window-rule-as-guard-design.md
sed -n '1,70p'  docs/roadmap/115-guardrail-architecture-mike-commissioned/120-every-guard-declares-the-purpose-it-answers-to.md
sed -n '1,6p'   docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/070-p5-rpi-f10-routed-upward-the-publish-safety-ch.md
sed -n '1,51p'  docs/roadmap/320-child-filed-findings-via-pointing-up/420-a-queued-review-pointer-may-name-a-moving-bound.md
```

His answer is the quoted text, *"Everything, on every check now"* (`115/010` lines 32–33, `115/120`
lines 69–70); the rest of those lines is the offering session's reading of it. `260/070` and
`320/420` carry no answer of his: test whether the delta needed one. `320/420` lines 1–51 and
`260/070` lines 1–6 are child repos' reports, written before the work: evidence, not the author's
account. Test the delta against those words and against what each filed problem asked for.

## What the work is

One commit on `main`, authored 2026-11-09 UTC (stamped 2026-11-10 NZDT):

- **`dd3d60d4`** — `doctrine: land the evidence-window rule and the declaration standard's design`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit dd3d60d4` (subject, stat and diff,
never the body; board files left out). Plain `git show` prints the body before the diff, and
reading is atomic (`REVIEW.md` rule 1), so it is barred. Check first that your tree has the delta:
`git merge-base --is-ancestor dd3d60d4 HEAD` exits 0. The pointer names the bound as "the commit
that closes `115/010`, on `main`"; this brief pins it to `dd3d60d4` (rule 4, the sentence this pass
reviews). Record the pin in your verdict's scope.

Delta paths:

- `docs/method/GUARDS.md`: the scope paragraph at the top, § *Before building a check: the evidence
  window*, § *What every check declares*.
- `docs/decisions/2026-11-09-1334-check-declaration-standard.md` (new): the schema, the readers,
  the warn-first report, the build split, the census of 16 registry checks.
- `docs/method/AUTONOMY.md` § Always confirm: two pre-flip bullets (the settings gate; flip and
  harden as one sitting).
- `docs/build/REPO-STANDARD.md`: the PVR sentence's pointer to the gate.
- `docs/method/REVIEW.md` rule 4: the sentence on pinning a moving bound.
- `docs/decisions/README.md` (one index line) and `CHANGELOG.md` (the 2026-11-09 entry). The
  pointer's path list omits the decisions index; it is in the commit.
- The commit also files a new board item, `260/130` (a tool to read the settings). Read it with
  `--path` if you need it: it is the author's deferral, part of the delta.

**The files have moved since.** Three later commits edit `GUARDS.md` inside or beside these
sections: `ba55be27` (the "none of this is built" paragraph, rewritten when step 0 landed),
`2a6d7a41` (the "Not settled here" allow-marker paragraph, replaced by an answer of 2026-11-12), and
`55f23034` (a commit-message plane, elsewhere in the file). Read each body-free with
`python3 tools/coldsweep.py --root . --commit <sha> --path docs/method/GUARDS.md`. List the rest
with `git log --oneline dd3d60d4..HEAD -- docs/method/GUARDS.md docs/method/AUTONOMY.md
docs/method/REVIEW.md docs/build/REPO-STANDARD.md docs/decisions/2026-11-09-1334-check-declaration-standard.md`.
Judge the delta as landed and as it stands at HEAD, and say whether later changes kept or undid its
claims.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- **Evidence window.** "A guard may only enforce a rule whose licensing context fits inside its
  evidence window"; three questions in order; a check that cannot pass them "is not built".
- "Each outcome has a real case": `datescan` (left directive), `harvestscan` (window widened), a
  floor `flags` declaration (window widened).
- "A check that only warns does not enforce, so this rule does not bar it"; and "that reading of
  'enforce' is this doc's, not his words".
- "It can be shown wrong", with grounds "as the board records them (`115/010`, not re-measured
  here)", and one named counter-case.
- "It applies to existing checks too, and a check that fails it is a finding for the principal,
  never a revert."
- Adopted "on Mike's 2026-11-09 answer"; "the wording is a proposal from `115/010`".
- **Declarations.** Five fields "in one declaration beside its `why`", the fourth requirement
  folded in, "one standard and not two"; "a check that cannot meet a field states that, and is
  marked. None goes red for it and none is unwired for it."
- "Citation is not catch": "a machine can check that a citation resolves and only a reader can pass
  the field." "A replay fails when the check stops firing."
- **Design note.** The schema (`Unmet`, `Grounding`, `Window` with four `fits` values, `Declares`);
  a citation grammar ("prose is not a citation") and a replay grammar; the per-field
  machine/reviewer split table; "a malformed `declares` in a child's `.atelier-floor.json` is
  reported as missing and is never a `ConfigError`: a warn-first field must not be able to fail the
  floor closed"; step 0 as one lane, then groups A–D in series, then group E.
- **Census.** "All 16 registry checks fail the bar today"; "the best meet three of five"; "56 of 80
  fields owed"; the per-check table and totals; "the registry's `why` strings cite nothing in any of
  the 16"; the board's "7 of 15" and "at least four" figures, re-read.
- **Settings gate.** "Every check above reads what the repo contains"; the gate reads and records,
  by named `gh api` endpoints, the wiki, Actions policy, fork-PR approval, private vulnerability
  reporting, and rulesets or branch protection; "where no house value is ruled ... the value read
  goes in front of the confirmation".
- "Branch protection and fork-PR approval cannot be set while a repo is private on the free plan";
  "the flip is not finished until they read back"; "One flip's observation."
- **Rule 4.** "A pointer written in the landing commit cannot name that commit's own SHA, so where it
  names a moving bound such as `..HEAD` the taker pins the bound to a fixed SHA in its claim and
  records the pin in the verdict's scope"; "the one recorded case had grown four commits past the
  landing".
- **Changelog.** "Doctrine and one design note; no scanner or tool changes", and its summary of all
  four.

## Scope

The widest the work admits: intent, decisions, assumptions, design, the doctrine text, the design
note's schema and census against the checks and tests as they stood at `dd3d60d4` and stand now,
and real-world behaviour: the settings gate read live and read-only against this repo. The lenses
organise it; they do not bound it. Anything not named a non-goal is in scope, and a non-goal that
fences off the risk is a finding.

**Non-goals:** the step-0 build in `tools/floor.py` (`ba55be27`, its own pass, `160/1430`), except
where the built code falsifies a design claim; the 2026-11-12 answer that settled the allow-marker
question (`2a6d7a41`, its own pass, `160/1440`), except where it bears on whether this delta's rule
was coherent as landed; `320/420` part (b), the grammar and guard, which stays open; the tool that
would automate the settings read (`260/130`); the earlier pre-flip gate additions (their own pass,
`160/740`); whether any warning becomes a block.

## The four lenses — run all four

1. **Approach and assumptions** (most important). Is a window test the right gate on building a
   check, and is "warn-only does not enforce" a reading that keeps the rule or swallows it? Is a
   declaration on the registry entry the right home, five fields the right set, and a warn-first
   report the right posture for a standard the principal asked for "on every check now"? Is a
   doctrine checklist the right form for a pre-flip settings gate, or only the first step? Does
   pinning "to a fixed SHA" fix the moving bound or only freeze it?
2. **Correctness and quality.** Does each claim above hold against the tree, the tools and the
   platform? Does the census match the checks? Is anything stated as decided that is open, or as an
   answer of his that was not given? Does any sentence overclaim its grounds?
3. **Completeness and harvest.** Every place these four rules must reach (V3): skills, templates,
   the onramp, other method docs, the tool READMEs, the registry, every pre-flip list. Settings the
   gate should read and does not. Checks outside the registry the rule and the standard reach.
4. **Security and privacy** — a must. The settings gate is a publication control: what a missed
   setting exposes, whether its reads need scopes a session should not hold, and whether the
   recorded values themselves leak. This repo is public: whether any of the delta names what a
   public record should describe by type only. `/security-review` cannot reach this delta: it is
   markdown, which that scanner excludes, so a clean pass is empty; say so in one line.

## Load-bearing assumptions to attack

Each is a falsifiable claim. Damage it with a probe or confirm it by re-driving; never by reasoning
alone.

- **LA1.** The evidence-window predicate fits every recorded divergence the `115/010` count names,
  and its counter-case is the only shape that would disprove it.
- **LA2.** Reading *enforce* as excluding warn-only checks leaves the rule able to refuse a build;
  it does not let a check escape by being declared warn-only and staying so.
- **LA3.** Each of the three worked cases is described as the check really behaves.
- **LA4.** The census marks, the per-check table and the totals hold against the checks, their
  docstrings and their tests at `dd3d60d4`; the replays it names exist and fail when the check
  stops firing.
- **LA5.** The schema can express every check in the registry, including warn-only and
  marker-carrying ones, and a malformed declaration cannot fail the floor closed.
- **LA6.** The settings gate reads every setting it claims, by endpoints that return what the gate
  needs, and the settings it names are the ones through which a flip exposes a repo.
- **LA7.** Branch protection and fork-PR approval cannot be set on a private free-plan repo, so the
  unprotected window after a flip is unavoidable.
- **LA8.** A taker pinning the bound "to a fixed SHA in its claim" restores the delta the author
  queued.
- **LA9.** The principal's answer, *"Everything, on every check now"*, licenses landing the
  evidence-window rule and the declaration standard as doctrine, and `260/070` and `320/420`(a)
  needed no word of his.

## Re-run list (V2)

The brief-writer ran every line once on 2026-11-14 UTC at `2c1f0296`, from the worktree root unless
it says otherwise; each exited 0. Re-run them; a line that no longer reproduces is a finding.

```
git merge-base --is-ancestor dd3d60d4 HEAD
python3 tools/coldsweep.py --root . --commit dd3d60d4
python3 tools/floor.py --root . --list
python3 tools/floor.py --root . --declarations
python3 tools/reviewscan.py --root . .
python3 tools/pointerscan.py --root . .
cd tools && python3 -m unittest test_indexscan.DateRule.test_a_line_dated_before_its_file_is_flagged test_pointerscan test_publishscan
```

The last ran 113 tests in about 35 s. To test a census mark at the commit, read the tool and its
test from a scratch checkout of `dd3d60d4` (`git worktree add <scratch> dd3d60d4`), never by
editing your review tree.

**Live reads, read-only.** The settings gate's reads against this repo, each a GET:

```
gh repo view mike548141/atelier --json hasWikiEnabled,visibility
gh api repos/mike548141/atelier/actions/permissions
gh api repos/mike548141/atelier/actions/permissions/workflow
gh api repos/mike548141/atelier/actions/permissions/fork-pr-contributor-approval
gh api repos/mike548141/atelier/private-vulnerability-reporting
gh api repos/mike548141/atelier/rulesets
gh api repos/mike548141/atelier/rules/branches/main
```

Each answered on 2026-11-14 UTC. Test LA7 from platform documentation or a read-only call; **a flip,
or any settings write to test it, is NOT RUN**: no visibility change, no ruleset, no setting. Say
which claims you could not test for that reason.

The delta's recorded proof (V2): "the endpoints were read live against atelier on 2026-11-09" (the
`260/070` landing note, barred until phase 2; the claim is also implied by the delta's endpoint
list). Re-check it by the reads above.

## House rules for this run

- **Live systems:** only the read-only reads above. No live writes, no push from a child, no write
  to GitHub. A check that would need one is marked NOT RUN.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path, and name no child repo.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling (a held-back file, now folded into this file
below the verdict; by count: 16 questions, 12 facts), every item under
`docs/roadmap/160-doctrine-review-owed/` beyond its title, every commit's message body, and these
records beyond the `sed` ranges in *The acceptance test*:

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/010-mint-the-evidence-window-rule-as-guard-design.md`
  (line 34 onward)
- `docs/roadmap/115-guardrail-architecture-mike-commissioned/120-every-guard-declares-the-purpose-it-answers-to.md`
  (line 71 onward)
- `docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/070-p5-rpi-f10-routed-upward-the-publish-safety-ch.md`
  (line 7 onward)
- `docs/roadmap/320-child-filed-findings-via-pointing-up/420-a-queued-review-pointer-may-name-a-moving-bound.md`
  (line 52 onward)

The delta's own `CHANGELOG.md` entry, design note and doc paragraphs carry the author's account of
why; they are the delta, and reading the delta is never barred. `tools/README.md` and the comments
in `tools/floor.py` that describe the declarations are step 0's account, not this delta's: read
them as evidence of what was built, and disclose that you did.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/010-mint-the-evidence-window-rule-as-guard-design.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/120-every-guard-declares-the-purpose-it-answers-to.md \
  --also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/070-p5-rpi-f10-routed-upward-the-publish-safety-ch.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/420-a-queued-review-pointer-may-name-a-moving-bound.md \
  'evidence window|licensing context|Declares|declaration|pre-flip|moving bound|fixed SHA|hasWikiEnabled'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions, LA1–LA9 and
the re-run list. Append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, any orchestrator, what you read, the UTC day), the pinned bound,
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-claim ledger, findings with stable IDs (prefix `EW`:
`EW1`, `EW2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is self-authored doctrine and a design others will build to, so every finding is the
principal's to decide (rule 3): record all, apply nothing. Counsel per finding is welcome, labelled
as counsel and kept beneath it.

---

## Verdict — act 1 (cold pass, 2026-11-22 UTC)

**Status of this pass:** act 1 written 2026-11-22 UTC; act 2 (reconcile) owed; fold by the
orchestrator.

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. The reviewer alone read the delta, answered the lenses, formed every finding and
  assigned every severity below.
- **Spawn:** a headless per-pass orchestrator, session `3715b04c` (Opus 5.5), itself started by
  the drain session `eca14b23` (Opus 5.5), under the principal's drain order of 2026-11-23 NZDT
  (verbatim: *"Start a fable drain or whatever it is called now. Target 100% of weekly budget by
  11.30am NZT todat"*). Both are rule-4 off-tier orchestrators, disclosed here before the
  findings: they hold the context partition, form no finding and write no severity. Neither
  wrote the brief or any of the delta. Neither the reviewer nor either orchestrator was started
  or instructed by the barred sessions `fef270f6`, `58027096` or `d0ca5d24`, and no contact with
  the author came after the spawn.
- **Orchestrator direction received** (process only, summarised; no question about the delta, no
  pointer to risk): the worktree and brief paths; read the brief and `REVIEW.md`; run commands
  with absolute paths; the partition (the `.deferred.md` sibling removed from the tree, not to be
  recovered from history or other checkouts; rule-2 material barred until act 2); live systems
  read-only with field allowlists; `nice`, one suite at a time, single process; write only this
  file and a private running log; act-1 verdict shape as the brief lists it; stop after act 1 and
  wait for the release message.
- **Worktree:** a review worktree of this repository at `4613ca76`, detached, holding the delta
  (`git merge-base --is-ancestor dd3d60d4 HEAD` → exit 0). Read-only to the reviewer except this
  file. Its only working-tree change is the sibling's deletion, which is the partition.
- **What was read, in order:** this brief whole; `docs/method/REVIEW.md` (rules 1–4, lenses,
  V1–V7, lifecycle, the method-record ruling, the macro/micro list); the four acceptance-test
  `sed` ranges exactly as given; the delta body-free (`tools/coldsweep.py --commit dd3d60d4`,
  exit 0, 7 files, 366+/3−); the three later `GUARDS.md` hunks body-free; the author's deferral
  item `260/130` by `--path` (disclosed: a board file); `GUARDS.md`, `AUTONOMY.md`, `REVIEW.md`,
  `REPO-STANDARD.md`, the design note and `CHANGELOG.md` at HEAD; `tools/floor.py` and the
  sixteen tools and test modules at a scratch checkout of `dd3d60d4` (removed before this was
  written); `tools/floor.py`, `tools/README.md` § flipcheck and `tools/flipcheck.py`'s docstring
  at HEAD (step-0-class evidence of what was built after the delta, disclosed); board items
  `260/110` and the `docs/method/census/` rows the sweep surfaced; GitHub's plans page and the
  Actions-permissions REST reference, read-only. **Not read:** the session log, any prior verdict,
  the sibling, any commit body, any `160/` item beyond its title, the four records past their
  `sed` ranges. The onramp's board index and commit subjects were met; none read as the author's
  account.
- **Pinned bound:** the pointer's "the commit that closes `115/010`, on `main`" is pinned to
  **`dd3d60d4`** (one commit), as the brief pins it; the pin is recorded here as the scope. The
  delta is also judged as it stands at HEAD `4613ca76`.

### Per-lens answers

**Lens 1 — approach and assumptions.** A window test is the right gate on building a check: it
asks the one question that the recorded build failures could have answered before code (the
three worked cases hold against the tools, LA3). Its weak joint is the carve-out: *"a check that
only warns does not enforce, so this rule does not bar it"* keeps the rule only while the check
stays warn-only, and nothing — in the doctrine, the design or the built reader — re-asks the
question when a warn becomes a block (EW1). A declaration on the registry entry is the right
home (the principal ruled the slot, 2026-08-23), five fields are a defensible set, and warn-first
is the posture his earlier words set for new checks; "on every check now" is met in form by
step 0. A doctrine checklist is a first step for a pre-flip settings gate, and the delta says so
by filing the tool; but the list is the child's five findings carried over, with no enumeration
of what a flip exposes, so it cannot say whether it is complete (EW3). Pinning to a fixed SHA
fixes the reviewed delta and only freezes the bound; later edits to the same surfaces depend on
each queuing its own pointer, which the sentence does not say (EW6).

**Lens 2 — correctness and quality.** The claims hold against the tree with these exceptions:
two census cells are contradicted by the test module they describe and the ❌ propagated into
step 0 (EW2); the "private on the free plan" cause bundles a plan-gated setting with a
visibility-gated one (EW5); the design note's *Not decided here* and *Status* are stale at HEAD
(EW4, EW9). Nothing is stated as his ruling that was not given: the two answers are quoted and
labelled answers, and the "enforce" reading is owned as the doc's. The census's "best meet three
of five" is a reader's count the machine reads as 2/5 (EW7).

**Lens 3 — completeness and harvest.** Mirror sites: `REPO-STANDARD.md` points at the gate (one
home, V4 kept); `REVIEW.md` rule 4 carries the sentence; the census docs of 2026-11-16 index all
four as rows (GRD7, GRD9, AUT8, REV16). No skill, command or template restates the gate, the
window rule or the declaration standard, so there was nothing to sweep (V3 discharged); the
create-repo skill and the `CLAUDE.md` template carry only the visibility fact. Checks outside the
registry the rule reaches are named by the design (group E) and the three checks added since
arrived with a `Declares` (`floor.py --list` shows `decl n/5` on all 19). Settings the gate
should read and does not: EW3.

**Lens 4 — security and privacy.** `/security-review` cannot reach this delta: markdown is
excluded by that scanner, so its clean pass is empty and is weighed as nothing. The gate is a
publication control and its design enumerates no threats; the live reads against this repo show
exposure- and protection-bearing settings it does not read (EW3). The reads it names need the
`repo` scope and, for Actions permissions, repository admin, which a session that can flip a
repo already holds; the recorded values (policy words, ruleset names, booleans) carry no secret
and may sit in a public record. The delta names the child by type only ("the first child's
post-flip review", "the networking case"): nothing a public record should describe by type is
named. Reads for this pass printed allowlisted fields only.

### V1–V7

- **V1.** Mostly held; three overclaims, each small: the free-plan cause (EW5), the design note's
  Status at HEAD (EW9), and the census legend not matching its marks (EW2).
- **V2.** Every line of the re-run list re-run (ledger below); all reproduce. The implied proof
  "the endpoints were read live" re-checked: all seven answered on 2026-11-22.
- **V3.** Discharged with grounds: no restatement surface outside `docs/` exists for these four
  rules (sweep and grep of `skills/`, `commands/`, `docs/build/templates/`).
- **V4.** Kept: `REPO-STANDARD.md` points, does not copy. One drift: the open allow-marker
  question is now answered in `GUARDS.md` and still open in the design note (EW4).
- **V5.** Two contradictions at HEAD, both time-made: EW4 and EW9. Cross-references checked for
  the rule reached: the design note's link to `GUARDS.md` § *What every check declares* reaches
  that section; `REPO-STANDARD.md`'s pointer reaches the gate bullet in § Always confirm;
  `GUARDS.md`'s link to the design note resolves.
- **V6.** Run as lens 4; EW3 is its finding.
- **V7.** Provenance stated in the brief and repeated above.

### Load-bearing assumptions — damaged or confirmed

- **LA1 — part-confirmed, not probed to the count.** The three worked cases match the tools; the
  counter-case shape is the right negation of the predicate. The divergence count the grounds
  rest on lives in `115/010` past line 33 and in `docs/reviews/`, both barred until act 2; the
  delta itself says "not re-measured here" (honest, V1). Re-measured at reconcile.
- **LA2 — damaged (EW1).** Probe: `floor.py` at HEAD checks `Window.fits` for membership only
  (line 3313); `WINDOW_FITS` has no tie to `warn_only`; three checks carry `outside-warn-only`;
  the indexscan and pathscan registry comments call the flip to blocking "one visible argument
  and a separate ruling" and name no re-run of the window questions; `GUARDS.md` and the design
  note contain no such sentence (grep). A check can be declared warn-only, pass the gate, and
  later block on a context it cannot see with the gate never asked again.
- **LA3 — confirmed.** `datescan.py` lines 7 and 121–124 (the third clause "NOT mechanically
  checked", intent unseen); `harvestscan.py` lines 40–70 (the widening measured by `--replay`,
  two folds); `floor.py` line 163 (`flags` → `leakscan --disable ipv4` with its `why`);
  `pointerscan` registry `warn_only=True`, "judgement-adjacent text"; `harvestscan` registry
  "cannot ground its constant".
- **LA4 — damaged in two cells (EW2); otherwise confirmed.** All four ✅ replays exist at
  `dd3d60d4` (`test_publishscan.py:43`, `test_pointerscan.py:106`, `test_board.py:758`,
  `test_indexscan.py:242`); the two posture ✅ are declared in registry comments (`floor.py`
  lines 626–648, 833–835) and nowhere else carries either word; the 16 `why` strings cite no
  document. `test_licenscan.py` lines 100–108 hold a firing test tied to a named review finding.
- **LA5 — confirmed with one gap.** `_load_declares` (HEAD lines 1808–1840) returns `None` on
  any shape error, never a `ConfigError`. Warn-only checks fit as `outside-warn-only`. A
  marker-carrying check has no `fits` value of its own: after the 2026-11-12 answer a reasoned
  marker brings the context inside, so it reads `inside`, and `leakscan`'s HEAD window text
  still waits on the question (EW4, note).
- **LA6 — damaged in part (EW3).** Each of the five settings answers by the named endpoint
  (seven GETs, 2026-11-22). The settings it names are some of those through which a flip exposes
  a repo, not all: read-only GETs on this public repo returned `has_issues: true`,
  `has_projects: true`, `allow_forking: true`, `secret_scanning: disabled`,
  `push_protection: disabled`, and the wiki, pages and discussions off.
- **LA7 — half damaged (EW5).** Branch protection: GitHub's plans page lists "Protected branches"
  under Pro and Team as a private-repository feature and not under Free, so on Free it is
  public-only (holds). Fork-PR approval: the private-repository counterpart is a different
  endpoint, which answered HTTP 422 "not allowed for public repositories" on this repo, and the
  approval endpoint is documented for public forks: it is unavailable on a private repo on every
  plan. Both halves make the window unavoidable; the stated cause is wrong for one. Could not be
  tested by a flip or any write (NOT RUN, by the brief). Rulesets: the docs name Team and
  Enterprise, yet this Free public repo has an active ruleset, so platform docs and reads
  disagree; the delta's "One flip's observation" is the right hedge.
- **LA8 — confirmed as far as it goes (EW6).** `git rev-list --count dd3d60d4..2c1f0296` = 58;
  17 of them touched the delta's paths. The pin restores the queued delta exactly. What it does
  not do is say that later commits on the same surfaces are reviewed only by their own pointers;
  `pointerscan` has no handling of a symbolic bound (grep empty; part (b) open, as the delta
  says).
- **LA9 — confirmed.** *"Everything, on every check now"* was put to him with `115/010` and
  `115/120` together (both items record it); it licenses landing both as doctrine with the
  cost named. `260/070` adds a stop to the always-confirm floor, a narrowing: `AUTONOMY.md`
  (lines 120–124) requires his words to *widen* authority, not to add a stop, so no word of his
  was owed; `320/420`(a) writes down the practice the one instance used. Both are self-authored
  doctrine and are reviewed by this pass, which is the rule-4 answer.

### Per-claim ledger

| Claim (as extracted in the brief) | Result |
|---|---|
| Evidence-window predicate; three questions; a failing check "is not built" | Holds; carve-out gap EW1 |
| Each outcome has a real case (`datescan`, `harvestscan`, `flags`) | Holds (LA3) |
| Warn-only does not enforce; the reading is the doc's, not his | Honest; gap EW1 |
| "It can be shown wrong"; grounds not re-measured; one counter-case | Holds as stated; LA1 deferred |
| Applies to existing checks; a failure is a finding, never a revert | Holds; consistent with GRD2 |
| Adopted on the 2026-11-09 answer; wording from `115/010` | Holds (acceptance test) |
| Five fields in one declaration; none goes red or is unwired | Holds; built so (step 0) |
| Citation is not catch; a replay fails when the check stops firing | Holds; GRD10 says the tool checks resolve only |
| Schema; grammars; machine/reviewer split; malformed → missing | Holds (LA5) |
| Step 0 one lane, then groups A–D, then E | Holds; E's new checks carry `Declares` |
| All 16 fail; best meet three of five; 56 of 80 owed; per-check table | Two cells wrong (EW2); counts differ from the tool's (EW7) |
| `why` strings cite nothing in any of the 16 | Holds |
| "7 of 15" and "at least four" re-read | Holds as stated |
| Gate reads five settings by named endpoints; unruled value in front | Endpoints answer; list un-enumerated (EW3) |
| Branch protection and fork-PR approval unavailable on private free plan | Half right (EW5) |
| Rule 4: taker pins a moving bound; one case grew four commits | Holds; silent on later commits (EW6) |
| Changelog: doctrine and one design note, no tool changes | Holds at the commit |
| Design note Status "nothing built and no check changed" | False at HEAD since 2026-11-10 (EW9) |

### Findings

- **EW1 — MODERATE — the warn-only carve-out has no re-entry.** `GUARDS.md` § *Before building
  a check* exempts a check that only warns, and neither that section, the design note nor the
  built reader re-runs the three questions when a warn-only check moves to blocking.
  `Window.fits = "outside-warn-only"` is a terminal value (`floor.py` line 3313 tests membership
  only; three checks carry it at HEAD); the registry comments make the flip to blocking "one
  visible argument and a separate ruling" with no window re-check named. So a check can be
  declared warn-only, pass the gate, and later block on a rule whose licensing context it cannot
  see, which is what the rule exists to refuse. *Counsel:* one sentence in the section — a move
  from warn to block re-asks the three questions and rewrites `fits` — and a `test_floor.py` pin
  that a non-`warn_only` check may not carry `outside-warn-only`.
- **EW2 — MODERATE — two census cells contradict the tests, and the ❌ propagated.** `licenscan`
  *Incident and replay* ❌: `tools/test_licenscan.py::test_only_suffix_header_still_blocks`
  ("the end-to-end teeth for B2": a GPL-2.0-only header in a permissive repo must block) is a
  firing test tied to a named review finding, and the schema's own `Grounding.incident` grammar
  admits "a verdict path", so the legend gives 🟡 at least. `licenscan` *Rule* ❌: its docstring
  cites `115/290` (ruled 2026-10-16) and `AUTONOMY`'s making-public floor; the legend's 🟡 is
  "names a document, a board item or a review with no section". Step 0 wrote both as
  `Unmet("no incident named")` and `Unmet("no rule text cited")` (`floor.py` lines 1281–1287 at
  HEAD). The root is the legend: its 🟡 wording does not say the citation must be *of the rule
  served* or the incident *of the defect class*, so the ❌ cells for `publishscan` and
  `licenscan` (Rule) and `spellscan`, `wrapscan`, `licenscan` (Incident) cannot be re-derived
  from it; for `spellscan` and `wrapscan` the tests name exemption findings (SS1, SS3, WS2,
  WS4), so ❌ is right on the standard's definition and wrong on the legend's words. *Counsel:*
  restate the legend (a citation *of the rule the check serves*; an incident *of the defect
  class the check exists to catch*), re-mark `licenscan`, and let "56 of 80" move.
- **EW3 — MODERATE — the settings gate enumerates no threats, and misses settings a flip
  changes.** The five settings are the child's P5 findings carried over; `REVIEW.md` lens 4
  makes threat enumeration a first-class design step and its absence the finding. Read-only
  GETs against this repo on 2026-11-22 returned settings the gate does not read: secret
  scanning and push protection both `disabled` (free on public repos, so a flip is the moment
  they become available and are missed), `has_issues: true` (the inbound surface `publishscan`'s
  F1 grounding names), `has_projects: true`, `allow_forking: true`, and `has_pages`,
  `has_discussions` (off here; each a publication or inbound surface), plus deploy keys,
  webhooks and Actions secrets (0, 0, 0 here), which `AUTONOMY.md` already names as "new trust
  surfaces". `flipcheck.py` reads the same five. The bullet "The gate reads the platform's
  settings, not only the tree" reads as complete. This is the finding nearest MAJOR: the brief's
  worst failure is a setting published unexamined. *Counsel:* a short enumeration in the design
  (content planes: wiki, pages; inbound: issues, discussions, fork PRs and their workflows;
  trust: keys, hooks, secrets, apps; protection: rulesets, push protection), the read list
  derived from it, and the "no house value" rule applied per setting.
- **EW4 — minor — the allow-marker question is answered in one home and open in another.**
  `GUARDS.md` at HEAD (2a6d7a41) records the 2026-11-12 answer; the design note, untouched since
  landing, still says *Not decided here: whether an allow-marker brings a licensing context inside
  the window* and that group A "cannot finish without it"; `leakscan`'s HEAD window text still
  waits on it. *Counsel:* one line in the design note pointing at the answer; the registry text
  is `160/1430`'s.
- **EW5 — minor — one cause for two differently gated settings.** "Branch protection and fork-PR
  approval cannot be set while a repo is private on the free plan": branch protection is
  plan-gated (public-only on Free), fork-PR approval is visibility-gated on every plan (its
  private counterpart is a different endpoint; HTTP 422 on this public repo). The hardening step
  after a flip is the same, so the rule's effect stands; the stated cause is half wrong, and the
  design-note deferral item repeats it. *Counsel:* "cannot be set on a private repository (fork-PR
  approval, any plan; branch protection, on the free plan)".
- **EW6 — minor — the pin freezes the bound and says nothing about what it leaves out.** The
  rule-4 sentence restores the queued delta (58 commits, 17 on the delta's paths, would have
  been swept by a literal `..HEAD` at the brief-writer's HEAD) but is silent that later commits on
  the same surfaces are reviewed only by their own pointers, which landing = queuing requires and
  nothing checks (part (b) open). A taker could read the pin as closing them. *Counsel:* one
  clause: "later commits on the same surfaces stay with their own pointers".
- **EW7 — note — two counts of one thing.** The census's "the best meet three of five" is the
  reader's count; `floor.py --declarations` at HEAD reads the best at 2/5 and "0 meet all five",
  because the machine says only `resolves` for Rule. The design says the machine says less, so
  this is not a contradiction, but the totals will be compared. *Counsel:* one sentence in the
  census saying the tool's `n/5` reads lower by design.
- **EW8 — note — LA1 deferred.** The divergence count behind "It can be shown wrong" is in
  barred material; the delta says "not re-measured here". Re-measured at reconcile.
- **EW9 — minor — the design note's Status is stale at HEAD.** Its header reads "proposed (design
  only; nothing built and no check changed)" and the decisions index says "design only", while
  step 0 landed 2026-11-10 and every registry check carries a `Declares`. `GUARDS.md` was updated
  for it (ba55be27); the note and the index were not. *Counsel:* a dated Status line and index
  phrase.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE (EW1, EW2, EW3), 4 minor (EW4, EW5, EW6, EW9),
2 notes (EW7, EW8).** Every finding is the principal's to decide (rule 3); nothing applied.

### Re-run ledger (V2)

| Line | Result 2026-11-22 UTC |
|---|---|
| `git merge-base --is-ancestor dd3d60d4 HEAD` | exit 0 |
| `coldsweep.py --root . --commit dd3d60d4` | exit 0; 7 files, 366+/3−, body not printed |
| `floor.py --root . --list` | exit 0; 19 checks, `decl n/5` column present |
| `floor.py --root . --declarations` | exit 0; "21 checks, 0 meet all five" |
| `reviewscan.py --root . .` | exit 0; 254 briefs clean |
| `pointerscan.py --root . .` | exit 0; 877 files, 1162 items |
| `cd tools && python3 -m unittest …` (three targets) | OK, 114 tests in 38.9 s (brief: 113) |
| Seven live GETs | all answered; wiki off, PUBLIC, Actions all/read, approval `first_time_contributors`, PVR enabled, one active ruleset, three branch rules |

Each tool was run as `/usr/bin/python3 tools/<x>.py` under `nice`, one at a time. **NOT RUN:**
any flip or settings write (LA7's "cannot be set" tested from documentation and GETs only).

### Follow-up checklist

- [ ] Principal rules on EW1–EW9 (rule 3); the author may add counsel beneath each.
- [ ] Act 2: open the sibling and the barred records; re-measure LA1; screen the commit body;
      append `### Reconcile`.
- [ ] If EW2 is accepted: re-mark `licenscan`, restate the legend, re-total; step 0's `Unmet`
      text follows under `160/1430`.
- [ ] If EW3 is accepted: the enumeration lands in the design note and `AUTONOMY.md`, and
      `flipcheck.py`'s read list follows under `260/130`.
- [ ] If EW1 is accepted: the re-ask sentence in `GUARDS.md` and a `test_floor.py` pin.
- [ ] EW4, EW5, EW9: one-line edits, each a doctrine or design-note edit that queues its own
      pointer.

### Reconcile (act 2, 2026-11-22 UTC)

Act 1 was committed unrevised (`dbfee578`, on `origin/main`) before the orchestrator released the
sibling by path. Then read, in this order: the sibling (16 questions, 12 facts); the four records
past their `sed` ranges (`115/010` line 34 on, `115/120` line 71 on, `260/070` line 7 on,
`320/420` line 52 on); the queue pointer `160/1300` whole; the commit body of `dd3d60d4`; the
titles of `160/1430` and `160/1440`; the overall lines of the six first-of-kind scanner cold
passes of 2026-07-23 to 2026-07-29 and the Status line of the unrun step-0 brief
(2026-11-14-0318). No prior verdict on this delta exists. Act-1 text above is unchanged.

**The author's account.** The commit body matches the delta: it names the answer as an answer
to options "offered on `115/010` and `115/120`", calls the design note design only, says the
census sizes the build, and files the gate and the rule-4 sentence as two small unrelated gaps.
The landing notes in the four records say the same, and `260/070`'s note carries the proof the
brief flagged (*"The endpoints were read live against atelier on 2026-11-09"*), re-run clean in
act 1. The pointer's three questions are the sibling's 1–3. Nothing in the account changes an
act-1 severity.

**Per-finding notes against the sibling's questions.**

- **EW1** answers Q2 and Q7 directly: nothing ties a move from warn to block to the window
  question, and the sibling's reading ("a separate decision with a date and a fleet probe first")
  is the design's only sentence on the move. Stands, MODERATE.
- **EW2** answers Q1. The sibling's fact 3 says the brief-writer "did not check any mark against
  its tool"; act 1 did, and found the two `licenscan` cells. `115/120`'s step-0 note confirms the
  propagation route: fields "without a ✅ in the census are `Unmet` with the reason". Stands.
- **EW3** answers Q3 and Q13. The sibling's fact 10 lists the same unread settings (the
  `security_and_analysis` block, pages, discussions, projects, forking) and adds environments
  and their secrets, Actions variables, collaborators and teams; the counsel's enumeration should
  take those too. On Q13's last question: the sentence "every settings finding in the first
  child's post-flip review came through that gap" grounds the five named and says nothing for
  completeness; the finding is that the bullet reads as if it did. Stands.
- **EW4** answers Q6 in part. Fact 6 agrees (`_MARKER_OPEN`, `floor.py` line 618 at HEAD). On the
  day it landed the rule was decidable for marker-leaning blocking checks only as "outside, way
  out not yet named", which is what step 0 then wrote; the rule itself was coherent, its answer
  pending. Stands, minor.
- **EW5** answers Q14. The gate does not say what an organisation or paid plan changes;
  `flipcheck.py` says only that a 403 or 404 is printed as *not available*. "One flip's
  observation" is the honest hedge and is enough for a doctrine that *names* the window; it would
  not be enough for one that accepted it silently, and this one does not. Stands, minor.
- **EW6** answers Q15 and gains a fact (EW11 below). The sentence says "a fixed SHA", not "the
  landing commit", so `HEAD` at claim time satisfies its letter while repeating the recorded
  defect. Stands, minor; EW11 carries the new fact.
- **EW7** answers Q10 in part: `floor.py --declarations` at HEAD prints "✅ grounding met" for
  `pointerscan` and `publishscan` on a resolving replay, while Rule prints `resolves`. See EW13.
- **EW8 → re-measured (Q4).** The six first-of-kind passes exist as files: `datescan` S3 and
  `spellscan` S5 (2026-07-23, PASS-WITH-FINDINGS, each directing a narrowing), `wrapscan` S1
  (2026-07-23, 1 MAJOR), `pathscan` S2 (2026-07-26, 3 MAJOR with "line-level narrowing
  documented"), `stampscan` S4 (2026-07-26, on declared narrowing), `harvestscan` B4
  (2026-07-29, the shelve-then-wire case, 1 MAJOR). Each shows a sound engine whose scope was
  cut on contact with the corpus, which is the shape `115/010` names. The "four killed or
  shelved" and "about one build in three" figures are not re-derived here: `115/010` cites no
  files for them and the count would need every build's record. The rule's grounds therefore
  hold in shape and are unverified in count; the delta says so ("not re-measured here"), which
  V1 accepts. Stays a note; *counsel:* cite the passes by file in `GUARDS.md` so the count can be
  re-derived.
- **EW9** answers Q8. Which binds a session building a check today: `GUARDS.md` (adopted, step 0
  built, "binds as a review question" for passing a field); the design note's "proposed, nothing
  built" is false at HEAD and a reader of the note alone does not learn it. Stands, minor.
- **Q5 (the "finding for the principal" clause).** No board item was filed for any blocking check
  that fails the window; the clause's only trace is the `Unmet` window marks step 0 wrote. See
  EW12.
- **Q9 (one `fits` for two planes).** The schema has one `fits` with `hook` and `ci` as prose;
  no registry entry at HEAD is inside on one plane and outside on the other, so the limit has not
  bitten. The third outcome, "not built", has no value by design: a check that is not built has
  no entry. Noted, no finding.
- **Q11 (board items as citations).** `_citation_problem` (`floor.py` lines 3209–3213) resolves
  `board NNN/NNN` by globbing the live section directory only; an item that moves to an archive
  store would read "no such board item". See EW14.
- **Q12.** Answered by EW10 below.
- **Q16.** Act 1's LA9 stands. The bridge from the `115/120` answer to `115/010` is the offering
  session's reading ("Also answers `115/010`") and the commit body's "offered on `115/010` and
  `115/120`"; both items record the one answer. "Adopted on his answer" and "wording is a
  proposal from `115/010`" both hold: he picked the option, the item supplied the words.
  `260/070` (a floor stop, a narrowing) and `320/420`(a) (practice written down) needed no word
  of his; both are self-authored doctrine, which this pass is the rule-4 answer to.

**Findings formed at reconcile** (each marked as such; the sibling's question that led there is
named; each rests on a probe run in act 2):

- **EW10 — minor, formed at reconcile (Q12) — the gate's named endpoints do not read classic
  branch protection.** The bullet says "rulesets or branch protection (`rulesets`,
  `rules/branches/<branch>`)". `rules/branches/<branch>` returns ruleset rules only: on this repo
  the three rules it returned all come from the one ruleset, and
  `branches/main/protection` answered 404 "Branch not protected" (GET, 2026-11-22). A session
  following the doctrine by hand never reads classic protection; `flipcheck.py` does
  (`read_protection`, the `branches/<branch>/protection` call), so the tool exceeds the
  doctrine it implements. *Counsel:* name the third endpoint in the bullet.
- **EW11 — minor, formed at reconcile (Q15) — the delta's own pointer was not queued in the
  landing commit.** `git log --diff-filter=A -- <pointer path>` → `a7481611` ("board: queue the
  cold pass …"), committed one second after `dd3d60d4`; `coldsweep --commit dd3d60d4` lists no
  `160/` file. The delta that added the moving-bound sentence to rule 4 landed and queued in two
  commits, the TA9 shape (intent met, letter not). Two consequences: the sentence's premise ("a
  pointer written in the landing commit cannot name that commit's own SHA") did not apply to its
  own case, where the follow-up pointer could have named `dd3d60d4` and did not; and part (b)'s
  proposed resolver, "the commit that adds this file", would here resolve to the wrong commit,
  so (b) needs the follow-up case stated before it is built. *Counsel:* the rule-4 sentence
  names the landing commit as the pin's default and the pointer names the SHA whenever it is
  written after the landing.
- **EW12 — note, formed at reconcile (Q5) — the "finding for the principal" clause left no
  finding.** "It applies to existing checks too, and a check that fails it is a finding for the
  principal, never a revert": no board item was filed for any blocking check marked short on
  Window; the `Unmet` marks in step 0 are reported on `--declarations` and the CI line and
  reach no ruling. The clause is not inert, since the marks exist, but its "finding" has no home
  he reads. *Counsel:* say where such a finding is filed (a board item under `115`, or the
  registry mark counts as filed).
- **EW13 — minor, formed at reconcile (Q10) — the machine says `met` for a resolving replay.**
  The design's split table gives Rule `resolves` and Grounding `met` "if every replay resolves",
  though both are existence checks; `floor.py --declarations` at HEAD prints "✅ grounding met"
  for `pointerscan` and `publishscan`. A replay that still passes with the check removed reads
  `met`, which is the "citation is not catch" defect in the next column. *Counsel:* the machine
  word is `resolves` for Grounding too; `met` waits on `reviewed`, as Rule does; what would catch
  an inert replay is a mutation run (the check disabled, the replay must fail), which no reader
  does today.
- **EW14 — minor, formed at reconcile (Q11) — a board-item citation rots when the item moves.**
  `_citation_problem` resolves `board NNN/NNN` against `docs/roadmap/NNN-*/NNN-*.md` only; an
  item moved to an archive store (`990-…` exists) stops resolving and the field drops to
  `unmet` with "no such board item". The standard's own "never restated" test wants a rule home,
  and a board item is a record that closes and moves. *Counsel:* either the grammar names the
  archive store as a second place to look, or a board item counts as grounding (an incident)
  and not as the rule served.

**Overall, restated:** **PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE (EW1, EW2, EW3), 8 minor
(EW4, EW5, EW6, EW9, EW10, EW11, EW13, EW14), 3 notes (EW7, EW8, EW12).** Of the fourteen, five
(EW10–EW14) were formed at reconcile from the sibling's questions and are marked so. Every
finding is the principal's to decide (rule 3); nothing applied. The sibling is folded in by the
orchestrator below this line; it is not folded here.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

The text below is the brief's held-back sibling, verbatim, as the brief-writer wrote it on
2026-11-14 UTC. It was partitioned out of the review tree before the reviewer started, held
outside the repository while act 1 ran, and released to the reviewer only after act 1 was
committed and pushed (`dbfee578`). The reviewer read it for act 2 (`### Reconcile` above). The
off-tier orchestrator (session 3715b04c, Opus 5.5) folded it here and forms no finding; only its
headings are demoted two levels so they nest under this one.

### Held back — the evidence-window rule, the check declaration standard, the pre-flip settings gate, and the pinned review bound

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `fef270f6`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

#### The pointer's own questions

1. Do the census's marks hold against the checks themselves?
2. Does reading *enforce* as excluding warn-only checks swallow the rule?
3. Does the settings gate read every setting it claims?

#### The brief-writer's questions

4. The rule's grounds are "the board's count, not re-measured", yet it lands as doctrine that can
   refuse a build and judge every existing check. Is a rule whose own test was never run on its
   grounds stated with the strength its evidence supports (V1)? Can the four cold passes and four
   killed builds be re-derived from the record, and does each really show a licensing context
   outside the window?
5. "It applies to existing checks too, and a check that fails it is a finding for the principal."
   The census marks Window short of the bar on several checks that block. Did the delta, or
   anything since, file those findings? If not, is the clause inert?
6. As landed, the rule left open whether an allow-marker brings the licensing context inside the
   window, while several blocking checks lean on markers. Was the rule decidable for those checks
   on the day it landed? (`2a6d7a41` answered it later; that edit is `160/1440`'s subject.)
7. A warn-only check escapes the rule. What makes a check that later moves from warning to block
   face the window question again? The design note says a move to blocking is a separate decision
   "with a date and a fleet probe first"; does any doctrine tie that move to this test?
8. `GUARDS.md` says the rule was "adopted" and the standard binds "as a review question"; the design
   note's status is "proposed". Which one binds a session building a new check today, and does a
   reader of either learn that?
9. `Window.fits` is one value per check, but the rule asks about "every plane the check runs on",
   and `hook` and `ci` are separate strings. Can the schema state a check that is inside on one
   plane and outside on another? Has the rule's third outcome, "the check is not built", any value,
   or is it meant to have none?
10. The machine column passes Grounding as `met` "if every replay resolves", while the doctrine
    says a replay passes only if "the test fails if the check stops firing". Is a machine `met` on
    that field consistent with "citation is not catch"? What would catch a replay that still
    passes with the check removed?
11. The citation grammar admits `board 320/200`. A board item is a record that changes, closes and
    moves to the archive store. Is a board item a rule a check can serve, by the standard's own
    "never restated" test?
12. The gate names "rulesets or branch protection" and reads `rules/branches/<branch>`. That
    endpoint returns ruleset rules; classic branch protection is a separate endpoint (fact 9). Does
    the gate read classic protection at all?
13. Settings the gate does not name: the repo-level `security_and_analysis` block (secret scanning,
    push protection, Dependabot), Pages, Discussions, Projects, forking, deploy keys, webhooks,
    environments and their secrets, Actions secrets and variables, collaborators and teams. Which
    does a flip change the exposure of? Is "every settings finding in the first child's post-flip
    review came through that gap" grounds for the five named, or for completeness?
14. LA7: is it true on the current free plan that branch protection and rulesets cannot be set on a
    private repo, and that fork-PR approval (a public-repo setting) cannot be set before the flip?
    If an organisation or paid plan changes that, does the gate say so? Is "One flip's
    observation" enough grounds for doctrine that accepts an unprotected window?
15. The rule-4 sentence says the taker "pins the bound to a fixed SHA in its claim". Any fixed SHA,
    including `HEAD` at claim time, which in the recorded case already sat four commits past the
    landing. Does the sentence say the pin is the landing commit? Rule 4 already puts the pointer in
    the landing commit, so the commit that adds the pointer is the landing: is that derivable now,
    without part (b)?
16. The principal's answer was put to him with `115/120`'s options; `115/010` said the decision to
    land its rule at all was his. Did *"Everything, on every check now"* answer that? `GUARDS.md`
    says both "adopted on Mike's 2026-11-09 answer" and "the wording is a proposal from
    `115/010`"; can both hold? `260/070` adds to the always-confirm list and `320/420`(a) changes
    rule 4, with no word of his recorded on either: was one needed?

#### Facts read off the machine (2026-11-14 UTC, worktree at `2c1f0296`)

1. Re-run lines, all exit 0: `merge-base --is-ancestor dd3d60d4 HEAD`; `coldsweep --commit
   dd3d60d4`; `floor.py --list`; `floor.py --declarations`; `reviewscan` ("clean — 8
   post-2026-07-21 decision record(s) carry a review line; 238 review brief(s) …"); `pointerscan`
   ("clean — every queued-review pointer is refs-only and current"); the unit-test line, 113 tests
   OK in about 35 s. Python 3.14.6.
2. `dd3d60d4` touches no file under `tools/`. At that commit `tools/floor.py` holds 16 `why="`
   registry strings, matching the census's 16.
3. The census table is internally consistent: its ✅ counts are 5 + 3 + 9 + 5 + 2 = 24 of 80, so 56
   owed; no row has five ✅; three rows (`leakscan`, `pointerscan`, `sizescan`) have three. The
   brief-writer did not check any mark against its tool.
4. The replays the census marks ✅ exist at HEAD: `tools/test_indexscan.py` `DateRule` line 226 and
   `test_a_line_dated_before_its_file_is_flagged` line 242; `tools/test_pointerscan.py`
   `test_the_live_specimen_is_flagged` line 106; `tools/test_publishscan.py`
   `test_the_grounded_pattern_reds` line 43; `tools/test_board.py` `StagedPlane` line 836. Whether
   each fails when its check stops firing was not probed.
5. At HEAD `floor.py --declarations` prints "21 checks, 0 meet all five". `--list` shows 19 checks
   on the hook and CI planes; `--list --plane msg` shows the other two, `namescan` and `quotescan`.
6. At HEAD `tools/floor.py` lines 614–621 still say the allow-marker question is "carried, not
   settled" (`_MARKER_OPEN`), and `leakscan`'s window line in `--declarations` prints it, while
   `GUARDS.md` since `2a6d7a41` says a reasoned marker counts.
7. The design note's status line reads "proposed (design only; nothing built and no check
   changed)", unchanged at HEAD; `GUARDS.md` § *Before building a check* says "Adopted on Mike's
   2026-11-09 answer".
8. The gate's reads against atelier, each answered: wiki off, visibility public; Actions enabled,
   `allowed_actions: all`; default workflow permissions `read`, cannot approve reviews; fork-PR
   approval `first_time_contributors`; private vulnerability reporting `enabled: true`; one active
   ruleset; `rules/branches/main` returns `deletion`, `non_fast_forward` and `required_signatures`,
   all from that ruleset.
9. `gh api repos/mike548141/atelier/branches/main/protection` returns 404 "Branch not protected":
   no classic protection is set, and the protection `main` has comes from the ruleset alone.
10. `gh api repos/mike548141/atelier` returns a `security_and_analysis` block of five settings, and
    `has_pages`, `has_discussions`, `has_projects` and `allow_forking`; the gate names none of
    them. Their values are not recorded here, since this file is public.
11. A sweep of `skills/`, `docs/build/templates/` and `commands/` for `wiki` or `hasWikiEnabled`
    finds nothing.
12. Outside the board and the barred records, only `docs/method/REVIEW.md` (lines 225, 229 and 511) and
    `CHANGELOG.md` carry the rule-4 pin wording or "landing = queuing" (`coldsweep`).

The probes are not in the tree; each fact above is reproducible from the brief's re-run lines and
live reads, or a one-line `grep`.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

The Fable 5.1 reviewer's running work log, kept outside the repository while the pass ran and
appended here unchanged at the fold by the orchestrator; only its headings are demoted two levels
so they nest under this one.

### Review log — atelier 160/1300 cold pass (Fable 5.1)

Reviewer: Fable 5.1 (claude-fable-5-1), spawned by per-pass orchestrator 3715b04c (Opus 5.5),
started by drain session eca14b23 (Opus 5.5). Worktree:
/Users/mike/worktrees/fable/atelier-160-1300-2102/atelier at HEAD 4613ca76. Brief:
docs/reviews/2026-11-14-0211-evidence-window-declaration-settings-gate-cold.md (327 lines).
Sibling .deferred.md shows as deleted in the working tree (expected partition). Not opened.

#### Act 1

- 2026-11-22T21:04Z `git status --short` → only ` D` the sibling. HEAD 4613ca76.
- Read the brief whole (lines 1-327). Noted: acceptance-test sed ranges; re-run list V2 (7 lines);
  live reads (7 GETs); LA1-LA9; non-goals; deferred-reading bars; coldsweep command.
- Read docs/method/REVIEW.md lines 25-300 (rules 1-4), 302-460 (lenses, V1-V7), 460-560
  (lifecycle, method-record ruling), 760-835 (macro/micro list, what review is not). Verdict shape
  taken from there.
- `git merge-base --is-ancestor dd3d60d4 HEAD` → exit 0 (tree holds the delta). Re-run line 1 OK.
- Acceptance test: ran the four `sed` ranges exactly as the brief gives them (115/010 1-33,
  115/120 1-70, 260/070 1-6, 320/420 1-51). His answer in both 115 items is the quoted
  *"Everything, on every check now"* with the offering session's reading beside it; 260/070 and
  320/420(a)/(b) carry no word of his. 320/420 lines 1-51 describe the mechanism, the cost (four
  commits, a pin-bump commit reviewed) and the two fixes (a) doctrine, (b) grammar + guard.
- `coldsweep.py --root W --commit dd3d60d4` → exit 0, 461 lines saved to scratch
  delta-dd3d60d4.txt; subject + stat + diff of 7 files; 6 board files left out; 0 barred files.
  Read the whole diff. Stat matches the brief (366+/3-, 7 files).
- Later commits on delta paths: `git log --oneline dd3d60d4..HEAD -- <5 paths>` → 18 commits; on
  GUARDS.md 7 (ba55be27, 2a6d7a41, 55f23034 as the brief says, plus 571cd373, ef4972e6, 641f017f,
  aca05c14, none inside the two sections); on AUTONOMY.md 2 (34c62cb7 added the `flipcheck.py`
  sentence to the gate bullet; aa3409b0 elsewhere); on REVIEW.md 8, none touching the rule-4
  sentence (`git log -S"pins the bound"` → only dd3d60d4); on the design note 0; on
  REPO-STANDARD 3, PVR sentence unchanged at HEAD lines 86-96.
- `coldsweep --commit <sha> --path docs/method/GUARDS.md` for ba55be27 (step-0 paragraph
  rewrite), 2a6d7a41 (allow-marker paragraph replaced by the 2026-11-12 answer), 55f23034 (commit
  -message plane, elsewhere). Exit 0 each; bodies not printed.
- `coldsweep --commit dd3d60d4 --path docs/roadmap/260-.../130-...md` → the author's deferral
  item, 15 lines (disclosed: a board file read with --path). It says fork-PR approval and branch
  protection "cannot be read as set on a private free-plan repo".
- Scratch worktree of dd3d60d4 added under the scratchpad (`git worktree add`), removed at the
  end of act 1.
- Registry at dd3d60d4: 16 `Scanner(` blocks; names secretscan leakscan conflictscan linkscan
  reviewscan publishscan sizescan board datescan wrapscan spellscan harvestscan pointerscan
  pathscan indexscan licenscan; the 16 `why=` strings cite no document (census claim holds).
- Census replays exist at dd3d60d4: test_publishscan.py:43 test_the_grounded_pattern_reds;
  test_pointerscan.py:106 test_the_live_specimen_is_flagged; test_board.py:758 class StagedPlane
  ("BS1's fund"); test_indexscan.py:226/242 DateRule.test_a_line_dated_before_its_file_is_flagged.
- Posture cells: floor.py@dd3d60d4 lines 626-648 sizescan comment "forbid-the-act declaration";
  lines 833-835 indexscan "MAKES THE FAILURE CHEAP". No other registry entry or docstring carries
  either word (grep). Census ✅ forbids / ✅ cheap hold; 14 ❌ hold.
- Docstring citations at dd3d60d4 (ast docstring, regex): licenscan cites 115/290 and
  "AUTONOMY: making a repo public is a floor action" (lines 13-15, 41); publishscan cites 260/090
  and F1; spellscan CONVENTIONS.md; wrapscan seam S1; datescan seam S3; secretscan SECRETS.md;
  leakscan REPO-STANDARD.md § Personal data; reviewscan REVIEW.md; pointerscan REVIEW.md;
  board ADR 2026-..; conflictscan 320/200; linkscan PROPAGATION.md; harvestscan ROADMAP.md only;
  pathscan GUARDS.md/320/*; indexscan 200/010.
- Test modules at dd3d60d4 naming review findings: test_spellscan SS1 (l.52), SS3 (l.215, 236);
  test_wrapscan WS2 (l.97), WS4 (l.159, 187) — exemption cases; test_licenscan B2 l.90-108:
  `test_only_suffix_header_still_blocks` = a GPL-2.0-only header in a permissive repo must BLOCK
  (a firing test tied to review finding B2); LC1/LC2 (ruled 2026-08-06) l.416-427.
- HEAD floor.py: 21 `declares=Declares(`; licenscan l.1269-1290 `rule=Unmet("no rule text
  cited")`, `grounding=Unmet("no incident named")`; wrapscan l.898-917, spellscan l.920-945 as
  the census marks. `_load_declares` l.1808-1840 returns None on any shape error (design claim
  "never a ConfigError" holds as built). `Window.fits` membership only checked (l.3313); no tie
  between `outside-warn-only` and `warn_only` (grep WINDOW_FITS/warn_only >3100). Checks carrying
  `outside-warn-only` at HEAD: harvestscan (l.980), pointerscan (l.1010), sweepscan (l.1197).
- Worked cases at dd3d60d4: datescan.py l.7, 121-124 (third clause "NOT mechanically checked";
  intent a text scanner cannot see); harvestscan.py l.40-70 (widening measured by --replay, two
  folds); floor.py l.163 `"flags": {"leakscan": {"args": ["--disable","ipv4"], "why": "IPs are…`;
  pointerscan registry l.765-771 warn_only=True "read judgement-adjacent text". LA3 holds.
- Re-run list: line 1 exit 0; line 2 exit 0 (461 lines); `floor.py --list` exit 0 (19 checks,
  `decl n/5` column present); `floor.py --declarations` exit 0 (148 lines, "21 checks, 0 meet all
  five"); `reviewscan --root W W` exit 0 (254 briefs clean); `pointerscan --root W W` exit 0
  (877 files, 1162 items); unittest line from tools/ (subshell cd): "Ran 114 tests in 38.9s OK"
  (brief said 113; one more test now). All reproduce.
- Live reads 2026-11-22 (GET, --jq allowlisted): hasWikiEnabled false, visibility PUBLIC;
  actions/permissions enabled true allowed_actions all; workflow default read,
  can_approve false; fork-pr-contributor-approval first_time_contributors; PVR enabled true;
  rulesets one active branch ruleset; rules/branches/main deletion, non_fast_forward,
  required_signatures. All seven answered → the delta's implied "endpoints answer" holds.
- Extra read-only GETs for lens 4: repos/... → has_issues true, has_projects true,
  has_discussions false, has_pages false, allow_forking true, secret_scanning disabled,
  push_protection disabled, dependabot_updates disabled; pages 404; fork-pr-workflows-private-
  repos → HTTP 422 "not allowed for public repositories"; deploy keys 0, actions secrets 0,
  webhooks 0. No values beyond these printed; none are secrets.
- Platform docs (WebFetch, read-only): GitHub plans page lists "Protected branches" under Pro and
  Team "in private repositories" and not under Free → branch protection is public-only on Free
  (LA7 half holds). Rulesets page: "GitHub Team and GitHub Enterprise" with no Free statement,
  yet this Free public repo has an active ruleset (docs and reads disagree). Actions permissions
  REST page: fork-pr-contributor-approval "Gets the fork PR contributor approval policy"; the
  private counterpart is a different endpoint "for a private repository" → fork-PR approval is
  visibility-gated on every plan, not plan-gated (LA7 other half: cause mis-stated).
- Sweep (brief's coldsweep line) exit 0, 603 hits / 746 files, 1014 barred files excluded.
  Mirror sites found: REPO-STANDARD.md:92 (pointer), REVIEW.md:229-230, census docs
  2026-11-16-1142/-1204/-1220 (rows GRD1/7/9, AUT8, REV16), tools/README.md, flipcheck.py.
  None in skills/ (grep flip|visibility|pre-publish: create-repo and fleet-sweep mention
  visibility only), none in docs/build/templates (CLAUDE.md visibility fact only).
  PRINCIPLES.md §6 (l.265-289) names skills/, commands/, templates as sweep surfaces.
- AUTONOMY.md l.120-126: "Widening your own authority — editing this file … to grant the agent
  more"; the delta adds floor stops (narrows), so no confirm owed on that line; l.125 "New trust
  surfaces — deploy keys, webhooks, CI secrets, GitHub app installs" exist as a floor item the
  gate does not read.
- 260/110 l.1-40 (board, not barred): the four earlier gate additions, built 2026-10-05.
- tools/README.md l.2704-2719 and flipcheck.py docstring l.1-45 read (step-0-class evidence of
  what was built after the delta; disclosed). It reads the five settings, GET only.
- LA8 probe: `git rev-list --count dd3d60d4..2c1f0296` = 58; of them 17 touched the delta paths
  (incl. CHANGELOG, decisions index). `grep -i '\.\.HEAD|moving bound|symbolic' pointerscan.py`
  → nothing: (b) unbuilt, as the delta says.
- Pre-commit: hooksPath → .githooks/pre-commit runs `floor.py --plane hook`; datescan baseline
  on the brief: 0 findings before I wrote.
- No ADR 0009 exists in atelier's docs/decisions (the child report's "ADR 0009" is the child's).
- LA2 probe at HEAD: `grep -n "WINDOW_FITS\|warn_only" tools/floor.py` (>3100) → l.3313 membership
  test only; no tie between fits=outside-warn-only and warn_only; `grep -i "becomes a block|flip to
  blocking|re-ask|outside-warn-only" GUARDS.md design-note` → only the schema's Literal and the
  "no move to blocking" paragraph. Finding EW1.
- Candidate findings formed and recorded in the brief: EW1 MODERATE (warn-only carve-out has no
  re-entry; LA2), EW2 MODERATE (licenscan census cells vs test_licenscan B2 firing test and
  115/290 citation; legend wording; propagated to HEAD registry l.1281-1287), EW3 MODERATE (gate
  enumerates no threats; GETs show secret scanning / push protection disabled, issues/projects/
  forking on, keys/hooks/secrets unread), EW4 minor (design note "Not decided here" vs GUARDS at
  HEAD after 2a6d7a41), EW5 minor (free-plan cause bundles plan-gated and visibility-gated), EW6
  minor (pin silent on later commits; 58/17 commits probe), EW7 note (3/5 vs tool's 2/5), EW8 note
  (LA1 deferred to act 2), EW9 minor (design note Status/index stale since ba55be27).
- Items checked and sound: LA3 (three cases), LA5 malformed→None, LA9 (AUTONOMY l.120-124 widen
  vs narrow), V3 (no skill/template restatement), V4 (REPO-STANDARD points), the four ✅ replays,
  the two ✅ postures, the `why` claim, the seven endpoints, the rule-4 sentence unchanged since
  dd3d60d4, the CHANGELOG entry present at HEAD l.582.
- Verdict appended below `---` (brief now 619 lines); Status line updated to ACT 1 WRITTEN.
  Scratch worktree removed (`git worktree list | grep -c dd3d60d4` → 0).
- Gates on the brief (each `/usr/bin/python3 tools/<x>.py --root W <brief>`): datescan 0,
  wrapscan clean (85-col budget), spellscan exit 0, leakscan 0, linkscan exit 0, reviewscan
  exit 0, attribscan 0, secretscan clean. pathscan exit 1 with 3 missing-path findings, all in
  the brief-writer's lines 274/276 (docs/ROADMAP-DONE.md and docs/SESSIONS.md, retired since the
  brief was written; the sibling link, which the orchestrator fixes at the fold); pathscan is
  warn-only on the hook plane (`floor.py --list`), none is in my text, and I may not edit the
  brief's own lines. pdlistscan takes no file argument; run whole-root instead (below).

#### Act 2 (released 2026-11-22T21:23Z after act 1 committed as dbfee578 on origin/main)

- `git fetch`; `merge-base --is-ancestor dbfee578 origin/main` → yes. Tree still only ` D` sibling
  + ` M` brief.
- Read the held sibling at the path the orchestrator gave (107 lines: 16 questions, 12 facts).
- Read the barred records: 115/010 l.34-39 (landing note: "grounds are this item's count, not
  re-measured"); 115/120 l.71-99 (design done, step 0 landed 2026-11-10 with the propagation
  rule "fields without a ✅ in the census are Unmet", the 2026-11-12 answer); 260/070 l.7-12
  (landing note, "endpoints were read live 2026-11-09"); 320/420 l.52-55 ((a) done, (b) open).
- `git log -1 --format=%B dd3d60d4` (commit body, 20 lines); pointer 160/1300 whole; first
  lines of 160/1430 and 160/1440; Status line of docs/reviews/2026-11-14-0318-check-
  declarations-step-0-cold.md (BRIEF ONLY, not run → no prior verdict to reconcile with).
- Q4 re-measure: `ls docs/reviews | grep <scanner>`; overall lines of 2026-07-23-0618 datescan
  (PWF 0 MAJOR, "narrow to attribution blockquotes"), 2026-07-23-0707 spellscan (PWF),
  2026-07-23-0707 wrapscan (1 MAJOR), 2026-07-26-2215 pathscan (3 MAJOR, narrowing documented),
  2026-07-26-2215 stampscan (declared narrowing), 2026-07-29-1306 harvestscan (1 MAJOR, shelve
  then wire). Shape holds; "four killed", "one in three" not re-derived (no file citations).
- Q12 probe: `gh api repos/mike548141/atelier/branches/main/protection` → 404 "Branch not
  protected" (GET); flipcheck.py l.183-215 reads rulesets, rules/branches and
  branches/<b>/protection; the AUTONOMY bullet names only the first two. → EW10.
- Q15 probe: `git log --diff-filter=A -- <pointer path>` → a7481611 ("board: queue the cold
  pass…"), committer date 2026-11-10T02:42:16+13:00, one second after dd3d60d4 (…:15);
  `rev-list --count dd3d60d4..a7481611` = 1. coldsweep of dd3d60d4 listed no 160/ file. → EW11.
- Q5: sweep.txt roadmap hits for "window" → none filed after 2026-11-09 for a blocking check;
  step-0 Unmet marks are the only trace. → EW12 (note).
- Q10 probe: rerun-floor-declarations.txt l.40, l.89 "✅ grounding met" (pointerscan,
  publishscan) vs "🔎 rule resolves". → EW13.
- Q11 probe: floor.py l.3209-3213 `_citation_problem` globs docs/roadmap/{sec}-*/{item}-*.md
  only; `ls docs/roadmap` shows 990-done-before-the-split and 250-session-archive stores. → EW14.
- `floor.py --list --plane msg` → namescan, quotescan (sibling fact 5 confirmed);
  `_MARKER_OPEN` floor.py l.618-620 (fact 6 confirmed).
- Appended `### Reconcile` beneath the act-1 verdict (brief now 747 lines); Status line updated
  to RUN, both acts. Act-1 text untouched. Sibling not folded, nothing deleted or restored.
- Gates after act 2: see the gate run recorded in the session (datescan, wrapscan, spellscan,
  leakscan, linkscan, reviewscan, attribscan, secretscan clean; pathscan the same 3 brief-writer
  lines 274/276, warn-only; pdlistscan whole-root clean).
