# Cold pass — personal data in a public repo is one closed list only the principal adds to (160/630)

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: a rule of the public repo and a test that enforces it).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN 2026-11-16 UTC on Fable 5.1: FAIL (1 MAJOR, 3 MODERATE, 3 minor,
PCL1–PCL7); act 1 verdict (committed `e5b187a1`) and act 2 reconcile below the divider; the
held-back sibling is folded below the reconcile. Brief written 2026-11-09 UTC by session
`d16dc612`, a headless Opus 5.5 brief-writer.
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

---

## Verdict — act 1 (cold pass, 2026-11-16 UTC)

**Overall: FAIL — 1 MAJOR, 3 MODERATE, 3 minor, 0 notes (PCL1–PCL7).** The claim the delta set out
to make true ("listed in one place") is true at HEAD and a test keeps it so; what fails is the grant
rule at its own home (PCL1) and the coverage the list and test claim for the marker check (PCL2).

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Ran on 2026-11-16 UTC, from 07:43 UTC.
- **Spawn:** a headless Opus 5.5 orchestrator session, itself started by drain session `1e053526`
  (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition, form no
  finding and write no severity. Neither was started or instructed by a barred session
  (`722ac2e2` and its workers, `d16dc612`, `74f2b8cd`). No contact with any of them during the pass.
- **The spawn prompt** was process only: this file's path, the review worktree, the two files I may
  write, the barred set (this brief's § *Deferred reading*, repeated), the sibling's removal from
  the worktree, read-only git and live systems, load and interpreter rules, the deliverable's shape
  and the release timing. It carried no question about the delta, no pointer to where risk lives
  and no request about any finding. It is not pasted here because it names machine-local paths,
  which the standard under review keeps out of a public repo; the orchestrator holds it verbatim.
- **Mandate:** the principal's drain order of 2026-11-16, verbatim: *"I want to use things other
  than my weekly budget to clear as many fable reviews as possible like using fable drain. I
  thought we could start by using up all the API credits I have."* and *"As always you must ensure
  that nothing harms the integrity or quality of the review process and verdicts, for example if
  the review is done by API it must be as good as running it locally"*. This pass ran through the
  Agent SDK on the Platform API credit; nothing in the method below was shortened for it.
- **Worktree:** `atelier-160-1120-0742`, at `be9b3ad0` = `origin/main`, with `920cfed1` an
  ancestor (`merge-base --is-ancestor`, exit 0). The sibling `.deferred.md` shows as deleted in
  `git status`; I did not look for it anywhere.
- **What I read:** this brief whole; `docs/method/REVIEW.md` lines 25–566; the delta body-free via
  `tools/coldsweep.py --commit 920cfed1` scoped to the 16 paths (footer: body not printed, 0 board
  files, 0 rule-2 files); subjects only of the 76 commits since on those paths; diffs since on the
  four doctrine surfaces; at HEAD `docs/PERSONAL-DATA.md`, `tools/test_personal_data.py`,
  `docs/build/REPO-STANDARD.md` § *Repo-craft conventions*, both child templates, `CLAUDE.md`,
  `tools/pdlistscan.py` lines 1–70, `tools/README.md` § *pdlistscan*, `CHANGELOG.md` lines
  270–300, `docs/decisions/0005-going-public.md` lines 28–70, `docs/method/GUARDS.md` lines
  190–200, 265–275, 452–462, 586–592, `docs/method/AUTONOMY.md` lines 45–57, the register draft's
  first 40 lines, `.github/workflows/ci.yml` (grep), `tools/leakscan.py` lines 107–142, and the
  board index `docs/ROADMAP.md` (grep for the subject: items 630 ✅, 1120 ⏳, 1340 ⏳).
- **Residual exposure, named:** the delta's own changelog entry and test docstring carry the prior
  pass's finding ids (PI1–PI10) and what was done about each; I read them as the delta. I opened
  no prior verdict, no session log, no commit body, and neither barred item file. A count-only
  `git log --format=%b | grep -c` over all history (for PCL6) read no body text. My start-up reading
  skipped the session-log step (`CLAUDE.md` step 4, cold reviewer). The harness loaded user-level
  instruction files and a memory index that hold private context; none of it concerns this delta.
- **Method record:** every command, file range and result is in a running log kept outside the
  repo (machine-local path, held by the orchestrator), written as the pass ran; this verdict
  carries the evidence that decides each finding.

### Re-run ledger (V2)

`uptime` before the heavy runs: load 2.68. Interpreter: the 3.14 `python3` by absolute path (the
brief's note on 3.9 holds). One process at a time, under `nice -n 10`, foreground.

| Line | Result |
|---|---|
| `cd tools && python3 -m unittest test_personal_data` | 11 tests, OK, exit 0 |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | exit 0; every scanner ✓ incl. leakscan (structural + local) and pdlistscan; pointerscan ⚠ 4 queue-state on other passes' pointers (1080, 1250, 1420, 994), not this delta |
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | exit 0; all ✓; same pointerscan ⚠ |

Children: none read (read-only, counted, not named); no child was needed for a finding.

### Lens 1 — approach and assumptions

The problem is the right one at the right altitude: an honest claim, one home, a test, and the
grant rule in prose, with scanner enforcement deferred and then delivered by `pdlistscan` in a
later commit (`6607c0eb`, its own pass queued as `1340`). The pick's third clause ("so the scanner
refuses any other excuse") was therefore not delivered by this delta, and the delta says so.

Load-bearing assumptions I named, each probed:

- **A1 — the test sees every tracked file.** Probed: 1402 tracked files, 0 binary, 0 case-variants
  of the three pinned strings. Confirmed.
- **A2 — the test runs in a gate.** `.github/workflows/ci.yml:108` runs `unittest discover -s
  tools`; the floor does not run tests. Confirmed for CI; the hook plane cannot catch it (the
  design accepts this; `pdlistscan` now fills the hook side).
- **A3 — "closed" is enforced.** `EXPECTED_IDS` in the test must change with the list. A session
  can change both; the docstring says so ("a visible act"). Confirmed as honest.
- **A4 — globs anchor.** `glob_rx` adds `\Z`, `re.match` anchors the start, `*` stays in a
  segment. Confirmed; the parsed place set for PD1–PD3 matches the file.
- **A5 — the marker check covers every personal-data allow-marker.** Damaged: PCL2.
- **A6 — the list's own grants meet the rule it states.** Damaged: PCL1.
- **A7 — every mirror site carries the whole rule.** Damaged: PCL3, PCL4.
- **A8 — each pointer reaches the rule it cites.** One does not: PCL5. ADR 0007, the register
  draft and AUTONOMY reach what the text says.
- **A9 — the list's places pass the purpose test.** PD1 in `tools/floorfleet.py`,
  `tools/test_floorfleet.py`, `tools/test_templates.py`: the owner classifier and the template's
  real workflow address, where a placeholder would not serve. Confirmed.
- **A10 — PD5's commit-body claim matches history.** Damaged: PCL6.

### Lens 2 — correctness and quality

Claims re-driven at HEAD: the list names five entries with data, why, how granted and where; the
test fails on a stray listed string, a stale place, a scoped personal-data marker outside a named
place, a changed entry set, and the old claim's return (read in the source; the suite is green at
HEAD and the probe in PCL2 shows which case it does not fail on). "No scanner behaviour changed":
the diff to `leakscan.py`, `secretscan.py` and `floor.py` is docstring, `--help` text and one
`why` string. Confirmed. "One entry cannot be pinned": PD4 and PD5, and the test pins exactly
those as unpinned. Confirmed. Overclaims: PCL2 (marker coverage), PCL3 ("whole rule" in a child's
own files), PCL4 ("a repo with no such file holds no exceptions").

### Lens 3 — completeness and harvest

V3 sweep (coldsweep, barred files out): the old framing survives on one live doctrine surface
(PCL7); the rest are history or quoted corrections. The standard's file set, the templates
directory and `create-repo` do not carry the list file the standard now requires of every repo
(PCL4). The private-repo half of the grant rule reaches no child surface (PCL3). Nothing the delta
duplicated: the register draft is named as a destination, not a second home.

### Lens 4 — security and privacy (V6)

What the list publishes is already in `CLAUDE.md` and the plugin manifests; the new file adds no
datum, only a labelled gathering of three. The grounds for each entry are a purpose a placeholder
would not serve (A9). Design altitude: the rule's one hole is the grant form (PCL1), the code
altitude hole is the unscoped marker (PCL2). `/security-review` not run: the delta is landed, not
pending, and the only dirty path in the worktree is the removed sibling, so the scanner could read
nothing of the work; a scratch clone was used for the PCL2 probe and deleted.

### Standing checklist

- **V1** — three claims stronger than their evidence: PCL2, PCL3, PCL4.
- **V2** — three lines re-run, all green; the ledger above.
- **V3** — PCL3, PCL4, PCL7.
- **V4** — one home for the list (`docs/PERSONAL-DATA.md`); the standard, `CLAUDE.md`, `README.md`,
  `tools/README.md` and the templates point at it rather than copy it. Discharged.
- **V5** — PCL1 (the list's grant forms against the standard's rule), PCL5 (a pointer that reaches
  no rule). Cross-references otherwise reach the rule named: ADR 0007 → `allowed_signers`; the
  register draft → "heading", a draft awaiting his acceptance; AUTONOMY → widening is a floor act.
- **V6** — lens 4 above.
- **V7** — provenance above, and in the brief.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `920cfed1` | yes (`coldsweep --commit`, 16 paths) | PCL1–PCL7 |

### Findings

**PCL1 — MAJOR — The list's own grant form admits what the rule forbids.** The standard
(`docs/build/REPO-STANDARD.md` lines 198–203): *"In a public repo only the principal grants an
exception, in his own words, and the list is closed until he adds to it... it never adds an entry
itself."* The list (`docs/PERSONAL-DATA.md` lines 24–27) then defines a second form, *his call*:
*"a decision he made that a decision record keeps, not necessarily in his exact words"*, and four
of five entries (PD2–PD5) rest on it, all citing `docs/decisions/0005-going-public.md`. That ADR
carries no quoted words of his (grep for a quotation: 0; "verbatim"/"his words": 0); it is a
session's account that the exposure was "accepted knowingly". So at the rule's own home, a session
wrote the first list, chose its entries, and licensed them by a form the rule does not allow, and
the list does not say that these entries predate the rule or were never put to him. Any future
entry can take the same route: write a decision record, cite it as "his call". This is the failure
the brief names first among the worst (a grant wording that lets a session grant what only the
principal may). The acceptance test ("only you grant") is met in prose and not in the register.
*Counsel:* one ask, with the five entries in plain words, for his grant of PD2–PD5 in his own
words; cite them; strike or confine *his call* to entries he has named as grandfathered.

**PCL2 — MODERATE — An unscoped allow-marker opens a route every gate passes.** The list says a
personal-data allow-marker in a file no entry names fails the suite (lines 14–17); the test
docstring says the same and that the unscoped form "is counted separately". Nothing counts it:
`MARKER_RX` matches `leakscan:allow:<scope>:` only, and `leakscan` (lines 107–109) exempts every
structural rule on an unscoped marker. Probe on a scratch clone: a file with an `example.org`
address and `<!-- leakscan:allow: probe reason -->`, staged in the clone: `test_personal_data`
11 OK; `leakscan` exit 0 ("allow-marker breakdown: email×1"); `pdlistscan` clean, exit 0. Three
greens on an email in an unlisted file, which is the silent failure the brief names. Today's tree
uses the unscoped form outside `tools/` on six lines, none personal, so the route is open, not
used. The scanner non-goal does not cover this: the absence makes the list's claim false.
*Counsel:* the test (and `pdlistscan`) count an unscoped marker on a line any personal-data rule
would fire on; or `leakscan` refuses the unscoped form where a personal-data rule fires, which
needs no notion of a list.

**PCL3 — MODERATE — The private-repo half of the grant rule reaches no child.** The acceptance
test's second answer ("Ordering the work is permission") lands in the standard (lines 201–203):
the order is the grant, the session records, marks its own call and asks when unsure. The child
`CLAUDE.md` template (lines 147–160) and `CONTRIBUTING.md` template (109–113) carry the public-repo
half only, then "Full rule:" a pointer. The delta's changelog claims *"a child reading only its
own files gets the whole rule"*. Most children are private, so the half they get is the half they
cannot use, and the duty to mark an exception as the session's own call reaches none of them.
*Counsel:* one sentence in each template, the standard's own.

**PCL4 — MODERATE — "One list per repo" with no list in the file set, the templates or the
scaffold, and no item to carry it.** The standard (lines 204–207): *"One list per repo,
`docs/PERSONAL-DATA.md`... A repo with no such file holds no exceptions."* The standard file set
(lines 48–100), `docs/build/templates/docs/` and `skills/create-repo/SKILL.md` do not mention the
file. The delta's changelog admits children keep the old sentence "until someone updates them"; the
board index has no item for it (grep: 630, 1120, 1340 only), and the constraint sits outside the
stamped block, so no pin bump carries it. Read as written, every private child today "holds no
exceptions", which is false by the standard's own account of private repos. *Counsel:* add the
file to the file set and the scaffold; soften the sentence to a duty ("must hold none"); one board
item for the children's sentence and list.

**PCL5 — minor — A pointer that reaches no rule (V5).** The standard (lines 208–209): *"The guard
rules for the marker that pairs with an entry are in `method/GUARDS.md`."* GUARDS.md holds no
rule about a marker pairing with a list entry (grep entry/register/personal: lines 197, 270, 456,
590 — a reasoned marker brings context inside the window; a marker lowers a blocking finding to
nothing; the register replaces the rest). The nearest rule says the opposite of "a marker is not a
grant" for the checks it governs. *Counsel:* point at the rule meant, or state it in the standard.

**PCL6 — minor — PD5 states a rule history already breaks, undisclosed.** PD5: *"commit headers
only. It is not a licence for the same details in a commit message body."* A count over all
commit bodies (no body read): the email once, the account name four times. The list's own
*Records* paragraph says history keeps what a push published; PD5 should say the same of bodies.
*Counsel:* one clause: bodies before this date hold both; none may be added.

**PCL7 — minor — One live surface still names the old boundary (V3).**
`docs/method/COMMUNICATION.md:172`: *"the no-personal-data boundary"*, a live doctrine sentence
naming a rule the delta replaced. The other hits (`COMMUNICATION.md:25`, `TOOLBOX.md:26`, the
2026-07-15 ADR, `CHANGELOG.md`) are history or a quoted correction and stand.

### Follow-up checklist

- [ ] PCL1 — put PD2–PD5 to the principal; cite his words; settle the *his call* form.
- [ ] PCL2 — close the unscoped-marker route in the test, `pdlistscan` or `leakscan`.
- [ ] PCL3 — the private-repo sentence in both child templates.
- [ ] PCL4 — the list file in the file set and scaffold; a board item for the children.
- [ ] PCL5 — repoint or restate the GUARDS reference.
- [ ] PCL6 — PD5's clause on bodies already in history.
- [ ] PCL7 — `COMMUNICATION.md:172`.
- [ ] Not this delta: `pdlistscan` (`6607c0eb`) has its own pass queued (`1340`); PCL2 bears on it.

Every finding is the principal's to decide (rule 3); nothing applied. Act 2 (`### Reconcile`)
follows once the sibling is released.

### Reconcile (act 2, written 2026-11-16 UTC, after the act-1 commit `e5b187a1`)

**Overall, restated: FAIL — 1 MAJOR, 3 MODERATE, 3 minor, 0 notes (PCL1–PCL7).** Nothing in
act 1 is revised; PCL7 is extended here and the extension is marked.

**Opened at act 2:** the held sibling (one pointer block, three questions, one fact, the
brief-writer's re-run results); the queue pointer `1120` and the intent record `630` whole; the
prior verdict `docs/reviews/2026-10-04-2215-pii-by-purpose-cold.md` (PI1–PI11, its follow-ups);
the delta's commit body (`git log -1 --format=%B 920cfed1`). Two further probes ran, named below.
No session log was opened: nothing a finding needed was there.

**The pointer's two questions.**

- *Whether the test can be satisfied while personal data stands unlisted:* yes, by two routes,
  one by design and one not. By design, data the list never pins (PD4, PD5, and any name nobody
  listed) is left to the leak scanner, and the list and `pdlistscan` say so. Not by design: PCL2,
  where an unscoped marker makes the leak scanner stand aside as well, so the three gates agree
  on green over an unlisted address. The answer to the pointer's question is PCL2.
- *Whether the private-repo grant wording follows his 2026-10-03 words:* the intent record now
  carries his second answer of 2026-11-09, *"Ordering the work is permission"*, re-put in plain
  terms, which it records as confirming the wording the standard carries. So the wording in the
  standard is answer-backed, and act 1 raised no finding on it. PCL3 is the mirror, not the
  wording: the answer-backed sentence reaches no child.

**The brief-writer's three questions.**

1. *The unit of "listed":* a backticked string under an entry's `Data`, matched as a
   case-sensitive substring of each tracked text file. Not counted: a case variant, a given name
   alone (PD4), a wrapped name across a line break, a commit header or body, a binary. Probed at
   act 1 (0 case variants, 0 binaries) and at act 2 (0 wrapped full names outside named places),
   so none of these holds a leak today; the gap that does matter is the marker, PCL2.
2. *Does the private-repo grant stay narrow once a session judges what the work needs:* the
   standard gives it the purpose test (a placeholder or an invented example would fail it) and
   the duty to mark the judgement as the session's own call and ask when unsure, which is as
   narrow as an unreadable grant can be made in prose; no scanner can read it, as `pdlistscan`
   says. The duty is only as good as its reach, and it reaches no child: PCL3.
3. *Every surface the old claim stood on, stamped copies included:* the sweep reached PI6's list
   except one (`tools/licenscan.py`, below) and did not reach `COMMUNICATION.md:172`; stamped
   copies in children were not read by this pass (read-only, counted) and the delta's own account
   says they keep the old sentence: PCL4, PCL7.

**The held-back fact** (the first name unpinnable) matches act 1's A3 and the test's `UNPINNED_IDS`;
nothing changes.

**Re-run results against the brief-writer's:** identical in kind (11 OK; CI exit 0 with the
`secretscan` advisories; hook exit 0); mine at `be9b3ad0`, with `pdlistscan` in the floor since.

**Per finding, against the prior verdict, the intent record and the author's account.**

- **PCL1 (MAJOR) — new.** PI2's counsel was the sentence the delta wrote ("in his words, and the
  list is closed until he adds to it"), and the commit body says the standard and `CLAUDE.md`
  carry it. Nothing in the intent record, the pointer or the body says PD2–PD5 were put to him,
  and his answer of 2026-11-09 picked the shape of the rule, not the entries. The *his call* form
  is the delta's own addition; no counsel asked for it. Stands as new, MAJOR.
- **PCL2 (MODERATE) — new.** The intent record lists "a scanner that enforces the closed list" as
  not done, for him, and then records `pdlistscan` landing; the prior verdict's probes B, C and G
  (PI2) showed a scoped marker with a thin reason passing the guard, and the delta's test closes
  that form. The unscoped form was not probed then and is not counted now. Stands.
- **PCL3 (MODERATE) — new; partly foreseen.** PI7 said a child reading only its stamped template
  does not get a complete rule; the author's account says PI7 was taken and the changelog says a
  child now gets the whole rule. The half missing is the half his second answer added after PI7
  was written, so the overclaim is the delta's. Stands.
- **PCL4 (MODERATE) — half recorded, half new.** The intent record holds "whether the rule moves
  into the stamped floor block" as open, for him, and the changelog says children keep the old
  sentence; neither is a board item, so a reader of the board finds no owner. The file-set,
  templates and scaffold gap is new. Stands; counsel unchanged.
- **PCL5 (minor) — derived from PI3's counsel.** PI3 asked the standard to "cite `GUARDS.md` for
  what binds now and name the register as the coming home", and the delta did exactly that. The
  sentence overstates what the citation reaches; the defect is the wording, not the counsel.
  Stands as minor.
- **PCL6 (minor) — new.** PI1 noted the commit-header identity is "a record, though not one where
  it appears"; the delta's PD5 records it and adds the bodies clause. Stands.
- **PCL7 (minor) — extended at reconcile, marked as such.** PI6 named `tools/licenscan.py`'s
  docstring among the eleven surfaces; the delta's path list omits that file, and at HEAD its
  lines 5 and 10 still read "keeps personal/estate data out" and "no personal data", the absolute
  form the delta replaced elsewhere. So PI6's sweep is ten of eleven, plus `COMMUNICATION.md:172`,
  which PI6 did not list. Severity unchanged (minor); the follow-up gains one file.

**The author's account** (commit body and changelog) is accurate on what it changed and honest on
what it left: it names the scanner as not done and the children as not updated. Where it is
stronger than its evidence is the three places act 1 names (V1), none of which the body itself
asserts; the "whole rule" claim is the changelog's.

**Follow-ups, restated:** PCL1–PCL7 as listed above, with PCL7 now also naming
`tools/licenscan.py` lines 5 and 10. The cycle stays open (a MAJOR stands); every finding is the
principal's to decide (rule 3), nothing applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

The text below is the brief's held-back sibling,
`2026-11-09-0153-personal-data-closed-list-cold.deferred.md`, copied verbatim. It was removed from
the review worktree before the reviewer started, held outside the tree until act 1 was committed
(`e5b187a1`), then released to the reviewer for act 2. The orchestrator forms no finding and has
not edited it; the sibling file itself is deleted in the fold commit, so the brief's mentions of it
by name now point here.

# Deferred reading for `2026-11-09-0153-personal-data-closed-list-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether the test can be satisfied while personal data stands unlisted; whether the private-repo
grant wording follows his 2026-10-03 words.

## The brief-writer's questions

1. What is the test's unit of "listed", and what spelling of a listed datum would it not count?
2. Does "the principal's order for the work is the grant" stay narrow once a session has to judge
what the work needs?
3. Every surface the old claim stood on: did the sweep reach them all, including stamped copies?

## What the brief-writer held back

- One entry (the first name used as the doctrine's voice) is stated as unpinnable; the changelog
  says so.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`test_personal_data`: 11 tests, OK, exit 0. `floor.py --plane ci`: exit 0, with 28 `secretscan`
advisories reported and not blocking. `--plane hook`: exit 0.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/1120 cold pass (personal-data closed list)

Reviewer: Fable 5.1 (claude-fable-5-1). Spawned by a headless Opus 5.5 orchestrator under drain
session 1e053526. Worktree: /Users/mike/worktrees/fable/atelier-160-1120-0742/atelier (HEAD be9b3ad0,
origin/main). Sibling .deferred.md deleted from the worktree on purpose; not sought.

## Act 1

- 2026-11-16T07:43Z `uptime` -> load 3.39/2.91/2.97 (16 GB laptop, several passes running). OK to
  proceed under nice.
- `git status --short` -> only ` D docs/reviews/...deferred.md`. `git log --oneline -3` -> be9b3ad0
  claim commit on top of 160/1170 fold.
- Read the brief in full (lines 1-220): acceptance test = principal's answers "Honest claim + only
  you grant" and "Ordering the work is permission"; delta = commit 920cfed1, 16 paths; re-run lines
  = unittest test_personal_data, floor.py --plane ci, floor.py --plane hook; bars = ROADMAP-DONE,
  SESSIONS, sessions/, docs/reviews/ prior verdicts, sibling, commit bodies, queue pointer 1120,
  intent record 630 beyond title.
- Read `docs/method/REVIEW.md` lines 25-301 (rules 1-4), 302-566 (lenses, re-run, V1-V7,
  lifecycle, method record). Verdict shape taken from there.
- `git merge-base --is-ancestor 920cfed1 HEAD` -> exit 0.
- Delta read body-free: `coldsweep.py --root . --commit 920cfed1 --path <16 paths>` -> 780 lines to
  scratch /tmp/pcl-delta.txt, read whole. coldsweep footer: subject, stat and diff of 16 files;
  body not printed; 0 board files; 0 rule-2 files touched.
- `git log --oneline 920cfed1..HEAD -- <16 paths> | wc -l` -> 76 (brief said 27 at 457615cc).
  `docs/PERSONAL-DATA.md` and `tools/test_personal_data.py`: 0 commits since the delta.
  `docs/build/REPO-STANDARD.md`, `CLAUDE.md`: no personal/grant lines changed since (git diff grep).
  Templates CLAUDE.md/CONTRIBUTING.md changed since (40+/23-), none of it the personal-data rule
  (diff read line by line; hunks are the floor stop list, the asking device, cclive, the pin check,
  the root-naming rule, the review step, claim JSON).
- Subjects since on these paths that touch the subject: 6607c0eb "pdlistscan: in a public repo,
  personal data stands only where the closed list names it" (the scanner follow-up the delta left
  open), 1b4d51f8 principles §9. pdlistscan landed 6607c0eb; its own pass is board 1340 (index).
- CI: `.github/workflows/ci.yml:108` runs `python3 -m unittest discover -s tools -p 'test_*.py'`,
  so test_personal_data is in the suite CI runs. floor.py does not run tests (grep: 0).
- Lens 1 assumptions I named: A1 the test sees every tracked file (binary/case) · A2 the test runs in
  a gate · A3 "closed" is enforced · A4 globs anchor · A5 the marker check covers every
  personal-data allow-marker · A6 the list's own grants meet the grant rule it states · A7 mirror
  sites carry the whole rule (templates, standard file set, create-repo) · A8 pointers reach the
  rule they cite (GUARDS, ADR 0005/0007, register draft, AUTONOMY) · A9 the list's places pass the
  purpose test · A10 PD5's commit-body claim matches history.
- A1 probe (/usr/bin/python3 over `git ls-files`): 1402 tracked, 0 binary, 0 case-variants of the
  three pinned strings. Sound.
- A4: `glob_rx` appends `\Z`, `re.match` anchors the start; `*` stays in a segment. Sound.
- A5 probe: `tools/leakscan.py:107-109` grammar: `leakscan:allow: <reason>` (unscoped) exempts
  every STRUCTURAL rule; `MARKER_RX` in the test needs `allow:<scope>:` so the unscoped form is
  invisible to it; test docstring says it "is counted separately" (nothing counts it);
  pdlistscan docstring says the unscoped form "is the leak scanner's to judge" but leakscan honours
  it. Scratch probe: `git clone` of the worktree to /tmp/pcl-scratch/clone, added
  `docs/method/ZZ-PROBE.md` holding an example.org email + `<!-- leakscan:allow: probe reason -->`,
  `git add` in the clone only. `python3.14 -m unittest test_personal_data` -> 11 tests OK;
  `leakscan.py --root . docs/method/ZZ-PROBE.md` -> exit 0, "allow-marker breakdown: email×1";
  `pdlistscan.py --root .` -> clean, exit 0. Three gates green on an email in an unlisted file.
  Scratch removed after. Tree today: unscoped markers outside tools/ and instruments/ at
  CHANGELOG.md:2753,2764,3263; docs/method/SIGNING.md:120 (a vendor noreply address);
  docs/roadmap/110-.../README.md:26 (a PCIe lane string); skills/create-repo/instance.yaml.example:16
  (an RFC 2606 placeholder). None personal; the route is open, not used. -> candidate PCL2.
- Scoped personal markers outside tools/ and instruments/ (coldsweep, file only): CHANGELOG.md,
  CLAUDE.md, docs/PERSONAL-DATA.md, docs/roadmap/115-.../230-...md. All in PD1/PD2/PD3 named places
  (CHANGELOG.md, CLAUDE.md, docs/PERSONAL-DATA.md, docs/roadmap/**). Sound.
- A6: `docs/PERSONAL-DATA.md` "Granted by": PD1 his words 2026-10-03 (quoted in REPO-STANDARD,
  verified at lines 177-190); PD2-PD5 "his call" citing ADR 0005. ADR 0005 lines 28-70 read: an
  agent-written decision record, "accepted knowingly", "the name is attribution"; grep for
  quoted words of him (`*"`, "verbatim", "his words") -> see next call. The standard's rule
  (REPO-STANDARD lines 198-203): "In a public repo only the principal grants an exception, in his
  own words, and the list is closed until he adds to it... it never adds an entry itself." The
  list's own "Granted by" paragraph defines "his call" to admit a decision record. -> candidate
  PCL1.
- A7: child template CLAUDE.md lines 147-160 and CONTRIBUTING 109-113 at HEAD carry the default,
  purpose test, list file, public-repo grant and marker-not-a-grant; NEITHER carries the
  private-repo half ("the order for the work is the grant; record, mark as own call, ask when
  unsure", REPO-STANDARD lines 201-203). CHANGELOG delta entry claims "a child reading only its
  own files gets the whole rule". -> candidate PCL3.
  REPO-STANDARD "The standard file set" (line 48-100): no `docs/PERSONAL-DATA.md`; `ls
  docs/build/templates/docs` -> no PERSONAL-DATA template; create-repo SKILL.md grep -> no mention.
  Standard line 204-207 says "One list per repo... A repo with no such file holds no exceptions".
  -> candidate PCL4.
- A8: GUARDS.md grep personal/entry/register: line 197 (a reasoned marker brings context inside
  the window), 270, 456 (a marker lowers a blocking finding to nothing), 590 (register 110/100
  replaces it). No rule about a marker pairing with a list entry. Standard line 208-209 says "The
  guard rules for the marker that pairs with an entry are in method/GUARDS.md". -> candidate PCL5
  (V5 pointer reaches no such rule). ADR 0007 names allowed_signers (lines 20,47,69) - sound.
  Register draft (decisions/2026-10-03-0641) is a draft, "Mike rules on acceptance", owes 160/1130;
  the standard calls it "where the per-exception record is heading" - honest, sound. AUTONOMY lines
  45-57: making public / widening is a floor action - sound.
- A9: `mike548141` in tools/floorfleet.py:1595,1604, tools/test_floorfleet.py:57,124,
  tools/test_templates.py:131,197: the owner-classifier and the template's real workflow address;
  a placeholder would not serve (the classifier tells the real owner from a fork). Sound.
- A10: `git log --format=%b | grep -c` (counts only, no body read): email 1, account name 4.
  PD5 says "commit headers only. It is not a licence for the same details in a commit message
  body" while history holds one body with the email. -> candidate PCL6 (minor).
- Old framing sweep (coldsweep, pattern shareable repo|no-personal-data|declared where it
  appears|declared allowance|repo that can go public|fewest exceptions): live hits
  docs/method/COMMUNICATION.md:172 "the no-personal-data boundary" (a live doctrine sentence);
  COMMUNICATION.md:25 and TOOLBOX.md:26 are a quoted correction; the rest are history (CHANGELOG,
  ADR 2026-07-15) or the test's own stale-phrase list. -> candidate PCL7 (minor, V3).
- Re-run 1: `cd tools && nice -n 10 python3.14 -m unittest test_personal_data` -> Ran 11, OK, exit 0.
- Re-run 2: `nice -n 10 python3.14 tools/floor.py --plane ci --root .` -> exit 0; 167 lines; every
  scanner ✓ incl. leakscan (structural + local) and pdlistscan; pointerscan ⚠ 4 queue-state on
  items 1080, 1250, 1420, 994 (other passes' claims, not this delta).
- Re-run 3: `nice -n 10 python3.14 tools/floor.py --plane hook --root .` -> exit 0; 99 lines; all ✓;
  same pointerscan ⚠. `uptime` before the heavy runs: load 2.68.
- Register parse check: see next call (ids, pinned counts, place globs).
- ADR 0005 grep: 0 lines with a quotation of him (`*"`), 0 "verbatim"/"his words". PD2-PD5 rest on
  an agent-written record. PCL1 confirmed.
- Register parse (python3.14, import test_personal_data): PD1 1 string / 17 globs, PD2 1 / 5,
  PD3 2 / 5, PD4 0, PD5 0; matches the file. A4 confirmed.
- Verdict appended to the brief below `---` at 2026-11-16T07:52Z: FAIL, PCL1 MAJOR, PCL2-PCL4
  MODERATE, PCL5-PCL7 minor. Status line updated. Findings in order of severity: PCL1 grant form
  "his call" vs "in his own words"; PCL2 unscoped-marker route (probe above); PCL3 private-repo
  half absent from child templates; PCL4 list file absent from file set/templates/scaffold, no
  board item; PCL5 GUARDS pointer; PCL6 PD5 vs commit bodies; PCL7 COMMUNICATION.md:172.
- Gates on the brief (python3.14 tools/<gate>.py --root . <brief>): datescan 0, spellscan 0,
  wrapscan 0, linkscan 0, leakscan 0 (structural + local), reviewscan 0, attribscan 0. Lines over
  100 columns: only in the brief-writer's part (title, two command lines, table rows); none in the
  verdict's prose beyond table rows.
- Left out and why: child repos (not needed for a finding; read-only, counted); `/security-review`
  (landed delta, nothing pending but the removed sibling); the sibling, prior verdicts, session
  logs, commit bodies, items 630/1120 (rule 2, until act 2). Scratch /tmp/pcl-scratch removed;
  /tmp/pcl-*.txt are command captures of this repo's own output, no live captures.
- ACT 1 SAVED 2026-11-16T07:5xZ. Waiting for the orchestrator's release of the sibling for act 2.

## Act 2 (released by the orchestrator after e5b187a1)

- Opened: the held sibling at the orchestrator's path (3 questions, 1 fact, pointer block,
  re-run results at 457615cc: 11 OK / ci 0 / hook 0); `git log -1 --format=%B 920cfed1` (body:
  PI1/PI2 account, "PI3-PI10 take the reviewer's counsel", "no scanner behaviour changed");
  queue pointer 1120 whole; intent record 630 whole (his two answers of 2026-11-09; "Not done,
  for him": scanner, stamped-block move, private-repo wording; pdlistscan landed);
  prior verdict 2026-10-04-2215 lines 363-500 (PI1-PI11) and 531-546 (follow-ups).
- Probe: wrapped full name across a line break (/usr/bin/python3 regex over git ls-files) -> 0
  hits outside named places. Probe: `grep -n -i "shareable|go public|personal" tools/licenscan.py`
  -> lines 5 and 10 still carry the absolute form; licenscan.py is not in the delta's 16 paths
  though PI6 listed it. PCL7 extended at reconcile (marked), severity unchanged.
- Reconcile appended; overall restated FAIL (1 MAJOR, 3 MODERATE, 3 minor). PCL1, PCL2, PCL6 new;
  PCL3 new/partly foreseen by PI7; PCL4 half recorded in the intent record (no board item); PCL5
  derived from PI3's counsel. Act-1 text untouched.
- Gates re-run on the brief: see the command output in the session (all expected 0).
- ACT 2 SAVED. Sibling not folded or deleted (the orchestrator folds).
