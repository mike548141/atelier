# Cold pass — ccmail's cache is private and expires, and its domain-wide reach is written down (210/130)

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a credential-holding instrument,
doctrine by function through ADR 0006's controls).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** RUN. Act 1 (phase 1) written 2026-11-22 UTC by a Fable 5.1 reviewer under the
orchestrator of drain session `eca14b23`; verdict FAIL (1 MAJOR, 2 MODERATE, 4 minor, 1 note). Act
2 (reconcile) written 2026-11-22 UTC by the same reviewer after the sibling's release; the
verdict stands unchanged. Sibling and review log folded below by the orchestrator, 2026-11-22.
Brief written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
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
(`2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.deferred.md`, now folded
below the verdict and removed), every delta commit's message
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


---

## Verdict — act 1 (phase 1), 2026-11-22 UTC

**Overall: FAIL — 1 MAJOR, 2 MODERATE, 4 minor, 1 note (CCR1–CCR8).** Every finding is the
principal's to decide (rule 3): recorded, nothing applied. Counsel sits beneath each finding,
labelled.

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection.
- **Spawn:** a headless per-pass orchestrator session (Opus 5.5), itself started by drain session
  `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators holding the context partition; they
  formed no finding and wrote no severity. Drain session `eca14b23` wrote no brief and no delta and
  started no brief-writer for this pass. The reviewer was not started or instructed by `722ac2e2`,
  any worker it dispatched, `d16dc612` or `74f2b8cd` (the brief's barred set).
- **Approval:** the principal's drain order, 2026-11-23 NZDT, verbatim: *"Start a fable drain or
  whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*. The pass started
  2026-11-22 19:55 UTC, before the approval lapsed at the reset (2026-11-22 23:00 UTC).
- **What the orchestrator told the reviewer:** process only (paths, the barred set, what may be
  written, the live-systems rule, load limits, the deliverable's shape, the release timing). It
  carried no question about the delta, no pointer to where the risk lives and no request about a
  finding. The spawn prompt is attached in full to the review log named below, which the fold
  appends here. Contact after the spawn: none.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1200-1953/atelier`, HEAD `f5e4802e` =
  `origin/main`; `git merge-base --is-ancestor c23fb6f1 HEAD` exit 0. The delta is one commit,
  `c23fb6f1`; the moving bound is pinned at `f5e4802e`. The sibling `.deferred.md` was removed from
  the worktree before the spawn (the one line in `git status`) and was not sought anywhere.
- **What was read:** the brief whole; `docs/method/REVIEW.md` (rules 1–4, lenses, re-run rule,
  V1–V7, the application-pass clause, the deliverable list); the delta via `coldsweep --commit
  c23fb6f1 --path …` (subject, stat, diff; no body; no board file); the three later commits that
  touch `instruments/ccmail` and its man page (`9fc40236`, `5a90b0d4`, `5914535b`) the same way;
  `instruments/ccmail` at HEAD whole, `instruments/ccmail.test.js`, `instruments/man/ccmail.1`,
  `instruments/README.md` §ccmail and §Install, `docs/decisions/0006-instruments-in-atelier.md`
  lines 143–358, `instruments/ccpdf/pdfrender.swift`, `instruments/ccpdf/selftest`,
  `docs/method/SECRETS.md` §triad. Not opened: `docs/sessions/`, `docs/SESSIONS.md`, any file in
  `docs/reviews/` other than this one, the queue pointer, the intent record, any commit body.
- **Residual exposure, named (application pass):** the delta carries the prior pass's finding ids
  (CC1–CC13) and the author's one-line account of each in `CHANGELOG.md`, the ADR addendum and
  code comments. Those are the delta and were read; the prior verdict file was not. The harness
  loaded user-level and repo instruction files and a memory index before the brief; none names
  this delta's content. Every tree sweep ran through `coldsweep` with both board items
  `--also-exclude`d (828 files barred); `--include-barred` was not used.
- **Review log:** `~/.claude/fable-drain/notes/atelier-160-1200-1953.md` (commands, reads,
  probes, the spawn prompt). Probes and fixtures lived under the session scratchpad and were
  deleted at the end of the act.

### The acceptance test

The principal's pick, *"Keep it, lock the cache"*, has two parts and both are built: the
delegated route stays, its reach is written in four places (ADR addendum, man page, README, the
tool's header); the cache is created 0700/0600, tightened on every run and swept at 30 days. The
rest of the delta applies the earlier reviewer's counsel. Two places go past the pick and are
recorded under CCR7: a new standing requirement on every future credential-holding instrument,
and a code comment that calls the 30-day figure *"the operator's ruling"* where the ADR itself
calls the pick an answer to an offered option.

### Lens 1 — approach and assumptions (named first, then damaged or confirmed)

| # | Load-bearing assumption | Result |
| --- | --- | --- |
| A1 | The sweep's root is always `ccmail`'s own cache | **Damaged.** `defaultDest()` returns `CCMAIL_DEST` unchanged and `main` sweeps it; probe deleted four operator folders → CCR1 |
| A2 | 0700/0600 "locks" the cache against the adversary the delta names | **Damaged by reading.** The named adversary runs *as the operator*; mode bits do not bind it. Only the expiry bounds that exposure → CCR6 |
| A3 | Newest mtime stands for "last used" | **Damaged.** Reads never renew; an identical re-fetch is reused without a write and does not renew either (probe) → CCR4 |
| A4 | A lowercase-hex name under the root is one `ccmail` made | **Holds under the default root; fails under A1.** `ID_RE` admits 1–64 hex characters; Gmail ids are 16. `1`, `2024`, `cafe` match → part of CCR1 |
| A5 | The reach statement is on every surface the tool speaks from | **Damaged.** Four stale sites in `instruments/ccmail`, two in ADR 0006's 2026-09-09 amendment, one in its controls list → CCR2 |
| A6 | Every limit on the sweep is pinned by a test | **Holds, less one.** Symlink root, `$HOME`, work tree, symlink entry, loose file, stray name: each tested. The `/` refusal is untestable and is the one limit read, not run |
| A7 | The pixel budget protects the file reader | **Damaged for this machine.** The installed renderer predates the delta → CCR3. The source and the scratch build hold (re-run) |
| A8 | PKCE and `state` close the loopback race | **Confirmed by reading and unit tests;** the live consent is a write and was NOT RUN (see re-run ledger) |

Right problem, right altitude: the pick was applied at the altitude asked. The one altitude point
is A2: "lock" buys protection against other local accounts and backup readers, not against the
adversary the same addendum defines, and the record should say which (CCR6).

### Lens 2 — correctness and quality

Claims the brief extracted, each re-driven:

- *Reach stated on ADR, man, README, header, per route* — true of the four named passages;
  false of the same files' other passages (CCR2), and the `--help` text says the opposite.
- *0700/0600 whatever the umask; every run tightens and deletes at 30 days; one stderr line* —
  confirmed by the unit suite (67/67) and by the whole-tool probe: `--status` with no route
  printed the one line and tightened the root. The deletion is by newest write time, which the
  man page states exactly and the README, `--status` and the code comment loosen to "untouched"
  (CCR4).
- *Never follows a symlink; refuses a link, `$HOME`, `/`, a work tree* — confirmed (tests, code).
  The refusal list does not include an operator-chosen directory (CCR1).
- *`ccpdf` refuses an oversize page before allocation* — confirmed in the source (check precedes
  `CGContext`) and the scratch build (selftest cases 4–6); not true of the installed binary
  (CCR3).
- *`wx` creation, hex id, byte caps, bidi/control removal, 60 s timeout, `state` + PKCE* — all
  confirmed in code and tests. Two overstatements: "requests time out after 60 seconds" is an idle
  timeout (CCR8), and "removed from names and listings" leaves the listing's sender lines raw
  (CCR5).
- *Overtaken, not built: CC10* — the live read (route names and booleans only) found the
  delegation route **not live** and the keychain route **live** on 2026-11-22. So the credential
  carrying the tool on that day is the one-mailbox token the addendum says is one `security`
  command away; the domain-wide statement describes the preferred route, which was dark. This is a
  fact for the record, not a finding on the delta; the delta's `--status` is what made it visible.

Honest about done versus stubbed: yes. The ADR names what was considered and not built (sandbox
profile, subject check) with reasons, and the changelog names the three findings not applied.

### Lens 3 — completeness and harvest

- **V3 mirror sweep:** incomplete (CCR2). The delta edited the header's first paragraph and left
  the file's other three statements of "stores nothing / adds nothing / your own mailbox and
  nothing else", and in the ADR marked the withdrawn fallback line but not the amendment's
  "stores nothing at all" bullet or the controls list's "cannot … reach another mailbox".
- **One home (V4):** the new per-route requirement lives only in the 2026-11-09 addendum; the
  precedent clause future builders are pointed at ("inherits these four controls") still lists
  four (CCR7). `SECRETS.md`'s least-privilege leg speaks of blast radius and does not carry it.
- **Tests that would stay green on a broken check:** none found. Each sweep-limit test asserts
  the protected object survives, so removing the guard fails the test. The umask test runs at
  `umask 000`. The `CACHE_DAYS === 30` test pins a number, which is what it is for.
- **What already existed and was ignored:** the test suite's own hygiene. Only one spawn test
  deletes `XDG_CACHE_HOME` and `CCMAIL_DEST` from its environment; the id-refusal and `--get`
  tests inherit them, so a developer with `XDG_CACHE_HOME` set sweeps their real cache by running
  the tests (CCR8).
- **Later commits on the surface:** `--headers` (`9fc40236`, `5a90b0d4`) writes into the same
  cache and so inherits CCR1's reach when `CCMAIL_DEST` is set; no separate finding.

### Lens 4 — security and privacy (V6)

Checked by hand against OWASP ASVS V12 (file and resource handling) and Google's native-app
OAuth guidance, with the probes below. `/security-review` was discharged by grounds: it reads the
session's pending diff, which here is only the removed sibling; the delta's 1,191 lines were read
and probed directly instead, and the skill's finding-forming would be this reviewer's in any case.

- *Path traversal and name injection:* `requireMessageId` gates every id an operator supplies
  before a URL or path splice; `safeName` strips separators, controls, bidi overrides and leading
  dots, caps bytes and the extension. Sound.
- *Symlink and TOCTOU on write:* `wx` with 0600, then `lstat` and a byte compare on `EEXIST`.
  Sound. On delete: `lstat`, then not a link, then `realpath` parent equals root, then `rmSync`;
  `rmSync` does not follow a link inside the folder (test). Sound for the default root.
- *Permissions:* 0700/0600 at creation (umask can only tighten) and on every run. Sound as a
  control against other local principals; not a control against a same-user process (CCR6).
- *Deletion reach:* the root is whatever `CCMAIL_DEST` names (CCR1). The brief's named worst
  failure is reachable with a documented environment variable.
- *Resource bounds:* 64 Mpx page budget before allocation; `unzip -p` into a 256 MiB buffer;
  60 s idle timeout. Bounded. A hostile PDF carrying `/OpenAction` Launch, a page-open Launch and
  a JavaScript action rendered to a JPEG and ran nothing (probe), re-confirming the ADR's claim.
- *Authentication:* S256 PKCE (64-char verifier), 24-byte `state`, a callback without the state
  answered 400 and the server keeps waiting; `code_verifier` sent at exchange. Sound. The client
  secret and refresh token are readable by one `security` command as the operator: stated, per
  route, as the pick required.
- *Output to the terminal:* filenames and `--headers` values are scrubbed; `--search` rows and
  the list header print Subject/From/Date raw (CCR5).
- *Privacy of the record:* no secret, token, account or message id was printed by any probe;
  the live read was filtered to route names and booleans and its captures deleted.

### The standing checklist

- **V1** — CCR2 (`--help`: "your own mailbox and nothing else"), CCR3 (a control true of the
  source, not of the deployed binary), CCR4, CCR5, CCR8.
- **V2** — both re-run lines re-run (ledger below); the ADR's PDFKit claim re-run with a hostile
  PDF; the sweep's reach and the renewal claim probed; route liveness read live.
- **V3** — CCR2.
- **V4** — CCR7 (a fifth control outside the four-control precedent clause).
- **V5** — CCR1 (man: a chosen dest "is never swept" versus behaviour), CCR2 (`--help` and ADR
  controls list versus the addendum), CCR7 ("ruling" in code versus "answer" in the ADR).
  Cross-references checked for the rule reached: `--status` points at `man ccmail,
  AUTHORISATION`, and §*What the routes reach* is a subsection of that section; the README's
  "2026-11-09 addendum" and the header's "ADR 0006's 2026-11-09 addendum" reach the addendum
  that holds the reach table.
- **V6** — lens 4 above.
- **V7** — stated above; repeated from the brief's provenance, with the spawn prompt attached.

### Findings

**CCR1 — MAJOR — The sweep deletes under any directory `CCMAIL_DEST` names, and the man page
says the opposite.** `defaultDest()` returns `CCMAIL_DEST` as the root and `main` runs
`cacheHygiene` on it before every command, `--status` included. Probe (review log, *probe-dest*):
a directory holding folders `2024`, `1`, `cafe`, `deadbeef` and `Invoices`, each unwritten for
40 days, set as `CCMAIL_DEST`; `ccmail --status` with no route exited 1 and its stderr read
`cache  made 1 path(s) private; removed 4 message folder(s) not touched for 30+ days`; only
`Invoices` remained and the directory was made 0700. The guards (symlink, `$HOME`, `/`, work
tree) do not cover an operator's downloads folder, and `ID_RE` admits one to sixty-four hex
characters where a Gmail id is sixteen, so year and single-digit folder names qualify. The man
page's WHERE FILES LAND says *"A --dest you choose is not part of the cache: it is never swept"*
and its ENVIRONMENT entry describes
`CCMAIL_DEST` only as *"Base directory for downloads, replacing the cache default"*; the ADR says
the sweep touches *"only real directories named as message ids directly under the cache root"*.
This is the brief's named worst failure (a sweep that deletes outside its own cache), reachable
with a documented knob, undocumented, and irreversible. The brief's own house rule, which told this
reviewer to point `CCMAIL_DEST` at scratch, shows the knob is in use.
*Counsel:* sweep only a root `ccmail` itself created (a marker file written at first use, or the
two default roots `~/.cache/ccmail` and `$XDG_CACHE_HOME/ccmail`), never a root an environment
variable supplied; tighten `ID_RE` to the sixteen-character shape where a name is to be deleted;
state in the man page's ENVIRONMENT entry whether `CCMAIL_DEST` is swept; add the probe as a test.

**CCR2 — MODERATE — The reach statement did not reach every surface the delta says it did; the
tool's own `--help` still says the opposite.** `instruments/ccmail` at HEAD: line 39 *"Route 1 has
no secret"*; lines 235–237 *"This route is preferred because it adds NOTHING: no new grant, no new
stored secret"*; lines 394–396 *"try the route that stores nothing … adds no credential to the
estate at all, so when it works there is nothing to keep, rotate or lose"*; and the `--help`
NOTES, line 1422, *"Access is read-only (gmail.readonly) on your own mailbox and nothing else"*,
which is the first text an operator reads and contradicts the header's *"reaches EVERY mailbox in
the domain"*. ADR 0006: the 2026-09-09 amendment's bullet *"The preferred route stores nothing at
all"* (line 202, and line 210) and the controls list's *"It cannot send, reply, label, delete, or
reach another mailbox"* (line 165) stand unmarked, while the same delta marked the fallback line
two bullets below *"withdrawn by the amendment below"*, so the form was known. The changelog claims
the header says the reach; it does in one paragraph and denies it in three.
*Counsel:* sweep the file and the ADR with the same marker form; change the NOTES line to state
the route's reach or drop the clause.

**CCR3 — MODERATE — The pixel budget is not in the renderer this machine runs.** The installed
`pdftoppm` under `~/.local/bin` is a plain binary last modified 2026-09-09 (local time), two
months before the delta. The changelog and README say *"Re-run `instruments/ccpdf/setup` to put the
new build on PATH"*; nothing ran it, nothing checks it, and the file reader shells out to the old
build, so the 104-second, 4.4 GB page the review measured is still what a hostile attachment buys
on this machine. The claim *"`ccpdf` refuses an oversize page"* is true of the source and the
scratch build (re-run) and false of the deployed tool. Setup was not run by this pass (barred).
*Counsel:* the principal runs `instruments/ccpdf/setup` once; then make the gap visible, by having
`instruments/install` rebuild `ccpdf` when the source is newer than the binary, or by a check that
compares the installed binary's date with the source.

**CCR4 — minor — "A re-fetch into a folder renews it" is false for the common re-fetch.**
`writePrivate` reuses a file whose bytes match without writing, so neither the file's nor the
folder's mtime moves. Probe (*probe-renew*): a folder aged 29 days, re-fetched with identical bytes
on day 29, was deleted by the sweep on day 31. A read by the Read tool renews nothing either. The
man page says "nothing has been written for 30 days", which is exact; the README, `--status` and
the code comment above `newestMtime` say "untouched", which is not. Impact: a refetch.
*Counsel:* touch the folder's mtime when a file is reused, or say "unwritten" everywhere.

**CCR5 — minor — Sender-controlled Subject/From/Date lines print unscrubbed.** `cmdSearch`
(lines 1117–1118) and `cmdList` (line 1134) write the sender's strings straight to the terminal;
the same delta scrubbed bidi and control characters from filenames (`printable`) and the
changelog says *"removed from names and listings"*. An escape sequence in a subject reaches the
operator's terminal on `ccmail --search` and `ccmail <id>`. Read-confirmed; the strings are fixed
templates.
*Counsel:* pass the three header values through `printable` (or the `--headers` scrub).

**CCR6 — minor — The lock is credited against an adversary it cannot stop.** The addendum's
threat table answers *"The cache holding other people's mail at rest"* with 0700/0600 and the
30-day sweep. The same addendum's adversary is *"anyone able to run a command as the operator"*,
and mode bits do not bind a process running as the operator: every session on the machine reads
the cache. What the modes buy is protection from other local accounts and from backup or sync
tooling that honours them; what bounds the stated adversary is the expiry alone. The credential
row says *"Not prevented: stated above"*; the cache row should be as plain.
*Counsel:* one clause in the table row naming what the lock does and does not stop.

**CCR7 — minor — Two statements go past the pick and read as his.** (a) *"Required of every
future credential-holding instrument: its ADR entry carries a line stating what a compromised
session … can read with it, per route"* is a standing control on future work, written by the
applier, sitting beneath the paragraph headed *"Decision (the principal, …)"*, and restated in the
changelog without attribution; it is also not in the controls list the precedent clause points
at (*"inherits these four controls"*), so a future builder reading the clause does not meet it.
(b) `instruments/ccmail` line 93: *"30 days is the operator's ruling (2026-11-09), not a default"*,
where the ADR says the pick *"is an answer to a choice put to him, not a new ruling in his own
words"* and the 30 days came from the option text. Both are doctrine by function (rule 3) and are
his to confirm, which this pass puts to him.
*Counsel:* attribute (a) to the applier and ask; fold it into the controls list once confirmed;
change (b) to "the answer he gave".

**CCR8 — note — Two small overstatements and a test-hygiene gap.** (a) *"requests time out after
60 seconds"* (changelog, and the brief's claim list) is an idle timeout on the socket; a response
that trickles is not bounded. The ADR's table says "idle" and is right. (b) Only the whole-tool
hygiene test deletes `XDG_CACHE_HOME` and `CCMAIL_DEST` from its environment; the id-refusal and
`--get` spawn tests inherit them, so running the suite with `XDG_CACHE_HOME` set sweeps the real
cache. (c) The `/` refusal is the one sweep limit no test can pin.

### Per-commit ledger

| Commit | Read body-free | Findings |
| --- | --- | --- |
| `c23fb6f1` (the delta) | yes, `coldsweep --commit`, 8 paths, 0 board files | CCR1–CCR8 |
| `9fc40236` (`--headers`, after the delta) | yes | none formed; inherits CCR1 under `CCMAIL_DEST` |
| `5a90b0d4` (`--headers` list) | yes | none |
| `5914535b` (man wrap) | yes | none |

### Re-run ledger (uptime checked before each; heavy lines under `nice -n 10`, one at a time)

| Line | Result |
| --- | --- |
| `CCMAIL_DEST=<scratch> node --test instruments/ccmail.test.js` (node 24.18.0) | exit 0; 67 tests, 67 pass, 0 fail, 0 skipped |
| `swiftc -O instruments/ccpdf/pdfrender.swift -o <scratch>/pdftoppm` | exit 0 |
| `bash instruments/ccpdf/selftest <scratch>/pdftoppm` | exit 0, *"pixel budget enforced"* (four CoreGraphics notices from the sed-edited fixtures) |
| `mandoc -T lint -W style instruments/man/ccmail.1` | exit 0, silent |
| Hostile PDF (Launch + JavaScript actions) through the scratch build | exit 0, rendered, marker file not created |
| Sweep against a `CCMAIL_DEST` directory (probe) | 4 of 5 folders deleted, root made 0700 (CCR1) |
| Identical re-fetch, then sweep two days on (probe) | folder deleted (CCR4) |
| Live read, `ccmail --status --json` with `CCMAIL_DEST=<scratch>`, filtered to names and booleans | authorised true; delegation live **false**; keychain live **true**; `retentionDays` 30 |
| Installed renderer's modification date | 2026-09-09, before the delta (CCR3) |
| NOT RUN: `ccmail --auth` (mints a grant: a write); `instruments/ccpdf/setup` (barred); `/security-review` (discharged by grounds, lens 4) | would have shown the live consent round-trip; the installed budget; nothing the hand pass did not |

Children: none read; none needed.

### Follow-up checklist (for the principal's decisions, rule 3)

1. CCR1: decide the sweep's reach; until then, no `CCMAIL_DEST` pointing at a shared folder.
2. CCR3: run `instruments/ccpdf/setup` once, and decide whether install should keep it current.
3. CCR2, CCR4, CCR5, CCR6, CCR8: wording and small code changes, one application commit.
4. CCR7: confirm or decline the standing per-route requirement in his own words, and the
   30-day attribution.
5. Phase 2 of this pass: reconcile against the sibling, then fold.

*Act 1 ends here. Nothing above is revised in act 2.*

### Reconcile (act 2, phase 2, 2026-11-22 UTC)

Opened after act 1 was committed (`00b8e4b5`), on the orchestrator's release message, which
named one path and nothing else: the held sibling (one pointer block, three questions, two
facts, the brief-writer's re-run results), the delta commit's message body, the queue pointer
`160/1200`, the intent record `210/130`, and the prior verdict
`docs/reviews/2026-09-25-0715-ccmail-build-cold.md` (its findings CC1–CC4, CC9, CC10 and its
reconcile notes on CC1 and CC2). Not opened: `docs/sessions/`; nothing there was needed to
reconcile and the brief's barred list is honoured by default.

**The sibling's questions, answered against act 1.**

- *Pointer: can the sweep delete anything outside its own cache?* Yes: CCR1, formed in act 1
  before this question was read. The author's commit body lists the refusals (link, home, root,
  work tree) and says tests pin them; it is silent on `CCMAIL_DEST`, which is the route.
- *Pointer: is the threat table complete?* Two gaps, both act-1 findings: the cache row credits
  a lock against an adversary it does not bind (CCR6), and no row covers the sweep's root being
  supplied from the environment (CCR1). The unscrubbed listing lines (CCR5) are a near miss of the
  filename row rather than a missing row.
- *Brief-writer 1: is every sweep limit pinned by a test that fails if the limit is removed?*
  Yes, less one: lens 3 and A6 in act 1. The `/` refusal is read, not run; no test can own `/`.
- *Brief-writer 2: `rmSync` on a directory, a symlink swapped in during the walk.* Answered by
  reading `cacheHygiene`: the entry is `lstat`ed (a link is skipped), then resolved with
  `realpathSync`, then its resolved parent must equal the resolved root, and `rmSync` is handed
  the **resolved** string, never the entry's name. A swap before resolution is caught by the
  parent check; a swap after it changes nothing, because the deletion is addressed by a real path
  under the root; and `rmSync` unlinks a link met inside the tree rather than following it (the
  act-1 test re-run). What the check buys is that no name under the root can steer the deletion
  outside the root. The residual is a same-user race on the contents of a folder already judged
  expired, by a principal who could delete them directly. No finding.
- *Brief-writer 3: does the stated reach hold for the identity the cloud login actually carries,
  and is that checkable read-only?* Not checkable from this repository: the reach is a statement
  about the identity's registration in the Workspace admin console, which neither `ccmail` nor
  anything in the tree can read. A live read of the admin API would print estate facts and was
  not needed for any finding, so it was NOT RUN. The act-1 live read did establish that the route
  the statement describes was **not live** on 2026-11-22 while the one-mailbox keychain route was,
  which is the fact a reader of the reach statement needs beside it.

**The held facts.** Both were found independently in act 1: the sweep's run on every working
command including `--status` is A7 and is the lever CCR1's probe used; the registry entry owed
outside this repository is noted under the acceptance test and CCR7 and raises nothing new. The
brief-writer's re-run counts (62 tests at `457615cc`) differ from act 1's 67 by the five tests
the later `--headers` commits added.

**Per finding, against the author's account and the prior verdict.**

- **CCR1 — stands, MAJOR.** The author anticipated the class (the pointer's first question) and
  answered it for four roots; `CCMAIL_DEST` is a fifth, documented in the same man page the
  commit body cites, and it is the one the probe used. The prior verdict asked for the lock and a
  documented clear (CC2); the sweep is the applier's design, so the reach of its root is the
  applier's to have bounded.
- **CCR2 — stands, MODERATE; the prior verdict strengthens it.** Its reconcile quotes the
  2026-09-09 record's strongest form of the claim, *"adds no credential to the estate at all"*,
  as the sentence CC1 was about. That sentence stands verbatim in `instruments/ccmail` at HEAD
  (lines 395–396), two months after the finding and in the file the delta edited to answer it.
- **CCR3 — stands, MODERATE.** The prior CC4 was found on a fresh build from HEAD; the applier
  fixed the source and wrote "re-run setup" in two places; the installed binary is still the one
  CC4 measured. The prior CC10 was the same class, an owed operator step (then `--auth`) left
  undone for seventeen days; this one is at fourteen. Counsel unchanged: make the deployed state
  checkable rather than owed.
- **CCR4 — stands, minor.** Not anticipated anywhere. The intent record's answer line says
  "a 30-day expiry"; the man page's "nothing has been written for 30 days" is the exact meaning.
- **CCR5 — stands, minor.** The prior CC5 and CC11 asked for the name scrub; the applier's
  changelog widened the claim to "listings" without widening the code.
- **CCR6 — stands, minor, with its frame corrected.** The prior CC2 named the threat as
  world-readable files under a 022 umask, that is, other local principals, and the lock answers
  that threat exactly as counselled. The finding is only that the addendum's table places the row
  under an adversary heading (a compromised session as the operator) the lock does not bind, and
  should say which adversary it does.
- **CCR7 — stands, minor; its origin is now known.** The standing per-route requirement is the
  prior reviewer's *recurrence prevention* under CC1, which said it should join *"the ADR's
  controls list for future credential-holding instruments"*. The applier wrote it as a paragraph
  of the addendum and left the controls list at four, so the counsel was applied in substance and
  not in the place it named (V4), and the commit body states it as a bare "must". The principal's
  answer covered the reach being written down; the requirement on future instruments was never
  put to him, so it stays his to confirm. The 30-day figure is the option text's, as the intent
  record's answer line shows.
- **CCR8 — stands, note.** CC11 asked for "a `request()` timeout"; the idle timeout is a fair
  reading of it, and only the changelog's wording overstates.

**Prior findings as applied, checked where act 1 reached them.** CC1: written down, four places
(CCR2 for the remnants). CC2: lock and sweep built (CCR1, CCR4, CCR6 on the design). CC3: table
present (CCR6 on one row). CC4: built in source (CCR3 on deployment). CC5, CC6, CC7, CC8, CC11:
confirmed in code and tests. CC9: the fallback line marked; the registry entry owed, disclosed.
CC10: overtaken; the keychain route was live on 2026-11-22 and the delegation route was not.
CC12, CC13: records, not reached.

**Screening the commit body.** It carries the author's account only: the pick, the finding ids
and one line each. Nothing in it names a reviewer, a question for this pass, or contact with
this review chain. The queue pointer's claim block discloses the orchestrator shape as rule 4
requires. No finding was formed at reconcile.

**Overall, restated: FAIL — 1 MAJOR (CCR1), 2 MODERATE (CCR2, CCR3), 4 minor (CCR4–CCR7),
1 note (CCR8).** Every finding is the principal's to decide (rule 3); nothing was applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (`00b8e4b5`, local, landed
with this fold); folded here verbatim (headings demoted two levels) and the sibling file removed,
per the brief. The orchestrator, a headless Opus 5.5 session started by drain session `eca14b23`,
held the partition, formed no finding and wrote no severity; drain session `eca14b23` wrote no
brief and no delta and started no brief-writer for this pass.*

### Deferred reading for `2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

#### The queue pointer's questions (the author's framing, verbatim)

> whether the sweep can delete anything outside its own cache; whether the addendum's threat table
is complete.

#### The brief-writer's questions

1. Is every limit the sweep's comment names pinned by a test that would fail if the limit were
removed?
2. `rmSync` on a directory, a symlink swapped in during the walk: what does the real path check buy
at that moment?
3. Does the stated reach hold for the identity the cloud login actually carries, and is that claim
checkable read-only?

#### What the brief-writer held back

- The sweep runs on every working run, `--status` included (`instruments/ccmail`, the housekeeping
  block); there is no separate command.
- The changelog says a private-registry entry is owed outside this repository.

#### Re-run results (2026-11-09 UTC, at `457615cc`)

`ccmail.test.js`: 62 tests, 62 pass, exit 0. `swiftc` build to scratch: exit 0. `ccpdf/selftest`:
exit 0, "selftest ok". No live `ccmail` run was made by the brief-writer.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels; three lines over 100 columns wrapped, and in one of
them the orchestrator's session-scratchpad path shortened to `<scratchpad>`. No public-repo gate
blocked a token, so no placeholder was otherwise needed.*

### Review log: atelier 160/1200, ccmail cache + recorded reach cold pass

Reviewer: Fable 5.1 (claude-fable-5-1), spawned by a headless per-pass orchestrator (Opus 5.5),
itself started by drain session eca14b23.
Worktree: /Users/mike/worktrees/fable/atelier-160-1200-1953/atelier
Brief: docs/reviews/2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.md
Scratch: <scratchpad>/reviewer/ (the orchestrator's session scratchpad)

#### Act 1

- 2026-11-22T19:55Z read the brief whole (lines 1-219).
- `git merge-base --is-ancestor c23fb6f1 HEAD` exit 0. HEAD = origin/main = f5e4802e.
  `git status --short`: only ` D docs/reviews/...deferred.md` (expected partition removal).
- `git log --oneline c23fb6f1..HEAD -- <delta paths>`: ~90 commits touch the paths since the delta
  (mostly CHANGELOG.md); on ccmail itself: 9fc40236 (--headers), 5a90b0d4 (--headers names system
  and content type), 5914535b (man wrap). Will read these commits body-free via coldsweep.
- uptime load 10.80 at start; heavy lines under nice -n 10, one at a time.
- Read docs/method/REVIEW.md: lines 25-300 (rules 1-4), 302-340 (lenses), 394-460 (re-run, V1-V7),
  530-560 (application pass), 760-818 (deliverable shape).
- `python3 tools/coldsweep.py --root . --commit c23fb6f1 --path <8 delta paths>` exit 0 -> scratch
  delta.diff, 1775 lines; read whole. Footer: body not printed, 0 board files, 0 barred files.
- Now reading instruments/ccmail at HEAD whole, ccmail.test.js, man page, README section, ADR 0006,
  and the 3 later ccmail commits (9fc40236, 5a90b0d4, 5914535b) body-free.
- Read instruments/ccmail at HEAD: lines 1-600, 1000-1250, 1380-1507 (header, config, keychain,
  routes, resolver, api, names, cache sweep, consent, status, get, headers, main).
- Body-free reads of the later commits on the delta's paths: 9fc40236 (--headers, 288 lines),
  5a90b0d4 (header list, 126 lines), 5914535b (man wrap, 23 lines). All exit 0, body not printed.
- Read ADR 0006 lines 150-222 (controls list, 2026-09-09 amendment) and headings; man page .SH/.SS
  map (What the routes reach is .SS under .SH AUTHORISATION, lines 151-186); man ENVIRONMENT
  lines 436-451 (CCMAIL_DEST: "Base directory for downloads, replacing the cache default", silent
  on the sweep); README lines 100-125, 686-700, 712.
- Test suite exposure check: grep spawnSync/PATH/HOME in ccmail.test.js: every spawn of the tool
  sets HOME=<tmp>, PATH=/nonexistent, CCMAIL_CONFIG=<none>; in-process keychain tests use fake
  spawn results. Only the 'every working run tidies' test deletes XDG_CACHE_HOME/CCMAIL_DEST from
  its env; the id-refusal and --get tests inherit them (sweep lands on CCMAIL_DEST if set).
- coldsweep tree sweep (-i 'stores nothing|adds nothing|...|your own mailbox and nothing else',
  both board items --also-exclude): stale wording at instruments/ccmail:39, :235, :394-396, :1422
  (HELP: "on your own mailbox and nothing else"); ADR 0006:202, :210 (2026-09-09 amendment bullet
  "The preferred route stores nothing at all", unmarked). 828 files excluded as barred.
- RE-RUN 1: `CCMAIL_DEST=<scratch>/ccmail-dest nice -n 10 node --test instruments/ccmail.test.js`
  exit 0; tests 67 pass 67 fail 0 skipped 0 (node v24.18.0). Load 4.6 at start. Scratch dest was
  chmod'd to 0700 by the run (the sweep ran on CCMAIL_DEST).
- RE-RUN 2: `nice -n 10 swiftc -O instruments/ccpdf/pdfrender.swift -o <scratch>/pdftoppm` exit 0;
  `nice -n 10 bash instruments/ccpdf/selftest <scratch>/pdftoppm` exit 0, "selftest ok ... pixel
  budget enforced" (4 CoreGraphics error lines on stderr, from the sed-edited PDFs).
- `mandoc -T lint -W style instruments/man/ccmail.1` exit 0, no output.
- PROBE renew (scratch probe-renew.js, requires the worktree ccmail as a module): write x.pdf,
  age folder+file 29 days, re-fetch identical bytes via writeAttachments -> file reused, newest
  mtime NOT renewed; cacheHygiene with now+2d removes the folder. Code comment (ccmail ~line 611,
  "a re-fetch into a folder renews it") is false for the identical re-fetch. Candidate minor.
- PROBE dest (scratch probe-dest.sh): CCMAIL_DEST=<scratch>/probe-dest holding folders 2024, 1,
  cafe, deadbeef, Invoices, each aged 40 days; HOME=<scratch>, PATH=/nonexistent, no config;
  `node ccmail --status` exit 1 (no route) and stderr `cache  made 1 path(s) private; removed 4
  message folder(s) not touched for 30+ days (<dest>)`; after: only Invoices remains; dest mode
  755 -> 700. CONFIRMS: the sweep deletes operator folders under CCMAIL_DEST. Man page: a chosen
  --dest "is never swept"; CCMAIL_DEST "Base directory for downloads, replacing the cache default".
  Candidate MAJOR (the brief's named worst failure: a sweep that deletes outside its own cache).
- LIVE READ (allowed by the brief; route names and booleans only): `CCMAIL_DEST=<scratch>
  node instruments/ccmail --status --json` exit 0, filtered by a python script to:
  authorised True; delegation live False; keychain live True; retentionDays 30; dest == scratch;
  1 stderr line (the cache line). Captures deleted. Nothing on Google changed (token mint = read).
- Installed renderer ($XDG_BIN_HOME or ~/.local/bin/pdftoppm): exists, not a symlink, modified
  2026-09-09T15:02+1200, i.e. before the delta: the pixel budget is NOT in the binary the file
  reader runs. Setup not run by me (barred). Candidate MODERATE.
- PROBE hostile PDF (scratch mk_hostile_pdf.py: /OpenAction Launch /usr/bin/touch <marker>, page
  /AA /O Launch, catalog /AA /WC JavaScript): scratch pdftoppm -jpeg -r 100 -f 1 -l 1 exit 0,
  marker NOT created, out-1.jpg written, stderr empty. ADR claim "did nothing in PDFKit" holds.
- Read pdfrender.swift 95-165: budget check (wantW*wantH > maxPixels -> fail) precedes CGContext
  creation; CCPDF_MAX_PIXELS validated finite >= 1; -r validated finite > 0. Claim holds.
- unzip bound: unzipEntry maxBuffer 256 MiB, unzipList 32 MiB (ccmail:752-764). "Bounded" holds.
- Raw listing prints: ccmail:1117-1118 (--search rows: subject, from, date) and :1134 (list header:
  subject, from, date) print sender strings unscrubbed; printable() applied to filenames only.
  Read-confirmed (deterministic template strings). Candidate minor.
- SECRETS.md grep (blast radius/least/reach): the least leg at :61-66 speaks of blast radius; no
  home for a per-route reach line there. Tree-wide coldsweep found no other surface describing
  route 1 as storing nothing beyond ADR/README/man/ccmail.
- Sound, checked: ID_RE guards every URL/path splice of an operator-given id (requireMessageId in
  cmdList/cmdGet/--headers); writePrivate wx + lstat + byte compare; mkdirSync mode 0700 (umask can
  only tighten); tightenTree skips symlinks; rmSync on a real dir only after realpath parent ==
  root; sweep refuses symlink/home/root/worktree roots (tests pin all but `/`); PKCE S256 verifier
  64 chars, state 24 bytes, callback without state answered 400 and ignored; token exchange sends
  code_verifier; idle timeout 60 s on every request; keychain exit 44 vs other failures; --status
  prints retentionDays; man page section the --status text points at exists (AUTHORISATION).
- NOT RUN: a real --auth consent (mints a grant: a write); `/security-review` (reads the session's
  pending diff, which here is only the removed sibling) discharged by a hand pass against OWASP
  ASVS V12 file handling and the OAuth native-app guidance; instruments/ccpdf/setup (barred).

##### Spawn prompt (attached per REVIEW.md rule 4; process only, no question about the delta)
The orchestrator's message to the reviewer, in full:
```
You are the cold reviewer for atelier board item `160/1200`: the rule-4 code cold pass on
`ccmail`'s private, expiring cache and its written-down domain-wide reach.

WHO YOU ARE
- Worktree (absolute; use `git -C "<worktree>"`, never `cd`): <worktree>. Double-quote every path
  in every shell command.
- Brief: <worktree>/docs/reviews/2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.md. Read it
  in full FIRST and follow it (its lenses, re-run list, house rules, barred reading, finding prefix
  `CCR`, process). Read `docs/method/REVIEW.md` for the verdict shape and the standing checklist
  V1–V7.
- Scratchpad for your probes, fixtures and builds: <scratchpad>/reviewer/ (create it). Delete your
  probes and fixtures there when you finish each act.

PROVENANCE (state this in your verdict)
- You are Fable 5.1, tier checked at selection. You were spawned by a headless per-pass
  orchestrator session (Opus 5.5), itself started by drain session eca14b23 (Opus 5.5). Both are
  rule-4 off-tier orchestrators: they hold the context partition, form no finding and write no
  severity. Drain session eca14b23 wrote no brief and no delta and started no brief-writer for
  this pass.
- The brief's barred sessions are `722ac2e2` and every worker it dispatched, `d16dc612`, and
  `74f2b8cd`. You were not started or instructed by any of them.
- You run under the principal's drain order, 2026-11-23, verbatim: "Start a fable drain or
  whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat". The approval
  lapses at the reset, 2026-11-22 23:00 UTC; a pass already running may finish.
- The worktree is at origin/main and contains the delta commit `c23fb6f1` (verified:
  `git merge-base --is-ancestor c23fb6f1 HEAD` exits 0). Re-check it yourself.

THE PARTITION
- The brief's `.deferred.md` sibling was removed from this worktree on purpose (it shows as a
  deleted file in `git status`; that is expected, do not restore it). Do not look for it in git
  history, `git show`, other checkouts, other worktrees, scratchpads, tmp, `~/.claude/fable-held/`,
  or anywhere else. Honour every rule-2 bar the brief lists (prior verdicts, sessions logs, the
  queue pointer, the intent record beyond its title, commit message bodies). The orchestrator will
  send you the sibling's path after act 1 is committed.

WHAT YOU MAY WRITE
- Only two files: (1) the brief file itself, and (2) your review log (below). Nothing else in the
  worktree. No commit, no push, no other git writes; the orchestrator commits.
- Act 1 goes below a `---` divider at the end of the brief. Update the brief's Status line to say
  the pass ran (act 1 / act 2 as appropriate); never write "fold-in owed".
- Wrap prose at ≤ 100 columns, absolute ISO 8601 dates from `date -u`, NZ English. Before
  finishing each act, run the repo's own gate on the brief, e.g. `python3 "<worktree>/tools/
  datescan.py" --root "<worktree>" "<brief path>"` (check `--help` for the exact form; also try
  spellscan/wrapscan if they exist in `tools/`) and fix your own text until clean. Verbatim source
  text that a gate flags takes an allow marker; never edit a quote.
- This repo is PUBLIC. Refer to the orchestrator and the drain session by session id only. Never
  write a session NAME, the name or path of any private repo, any path under the user's home that
  names a private repo, any estate fact, email address, secret, placeholder token, or child repo
  name/path (children by count only).

LIVE SYSTEMS
- Read-only reads of live systems are allowed as the review needs them (principal, 2026-11-09,
  verbatim: "reads of live systems is fine as needed, Reviews that need writes should be
  de-priortised"). A read means nothing on the target changes; if a verb's effect is unsure, treat
  it as a write. NO live writes of any kind; a check that would need one is marked NOT RUN with the
  reason and what it would have shown.
- Per the brief: `ccmail`'s sweep runs on every working run, `--status` included, and deletes
  files: ALWAYS run it with `CCMAIL_DEST` set to a directory under your scratchpad, never against
  the real cache. Read no mailbox: no real message id, no `--search`. Report route names and
  booleans only.
- Allowlist fields before printing anything from a provider or keychain read, since such reads can
  carry credentials; never dump a user, key, token or certificate object raw; never print a secret
  or keychain value. Leave no live captures in scratch.
- Never run an installed tool by bare name from PATH; use the worktree's own copy. Do not run
  `instruments/ccpdf/setup`. Never mutate the worktree's `tools/` or `instruments/`; probe on
  scratch copies.
- Python: use `/usr/bin/python3` for your own scripts where it suffices; the brief notes the repo's
  tests need the `python3` on PATH (3.10+), so use that only where the brief says. No GUI apps;
  never `open` anything.

LOAD (the principal's instruction is to keep this 16 GB laptop from crashing; several passes run
at once)
- Check `uptime` before heavy lines. Run any test suite or build under `nice -n 10`, one at a
  time, single process (no parallel runners), foreground with a long timeout. Prefer the targeted
  tests a finding needs over whole suites.

REVIEW LOG (principal, 2026-11-16: a review's work must be open and checkable once complete)
- Keep a running work log at ~/.claude/fable-drain/notes/atelier-160-1200-1953.md. It is the one
  file outside the brief you may write. Commands, files and evidence only.
- As you work, append: each step you took (the command run, or the file and line range read) and
  what it showed; each candidate finding with that evidence and the rule or requirement it breaks;
  each item you checked and found sound, with that evidence; what you left out and why. Enough
  detail that someone else could repeat the steps and reach the same verdict. If you are
  interrupted and resumed, read this log first.
- No secrets, tokens or live captures in it. The verdict itself goes only in the brief. Act 1
  entries are written before the sibling is released. It is private while the pass runs and is
  opened (appended to the brief) at the fold.

HOW TO FINISH
- Act 1: finish the full phase-1 verdict in the brief per its Process section, run the gates, then
  end your reply with: the overall verdict line, the tally by severity, the brief path, and the
  exact words "ACT 1 SAVED". Then stop and wait; do not open the sibling until the orchestrator
  sends you its path.
- Act 2 (after the orchestrator's message): read only the one held file it names, then do phase 2
  per the brief (`### Reconcile`, never revise act-1 text). Do NOT fold the sibling into the brief
  and do not delete anything: the orchestrator does the fold. End with "ACT 2 SAVED".
```
(Transcribed in full; the only edits are `<worktree>` and `<scratchpad>` for the two long
absolute paths, which appear in the log header above.)

##### Act 1 close, 2026-11-22 ~20:15 UTC
- Verdict appended to the brief below `---`; Status line updated to RUN / act 1 written.
- Findings: CCR1 MAJOR (CCMAIL_DEST swept; man page says a chosen dest is never swept), CCR2
  MODERATE (stale "stores nothing"/"your own mailbox" wording at ccmail:39,235,394,1422 and ADR
  0006:165,202,210), CCR3 MODERATE (installed pdftoppm dated 2026-09-09, budget not deployed),
  CCR4 minor (identical re-fetch does not renew), CCR5 minor (search/list print sender headers
  raw), CCR6 minor (0700/0600 credited against a same-user adversary), CCR7 minor (standing
  requirement + "operator's ruling" go past the pick), CCR8 note (idle vs request timeout; test
  env inherits XDG_CACHE_HOME/CCMAIL_DEST; `/` refusal untestable). Overall FAIL.
- Gates on the brief: datescan exit 0 clean; reviewscan exit 0 (deferred material kept out);
  spellscan exit 0 on a scratch copy (the repo ignores docs/reviews); wrapscan ignores
  docs/reviews, so a character-count check was run by hand: all act-1 prose lines <= 100.
- Scratch cleaned: probes, fixtures, the scratch renderer, captured diffs and run logs deleted.
- No git write. `git status --short`: the brief modified; the sibling's removal (pre-existing).

#### Act 2 (released by the orchestrator after local commit 00b8e4b5)
- Read the held sibling:
  ~/.claude/fable-held/atelier--2026-11-09-0153-ccmail-cache-and-recorded-reach-cold.deferred.md
  (31 lines): pointer's two questions (sweep reach outside its cache; threat-table completeness),
  3 brief-writer questions (limits pinned by tests; rmSync vs a swapped-in symlink; whether the
  stated reach holds for the identity the cloud login carries, checkable read-only), 2 held facts
  (sweep on every run incl. --status; registry entry owed outside the repo), re-run results at
  457615cc (62 tests then; 67 at HEAD because --headers added 5).
- Opening the barred records: commit body of c23fb6f1, the queue pointer, intent record 210/130,
  prior verdict docs/reviews/2026-09-25-0715-ccmail-build-cold.md.
- Read: `git log -1 --format=%B c23fb6f1` (the body: the pick, CC ids one line each, "Future
  credential-holding instruments must state that line", "tests pin it" for four roots; silent on
  CCMAIL_DEST); the queue pointer (claim block discloses the orchestrator shape); intent record
  210/130 (the 💬 answer line names "private permissions and a 30-day expiry" as the option's
  text; CC10 overtaken; CC1(iii) not built); prior verdict lines 359-415 (CC1-CC4), 449-468
  (CC9, CC10), 593-603 (reconcile on CC1, CC2). docs/sessions/ not opened (not needed).
- Reconcile written beneath the act-1 verdict; no act-1 text revised; no finding formed at
  reconcile. Key links: CCR7(a) traces to the prior CC1 "recurrence prevention", which named the
  controls list; CCR2 strengthened by the prior reconcile's quoted sentence surviving at
  ccmail:395-396; CCR3 is the same class as the prior CC10 (owed operator step left undone).
  Sibling Q2 (rmSync race) answered by reading cacheHygiene: deletion addressed by the resolved
  path under the resolved root; no finding. Sibling Q3 (reach of the real identity) NOT RUN:
  not readable from the repo; an admin-API read would print estate facts and no finding needed it.
- Status line updated: act 2 written, verdict unchanged. Gates re-run (see the verdict's own
  text for results). Scratch left empty. No git write; the sibling untouched (orchestrator folds).
