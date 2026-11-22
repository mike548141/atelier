# Cold pass — coverage accounting: a scan of nothing no longer reads as clean

**Board:** `docs/roadmap/160-doctrine-review-owed/1380-rule-4-cold-pass-queued-coverage-accounting.md`
**Status:** PASS RUN, both acts — PASS-WITH-FINDINGS (0 MAJOR · 2 MODERATE · 5 minor ·
2 note), 2026-11-22 UTC, Fable 5.1; the sibling folded in below the verdict by the orchestrator
on 2026-11-22. Brief written 2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as
session `2a99cef1`); run under the principal's drain order of 2026-11-23 NZDT.

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

---

## Verdict (act 1) — PASS-WITH-FINDINGS

**Status:** RAN, act 1 written 2026-11-22 UTC; act 2 (reconcile against the sibling) owed.
**Overall:** PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 4 minor · 2 note (8 findings, `VC1`–`VC8`).

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1, the principal-named review tier, checked at selection. Ran on
  2026-11-22 UTC, 22:44–23:40, on the laptop under Mike's drain order of 2026-11-23 NZDT.
- **Spawn:** started by a headless per-pass orchestrator, session `ea866db1` (Opus 5.5), itself
  started by drain session `eca14b23` (Opus 5.5). Both are off-tier orchestrators under rule 4:
  they hold the context partition and commit the records, form no finding and write no severity.
  Neither wrote this brief or any of the delta. I was not started or instructed by `2a99cef1`,
  `58027096` or `d0ca5d24`, and had no contact with any session during the run.
- **Review tree:** `/Users/mike/worktrees/fable/atelier-160-1380-2242/atelier`, HEAD `585b7d6b`,
  read-only to me except this file; no git command that writes was run. Both commits present
  (`merge-base --is-ancestor` printed nothing).
- **What I read:** this brief; `docs/method/REVIEW.md` 418–530; the two commits body-free through
  `tools/coldsweep.py --commit … --path` for `tools/report.py`, `tools/test_report.py`,
  `docs/method/GUARDS.md`, `CHANGELOG.md`; `git diff --stat` of each commit (no body); at HEAD
  `tools/report.py` 585–670, `GUARDS.md` 575–610, `tools/floor.py` 1340–1350, 2272–2336,
  2950–2975, 3107–3135, `tools/test_floor.py` 3390–3450, and every scanner's coverage call site
  and counter increment (listed in the log). The scanner hunks of each commit were examined at
  their HEAD call sites and by probe, not read line by line as diffs. I did not open the sibling,
  any prior verdict, the session log, the queue pointer, the intent record, `docs/ROADMAP.md`,
  `docs/ROADMAP-DONE.md` or any commit message body. `coldsweep` left the two board-store files
  out of both commit reads by default. `--include-barred` was not used.
- **Work log** (every command, file and line, and what it returned):
  `~/.claude/fable-drain/notes/atelier-160-1380-2242.md`, appended to this file at the fold.
- **Interpreters:** `/usr/bin/python3` is 3.9.6 and the tools use `str | None` in signatures,
  so every tool ran on the 3.14.6 interpreter by its absolute path, from the worktree's `tools/`.

### Method, in order

1. Acceptance test and the two commits, body-free; the helper at HEAD; every call site.
2. Direct probes of all 23 scanners on scratch repos built in the scratchpad: empty, one file,
   every ignore file naming the one file, binary-only stage, findings fixtures, a declared
   index, an indented declaration, a declared-public repo, a malformed floor config, a repo with
   a decision record lacking a review line, and a repo with a docs tree and a code-only stage.
3. The floor on those repos, hook and CI planes, from the repo's own directory; then on the
   worktree, both planes (the re-run obligation).
4. `test_report` and the twenty scanner test modules, one at a time under `nice -n 10`.
5. Mutation of the counting in a scratch copy of `tools/` (26 mutations), each scanner's own
   module run against it.
6. The five-checkout probe rebuilt: old tools (`aca05c14^`) against HEAD on five children, 18
   scanners, by exit code.
7. OWASP ASVS 4.0.3 V7 fetched and checked against the line, not recalled.

Load averages ran 4–26 on 12 cores; every heavy step ran alone, in the foreground, under `nice`.

### Per-lens answers

**Lens 1 — approach and assumptions.** The design is the right altitude for the count: only a
scanner knows what it evaluated, and the mutation probe shows each scanner's own pins catch a
wrong count. It is the wrong altitude for the *reason*: on the hook plane the floor knows why a
scanner's staged subset is empty and the scanner does not, so the alarm fires with no cause on
every code-only commit (`VC1`). The doctrine sentence is a convention this delta met, not a rule
anything enforces, and the three registry scanners added since all miss it (`VC2`).

- **A1 — no false comfort: confirmed, with a letter breach.** Every scanner driven to a scan of
  nothing printed a zero and the warning (empty repo: 18 scanners; empty stage; an ignore file
  that empties the set; an empty signscan range). Counters increment at the top of each per-file
  scan function after the file is read, never before the walk. Two second counts carry no run
  information: reviewscan passes `n_checked` twice and publishscan passes `len(NEVER_PUBLISH)`,
  a constant (69); both still warn when the first count is zero (`VC5`, note).
- **A2 — the incidents are caught: confirmed.** A repo-relative ignore glob plus an absolute path
  to the same file: `0 file(s) opened … ⚠️ scanned nothing`, exit 0, with `1 file(s) by
  .<scanner>ignore` on the suppressed line beside it (spellscan, wrapscan, datescan, linkscan). A
  missing or no-match path argument is a usage error (exit 2) on all eight path-taking scanners,
  so the original "exited 0" shape cannot recur by that route. An ignore list that empties the
  set: the same warning on seven scanners. Through the floor: the empty-stage hook run on the
  worktree printed ten warnings and the staged scanners refuse to run from another repo's cwd.
- **A3 — not in scope is honest: confirmed, with one test gap.** indexscan says not-in-scope only
  when files were opened and none declares; a malformed declaration is exit 2 (`match= is
  required`); a declaring index is in scope (`1 declaration(s) checked`, `in_scope: true`).
  pdlistscan says not-in-scope only when the floor config does not declare public; a missing
  list on a public repo is a finding and `in_scope: true`; a malformed config is exit 2. A
  declaration indented four spaces is unseen (Markdown code-block depth; defensible). The pin
  for pdlistscan's public case would not notice the not-in-scope wording appearing (`VC7`).
- **A4 — the warning carries signal: damaged.** On a repo with a docs tree, a code-only commit on
  the hook plane prints seven `⚠️ scanned nothing … covers nothing` lines (reviewscan, sizescan,
  datescan, wrapscan, spellscan, pathscan, attribscan); the worktree's own empty-stage hook run
  prints ten; the CI plane on the same tree prints none. The output never says why, and the
  routine case is indistinguishable from the incident case except by the suppressed line
  (`VC1`). On real children the CI plane fires only where it is true (two children with no
  post-boundary decision records; one public child with no list).
- **A5 — informational is safe: confirmed.** No exit status moved on 89 of 90 old-against-new
  pairs; the one difference is leakscan rule changes landed since, not coverage. The floor's
  advisory-count parse is anchored to its own line and the floor ran on the worktree with
  advisory counts intact; nothing under `.github/`, `skills/` or `docs/build/` parses scanner
  stdout; every `--json` consumer gets one new key and the twenty test modules pass.
- **A6 — the doctrine is met: damaged.** `GUARDS.md` says *every guard*. sweepscan, namescan and
  quotescan (all in `SCANNERS`) print no coverage line and carry no `coverage` key; namescan and
  quotescan over an empty range print `✓ … clean … on the pushed range`, exit 0, the state the
  delta exists to name. No test, selftest or floor check requires the line (`VC2`). The floor's
  own line, landed since, counts a check that exited 2 as run (`VC3`).

**Lens 2 — correctness and quality.** `coverage_line`'s word choice is right at every call site
(`units_what` is passed wherever `unit.split()[0]` would mis-derive: links, path references,
signatures, checks). The `--json` key is present on every scanner that prints the line, with the
unit key named per scanner (leakscan adds two extra keys, documented in its own tally). The
stream is the scanner's own on every path probed. Overclaims against text: `CHANGELOG.md`
"every tree scanner in the registry" was true at `641f017f` and is false by three today
(`VC2`); `CHANGELOG.md` 283–284 cites "GUARDS.md § coverage", a heading that does not exist
(`VC6`); `floor.py` 2326–2331 promises `ran` is False for an unexecutable check and 2967 sets it
True on invocation (`VC3`); `GUARDS.md` "every guard also states what it actually looked at" is
not met on reviewscan's and publishscan's findings paths in human output (`VC4`). publishscan's
warning says "no files were evaluated" over a scanner that opens no file, and signscan counts a
failed signature as "verified" (`VC8`).

**Lens 3 — completeness and harvest.** `tools/README.md` documents each scanner's `suppressed:`
line and never the `coverage:` line (`VC6`, V3). The recorded probe cannot be rebuilt from the
record: no command, child set or scanner set is written down; my rebuild is in the log (V2).
Mutation: 25 of 26 mutations caught by the scanner's own module, including a counter starting
at 1, an off-by-one, a double count, the helper warning on AND instead of OR, a constant
`scanned_nothing`, indexscan declaring out-of-scope with nothing opened, signscan's verified
count mirroring examined, and pdlistscan never scanning. One survived (`VC7`).

**Lens 4 — security and privacy.** Every string the line prints is a source literal or an
integer: nouns, units, `files_what`, `units_what` and the two `not_in_scope` reasons
(indexscan 292, pdlistscan 316). No path, glob, config value or file content reaches the line
or the dict, so nothing is carried unescaped into a public child's CI log; the dict is ints,
bools and nothing else. Checked against ASVS 4.0.3 V7.1.1, V7.1.2 (no credentials or other
sensitive data in logs) and V7.3.1 (encode to prevent log injection): met by construction,
since no untrusted bytes are interpolated. `/security-review` reads the session's pending diff,
which here is only the sibling's removal; discharged on those grounds, with the manual check
above in its place. No live system was written; child checkouts were read only.

### Standing checklist

- **V1** — one claim stronger than its evidence survives at HEAD: "every tree scanner in the
  registry" (`VC2`); the floor's `ran` docstring (`VC3`); the "§ coverage" citation (`VC6`).
- **V2** — re-run: `test_report` 110 OK; twenty modules OK; floor hook and CI on the worktree
  exit 0 (17 coverage lines each; 10 and 0 warnings); empty scratch repo direct; five-checkout
  probe rebuilt, 89/90 identical, the one difference explained. Ledger below.
- **V3** — the changed rule reached `GUARDS.md`, the helper docstring and `CHANGELOG.md`; it did
  not reach `tools/README.md`, the scanners' reference (`VC6`). No child template or skill
  describes scanner output, so nothing else is stale.
- **V4** — one home: the shape lives in `report.coverage_line`; `GUARDS.md` names the form and
  points at it. Discharged.
- **V5** — contradictions: `CHANGELOG.md` → "GUARDS.md § coverage" reaches no heading (the rule is
  in the paragraph at `GUARDS.md` 593–605, so the rule is reachable, the pointer is not)
  (`VC6`); `floor.py` docstring versus behaviour (`VC3`). The `GUARDS.md` paragraph, the helper
  docstring and both `CHANGELOG.md` entries agree with each other and with the code.
- **V6** — lens 4 above; no finding.
- **V7** — provenance stated in the brief and in this verdict.

### Findings

- **VC1 — MODERATE (design, A4).** The warning fires on every code-only commit on the hook plane
  and never says why. Probe: a scratch repo with a docs tree, roadmap, decision record and
  licence, one `.py` change staged, `floor.py --plane hook` from inside it: 7 of 16 coverage
  lines end `⚠️ scanned nothing … covers nothing` (reviewscan, sizescan, datescan, wrapscan,
  spellscan, pathscan, attribscan); the same tree on the CI plane: 0 of those 7. The worktree's
  own hook run with nothing staged: 10 of 17. The only cue that separates "this commit staged no
  Markdown" from "the scanner emptied its own set" is the `suppressed:` line beside it, which
  the warning does not reference. The brief's third failure mode: a reader who sees seven alarms
  on every routine commit stops reading the eighth. Counsel: on the hook plane a scanner whose
  staged subset is empty by construction has nothing to check, which `GUARDS.md` already names
  as the not-in-scope state; print `not in scope here: no staged file this check reads`, or have
  the floor (which knows the staged set) fold those lines, and keep the ⚠️ for the case where
  the scanner's own filtering emptied a non-empty candidate set.
- **VC2 — MODERATE (doctrine reach, A6).** `GUARDS.md` says every guard states what it looked at;
  nothing enforces it, and the first three registry scanners added after the delta all miss it.
  Probe: `namescan --root <public scratch> --range HEAD..HEAD` and quotescan the same print
  `✓ … clean — … on the pushed range.`, exit 0, no coverage line, no `coverage` key; sweepscan
  prints none on any run; the worktree's CI plane ran both and printed 17 coverage lines for 20
  checks. `grep coverage_line tools/{sweepscan,namescan,quotescan}.py` is empty. No test,
  `--selftest` or floor check asserts the line for each `SCANNERS` entry. Counsel: a floor
  selftest or `test_floor` pin that drives every registry scanner on an empty tree and asserts a
  `coverage:` line (or a declared exemption with its reason), and the three scanners brought
  in, with a commit range as the unit for the two message-plane checks.
- **VC3 — minor (since-landed floor line, `ba55be27`).** `Result.ran` is set True at
  `floor.py` 2967 for any check the floor invoked, including one that exited 2; the docstring at
  2326–2331 says an "unexecutable or scope-refused check is False". Probe: the floor run on a
  scratch repo from another repo's cwd had secretscan, leakscan and conflictscan refuse
  `--staged` (exit 2, the floor's own footer saying "the scan itself could not run") and the
  line still read `12 check(s) run · 19 check(s) listed`. `test_floor.py` 3390–3450 builds
  `ran` by hand and never drives an exit-2 check. A refusal is the case the floor's line was
  built to expose.
- **VC4 — minor (doctrine not met on two findings paths).** reviewscan (649, 658) and
  publishscan (556, 731) print the coverage line only in their clean branches; `--json` carries
  it on both. Probe: a decision record with no review line → reviewscan exit 1, 0 coverage lines;
  a tracked `.env` → publishscan exit 1, 0 coverage lines. attribscan, stampscan, sizescan,
  licenscan, indexscan and the prose scanners print on both. The first `CHANGELOG.md` entry
  discloses "the clean result for the ones that print a tally only then", so the record is
  honest; `GUARDS.md` "every guard also states what it actually looked at" is not.
- **VC5 — note (A1 letter).** reviewscan passes `n_checked` as both counts; publishscan's second
  count is `len(NEVER_PUBLISH)`, 69 on every run. Both warn correctly at zero (probed), so the
  substance of A1 holds, but one of each line's two numbers carries no information about the
  run, and publishscan's warning reads "no files were evaluated" for a scanner that opens no
  file (a `files_what="paths"` would fix the wording).
- **VC6 — minor (V3, V5).** `tools/README.md` documents the `suppressed:` line for several
  scanners (592, 1373, 1381, 1397, 1413, 1522) and never the `coverage:` line, so the scanners'
  reference does not describe an output line every scanner now prints. `CHANGELOG.md` 283–284
  cites "GUARDS.md § coverage"; `GUARDS.md` has no such heading (the rule sits in a paragraph
  under suppression accounting).
- **VC7 — minor (test gap, A3).** A pdlistscan that printed `not in scope here` on a public repo
  while still scanning survives `test_pdlistscan`: the public-case pins (230–238) assert the
  count prefix with `assertIn` and the absence of "scanned nothing", never the absence of the
  not-in-scope tail, and the `in_scope` pins (213, 258) read `--json` only. The second
  motivating question of the pointer has no pin on the human line.
- **VC8 — note (wording).** signscan's unit `signature(s) verified` counts every machine-plane
  commit, including a failed one: an unsigned commit printed `1 commit(s) examined · 1
  signature(s) verified` beside FAIL. "checked" is the honest word. Its `--json` twin keys the
  commit count as `files_opened` because `coverage_dict` has no noun key; the human line says
  commits.

### Commit ledger

- `aca05c14` — read body-free: yes (`coldsweep --commit`, the four core paths; `diff --stat`;
  the scanner call sites and counters at HEAD). Findings formed on it: `VC4`, `VC5`, `VC6` (the
  README gap), `VC1` (design).
- `641f017f` — read body-free: yes (the same four paths; `diff --stat`; call sites at HEAD).
  Findings formed on it: `VC7`, `VC8`, `VC1` (design).
- Landed since (`ba55be27` and later) — subjects only; the floor's coverage code and its pins
  read at HEAD. Findings formed on it: `VC2`, `VC3`, `VC6` (the `§ coverage` citation).

### Re-run ledger

- `cd tools && python3 -m unittest test_report` — Ran 110, OK (13 s).
- The twenty scanner test modules, one at a time — all OK (3–64 s each; `test_linkscan` 89 OK).
- `floor.py --root .` (hook plane) on the worktree — exit 0; `coverage:` ×17; `scanned nothing`
  ×10 (an empty stage).
- `floor.py --plane ci --root .` on the worktree — exit 0; `coverage:` ×17; `scanned nothing` ×0;
  1 skipped (sweepscan, hook-only).
- An empty scratch repo, every scanner direct — 18 warn and exit 0; pdlistscan not-in-scope;
  sweepscan prints no line.
- The five-checkout probe, old against new — 5 children × 18 scanners, 90 pairs, 89 identical
  exit codes; the one difference is leakscan rule changes landed since (ipv4, email, metadata
  kinds), not coverage; harvestscan on one large child hit my 240 s cap on the new tools.

No line was NOT RUN. Scratch repos and outputs were deleted at the end of act 1.

### Follow-up checklist (the principal's to decide; nothing applied)

- [ ] `VC1` — decide the hook-plane form of "nothing staged for this check" (not-in-scope wording,
      or the floor folding the lines); then re-probe a code-only commit for zero alarms.
- [ ] `VC2` — a pin that every `SCANNERS` entry prints a `coverage:` line on an empty tree;
      sweepscan, namescan, quotescan brought in.
- [ ] `VC3` — `ran=False` (or a third state) for a check that exited 2; a pin that drives one.
- [ ] `VC4` — reviewscan and publishscan print the line on the findings path too.
- [ ] `VC5`, `VC8` — wording: `files_what="paths"` for publishscan; `checked` for signscan; a
      noun key in `coverage_dict` or a documented exception.
- [ ] `VC6` — one paragraph in `tools/README.md` on the `coverage:` line; fix the `§ coverage`
      citation in `CHANGELOG.md` or give `GUARDS.md` the heading.
- [ ] `VC7` — a pdlistscan pin asserting the public-case human line carries no not-in-scope tail.
- [ ] Record the five-checkout probe's command, child count and scanner set in the item so the
      next pass can re-drive it exactly.

Act 2 (`### Reconcile`) follows once this act is committed and the sibling is released.

### Reconcile (act 2, 2026-11-22 UTC)

Opened after act 1 was committed (`b514a34f`): the held sibling (the brief-writer's re-run table
and five leads), the message bodies of `aca05c14`, `641f017f` and `ef00f8b5`, the queue pointer,
the intent record `115/130` whole with its three landing notes, and the prior verdicts that
mention the line. Act-1 text above is unrevised; corrections are stated here.

**Against the sibling's leads.**

- *A1 lead (publishscan constant, reviewscan mirror)* → `VC5` found the same by reading and
  probed both to zero; the sibling's open question (non-zero over nothing) is answered no.
- *A4 lead (ten warnings on an empty stage; whether a real hook run looks like that)* → `VC1`
  answers it: a real code-only commit on a tree with docs prints seven. The two prior verdicts
  that met the empty-stage reading (`2026-11-09-0126-ladder-floor-cold.md` 717,
  `2026-11-09-0126-git-resolved-staged-scope-cold.md` 407) recorded it as an observation, not a
  finding; this pass is the first to weigh it against the item's third failure mode.
- *A2 / wording lead (the head line still says "clean")* → not weighed in act 1. Formed here as
  `VC9` below.
- *A6 lead (three post-delta scanners; 16 lines against 17 rows)* → `VC2`. The count has since
  moved to 17 lines for 20 checks on the CI plane (licenscan joined the registry); the three
  scanners still print none.
- *The probe has no recorded command* → act 1 said the same (V2) and rebuilt it; the follow-up
  checklist already asks for the command to be recorded.
- The sibling's re-run table of 2026-11-14 matches mine within normal variance; `test_leakscan`
  grew from 422 to 469 tests and `test_sizescan` from 117 to 121 in the week between.

**Against the author's account.**

- `aca05c14`'s body says the first probe's only scanned-nothing result was indexscan "in every
  child"; `641f017f` then made that the not-in-scope form. My rebuild on five children shows
  reviewscan warning on two (no post-boundary decision records) and pdlistscan on one (public,
  list absent). Either the author's five children differ from mine or those states arose since;
  neither reading changes a finding.
- The bodies say 55 runs then 60 runs; `CHANGELOG.md` and the landing note carry 60. Consistent
  with the scanner sets of each slice; no contradiction.
- The 2026-11-16 landing note (the floor's own line, `ba55be27`) says "a check counts as run only
  when floor invoked it" and `tools/README.md` 2765–2777 says the same, adding that one "refused
  before it started is listed and not run". That is the design `VC3` describes: a check floor
  invoked that then refused itself (exit 2) counts as run. `VC3` stands as minor; the author's
  account shows the choice was deliberate, and the `floor.py` docstring's "unexecutable … is
  False" is the overclaim, not the code.
- **Correction to `VC6`.** Act 1 said `tools/README.md` "never mentions the coverage line". My
  act-1 grep stopped at ten hits (`head`), and the released reads show the README documents the
  floor's own line at 2765–2777 ("in the shape every tree scanner prints"). What stands: no
  README section describes the per-scanner `coverage:` line beside the per-scanner
  `suppressed:` lines it does document, and the "GUARDS.md § coverage" citation still reaches no
  heading. `VC6` stays minor with that narrower wording.
- The queue pointer's title still says "eleven scanners" although the brief and both commits
  cover twenty; a record nit for the orchestrator's fold, not a finding on the work.

**Finding formed at reconcile.**

- **VC9 — minor (formed at reconcile, from the sibling's A2 lead).** On a scan of nothing the
  scanner's first line still reads `✓ <name> clean — …` and the floor board still renders ✅;
  only the third line differs. Evidence from act 1: every empty-repo run opened `✓ … clean`
  (18 scanners), and the worktree's empty-stage hook run showed ✅ against all 19 checks while
  ten of their lines said `covers nothing`. The floor already has a state for "told the check
  ran, not what it checked" (`Result.partial`, `floor.py` 2278–2283, rendered 🟡); a check whose
  own line says it covered nothing is that state, and the board does not show it. Counsel: let
  the floor read `scanned_nothing` from the `--json` twin, or have `report.clean_head` take the
  coverage into its wording, so the glyph and the first line agree with the third.

**Overall line restated:** PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 5 minor · 2 note
(`VC1`–`VC9`; `VC9` formed at reconcile; `VC6` narrowed as stated above).

- [ ] `VC9` — the clean head line and the floor glyph on a scan of nothing (added to the
      follow-up checklist above; the principal's to decide).

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (`b514a34f`); folded here
verbatim (headings demoted two levels to sit under this one) and the sibling file removed, per
the brief. The orchestrator (headless Claude Opus 5.5 session `ea866db1`, started by drain session
`eca14b23`) held the partition, formed no finding and wrote no severity.*

### Deferred — coverage accounting cold pass (brief-writer's held-back material)

**Board:** `docs/roadmap/160-doctrine-review-owed/1380-rule-4-cold-pass-queued-coverage-accounting.md`
**Status:** sibling of the unrun brief `2026-11-14-0259-coverage-accounting-cold.md`, written
2026-11-14 UTC by the brief-writer (session `2a99cef1`). Open only after phase-1 findings are
committed; fold in below the reconcile, then delete.

The brief-writer forms no finding and writes no severity. What follows is what it saw while
grounding the brief, held back so it cannot steer phase 1. Weigh each as a lead, not a result.

#### Re-run results, 2026-11-14 UTC (load 3–5 on 12 cores, Python 3.14.6)

All exit 0, one at a time from `tools/`:

| module | tests | seconds |
|---|---|---|
| `test_report` | 110 | 12 |
| `test_datescan` | 100 | 13 |
| `test_wrapscan` | 71 | 16 |
| `test_spellscan` | 90 | 22 |
| `test_conflictscan` | 88 | 16 |
| `test_harvestscan` | 54 | 23 |
| `test_pointerscan` | 52 | 6 |
| `test_indexscan` | 57 | 12 |
| `test_licenscan` | 79 | 3 |
| `test_reviewscan` | 70 | 10 |
| `test_publishscan` | 60 | 28 |
| `test_sizescan` | 117 | 14 |
| `test_secretscan` | 272 | 20 |
| `test_leakscan` | 422 | 43 |
| `test_linkscan` | 89 | 6 |
| `test_pathscan` | 172 | 14 |
| `test_attribscan` | 36 | 7 |
| `test_blockscan` | 58 | 36 |
| `test_pdlistscan` | 24 | 5 |
| `test_signscan` | 18 | 49 |
| `test_stampscan` | 125 | 11 |

- `tools/floor.py --root .` (default plane, clean tree, nothing staged): exit 0, 29 s, 16
  `coverage:` lines, **10 of them `scanned nothing`**.
- `tools/floor.py --plane ci --root .`: exit 0, 33 s, 16 `coverage:` lines, 0 `scanned nothing`.
- Empty scratch repo, `spellscan --root <scratch>`: exit 0; output opens `✓ spellscan clean —
  no US spellings found.` and its third line is the `scanned nothing` warning.

#### Leads the brief-writer noticed (not findings)

- **A1:** `publishscan`'s unit count is `len(NEVER_PUBLISH)`, a constant (69 at HEAD), so only its
  path count can reach zero. `reviewscan` passes `n_checked` as both counts. Whether either can
  report non-zero over nothing evaluated is the reviewer's to probe.
- **A4:** the default-plane floor run above printed the warning ten times on a clean tree with
  nothing staged. Whether a real hook run ever looks like that, and whether ten warnings there
  are signal or noise, is open.
- **A2 / wording:** the empty-repo run still leads with `✓ … clean`. The warning avoids "clean",
  but the scanner's own first line does not; whether the pair reads as the item's opening claim
  wants is the reviewer's call.
- **A6:** `sweepscan`, `namescan` and `quotescan` (added after `641f017f`) do not call
  `report.coverage_line` at HEAD (by `grep`). `floor.py --list --root .` shows 19 rows (`board`
  and `sweepscan` among them; `blockscan`, `signscan` and `stampscan` are not rows there), while
  both floor runs printed 16 coverage lines, one fewer than the 17 rows left after `board` and
  `sweepscan`. Which rows print none, and whether the `GUARDS.md` "every guard" sentence binds
  them, is open.
- The five-checkout probe is recorded only as counts in `CHANGELOG.md`; no command was found.

#### Nothing else is deferred

The brief-writer read no commit body and no prior verdict, so it holds no author account beyond
what the brief's exposure line names.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Appended by the orchestrator at the fold (session `ea866db1`), verbatim, headings demoted two
levels to sit under this one; the working file was then deleted.*

### Review log — atelier board 160/1380, coverage accounting cold pass

Reviewer: Fable 5.1 (tier checked at selection). Orchestrator: session ea866db1 (Opus 5.5,
off-tier, forms no finding), started by drain session eca14b23 (Opus 5.5). Worktree:
`/Users/mike/worktrees/fable/atelier-160-1380-2242/atelier`. Brief:
`docs/reviews/2026-11-14-0259-coverage-accounting-cold.md`. Commands, files, evidence only.
Act 1 entries are written before the sibling `.deferred.md` is opened.

#### Act 1

- 2026-11-22T22:44Z `date -u`; `uptime` load 13.86 on 12 cores (several passes run at once).
  `git status --short` shows only one deletion, the sibling
  `docs/reviews/2026-11-14-0259-coverage-accounting-cold.deferred.md` (the partition, left
  alone). HEAD 585b7d6b (claim commit).
- Read the brief whole (lines 1-289). Read `docs/method/REVIEW.md` lines 418-530 (standing
  checklist V1-V7, lifecycle, open-record ruling).
- `git merge-base --is-ancestor aca05c14 HEAD` and `641f017f HEAD`: both present, nothing printed.
- `git log --oneline 641f017f..HEAD -- tools/report.py docs/method/GUARDS.md tools/*scan.py`:
  20 commits now (brief saw 7 on 2026-11-14). Subjects only read. None names coverage.
- `git diff --stat aca05c14^ aca05c14` and `641f017f^ 641f017f`: 28 and 32 paths; no message body
  printed by `diff --stat`. Board-store paths (`docs/ROADMAP.md`, the `115/130` item) not opened.
- `tools/coldsweep.py --commit aca05c14 --path tools/report.py --path tools/test_report.py --path
  docs/method/GUARDS.md --path CHANGELOG.md` and the same for `641f017f`: read body-free. Both
  `coverage_line`/`coverage_dict` versions, the GUARDS.md paragraph and both CHANGELOG entries read.
- Read at HEAD: `tools/report.py` 585-670 (`coverage_line`, `coverage_dict`);
  `docs/method/GUARDS.md` 575-610 (the paragraph plus the treeline paragraph after it).
- `grep -n "coverage_line\|coverage_dict" tools/*.py` (non-test): 23 scanners call it plus
  `tools/floor.py` 3107-3135 (`coverage_counts`/`coverage_summary`, landed since the delta in
  `ba55be27`). Not calling it: `sweepscan`, `namescan`, `quotescan` (all three in the floor
  registry `SCANNERS`, `tools/floor.py` 1166-1230) and `stashscan` (not a floor check).
  Registry membership by `grep -c '^        "<name>",' tools/floor.py`: blockscan, signscan,
  stampscan, stashscan 0; sweepscan, namescan, quotescan, licenscan 1.
- Read `tools/reviewscan.py` 560-665: `n_checked = len(records) + len(briefs)`, passed twice
  (`coverage_line(n_checked, n_checked, unit="check(s) run")`); the coverage line is printed on the
  two clean paths only (lines 649, 658), never when `failures` or `misplaced` is non-empty.
- Read `tools/publishscan.py` 408-420: second count is `len(NEVER_PUBLISH)`, a constant.
- Read every call site's unit/noun arguments (linkscan 126-131, pathscan 520-525, harvestscan
  741-771, pointerscan 881-932, indexscan 280-300, leakscan 530-545, signscan 200-222, pdlistscan
  295-320, sizescan 1060-1072). Every noun, unit, `files_what`, `units_what` and `not_in_scope`
  string is a literal in source; none interpolates a path or config value.
- Read `tools/indexscan.py` 454-478 (`discover`), 690-712, 755-785; `DECL_START_RX` line 201
  (`^\s{0,3}<!--\s*indexscan:maps\b`); a malformed declaration raises `ConfigError` (exit 2).
  `out_of_scope` = `files_opened > 0 and declarations == 0`.
- Read `tools/pdlistscan.py` 155-175, 205-230, 270-320: a missing `.atelier-floor.json` is "not
  public" (out of scope); an unreadable or malformed one raises `ConfigError`.
- `grep -n -B3 "files_opened += 1|..."` over the prose scanners: increments sit at the top of each
  per-file scan function (after the file is read), e.g. datescan 635, spellscan 597, wrapscan 497,
  conflictscan 429/589, secretscan 1428/1778/1797/2043, leakscan 3089/3325/4023, linkscan 822,
  pathscan 1243, sizescan 932, stampscan 988, licenscan 539.
- Mirror sites: `grep -rn -i "coverage[:_ ]|coverage line|scanned nothing"` over md, yml, json, sh,
  py and js files outside the scanners and barred records: only `CHANGELOG.md` and `GUARDS.md`
  describe the line.
  `tools/README.md` documents the `suppressed:` line for several scanners (592, 1373, 1381, 1397,
  1413, 1522) and never mentions the coverage line. `tools/test_floor.py` 3393-3448 pins the
  floor's own line.
- `CHANGELOG.md` 281-284 (treeline entry, `450/010`) says "GUARDS.md § coverage gains the
  one-sentence rule"; GUARDS.md has no heading named coverage, the sentence sits in the paragraph
  at 603-605.
- Interpreters: `/usr/bin/python3` is 3.9.6; `python3` on PATH is
  `/Library/Frameworks/Python.framework/Versions/3.14/bin/python3` 3.14.6. The tools use
  `str | None` in signatures, so they run on 3.14 by that absolute path; my own scripts run on
  `/usr/bin/python3`.
- Built scratch repos in the scratchpad (`build_scratch.sh`): r_empty, r_onefile, r_allignored
  (every `.<scanner>ignore` names the one file), r_binonly (one staged binary), r_findings
  (conflict marker, >100-col line, bad dates, dangling link), r_indexdecl, r_indexindent (the
  declaration indented four spaces), r_public, r_publicbroken (malformed floor config). Old tools
  extracted with `git archive aca05c14^ tools` (40 scanner files), HEAD tools copied for mutation
  (48). 23 children under the local checkout root carry `.atelier-floor.json` (count only).
- 2026-11-22T22:50Z `uptime`: load 25.67 on 12 cores. Probes run one at a time under `nice -n 10`.

##### Probes (direct, scratch repos; `probe_direct.py` runs each scanner with and without `--json`)
- r_empty: all 18 scanners that take `--root` alone print `coverage:` with the ⚠️ warning and
  exit 0; `--json` carries a `coverage` key with `scanned_nothing: true`. pdlistscan prints `not in
  scope
  here` (no floor config). sweepscan prints no coverage line, no `coverage` key. namescan,
  quotescan, licenscan, blockscan, signscan need their own arguments (exit 2 here; driven below).
- r_onefile (one 3-line README): prose scanners print `1 file(s) opened · 3 line(s) read`;
  linkscan `1 Markdown file(s) opened · 0 internal link(s) checked — ⚠️` (no links, a true zero);
  pathscan the same for path references; sizescan `1 file(s) opened · 0 line(s) read — ⚠️`
  (README is a candidate opened for its header; `COLD_CHECKBOX_FILES = {"ROADMAP.md"}`, sizescan
  301); indexscan `not in scope here: no index declares a mapped directory.` with
  `in_scope: false`; reviewscan/harvestscan/pointerscan 0/0 ⚠️.
- r_allignored, reasoned globs (`README.md  # probe…` in every `.<scanner>ignore`): datescan,
  wrapscan, spellscan, linkscan, pathscan, indexscan, stampscan print `0 file(s) opened` ⚠️, exit 0,
  `suppressed: … 1 file(s) by .<scanner>ignore` beside it (incident 2 caught). secretscan,
  leakscan, conflictscan read the ignore files themselves (14-15 files), no warning (correct).
  Unreasoned globs exit 2 (`allowmarker.load_ignore_globs`, 504-520), a config error.
- Incident 1 (absolute path): `<scanner> --root r_onefile <abs path outside root>` scans that file
  (`1 file(s) opened`); a missing or no-match path is `path does not exist`, exit 2 (eight
  scanners). `--root r_allignored <abs path of the ignored README>`: spellscan, wrapscan,
  datescan, linkscan print `0 file(s) opened` ⚠️ with `1 file(s) by .<scanner>ignore`, exit 0.
- r_findings (conflict marker, long line, bad dates, dangling link): conflictscan, linkscan,
  datescan, wrapscan, pathscan exit 1 and print the coverage line on the findings path.
- r_findings2 (`.env`, US spelling, IPv4, synthetic AKIA key): spellscan, leakscan, secretscan
  exit 1 with the line; **publishscan exits 1 with 0 coverage lines**. licenscan on r_empty
  (`✗ … unrecognised`, exit 1) prints the line. By code: publishscan 540-560 and 718-735 print
  `_coverage_line` only in the `else` (clean) branch; reviewscan 649/658 the same (both clean
  paths, never when `failures` or `misplaced`); attribscan 492, stampscan `_coverage_tail`
  (1080, 1105) and sizescan 1069 print on both.
- r_review (one post-boundary ADR with no review line): reviewscan exit 1, human output has 0
  `coverage` lines, `--json` has the key.
- indexscan: r_indexdecl with `dir=` only → `match= is required`, exit 2; with `match=*.md` →
  `2 Markdown file(s) opened · 1 declaration(s) checked`, `in_scope: true` (a missing-dir
  finding, my fixture's path). r_indexindent (declaration indented four spaces) → `not in scope
  here`, `in_scope: false`: the indented comment is not matched by `DECL_START_RX` (0-3 spaces).
- pdlistscan: r_public (declares public, no list file) → `no-list` warning finding and
  `0 tracked file(s) opened · 0 line(s) read — ⚠️`, `in_scope: true`; r_publicbroken (malformed
  JSON) → `cannot read …/.atelier-floor.json`, exit 2 (a broken config is a broken scan).
- signscan `--repo r_onefile --boundary HEAD` (empty range): `0 commit(s) examined · 0
  signature(s) verified — ⚠️ scanned nothing: no commits were evaluated`, exit 0; `--json` key is
  `files_opened: 0` (the dict has no noun key). `--rev HEAD` on an unsigned commit: FAIL, exit 1,
  `1 commit(s) examined · 1 signature(s) verified`.
- namescan and quotescan `--root r_public --range HEAD..HEAD` (an empty range, repo declared
  public): `✓ namescan clean — no private name in a branch or title on the pushed range.`, exit 0,
  no coverage line; quotescan the same. blockscan `--root <worktree>`: `7 file(s) opened · 4541
  line(s) read`, `coverage` key present.
- floor on scratch repos, run from the worktree cwd: secretscan/leakscan/conflictscan refuse
  `--staged` when cwd is another repo (exit 2) and the floor's line still says `12 check(s) run ·
  19 check(s) listed` (`Result.ran=True` is set at floor.py 2967 for any invoked check; the
  docstring at 2326-2331 says an unexecutable or scope-refused check is False).
- floor hook plane from inside r_pyonly (one `.py` staged, no docs tree): 3 ⚠️ (linkscan 0
  links, reviewscan 0 records, sizescan 0 lines), 2 not-in-scope, 7 skipped `(no docs tree)`.
  r_binonly: leakscan blocks the binary; secretscan `0 file(s) opened` ⚠️ (reads no binary).
- floor hook plane from inside r_docsrepo (docs tree, roadmap, ADR, LICENSE; a code-only
  change staged): **7 ⚠️ scanned-nothing lines** (reviewscan, sizescan, datescan, wrapscan,
  spellscan, pathscan, attribscan), 2 not-in-scope, exit 1 (board check; unrelated). CI plane on
  the same repo: 2 ⚠️ (pathscan, attribscan first-commit).
- Re-run obligation, floor on the worktree (cwd the worktree, `--root .`): default (hook) plane
  2026-11-22T23:01Z-23:02Z, exit 0, 17 `coverage:` lines, **10 `scanned nothing`** (nothing is
  staged: secretscan, leakscan, conflictscan, reviewscan, publishscan, sizescan, datescan,
  wrapscan, spellscan, attribscan), 0 not-in-scope, floor line `19 check(s) run · 19 check(s)
  listed`. CI plane 23:03Z-23:04Z, exit 0, 17 `coverage:` lines, 0 `scanned nothing`, 0
  not-in-scope, 1 skipped (sweepscan), floor line `20 check(s) run · 21 check(s) listed`;
  namescan and quotescan ran and printed no coverage line. Outputs kept in the scratchpad only.
- Read `tools/test_floor.py` 3390-3450: the floor's pins build `Result(..., ran=r)` by hand and
  the end-to-end pin checks `ran` adds up; no pin drives a check to exit 2 and asserts `ran`.

##### Re-run ledger and tests
- `cd tools && python3 -m unittest test_report`: Ran 110, OK (13 s), 2026-11-22T23:05Z.
- The twenty scanner test modules one at a time under `nice -n 10`, 23:05Z-23:15Z: all OK
  (datescan, wrapscan, spellscan, conflictscan, harvestscan 54, pointerscan 53, indexscan 57,
  licenscan, reviewscan 70, publishscan 60, sizescan, secretscan, leakscan, linkscan 89, pathscan,
  attribscan 36, blockscan 58, pdlistscan 24, signscan, stampscan). Load 7-9 throughout.
- OWASP ASVS 4.0.3 V7 fetched from the ASVS repository (raw `0x15-V7-Error-Logging.md`): V7.1.1
  (no credentials or payment details in logs), V7.1.2 (no other sensitive data), V7.3.1 (encode
  data to prevent log injection). Checked against the line: every string it prints is a literal
  in source or an integer; `not_in_scope` reasons are the two literals in indexscan 292 and
  pdlistscan 316; no path, glob, config value or file content reaches the line or the dict.
- Mutation probe on the scratch copy of tools (`mutate.py`, `mutate2.py`; the worktree untouched):
  26 mutations, 25 CAUGHT by the scanner's own module (counter starting at 1, off-by-one, double
  count, helper warning on AND instead of OR, json `scanned_nothing` constant, indexscan
  out-of-scope with no file opened, signscan verified mirroring examined, pdlistscan never
  scanning). 1 SURVIVED: pdlistscan printing `not in scope here` on a public repo while still
  scanning (`test_pdlistscan.py` 230-232 asserts the count prefix with `assertIn` and the absence
  of "scanned nothing", never the absence of "not in scope here"; the `--json` `in_scope` pin at
  213/258 does not cover the human line).

##### The five-checkout probe (`probe5.py`, 23:26Z-23:38Z, read-only, cwd each child)
- The first five floor-adopting children by sorted path; 18 scanners (the 20 minus signscan and
  blockscan, which need a trust list or a map); old tools at `aca05c14^` against HEAD's copy; 180
  runs, 90 pairs, 89 identical exit codes. The one difference: child 4, leakscan, old 1, new 0;
  the old run's findings were ipv4 ×12, email ×2, metadata ×1 by rule kind, rules that later
  commits changed (`af74cf91`, `5c2fc7e6`, `51720d97`), not a coverage effect. harvestscan on
  child 4 hit my 240 s cap on the new tools (its known quadratic walk), so that pair has no
  coverage line to read. New-tool runs with no coverage line: none other.
- `scanned nothing` on real children: reviewscan on children 3 and 5 (no post-boundary decision
  records), pdlistscan on child 5 (declared public, list absent). `not in scope here`: pdlistscan
  on children 1-3 (not declared public), indexscan on child 5. Children 1-3 ran in about 9 s each
  per tool set; children 4 and 5 took about 700 s each (large trees, 36 runs each).
- The brief's recorded probe ("five child checkouts, 60 runs, exit codes identical") records no
  command, no child set and no scanner set, so it cannot be re-driven exactly; 60 is consistent
  with 12 scanners × 5 children under the first commit's set. My 90-pair rebuild differs by one
  pair, explained above.

##### Closing act 1
- Verdict appended to the brief below a `---` divider; the header Status line updated to RAN,
  act 1, PASS-WITH-FINDINGS (0 MAJOR · 2 MODERATE · 4 minor · 2 note), act 2 owed.
- On the brief file from the worktree: `datescan`, `wrapscan`, `spellscan`, `linkscan` all exit 0;
  `leakscan` and `secretscan` over the brief and this log exit 0 (2 files, 708 lines). The two
  ledger tables were rewritten as lists to keep every line within 100 characters.
- Scratch repos, the old/new tool copies and every captured output deleted from the scratchpad;
  only my probe scripts remain there. No live system was written; no git command that writes ran.
- 2026-11-22T23:45Z act 1 saved. The sibling and the barred records stay unopened until act 2.

#### Act 2 (after the orchestrator's release, act 1 committed as b514a34f)

- 2026-11-22T23:5xZ `git log -1`: b514a34f "reviews 160/1380: act 1 of the Fable cold pass on
  coverage accounting". `git status --short`: only the sibling deletion.
- Read the held sibling at the one path the orchestrator gave (under `~/.claude/fable-held/`),
  whole: the brief-writer's 2026-11-14 re-run table (21 modules, all OK), two floor runs (16
  coverage lines each, 10 and 0 `scanned nothing`), the spellscan empty-repo run, and five leads
  (A1 publishscan constant and reviewscan mirror; A4 ten warnings on an empty stage; A2 the head
  line still says "clean"; A6 the three post-delta scanners and 16 lines against 17 rows; no
  recorded probe command).
- Read the commit bodies of `aca05c14`, `641f017f`, `ef00f8b5` (`git log -1 --format=%B`):
  `aca05c14` records 55 runs on five children with indexscan the only scanned-nothing result;
  `641f017f` records 60 runs, "one extra line each (indexscan one line shorter)", blockscan
  probed on this repo only, floor left to another lane. `ef00f8b5` is the claim, no account.
- Read the queue pointer `160/1380` whole (title still says "eleven scanners"; the claim note of
  2026-11-22T22:42Z names this pass's orchestrator and reviewer) and the intent record `115/130`
  whole, including its three landing notes (2026-11-09, 2026-11-10, 2026-11-16). The third
  landing note says the floor's own line is "described in `tools/README.md`" and "a check counts
  as run only when floor invoked it".
- `grep -n "coverage:\|check(s) run\|coverage line\|coverage_line" tools/README.md`: lines 2560,
  2569, 2765-2777. `tools/README.md` 2765-2777 is a section on the floor's own `coverage:` line:
  "A check counts as run only when floor invoked it; one disabled, skipped …, missing, or refused
  before it started is listed and not run". No README section describes the per-scanner line;
  `grep -n "scanned nothing\|file(s) opened"`: only 2772 (the floor section). **Correction to
  act 1:** my act-1 README grep piped through `head` and stopped at ten hits, so VC6's "never
  mentions the coverage line" is too strong; the per-scanner claim stands, the floor's line is
  documented. Recorded in the reconcile, act-1 text unrevised.
- `grep -n "coverage_line\|scanned nothing" docs/reviews/*.md` (prior verdicts, released):
  `2026-11-09-0126-ladder-floor-cold.md` 717 and `2026-11-09-0126-git-resolved-staged-scope-cold.md`
  407 both record "nothing staged so the staged scanners report scanned nothing" as an observed
  reading, neither as a finding; `2026-07-10-linkscan.md` L1 is the typo'd-path incident, fixed as
  a usage error (the exit-2 behaviour I probed). No prior verdict reviewed the coverage line.
- `### Reconcile` appended beneath the act-1 verdict: per-lead and per-account notes, the `VC6`
  correction, `VC9` formed at reconcile (clean head line and ✅ glyph on a scan of nothing), the
  overall line restated (0 MAJOR · 2 MODERATE · 5 minor · 2 note). Header Status updated to acts
  1 and 2. Nothing folded, nothing deleted; the sibling stays where it is for the orchestrator.
- On the brief alone from the worktree: datescan, wrapscan, spellscan, linkscan exit 0 (no
  sibling-link hit: the brief names the sibling in backticks, not as a link); leakscan and
  secretscan over the brief and this log exit 0. This log keeps every line within 100 characters
  (the width the brief passes at); wrapscan's 85-column default flags it as a file outside
  `docs/reviews`, which is where the fold puts it.
- 2026-11-22T23:52Z act 2 saved. No git write ran; `git status --short` shows the sibling
  deletion and the modified brief only.
