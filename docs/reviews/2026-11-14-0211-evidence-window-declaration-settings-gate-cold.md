# Cold pass — the evidence-window rule, the check declaration standard, the pre-flip settings gate, and the pinned review bound

**Board:** `docs/roadmap/160-doctrine-review-owed/1300-rule-4-cold-pass-queued-evidence-window-declaration-settings-gate.md`
**Status:** ACT 1 WRITTEN 2026-11-22 UTC (PASS-WITH-FINDINGS, 0 MAJOR, 3 MODERATE); act 2
owed. Brief written 2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as
session `fef270f6`); run 2026-11-22 UTC by a Fable 5.1 reviewer under the 2026-11-23 drain order.

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
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-14-0211-evidence-window-declaration-settings-gate-cold.deferred.md` (a
held-back file; by count: 16 questions, 12 facts), every item under
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
