# Cold pass — the exception-register design, redrafted and reworked to one central file (160/650, 110/100)

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4 (a design every scanner and
child would build to, doctrine by function).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1130-rule-4-cold-pass-queued-exception-register-redraft.md`
(barred until phase 2).
**Size:** large: a 532-line draft ADR on a failed design (16 prior findings to trace), with counts
over the child repos to re-derive; no code to run.
**Why it earns a review:** The design replaces how every guard exception in every child is recorded.
It forecloses alternatives and it is a commitment before build, the cheapest moment to catch a wrong
premise. The worst failure is a migration that turns children red, or a register that records a
grant nobody can check.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, and the Opus worker it dispatched, which wrote both the redraft and the rework (per
  the queue pointer and `160/650`). The author queued this pass and does not take it.
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

The principal's answers to the redraft's four questions, 2026-11-09, verbatim, each a pick from
offered options: Q1 *"Large: one central file"*; Q2 *"Yes, short ID + pointer"*; Q3 *"Mark
'unrecorded' + review date"*; Q4 *"Separate investigation"* (binary contents go to `115/390`,
outside this design). The design is a draft: the principal rules on acceptance after this pass, and
approves this pass first. The ADR's § *Open questions for Mike* says none remains, with what is left
his.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

A draft ADR, no code. Two commits on `main`: `c687e446` redrafted it on the failed pass's counsel;
`7c2beaea` then reworked it to the one-central-file shape on the principal's answers. **The subject
is the ADR at HEAD.** Read both commits; the queue pointer's delta names the file at HEAD, since
the rework came after the redraft.

Commits on `main`: `c687e446`, `7c2beaea`. The landing commit is `7c2beaea`. **Check your tree has
it before reading anything:** `git merge-base --is-ancestor 7c2beaea HEAD` exits 0, and an
orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `docs/decisions/2026-10-03-0641-the-exception-register.md`, `docs/decisions/README.md`.
Read each at HEAD and read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit c687e446 --path docs/decisions/2026-10-03-0641-the-exception-register.md --path docs/decisions/README.md
python3 tools/coldsweep.py --root . --commit 7c2beaea --path docs/decisions/2026-10-03-0641-the-exception-register.md --path docs/decisions/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 7c2beaea..HEAD -- docs/decisions/2026-10-03-0641-the-exception-register.md docs/decisions/README.md
```

At `457615cc` this printed nothing. Read anything new the same way.

**Application pass.** This delta reworks a design on the counsel of a failed pass, and the ADR's own
§ *What changed, and why* names those findings. It cannot fully honour rule 2: the delta carries
finding ids and the decisions stamped on them. Sequence (`REVIEW.md` § *Applying decisions to
doctrine*): review the work at HEAD and commit findings first; open the prior verdict after. Name
that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- One central file per repo, `.atelier-exceptions.jsonl`, append-only under a union merge, replaces
  the scattered notes.
- Each record names who granted it (`principal-ruled`, `principal-answer`, `agent`), the short
  session id, the date and a pointer to his words.
- Old and new forms both work from the start; the old form retires only on a later dated ruling at
  zero unmigrated, so no child goes red.
- § 8 states what the central choice costs and how each cost is paid; § 9 is the smallest first
  build.
- § *What changed, and why* answers each of the sixteen findings of the failed pass.
- `.leakscanbinaries` moves in and floor softening stays in `.atelier-floor.json`, stated as the
  writer's readings.
- § *What exists, measured* states counts over the tree and the child repos. Re-derive them
  read-only and by count (V2); the brief-writer did not.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** scanning inside binary files (`115/390`, by his answer); building any of it; ruling
on acceptance, which is the principal's.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. A design that records who granted what, in repos some of
which are public. Enumerate the threats yourself at design altitude: who can write a record, what a
record exposes, what trusts it. No code exists, so `/security-review` has nothing to read: discharge
it in one line.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- the adopting child repos, read-only and by count only: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch file
- `nice -n 10 python3 tools/floor.py --plane ci --root .`

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
(`2026-11-09-0153-exception-register-redraft-cold.deferred.md`), every delta commit's message body,
the queue pointer
`docs/roadmap/160-doctrine-review-owed/1130-rule-4-cold-pass-queued-exception-register-redraft.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md`
- `docs/roadmap/110-estate-duplication-exception-audit-mike/100-two-granularities-the-2026-08-09-audit-never-asked-about.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default):
`docs/reviews/2026-10-04-2215-exception-register-design-cold.md`. The delta's docstrings, comments,
ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1130-rule-4-cold-pass-queued-exception-register-redraft.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/650-rule-4-cold-pass-queued-exception-register-design.md \
  --also-exclude docs/roadmap/110-estate-duplication-exception-audit-mike/100-two-granularities-the-2026-08-09-audit-never-asked-about.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`c687e446` and `7c2beaea`: read body-free
yes/no, findings by id), findings with stable ids (prefix `ERD`: `ERD1`, `ERD2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

