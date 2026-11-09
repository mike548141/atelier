# Cold pass — eight guard and evidence additions the principal approved in one list

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function; one change is to `floor.py`, which every child runs).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1150-rule-4-cold-pass-queued-guard-and-evidence-doctrine-batch.md`
(barred until phase 2).
**Size:** medium: nine commits, wording in five method files plus one new page, and one small change
to `tools/floor.py` with tests; eight rules to test against their approved lines.
**Why it earns a review:** These rules govern what counts as evidence and how a guard is written,
and one code change alters what every child's floor prints. A wrong evidence rule manufactures false
confidence everywhere it is read.

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
  the sibling, by count here: a held-back sibling with one pointer block, 2 questions and 1 fact.

## The acceptance test

*"Approve all 20"*, on 2026-11-09, after reading a one-line summary of each of twenty items,
approving the recommendation on each. The recommendation approved, item by item:
- `320/020`: adopt the rule as a short companion to the guard rules, noting atelier's own guards are
  not yet audited against it.
- `320/030`: adopt "capture, do not compose" test fixtures as doctrine.
- `320/390`: adopt the child's rule as house doctrine; no guard (not mechanisable).
- `370/010`: adopt the artefacts-over-reports rule and write-then-rename, as data-integrity doctrine
  with no scanner.
- `380/010`: adopt "show a positive control first" as its own rule, mandatory where a negative
  authorises an irreversible act.
- `400/010`: write a one-page decision guide on the four axes.
- `320/050`: add a "who is protected from whom" declaration to guard doctrine, with the
  pathspec-commit caveat.
- `020/350`: escape visibly the bidi override and isolate set (U+202A–202E, U+2066–2069); leave
  joiners alone.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Nine commits on `main`: one per addition (`320/020` to `400/010`, with a code commit for `020/350`)
and one changelog commit.

Commits on `main`: `8a58b882`, `9f5736cb`, `6643d5ec`, `23b8570f`, `79db6ed9`, `9d652f4b`,
`7688af74`, `32b18fe5`, `28c67b4a`. The landing commit is `28c67b4a`. **Check your tree has it
before reading anything:** `git merge-base --is-ancestor 28c67b4a HEAD` exits 0, and an orchestrator
merges `origin/main` into the review branch before it spawns.

Delta paths: `docs/method/EVIDENCE.md`, `docs/method/GUARDS.md`, `docs/method/DATA-PROTECTION.md`,
`docs/method/CONCURRENCY.md`, `docs/method/MECHANISMS.md`, `docs/method/README.md`, `README.md`,
`tools/floor.py`, `tools/test_floor.py`, `CHANGELOG.md`. Read each at HEAD and read each commit
body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit 8a58b882 --path tools/floor.py --path tools/test_floor.py
python3 tools/coldsweep.py --root . --commit 9f5736cb --path docs/method/EVIDENCE.md
python3 tools/coldsweep.py --root . --commit 6643d5ec --path docs/method/CONCURRENCY.md --path docs/method/EVIDENCE.md
python3 tools/coldsweep.py --root . --commit 23b8570f --path docs/method/EVIDENCE.md
python3 tools/coldsweep.py --root . --commit 79db6ed9 --path docs/method/DATA-PROTECTION.md
python3 tools/coldsweep.py --root . --commit 9d652f4b --path docs/method/GUARDS.md
python3 tools/coldsweep.py --root . --commit 7688af74 --path docs/method/GUARDS.md
python3 tools/coldsweep.py --root . --commit 32b18fe5 --path README.md --path docs/method/MECHANISMS.md --path docs/method/README.md
python3 tools/coldsweep.py --root . --commit 28c67b4a --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 28c67b4a..HEAD -- docs/method/EVIDENCE.md docs/method/GUARDS.md docs/method/DATA-PROTECTION.md docs/method/CONCURRENCY.md docs/method/MECHANISMS.md docs/method/README.md README.md tools/floor.py tools/test_floor.py CHANGELOG.md
```

At `457615cc` this printed 16 commit(s). Read anything new the same way.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- `EVIDENCE.md` §16 capture, do not compose fixtures of another program's output; §17 a check in the
  same invocation as its act is not a check, with a pointer in `CONCURRENCY.md`; §18 a negative
  needs a positive control first, mandatory where the negative authorises an irreversible act.
- `DATA-PROTECTION.md`: corroborate from the artefacts; never overwrite a running executable; write
  a new path and rename.
- `GUARDS.md`: forbid or make cheap, by which side of the boundary the writer is on; a guard
  declares who it protects from whom, with the pathspec caveat; atelier's own guards are not yet
  audited against either.
- `docs/method/MECHANISMS.md`: a one-page guide to which mechanism a new need should take.
- `tools/floor.py` `strip_controls` renders U+202A–202E and U+2066–2069 as `<U+XXXX>` instead of
  passing them to the terminal; joiners and zero-width spaces are left alone. The changelog says no
  local child's config carries any and the fleet report is byte-identical before and after.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** an audit of atelier's existing guards against the new rules, which the delta says is
not done, except where a claim implies it.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. `020/350` handles untrusted text at a parse seam that prints
child configuration to a terminal; weigh it by hand. Elsewhere doctrine text, with
`/security-review` aimed only at the `tools/floor.py` diff from a clean tree, or discharged by
grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `cd tools && python3 -m unittest test_floor`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `nice -n 10 python3 tools/floor.py --plane hook --root .`
- `nice -n 10 python3 -m unittest discover -s tools`
- the adopting child repos, read-only and by count only: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch file,
  read back the claim about child configs, by count

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
(`2026-11-09-0153-guard-and-evidence-doctrine-batch-cold.deferred.md`), every delta commit's message
body, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1150-rule-4-cold-pass-queued-guard-and-evidence-doctrine-batch.md`,
and the intent records beyond their titles:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/020-proposal-strict-where-we-author-forgiving-where-we-read.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/030-proposal-capture-do-not-compose-fixtures.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/390-missing-house-rule-a-check-in-the-same-invocation-as-the-act-is-not-a-check.md`
- `docs/roadmap/370-the-report-can-lie-while-the-work-is-fine/010-prefer-artefacts-over-reports.md`
- `docs/roadmap/380-silence-read-as-an-answer/010-make-the-instrument-show-a-positive-first.md`
- `docs/roadmap/400-choosing-among-implementation-mechanisms-mike-comm/010-no-doctrine-says-which-mechanism-a-new-need-should-take.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/050-proposal-a-guard-declares-who-it-protects-from-whom.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/350-bidi-and-zero-width-strip-decision.md`

The delta's docstrings, comments, ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1150-rule-4-cold-pass-queued-guard-and-evidence-doctrine-batch.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/020-proposal-strict-where-we-author-forgiving-where-we-read.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/030-proposal-capture-do-not-compose-fixtures.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/390-missing-house-rule-a-check-in-the-same-invocation-as-the-act-is-not-a-check.md \
  --also-exclude docs/roadmap/370-the-report-can-lie-while-the-work-is-fine/010-prefer-artefacts-over-reports.md \
  --also-exclude docs/roadmap/380-silence-read-as-an-answer/010-make-the-instrument-show-a-positive-first.md \
  --also-exclude docs/roadmap/400-choosing-among-implementation-mechanisms-mike-comm/010-no-doctrine-says-which-mechanism-a-new-need-should-take.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/050-proposal-a-guard-declares-who-it-protects-from-whom.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/350-bidi-and-zero-width-strip-decision.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (each of the nine commits: read body-free
yes/no, findings by id), findings with stable ids (prefix `GEB`: `GEB1`, `GEB2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

