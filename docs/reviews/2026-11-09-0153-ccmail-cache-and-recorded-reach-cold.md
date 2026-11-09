# Cold pass — ccmail's cache is private and expires, and its domain-wide reach is written down (210/130)

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a credential-holding instrument,
doctrine by function through ADR 0006's controls).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY. Not run. Held for the principal's explicit approval of the Fable pass.
Written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1200-rule-4-cold-pass-queued-ccmail-cache-and-recorded-reach.md`
(barred until phase 2).
**Size:** large: one commit, 1,191 added lines across the tool, its tests, the man page, an ADR
addendum and a Swift renderer with a build step; one tool that holds a credential and now deletes
files.
**Why it earns a review:** A tool holding a mail credential now deletes files on a sweep and states
what anyone able to run a command as the operator could read. The worst failures are a sweep that
deletes outside its own cache, or a stated reach that understates what the credential can see.

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

The principal's answer on `210/130`, 2026-11-09, verbatim: *"Keep it, lock the cache"*: the
delegated route stays and its domain-wide reach is written down; the attachment cache gets private
permissions and a 30-day expiry. The rest of the delta applies a reviewer's counsel.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

One commit on `main`, `c23fb6f1`.

Commits on `main`: `c23fb6f1`. The landing commit is `c23fb6f1`. **Check your tree has it before
reading anything:** `git merge-base --is-ancestor c23fb6f1 HEAD` exits 0, and an orchestrator merges
`origin/main` into the review branch before it spawns.

Delta paths: `instruments/ccmail`, `instruments/ccmail.test.js`, `instruments/man/ccmail.1`,
`instruments/README.md`, `instruments/ccpdf/pdfrender.swift`, `instruments/ccpdf/selftest`,
`docs/decisions/0006-instruments-in-atelier.md`, `CHANGELOG.md`. Read each at HEAD and read each
commit body-free, scoped to paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit c23fb6f1 --path instruments/ccmail --path instruments/ccmail.test.js --path instruments/man/ccmail.1 --path instruments/README.md --path instruments/ccpdf/pdfrender.swift --path instruments/ccpdf/selftest --path docs/decisions/0006-instruments-in-atelier.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline c23fb6f1..HEAD -- instruments/ccmail instruments/ccmail.test.js instruments/man/ccmail.1 instruments/README.md instruments/ccpdf/pdfrender.swift instruments/ccpdf/selftest docs/decisions/0006-instruments-in-atelier.md CHANGELOG.md
```

At `457615cc` this printed nothing. Read anything new the same way.

**Application pass.** This delta applies the principal's answer and an earlier pass's counsel. It
cannot fully honour rule 2: the delta carries finding ids and the decisions stamped on them.
Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the work at HEAD and commit
findings first; open the prior verdict after. Name that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- ADR 0006's 2026-11-09 addendum, `man ccmail`, the README and the tool's header say what anyone
  able to run a command as the operator could read, per route.
- Cache directories are 0700 and files 0600, whatever the umask. Every working run tightens looser
  existing paths and deletes message folders untouched for 30 days, with one line on stderr.
- The sweep never follows a symlink and refuses a root that is a link, `$HOME`, `/` or in a work
  tree; tests pin each limit.
- `ccpdf` refuses an oversize page: a 64-megapixel default budget, `CCPDF_MAX_PIXELS` to adjust, a
  named error before allocation, asserted by the selftest.
- Files are created with `wx`; a message id must be hex; names are capped and bidi and control
  characters removed; requests time out after 60 seconds; the loopback consent sends `state` and a
  PKCE challenge.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** the routes' existence, which the principal's answer kept; a sandbox profile for
`ccpdf`, which the delta considered and did not build, except where a claim depends on it.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. This is the reason for this pass: a credential holder that
deletes files and parses mail content. Check it by hand and against an open catalogue (OWASP ASVS,
the file-handling and authentication chapters). Aim `/security-review` at the `instruments/ccmail`
diff from a clean tree, or discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `node --test instruments/ccmail.test.js`
- `swiftc -O instruments/ccpdf/pdfrender.swift -o <scratchpad>/pdftoppm && bash
  instruments/ccpdf/selftest <scratchpad>/pdftoppm`

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; **no live writes**. A check that
  would need a write is marked NOT RUN in the verdict, with what it would have shown. `ccmail` runs
  its sweep on every working run, `--status` included, and that deletion is a local write: **always
  run it with `CCMAIL_DEST` set to a directory under your scratchpad**, never against the real
  cache. Read no mailbox: no real message id, no `--search`. A live read of whether a route is
  authorised is the most this pass needs. Report only route names and booleans.
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
- Do not run `instruments/ccpdf/setup`: it installs onto `PATH`. Build to your scratchpad only, as
  the re-run line does.
- Print no credential, token or keychain value; never run a command that would.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the
deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the
reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
(`2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.deferred.md`), every delta commit's message
body, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1200-rule-4-cold-pass-queued-ccmail-cache-and-recorded-reach.md`,
and the intent records beyond their titles:

- `docs/roadmap/210-instruments-open-features/130-ccmail-rule-4-review-queued.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default): `docs/reviews/2026-09-25-0715-ccmail-build-cold.md`. The
delta's docstrings, comments, ADR text, `tools/README.md` and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1200-rule-4-cold-pass-queued-ccmail-cache-and-recorded-reach.md \
  --also-exclude docs/roadmap/210-instruments-open-features/130-ccmail-rule-4-review-queued.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`c23fb6f1`: read body-free yes/no,
findings by id), findings with stable ids (prefix `CCR`: `CCR1`, `CCR2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger (commands and results, children by count only) and a follow-up checklist. Then STOP: act 1 is
committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commits' bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling's questions and
the author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding on this delta is the principal's to decide (rule 3): record all, apply nothing.
Counsel per finding is welcome, labelled as counsel and kept beneath it.

