# Cold pass — coverage accounting: a scan of nothing no longer reads as clean

**Board:** `docs/roadmap/160-doctrine-review-owed/1380-rule-4-cold-pass-queued-coverage-accounting.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `2a99cef1`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4: a shared reporting helper and its
use in twenty floor scanners, plus a doctrine sentence in `docs/method/GUARDS.md`, all
self-authored, all inherited by every child through the floor.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** large in breadth, shallow per file: two commits, about 1,500 added lines
across 46 paths (two of them board files). `tools/report.py` gains two functions (about 60 lines at HEAD); each of twenty
scanners gains a count and one print site; twenty test modules gain pins; `GUARDS.md` gains one
paragraph; `CHANGELOG.md` two entries. Most of the time goes on driving scanners into a scan of
nothing, not on reading.
**Why it earns a review:** this is a silent-failure surface by design. The whole point of the line
is to tell a reader that a green exit covered nothing. Two failure modes manufacture confidence:
a count that is non-zero over a scan that evaluated nothing (the line then *certifies* a vacuous
run it was built to expose), and a `not in scope here` that fires where the guard should have
looked (a public repo or an adopted opt-in treated as out of scope, printed without the warning).
A third mode erodes it: a warning that fires on every routine run trains every reader to skip it.
The doctrine sentence binds every future guard, so a wrong rule here spreads.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09/10 UTC, and the worker it dispatched (per the queue pointer). The author queued this
  pass and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `2a99cef1`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `2a99cef1` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **the intent record
  `115/130` whole, including its two landing notes** (the author's account of what landed and what
  stays open); the delta's `CHANGELOG.md`, `GUARDS.md` and `tools/report.py` hunks through
  `tools/coldsweep.py --commit` (body-free), the coverage call sites by `grep`, and commit subjects
  through `git log`; the opening of `docs/roadmap/115-guardrail-architecture-mike-commissioned/README.md`
  (the commission); the whole unrun brief `2026-11-14-0238-pdlistscan-closed-list-cold.md` (for house
  form) and the lines of four other unrun briefs that mention the coverage line, read to learn
  whether any already covered this subject (none does: each names it a non-goal). It opened **no
  commit message body and no prior verdict**. Its harness also loaded user-level and repo
  instruction files and a memory index, which hold private context this brief does not carry.
  Everything evaluative it formed is in the sibling.

## The acceptance test

The section `115` commission, in the principal's words (2026-08-15, quoted verbatim in
`docs/roadmap/115-guardrail-architecture-mike-commissioned/README.md`): *"research what guardrails
we can and should build in atelier to ensure the best outcomes from atelier itself and the child
repos"*. The item is one answer that research produced; it carries no words of his about this
design. Its own opening is the claim to test: **a guard reports whether its rule fired at all, and
over what, so "clean" and "scanned nothing" stop looking identical.** Its two motivating incidents,
stated in the item's body before any landing note, are the cases the work must catch: a scanner
given an absolute path that matched no repo-relative entry, emptied its own file set and exited 0;
and a check whose skip-list excluded whole stores while printing a clean claim.

The line's wording, the unit per scanner, the choice to keep it informational (no exit change), the
`not_in_scope` form and which scanners use it are **the run's choices, not his**. Whether they are
the right ones is yours to attack.

## What the work is

Two commits on `main`. First confirm your tree has both:

```
git merge-base --is-ancestor aca05c14 HEAD || echo "MISSING aca05c14"
git merge-base --is-ancestor 641f017f HEAD || echo "MISSING 641f017f"
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read each body-free, a few paths at a time:

```
python3 tools/coldsweep.py --root . --commit aca05c14 \
  --path tools/report.py --path tools/test_report.py \
  --path docs/method/GUARDS.md --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit aca05c14 --path tools/<name>.py --path tools/test_<name>.py
python3 tools/coldsweep.py --root . --commit 641f017f \
  --path tools/report.py --path tools/test_report.py \
  --path docs/method/GUARDS.md --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit 641f017f --path tools/<name>.py --path tools/test_<name>.py
```

`aca05c14` touches `datescan`, `wrapscan`, `spellscan`, `conflictscan`, `harvestscan`,
`pointerscan`, `indexscan`, `licenscan`, `reviewscan`, `publishscan`, `sizescan`. `641f017f` touches
`secretscan`, `leakscan`, `linkscan`, `pathscan`, `attribscan`, `blockscan`, `pdlistscan`,
`signscan`, `stampscan`, and again `datescan`, `harvestscan`, `pointerscan`, `indexscan`. Plain `git
show` is barred: it prints the message body before the diff, and reading is atomic (rule 1).
Always pass `--path`; never name a board-store file (the delta's board hunks are the intent record's
landing notes, barred below). Review each delta path at HEAD too. Confirm what has landed since:

```
git log --oneline 641f017f..HEAD -- tools/report.py docs/method/GUARDS.md tools/*scan.py
```

On 2026-11-14 UTC that printed seven commits, none of them about coverage: new scanners
(`sweepscan`, `namescan`, `quotescan`), a commit-message plane, a `leakscan --messages` mode, a
floor five-things report (`ba55be27`), and a doctrine record. Read them only where they meet the
coverage line. Read as context, never as the subject: `GUARDS.md`'s suppression-accounting
requirement the new paragraph sits beside (`report.suppressed_line`), and `tools/floor.py`, which
passes each scanner's output through.

## What the delta claims (extracted, not evaluated)

- **One shared line** from `report.coverage_line`: `  coverage: N <noun> · M <unit>`, known zeros
  printed; when either count is zero it ends `— ⚠️ scanned nothing: no <what> were evaluated, so
  this result covers nothing.` It avoids the word "clean" on purpose.
- **Informational only:** it never changes an exit status.
- **A `--json` twin**, `report.coverage_dict`: `files_opened`, a unit key, `scanned_nothing`, added
  as one new `coverage` key; nothing existing moves. With `in_scope=False`, `scanned_nothing` is
  forced false.
- **A not-in-scope form:** `not_in_scope="<why>"` gives `— not in scope here: <why>` with no glyph.
  Used by `indexscan` (no index declares a mapped directory) and `pdlistscan` (repo not declared
  public).
- **Every tree scanner in the registry prints it** (the second `CHANGELOG.md` entry), on the stream
  it already uses, on the findings path as on the clean one, with units per scanner (lines; lines
  or binaries for `leakscan`; internal links for `linkscan`; path references for `pathscan`; items
  for `harvestscan` and `pointerscan`; declarations for `indexscan`; checks for `reviewscan`;
  never-publish rules over path names for `publishscan`, which opens no file; commits and
  signatures for `signscan`). An exempt file `secretscan` reads only for private keys counts as
  opened.
- **`GUARDS.md`:** every guard states what it actually looked at and says in words when that is
  nothing; a legitimately out-of-scope guard says so rather than looking clean.
- **Probe recorded:** old against new on five child checkouts, 60 runs, exit codes identical. Each
  scanner pinned in its own test module.
- **Stated as not done:** `floor.py`'s own summary, and the label plane (a job or board named for a
  property it does not cover).

## Scope

The widest the work admits: intent, decisions, assumptions, design, doctrine, code, test code and
live behaviour on this machine, including what a child's hook and CI output now looks like. The
lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** each scanner's own rule and findings (only how it counts what it evaluated); the
label plane, which the delta says it does not reach (weigh only whether that is said truthfully);
the scanners added after `641f017f` except as a test of the `GUARDS.md` sentence's reach (A6).

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **A1. No false comfort.** For every scanner, a run that evaluated nothing prints a zero in at
     least one count. In particular, no count is a constant or a mirror of the other count (a rule
     table length, the same number passed twice), and no count is incremented before the rule
     actually runs on the content. (The pointer's first question.)
   - **A2. The incidents are caught.** The two motivating cases re-driven on today's code: a
     scanner handed an absolute path (or a path outside the tree, or a pattern matching nothing)
     and a skip-list that empties the set both print `scanned nothing`, through `tools/floor.py`
     as well as directly.
   - **A3. Not in scope is honest.** `not_in_scope` fires only where the guard truly has nothing to
     check: never for a repo that declares public, never for a declared index, and never because
     the declaration was unreadable. A broken config is a broken scan, not "not in scope". (The
     pointer's second question.)
   - **A4. The warning carries signal.** It does not fire on runs that are routine and correct
     (for example a hook-plane run over a stage with nothing a scanner reads), or where it does,
     that is the intended reading and the output says why. Compare the hook and CI planes.
   - **A5. Informational is safe.** Keeping the line out of the exit status is the right call for
     a floor whose consumers read exit codes; nothing that parses scanner output (floor, tests,
     CI, `--json` consumers) is broken by the extra line or the new key.
   - **A6. The doctrine is met.** `GUARDS.md` says *every guard*: check the registry and the
     scanners added since for any that print no coverage line, and whether the sentence is a rule
     the floor enforces or one that only this delta happened to meet.
   Ask too whether this is the right altitude: a per-scanner count and a shared line, versus one
   coverage check in the floor wrapper over every scanner's output.
2. **Correctness & quality.** Diff both commits; drive scanners against scratch repos you build
   (empty, all-ignored, absolute path, binary-only stage, a findings run) on both planes. Check
   `coverage_line`'s word choice for each unit (`what` derived from the unit string), the
   `--json` key on every scanner, and the stream each line goes to. Record each overclaim against
   the text that makes it: docstrings, `GUARDS.md`, both `CHANGELOG.md` entries.
3. **Completeness / harvest.** Every surface that describes the line says the same thing (V3, V4,
   V5). Tests that would stay green on a broken count: mutate the counting in a scratch copy,
   never the worktree, and see which pin catches it. Is the five-checkout probe reproducible from
   anything recorded?
4. **Security & privacy** — mandatory. The new line prints counts and a reason string; check that
   no reason or noun carries a path, config value or other tree content unescaped into CI logs of
   a public child, and that the `--json` shape cannot be made to carry one. Weigh against OWASP
   ASVS output-encoding and logging items, checked, not recalled. `/security-review` reads the
   session's pending diff, not this delta: aim it only at a scratch clone holding the delta as
   pending changes, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root unless a `cd` is shown, in the foreground, under a load average between 3 and 5 on 12 cores;
its results are held in the sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 on
this machine.

- `cd tools && python3 -m unittest test_report` and the same for each of the twenty scanner test
  modules named above (each between 3 and 50 seconds; one at a time)
- `python3 tools/floor.py --root .; echo $?` (the default plane) and
  `python3 tools/floor.py --plane ci --root .; echo $?`, each with `grep -c "coverage:"` and
  `grep -c "scanned nothing"` over the output (about 30 seconds each)
- An empty scratch repo (`git init` in your scratchpad) scanned directly, for example
  `python3 tools/spellscan.py --root <scratch>; echo $?`
- The recorded probe: five child checkouts, old against new, by exit code. No command is recorded;
  rebuild it, read-only, and say where your counts differ and why.

Run the tool from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** none is needed. Child checkouts on this machine may be **read** for the probe.
Any probe that would write to a real repo, board, config or CI is **NOT RUN**: build the case in
your scratchpad and say which probes you could not build.

- Name no private repo, host, client or private path. This repo is PUBLIC; a child seen in the
  probe is referred to by count or type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0259-coverage-accounting-cold.deferred.md`, the message bodies of
`aca05c14`, `641f017f` and the claim commit `ef00f8b5`, and the intent record
`docs/roadmap/115-guardrail-architecture-mike-commissioned/130-a-guard-reports-whether-its-rule-fired-at-all.md`
beyond its body before the first nested `- [ ]` landing note (the two `🔧` notes are the author's
account of what landed).

The delta's own text carries the author's account of why (docstrings, `CHANGELOG.md` entries); it
is the delta, and reading the delta is never barred. The acceptance test above quotes the
commission, so you need not open other records for it.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1380-rule-4-cold-pass-queued-coverage-accounting.md \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/130-a-guard-reports-whether-its-rule-fired-at-all.md \
  --also-exclude docs/reviews/2026-11-14-0259-coverage-accounting-cold.deferred.md \
  '<pattern>'
```

The intent record is excluded whole from sweeps; read its opening by hand, stopping at the first
nested landing note. `--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions A1–A6 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a commit ledger (`aca05c14`,
`641f017f`: read body-free yes/no, findings by id), findings with stable IDs (prefix `VC`: `VC1`,
`VC2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS /
FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP: act 1 is committed,
unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the commit bodies; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never
revise act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** The coverage line is guard code and the `GUARDS.md` sentence is doctrine
(judged by function, `REVIEW.md` rule 3): the author applies nothing on its own, and neither does
the reviewer. Record all; the findings are the principal's to decide, after a plain-language
account. Counsel per finding is welcome, labelled as counsel and kept beneath it.
