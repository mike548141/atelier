# Cold pass — personal data in a public repo is one closed list only the principal adds to (160/630)

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: a rule of the public repo and a test that enforces it).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1120-rule-4-cold-pass-queued-personal-data-closed-list.md`
(barred until phase 2).
**Size:** medium: one commit (16 files, 495 lines added), mostly wording, plus a 96-line list and
one new test module; needs a sweep of every surface that states the rule.
**Why it earns a review:** The rule decides what personal data may stand in a public repo, where a
push cannot be retracted, and its enforcement is one test whose green is read as "the list matches
the tree". The worst failure is a silent one: personal data standing in the tree unlisted while the
test stays green, or a grant wording that lets a session grant what only the principal may.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the worker it dispatched, which wrote the work (per the queue
  pointer). The author queued this pass and does not take it.
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
  the sibling, by count here: a held-back sibling with one pointer block, 3 questions and 1 fact.

## The acceptance test

The principal's answer on `160/630`, 2026-11-09, verbatim: *"Honest claim + only you grant"*. The
option he picked read: reword the claim to "listed in one place", add a test that keeps that list
matching the files, and add a rule that in a public repo only he grants a personal-data exception,
in his own words, so the scanner refuses any other excuse. A second answer on the private-repo grant
wording, the same day, verbatim: *"Ordering the work is permission"*: in a private repo, the
principal's order for the work is the grant for the personal data that work needs, and the session
notes that it judged so. Judge the wording against both, and against the standing purpose rule in
`docs/build/REPO-STANDARD.md` § *Repo-craft conventions*.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

One commit on `main` that applies the principal's answer and the prior pass's counsel on `160/630`.

Commits on `main`: `920cfed1`. The landing commit is `920cfed1`. **Check your tree has it before
reading anything:** `git merge-base --is-ancestor 920cfed1 HEAD` exits 0, and an orchestrator merges
`origin/main` into the review branch before it spawns.

Delta paths: `docs/PERSONAL-DATA.md`, `tools/test_personal_data.py`, `docs/build/REPO-STANDARD.md`,
`CLAUDE.md`, `docs/build/templates/CLAUDE.md`, `docs/build/templates/CONTRIBUTING.md`,
`docs/method/PRINCIPLES.md`, `README.md`, `commands/scan.md`, `commands/install-hook.md`,
`skills/create-repo/SKILL.md`, `tools/README.md`, `tools/floor.py`, `tools/leakscan.py`,
`tools/secretscan.py`, `CHANGELOG.md`. Read each at HEAD and read each commit body-free, scoped to
paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit 920cfed1 --path docs/PERSONAL-DATA.md --path tools/test_personal_data.py --path docs/build/REPO-STANDARD.md --path CLAUDE.md --path docs/build/templates/CLAUDE.md --path docs/build/templates/CONTRIBUTING.md --path docs/method/PRINCIPLES.md --path README.md --path commands/scan.md --path commands/install-hook.md --path skills/create-repo/SKILL.md --path tools/README.md --path tools/floor.py --path tools/leakscan.py --path tools/secretscan.py --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 920cfed1..HEAD -- docs/PERSONAL-DATA.md tools/test_personal_data.py docs/build/REPO-STANDARD.md CLAUDE.md docs/build/templates/CLAUDE.md docs/build/templates/CONTRIBUTING.md docs/method/PRINCIPLES.md README.md commands/scan.md commands/install-hook.md skills/create-repo/SKILL.md tools/README.md tools/floor.py tools/leakscan.py tools/secretscan.py CHANGELOG.md
```

At `457615cc` this printed 27 commit(s). Read anything new the same way.

**Application pass.** This delta applies the principal's answer and the counsel of an earlier failed
pass on the same subject. It cannot fully honour rule 2: the delta carries finding ids and the
decisions stamped on them. Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the
work at HEAD and commit findings first; open the prior verdict after. Name that residual exposure in
the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- `docs/PERSONAL-DATA.md` names every personal-data exception atelier holds, with why held, how
  granted and where it may stand.
- `tools/test_personal_data.py` fails the suite when a listed string stands in a tracked file no
  entry names, when an entry names a place its string left, when a personal-data allow-marker stands
  outside a named place, when the entry set changes without the test, or when a surface returns to
  the old claim. One entry cannot be pinned to files and says so.
- In a public repo an exception is the principal's alone to grant, in his own words; an allow-marker
  is not a grant.
- The rule is the same across the standard, atelier's `CLAUDE.md` and both child templates; no
  scanner behaviour changed.
- The rule sits outside the stamped doctrine block, so existing children keep the old sentence until
  someone updates them.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the scanner enforcement left as a follow-up by the delta, except where its absence
makes a claim false; the personal data of any other repo.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. This delta's subject is personal data in a public repo. Weigh
what the list itself publishes and whether its grounds hold. Quote no personal datum beyond what the
list already holds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `cd tools && python3 -m unittest test_personal_data`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `nice -n 10 python3 tools/floor.py --plane hook --root .`

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
(`2026-11-09-0153-personal-data-closed-list-cold.deferred.md`), every delta commit's message body,
the queue pointer
`docs/roadmap/160-doctrine-review-owed/1120-rule-4-cold-pass-queued-personal-data-closed-list.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default): `docs/reviews/2026-10-04-2215-pii-by-purpose-cold.md`. The
delta's docstrings, comments, ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1120-rule-4-cold-pass-queued-personal-data-closed-list.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/630-rule-4-cold-pass-queued-pii-by-purpose.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`920cfed1`: read body-free yes/no,
findings by id), findings with stable ids (prefix `PCL`: `PCL1`, `PCL2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger (commands and results, children by count only) and a follow-up checklist. Then STOP: act 1 is
committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

