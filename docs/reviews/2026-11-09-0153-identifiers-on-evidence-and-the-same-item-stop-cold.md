# Cold pass — ccclose --identifiers credits on evidence (160/960), and a peer's edits stop only a claim of the same item (010/160, 160/260)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: a close-out instrument and a concurrency rule every session reads).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1170-rule-4-cold-pass-queued-identifiers-on-evidence-and-the-same-item-stop.md`
(barred until phase 2).
**Size:** large: two unrelated subjects in one pass. One is 757 added lines of instrument code,
tests, design note and man page; the other is 169 added lines of doctrine, an ADR amendment and the
board tool's docstring.
**Why it earns a review:** `ccclose --identifiers` credits commits to a session in close-out
records, so a false credit is a false record. The claim rule decides when a session may start beside
a live peer, so a wrong narrowing lets two sessions take one item.

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

The principal's answer on `160/960`, 2026-11-09, verbatim: *"Credit only on evidence"*. The option
read: `ccclose --identifiers` lists a commit only where the session's own transcript shows it made
it, and shows anything uncertain as uncertain. The principal's answer on `010/160`, the same day,
verbatim: *"Stop only for the same item"*. The option read: a session still works in its own
worktree and stops only where a peer's unsaved changes touch the item it wants; claiming a different
item beside a live peer is allowed. That answer also covers `160/260`'s BA1.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Two commits on `main`, on two subjects: `4e3b3984` (`ccclose`) and `2744f6aa` (the claim rule, with
the board tool's docstring and an ADR amendment). The second also touched one session record, which
stays barred, so scope to the paths below.

Commits on `main`: `4e3b3984`, `2744f6aa`. The landing commit is `2744f6aa`. **Check your tree has
it before reading anything:** `git merge-base --is-ancestor 2744f6aa HEAD` exits 0, and an
orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `instruments/ccclose`, `instruments/ccclose.test.js`, `instruments/ccclose.design.md`,
`instruments/man/ccclose.1`, `instruments/README.md`, `docs/method/RECORD.md`,
`docs/method/CONCURRENCY.md`, `tools/board.py`, `tools/README.md`, `docs/roadmap/README.md`,
`docs/decisions/2026-08-15-0610-board-store-per-item-files.md`, `CHANGELOG.md`. Read each at HEAD
and read each commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit 4e3b3984 --path CHANGELOG.md --path docs/method/RECORD.md --path instruments/README.md --path instruments/ccclose --path instruments/ccclose.design.md --path instruments/ccclose.test.js --path instruments/man/ccclose.1
python3 tools/coldsweep.py --root . --commit 2744f6aa --path CHANGELOG.md --path docs/decisions/2026-08-15-0610-board-store-per-item-files.md --path docs/method/CONCURRENCY.md --path docs/roadmap/README.md --path tools/README.md --path tools/board.py
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 2744f6aa..HEAD -- instruments/ccclose instruments/ccclose.test.js instruments/ccclose.design.md instruments/man/ccclose.1 instruments/README.md docs/method/RECORD.md docs/method/CONCURRENCY.md tools/board.py tools/README.md docs/roadmap/README.md docs/decisions/2026-08-15-0610-board-store-per-item-files.md CHANGELOG.md
```

At `457615cc` this printed 10 commit(s). Read anything new the same way.

**Application pass.** Both subjects apply the principal's answers and earlier passes' counsel. It
cannot fully honour rule 2: the delta carries finding ids and the decisions stamped on them.
Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the work at HEAD and commit
findings first; open the prior verdict after. Name that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- `ccclose`'s Commits line lists a commit only where one command of the session or its subagents
  made it: subject, repo, a non-error result and the time must all fit, one command to one commit; a
  commit command quoted in a heredoc, grep or echo is no evidence.
- What does not fit prints as unconfirmed, with why. The JSON gains fields and changes no existing
  meaning.
- The limits are written into `ccclose.design.md` §15.1, the man page, the README and `RECORD.md`.
- `CONCURRENCY.md` § *Claiming at a dirty primary checkout* (CF3): a peer's uncommitted edits stop a
  claim only where they touch the item wanted; a different item beside a live peer is claimed with
  `--rebuild --from-index`, by pathspec.
- A peer's staged entries and a monolithic board are named as the cases this does not cover.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** `ccclose` behaviour outside `--identifiers`, except where the delta changed it.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. `ccclose` parses session transcripts, which are untrusted
text with a path to a record; weigh that parse. Aim `/security-review` at the `instruments/ccclose`
diff from a clean tree, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `node --test instruments/ccclose.test.js`
- `cd tools && python3 -m unittest test_board`
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
- `ccclose` reads session transcripts: quote none, and report only counts of credited or unconfirmed
  commits from any real session you point it at.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-identifiers-on-evidence-and-the-same-item-stop-cold.deferred.md`), every delta
commit's message body, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1170-rule-4-cold-pass-queued-identifiers-on-evidence-and-the-same-item-stop.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md`
- `docs/roadmap/010-board-store-migration-per-item-files-mik/160-cf3-s-sibling-stop-is-now-stricter-than-its-cause.md`
- `docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default):
`docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.md`,
`docs/reviews/2026-09-25-0715-bw-rulings-applied-cold.md`. The delta's docstrings, comments, ADR
text, `tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are the
delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1170-rule-4-cold-pass-queued-identifiers-on-evidence-and-the-same-item-stop.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md \
  --also-exclude docs/roadmap/010-board-store-migration-per-item-files-mik/160-cf3-s-sibling-stop-is-now-stricter-than-its-cause.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`4e3b3984` and `2744f6aa`: read body-free
yes/no, findings by id), findings with stable ids (prefix `IDS`: `IDS1`, `IDS2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results, children by count only) and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

