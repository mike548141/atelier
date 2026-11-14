# Cold pass — `attribscan`, an attribution to the principal carries his words

**Board:** `docs/roadmap/160-doctrine-review-owed/1330-rule-4-cold-pass-queued-attribscan.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `a18861ae`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
