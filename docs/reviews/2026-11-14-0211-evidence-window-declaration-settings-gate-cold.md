# Cold pass — the evidence-window rule, the check declaration standard, the pre-flip settings gate, and the pinned review bound

**Board:** `docs/roadmap/160-doctrine-review-owed/1300-rule-4-cold-pass-queued-evidence-window-declaration-settings-gate.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `fef270f6`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
