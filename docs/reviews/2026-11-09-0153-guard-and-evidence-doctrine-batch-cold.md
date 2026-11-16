# Cold pass — eight guard and evidence additions the principal approved in one list

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function; one change is to `floor.py`, which every child runs).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN 2026-11-16 UTC. Act 1 (verdict, on main at `b3f090c2`) and act 2
(reconcile) written by a Fable 5.1 reviewer under an off-tier orchestrator and the principal's
2026-11-16 drain order; sibling and review log folded below by the orchestrator. Overall:
PASS-WITH-FINDINGS, 0 MAJOR · 2 MODERATE · 4 minor · 2 note; every finding awaits the
principal's decision (rule 3), nothing applied. Brief written 2026-11-09 UTC by session
`d16dc612`, a headless Opus 5.5 brief-writer.
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
(folded below the verdict, § *Deferred sibling*), every delta commit's message
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


---

## Verdict — act 1 (phase 1), 2026-11-16 UTC

### Provenance (rule 4, V7)

- **Reviewer:** this session, on **Fable 5.1** (`claude-fable-5-1`), tier checked at selection.
  Run through the Agent SDK on the principal's Platform API credit, no claude.ai connectors (none
  needed). Day of run: 2026-11-16 UTC (`date -u`, 06:34 at open).
- **How spawned:** by a headless orchestrator session (Opus 5.5), itself started by drain session
  `1e053526` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition,
  form no finding and write no severity, and neither wrote the brief or the work. I was not started
  or instructed by any barred session (`722ac2e2` and its workers, `d16dc612`, `74f2b8cd`). No
  contact from any of them during the pass.
- **The approval this brief's Status line waited for**, the principal's drain order of 2026-11-16,
  as relayed in the spawn prompt, verbatim: *"I want to use things other than my weekly budget to
  clear as many fable reviews as possible like using fable drain. I thought we could start by using
  up all the API credits I have."* and *"As always you must ensure that nothing harms the integrity
  or quality of the review process and verdicts, for example if the review is done by API it must be
  as good as running it locally"*.
- **Spawn prompt, the direction it carried (process only; no question about the delta, no pointer
  to where the risk lives), verbatim excerpts:** *"The brief's `.deferred.md` sibling has been
  removed from the worktree on purpose and held elsewhere. Do NOT look for it in git history, other
  checkouts, scratchpads or tmp, and do not read the brief's barred list (rule 2) until act 2 is
  released. Act 1 is written and handed back BEFORE you see the sibling."* · *"The brief file only
  (no other repo file): act 1 appended below a `---` divider; update the brief's Status line"* · a
  running review log outside the repo, *"Commands, files and evidence only"* · *"No commit, no
  push, no git writes of any kind"* · *"LIVE SYSTEMS: read-only reads of live systems are allowed
  as the review needs them ... NO live writes of any kind"* · *"Child repos (the floorfleet run)
  are read-only and counted, never named"* · load rules (`nice -n 10`, one suite at a time, single
  process) · *"End your reply with exactly: the verdict line ... and the words 'ACT 1 SAVED'. Then
  stop and wait: the orchestrator commits act 1, then messages you the held sibling's path to
  release act 2."* The barred set is the brief's own list; the orchestrator added nothing to it.
  The release message is recorded in act 2.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1150-0632/atelier`, detached at
  `9edde0ad`; `git merge-base --is-ancestor 28c67b4a HEAD` exit 0. Read-only to me except this
  file. The sibling shows as a pending deletion (` D`) in `git status`; I did not seek it.
- **What I read:** this brief whole; `docs/method/REVIEW.md` whole; the nine delta commits through
  `coldsweep.py --commit` (subject, stat, diff; "message body not printed" on each; `--path` scoped
  as the brief lists; `git show --stat --format='%h %s'` confirmed no commit touched a path the
  scoping hid); the delta files at HEAD and `git diff 28c67b4a HEAD` on them; the cross-referenced
  sections of `EVIDENCE.md`, `CONCURRENCY.md`, `COMMUNICATION.md`, `ECONOMICS.md`,
  `PRINCIPLES.md`, `GUARDS.md`; `tools/floor.py` (the seam, the registry, `Config.load`),
  `tools/floorfleet.py`, `tools/report.py`, `tools/blockscan.py`; board item **titles only** by
  `ls` for `180/010`, `020/220`, `115/120`, `020/460`, and the programme README of `020/` at lines
  283–292 (not on the barred list; it holds the premise `MECHANISMS.md` cites). I opened none of
  the barred records, no commit body, no prior verdict, no session log. My harness loaded
  user-level and repo instruction files and a memory index, which carry private context this
  verdict does not. The start-up session-log step was skipped (REVIEW rule 2).
- **Method record:** every command, file range and result is in the running log the spawn prompt
  names (`atelier-160-1150-0632.md` in the drain's notes), appended to this file at the fold.
- **`/security-review`: NOT RUN**, discharged by grounds. It reads the session's pending diff, and
  this worktree's pending diff is the deliberate deletion of the sibling: a run would have printed
  the deferred material into my context before act 1 was written (the SL2 shape). The one code
  diff was weighed by hand under lens 4 instead.

### Load-bearing assumptions, named first and probed

| # | Assumption the work rests on | Probe | Result |
|---|---|---|---|
| A1 | The eight additions say what the principal picked and no more | Each delta section read against the acceptance list | Confirmed for all eight; the one premise he approved inside a pick that is false is GEB2 |
| A2 | The bidi escape changes nothing in the fleet today | 22 child configs and 44 workflow/pins files scanned read-only for U+202A–202E, U+2066–2069: 0 hits; fleet JSON with the escape disabled on a scratch copy vs enabled: byte-identical, 23 children | Confirmed |
| A3 | The seam is the only place child config text reaches a terminal | `Config.load` read; `floorfleet.py` imports `floor.strip_controls` (line 1041) and uses it on `ref` and lines | Confirmed for config text; but other tracked text now takes other seams (GEB6) |
| A4 | The grounded reproductions in the GUARDS additions reproduce | Registry at `28c67b4a` and at HEAD counted | Damaged: GEB1 |
| A5 | "Not mechanisable" (§17) is true | The delta's own `MECHANISMS.md` table and board `020/460` title | Damaged: GEB2 |
| A6 | Each cross-reference reaches the rule it names | Every pointer in the delta followed to its target text | One dangles by rule: GEB3; the rest hold |
| A7 | Doctrine text is the right altitude for five of the eight (review questions, no scanner) | Lens 1 reasoning below | Confirmed as the approved choice; see GEB2 for the stated reason |

### Lens 1 — approach and assumptions

The right problem, at the right altitude. All five rules bind as review questions with no scanner,
which is consistent with the programme's premise (directive first) and with each pick. Homes are
defensible: §16–§18 extend `EVIDENCE.md`'s run of "a claim is never stronger than its evidence"
rules; the corroborate-from-artefacts rule sits where the irreversible act lives; the two guard
rules sit beside the fourth requirement they refine. Two premises inside the text do not survive
probing (GEB1, GEB2); neither invalidates the rule it sits under, but both would mislead the next
reader who trusts the doctrine's account of the tree.

### Lens 2 — correctness and quality

Honest about done versus stubbed: each addition says "answer, not a ruling"; GUARDS says the
audit of atelier's own guards is unmeasured; MECHANISMS says it is "not a decision tree anyone
ruled". The code does what its changelog line says, and its tests exercise the three edges that
matter (idempotence, key collision, the rendered line). Overclaims: GEB1 (a "reproduced here" that
would not reproduce), GEB4 (six instances, four listed), GEB8 (an "only this mechanism" that is
not so).

### Lens 3 — completeness and harvest

V3 sweep: `MECHANISMS.md` is indexed in `README.md`, `docs/method/README.md` (item 17) and the
changelog; no template, skill or build doc carries a method-doc index it is missing from. The
floor's seam is described in `floorfleet.py`'s comments as dropping C0, which stays true. What the
work left undeclared: a home for write-then-rename (GEB5). What arrived after it and diverged
from its ruling: two more bidi homes (GEB6, HEAD-state, not the delta's authorship).

### Lens 4 — security and privacy (V6)

The floor change, by hand. The override and isolate set is escaped after the C0/C1 strip, on
keys and values at any depth, through the one seam both the floor and the fleet board read, so the
spoof (a reordered line over a red result) is closed on both surfaces at once. Error paths echo
no raw child text (`Config.load` prints the decoder's message and an escaped key). Keys that
collapse onto a literal marker refuse loudly (tested). Residuals, all by the pick: joiners,
zero-width spaces and the marks pass through; a config may type the literal marker `<U+202E>` and
read as if escaped (harmless: nothing reorders); homoglyphs are out of scope. Doctrine text has no
input surface; no personal data entered the delta (the de-naming of a child in `EVIDENCE.md` is a
later commit). The catalogue check for this class (CWE-150, CWE-117) is what `report.py` cites for
its own seam; the floor's seam now covers the same vectors for config text.

### The standing checklist

- **V1** — GEB1, GEB4, GEB8: three claims stronger than their evidence.
- **V2** — Re-run: all five re-run lines (ledger below), the child-config claim and the
  byte-identical claim; all reproduce. The GUARDS "reproduced here" does not (GEB1).
- **V3** — Swept; no missing mirror (lens 3).
- **V4** — GEB5 (a rule with its home undeclared); GEB6 (three homes for the bidi set at HEAD).
- **V5** — Cross-references checked for the rule reached: CONCURRENCY line 296 "Verify the act,
  not the absence of an error" is the bullet directly above the new one; EVIDENCE §14, §15 and §1
  hold what §16 and DATA-PROTECTION cite; COMMUNICATION "The reply plane is UNWIRED" holds
  MECHANISMS' axis-1 example; ECONOMICS "Heavy skills are episodic costs" holds axis 4; ADR 0006,
  `commands/`, `instruments/browser-fetch/` (an MCP server on the official SDK, with a venv) all
  exist as described. Dangling by rule: GEB3. Internal contradiction: GEB2.
- **V6** — Lens 4 above; scanner NOT RUN with grounds.
- **V7** — Provenance above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `8a58b882` floor + tests | yes | GEB7 (note); GEB6 bears on it at HEAD |
| `9f5736cb` §16 | yes | none |
| `6643d5ec` §17 + CONCURRENCY bullet | yes | GEB2 |
| `23b8570f` §18 | yes | none |
| `79db6ed9` DATA-PROTECTION | yes | GEB5 |
| `9d652f4b` GUARDS, forbid or cheap | yes | none |
| `7688af74` GUARDS, who from whom | yes | GEB1, GEB4 |
| `32b18fe5` MECHANISMS + two indexes | yes | GEB3, GEB8 |
| `28c67b4a` changelog | yes | none; both of its live claims re-driven and true |

### Findings

Every finding is the principal's to decide (rule 3); nothing applied. Counsel is labelled.

**GEB1 — MODERATE.** `docs/method/GUARDS.md` § *Declare the threat model*, second bullet:
*"(reproduced here by reading `tools/floor.py`'s registry: most hook-plane checks render absolute
worktree paths)"*. At the landing commit, 11 of the registry's 16 hook-plane templates already
carried `--staged` (`320/600`, landed 2026-11-03 in two commits, six days before this sentence was
written); at HEAD, 12 of 19. The registry's own comments give as the reason the exact hazard this
bullet presents as live: "a working-tree read let one writer's unstaged draft block another's
commit". So the reproduction stated in the present tense would not reproduce on the day it was
written (V2), and the doctrine contradicts the code it cites (V5). The rule above it stands; the
grounding misleads the next reader into believing the hook plane reads the worktree.
*Counsel:* date the reproduction to the filing (2026-08-19), name `320/600` as the fix that a
"who from whom" declaration would have made visible earlier, and list the hook checks that still
read the tree (at HEAD: the whole-tree link check and the warn-only checks) as the honest residue.

**GEB2 — MODERATE.** `docs/method/EVIDENCE.md` §17: *"**No guard:** the class is not
mechanisable, since nothing inspects a session's shell invocations"*. The same delta's
`MECHANISMS.md` table says a hook *"Intercepts a tool call or turn, unasked"* (`PreToolUse`), and
the board holds `020/460` (session hooks as a house enforcement plane). A `PreToolUse` hook
receives the shell command string before it runs; a check for a read verb chained by `&&`, `;` or
`|` to an irreversible verb is mechanisable, at least as an advisory. The no-guard decision is the
principal's answer and stands; the reason written into doctrine is false by the delta's own page,
and a false "cannot" forecloses the question for every future reader (V5; rule 3's "informed"
condition). *Counsel:* replace the reason with the true one (no hook plane is wired yet; `020/460`
owns the question), keep "no guard today".

**GEB3 — minor.** `docs/method/MECHANISMS.md` axis 1: *"The programme's premise is directive
first, enforced second (`GUARDS.md`)"*. `GUARDS.md` does not state that premise; its home is the
`020/` programme README, § *All doctrine directive first, enforced second (Mike, 2026-08-09)*, a
board record. A pointer to a file that does not hold the rule is dangling by rule (V5).
*Counsel:* point at the home, or lift the premise into `GUARDS.md` in his words so doctrine does
not depend on a board README.

**GEB4 — minor.** `GUARDS.md` § *Declare the threat model*: *"Six instances in one evening across
three parallel sessions ... :"* is followed by four bullets. The count and the list disagree (V1).
*Counsel:* say "four of the six" or list all six.

**GEB5 — minor.** `docs/method/DATA-PROTECTION.md`: *"The write-then-rename convention belongs in
whatever governs how a tool is written"*. No such home exists (`tools/README.md`, `docs/build/`
and the rest of `docs/method/` carry no rename rule); the convention is placed here while the
text says its home is elsewhere and unnamed. `GUARDS.md` § *A rule with no home is not a rule*
(V4). *Counsel:* declare this file the home, or name the file that is.

**GEB6 — minor, formed on the tree at HEAD, not on the delta's authorship.** The bidi set now
has three homes in `tools/` with three behaviours: `floor.py` escapes to `<U+XXXX>` and leaves
joiners (his pick, `020/350`); `blockscan.py` `_UNSAFE_RX` escapes as `\xNN`/`\uNNNN` and
includes joiners and zero-width characters; `report.py` `_MESSAGE_CONTROL_RX` drops the bidi set
silently and `safe_text` drops every `Cf`. The last two landed on 2026-11-09 after this delta's
landing commit, so the delta ignored nothing; but the pick's stated rationale ("a reader should see
that one was there rather than have it vanish") is now contradicted on two surfaces that print
tracked text to the same terminal (V4). *Counsel:* one seam, as `strip_controls`'s docstring
already argues for the floor and the fleet board; the principal decides whether his answer on
`020/350` binds the other two.

**GEB7 — note.** `tools/floor.py` `strip_controls` docstring opens *"Remove C0 control
characters (and DEL)"* while `CONTROL_CHARS_RE` has covered C1 since FR3; the delta edited that
sentence and kept the stale clause. Pre-dates the delta.

**GEB8 — note.** `MECHANISMS.md` axis 2: *"An MCP server sits available to be queried repeatedly
mid-reasoning, which none of the others do"*. An instrument is also called repeatedly
mid-reasoning through the shell tool; the real distinction is a typed tool surface against a
shell. Overclaim (V1).

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 2 MODERATE · 4 minor · 2 note.

The eight rules match what was picked and are honest about their status; the two MODERATE
findings are false premises inside the text, not wrong rules. No scope was cut silently.

### Re-run ledger

Python on `PATH` is 3.14.6 (`/usr/bin/python3` is 3.9.6, used only for my own helper scripts). All
suites under `nice -n 10`, single process, one at a time; `uptime` read before each (load 3.6 at
open, rising to 13 while several reviews ran).

| Line | Result |
|---|---|
| `python3 -m unittest discover -s tools -p test_floor.py` (the brief's `cd tools && ... test_floor`, run without a persisting `cd`) | exit 0, 255 tests OK, 248 s |
| `python3 tools/floor.py --plane ci --root <worktree>` | exit 0; advisory and report-only lines, nothing blocked |
| `python3 tools/floor.py --plane hook --root <worktree>` | exit 0; nothing blocked |
| `python3 -m unittest discover -s tools` | exit 0, 3134 tests OK, 896 s (one selftest warned that a synthetic over-cap fixture was not read whole, by design) |
| `python3 tools/floorfleet.py --root <estate parent> --json` to scratch, read by count | exit 0; 23 children, 0 unenrolled; with the escape disabled on a scratch copy of `tools/`: byte-identical JSON (24,867 bytes each) |
| Child configs scanned read-only for the escaped set | 22 configs, 0 carry any of it (0 carry zero-width or C0/C1 either); 44 workflow and pins files, 0 |

No check needed a live write; nothing is NOT RUN on those grounds. Scratch copies and JSON were
deleted at close.

### Follow-up checklist

- [ ] GEB1 — re-ground the hook-plane sentence; cite `320/600`.
- [ ] GEB2 — restate §17's no-guard reason; hand the hook question to `020/460`.
- [ ] GEB3 — point the premise at its home or lift it into `GUARDS.md`.
- [ ] GEB4 — reconcile "six" with the four listed.
- [ ] GEB5 — name write-then-rename's home.
- [ ] GEB6 — one seam for the bidi set, or a ruling that the three may differ.
- [ ] GEB7, GEB8 — wording.

### Reconcile — act 2 (phase 2), 2026-11-16 UTC

**Opened after act 1 was committed (`f3cc4a98`), on the orchestrator's release message (recorded in
the review log):** the sibling; the queue pointer; the eight intent records whole; the nine commit
bodies (`git log -1 --format=%B`); the three prior verdicts in `docs/reviews/` that name any of the
eight items, read at their matching lines only (`2026-08-09-0823` names `020/350` as the queued
decision; `2026-08-22-0031` names `320/050` as a proposal then existing; `2026-11-09-0207`, the
`320/600` pass, lists `320/050` among board items it met by line and did not read). Not opened:
`docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`; the author's account is complete in
the bodies and the intent records. No act-1 text is revised.

**The queue pointer's two questions.** *Restates a rule already homed elsewhere:* none of the eight
does; §17 and §18 each say which neighbouring rule they sit beside and how they differ, and the
reading holds. The two home defects found are a premise cited to the wrong file (GEB3) and a rule
placed while naming its home as elsewhere (GEB5). *Does the escape reach every surface that prints
a child's config:* yes. Both readers of `.atelier-floor.json` pass the parsed document through the
one seam (`floor.py` `Config.load`; `floorfleet.py` line 1041), and `floorfleet` also runs its
workflow `ref` and each `floor.yml` line through it (lines 248 and 757). The brief-writer's
question 1 asked the wider form, child-sourced text of any kind: the pre-commit hook text is read
and only tested for a substring, never printed; the local-read texts feed `classify`, whose
state and detail strings are fixed literals; the one child-sourced string printed raw is the
repo's directory name (and, with `--from-github`, its slug, which the forge restricts to ASCII).
A directory name is set by the operator, not by the child's content, so it is outside the item's
scope; recorded here as checked, not as a finding. Tracked text printed by the scanners goes
through `report.py`'s seam, which is GEB6.

**The brief-writer's question 2** (a child's first honest compliance step): each rule states it.
§16: capture the fixture and record program, version and date; §17: run the check alone, read it,
then act; §18: one extra call against a known-present case, printed on the line above. The
`CONCURRENCY.md` pointer bullet does not say whether it is copied into the child doctrine block;
the bullet above it says it is not, and the pointer route reaches the child either way.

**Per finding, against the sibling and the author's account:**

- **GEB1 — stands, strengthened.** The intent record (`320/050`) gives the reproduction with its
  date and count: *"11 of the 15 hook-plane checks render absolute worktree paths and 4 take
  `--staged`"*, as of the filing on 2026-08-19. The delta dropped the date and the count and wrote
  "most", in the present tense, six days after `320/600` had inverted the ratio (11 of 16 staged
  at landing). The commit body repeats the stale shape as a current fact: *"floor reads the
  worktree, not the staged set"*. The `320/600` pass's own verdict (`2026-11-09-0207`) was in the
  tree when the sentence was written. Counsel unchanged: date it, cite `320/600`, name the residue.
- **GEB2 — stands, strengthened.** The intent record said *"⚠️ What is not established:
  whether the class is mechanisable. Nothing here inspects a session's shell invocations"*. The
  recommendation hardened "not established" into "(not mechanisable)", and the doctrine states it
  as fact; the commit body says the same. So the principal approved a one-line summary carrying a
  claim its own source marked open, which is the rule-3 "informed" condition this finding turns
  on. The decision (no guard) stands as his answer; the stated ground does not.
- **GEB3 — stands.** The intent record cites the premise as *"the policy-as-code programme's own
  premise (directive first, enforced second)"* and, in its closing note, *"GUARDS.md's enforcement
  premise"*; the delta copied the second attribution. The premise's home is the programme README
  (his words, 2026-08-09), not `GUARDS.md`.
- **GEB4 — stands, counsel refined.** The intent record's wording is *"Six instances, four shapes,
  one evening, three parallel sessions"*, then four numbered shapes plus two run-level members. The
  delta kept "six instances" and dropped "four shapes". Counsel: restore "in four shapes".
- **GEB5 — stands.** The phrase is copied from the intent record (*"belongs in whatever governs
  how tools are written rather than in a scanner"*). A board item may leave a home open; doctrine
  placed in a file is that file's rule or it is homeless.
- **GEB6 — stands as filed** (HEAD-state; the two later seams post-date the delta). The intent
  record `020/350` framed the decision for the floor's seam only; nothing in the account reaches
  `report.py` or `blockscan.py`.
- **GEB7 — stands.** Not addressed by any account.
- **GEB8 — stands.** The phrase *"which none of the others do"* is copied from the intent record's
  candidate axes.

**Against the author's account generally.** The commit bodies claim nothing the diffs do not show.
`8a58b882`'s "12 failures on the old seam" was not re-driven (the old seam is gone); its two live
claims were, and reproduce. `32b18fe5`'s correction of the item's premise (browser-fetch is
in-estate, not third-party) is right: the item said *"adopted once (browser-fetch, third-party)
but never built in-estate"* and `instruments/browser-fetch/server.py` is in this repo. The §18
example in doctrine is genericised from the intent record's named pools and named child, which is
the right call for a public doctrine file.

**Re-run results against the sibling's (2026-11-09 at `457615cc`):** `test_floor` 187 then, 255
now; the full suite 2,643 then, 3,134 now, both OK (the tree grew by 66 commits on the delta's
paths); both planes exit 0 then and now; `floorfleet` 23 rows then and 23 now; children carrying
the escaped set 0 of 21 then, 0 of 22 configs now; the before-and-after byte comparison the
brief-writer did not run was run here and is byte-identical.

**No finding formed at reconcile.** The sibling's questions were both answered by act-1 probes
already run; nothing in the barred records changed a severity.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 4 minor · 2 note.** Every
finding is the principal's to decide (rule 3); nothing applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

The text below is the brief's held-back sibling,
`2026-11-09-0153-guard-and-evidence-doctrine-batch-cold.deferred.md`, copied verbatim. It was
removed from the review worktree before the reviewer started, held outside the tree until act 1 was
committed (locally as `f3cc4a98`, the hash the reviewer's own text cites; it landed on
main as `b3f090c2` after a rebase onto concurrent work), then released to the reviewer for act 2. The orchestrator forms no finding
and has not edited it; the sibling file itself is deleted in the fold commit.

# Deferred reading for `2026-11-09-0153-guard-and-evidence-doctrine-batch-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether any addition restates a rule already homed elsewhere; whether escaping in `strip_controls`
reaches every surface that prints a child's config.

## The brief-writer's questions

1. Which printing surfaces of `floor.py` and `floorfleet.py` carry child-sourced text and do not
pass through `strip_controls`?
2. §16–§18 as read by a child: what would a child's first honest compliance step be, and does the
rule say so?

## What the brief-writer held back

- The changelog carries a measured claim about the fleet (byte-identical report); it is in the
  re-run list.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`test_floor`: 187 tests, OK, exit 0. `floor.py --plane ci`: exit 0, with 28 `secretscan` advisories
reported and not blocking. `--plane hook`: exit 0. Full suite under `python3` 3.14: 2,643 tests, OK,
exit 0, 1,228 s at a load of about 20. `floorfleet --json`: exit 0; 23 rows, 1 parent, 21 wired
children, 1 absent. Children whose `.atelier-floor.json` carries a bidi override or isolate
character: 0 of 21. The before-and-after comparison of the fleet report was not run.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/1150, cold pass on the guard and evidence doctrine batch

Reviewer: Fable 5.1 (claude-fable-5-1), Agent SDK lane on Platform API credit.
Spawned by a headless orchestrator (Opus 5.5), started by drain session 1e053526 (Opus 5.5).
Worktree: /Users/mike/worktrees/fable/atelier-160-1150-0632/atelier (detached HEAD 9edde0ad).
Brief: docs/reviews/2026-11-09-0153-guard-and-evidence-doctrine-batch-cold.md. Prefix GEB.
Sibling .deferred.md absent from the worktree on purpose (git status shows ` D`); not sought.

## Act 1

- 2026-11-16T06:34Z `date -u` -> Mon Nov 16 06:34:02 UTC 2026. `uptime` load 3.57 3.17 3.57 (16 GB laptop, several reviews live).
- `git merge-base --is-ancestor 28c67b4a HEAD` exit 0. HEAD 9edde0ad. python3 on PATH = 3.14.6; /usr/bin/python3 = 3.9.6.
- Read the brief whole (246 lines).
- Read docs/method/REVIEW.md whole (708 lines) for rules 1-4, the four lenses, V1-V7 and the verdict/method-record shape.
- `git log --oneline 28c67b4a..HEAD -- <the ten delta paths>` -> 66 commits (brief said 16 at 457615cc). None of them is a delta commit; checked by diffing the delta's sections at HEAD against the landing commit (below).
- `git show --stat --format='%h %s' <sha>` for each of the nine (subject + stat only, no body): every one touches only delta paths; no board-store or barred file was hidden by the brief's `--path` scoping.
- Nine `coldsweep.py --root <worktree> --commit <sha> --path ...` reads, exit 0 each, saved to scratch /tmp/geb-1150-scratch/c1..c9 and read whole. Each printed "message body not printed", 0 board-store files, 0 rule-2 barred files. Per-commit: 8a58b882 floor.py+test_floor.py (BIDI_CHARS_RE, strip_controls escapes to <U+XXXX>, 5 new tests); 9f5736cb EVIDENCE §16; 6643d5ec EVIDENCE §17 + CONCURRENCY bullet; 23b8570f EVIDENCE §18; 79db6ed9 DATA-PROTECTION new section; 9d652f4b GUARDS "Choosing between them"; 7688af74 GUARDS "Declare the threat model"; 32b18fe5 MECHANISMS.md new + README.md + method/README.md item 17; 28c67b4a CHANGELOG Added block.
- Candidate (from reading 7688af74): GUARDS "Declare the threat model" says "Six instances in one evening across three parallel sessions ... :" then lists four bullets. Check at HEAD before forming.
- Candidate (from reading 32b18fe5 vs 6643d5ec): MECHANISMS axis 4 "A scanner runs near-free on every commit once built" vs EVIDENCE §17 instance 4 "staged in the minutes the slow floor took". Weigh as V5.
- Decision: /security-review NOT RUN. The worktree's pending diff is the deliberate deletion of the brief's .deferred.md sibling (git status ` D`); a pending-diff scanner would print the deleted sibling's content into my context before act 1 is written (REVIEW.md lens 4, SL2 caution). Discharged by grounds; floor.py diff weighed by hand instead.
- Delta sections at HEAD: `git diff 28c67b4a HEAD -- <doc paths>` touches EVIDENCE.md only outside §16-18 (§3 pointer, §15 grounding de-named, bearing line de-named); GUARDS.md additions (lines 81-150 at HEAD) byte-for-byte the landing text; DATA-PROTECTION.md and MECHANISMS.md unchanged since landing. EVIDENCE headings at HEAD: §1-§18 contiguous, §16-18 are the delta.
- Cross-refs reached (V5): CONCURRENCY.md line 296 "Verify the act, not the absence of an error" is the bullet directly above the delta's line-320 bullet -> "mirror of the bullet above" holds. EVIDENCE §14 (instrument must not lie), §15 (test cannot falsify its own code), §1 (provenance) all hold the rules DATA-PROTECTION/§16 cite. COMMUNICATION.md:111 "The reply plane is UNWIRED (Mike, 2026-08-15)" holds MECHANISMS' axis-1 remedy example. ECONOMICS.md:412 "Heavy skills are episodic costs" holds axis 4. docs/decisions/0006-instruments-in-atelier.md exists. commands/ exists (4 entries). instruments/browser-fetch/server.py line 3: "MCP server ... built on the official mcp SDK (FastMCP, stdio)"; setup line 11 creates a venv -> MECHANISMS table row and axis-4 claim hold. GUARDS "directive first, enforced second": grep found no such phrase in GUARDS.md (check PRINCIPLES/other home later).
- Board titles cited by the delta (not barred, titles only): 180/010 "the plugin was never installed so the hand-carried prompt never stopped" (matches MECHANISMS); 020/220 "the census nobody has run: which rules have a..." (matches §17 "the kind 020/220 exists to count"); 115/120 "every guard declares the purpose it answers to" (matches GUARDS 320/050 "registry slot of 115/120"); 020/460 cites MECHANISMS.md (a later item pointing at the delta).
- Mirror sites (V3): MECHANISMS.md listed in README.md:73, docs/method/README.md:91 (item 17), CHANGELOG. docs/build/REPO-STANDARD.md and PRINCIPLES.md reference GUARDS.md by rule, not as an index of method docs -> no stale index found. PRINCIPLES §6 sweep surface list = docs/, skills/, commands/, docs/build/templates/, inlined floor blocks. Grep of skills/ and docs/build for "control character|bidi|strip_controls": none. tools/floorfleet.py comments (lines 237, 748) say "floor.strip_controls drops the C0 range wholesale" — still true; they do not claim C0 is the whole behaviour. tools/README.md:2277 says another tool prints "heading text and map paths ... with control and bidi characters escaped" -> check for a second bidi set (V4) below.
- `nice -n 10 python3 -m unittest discover -s "<worktree>/tools" -p test_floor.py` (PATH python3 3.14.6; equivalent to the brief's `cd tools && python3 -m unittest test_floor`, written without a persisting cd): exit 0, "Ran 255 tests in 248.385s OK". A fixture printed "board: docs/ROADMAP.md rebuilt (13 lines)" (a temp dir); worktree git status unchanged afterwards (only the sibling's ` D`).
- Hook-plane registry claim (GUARDS 320/050 bullet 2, "reproduced here by reading tools/floor.py's registry: most hook-plane checks render absolute worktree paths"): `git show 28c67b4a:tools/floor.py` (file content only) -> 16 `hook=[` templates, 11 carry `--staged`; at HEAD 19 templates, 12 with `--staged`. `git log --format='%h %ad %s' -S'320/600' -- tools/floor.py` -> 7673da13 and 38bdcb1b, both 2026-11-03, "read the staged index at the hook, not the disk (320/600)". So on 2026-11-09, when the sentence was written as present-tense doctrine, most hook-plane checks read the index, not the worktree. CANDIDATE GEB finding (V1/V2/V5).
- Candidate: GUARDS 320/050 "Six instances ... :" followed by four bullets (V1, minor).
- Child configs, read-only count via /usr/bin/python3 -I helper over the estate's sibling clones: 22 `.atelier-floor.json` found, 0 carry any of U+202A-202E/U+2066-2069, 0 carry zero-width/marks, 0 carry C0/C1; 44 workflow/pins files, 0 carry the bidi set. Supports the changelog's "No local child's config carries any".
- Fleet report byte comparison (re-drives the changelog's "byte-identical before and after"): copied tools/ to scratch, replaced BIDI_CHARS_RE in the copy with a never-matching pattern, ran `floorfleet.py --atelier <worktree> --root <estate parent dir> --json` from the copy and from the worktree (read-only; local file reads), both exit 0, `cmp` -> byte-identical, 24867 bytes each; JSON read back: 23 children, 0 unenrolled. Scratch copy and JSON deleted at close.
- `nice -n 10 python3 tools/floor.py --plane ci --root <worktree>` exit 0 (advisory and report-only findings printed, nothing blocked; "declarations: 21 checks, 0 meet all five" is the 115/120 step-0 report, not the delta). Load at start 9.17.
- `nice -n 10 python3 tools/floor.py --plane hook --root <worktree>` exit 0, nothing blocked. Load at start 10.46 (several reviews live).
- V4 probe: `grep -n -i '202a|2066|bidi' tools/*.py` -> three homes for the bidi set: floor.py BIDI_CHARS_RE (escape `<U+XXXX>`, joiners left), tools/blockscan.py:883 `_UNSAFE_RX` (escape `\xNN`/`\uNNNN`, INCLUDES U+200B-200F, U+2060-2064, U+FEFF), tools/report.py:104 `_MESSAGE_CONTROL_RX` (DROPS the bidi set silently; `safe_text` drops all Cf). `git log -S'u2066' --format='%h %ad %s'` -> f62b5c45 (160/730) and 09940dfa (160/430), both 2026-11-09; `merge-base --is-ancestor` shows both are AFTER the delta's landing 28c67b4a. So not something the delta ignored; drift from the 020/350 pick after it. Candidate minor, labelled HEAD-state.
- Config.load error path (floor.py 2076-2092): a JSON error raises ConfigError with the decoder's message (position only); the collapse refusal carries the stripped key repr. No raw child text reaches the terminal before the seam. Sound.
- `grep -rn -i 'directive first' docs README.md skills` (excluding barred stores): the premise lives at docs/roadmap/020-.../README.md:285 "### All doctrine directive first, enforced second (Mike, 2026-08-09)"; GUARDS.md has no such statement (its two "directive" uses, lines 158 and 172, are the evidence-window section landed later). MECHANISMS.md:32 cites GUARDS.md for it. Candidate GEB (V5 dangling by rule).
- `grep -rn -i 'rename' tools/README.md docs/build docs/method`: write-then-rename appears only in the delta's DATA-PROTECTION paragraph, which says it "belongs in whatever governs how a tool is written". No such home exists. Candidate minor.
- EVIDENCE §17 "nothing inspects a session's shell invocations" vs MECHANISMS table "Hook | PreToolUse, Stop and kin | Intercepts a tool call or turn, unasked" and board 020/460 (title: Claude Code session hooks as a house enforcement plane). A PreToolUse hook receives the shell command before it runs. Candidate GEB (V5 within the delta; lens 1 premise).
- Board 020/460 title read by `ls` only.
- Full suite started in the background at load ~10: `nice -n 10 python3 -m unittest discover -s <worktree>/tools` -> scratch discover.out; result recorded below when it ends.
- 06:50Z act 1 appended to the brief below `---` (provenance, assumptions table A1-A7, four lenses, V1-V7, per-commit ledger, GEB1-GEB8, overall PASS-WITH-FINDINGS 0/2/4/2, re-run ledger with one placeholder for the running full suite, follow-ups). Status line updated (never "fold-in owed").
- Checked docs/build/templates/CLAUDE.md for a method-doc index: it carries pointers to PROPAGATION/ECONOMICS/TOOLBOX/CONCURRENCY/REVIEW only, no enumerated list -> no V3 miss for MECHANISMS.md.
- Brief max line length 245 pre-verdict (code blocks and long paths); my prose kept at <= 100.
- Full suite: `nice -n 10 python3 -m unittest discover -s <worktree>/tools` exit 0, "Ran 3134 tests in 896.296s OK" (load peaked 16.8 during the run with other reviews live; eased to 2.8 at its end). Placeholder in the re-run ledger filled.
- Scanners over the brief: datescan exit 0 clean (485 lines read); linkscan exit 0 (no internal links in the brief); spellscan and wrapscan skip docs/reviews by the repo's ignore files ("scanned nothing"), so both were re-run on a scratch copy of the brief outside that ignore: spellscan clean (485 lines), wrapscan `--limit 100` clean. awk width check: no prose line in the verdict over 100 columns after one rewrap (V5 bullet).
- No allow markers added. No file written other than the brief and this log. Scratch directory /tmp/geb-1150-scratch (commit diffs, test outputs, fleet JSON, patched tools copy, brief copy) deleted at the end of act 1.
- Act 1 handed back for commit; act 2 (reconcile) waits for the orchestrator's release message.

## Act 2

- Release message from the orchestrator, verbatim: "Act 1 is committed (f3cc4a98, brief file only, unrevised). Act 2 is now released. You may now read this one held file, the brief's deferred sibling: "/Users/mike/.claude/fable-held/atelier--2026-11-09-0153-guard-and-evidence-doctrine-batch-cold.deferred.md". Then do the brief's Phase 2: open the barred records it lists (rule 2 lifts now), screen the nine delta commits' message bodies, and append `### Reconcile` beneath your verdict in the brief: per-finding notes against the sibling's questions and the author's account, any finding formed at reconcile marked as such, and the overall line restated. Never revise act-1 text. Update the Status line (never "fold-in owed"). Do NOT fold or delete the sibling yourself: the orchestrator folds it. Append your act-2 steps to the same review log. Same rules as before: write only the brief and the log, no git writes, niced single-process tests, public repo (no private names, paths, secrets), run datescan/linkscan over the brief before finishing. End with "ACT 2 SAVED"." It carried no question about the delta and no pointer to where the risk lives.
- Read the sibling whole (pointer-block questions, 2 brief-writer questions, 1 held fact, re-run results at 457615cc).
- `git log -1 --format='%s%n%n%b' <sha>` for the nine delta commits: bodies read. 7688af74's body restates "floor reads the worktree, not the staged set"; 6643d5ec's body states "not mechanisable".
- Read the queue pointer whole and the eight intent records whole. Key lines: 320/050 "11 of the 15 hook-plane checks render absolute worktree paths and 4 take --staged" (filed 2026-08-19) and "Six instances, four shapes"; 320/390 "What is not established: whether the class is mechanisable"; 370/010 "belongs in whatever governs how tools are written"; 400/010 "which none of the others do", "browser-fetch, third-party ... never built in-estate"; 380/010 example used named pools (genericised in the delta).
- `grep -ln` of the eight item ids over docs/reviews/*.md -> three prior verdicts; read at the matching lines only (0823:421, 0031:114/117/190, 0207:272-284). None bears on a finding.
- Q1 probe: floorfleet.py `_read_local` (384-391) feeds classify; state/detail literals at 826-828; hook text (707) substring-tested only; `name=repo.name` (1065) printed raw in render (directory name / GitHub slug, not config text). floor.py `_heading_set` (3115) is the blockscan map check; headings are compared, not printed by floor.py.
- Appended `### Reconcile` beneath the verdict; act-1 text untouched. Status line updated to VERDICT COMPLETE. No finding formed at reconcile; overall restated 0/2/4/2.
- Not opened in act 2: docs/SESSIONS.md, docs/sessions/, docs/ROADMAP-DONE.md.
- Final: datescan and linkscan exit 0 over the brief after two rewraps in the reconcile; spellscan and wrapscan --limit 100 clean on a scratch copy; scratch deleted. Act 2 handed back; the sibling is left for the orchestrator to fold.
