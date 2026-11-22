# Cold pass — every check states its five declaration fields (`115/120`, step 0)

**Board:** `docs/roadmap/160-doctrine-review-owed/1430-rule-4-cold-pass-queued-check-declarations-step-0.md`
**Status:** ACT 1 WRITTEN 2026-11-22 UTC (PASS-WITH-FINDINGS, 0 MAJOR, 2 MODERATE); act 2, the
reconcile against the sibling, pending. Brief written 2026-11-14 UTC by a headless Opus 5.5
brief-writer (`cclive` lists it as session `263945c1`); run under the principal's drain order of
2026-11-23 NZDT by a Fable 5.1 reviewer (see the verdict below).

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
`docs/reviews/2026-11-14-0318-check-declarations-step-0-cold.deferred.md` (a held-back file; by
count: 14 questions, 10 facts), every item under `docs/roadmap/160-doctrine-review-owed/` beyond its
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
