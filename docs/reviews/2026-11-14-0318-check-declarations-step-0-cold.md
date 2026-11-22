# Cold pass — every check states its five declaration fields (`115/120`, step 0)

**Board:** `docs/roadmap/160-doctrine-review-owed/1430-rule-4-cold-pass-queued-check-declarations-step-0.md`
**Status:** PASS RAN, folded 2026-11-22 UTC: PASS-WITH-FINDINGS, 0 MAJOR, 2 MODERATE (CD1, CD2),
5 minor, 7 notes. Act 1 and act 2 written by a Fable 5.1 reviewer; sibling folded below the
verdict. Brief written 2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as
session `263945c1`); run under the principal's drain order of 2026-11-23 NZDT (see the verdict
below).

**Pass type:** code cold pass, first of its kind, per `docs/method/REVIEW.md` rule 4 (a schema and
reader every check in the estate now carries, in the floor every child floats on).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** medium-large: one commit, 7 files outside the board store, 1,097 lines added
and 11 removed. 646 are `tools/floor.py` (the schema, 21 registry declarations, the child-config
loader, the reader and three surfaces), 385 tests, 42 `tools/README.md`, 21 `CHANGELOG.md`, 7
`floorfleet.py`, 7 a `GUARDS.md` status paragraph.
**Why it earns a review:** this is the first machine reading of a guard's *purpose*, and it is
reported on every CI run in atelier and in every child. Its worst failure is a declaration that
reads as satisfied when it is not: a `met` or `resolves` that a reader takes as "this check serves
its rule", while the machine has only seen that a file, heading or test name exists. That is the
same silent-confidence class the standard exists to retire, now printed beside every check. The
second worst is a warn-only feature that can still change an exit code, fail the floor closed in a
child, or cost the hook plane time on every commit. The third is a declaration that states as open,
or as decided, something the record says otherwise.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09/10 UTC, and the worker it dispatched, which wrote the commit (per the queue pointer).
  The author queued this pass and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `263945c1`; `$CLAUDE_SESSION_ID` was unset), started 2026-11-14 UTC by an estate health sweep,
  orchestrator session `58027096` (Opus), on the principal's instruction that a brief is written for
  every review known to be owed (Mike, 2026-11-14, verbatim: *"include all briefs are written where
  we know a fable review is required"*). Neither wrote any of this delta. **Off-tier for review,
  disclosed: the brief-writer forms no finding and writes no severity**, and stops after writing.
  It ran no review and used no Fable model.
- **Barred from running this pass:** session `263945c1` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; `115/120` whole,
  including the author's landing note (the lines barred below); **the commit message body of
  `ba55be27`** (read before the body-free command was in hand); the design note whole; the unrun
  brief for `160/1300` and its sibling (read for house form, and for its non-goals). It opened **no
  prior verdict file**. Its harness also loaded user-level and repo instruction files and a memory
  index, which hold private context this brief does not carry. Everything evaluative it formed is
  in the sibling.

## The acceptance test

The principal's word is a pick from options a session offered, an answer and not a ruling in his
own words. Print it, and the problem as it was filed before the work, from the worktree root:

```
sed -n '1,70p' docs/roadmap/115-guardrail-architecture-mike-commissioned/120-every-guard-declares-the-purpose-it-answers-to.md
```

His answer is the quoted text on line 70, *"Everything, on every check now"*; the rest of that line
is the offering session's reading of it. Lines 1–66 are the problem as filed and the 2026-08-23
fold. Test the build against his words and against what the item asked for, not against the
design note alone: the design note is the author run's own plan (its status still reads
"proposed"), and is itself under a separate pass (`160/1300`).

## What the work is

One commit on `main`, authored 2026-11-10 NZDT (2026-11-09 UTC):

- **`ba55be27`** — `floor: every check states five things, reported only (115/120 step 0)`.

Read it body-free: `python3 tools/coldsweep.py --root . --commit ba55be27` (subject, stat and diff,
never the body; board files left out). Plain `git show` prints the body before the diff, and reading
is atomic (`REVIEW.md` rule 1), so it is barred. Check first that your tree has the delta:
`git merge-base --is-ancestor ba55be27 HEAD` exits 0. The pointer names the bound as "the commit
that closes step 0 of `115/120`, on `main`"; this brief pins it to `ba55be27`. Record the pin in
your verdict's scope.

Delta paths (the pointer's list, all in the commit):

- `tools/floor.py`: `Unmet`, `Grounding`, `Window`, `Declares`; the `declares` field on `Scanner`;
  a `Declares` on all 21 `SCANNERS` entries; `LOCAL_KEYS` and `_load_declares` for a child's
  `.atelier-floor.json`; the reader (`_citation_problem`, `_replay_problem`, `read_declaration`,
  `declarations_report`, `declarations_line`, `render_declarations`); `--declarations`, the `--list`
  column, the `--json` key and the CI line in `main`.
- `tools/floorfleet.py`: the one fleet-board line.
- `tools/test_floor.py` (28 new tests, among them `DeclarationSurfaceTest` and
  `DeclarationConfigTest`) and `tools/test_floorfleet.py`.
- `tools/README.md`: the `local` key and the `--declarations` section.
- `docs/method/GUARDS.md`: the "Step 0 is built" paragraph in § *What every check declares*.
- `CHANGELOG.md`: the 2026-11-10 entry.

**What it was built against:** `docs/method/GUARDS.md` § *What every check declares* and
§ *Before building a check: the evidence window*, and the design note
`docs/decisions/2026-11-09-1334-check-declaration-standard.md` (§ *What reads it*, § *How a miss is
reported*, § *How the build splits*, § *Census, 2026-11-09*). Both landed in `dd3d60d4`, the day
before.

**Since the delta.** No later commit touches `tools/floor.py`, `floorfleet.py` or their tests
(`git log --oneline ba55be27..HEAD -- tools/floor.py tools/floorfleet.py tools/test_floor.py
tools/test_floorfleet.py` prints nothing at `672acdd9`). Two later commits touch other delta paths:
`2a6d7a41` (`GUARDS.md`, recording the principal's 2026-11-12 answers, among them the allow-marker
question this step carried as open) and `4bfb4e16` (an unrelated `tools/README.md` section). Read
each body-free with `python3 tools/coldsweep.py --root . --commit <sha> --path <file>`. Judge the
delta as landed and as it stands at HEAD, and say whether a later change left any of its statements
stale.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "Every registry check now carries a `Declares` beside its `why`"; "All 21 checks state all
  five"; "a field that cannot honestly be met is an `Unmet` with its reason and the item that owes
  it".
- The census's 16 "as it stood", and "the five new checks from their own docstrings and tests".
- "Reported, and only reported. No exit code on any plane reads a declaration, here or in any
  child." "The hook plane prints nothing and pays nothing."
- "The reader says only a machine's half": a resolving citation reads `resolves` "until a verdict
  has read it against the check", recorded in `reviewed`; a replay "resolves by `ast`, with no
  import and no run", so "a broken test module is a finding, not a crash".
- "`N` counts `met` fields, which is the same test 'meets all five' uses."
- "A child's `local` check may carry a `declares` object"; "Malformed reads as *missing* and is
  never a config error"; "The `local` block's strict key checking stops at this key's door on
  purpose."
- A cited path "stays inside its base", which "stops one naming a file outside the repo"; a fleet
  check's citations resolve against atelier's tree, a local check's against its own repo.
- "Prose is not a citation: a restated rule is what this retires." The citation grammar, with
  `docs/build/` added beyond the design note's.
- "One question is carried, not settled": a check that blocks, or will on a date, and leans on an
  allow-marker "states `window` as `Unmet` and names that question"; "A warn-only check does not
  enforce, so it can."
- `GUARDS.md`: "The machine says only whether a citation or a replay resolves, so passing a field
  still binds as a review question."
- The CI and fleet line, for example `🟡 declarations: 21 checks, 0 meet all five`.

## Scope

The widest the work admits: intent, decisions, assumptions, the schema and reader as code, every
one of the 21 declarations against its check, docstring and tests, the surfaces as printed, the
tests as proof, the docs, and real-world behaviour: `floor.py` run on this tree and, read-only, on
child repos checked out on this machine. The lenses organise it; they do not bound it. Anything not
named a non-goal is in scope, and a non-goal that fences off the risk is a finding.

**Non-goals:** the standard and design themselves (`dd3d60d4`, its own pass, `160/1300`), except
where the build departs from the design or the build shows the design cannot be met as written;
the 2026-11-12 answers as doctrine (`2a6d7a41`, its own pass, `160/1440`), except where they make a
statement in this delta stale; groups A to E, which turn `Unmet` into met and are not built;
whether any warning becomes a block.

## The four lenses — run all four

1. **Approach and assumptions** (most important). Is a machine reading that stops at "exists" the
   right first step for a standard the principal asked for "on every check now", or does it
   manufacture a count that reads as progress? Is `Unmet` with a reason the honest form of an
   unmet field? Are four states (`met`, `resolves`, `unmet`, `missing`) the right vocabulary, and
   does each surface keep them apart? Is a declaration in `floor.py` source, edited in one lane, the
   right home given the contention the design note names?
2. **Correctness and quality.** Does each of the 21 declarations say what is true of its check? Do
   the reader's states match the design note's machine/reviewer table? Do the tests prove what
   their names say, and would they fail if the behaviour broke? Is anything stated as decided that
   is open, or as open that is decided?
3. **Completeness and harvest.** Every surface the design note names, and every consumer of the
   surfaces this changed (`--list` columns, the `--json` shape, the CI log). The checks the step
   did not reach (group E: checks outside `SCANNERS`, each child's `local` checks) and whether the
   reports say so. Every mirror of the standard that should now say "step 0 is built" (V3).
4. **Security and privacy** — a must. A child's `.atelier-floor.json` is author-supplied input to a
   reader that runs in CI: path containment (`_safe_rel`, symlinks), parsing an arbitrary file with
   `ast`, unbounded reads, and text from a declaration reaching a CI log where GitHub interprets
   `::` workflow commands. Whether the warn-first guarantee holds against a hostile or merely
   malformed config. This repo is public: whether any declaration names what a public record should
   describe by type only. `/security-review` reads the session's pending diff: where you can aim
   it at `ba55be27`'s Python, run it as the floor under this lens, never a discharge; its markdown
   share is excluded and weighs nothing. Say what it reached.

## Load-bearing assumptions to attack

Each is a falsifiable claim. Damage it with a probe or confirm it by re-driving; never by reasoning
alone.

- **LA1.** Every one of the 21 declarations is true of its check: each stated `Unmet` reason, each
  purpose gap, each window and posture matches the check's code, docstring and tests at `ba55be27`
  and at HEAD.
- **LA2.** A citation that `resolves` names the rule the check actually serves, not merely an
  existing heading; and `reviewed` cannot be set in a way that turns a rule `met` without a verdict.
- **LA3.** Every stated replay is a test that fails when its check stops firing on the named
  incident, not only a test method that exists.
- **LA4.** No surface lets an `Unmet`, `missing` or `resolves` field read as met: `--list`,
  `--declarations` (text and `--json`), the `--json` key on a scan run, the CI line, the fleet line.
- **LA5.** No exit code on any plane reads a declaration, and no declaration, config or reader
  error can fail the floor closed, here or in a child.
- **LA6.** The hook plane pays nothing for this step, in time or output, on any invocation the
  hooks make.
- **LA7.** `_load_declares` turns every malformed `declares` into *missing*, and the `local` block
  still rejects every other unknown key.
- **LA8.** A child's declaration cannot make the reader read, or report the existence of, a file
  outside that child's repo.
- **LA9.** The `--list` column change breaks no consumer that parses `--list` output, in this repo
  or in the floor workflow every child runs.
- **LA10.** The "carried, not settled" allow-marker statement was accurate when it landed and is
  still accurate at HEAD, everywhere it is stated (code, tests, README).
- **LA11.** The counts the surfaces print are right: 21 checks, 0 meeting all five, and the
  per-field totals, re-derived independently of the reader.

## Re-run list (V2)

The brief-writer ran every line once on 2026-11-14 UTC at `672acdd9`, from the worktree root unless
it says otherwise; each exited 0. Re-run them; a line that no longer reproduces is a finding.

```
git merge-base --is-ancestor ba55be27 HEAD
python3 tools/coldsweep.py --root . --commit ba55be27
python3 tools/floor.py --root . --declarations
python3 tools/floor.py --root . --declarations --json
python3 tools/floor.py --root . --list --plane ci
python3 tools/floor.py --root . --list --plane ci | awk '$2!="disabled" && $3!="local"{print $1}'
cd tools && python3 -m unittest test_floor
cd tools && python3 -m unittest test_floorfleet
```

`test_floor` ran 255 tests in about 184 s; `test_floorfleet` 127 in about 14 s; the awk line (the
floor workflow's own parse, `.github/workflows/floor.yml`) printed 21 names. Run them one at a time,
in the foreground, with a long timeout.

**Live, read-only.** The delta's recorded proof that old and new `floor.py` gave identical exit
codes and result sets "on five children, CI and hook planes" is in the commit body (barred until
phase 2); the CHANGELOG states the same outcome as "No exit code changes ... here and in every
child". Re-drive it against child repos checked out on this machine: run `floor.py` from
`ba55be27^` and from `ba55be27` with `--root <child>`, read-only, on the `ci` and `hook` planes, and
compare exit codes and results. Name no child in the verdict (this repo is public): count them.
A child with dirty work is another session's; skip it and say so. **Any write to a child, a push,
or a change to a child's `.atelier-floor.json` to test a local declaration is NOT RUN**: build such
a config in a scratch directory instead.

## House rules for this run

- **Live systems:** only the read-only runs above. No live writes, no push from a child, no write
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
`2026-11-14-0318-check-declarations-step-0-cold.deferred.md` (a held-back file, now folded below
the verdict; by count: 14 questions, 10 facts), every item under `docs/roadmap/160-doctrine-review-owed/` beyond its
title, every commit's message body, and
`docs/roadmap/115-guardrail-architecture-mike-commissioned/120-every-guard-declares-the-purpose-it-answers-to.md`
from line 71 onward (the author's landing notes, and a later answer that `2a6d7a41` carries into
`GUARDS.md`, which you may read there).

The delta's own `CHANGELOG.md` entry, `tools/README.md` section, `GUARDS.md` paragraph and code
comments carry the author's account of why; they are the delta, and reading the delta is never
barred. The design note is the author run's plan, not this delta: read it as the spec, and disclose
that you did.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/120-every-guard-declares-the-purpose-it-answers-to.md \
  'Declares|declares|declaration|Unmet|_MARKER_OPEN|resolves|decl [0-9]/5'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions, LA1–LA11 and
the re-run list. Append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, any orchestrator, what you read, the UTC day), the pinned bound,
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-claim ledger, findings with stable IDs (prefix `CD`:
`CD1`, `CD2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is a self-authored guard that reports on every check, built in the doctrine's own
machinery, so every finding is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, cold pass, Fable 5.1

### Provenance (V7)

- **Reviewer:** Fable 5.1, the principal-named review tier, tier checked at selection.
- **Spawn:** a headless per-pass orchestrator (Opus 5.5, session `cd7d5f1e`), itself started by
  the weekly drain session `eca14b23` (Opus 5.5). Both are off-tier orchestrators: they hold the
  context partition, form no finding and write no severity. Neither wrote the brief or the delta;
  `eca14b23` wrote no brief, no delta and started no brief-writer. I was not started or instructed
  by the barred sessions `263945c1`, `58027096` or `d0ca5d24`.
- **Order:** the principal's weekly drain order of 2026-11-23 NZDT, verbatim: *"Start a fable drain
  or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1430-2248/atelier`, HEAD `e24ff31f`,
  read-only to me except this file. The sibling `.deferred.md` was removed from it by the
  orchestrator before I started (it shows as a deletion in `git status`); I did not look for it.
- **What I read, and did not:** the brief; `REVIEW.md` §§ scope, re-run, standing checklist; item
  `115/120` lines 1–70 only; the delta body-free (`coldsweep --commit ba55be27`); the design note
  whole (the spec; disclosed); `GUARDS.md` §§ The fourth requirement, Before building a check, What
  every check declares, at HEAD; `2a6d7a41` and `4bfb4e16` body-free on their delta paths; the four
  later commits on the four code files, body-free (see *Pinned bound*); each scanner's module
  docstring where a declaration cites it; the three replay tests; `floor.yml`, `ci.yml`, the hook
  samples; `docs/method/census/2026-11-16-1204-...` rows GRD1–GRD12; `docs/decisions/README.md` line
  49. Not read: the session log, the record stores the brief bars (two of which no longer exist at
  HEAD), any prior verdict, any commit body, any `160/` item beyond its title, the sibling. The
  coldsweep tree search ran without `--include-barred`. The harness loaded user-level and repo
  instruction files and a memory index before I started; none carried this delta's framing. Day of
  the pass: 2026-11-22 UTC (2026-11-23 NZDT).
- **Work log:** every command and read, with its evidence, is in a running log kept outside the
  repo until the fold, when it is appended to this file.

### Pinned bound

`ba55be27`, `floor: every check states five things, reported only (115/120 step 0)`, ancestor of
HEAD (`git merge-base --is-ancestor` exits 0). Judged as landed and as it stands at HEAD
`e24ff31f`. The brief's *Since the delta* paragraph is stale at this HEAD: four later commits
touch the four code files (`734930ef` test graces; `ef4972e6` a `tree` stderr line printed before
the declarations line; `b462fd7d` rewrites quotescan's `why` and its `Declares` text;
`cf648679` flags spelling and the coverage line). None changes the reader; `b462fd7d` changes one
declaration's text and is judged below as HEAD state (CD6). The design note is the author run's
plan and is under `160/1300`; the 2026-11-12 answers as doctrine are under `160/1440`; both are
touched here only where they make a statement in this delta true or stale.

### My own load-bearing assumptions (lens 1, named first)

1. That "reported only" is enforced by structure, not by convention: the exit expression never
   reads the report. Probed (LA5): confirmed.
2. That the four states are kept apart on every surface, so a count of `met` cannot be inflated by
   `resolves`. Probed: confirmed on the registry; a child can inflate `met` itself (CD1).
3. That the 21 `Unmet` reasons are true of the checks, not written to fit the census. Probed by
   docstring: 19 of 21 hold as stated (CD5, CD6).
4. That nothing in a child's config can reach a CI log or a file outside its repo through the
   reader. Probed: no log vector; symlinks escape the containment (CD4).

### The acceptance test

The principal's answer, *"Everything, on every check now"* (an answer to options, not a ruling),
asked that each check state all fields now, even where it fails the bar. The build does that for
the 21 registry checks, with `Unmet` and a reason wherever the bar is not met, and prints
`0 meet all five` rather than rounding anything up. "Every check" is wider than the registry: the
checks that run on CI outside it (`stampscan`, `blockscan` in `ci.yml`; `signscan` in `floor.yml`)
and the hook-plane guards state nothing, which the design note names as group E and the delta's
surfaces do not (CD10). Against the item as filed (lines 1–66), the four fields plus the folded
posture are all present in the schema, and the two things the item said would have caught the
inversion (citation never restated; a replay that fires) are machine-checked to the extent a
machine can: a citation resolves, a replay exists. The item's own warning, "citation is not
catch", is carried into the reader as the `resolves` state and into `GUARDS.md` as the review
question. That is the honest first step, with the two gaps below.

### Lens 1 — approach and assumptions

A machine reading that stops at "exists" is the right first step **because the surfaces say so**:
the header and the CI line count `met` only, `resolves` has its own mark and its own words, and
every `Unmet` prints its reason and the item that owes it. It does not manufacture progress on the
registry: the number it prints is 0. It can manufacture progress in a child, because the one field
whose `met` is meant to record a person's reading, `reviewed`, is accepted as any non-empty string
(CD1). `Unmet` with a reason is the honest form, and the three shared `Unmet` constants keep the
reasons consistent; the cost is that a shared reason can go stale in six places at once, which is
what happened to `_MARKER_OPEN` (CD2). The four-state vocabulary is right and kept apart, except
that `missing` doubles as "the reader hit an exception" (CD3). The home in `floor.py` is the
principal's 2026-08-23 ruling; the contention the design note names is real and already visible
(`b462fd7d` edited one entry in another lane within nine days), and `_OWED`/`_MARKER_OPEN` as
constants is the right mitigation of it.

### Lens 2 — correctness and quality

- **The 21 declarations against their checks (LA1).** Each `Unmet` reason was read against the
  scanner's docstring and tests at HEAD (work log). 19 hold as stated. secretscan's "names the
  SECRETS doctrine, no section" is false: the docstring cites `SECRETS.md § The boundary's posture`
  and that heading exists (CD5). quotescan's reason at HEAD says "one field cannot state both",
  which the schema contradicts (CD6; `b462fd7d`). sizescan's `forbids-the-act` and its cost match
  the registry's `ADVISORY_BARRED_FROM` date; indexscan's `cheap-failure` matches its comment. The
  seven resolving citations each reach the rule the check serves: REPO-STANDARD § Repo-craft
  conventions holds the purpose test (leakscan, pdlistscan); REVIEW.md § Independence is more than
  fresh context holds rule 4 (pointerscan); CONCURRENCY.md § The trigger (sweepscan);
  CONVENTIONS.md § The declared defaults (spellscan); the board-store ADR (board); REVIEW.md
  § Review the design and its record (reviewscan).
- **Reader states against the design table.** Match: rule `resolves`/`met` via `reviewed`,
  grounding `met` if every replay resolves, purpose gap `met` if non-empty and not the `why`,
  window `met` if `fits` is valid, posture `met` if one of two words. The table's "Only a reviewer
  can say" column is the reader's blind spot by design; CD1 is where that blind spot is reachable
  from author input.
- **Tests.** 28 new tests in `test_floor.py` and one in `test_floorfleet.py`, as claimed; both
  suites green at HEAD. Two names overclaim: `test_a_citation_resolves_and_only_a_verdict_makes_
  it_met` proves that any non-empty `reviewed` makes it met, with a path that does not exist (CD1);
  `test_the_open_marker_question_is_carried_not_settled` pins a fact that `GUARDS.md` no longer
  states (CD2). `test_an_unreadable_replay_file_never_raises` pins the collapse to `missing` as
  intended behaviour (CD3). `test_declarations_never_change_an_exit_code` mocks `run` and proves
  the exit expression; the live re-drive proves the rest.
- **Open stated as decided / decided stated as open.** Nothing open is stated as decided. The
  allow-marker question is stated as open in code, README, CHANGELOG and a test while `GUARDS.md`
  (2026-11-12) and the 2026-11-16 census (GRD8, "enforced") record it decided (CD2).

### Lens 3 — completeness and harvest

- Every surface the design note names exists: the `--list` column, `--declarations` text and
  `--json`, the `declarations` key on every `--json` run (checked on both planes), the CI line, the
  fleet line, the test pins.
- Consumers of `--list`: `floor.yml` and `ci.yml` parse `$1`–`$3` with `awk`; the new column is
  `$4`–`$5`; `CONTRIBUTING.md`'s template line is human-read; `test_templates.py` asserts the
  command string. Nothing parses past `$3` (LA9 confirmed).
- The checks the step did not reach: the surfaces print "21 checks" and nowhere say what is
  outside the count (CD10). A child's `local` checks read `missing` with a reason, which is right.
- Mirrors of "step 0 is built": `GUARDS.md` ✓, CHANGELOG ✓, README ✓, census GRD9 ✓; the design
  note's status line and `docs/decisions/README.md` still say "nothing built" (CD11); the seam
  contract's two named homes do not list `declares` (CD7).
- Harvest: nothing duplicated. `_inside` already exists in `floor.py` for the `run` path and would
  have given `_safe_rel` the symlink-safe containment it lacks (CD4).

### Lens 4 — security and privacy (V6)

- **Path containment.** `..` segments and absolute paths are refused in rule, incident and replay
  (probe c). Symlinks are not: `_safe_rel` is lexical and `is_file()`/`read_text()` follow a link,
  so a committed symlink lets a declaration make the reader open a file outside the repo and
  report on it ("no such heading" after reading it), and name it as a verdict path (probe b; CD4).
  Threat bounded: the author already runs code in that CI; the fleet side resolves against
  atelier's own tree.
- **`ast` on an author-supplied file.** A syntax error is caught by the reader's broad `except`
  and never fails the floor; the cost is CD3. No import, no run, confirmed by reading.
- **Unbounded reads.** A cited file is read whole; bounded to the repo except through CD4.
- **CI log and `::` commands.** Control characters in every config string are stripped at the
  parse seam (`strip_controls`), so a declaration cannot start a log line; the CI line prints
  counts only; `--json` escapes; nothing in `floor.yml` or `ci.yml` runs `--declarations`. No new
  vector (probe e).
- **Warn-first against hostile or malformed config.** Held: six hostile `local` declarations on
  both planes, with and without the `declares` blocks, gave identical exit codes and result sets
  (probe, LA5); every malformed shape read `missing`, never `ConfigError` (LA7).
- **Public repo.** All 21 declarations read: they name board items, findings, doctrine files and
  dates; no person, child or private repo.
- **`/security-review`: NOT RUN.** It reads the session's pending diff; in this worktree the only
  pending change is the deleted sibling, the very exposure `REVIEW.md` (SL2) warns of, and none of
  `ba55be27`'s Python is pending. This lens therefore rests on the probes above, not on a scanner.

### Load-bearing assumptions LA1–LA11

| LA | Result | Probe |
|---|---|---|
| LA1 | **Damaged** on 1 of 21 at landing (secretscan, CD5) and 1 more at HEAD (quotescan, CD6) | each `Unmet` reason read against the scanner's docstring and tests (work log) |
| LA2 | First half confirmed (7 citations reach the rule); **second half damaged**: `reviewed="nothing at all"` turns rule `met` (CD1) | scratch child probe (a) |
| LA3 | Confirmed with a caveat: board and pointerscan replays drive the check and assert it fires; publishscan's asserts the pattern function only | the three test bodies read |
| LA4 | Confirmed: `--list` and the header count `met` only; `resolves` has its own mark and words on `--declarations` and in `--json`; the CI and fleet lines print counts | re-run lines 3–6; fleet line from `test_floorfleet` |
| LA5 | Confirmed | probe with/without `declares`: identical results on both planes; five children old vs new |
| LA6 | Confirmed by structure: hooks call `--plane hook` without `--json`; `declarations_report` is reached only on `--declarations`, `--list`, `--json` or `plane == "ci"` | `pre-commit.sample`, `commit-msg.sample`, `main()` read |
| LA7 | Confirmed | probe (f): unknown key inside `declares` → missing; `declare` typo → `ConfigError` |
| LA8 | **Damaged** at the symlink level (CD4) | probe (b), (c) |
| LA9 | Confirmed | every `--list` consumer found by grep parses `$1`–`$3` or is human-read |
| LA10 | Accurate when landed; **damaged at HEAD** in four places (CD2) | `2a6d7a41` hunk; grep of HEAD mirrors |
| LA11 | Confirmed: 22 `met` fields, 7 `resolves`, 21 checks, 0 meet all five, hand-derived from the diff before running the reader | work log § LA11 |

### Per-claim ledger

| Claim (brief § The claims) | Verdict |
|---|---|
| Every registry check carries a `Declares`; all 21 state all five; an honest `Unmet` carries its reason and the item | Holds; one reason false (CD5), one false at HEAD (CD6) |
| The census's 16 as it stood; the five new from their docstrings | Holds, with honest departures: three census ✅ windows restated as `Unmet` for the marker question; the design note's worked indexscan entry tightened to `Unmet` |
| Reported, and only reported; no exit code reads a declaration; hook plane prints and pays nothing | Holds (LA5, LA6) |
| The reader says only a machine's half; `resolves` until a verdict is recorded in `reviewed` | Holds for the registry; `reviewed` is unchecked text (CD1) |
| A replay resolves by `ast`, no import, no run; a broken test module is a finding, not a crash | Not a crash, confirmed; "a finding" overstates: it reads as a missing declaration on all five fields (CD3) |
| `N` counts `met`, the same test "meets all five" uses | Holds (LA11) |
| A `local` check may declare; malformed reads missing, never a config error; strict keys stop at this door | Holds (LA7) |
| A cited path stays inside its base | Holds lexically; not against symlinks (CD4) |
| Prose is not a citation; grammar adds `docs/build/` | Holds; a child's own rule citations are limited to `docs/method`, `docs/build`, `docs/decisions`, ADRs and board items (note) |
| One question carried, not settled; a marker-leaning check states `window` as `Unmet` | Held on 2026-11-10; stale since 2026-11-12 (CD2) |
| `GUARDS.md`: passing a field still binds as a review question | Holds |
| The CI and fleet line `🟡 declarations: 21 checks, 0 meet all five` | Reproduced on CI plane, `--declarations`, and the fleet board |

### Standing checklist V1–V7

- **V1.** Two claims stronger than their evidence: a test name says only a verdict makes a rule
  met (CD1); README says a broken test module is "a finding" (CD3). The rest hold.
- **V2.** Every re-run line reproduced (ledger below); the live claim re-driven on five children.
- **V3.** Three mirror misses: the 2026-11-12 answer not swept into code, README, CHANGELOG and
  test (CD2); `declares` absent from the seam contract's two named homes (CD7); the design note's
  status and its index row (CD11).
- **V4.** The marker statement lives in four places and went stale together (CD2); `_OWED` and the
  three shared `Unmet` constants are the right single-home shape for the reasons.
- **V5.** `floor.py` and `GUARDS.md` disagree at HEAD on the marker question (CD2); quotescan's
  reason disagrees with the schema (CD6). Cross-references checked for the rule reached: the seven
  resolving citations each hold the rule named (lens 2).
- **V6.** Lens 4 above; `/security-review` NOT RUN with grounds.
- **V7.** Stated above.

### Findings

Every finding is the principal's to decide (rule 3): recorded, none applied. Counsel is labelled.

- **CD1 — MODERATE.** `reviewed` is accepted as any non-empty string, so a rule turns `met` with
  no verdict named, and a child's `local` declaration reads `decl 5/5` and raises its CI line's
  "meet all five" count with `"reviewed": "nothing at all"` (probe a). Every other reference in the
  schema is checked for existence; this one, the only field whose `met` is defined as a person's
  reading, is not. The registry sets no `reviewed`, so today's counts are honest; the test
  `test_a_citation_resolves_and_only_a_verdict_makes_it_met` pins the gap with a path that does not
  exist. The brief's worst class, reached from author input. *Counsel:* `reviewed` resolves like a
  citation (a `_safe_rel` path under `docs/reviews/` that `is_file()`), else the rule stays
  `resolves` with the reason "reviewed names no verdict file"; rename the test to what it proves.
- **CD2 — MODERATE.** The "carried, not settled" allow-marker statement is stale at HEAD in four
  places: `_MARKER_OPEN` and its comment (`floor.py` 613–626, printed in six checks' `window`
  reasons), `tools/README.md` 2813, `CHANGELOG.md` 404, and the test pin at `test_floor.py` 3086.
  `GUARDS.md` § Before building a check answered it on 2026-11-12 (`2a6d7a41`: "A reasoned
  allow-marker counts as bringing the missing context inside the window") and the 2026-11-16 census
  records GRD8 as enforced. Six declarations now state as open something the record decided, the
  brief's third class, on every `--declarations` run. Accurate when landed. *Counsel:* the
  `160/1440` pass or the group-A lane restates the six windows (leakscan, sizescan, datescan,
  attribscan, namescan, quotescan) with a `fits` and the reasoned marker as licensing context, and
  retires `_MARKER_OPEN`, the README paragraph and the test together; `2a6d7a41`'s mirror list is
  where the miss belongs.
- **CD3 — minor.** One replay naming a test file that does not parse turns all five fields
  `missing — unreadable declaration: invalid syntax`, erasing a resolving rule and a met window
  and posture, and reusing `missing` ("not declared") for "the reader raised" (probe d; pinned by
  `test_an_unreadable_replay_file_never_raises`). The README's "a finding, not a crash" is half
  true. *Counsel:* catch `SyntaxError`/`ValueError` inside `_replay_problem` and return
  `"<replay>: test module does not parse"` as a grounding `unmet`; keep the outer `except` for
  reader bugs only.
- **CD4 — minor.** `_safe_rel` is lexical; a symlink committed inside the repo lets a citation,
  incident or replay make the reader open and report on a file outside it (probe b). LA8 as the
  brief wrote it, symlinks named, is damaged. Bounded: the author already runs code in that CI.
  *Counsel:* resolve `base / rel` and require it under `base.resolve()`, as `_inside` already does
  for `run`.
- **CD5 — minor.** secretscan's rule reason "names the SECRETS doctrine, no section" is false:
  `secretscan.py` line 44 cites `SECRETS.md § The boundary's posture`, a heading that exists
  (`SECRETS.md` line 223). *Counsel:* either cite it (the rule then `resolves`, and a reviewer
  decides whether the detection posture is the rule the check serves) or restate the reason.
- **CD6 — minor, HEAD state (`b462fd7d`, not `ba55be27`).** quotescan's rule reason says the two
  slices' sources cannot both be stated because "one field cannot state both"; `rule` is a tuple
  and reviewscan cites two. A declaration false of the schema it sits in. *Counsel:* cite both
  (`docs/method/AUTONOMY.md § Always confirm` exists) or drop the clause.
- **CD7 — minor.** The `declares` key is documented in README only; the two places README calls
  "the full contract" of the seam, `floor.py`'s module docstring § THE REPO-LOCAL SEAM (keys `run`,
  `why`, `planes`, `args`, `scope`) and the `.atelier-floor.json` bullet in `REPO-STANDARD.md`, do
  not carry it (V3).
- **CD8 — note.** pointerscan's incident is labelled `injected: ...` while its replay's docstring
  calls the text "instance 1, still standing when this shipped": a live specimen, which the
  schema would record as a board item or verdict path.
- **CD9 — note.** `GUARDS.md`'s posture pass is "one of the two words, and what it costs"; the
  reader marks posture `met` on the word alone, and `_load_declares` accepts an empty
  `posture_cost` (probe a: `met` with no cost). The registry test requires the cost; a child's does
  not.
- **CD10 — note.** The surfaces print "21 checks" and nowhere say what runs outside the count:
  `stampscan` and `blockscan` in `ci.yml`, `signscan` in `floor.yml`, the hook-plane guards. The
  design note names them as group E; the delta's CHANGELOG, README and line do not. Against
  "every check now", the count line reads as the whole.
- **CD11 — note.** The design note's status line ("nothing built and no check changed") and
  `docs/decisions/README.md` line 49 still say so at HEAD; the note is under `160/1300`, so noted
  here as the landing's unswept mirror only.
- **CD12 — note.** The purpose-gap machine half is exact inequality with the `why`: a one-character
  string is `met` (probe a). Design-accepted; stated so the `decl N/5` column is read as "stated",
  never as "right".

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (CD1, CD2), 5 minor (CD3–CD7), 5 notes
(CD8–CD12).**
The build does what it says on the registry and changes no exit anywhere; its two gaps are a
machine half left unread on the one field that models a person's reading, and a six-check
statement that the record has since decided.

### Re-run ledger (V2)

| Line | Result at `e24ff31f`, 2026-11-22 UTC |
|---|---|
| `git merge-base --is-ancestor ba55be27 HEAD` | exit 0 |
| `coldsweep --root . --commit ba55be27` | exit 0; subject, stat, diff; 2 board-store files left out |
| `floor.py --root . --declarations` | exit 0; "21 checks, 0 meet all five"; 148 lines |
| `floor.py --root . --declarations --json` | exit 0 |
| `floor.py --root . --list --plane ci` | exit 0; 21 rows with `decl N/5` |
| the `awk` line | 21 names |
| `python3 -m unittest test_floor` (tools dir) | 260 tests OK in 327 s under `nice -n 10` with Python 3.14 (the suite refuses < 3.11; the system `python3` is 3.9; the brief's 255 in 184 s predates five later tests) |
| `python3 -m unittest test_floorfleet` | 127 tests OK in 16 s |
| Live, read-only: old (`ba55be27^`) vs new (`ba55be27`) `floor.py` on five clean children, CI and hook planes, run from inside each child, no network | exit codes identical (1 = 1, from `board` on each, both versions), sorted result sets identical, 19–22 results per run; the new `--json` adds `declarations`. A first attempt from a scratch cwd made the hook plane degenerate and was discarded (work log). The dirty child was skipped as another session's; atelier excluded |

### Follow-up checklist (for the principal, rule 3)

- [ ] CD1: decide whether `reviewed` must name an existing verdict file before a rule is `met`.
- [ ] CD2: decide who restates the six marker-leaning windows and retires the four stale
      statements (`160/1440`'s pass, or a group-A lane), and whether `2a6d7a41`'s sweep is a
      `PROPAGATION.md` miss worth its own item.
- [ ] CD3, CD4: two reader hardenings, each a few lines, in one lane on `floor.py`.
- [ ] CD5, CD6: two reason corrections in the registry.
- [ ] CD7, CD11: three mirror sweeps (seam docstring, REPO-STANDARD bullet, design note status).
- [ ] CD8–CD10, CD12: notes to carry into the group lanes; none needs its own item.
- [ ] The brief's *Since the delta* paragraph: a brief-writer's staleness, not the work's; the
      review-brief skill may want a "re-check the since-line at claim" step.

### Reconcile

Act 2, 2026-11-22 UTC, after act 1 was committed (`8f96202b`). Read now: the sibling (14
questions, 10 facts), the commit body of `ba55be27`, item `115/120` from line 71 (the author's
landing notes and the 2026-11-12 answer), and the `160/1430` pointer. No act-1 text is revised.

**Against the sibling's questions.**

- Q1 (a resolving citation names the rule it claims): lens 2 answered it independently; all
  seven reach the rule the check serves. No change.
- Q2 (an `Unmet` reading as met in any view): LA4 confirmed; no surface does. The inverse route,
  `met` with nothing behind it, is CD1.
- Q3 (`window met` on `fits="outside-warn-only"`): `GUARDS.md`'s pass bar is "inside the window, or
  outside with its way out named", so `met` is the right word for a stated way out; what a `decl
  N/5` reader cannot tell is "stated" from "right", which CD12 already says of the purpose gap.
  CD12 now reads as covering the window too; no new finding.
- Q4 (the marker question stale in six declarations, README and a test): CD2, formed before the
  sibling was opened, with the same four sites. Whose job: the landing note on `115/120` records
  the 2026-11-12 answer and says "Group A is no longer waiting on it", so the session that recorded
  it (`d0ca5d24`, per the item) had the mirror list in hand and swept `GUARDS.md` only. The counsel
  under CD2 stands.
- Q5 (is any met gap a restated mechanism; is "not identical to `why`" the bar meant): read at
  reconcile, each of the 16 `met` gaps names a need of the rule and what the check reads instead;
  the six that would have failed the design's bar are stated `Unmet` ("technique limits only"). The
  machine's bar is weaker than the design's words and CD12 says so. No new finding.
- Q6 (`reviewed` as any non-empty string): CD1, exactly, probed before the sibling was opened. The
  landing note confirms the intent the code does not check: "`reviewed` (a verdict reading each
  cited rule against its check) is what takes any rule from `resolves` to `met`".
- Q7 (an incident as any existing file): I had read the code and not weighed it. Probe (b)
  accepted a scratch symlink under `docs/decisions/`, not a verdict, as an incident, so the
  evidence exists:
  **CD13 — note, formed at reconcile.** `_read_grounding` accepts any `_safe_rel` path that
  `is_file()` as an incident, so `README.md` would stand where the design says "a verdict path".
  Same class as CD1 (an existence test looser than the design's words); the registry's three stated
  incidents are a board item and two `injected:` labels, so today's count is unaffected.
  *Counsel:* require `docs/reviews/` for a path incident, or widen the design's words.
- Q8 (one broken test file erases the whole declaration): CD3.
- Q9 (does each replay fail when the check stops firing): LA3, with the publishscan caveat.
- Q10 (`--plane hook --json` computes the report): I confirmed LA6 "by structure" for the callers
  that exist. The sibling's sharper point is right: **CD14 — note, formed at reconcile.** The
  README's "the hook plane prints nothing and pays nothing" is true of every hook caller today
  (none passes `--json`) and false of the plane: `test_the_json_key_is_present_on_every_run` pins
  that `--plane hook --json` carries the key, which means it read every cited file and parsed
  every replay module. A statement about callers worded as one about the plane. *Counsel:* say
  "the hooks' invocation" in README and the class docstring, or skip the report on `hook`.
- Q11, Q12 (what the fleet line and the CI line count): CD10 already says the line gives no account
  of what is outside it; the sibling adds that the fleet line is atelier's registry only (an empty
  `Config()`) and a child's CI line is atelier's 21 plus that child's `local` checks, with no
  origin split. Both are now part of CD10's note; no new finding.
- Q13 (`::` commands and symlinks): lens 4; the `::` vector is closed by `strip_controls` at the
  parse seam and by the reader never printing a reason at column 0; the symlink gap is CD4.
- Q14 (three census ✅ windows moved to `Unmet`): the commit body says it openly ("three windows
  the census marked as met are not `met` here") and gives the reason. A departure from step 0's
  letter ("`Unmet` wherever the census has no ✅") in the direction of honesty, recorded in the
  per-claim ledger as such; the design note's own "Not decided here" named the question, so the
  design foresaw it. No finding. The landing note's "the checks in Group E that lean on a marker"
  misnames attribscan, namescan and quotescan, which are registry checks, not group E (note only).

**Against the sibling's facts.** Fact 1's totals (22 met, 7 resolves, 76 unmet, 0 missing) match
my hand count (LA11). Facts 2 and 3
are stale at this HEAD (260 tests, four later commits), as act 1 says. Fact 8 (`GOOD` cites
`docs/x.md`, a form the grammar does not know) confirms that `DeclarationConfigTest` tests <!-- pathscan:allow: a fixture string quoted from DeclarationConfigTest.GOOD, not a repo path -->
loading, not resolving; the resolving tests are in `DeclarationReaderTest`, so no gap. Fact 10 is
CD11.

**Against the author's account.** The commit body's four claims checked: all 21 state all five ✓;
every stated citation and replay pinned to resolve ✓ (the registry test); the marker question
"stays open" ✓ on 2026-11-10 and stale since 2026-11-12 (CD2); old against new on five children
identical ✓ re-driven on five, both planes. The landing note's "probe on five children, one at a
time" matches the re-drive shape. Nothing in the body or the notes was formed into a finding
except where act 1 had already found it.

**Overall, restated.** PASS-WITH-FINDINGS — 0 MAJOR, 2 MODERATE (CD1, CD2), 5 minor (CD3–CD7),
7 notes (CD8–CD14; CD13 and CD14 formed at reconcile).

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

Preface (orchestrator, session cd7d5f1e, which forms no finding): the text below is the brief's
held-back sibling, `2026-11-14-0318-check-declarations-step-0-cold.deferred.md`, verbatim. It was
removed from the review worktree before the reviewer started, held outside the repo, and released
to the reviewer only after act 1 was committed (`8f96202b` before rebase). The reviewer read it for
act 2 (`### Reconcile` above). The separate file is removed in the fold commit; this copy is its
record.

# Held back — every check states its five declaration fields (`115/120`, step 0)

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `263945c1`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Does a `Declares` citation that resolves actually name the rule it claims?
2. Can an `Unmet` read as met in any view?

## The brief-writer's questions

3. The design note's table makes `window` `met` whenever a `fits` value is present. Three checks
   declare `fits="outside-warn-only"`, a statement that the licensing context is *outside* their
   window, and each reads `window ✅ met`. Does `met` there tell a reader the field is stated, or
   that the check passes the window test? Is a reader of `decl N/5` able to tell which?
4. `_MARKER_OPEN` says the fits answer "waits on the open question whether an allow-marker brings
   the licensing context inside the window". `2a6d7a41` (2026-11-12) recorded the principal's answer
   in `GUARDS.md`, and `tools/floor.py`, `tools/README.md` ("One question is carried, not settled")
   and the test that pins the text were not touched after it. Are six declarations, a README
   paragraph and a test now stating an open question that the record says is answered? Whose job
   was the sweep (V3)?
5. `purpose_gap` reads `met` when it is non-empty and not, case-insensitively, the `why` string
   verbatim. Is any of the registry's stated gaps a restated mechanism the test cannot see, and is
   "not identical to `why`" the bar the design note's "not the `why` text" meant?
6. `rule` turns `met` on any non-empty `reviewed` string. Nothing checks that it names a verdict
   file, or that the verdict read this rule against this check. Is that the machine's half, or a
   way to reach `met` with no verdict?
7. A grounding `incident` is accepted when it is `injected: …`, `board NNN/NNN`, or *any* file path
   that exists inside the base, not only a verdict under `docs/reviews/`. Could `README.md` stand
   as an incident? Does that match "a board item, a verdict path"?
8. `test_an_unreadable_replay_file_never_raises` asserts only that `grounding` reads `missing`. In
   `read_declaration`, any exception in any field sends all five fields to `missing`. Is one broken
   test file elsewhere in the repo meant to erase a check's whole declaration, including fields that
   resolved? Is `missing` (not declared) the honest state for "declared, and the reader failed"?
9. Two of the three replays name `injected:` incidents; the third names `board 010/020`. Does each
   replay fail when its check stops firing (LA3), or does it test a neighbouring behaviour?
10. `--json` on *any* plane, including `--plane hook --json`, computes `declarations_report`, which
    reads every cited file and parses every replay module. The hooks call `--plane hook` without
    `--json` today. Does "the hook plane pays nothing" hold for every caller, or only for the
    one invocation the hooks make?
11. `floorfleet`'s line is built from `floor.Config()`, an empty config, against this checkout's
    tree. It cannot see any child's `local` checks or their declarations. Does a fleet-board line
    that reads "21 checks" for every child say what it covers?
12. The CI line goes to stderr only on a text run; a `--plane ci --json` run carries the key and no
    line. The floor workflow runs the text plane (`floor.yml` line 134), so the line reaches every
    child's CI log, read from atelier's registry. Does a child reader of that line know it counts
    atelier's checks plus that child's `local` ones, and nothing of the child's purpose?
13. A child's `local.<name>.declares` text reaches `--declarations` output verbatim. If a floor
    workflow ever prints that table, or a reason string, inside Actions, can a crafted reason emit a
    `::` workflow command? Is `_safe_rel` enough against a symlink inside the child that points out
    of it (`Path.is_file` follows links)?
14. The census marked three windows as met that step 0 states as `Unmet` (per the commit body,
    barred until phase 2). Was moving a census ✅ to `Unmet` within step 0's brief ("`Unmet`
    wherever the census has no ✅"), or a departure from the design the principal approved?

## Facts read off the machine (2026-11-14 UTC, worktree at `672acdd9`)

1. `python3 tools/floor.py --root . --declarations --json`: 21 checks, 0 meet all five; field
   states across all 105 fields: 22 `met`, 7 `resolves`, 76 `unmet`, 0 `missing`. The commit body
   gives the same three totals.
2. `cd tools && python3 -m unittest test_floor`: 255 tests, OK, about 184 s. `test_floorfleet`: 127
   tests, OK, about 14 s.
3. `git log --oneline ba55be27..HEAD -- tools/floor.py tools/floorfleet.py tools/test_floor.py
   tools/test_floorfleet.py` prints nothing.
4. `docs/method/GUARDS.md` at HEAD has `## Before building a check: the evidence window` (line 151)
   and `## What every check declares` (line 214).
5. `test_the_open_marker_question_is_carried_not_settled` pins `_MARKER_OPEN` in the `window` of
   `leakscan`, `sizescan`, `datescan`, `attribscan`, `namescan` and `quotescan`.
6. The floor workflow parses `floor.py --list --plane ci` with
   `awk '$2!="disabled" && $3!="local"{print $1}'` (`.github/workflows/floor.yml` line 126). The
   new column comes after the origin column, so `$2` and `$3` keep their meaning; at HEAD the parse
   printed 21 names, including the 12-character `conflictscan`.
7. `.githooks/pre-commit` line 84 runs `floor.py --plane hook --root … --tools …`, with no `--json`.
8. `DeclarationConfigTest.GOOD` uses `"rule": ["docs/x.md"]`, which is not a form the citation
   grammar knows; it tests loading, not resolving.
9. The 2026-11-12 allow-marker answer is recorded in `115/120` line 96 onward and, through
   `2a6d7a41`, in `GUARDS.md` § *Before building a check*.
10. The design note's status line still reads "proposed (design only; nothing built and no check
    changed)" at HEAD, after step 0 built it.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/1430, cold pass on check declarations step 0 (`ba55be27`)

Reviewer: Fable 5.1. Worktree: `/Users/mike/worktrees/fable/atelier-160-1430-2248/atelier`.
Started 2026-11-22T22:51Z. Commands, files and evidence only. Act 1 entries are written
before the `.deferred.md` sibling is released.

## Setup

- `git status --short` → only ` D docs/reviews/...deferred.md` (the partition, expected).
  HEAD `e24ff31f`. `git merge-base --is-ancestor ba55be27 HEAD` → exit 0 (re-run line 1 OK).
- Read the brief in full (lines 1–302).
- Read `docs/method/REVIEW.md` § What a review actually checks, § Re-run every live-proven claim,
  § The standing checklist (lines 302–460) for lenses and V1–V7.
- Read the acceptance test: item `115/120` lines 1–70 only (`sed -n '1,70p'`). Line 70 holds the
  principal's answer *"Everything, on every check now"*. Lines 71+ not read (barred).
- `python3 tools/coldsweep.py --root <worktree> --commit ba55be27` → scratch `delta.txt`
  (1,449 lines; subject, stat, diff; body not printed; 2 board-store files left out). Read in
  full: CHANGELOG entry, GUARDS.md paragraph, README section, floor.py (schema, 21 Declares,
  `_load_declares`, reader, `main`), floorfleet line, test_floor.py (4 new classes), test_floorfleet.
- Read `docs/decisions/2026-11-09-1334-check-declaration-standard.md` in full (the spec; disclosed).
- Read `docs/method/GUARDS.md` lines 184–284 (§ Before building a check; § What every check
  declares) at HEAD, and lines 35–80 (§ The fourth requirement, posture table).
- `coldsweep --commit 2a6d7a41 --path docs/method/GUARDS.md`: the hunk replaces "Not settled
  here: whether an allow-marker counts..." with "A reasoned allow-marker counts as bringing the
  missing context inside the window" (the principal's pick, 2026-11-12 UTC). Evidence for LA10.
- `coldsweep --commit 4bfb4e16 --path tools/README.md`: one unrelated section added at line 2188;
  the `--declarations` section untouched.
- `git log --oneline ba55be27..HEAD -- tools/floor.py tools/floorfleet.py tools/test_floor.py
  tools/test_floorfleet.py` → FOUR commits (the brief said none at `672acdd9`; HEAD has moved):
  `734930ef` (test_floor.py only, graces), `ef4972e6` (floor.py: `tree_summary`, a stderr line
  before the declarations line), `b462fd7d` (floor.py: quotescan's `why` and its `Declares` text
  rewritten), `cf648679` (floor.py/test_floor.py: flags spelling + coverage line; no Declares hunk).
  Each read body-free with `coldsweep --commit <sha> --path ...`.

## Re-run list (V2), at HEAD e24ff31f

1. `git merge-base --is-ancestor ba55be27 HEAD` → 0.
2. `coldsweep --commit ba55be27` → 0 (above).
3. `python3 tools/floor.py --root <worktree> --declarations` → 0; 148 lines; header
   "floor declarations — 21 checks, 0 meet all five". Saved as scratch `decl.txt`.
4. `... --declarations --json` → 0; saved `decl.json`.
5. `... --list --plane ci` → 0; 21 rows, each `name state fleet decl N/5 why`.
6. `... --list --plane ci | awk '$2!="disabled" && $3!="local"{print $1}'` → 21 names.
7–8. test_floor / test_floorfleet: see below.

## LA11 — counts re-derived by hand from the diff, before running the reader

Per check, fields that the reader's rules would call `met` (text non-empty and != why; Window
with a valid fits; posture one of two words; grounding with every replay resolving; rule met only
with `reviewed` set, which no registry entry sets): secretscan 0, leakscan 1, conflictscan 0,
linkscan 0, reviewscan 1, publishscan 2, sizescan 2, board 1, datescan 1, wrapscan 0, spellscan 1,
harvestscan 1, pointerscan 2, pathscan 1, indexscan 2, attribscan 1, pdlistscan 2, sweepscan 2,
namescan 0, quotescan 1, licenscan 1 = 22 met fields; 7 `resolves` rules (leakscan, reviewscan,
board, spellscan, pointerscan, pdlistscan, sweepscan); 0 meet all five. The `--list` run printed
exactly these 21 N values. LA11 confirmed.

## Surfaces and callers (LA5, LA6, LA9)

- `.github/workflows/floor.yml` line 126: `floor.py --list --plane ci --root repo | awk '$2!=
  "disabled" && $3!="local"{print $1}'` (columns 1–3 unchanged; `decl N/5` is columns 4–5);
  line 134: `floor.py --plane ci --root repo --tools atelier/tools` (no `--json`).
- `tools/pre-commit.sample` line 84: `floor.py --plane hook --root ... --tools ...` (no `--json`);
  `commit-msg.sample` line 46: `--plane msg`. No hook caller passes `--json` or `--list`.
- `.github/workflows/ci.yml` lines 100–103, 181: same two shapes for atelier itself; lines 199,
  227–229 run `stampscan` and `blockscan` outside the registry (group E, on CI).
- `floor.py main` (delta lines 964–1013 of `delta.txt`): declarations computed on `--declarations`,
  `--list`, any `--json` run, and the stderr CI line when `plane == "ci"` and not `--json`. The
  hook plane without `--json` never reaches `declarations_report`. Exit is
  `1 if any(r.failed ...) else 0` with no read of the report.
- Other `--list` consumers found by grep: `docs/build/templates/CONTRIBUTING.md:45` (human-read),
  `tools/test_templates.py` (asserts the command string exists), `test_floor.py`. None parses a
  column past `$3`.
- `floor.py github_visibility` (lines 2528–2555) reaches the network only when
  `GITHUB_REPOSITORY` matches a slug; a local `--plane ci` run makes no request.

## LA1 — the Unmet reasons against each docstring (grep, `tools/<x>.py`)

secretscan: docstring line 10 names "the SECRETS doctrine"; line 44 cites `SECRETS.md § The
boundary's posture` — a SECTION is named; `SECRETS.md` line 223 has that heading. The Unmet
reason "no section" is inaccurate (candidate finding). conflictscan line 5 `320/200` ✓. linkscan
line 4 PROPAGATION.md, no section ✓. reviewscan line 60 F6 ✓. publishscan line 13/54 F1 ✓.
sizescan line 13 "three thousand lines", 117–124 the ruling restated ✓. datescan line 4 seam S3,
line 9 five-file sweep ✓. wrapscan line 4 seam S1 ✓. spellscan line 7 CONVENTIONS.md ✓.
harvestscan line 75 HV1, lines 50/91/113 `--replay` by hand ✓. pointerscan line 10 "REVIEW.md
rule 4"; rule 4 is at REVIEW.md line 203, inside § Independence is more than fresh context (line
25; next `##` is line 302) so the citation reaches the rule ✓. pathscan line 4 seam S2 ✓.
indexscan line 4 `200/010`; test_indexscan line 3/227 `320/430` ✓. attribscan line 4 `320/100` ✓.
pdlistscan line 4 `160/630` ✓; docstring does not name REPO-STANDARD, the cited § Repo-craft
conventions (REPO-STANDARD.md line 188) holds the purpose test (lines 193–213) ✓. sweepscan line
4 `320/060`, line 37 CONCURRENCY.md; § The trigger — assume you are not the only session is at
CONCURRENCY.md line 29 ✓. namescan line 4 NP2/160/360 ✓. quotescan line 5 QK1/160/900 ✓.
licenscan: no rule text, no incident in docstring ✓. leakscan line 5 cites "REPO-STANDARD.md §
Personal data" (a bullet, not a heading); the registry cites the real heading ✓.
sizescan posture_cost "(from 2026-12-09)" matches the registry comment `ADVISORY_BARRED_FROM` ✓.

## LA3 — the three stated replays, read (ast print of each method)

- publishscan `PatternTest.test_the_grounded_pattern_reds`: asserts `publishscan.matches(
  ".claude/settings.json")` is non-None and names "unprompted". Fails if the pattern stops
  matching the incident path; does not drive the tracked-file walk or the exit code. Partial ✓.
- board `StagedPlane.test_slip_a_is_caught_on_the_staged_plane`: real git repo, stages the item,
  rebuilds on disk, asserts `run_check(source=INDEX)` returns 1. Fails if the check stops firing ✓.
- pointerscan `GrammarTest.test_the_live_specimen_is_flagged`: feeds the real instance-1 pointer
  text, asserts detector "grammar" fires with 2 reasons ✓. Its docstring calls the text "instance
  1, still standing when this shipped": a live specimen, while the registry labels the incident
  `injected: ...` (candidate note: wrong incident class).

## LA10 — mirrors at HEAD still saying the marker question is open (grep)

`tools/floor.py` 613–626 (comment and `_MARKER_OPEN`, used by 6 windows), `tools/README.md` 2813
("One question is carried, not settled"), `tools/test_floor.py` 3086 (test pins the Unmet),
`CHANGELOG.md` 404 ("stays open"). Against: `GUARDS.md` lines 234–242 at HEAD (answered
2026-11-12), and `docs/method/census/2026-11-16-1204-...md` row GRD8 "enforced (blocks)".
Accurate when landed (2026-11-10, GUARDS.md then read "Not settled here"); stale at HEAD.

## Scratch child probe (LA2, LA5, LA7, LA8, lens 4) — `scratchpad/probe-child`, never a real child

Built a git repo with `docs/method/RULE.md` (heading "Real heading"), `tools/test_x.py` (class C,
test_y), `tools/test_broken.py` (`def (:`), `tools/t.py` (exit 0), `docs/roadmap/010-x/020-y.md`,
two symlinks to `/etc/hosts` (`docs/method/OUT.md`, `docs/decisions/out.md`), and six `local`
checks with `declares` (saved in the probe's `.atelier-floor.json`). Ran
`floor.py --root <probe> --tools <worktree>/tools --declarations` (exit 0; header "27 checks, 1
meet all five"):
- (a) `reviewed: "nothing at all"` + a resolving section citation + `purpose_gap: "x"` + a valid
  Window and posture → `decl 5/5`, rule `met`. Nothing checks that `reviewed` names a file. LA2
  DAMAGED (candidate CD finding). `test_floor.py` `test_a_citation_resolves_and_only_a_verdict_
  makes_it_met` pins `reviewed="docs/reviews/x.md"` (a path that does not exist) as `met`.
- (b) a citation to a symlink pointing outside the repo → "no such heading" (the target was
  opened and read); an incident naming the `docs/decisions/out.md` symlink is accepted as a verdict
  path (`is_file()` follows the link). `_safe_rel` is lexical only. LA8 damaged at the symlink
  level (candidate minor).
- (c) `..` segments and absolute paths in rule, incident and replay → "not a path inside the
  repo" / "no such decision record" ✓.
- (d) a replay naming a test file with a syntax error → ALL FIVE fields `missing — unreadable
  declaration: invalid syntax`, including a rule that resolved and a met window and posture
  (candidate finding: one bad replay path erases four honest fields and reuses `missing`).
- (e) a rule string carrying `\n::error::injected line\n` → loaded as
  `prose::error::injected line` (control characters stripped at the parse seam,
  `floor.py` line 1474 `strip_controls`); `--json` escapes; the CI line prints counts only. No
  new `::` vector reaches a CI log (nothing in `floor.yml`/`ci.yml` runs `--declarations`).
- (f) an unknown key inside `declares` → all `missing — not declared, or malformed`; a typo of the
  key itself (`declare`) → `ConfigError`, exit 1 (pre-existing strictness). LA7 confirmed.
- LA5: `--plane ci` and `--plane hook`, text and `--json`, on the probe with every `declares`
  present and again with every `declares` stripped (`probe-child-nodecl`): exit 1 both times on
  both planes, from real scanner results (ci: `board` rc 1; hook: secretscan, leakscan,
  conflictscan, attribscan rc 2 on my fixtures); the sorted result tuples are identical with and
  without declares; `meet_all_five` 1 vs 0. No exit read a declaration. Confirmed.
- Old `floor.py` (`ba55be27^`) on the probe config: `ConfigError: unknown 'declares'`, exit 1.
  A child that declares while a stale atelier checkout serves its hook fails closed (seam
  strictness, pre-existing; note only).
- New test count at `ba55be27`: DeclarationRegistryTest 6, DeclarationReaderTest 13,
  DeclarationConfigTest 4, DeclarationSurfaceTest 5 = 28 (+ DeclarationLineTest 1) ✓.
- `git diff ba55be27 HEAD -- tools/README.md`: no line of the `--declarations` section changed.
- V3 mirrors of the seam contract: `floor.py` module docstring § THE REPO-LOCAL SEAM (line 204+)
  lists `run`, `why`, `planes`, `args`, `scope` and not `declares`; `docs/build/REPO-STANDARD.md`
  has no `declares`; README line 2757 names those two as "the full contract" (candidate minor).
- Design note status line at HEAD: "proposed (design only; nothing built and no check changed)";
  `docs/decisions/README.md` line 49: "proposed, design only, review owed" (stale once step 0
  landed; candidate note).

## Live re-drive (V2), read-only, children counted not named

Driver `scratchpad/redrive.py`: old (`ba55be27^`) and new (`ba55be27`) tools dirs extracted with
`git archive` into scratch; per child, `floor.py --plane {ci,hook} --root <child> --tools <ver>
--json` under `nice -n 10`, GITHUB_* env unset (no network); compares exit codes and the sorted
(name, state, rc, ran) result set. 22 children carry `.atelier-floor.json` on this machine; one
is dirty (skipped, another session's); atelier itself excluded.
- First attempt (background, cwd = scratch): the CI plane on a 415-file child ran > 10 min under
  load 8–17 and the task was killed when my turn ended; the hook plane from a scratch cwd was
  degenerate (the `--staged` scanners exit 2: "reads the git index of the directory it is run
  in, and that is not the repo --root names"). Driver patched to `cwd=<child>`; children re-chosen
  by tracked-file count (117–193 files); reruns in the foreground.
- Hook plane, five children, 2026-11-22 ~23:23Z: old exit 1 = new exit 1 on each; sorted result
  sets identical; 19–20 results each; the only non-zero result is `board` rc 1 (the staged board
  check read outside a commit), on old and new alike. New `--json` adds the `declarations` key.
- CI plane, the same five, ~23:24–23:25Z, 6–9 s per run: old exit 1 = new exit 1 on each; result
  sets identical; 21–22 results; the only non-zero result is `board` rc 1 on every child with both
  tool versions (the extracted 2026-11-09 `board.py` reading indexes rebuilt by today's board.py:
  a vintage artefact, identical across the pair, so the comparison stands). The delta's claim
  "identical exit codes and result sets on five children, CI and hook planes" reproduces.
  Detail files: `scratchpad/child{1..5}-{ci,hook}.detail.txt`; no child name in this log.

## Test suites (re-run lines 7–8), foreground, `nice -n 10`, one at a time

- `python3 -m unittest test_floor` with the system `/usr/bin/python3` (3.9): ImportError, the suite
  refuses < 3.11. Re-run with `/usr/local/bin/python3` (3.14.6): `Ran 260 tests in 326.573s OK`
  (23:26–23:31Z). The brief's 255/184 s predates five later tests; load was 4–9.
- `python3 -m unittest test_floorfleet` (3.14.6): `Ran 127 tests in 16.431s OK`. The rendered board
  carried `🟡 declarations: 21 checks, 0 meet all five (floor.py --declarations)`.
- `git status --short` after both: only the sibling deletion and the brief (my act 1). Worktree
  otherwise untouched.

## Act 1 written

- Verdict appended below `---` in the brief (file now ~604 lines); Status line updated to "ACT 1
  WRITTEN 2026-11-22 UTC ... act 2 pending". Findings CD1–CD12: 0 MAJOR, 2 MODERATE (CD1 reviewed is
  free text; CD2 marker question stale at HEAD), 5 minor (CD3 unreadable replay collapses all five
  fields; CD4 symlink containment; CD5 secretscan reason false; CD6 quotescan reason false at HEAD;
  CD7 seam contract homes lack `declares`), 5 notes (CD8–CD12).
- Scanners on the brief from the worktree root: datescan 0, wrapscan 0, spellscan 0, linkscan 0,
  reviewscan 0, leakscan 0 (0 findings); pathscan exit 1 with 3 findings, all on the brief-writer's
  lines 259/261 (record files retired since 2026-11-14 and the removed sibling), none on act-1 text;
  pathscan is warn-only in the registry. My one line naming those files was reworded. Prose lines of
  act 1 checked at ≤ 100 characters.
- `/security-review` NOT RUN: the pending diff is the deleted sibling.
- Left out and why: the registry's 18 `Unmet` groundings were not mutation-tested (no replay exists
  to mutate); `--include-barred` never used; no child written to; scratch probes stay in the
  scratchpad (no live captures).

## Act 2 (reconcile), 2026-11-22 ~23:45Z, after act 1 committed as `8f96202b`

- Read the released sibling (14 questions, 10 facts), `git log -1 --format=%B ba55be27` (the body),
  item `115/120` lines 71+ (landing notes; the 2026-11-12 answer), the `160/1430` pointer.
- Q1→lens 2; Q2→LA4/CD1; Q3→CD12 (GUARDS.md bar "outside with its way out named"); Q4→CD2 (the
  item's third bullet shows the recording session had the list); Q5→16 met gaps re-read, CD12;
  Q6→CD1 (landing note states the intent); Q7→new CD13 note (probe (b) had accepted a non-verdict
  path as an incident); Q8→CD3; Q9→LA3; Q10→new CD14 note (README's "pays nothing" is about callers,
  `--plane hook --json` reads everything; pinned by test); Q11/Q12→CD10; Q13→lens 4 + CD4;
  Q14→commit body discloses the three ✅→Unmet moves; no finding; landing note misnames the three
  new checks as group E (note).
- Facts: 1 matches LA11; 2, 3 stale at HEAD; 8 confirms ConfigTest tests loading only; 10 = CD11.
- Appended `### Reconcile`; act-1 text unrevised. Overall restated: 0 MAJOR, 2 MODERATE, 5 minor,
  7 notes. Sibling not folded, nothing deleted (the orchestrator folds).
- Scanners on the brief after act 2 (worktree root): datescan 0 (one slash-date in my fact line
  reworded to words), wrapscan 0, spellscan 0, linkscan 0, leakscan 0, reviewscan 0; pathscan's
  remaining hits are the brief-writer's lines 259/261 only (two retired record files, the removed
  sibling); one fixture string quoted from the tests carries the repo's pathscan allow-marker.
  Act-2 prose ≤ 100 characters. `git status`: only the sibling deletion and the brief. No commit.
- Scratch left in the session scratchpad only: `delta.txt`, the commit dumps, `decl.*`, `list.txt`,
  `probe-child*/`, `old/`, `new/`, `redrive.py`, `child{1..5}-*.detail.txt` (scanner result tuples
  and local paths; no secrets, no provider reads). Finished 2026-11-22T23:43Z.
