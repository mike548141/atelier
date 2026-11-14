# Cold pass — every check states its five declaration fields (`115/120`, step 0)

**Board:** `docs/roadmap/160-doctrine-review-owed/1430-rule-4-cold-pass-queued-check-declarations-step-0.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `263945c1`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
