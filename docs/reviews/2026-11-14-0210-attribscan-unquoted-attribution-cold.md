# Cold pass — `attribscan`, an attribution to the principal carries his words

**Board:** `docs/roadmap/160-doctrine-review-owed/1330-rule-4-cold-pass-queued-attribscan.md`
**Status:** ACT 2 SAVED 2026-11-15 UTC — FAIL, 1 MAJOR · 5 MODERATE · 6 minor · 4 note, by a Fable
5.1 cold reviewer under a headless Opus 5.5 orchestrator (drain session `21a271a5`). Act 1 committed
unrevised as `f4998896`; the reconcile below was written after the sibling and the barred records
were opened; the orchestrator folded the sibling below the verdict on 2026-11-15. The findings are the principal's to
decide (rule 3). Brief written 2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as
session `a18861ae`).

**Pass type:** code cold pass, first of its kind, per `docs/method/REVIEW.md` rule 4: the first
scanner that reads records for a claim of the principal's authority.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** medium: one landing commit of about 950 added lines (516 the tool, 322 its
tests, 24 the floor registry entry, 23 a floor contract test, 54 the README section, 16 the
changelog entry), and one later hunk of about 70 lines that threads a coverage count through it.
**Why it earns a review:** it is guard code registered in the floor for every child repo, and on
2027-02-08 it starts to block commits by itself, with no edit, in every repo whose CI floats on
atelier's floor. Two failure modes matter. The worse is a **false clear**: a fabricated "he ruled"
that passes because something in a three-line window looks like evidence, so the record reads as
checked and later sessions defend it against him, the exact incident the check exists for. The
second is **noise on the flip date**: a guard that blocks ordinary prose, or a routine record
move, trains every session to reach for the allow marker, and then it guards nothing.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `a18861ae`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `a18861ae` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; **the queue pointer whole**; **the intent
  records `320/100` and `320/810` whole**, including the author's landing notes on both and a later
  measurement note under `320/100`; the delta through `tools/coldsweep.py --commit` (no commit body
  was printed: the one `git show` it ran printed the hash, date and subject only);
  `tools/attribscan.py` and the test names at HEAD; floor and README lines naming the scanner;
  commit subjects through `git log`; the brief
  `2026-11-14-0158-cclive-machine-wide-live-work-cold.md`, the first part of its sibling, and that
  brief-writer's session record and log line (read for house form). It opened **no prior verdict**.
  Its harness also loaded user-level and repo instruction files and a memory index, which hold
  private context this brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words that commissioned the build, 2026-11-09, quoted on `320/810` (asked which of
six candidate checks to build): *"all six, warnings at first and then move to blocking action. With
a staggered turn on of each so they dont all hit at once"*. One of the six is this one, "ruled" with
no quote. Those words fix three things only: the check is built, it warns first, and it then blocks
on a turn-on date staggered from the other five. **The date itself, 2027-02-08, is the run's
choice, not his**, and the delta says so.

The design follows the item that proposed the check (`320/100`, filed from a child repo by class
only, 2026-08-25), which offered this direction and did not prescribe it:

> the machine-decidable half is not the truth of the attribution but its **form** — flag
> `ruled|the owner's|his instruction|he directed` in a record where no adjacent quotation or dated
> transcript reference appears, and require either a quote, a citation, or a demotion to *"an
> agent's decision"*.

The incident behind it, as class: records in a child said *ruled 2026-08-23*, *the owner's ruling*,
*his instruction*, with no quote; some of those were an agent's own decision filed under his name,
and later sessions argued for them against him. No ruling of his fixes the design beyond the words
above. Judge the work against the offer and against its own claims below; whether a form check is
the right answer to an authorship defect is yours to attack.

## What the work is

Two commits on `main`. First confirm your tree has them:

```
for c in 20e7fc35 641f017f; do git merge-base --is-ancestor $c HEAD || echo "MISSING $c"; done
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read each commit body-free:

```
python3 tools/coldsweep.py --root . --commit 20e7fc35 \
  --path tools/attribscan.py --path tools/test_attribscan.py --path tools/floor.py \
  --path tools/test_floor.py --path tools/README.md --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit 641f017f \
  --path tools/attribscan.py --path tools/test_attribscan.py
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Always pass `--path`: `641f017f` also changes thirteen other scanners and a board item,
which are not this pass's subject. Review `tools/attribscan.py` and `tools/test_attribscan.py` at
HEAD too, and read the shared helpers it calls (`tools/report.py`, `tools/allowmarker.py`,
`tools/filewalk.py`) as far as attribscan depends on them. On 2026-11-14 UTC no commit after
`641f017f` had touched either attribscan file. Confirm what has landed since, and read anything new
the same way:

```
git log --oneline 641f017f..HEAD -- tools/attribscan.py tools/test_attribscan.py
git log --oneline 20e7fc35..HEAD -- tools/floor.py | head -20
```

`tools/floor.py` changed after the landing for other reasons; the attribscan registry entry is in
scope, and so is any later change to how the floor runs an entry with `advisory` or
`advisory_count` set.

## What the delta claims (extracted, not evaluated)

- **It reads the form, never the truth.** An attribution with no quotation, citation or demotion
  nearby is reported; whether the attribution is true, or a quotation is his, is out of reach.
- **What counts as an attribution:** `ruled` (never `overruled`, `ruled out`, `ruled it out`),
  `his ruling|instruction|directive`, `the owner's ...`, `the principal's ...`, `he directed`,
  `he instructed`, and, case-sensitively, a capitalised name's `ruling` or `directive`.
- **What counts as evidence:** in the same paragraph or list item, at most three lines either side,
  inline code removed: a double-quoted quotation, straight or curly; a `>` blockquote line; a
  citation (`ADR` and a number, `decisions/`, `sessions/`, `transcript`, `session` and a hex id, a
  board id); or a demotion (`the run's choice`, `an agent's decision`, and the like).
- **Ignored on purpose:** fenced code, inline code, `>` blockquote lines as attributions, and a
  generated `docs/ROADMAP.md` when `docs/roadmap/` exists.
- **Additions only, on both planes**, because a record's old line cannot be fixed without
  rewriting history; the whole-tree form reports and always exits 0.
- **The date cannot be moved** by any flag, environment variable or config key; the flip needs no
  edit to the floor.
- **Exempt only with a reason:** `attribscan:allow: <reason>` on the line or in its block; a bare
  marker exempts nothing.
- **A broken scan is not a pass:** an unresolvable revision exits 2, except `HEAD^` on a first
  commit, which passes and says so.
- **Fleet-safe at landing:** probed by exit code over every local child checkout and atelier on the
  CI plane's own argument, with the date patched, and none would have failed (the changelog's
  count).
- **The registry line tells the truth:** `--warn` stays out of the templates so the floor reports
  that the check will gate on its date; a child may declare the advisory form for adoption.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine. The lenses organise it; they do not bound it. Anything not named a
non-goal is in scope.

**Non-goals:** the other twelve scanners and the board item `641f017f` changes (the coverage line
across them, `115/130`, is its own work); the other five checks of `320/810`, each owed its own
pass; `320/080`'s corpus-checking quote verifier, which this scanner states it does not attempt.
Its *absence* is in scope only as far as this delta claims to stand in for it.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **A1.** The form (an attribution word with no evidence in a block of at most seven lines)
     separates unsupported attributions from supported ones well enough to warn now and to block
     from 2027-02-08. Measure it yourself: precision on a seeded sample of the whole-tree output,
     and recall on attributions you write in words the grammar does not list.
   - **A2.** Anything the evidence patterns match is evidence: any double-quoted string, any
     blockquote, any board id, the bare word `transcript`, a `session` followed by hex. Ask the
     item's own question: does a citation that resolves to nothing pass as evidence?
   - **A3.** Reading only added lines is the right plane: an old record is never re-judged, and a
     new unsupported attribution is never missed. Probe what a diff calls "added" (a rewrap, a
     moved or split file under `--no-renames`, a record-store split) and what it never sees (an
     unchanged attribution whose evidence a commit deletes; commits before the tip of a push on
     the CI plane's `HEAD^`).
   - **A4.** A generic use of `ruled`, or of a capitalised word before `'s ruling`, is rare enough
     not to be noise on the flip date (the item's other question).
   - **A5.** The date constant flips cleanly and alone: no flag, variable or config moves it, the
     floor needs no edit, and every repo whose CI floats on atelier's floor is safe on the day.
   - **A6.** The advisory form a child may declare still leaves its CI plane meaningful.
   Ask too whether a form check is the right altitude for an authorship defect, against what the
   proposal offered and against the doctrine that already owns the rule (`RECORD.md`, `00-APEX.md`
   § evidence).
2. **Correctness & quality.** Diff each commit; drive the tool on all three planes against scratch
   repos you build, and with the date patched across the flip. Record each overclaim against the
   text that makes it: the module docstring, the help text, the README section, the floor entry's
   comment and `why`, and the `CHANGELOG.md` entry, including where that entry sits in the file.
3. **Completeness / harvest.** Every surface that states the same fact (V3), one home (V4), no
   contradiction between docstring, README, floor comment and code (V5). Tests that would stay
   green on a broken change: mutate the code in a scratch copy, never the worktree. Compare the
   detector with its siblings' shared conventions (fence rule, allow-marker grammar, the advisory
   count line, the coverage line) and with `quotescan`, which shares its subject.
4. **Security & privacy** — mandatory. The scanner prints excerpts of records and file paths it did
   not choose, passes a revision string to git, and reads files a commit adds. Check
   terminal-control and bidi sanitising on every printed field (the path as well as the excerpt,
   text and `--json`); option injection through `--against`; and what a hostile file name, a huge
   file or a pathological line does to the regexes and the run. And the privacy half: the check's
   remedy is to quote the principal more often, in records that may be public. Weigh whether the
   design pushes his words into places the closed personal-data rule guards. Check against OWASP
   ASVS input-handling and output-encoding items, checked, not recalled. `/security-review` reads
   the session's pending diff, not this delta: aim it only at a scratch clone holding the delta as
   pending changes, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root unless it says otherwise, in the foreground, under a load average near 6 on 12 cores; its
results are held in the sibling. Read exit codes explicitly. `python3` on `PATH` is 3.14.6 and git
is 2.50.1 on this machine.

- `cd tools && python3 -m unittest test_attribscan; echo $?`
- `cd tools && python3 -m unittest test_floor.AdvisoryCountContract; echo $?` (about 45 s)
- `python3 tools/attribscan.py --selftest; echo $?`
- `python3 tools/attribscan.py --root . docs; echo $?` (the whole-tree report)
- `python3 tools/attribscan.py --against HEAD^ --root . docs; echo $?`
- `python3 tools/attribscan.py --against nosuchrev --root . docs; echo $?`
- `python3 tools/floor.py --list --root . | grep attribscan`
- The changelog's fleet claim: a probe by exit code over every local child checkout on the CI
  plane's own argument, on your run date and with the date patched to 2027-02-08. Read-only;
  report counts only.

Use `cd tools && python3 -m unittest test_<name>`, never the dotted `tools.test_<name>` form, which
raises `ModuleNotFoundError` here. Run the tool from your worktree, never by bare name from `PATH`.

## House rules for this run

**Live systems:** read-only. The whole-tree run over this repo and the fleet probe over local child
checkouts are reads, and both are in scope. Any probe that would write to a real repo (staging,
committing, installing a hook, editing a board) is **NOT RUN**: build the case in your scratchpad
(scratch repos, a scratch copy of the tool with the date patched) and say which probes you could
not build.

- Never print a secret, and quote no line from a child repo. This repo is PUBLIC: report child
  results by count only, and name no child, host, client or private path. An excerpt of atelier's
  own records is fine where the line is already public.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos and fixtures when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Your verdict will itself contain words like `ruled` about the principal; this file is under
  `docs/`, so expect attribscan to warn on your commit, and write each such line with its evidence.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0210-attribscan-unquoted-attribution-cold.deferred.md`, both delta
commits' message bodies, and the two intent records whole:
`docs/roadmap/320-child-filed-findings-via-pointing-up/100-unquoted-attribution-is-invisible-to-quotescan-and-a-corroboration-for-070.md`
and `docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md`.
Both carry the author's landing account and later measurement under the proposal, and reading is
atomic, so neither can be read in part. What you need from them is quoted in *The acceptance test*
above.

The delta's own text carries the author's account of why (the docstring and the README section
above all); it is the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1330-rule-4-cold-pass-queued-attribscan.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/100-unquoted-attribution-is-invisible-to-quotescan-and-a-corroboration-for-070.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/810-build-six-checks-warn-first-staggered.md \
  --also-exclude docs/reviews/2026-11-14-0210-attribscan-unquoted-attribution-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions A1–A6 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (`20e7fc35`,
`641f017f`: read body-free yes/no, findings by id), findings with stable IDs (prefix `AT`: `AT1`,
`AT2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS /
FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP: act 1 is committed,
unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** `attribscan` is self-authored guard code that will block commits in
every child on its date, so it is doctrine by function (rule 3): **the author applies nothing on
its own**. Record all findings; they are the principal's to decide, after a plain-language account.
Counsel per finding is welcome, labelled as counsel and kept beneath it, and a finding that bears
on whether the 2027-02-08 flip should happen as built says so in its first line.

---

## Verdict — act 1 (cold pass, run 2026-11-15 UTC)

**FAIL — 1 MAJOR · 5 MODERATE · 6 minor · 3 note.** The warning phase is sound and the date flips
cleanly and alone (A5 confirmed, fleet-probed). The flip to blocking on 2027-02-08 as built is not:
the evidence test is satisfied by any quoted token or any board id within three lines, the grammar
reads about one attribution phrasing in nine, a long verbatim quotation of him does not clear the
line it supports, a moved or split record is re-judged whole, and the advisory form a child may
declare reads nothing on CI. Findings are the principal's to rule (rule 3); the author applies
nothing on its own. Every finding that bears on the flip says so in its first line.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection. Spawned by a headless
  Opus 5.5 orchestrator session, itself started by drain session `21a271a5` (Opus 5.5). Both are
  rule-4 off-tier orchestrators: they hold the context partition, form no finding and write no
  severity; neither wrote the brief or the delta. The orchestrator commits this file. Not started or
  instructed by `a18861ae`, `58027096`, `d0ca5d24` or anything `d0ca5d24` started.
- **Authority to run:** the principal's weekly Fable drain. Mike, 2026-11-16 06:53 NZDT (shed
  session `21a271a5`): he invoked `/fable-drain`, the skill's named command for his drain order
  (`~/.claude/fable-drain.json`, `fable-drain` skill). Recorded here as his act, not his words.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1330-1950/atelier` at `9614b231`, read-only
  to me except this file. Scratch repos and tool copies lived in the session scratchpad and are
  deleted after act 2. Review log (open by design, user-local):
  `~/.claude/fable-drain/notes/atelier-160-1330-1950.md`.
- **What I read:** this brief; `tools/attribscan.py`, `tools/test_attribscan.py` at HEAD; the delta
  body-free through `tools/coldsweep.py --commit 20e7fc35` (six paths) and `--commit 641f017f` (two
  paths); `tools/report.py`, `tools/allowmarker.py`, `tools/filewalk.py` as far as attribscan calls
  them; `tools/floor.py` (the `Scanner` class, the state and advisory selection, `subtrees`,
  `_render`, the count reader); `tools/quotescan.py`; `tools/pins.py` (discovery);
  `docs/method/REVIEW.md`; `docs/PERSONAL-DATA.md`; the heads of `RECORD.md` and `00-APEX.md` by
  grep; `CHANGELOG.md` around the entry; `.github/workflows/ci.yml` and `floor.yml` by grep.
  **Exposure, disclosed:** the
  brief's whole-tree re-run line prints the first 40 findings, and the first two are excerpts of
  `docs/ROADMAP-DONE.md` (barred); I saw those two lines in the head of that output and nothing
  else from it. The precision sampler below excluded every barred path by prefix. The sibling
  `.deferred.md` is absent from the worktree and was not sought anywhere. No prior verdict, session
  log, pointer or intent record was opened; the commit bodies were not read.
- **Helpers:** one `web-fetch` subagent on Haiku fetched three OWASP ASVS 5.0 requirement texts
  (lens 4); it formed no finding. `/usr/bin/python3` (3.9.6) ran my probes on scratch copies; the
  brief's own re-run lines ran on `python3` (3.14.6) as written; git 2.50.1.

### Re-run ledger (V2)

All run 2026-11-15 UTC from the worktree root (or `tools/` where the line says so), foreground.

- `cd tools && python3 -m unittest test_attribscan` — 36 tests OK, exit 0 (7.2 s).
- `cd tools && python3 -m unittest test_floor.AdvisoryCountContract` — 33 tests OK, exit 0
  (54 s); the worktree was unchanged after it.
- `python3 tools/attribscan.py --selftest` — `selftest OK`, exit 0.
- `python3 tools/attribscan.py --root . docs` — 848 findings in 337 of 1218 files, exit 0;
  coverage 1218 files · 178,199 lines.
- `python3 tools/attribscan.py --against HEAD^ --root . docs` — clean, 1 file read, exit 0.
- `python3 tools/attribscan.py --against nosuchrev --root . docs` — `cannot resolve revision
  'nosuchrev'; refusing to pass over it`, exit 2.
- `python3 tools/floor.py --list --root . | grep attribscan` — `attribscan  enforced  fleet
  decl 1/5 …`.
- **The fleet claim** (read-only, counts only): 22 children and atelier discovered one level under
  the main checkout's parent, all with a records tree. On the CI argument (`--against HEAD^` with
  the absolute scope the floor renders): **0 non-zero exits on 2026-11-15 and 0 with the date
  patched to 2027-02-08**, 0 exit-2. Whole-tree share 1,504 of 6,208 Markdown files (24%);
  children 1,168 of 5,055; highest child share 4 of 11 files (36%). The CHANGELOG's 1,372 of
  5,144 (27%), 21 children and "1 of 2 files" were measured 2026-11-09; the drift is growth and
  the shape reproduces.

The date patch for the flip runs was a scratch copy whose `_utc_today()` returns 2027-02-08; the
worktree's `tools/` was not touched. Every scratch probe named below ran on that copy or the
unpatched one.

### Per-commit ledger

- `20e7fc35` — the attribscan landing (tool, tests, floor entry, floor test, README, CHANGELOG).
  Read body-free: yes, `coldsweep --commit` with six `--path`s; no body printed. Findings: AT1–AT7,
  AT8 (the CHANGELOG hunk), AT9–AT15.
- `641f017f` — the coverage line threaded through (attribscan hunks only). Read body-free: yes,
  `coldsweep --commit` with two `--path`s; the board item and the other scanners left out as
  non-goals. Findings: none; the counts reproduce in every mode and in `--json`.

No commit after `641f017f` touched either attribscan file (`git log` empty). `tools/floor.py` moved
seven times since the landing; none changed the attribscan entry except the declaration column
(`ba55be27`, `115/120` step 0, later work and not this pass's subject).

### Lens 1 — approach and assumptions

The load-bearing assumption under all six named ones is that **the form is a usable proxy for
authorship**: that a quotation mark or a board id near the word `ruled` tells a later reader whose
decision it was. On this repo's own records it is a weak proxy both ways (AT1, AT2, AT11): a quoted
doctrine phrase clears, an unrelated board id clears, a five-line verbatim quotation of him does
not. The proposal (`320/100`, quoted in the brief) offered exactly this form and called it "the
machine-decidable half"; the build took the offer without measuring it, and the CHANGELOG measured
the share of files carrying the form (27%) but not how often the form is right. As a warning the
check is a useful nudge at the moment of writing, which is where the incident lives. As a block it
teaches two things: the synonym (`Mike decided`, `he approved`, `at his request`: none read, AT1)
and the quote mark. The doctrine that already owns the rule says the real thing: `RECORD.md`'s
verbatim rule and its *an answer is not a ruling* line, and `00-APEX.md`'s "never emit a claim
stronger than its evidence". The scanner is a reminder of that doctrine, not an enforcement of it,
and its registry line should say so (the `why` reads as enforcement).

- **A1** (the form separates well enough to block): **damaged.** Recall 3 of 27 paraphrases (11%);
  precision of findings about 20 of 30 on the target form; false clears in 5 of 25 quote-cleared
  and 4 of 12 citation-cleared samples. AT1, AT2, AT11.
- **A2** (anything the evidence patterns match is evidence): **damaged.** `there is no transcript`,
  `session deadbeef`, `ADR 9999`, `100/200 of the budget`, `"--warn"`, `("no")`, inch marks, and a
  quoted reason inside another scanner's allow marker all clear a bare `He ruled this`. A citation
  that resolves to nothing passes. AT1.
- **A3** (added lines are the right plane): **damaged both ways.** A rewrap, a `git mv` and a
  record-store split re-judge old lines and block on the flip date (AT3); a commit that deletes the
  quotation beside an unchanged attribution is not seen (0 files read), and a push of several
  commits is judged by its tip only (AT5).
- **A4** (generic uses are rare): **damaged in part.** Every generic sense probed fires; in the
  seeded sample 6 of 30 findings were generic, future or hedged. AT11.
- **A5** (the date flips cleanly and alone): **confirmed.** One constant, read by `warn_only_today`
  only; no flag, variable or config key (`grep` of `environ|getenv` finds none); the scratch copy
  with the clock moved blocked where the live copy warned, on every probe; the floor's registry
  comment and `warns_only` need no edit; 23 repos probed on the CI argument with the clock moved:
  0 non-zero. The four-week chain holds: blockscan 2027-01-11 + 28 days = 2027-02-08; pdlistscan
  2027-03-08.
- **A6** (the advisory form leaves CI meaningful): **false.** AT4.

### Lens 2 — correctness and quality

What the code does, it does cleanly: the fence rule, the inline-code strip, the blockquote rules,
the allow-marker grammar (a bare marker exempts nothing; an empty-reason marker is noted on stderr
as unparseable), the `HEAD^`-on-a-first-commit pass, exit 2 on a bad revision, the advisory count
line printed with its zero, the coverage line in every mode. Overclaims against the text that makes
them: the README's "no reason to gate history, since `--against HEAD^` reads only what a commit
adds" and the docstring's "an old `ruled` cannot be fixed … so a check that reddened on one would be
a check nobody could clear" (AT3: a move or split reddens on old lines); the README's and
CHANGELOG's "advisory form for adoption" with no plane caveat, against the registry comment that
admits the empty diff (AT4); the CHANGELOG hunk's placement (AT8). The `why` field reads as
enforcement of authorship where the docstring says form. The help text and the module docstring
agree with the code on the grammar.

### Lens 3 — completeness and harvest

Surfaces stating the rule: docstring, help text, README section, floor entry comment and `why`,
CHANGELOG, test names: consistent on the grammar and the date (V3). The grammar is stated in full
twice, docstring and README, with no stamp (V4, AT14). The sibling conventions it shares: the
fence rule (same as `blockscan`), the allow-marker grammar (`allowmarker.marker_rx`), the advisory
count line, the coverage line (all shared helpers). Where it diverges: the against plane does not
pin the diff as `report.STAGED_DIFF_CMD` does (AT7); the printed path is raw where `pdlistscan`
sanitises its detail and `leakscan` shares the gap (AT6); `quotescan`, which shares its subject,
requires two or more words inside the quotes (`QUOTE_RX`), attribscan accepts two characters
(AT1). The registry's pushed-range convention (`--range pushed`) landed after this delta and is not
used (AT5). Tests that stay green on a broken change: two mutants survive (AT9).

### Lens 4 — security and privacy (V6)

Checked against OWASP ASVS 5.0, fetched 2026-11-15: **16.4.1** (L2) "Verify that all logging
components appropriately encode data to prevent log injection"; **2.2.1** (L1) input validated
against an allow list or expected structure; **1.2.5** (L1) OS calls use parameterised queries or
contextual encoding.

- **Output encoding (16.4.1):** the excerpt is sanitised (`report.safe_text`, Cc and Cf dropped;
  bidi probe stripped). The **path is not** (AT6): ESC `[2J` and U+202E in a file name reached the
  terminal on the tree plane and the CI log on the against plane; `--json` escapes both. The `word`
  field is regex-bounded (`\s` admits NBSP, which is printable).
- **Input handling (2.2.1, 1.2.5):** `--against` is passed to `git rev-parse --verify --quiet
  "<rev>^{commit}"` before any diff; `--all`, `--output=<file>`, `-q`, `--no-index`, `HEAD..HEAD`,
  `@{u}` and `:/base` all exit 2 and wrote no file. `git show HEAD:<rel>` takes a path from the diff
  header, prefixed. Argv lists throughout, no shell. Discharged.
- **Hostile inputs:** a 1 MB line costs at most 1.3 s; 100k backticks or quotes are linear; a file
  named `*.md` and a macron path read correctly; CRLF read correctly. A tracked symlink under
  `docs/` to a file outside the repo makes the tree plane traceback and exit 2 (no leak; AT12); a
  symlink to an in-repo non-Markdown file is read through.
- **Environment:** `GIT_EXTERNAL_DIFF` is defeated by `--no-ext-diff`; `GIT_DIFF_OPTS` and two
  repo-local diff settings crash the against plane to exit 2 (AT7). Fail-closed, as the contract
  says, but as a traceback.
- **Privacy:** AT13, weighed and not raised above a note.
- **`/security-review`:** NOT RUN, discharged by grounds. It reads the session's pending diff, which
  in this worktree is this brief and the deleted sibling, both barred material, so aiming it here
  would read what rule 2 bars and nothing of the delta; the delta is landed, so a scratch clone
  would hold no pending diff for it to read. The lens was worked by hand above.

### Standing checklist V1–V7

- **V1** — three overclaims recorded in lens 2 (AT3, AT4, AT8); the fleet and share claims hold.
- **V2** — every re-run line reproduced; the fleet claim reproduced in shape with drifted numbers.
- **V3** — one rule, swept: the grammar and the date agree across docstring, help, README, floor
  entry, CHANGELOG and tests; the four-week chain across the sibling checks holds.
- **V4** — the grammar is restated in full in the README with no stamp (AT14, note).
- **V5** — one CHANGELOG entry carries two dates and an orphan heading (AT8); the README's advisory
  claim contradicts the registry comment (AT4). Cross-references reached: `320/810` and `320/100`
  quoted in the brief carry the words the docstring attributes to them; `harvestscan`'s `--against`
  convention is as the docstring says.
- **V6** — lens 4; AT6, AT7, AT12, AT13.
- **V7** — stated above and in the brief's spawn section.

### Findings

Severity: MAJOR / MODERATE / minor / note. A first line that says **bears on the flip** means the
finding is about whether 2027-02-08 should block as built. Counsel is labelled and kept beneath.

**AT1 — MAJOR — Bears on the flip.** Measured on this repo's own records, the grammar and the
evidence test do not separate supported from unsupported attributions well enough to block.
*Recall:* 3 of 27 paraphrased attributions fire (`Mike ruled it`, `Mike's directive`, `the
principal's ruling`); `Mike decided`, `he approved`, `per Mike`, `at his request`, `his call`, `he
said no`, `Owner ruling 2026-08-23`, `the owner's call` and 16 more pass silently. *False clears,
the brief's worse failure mode:* over 653 non-barred `.md` files under `docs/`, 391 attribution
lines: 249 findings, 89 cleared by a quotation, 48 by a citation (37 of them a board id), 4 by a
demotion, 1 by a blockquote. A seeded sample (seed 1330) of 25 quote-cleared lines: 15 cleared by
his words or his recorded pick, 5 by a quotation that is not his (a quoted doctrine phrase, a quoted
exclusion text, a quoted board message), 5 not attributions at all. Of 12 citation-cleared lines:
4 cite the record holding the decision, 4 are cleared by a board id about something else, 4 are
generic lines. Scratch probes: `He ruled this; there is no transcript.`, `He ruled this. The flag is
"--warn".`, `He ruled this, see 100/200 of the budget.`, `He ruled this in session deadbeef.`, `He
ruled this: see ADR 9999.`, `Price 5" screws, 3" nails.` all clear a bare attribution. *Precision
of findings:* of 30 sampled, 20 are the target form, 6 generic or future (AT11), 2 supported but
unseen (AT2 and a Markdown link to a record file), 2 headings with the words in the body below a
blank line. The README discloses "the patterns are a grammar"; nothing measures it, and the
CHANGELOG's only measurement is the share of files carrying the form.
*Counsel:* keep the check warn-only past 2027-02-08 and set a new date only after the evidence
test is tightened and re-measured on the whole tree: a quotation of two or more words (as
`quotescan`'s `QUOTE_RX`) in the attribution's own sentence or the next line; a board id,
`transcript` or `session <hex>` counts only when it follows the attribution word in its sentence;
a quotation may close anywhere in the paragraph (AT2); and publish the measured precision beside
the share. Rename the registry `why` to say form, not authorship.

**AT2 — MODERATE — Bears on the flip.** A verbatim quotation of him that runs past the three-line
window does not clear the attribution it supports, so the house's own long-quote form is a
finding. Probe: the same text with the closing quote on line 3 gives 0 findings; on line 5, 1
finding, as a paragraph and as a list item. Real instance in the whole-tree output:
`docs/roadmap/210-instruments-open-features/230-ccarchive-a-real-calendar-schedule.md:30`, where
"Mike's ruling, verbatim (2026-10-05)" is followed by a five-line italic quotation of him.
`_QUOTE_RX` already spans newlines; only the `WINDOW` cut in `_block_bounds` defeats it.
*Counsel:* read quotations over the whole paragraph or list item; keep the cap, if wanted, for
citations and demotions.

**AT3 — MODERATE — Bears on the flip.** "Additions only" does not hold for a rewrap, a move or a
record-store split. `git diff --no-renames` calls every line of a moved file added, and a
re-wrapped paragraph's lines are added, so old unquoted attributions are re-judged and block on the
flip date. Probes on scratch repos, clock moved: a rewrap of one old line, 1 finding, exit 1; `git
mv` of a record, 1 finding, exit 1; a one-file log split into five per-day files, 5 findings, exit
1. The README says "no reason to gate history, since `--against HEAD^` reads only what a commit
adds", and splitting one-file stores is what `sizescan` presses every repo to do.
*Counsel:* drop an added line whose text also appears among the removed lines of the same diff (a
moved or re-wrapped line), on both planes; or follow renames on the CI plane and read only the
changed hunks of a renamed file. Say in the README what still re-judges.

**AT4 — MODERATE — Bears on the flip.** The advisory form a child may declare reads nothing on
the CI plane. The registry's advisory argv is `--warn --staged --root {root} {scope}`;
`tools/floor.py` selects the advisory argv on CI for every check without a message plane; on CI
the index equals HEAD, so the run prints "0 file(s) read", the coverage line says "scanned
nothing", exit 0, and the board shows `advisory`. Probe on a scratch repo whose tip adds an
unquoted attribution, clock moved: `--warn --staged`, clean, 0 files; `--against HEAD^` on the same
tip, 1 finding, exit 1. The registry comment admits "on CI that is an empty diff"; the README ("an
`advisory` form a child can declare for adoption with a why and a review date") and the CHANGELOG
("Registered in the floor with an advisory form for adoption") do not. No other softenable blocking
check carries `--staged` in its advisory argv (`harvestscan` does, and is warn-only on both
planes). The brief's A6 is false as built; the escape hatch the flip pushes children towards
removes their CI cover for this check without saying so on the board.
*Counsel:* a per-plane advisory in the floor, or an advisory argv of `--warn --against HEAD^` on CI;
until then the README says the advisory form covers the hook plane only.

**AT5 — MODERATE — Bears on the flip.** The CI plane judges a push by its tip. `--against HEAD^`
reads the lines added by the last commit only. Probe: three commits pushed together with the
unquoted attribution in the first: clean on `HEAD^`; `--against HEAD~3`, 1 finding, exit 1 with the
clock moved. The hook plane sees each commit where the hook is installed; CI is the plane the brief
says binds every child with no edit. The registry now carries a pushed-range convention (`--range
pushed`, `quotescan` and `namescan`, landed after this delta), which did not exist when attribscan
took `harvestscan`'s `HEAD^`. A shallow clone of depth 1 reads `HEAD^` as "first commit: nothing to
compare" and passes; `floor.yml` fetches depth 0, so only a child with its own workflow is exposed.
*Counsel:* on CI, compare against the push's `before` sha where the event carries one, falling back
to `HEAD^`; note the shallow-clone case in the README.

**AT6 — MODERATE — security.** The printed path is not sanitised (CWE-117 / CWE-150; ASVS 5.0
16.4.1). `render` passes the excerpt through `report.safe_text` and `f.path` raw. Probe: a file
under `docs/` named with ESC `[2J` and U+202E reached the terminal unaltered on the tree plane and
the CI plane; `--json` escapes both. The house named this class for the excerpt (`160/790` HX2) and
`test_an_excerpt_cannot_carry_a_control_character` pins the excerpt only. `leakscan` prints
`f.path` raw too, so the class is sibling-wide. Exploitability is low: a pull request has to land
the file name, and the hook plane prints it to its own author. Recurrence prevention: one shared
path renderer in `report.py` used by every finding line, and a test on the path as on the excerpt.
This is tooling the repo ships for others to adopt; `SECURITY.md`'s disclosure path applies to the
class, not urgently.

**AT7 — minor.** The CI plane does not pin the diff the way the staged plane does.
`report.STAGED_DIFF_CMD` pins `core.quotePath=false`, `diff.suppressBlankEmpty=false`,
`diff.interHunkContext=0` and strips `GIT_DIFF_OPTS`; `scan_against` runs a bare `git diff
--unified=0`. In a repo with `diff.interHunkContext=3` and `diff.suppressBlankEmpty=true`, or with
`GIT_DIFF_OPTS=-u5` in the environment, the run ends in a `DiffReadError` traceback and exit 2:
fail-closed, as the contract says, but a crash where the staged plane reads correctly.

**AT8 — minor.** The landing commit damaged the CHANGELOG. `20e7fc35` inserted the attribscan entry
between the heading `### Added (2026-11-10 — blockscan reads edits inside mapped sub-sections …)`
and its body and re-dated the body's heading `2026-11-09`. At HEAD, line 280 is that empty
2026-11-10 heading and line 307 its duplicate dated 2026-11-09 (V5: one entry, two dates). The
attribscan entry itself sits in the 2026-11-09 block, which is its landing date.

**AT9 — minor.** Two test gaps, found by mutating a scratch copy and running the 36 tests against
it: disabling `_in_scope` on the against plane (every `.md` in the repo read, past the floor's
scope) and dropping `--no-renames` both leave the suite green. Killed: sanitising, `WINDOW`, both
sides of the date, the board-index skip, quote-in-code, the bare marker, tree-never-blocks,
blockquote evidence, `transcript`, `--warn`, `ruled out`.

**AT10 — minor.** The name grammar is ASCII-only. `_NAME_RULING_RX` is `[A-Z][a-z]+`:
`Ngāio's ruling` and `Māori's directive` are not read, `Ngaio's ruling` is; `McDonald's ruling`
is not. `CONVENTIONS.md` requires macrons on te reo Māori, and the test fixture spells the name
without one.

**AT11 — minor.** Generic senses of the words are findings (A4 damaged in part):
`The court ruled`, `a ruled notebook`, `Monday's ruling`, `the Court's directive`,
`Python's directive`, `he directed the film`, `he instructed the class` all fire; in the seeded
sample 6 of 30 findings were generic, future (`await Mike's ruling round`, three times) or hedged
(`may have been ruled`). About one finding in five on the flip date would be noise of this kind,
and its remedy is the marker.

**AT15 — minor.** An inline code span that wraps across a line break is mis-paired, and the
example text inside it is read as prose. `_strip_code` works one line at a time; on a line whose
first backtick closes a span opened on the line above, every pair shifts by one and the last
span's text stays visible. Probe: the phrases of the grammar quoted in backticks as examples,
wrapped once mid-span, 1 finding on `ruled`; the same text unwrapped, 0. Found when this verdict's
own first draft warned three times on lines like these (since rewrapped). `allowmarker.
blank_code_spans` has the same one-line limit by design; for attribscan the effect is a false
finding on documentation of the grammar, which every README section about it will contain.

**AT12 — note.** Symlinks. A tracked symlink under `docs/` to a file outside the repo makes the
tree plane traceback (`relative_to` raises `ValueError`) and exit 2; a symlink to an in-repo
non-Markdown file is read through as Markdown. `filewalk._git_walk` skips symlinked directories,
not symlinked files.

**AT13 — note — privacy, weighed.** The remedy line leads with "Quote him". `Mike's ruling` (PD4,
his first name) is itself a phrase the name grammar reads, so the check fires most often on lines
naming him and asks for his verbatim words beside his name in a public record. The citation and
demotion routes carry no personal data, and the closed list already treats "his words, stored
verbatim where cited" as house practice, so no new class of data is pushed. The remedy order could
lead with the citation.

**AT14 — note.** Wording and surfaces. `commit blocked` prints on the CI plane, where nothing is a
commit; `--json` says `"clean": true` on a whole-tree run with findings (true by exit code, odd by
the word); the evidence grammar is stated in full in the docstring and the README with no stamp
(V4); the date appears in five prose places and one constant, consistent on 2026-11-15.

### Decided and not raised

Option injection through `--against` (every probe exit 2, no file written); pathological lines
(1.3 s per MB at worst); CRLF; a file named `*.md` and a macron file name; `GIT_EXTERNAL_DIFF`
(defeated by `--no-ext-diff`); the `decl 1/5` column (later work, `115/120`); the four-week date
chain (consistent); the whole-tree `clean: true` beyond a note.

### Owed ask (plain briefing, for the principal)

🎯 **One decision:** does the 2027-02-08 flip to blocking stand as built? The check works as a
warning now. On the flip date, as built, it would block some compliant records (long quotations,
moved or split files), pass fabricated ones written in other words or beside any quote mark, and
lose CI cover in any child that softens it.
- **(a) Keep the date as built.** Accepts AT1–AT5 as known holes; children learn the marker.
- **(b) Stay warn-only; re-date after AT1–AT5 are fixed and cold-reviewed.** *Recommended
  (counsel).* Keeps his "warnings at first and then move to blocking action" in order, with a
  gate worth having when it bites.
- **(c) Whole-tree report only, no flip.** Keeps the measurement, drops the gate.

### Follow-up checklist

- [ ] The principal rules AT1–AT15 (rule 3; the author applies nothing on its own).
- [ ] If (b): the fixes to AT1–AT5 land with their own cold pass (self-authored guard code), and
      the date constant moves as part of that landing, not before.
- [ ] AT6: a shared path renderer in `report.py`; sweep `leakscan`'s finding line; a path test.
- [ ] AT8: repair the CHANGELOG headings (a current-truth file; fix in place).
- [ ] AT9: a CI-plane scope test and a rename test.
- [ ] Act 2 (`### Reconcile`) after the orchestrator releases the sibling.

**Overall: FAIL — 1 MAJOR · 5 MODERATE · 6 minor · 3 note.** The warning phase and the date
mechanism pass; the flip as built does not.

### Reconcile (act 2, 2026-11-15 UTC)

Opened after act 1 was committed as `f4998896`: the held sibling (released by the orchestrator from
its hold outside the worktree), the two intent records `320/100` and `320/810` whole, the queue
pointer `160/1330`, the author's session record (`docs/sessions/2026-11-09-1233-queue-run-d0ca.md`)
and the brief-writer's (`2026-11-14-0210-brief-writer-a188.md`), the tail of `docs/SESSIONS.md`,
`docs/ROADMAP-DONE.md` (no mention of the scanner), the four prior verdicts of 2026-11-14 that name
it in passing, and both commit bodies. Act-1 text above is unrevised. One finding is formed here
and marked so; no act-1 severity moves.

**The author reached the headline conclusion first, and nowhere the scanner's own readers would
see it.** Under `320/100`, the author session (`d0ca5d24`) recorded on 2026-11-12 UTC a whole-tree
run over 30 local repositories (3,469 findings) and a seeded sample of 200 sorted by a Sonnet agent
and spot-checked: 62 real, 82 not an attribution, 44 attributions whose evidence the check missed,
precision about 31%, and the words "`attribscan` must not block as built", with a list of fixes it
calls owed before 2027-02-08 (a principal word in the same sentence as `ruled`, skip pending and
negated forms, widen the window to the whole item and across a blank line after a colon, more
citation spellings, exempt `decisions/`). Recall was not measured. No commit since has touched the
scanner; the README, docstring, floor entry, CHANGELOG and the `320/810` landing note still carry
the share (27%) and the fleet probe and nothing of the precision. AT1 stands as written and gains a
corroborating measurement on a wider corpus: the author's 31% real on 200 across 30 repos beside my
20 of 30 on the target form in this repo's non-barred docs (my class is wider: a dated attribution
by anyone with no adjacent evidence, where the author's "real" is an unsourced claim that the
principal decided). The two samples agree on what fools the check. That the warning conclusion
was reached by the author and left off every surface a reader of the scanner meets is the
record-side half of AT1: the measurement belongs in the CHANGELOG beside the share and in the
`320/810` landing note, not under the proposal alone.

Per finding, against the sibling and the author's account:

- **AT1 (MAJOR)** — the sibling's questions 1, 5 and 7 asked exactly this, unprobed; the author's
  2026-11-12 measurement answers it the same way. Stands. The author's owed-fix list and my counsel
  overlap on four of five points; mine adds the two-word quotation rule from `quotescan` and the
  rename of the registry `why`.
- **AT2 (MODERATE)** — the author names "a quote past the three-line window" and "a quote on the
  line after `verbatim:`" among what fools it; the sibling's question 10 (the repo's own verdicts
  after the flip) is this class. Stands; the fix is already on the author's list.
- **AT3 (MODERATE)** — the sibling's question 2, verbatim the same case. Not in the author's list.
  Stands.
- **AT4 (MODERATE)** — the sibling's question 4. The landing commit body repeats "an advisory form
  for adoption" with no plane caveat. Not in the author's list. Stands.
- **AT5 (MODERATE)** — the sibling's question 3. Not in the author's list. Stands.
- **AT6 (MODERATE)** — the sibling's question 8, unprobed there. Stands.
- **AT7, AT9, AT10, AT12, AT14** — not raised in the sibling or the records; stand.
- **AT8 (minor)** — the sibling's question 9 saw the same orphan heading on 2026-11-14 at line 280.
  Stands.
- **AT11 (minor)** — the author's "pending, not claimed" and "a bare `ruled` with no ruler" classes
  are this finding, measured by the author at 82 of 200 not an attribution at all. Stands at minor:
  it is a precision cost AT1 already carries at MAJOR.
- **AT13 (note)** — the proposal's worked example shows the incident's shape (a port-forward
  "ruled" that was the agent's own); the demotion route is the proposal's own third option. Stands.
- **AT15 (minor)** — not raised anywhere; stands.

**Formed at reconcile, from the sibling's question 6:**

**AT16 — note — formed at reconcile.** One reasoned allow marker exempts every attribution in its
block. `allowmarker.present` is run over the joined block, so a marker on one line clears a `ruled`,
a `his ruling` and a `he directed` on the two lines beside it (probe: three attributions and one
marker in one paragraph, 0 findings; the marker in its own paragraph, 2). The docstring says "on
the line or anywhere in its block", so it is disclosed; the cost is that the one reason covers
claims it was not written for, which is the shape the brief's second failure mode (the marker as
reflex) would exploit. Counsel: a marker exempts the line it sits on, or the single attribution
nearest it.

**Commit bodies, screened.** `20e7fc35`: the body restates the docstring and the fleet probe
("22 of 22 repos exit 0 before and on it"; `320/810` says 21 children and atelier, the CHANGELOG
"21 child checkouts and atelier", consistent), "Tests: 32" (36 at HEAD after `641f017f`,
consistent with the coverage commit's four), and "no child's records mostly so" (my fleet probe:
highest child share 36%, consistent). Co-authored on Opus 5.5. `641f017f`: the coverage commit's
body says nothing of attribscan beyond listing it among nine; its probe was "old against new on
five child checkouts, 60 runs, exit codes identical". Co-authored on Sonnet 5.5. Nothing in either
body changes a finding or a severity.

**The sibling's own re-run results** match mine in every exit code; its whole-tree count (848 in
337 of 1,175 files on 2026-11-14 at `2c1f0296`) and mine (848 in 337 of 1,218 on 2026-11-15 at
`9614b231`) agree on the findings and differ by 43 files added since. Its `--against HEAD^` read 5
files where mine read 1: different tips.

**Overall, restated: FAIL — 1 MAJOR · 5 MODERATE · 6 minor · 4 note.** The warning phase and the
date mechanism pass; the flip as built does not, and the author's own record agrees. The owed ask
above is unchanged: whether the 2027-02-08 flip stands as built, with counsel (b).

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

The text below is the brief's `.deferred.md` sibling, folded verbatim by the headless Opus 5.5
orchestrator (started by drain session `21a271a5`) after act 2 was saved. It was held out of the
review worktree until act 1 was committed as `f4998896`, then released to the reviewer for the
reconcile above. The orchestrator forms no finding and edited none of it; the sibling file itself
is removed from the tree in the same commit as this fold. Act 1 was first committed locally
as `c1973db6` and landed on `main` as `f4998896` after a rebase; the hashes above name the landed
commit.

# Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-14-0210-attribscan-unquoted-attribution-cold.md` (`REVIEW.md` rule
1). Written 2026-11-14 UTC by the brief-writer (`cclive` lists it as session `a18861ae`), which
authored none of the delta. Open this only after act 1 is committed. Everything here is a floor,
never a fence, and none of it is a finding: the brief-writer read the code once and probed none of
these past what is recorded below.

## What the barred intent records say, in brief

- `320/100` carries, under the proposal, a later measurement by the author session (2026-11-12
  UTC): a whole-tree run over 30 local repositories gave 3,469 findings; a seeded random sample of
  200, sorted by a Sonnet agent and spot-checked, put precision at about 31% (roughly 25% to 38%).
  It names what fools the check (a bare "ruled" with no ruler, pending forms such as "to be ruled
  on", evidence outside the window or in forms the patterns miss, a review's own verdict word, the
  body of an ADR) and lists fixes it calls owed before 2027-02-08. Recall was not measured. On
  2026-11-14 no commit after `641f017f` had changed the scanner, so none of those fixes had landed.
- `320/810` records the slice-2 landing with the same fleet probe the changelog states (22 of 22
  exit 0 on the landing date and on the flip date), the 1,372 of 5,144 whole-tree share,
  "Tests: 32" (36 at HEAD, after `641f017f`), and that the dates are the run's choice.

## The brief-writer's own questions

1. **Precision against the flip.** The fleet probe counts exit codes on `--against HEAD^`, which
   reads one commit per repo. Does "0 non-zero exits" say anything about how often an ordinary
   commit after 2027-02-08 will be blocked? Set it beside the author's own later measurement above.
2. **Moves and splits.** `scan_against` runs `git diff --no-renames`, and the staged plane reads
   what git reports as added. A record moved or split into per-item files (a routine operation in
   this estate) makes every old line "added". Does a record-store split after the flip get blocked
   by its own history, and does the README's "an old record is never re-judged" survive that?
3. **Push depth.** The CI template is `--against HEAD^`. A push of several commits is read at its
   tip only. Is the hook the only cover for the others, and is that stated anywhere a reader of the
   registry would see it?
4. **The advisory form on CI.** The floor entry's comment says a floor-level softening selects the
   advisory argv on both planes, and on CI that argv (`--warn --staged`) is an empty diff. Does a
   child that declares the advisory form get a CI line that reads as a pass while reading nothing?
5. **Evidence that is not evidence.** Any double-quoted run of two or more characters (a quoted
   term, a file name), any `>` line, any `NNN/NNN` (the item's own id included), the bare word
   `transcript`, and `session` plus six hex characters all clear a hit. A board id need not exist.
   How cheap is a false clear, and is it cheaper than writing the allow marker?
6. **One marker, several hits.** The allow marker is searched across the whole block, so one
   reasoned marker exempts every attribution within three lines of it. Intended?
7. **Name-possessive grammar.** `[A-Z][a-z]+'s (ruling|directive)` fires on any capitalised word:
   a sentence-initial "Today's ruling", "Board's ruling", a reviewer's verdict word. And the role
   grammar has no `his decision`, `his call`, `he decided`, `he chose`, `per <name>`. Which way
   does the trade fall, and is the recall gap stated (the README says only "a grammar")?
8. **Printed paths.** The excerpt passes through `report.safe_text`; `f.path` in `render` does not.
   A file name with a control character from a diff or a walk: what does it print?
9. **The changelog entry's place.** In `20e7fc35` the new entry was inserted directly under an
   existing `### Added (2026-11-10 — blockscan ...)` heading, leaving that heading empty and a
   second `### Added (2026-11-09 — blockscan ...)` heading after the new entry. At HEAD the empty
   heading is still there (line 280 on 2026-11-14), now followed by a later slice's entry.
10. **Its own verdicts.** This repo's reviews and briefs say `ruled` about the principal often, with
    quotes on adjacent lines that may fall outside the window. Will the scanner block the repo's own
    review records after the flip?

## What the brief-writer ran, and what it got

All from the worktree root on 2026-11-14 UTC unless stated, foreground, load average 5 to 6 on 12
cores, at `origin/main` `2c1f0296`.

- `cd tools && python3 -m unittest test_attribscan`: 36 tests, OK, exit 0, about 7 s.
- `cd tools && python3 -m unittest test_floor.AdvisoryCountContract`: 33 tests, OK, exit 0, about
  45 s. One fixture inside it prints a board-rebuild line to the terminal; the worktree stayed clean
  (`git status --short` empty afterwards).
- `python3 tools/attribscan.py --selftest`: `selftest OK`, exit 0.
- `python3 tools/attribscan.py --root . docs`: exit 0; 848 unquoted attributions in 337 of 1,175
  files; coverage 1,175 files, 171,549 lines. The first listed hit is in `docs/ROADMAP-DONE.md`, a
  line naming "the board-store ADR" with no number.
- `python3 tools/attribscan.py --against HEAD^ --root . docs`: exit 0, clean, 5 files read.
- `python3 tools/attribscan.py --against nosuchrev --root . docs`: exit 2, "cannot resolve
  revision".
- `python3 tools/floor.py --list --root .`: attribscan listed `enforced`, `fleet`, `decl 1/5`.
- The two `coldsweep --commit` lines in the brief: each exit 0, no body printed.
- `merge-base --is-ancestor` on `20e7fc35` and `641f017f`: both ancestors of `2c1f0296`.
- **Not run:** the fleet probe over child checkouts (left whole to the pass), and any probe of the
  questions above.
