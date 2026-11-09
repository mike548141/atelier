# Cold pass — a malformed allow-marker goes strict after a dated warning (160/480, 160/110), and a check may be lowered only declared, reasoned and expiring (020/170)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: the shared marker reader in every child, and guard doctrine).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1190-rule-4-cold-pass-queued-strict-markers-and-lowering.md`
(barred until phase 2).
**Size:** large: 32 files and 1,158 added lines in the marker commit across every scanner that reads
it, one doctrine commit, and a fleet census to re-derive.
**Why it earns a review:** `tools/allowmarker.py` decides what a scanner exempts in every child, and
it floats at `main`. A wrong read exempts a real secret or leak silently, or reds a child on the
cut-over date. The lowering rule decides how a repo may soften a check at all.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched, which wrote the work (per
  the queue pointer). The author queued this pass and does not take it.
- **Who wrote this brief:** session `d16dc612` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). `74f2b8cd` built none of this delta
  and forms no finding; its launch prompt was the only instruction, and it carried item numbers, the
  owed-or-not test and house rules, no framing of the work. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, ran no review and used no Fable model.
  Neither was started or instructed by the author. Whoever writes a brief does not run it (the
  principal's rule), so both are barred from this pass.
- **Who reviews:** a session on Fable 5.1 that passes rule 4's criterion, started once the principal
  has approved the Fable pass. **Barred from reviewing:** session `722ac2e2` and every worker it
  dispatched; `d16dc612`; `74f2b8cd`.
- **The principal's approval of this brief:** his request, 2026-11-09, verbatim: *"Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done"*. That approves the brief only;
  the Fable gate on the pass is unchanged.
- **Contact, disclosed (rule 4):** the brief-writer had no contact with `722ac2e2` or its workers.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the house-form brief
  `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` lines 1–728, verdict
  included (another surface); the queue pointer whole; the intent records' answer and closing notes,
  by extraction; commit subjects and file lists; the delta's `CHANGELOG.md` entries; the results of
  the re-run lines; parts of the delta's own files at HEAD (outlines, constants, comments). It
  opened no commit message body of this delta, and did not open `docs/SESSIONS.md`, `docs/sessions/`
  or the prior verdict on this subject. Its harness loaded user-level and repo instruction files and
  a memory index, which hold private context this brief does not carry. Everything evaluative is in
  the sibling, by count here: a held-back sibling with one pointer block, 3 questions and 2 facts.

## The acceptance test

The principal's answer on `160/480`, 2026-11-09, verbatim: *"Strict, with a warning period"*. The
option read: count broken markers across every repo first; a malformed marker then warns for a set
period (about 30 days) while items are queued in the affected repos, and after that it exempts
nothing. The same answer covers `160/110`'s LK1. The principal's answer on `020/170`, the same day,
verbatim: *"Allow if declared + expiring"*. The option read: a repo may lower a check's response
only with a written reason and an end date, visible in the fleet view; the new model replaces
E6d(i)'s "never lower" wording.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Two commits on `main`: `6d26b058` (the marker reader and the scanners) and `44f66053` (doctrine).

Commits on `main`: `6d26b058`, `44f66053`. The landing commit is `44f66053`. **Check your tree has
it before reading anything:** `git merge-base --is-ancestor 44f66053 HEAD` exits 0, and an
orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `tools/allowmarker.py`, `tools/blockscan.py`, `tools/datescan.py`, `tools/leakscan.py`,
`tools/linkscan.py`, `tools/pathscan.py`, `tools/reviewscan.py`, `tools/secretscan.py`,
`tools/spellscan.py`, `tools/stampscan.py`, `tools/test_allowmarker.py`, `tools/test_leakscan.py`,
`tools/test_pathscan.py`, `tools/test_report.py`, `tools/test_reviewscan.py`, `tools/README.md`,
`tools/leakscan-terms.example.txt`, `docs/method/GUARDS.md`, `docs/method/README.md`,
`.conflictscanignore`, `.leakscanignore`, `.licenscanignore`, `.secretscanignore`,
`.spellscanignore`, `.stampscanignore`, `.wrapscanignore`, `CHANGELOG.md`. Read each at HEAD and
read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit 6d26b058 --path tools/allowmarker.py --path tools/blockscan.py --path tools/datescan.py --path tools/leakscan.py --path tools/linkscan.py --path tools/pathscan.py --path tools/reviewscan.py --path tools/secretscan.py --path tools/spellscan.py --path tools/stampscan.py --path tools/test_allowmarker.py --path tools/test_leakscan.py --path tools/test_pathscan.py --path tools/test_report.py --path tools/test_reviewscan.py --path tools/README.md --path tools/leakscan-terms.example.txt --path docs/method/GUARDS.md --path .conflictscanignore --path .leakscanignore --path .licenscanignore --path .secretscanignore --path .spellscanignore --path .stampscanignore --path .wrapscanignore --path CHANGELOG.md
python3 tools/coldsweep.py --root . --commit 44f66053 --path CHANGELOG.md --path docs/method/GUARDS.md --path docs/method/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 44f66053..HEAD -- tools/allowmarker.py tools/blockscan.py tools/datescan.py tools/leakscan.py tools/linkscan.py tools/pathscan.py tools/reviewscan.py tools/secretscan.py tools/spellscan.py tools/stampscan.py tools/test_allowmarker.py tools/test_leakscan.py tools/test_pathscan.py tools/test_report.py tools/test_reviewscan.py tools/README.md tools/leakscan-terms.example.txt docs/method/GUARDS.md docs/method/README.md .conflictscanignore .leakscanignore .licenscanignore .secretscanignore .spellscanignore .stampscanignore .wrapscanignore CHANGELOG.md
```

At `457615cc` this printed 4 commit(s). Read anything new the same way.

**Application pass.** `160/480` and `160/110` apply the principal's answer and earlier passes'
counsel. It cannot fully honour rule 2: the delta carries finding ids and the decisions stamped on
them. Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the work at HEAD and commit
findings first; open the prior verdict after. Name that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- A malformed scoped marker exempts nothing from 2026-12-09. Until `MALFORMED_GRACE_UNTIL` (a dated
  constant, no flag or variable moves it) it still does, and every run warns on stderr.
- `python3 tools/allowmarker.py --census` lists malformed markers read-only. The changelog says a
  census of every repo with a floor found no live malformed marker, only documentation mentions.
- A marker inside an inline code span is a mention; `reviewscan`'s deferral waiver reads the shared
  grammar; a marker naming no rule is counted.
- `leakscan`: terms compared in Unicode NFC; the derived-form separator takes `/` and `+`; the path
  plane no longer honours a marker spelt in a filename.
- `GUARDS.md` § *Provenance, not direction*: a repo may lower a check's response only with a written
  reason and an end date, visible in the fleet view; the tool never lowers one on its own judgement.
  A table sets each lowering mechanism against the rule, with two gaps named as follow-ups.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the two gaps the delta names in the lowering table, except where a claim depends on
them.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. This delta changes what a guard exempts, in every child, on a
date. Treat each marker form as hostile input. Aim `/security-review` at the `tools/` diff from a
clean tree, or discharge it by grounds. Quote no fixture's secret-shaped bytes.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `cd tools && python3 -m unittest test_allowmarker`
- `cd tools && python3 -m unittest test_leakscan`
- `cd tools && python3 -m unittest test_pathscan`
- `cd tools && python3 -m unittest test_report`
- `cd tools && python3 -m unittest test_reviewscan`
- `python3 tools/allowmarker.py --census --root .`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `nice -n 10 python3 tools/floor.py --plane hook --root .`
- `nice -n 10 python3 -m unittest discover -s tools`
- the adopting child repos, read-only and by count only: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch file;
  then, for each child the report marks wired, `python3 tools/allowmarker.py --census --root
  <child>`, totals only

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; **no live writes**. A check that
  would need a write is marked NOT RUN in the verdict, with what it would have shown.
- Probes run on scratch copies and synthetic fixtures under your scratchpad only, deleted when you
  finish. Never mutate the worktree's `tools/` or `instruments/`.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live: touch nothing outside your worktree and scratchpad.
- Read-only git only, beyond committing this one file at the end of each phase (or handing it to the
  orchestrator to commit).
- Child repos are read-only and counted, never named: quote no child's name, path or excerpt.
- One heavy process at a time; foreground, long timeout. Never run an installed tool by bare name
  from `PATH`: use the worktree's own copy.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds, never with this brief or its
  sibling dirty. Over markdown its clean pass is empty; weigh it as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, placeholder token, email address, child repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-strict-markers-and-lowering-cold.deferred.md`), every delta commit's message body,
the queue pointer
`docs/roadmap/160-doctrine-review-owed/1190-rule-4-cold-pass-queued-strict-markers-and-lowering.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md`
- `docs/roadmap/160-doctrine-review-owed/110-the-e7-leakscan-cycle-closed-2026-08-09-0-majo.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/170-f1-rebuild-the-block-vs-advise-model-from-base.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default):
`docs/reviews/2026-10-03-0357-shared-allow-marker-grammar-cold.md`,
`docs/reviews/2026-08-09-0826-e7-leakscan-build-cold.md`. The delta's docstrings, comments, ADR
text, `tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are the
delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1190-rule-4-cold-pass-queued-strict-markers-and-lowering.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/480-rule-4-cold-pass-queued-the-shared-allow-marker-grammar.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/110-the-e7-leakscan-cycle-closed-2026-08-09-0-majo.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/170-f1-rebuild-the-block-vs-advise-model-from-base.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`6d26b058` and `44f66053`: read body-free
yes/no, findings by id), findings with stable ids (prefix `SML`: `SML1`, `SML2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

