# Cold pass — held-back review notes leave the shared scratch (160/380), a dated rule carries a readable kind (160/450), and a repo declares its visibility (260/050)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (doctrine by
function: review doctrine, the floor and the fleet view).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN 2026-11-16 UTC, acts 1 and 2, by a Fable 5.1 reviewer under a headless
Opus 5.5 orchestrator started by drain session `1e053526`: PASS-WITH-FINDINGS (verdict and
reconcile below; the held-back sibling and the review log are folded below them).
Brief written 2026-11-09 UTC by session `d16dc612`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1180-rule-4-cold-pass-queued-review-notes-date-kind-and-visibility.md`
(barred until phase 2).
**Size:** large: three subjects in four commits across doctrine, `floor.py`, `floorfleet.py` and
`coldsweep.py`, with a live check against GitHub in CI to reason about.
**Why it earns a review:** The first subject is about the independence of every cold pass. The
second decides how checkers read a dated rule across children. The third is meant to notice a
private repo turned public.

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

The principal's answers, 2026-11-09, verbatim, each a pick from offered options: on `160/380`,
*"Keep it out of that folder"* (held-back review notes never live in the orchestrator's scratch
folder; the rule says where they go); on `160/450`, *"Add a readable label"* (each dated rule
carries a `mandate` or `default` kind the checkers read; existing dates get labelled); on `260/050`,
*"Yes, with the loud alert"* (each repo declares its visibility in its floor config, cross-checked
against GitHub, public repos get the stricter checks, and a says-private-is-public mismatch is red).
He added the same day that this builds on the daily visibility check filed under `390/020`, never a
second one.

The offered option's words were written by the authoring session and put to the principal; the
quoted pick is his. Recorded as an answer, not a ruling in his words: where the delta's wording goes
past what he picked, say so. These are claims to test, not settled scope.

## What the work is

Four commits on `main`: `d7abac17` and `595db812` (`160/380`), `db2c39f9` (`160/450`), `c4424324`
(`260/050`). `CHANGELOG.md` is in the last.

Commits on `main`: `d7abac17`, `db2c39f9`, `c4424324`, `595db812`. The landing commit is `595db812`.
**Check your tree has it before reading anything:** `git merge-base --is-ancestor 595db812 HEAD`
exits 0, and an orchestrator merges `origin/main` into the review branch before it spawns.

Delta paths: `docs/method/CONCURRENCY.md`, `docs/method/REVIEW.md`, `docs/method/GUARDS.md`,
`docs/method/PROPAGATION.md`, `docs/build/REPO-STANDARD.md`, `docs/build/templates/CONTRIBUTING.md`,
`skills/review-brief/SKILL.md`, `tools/README.md`, `tools/floor.py`, `tools/floorfleet.py`,
`tools/coldsweep.py`, `tools/test_floor.py`, `tools/test_floorfleet.py`, `tools/test_coldsweep.py`,
`.atelier-floor.json`, `CHANGELOG.md`. Read each at HEAD and read each commit body-free, scoped to
paths so board records stay barred:

```
python3 tools/coldsweep.py --root . --commit d7abac17 --path docs/method/CONCURRENCY.md --path docs/method/REVIEW.md --path skills/review-brief/SKILL.md --path tools/README.md
python3 tools/coldsweep.py --root . --commit db2c39f9 --path docs/build/REPO-STANDARD.md --path docs/build/templates/CONTRIBUTING.md --path docs/method/GUARDS.md --path docs/method/PROPAGATION.md --path skills/review-brief/SKILL.md --path tools/README.md --path tools/coldsweep.py --path tools/floor.py --path tools/floorfleet.py --path tools/test_coldsweep.py --path tools/test_floor.py --path tools/test_floorfleet.py
python3 tools/coldsweep.py --root . --commit c4424324 --path .atelier-floor.json --path CHANGELOG.md --path docs/build/REPO-STANDARD.md --path tools/floor.py --path tools/test_floor.py
python3 tools/coldsweep.py --root . --commit 595db812 --path docs/method/CONCURRENCY.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Commits since the delta on these paths:

```
git log --oneline 595db812..HEAD -- docs/method/CONCURRENCY.md docs/method/REVIEW.md docs/method/GUARDS.md docs/method/PROPAGATION.md docs/build/REPO-STANDARD.md docs/build/templates/CONTRIBUTING.md skills/review-brief/SKILL.md tools/README.md tools/floor.py tools/floorfleet.py tools/coldsweep.py tools/test_floor.py tools/test_floorfleet.py tools/test_coldsweep.py .atelier-floor.json CHANGELOG.md
```

At `457615cc` this printed 7 commit(s). Read anything new the same way.

**Application pass.** `160/380` and `160/450` apply the principal's answers and earlier passes'
counsel. It cannot fully honour rule 2: the delta carries finding ids and the decisions stamped on
them. Sequence (`REVIEW.md` § *Applying decisions to doctrine*): review the work at HEAD and commit
findings first; open the prior verdict after. Name that residual exposure in the verdict.

**Claims the work makes (extracted from its own changelog entry and files, not evaluated):**

- `CONCURRENCY.md` § *Orchestrated queue runs* says held-back material goes in a user-local
  directory outside the repo, every worktree and any harness scratchpad, never a reviewer's working
  directory, with a close-time listing of the scratchpad root.
- `REVIEW.md` rule 1 no longer calls an orchestrator-held store structural unless the bytes never
  sit on a path the reviewer is given.
- `.atelier-floor.json` advisories take an optional `kind`; `floor.py` validates and shows it;
  `floorfleet.py` shows it and says aloud when it is missing; on the hook plane a mandate's or
  unlabelled `review-by` moving later than HEAD's is a warn-only line. No existing date is labelled
  by this change.
- `"visibility": "public" | "private"` in `.atelier-floor.json`. Inside Actions only, `floor.py`
  reads GitHub's live answer (the event payload if the API is unreachable): declared private but
  public is a red build; the reverse, an unreadable answer and no declaration all warn and never
  block. It detects and alerts and cannot stop a flip.
- `coldsweep.py` warns when an `--also-exclude` matches nothing.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** what a public declaration tightens and the daily external check, which the delta
names as `390/020`'s, except where a claim depends on them.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself, first, and damage each
with a probe or confirm it by re-driving. Ask whether this is the right problem, solved at the right
altitude.
2. **Correctness & quality** — does the work do what its claims above say; honest about done versus
stubbed; any overclaim or silent scope cut, each recorded against the text that makes it.
3. **Completeness / harvest** — every surface that states the rule (V3), one home (V4), no
contradiction with sibling doctrine (V5), tests that would stay green on a broken check, what
already exists that this ignored.
4. **Security & privacy** — mandatory. `260/050` calls GitHub from CI and turns the answer into a
red build; weigh token use and the unreachable path. `160/380` is itself a confidentiality rule for
cold passes. Aim `/security-review` at the `tools/` diff from a clean tree, or discharge it by
grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root
at `457615cc`; results are in the sibling. Read exit codes explicitly. Check `uptime` first and run
heavy lines under `nice -n 10`. Python is the `python3` on `PATH` (the tests need 3.10 or later;
`/usr/bin/python3` is 3.9 on this machine and some modules fail at import).

- `cd tools && python3 -m unittest test_floor`
- `cd tools && python3 -m unittest test_floorfleet`
- `cd tools && python3 -m unittest test_coldsweep`
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `nice -n 10 python3 tools/floor.py --plane hook --root .`
- `nice -n 10 python3 -m unittest discover -s tools`
- `gh repo view --json visibility  # read-only; run inside your worktree`
- the adopting child repos, read-only and by count only: `python3 tools/floorfleet.py --root <the
  directory that holds the main atelier checkout and its sibling clones> --json` to a scratch file,
  then the kinds and visibility the fleet view reports, by count

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
(`2026-11-09-0153-review-notes-date-kind-and-visibility-cold.deferred.md`), every delta commit's
message body, the queue pointer
`docs/roadmap/160-doctrine-review-owed/1180-rule-4-cold-pass-queued-review-notes-date-kind-and-visibility.md`,
and the intent records beyond their titles:

- `docs/roadmap/160-doctrine-review-owed/380-rule-4-cold-pass-queued-the-scratchpad-clause.md`
- `docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md`
- `docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/050-p3-the-floor-does-not-know-whether-a-repo-is-p.md`

Prior verdicts on this subject, barred until your own findings are committed (rule 2; `coldsweep`
excludes `docs/reviews/` by default): `docs/reviews/2026-09-25-0715-scratchpad-clause-cold.md`,
`docs/reviews/2026-10-03-0357-date-kind-rule-cold.md`. The delta's docstrings, comments, ADR text,
`tools/README.md` and `CHANGELOG.md` entries carry the author's account of why; they are the delta,
and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1180-rule-4-cold-pass-queued-review-notes-date-kind-and-visibility.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/380-rule-4-cold-pass-queued-the-scratchpad-clause.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/450-rule-4-cold-pass-queued-the-date-kind-rule.md \
  --also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/050-p3-the-floor-does-not-know-whether-a-repo-is-p.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, any orchestrator, what you read, the UTC day you ran on),
per-lens answers, V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (each of the four commits: read body-free
yes/no, findings by id), findings with stable ids (prefix `RNV`: `RNV1`, `RNV2`, …) and severities
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

## Verdict — act 1 (2026-11-16 UTC)

**Overall: PASS-WITH-FINDINGS** — 0 MAJOR, 3 MODERATE, 5 minor, 2 note (`RNV1`–`RNV10`).

### Provenance (rule 4, V7)

- **Reviewer:** Fable 5.1, the principal-named tier, checked at selection. Spawned by a headless
  Opus 5.5 orchestrator session, itself started by drain session `1e053526` (Opus 5.5). Both are
  rule-4 off-tier orchestrators: they hold the context partition, formed no finding and wrote no
  severity. `1e053526` wrote no brief and no delta. This pass ran on the Platform API credit lane
  under the principal's drain order of 2026-11-16; quality was not traded for cost.
- **Not started or instructed by** any barred session: `722ac2e2` and its workers, `d16dc612`,
  `74f2b8cd`. Contact after the spawn: one orchestrator message, process only (a resume after this
  reviewer's turn ended early: carry on in the foreground, use own results, disclose any helper,
  spawn no further background work). It carried no question about the delta and no pointer to
  where the risk lives.
- **Spawn prompt, in substance:** worktree path (below), brief path, the two files writable, the
  rule-2 bars (the `.deferred.md` sibling removed from the worktree on purpose, never to be sought
  in git history, other checkouts, scratch or `~/.claude`; `SESSIONS.md`, `docs/sessions/`, prior
  verdicts, the queue pointer and intent records beyond titles, delta commit bodies), load and
  live-system rules (reads only, no writes), public-repo wording rules, the act-1/act-2 shape and
  the running review log. The log is appended verbatim at the fold.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1180-0816/atelier`, read-only except this
  file. `git merge-base --is-ancestor 595db812 HEAD` exits 0. HEAD is 60 commits past the landing
  commit on the delta's paths (the brief counted 7 at `457615cc`); the delta's hunks were checked
  for drift by function (none on the three features; one later comment at `floor.py:1137`).
- **What was read:** the brief; `REVIEW.md` rules 1–4, lenses, V1–V7 and the lifecycle; the four
  commits body-free through `coldsweep.py --commit` (ledger below); the delta's files at HEAD; the
  board index `docs/ROADMAP.md` and three board items that are not barred (`390/020`, `180/120`,
  `180/200`) to check cross-references; `skills/review-drain/orchestrator-prompt.md`,
  `docs/method/session-open/dispatch-brief.md`, `.github/workflows/floor.yml` and the child
  template workflow. **Not read:** the session log, `docs/sessions/`, any prior verdict, the queue
  pointer, the three intent records beyond their titles, any commit body, the sibling.
- **Helper disclosed:** one in-process subagent (Agent tool, Haiku) was spawned for a single
  measurement (its own session id and whether a scratchpad path was named to it). No finding rests
  on its output; it informs the nuance in `RNV7`, which also rests on this reviewer's own
  environment. No other helper; no background work after the orchestrator's instruction.
- **Residual exposure, named:** the delta carries finding ids (`SK1`, `SK9`, `DK1`, `DK2`, `DK8`,
  `DK9`, `DK11`) and the principal's answers; the brief said so. The board index showed item
  titles only. Nothing read gave an evaluative account of the work.

### Method

Order: brief in full; `REVIEW.md` for the verdict shape; tree and landing-commit check; the four
commits body-free; the delta's hunks at HEAD and their drift; mirror sites by `coldsweep` sweeps
(`"visibility"`, `reads as a mandate`, where deferred siblings are held); the workflow that runs
the floor in CI; the re-run list; probes (below); then findings. Left out: 56 of the 60 later
commits on the delta's paths, read only as subjects; the whole-suite run's result, which had not
landed when this act was written (see the re-run ledger). Every command and what it returned is in
the review log, appended at the fold.

### Lens 1 — approach and load-bearing assumptions

- **A1 (`260/050`): "the live API answer wins over the event payload."** Damaged. The code reads
  `GITHUB_TOKEN` from the environment; the house workflow's floor step exports no token, and Actions
  exports none by default. Unauthenticated, a private repo's `GET /repos/<slug>` is a 404 (curl:
  nonexistent slug → 404, the same answer a private repo gives), so the live read fails and the
  payload answers for exactly the repos the check exists for; a public repo's read shares the
  runner IP's 60-per-hour limit (curl: `x-ratelimit-limit: 60`). `RNV1`.
- **A2 (`160/450`): "an unlabelled date reads as a mandate, the stricter reading."** Damaged in
  substance. The one fleet date on record, the C1b horizon, was ruled a default (GUARDS.md's own
  grounding, 2026-08-09); every dated advisory in the fleet is unlabelled (4 of 4); so the tool
  now reads ruled defaults as mandates. `RNV2`.
- **A3 (`160/380`): "every agent is handed the orchestrator's own scratchpad."** Confirmed for an
  in-process subagent (the helper's session id equalled this reviewer's; its output landed under
  this session's task directory); not true of a headless child session (this reviewer has its own
  session id and its own spill, keyed by it). The rule's conclusion survives on the same-user
  reachability the doctrine already states; the premise is narrower than written. `RNV7`.
- **A4: the fleet board shows what the floor config declares.** Damaged for `visibility`: the
  board does not read the key. `RNV3`.
- **Right problem, right altitude?** Yes for all three: a read surface named as such, a label the
  checkers read, a declaration checked against the live state. The acceptance picks are met in
  shape; the gaps are in wiring (`RNV1`), in the default the label takes (`RNV2`) and in the one
  view that would show the declaration fleet-wide (`RNV3`).

### Lens 2 — correctness and quality, claim by claim

- `CONCURRENCY.md` § *Orchestrated queue runs*: says what the changelog claims; the "one command"
  test of whether the rule is spent was re-driven (A3) and gives "shared" for the subagent shape,
  as the text says it did on 2026-09-25. The claim that the 2026-09-25 batch held twenty siblings
  in the scratchpad and moved them is in barred records and was not re-run.
- `REVIEW.md` rule 1: the qualified "structural" wording is present at HEAD (lines 92–105) and
  agrees with `CONCURRENCY.md`. Rule 2's "four times" matches `tools/README.md`.
- `floor.py` `kind`: validated (`DateKindTest`, 255 tests green), shown on the line and in
  `--json`; `moved_later` reports and never blocks (test re-run). Doctrine says it compares the
  *staged* date; the code reads the working tree. `RNV5`.
- `floorfleet.py` `kind`: shown; "date kind not recorded" said aloud (127 tests green).
- `coldsweep.py` empty `--also-exclude`: warns on the pattern path (56 tests green); silent in
  `--commit` mode. `RNV6`. The brief's own sweep command: all four bars matched files, no warning.
- `visibility`: key validated; the breach case is the one red and renders the loud block
  (`VisibilityDeclarationTest` green). Live path re-driven from this machine only as far as the
  unreadable-answer branch (🟡, exit 0, as claimed); TLS verification fails for the stock python
  here, an environment limit, so the 200 path was re-driven with curl.
- Honesty: "Not built" lines are present for the house-date declaration and the daily check. The
  changelog calls the dispatch-sentence mirror "owed" in the queue-run prompt and skill, which hold
  no rule; the actual mirror site already existed. `RNV8`.

### Lens 3 — completeness and harvest

- The acceptance pick on `160/450` reads "existing dates get labelled"; none were, no ask to the
  principal was queued, and the board index holds no item for it. `RNV2`.
- `create-repo` scaffolds no `visibility`, so every new repo starts 🟡 in CI. `RNV4`.
- A test that stays green on a broken check: the hook-plane date note has no render test. `RNV9`.
- What already exists that this ignored: `session-open/dispatch-brief.md` (landed 2026-11-03,
  `180/120`) is the copyable home of the scratch obligation; the delta's recipe did not reach it
  and the changelog pointed elsewhere. `RNV8`.

### Lens 4 — security and privacy (V6)

Threats enumerated for the new code: (1) token exfiltration — the slug is validated before any
URL is built and the URL is a literal `https://api.github.com/...`; no token is wired today
(`RNV1`); if one is, `urllib` forwards `Authorization` on a redirect to any host (CPython
`redirect_request` drops only content headers, checked on the python on `PATH`), so the wiring
should pair with a redirect-refusing opener; (2) rate limit or outage — falls through to the
payload, then to 🟡, never red, confirmed by test and by the re-drive; (3) a spoofed event payload
— `GITHUB_EVENT_PATH` is runner-owned; a forked PR cannot change the caller's repository object;
(4) red-build denial of service — only a declared-private-but-public repo reds, which no outsider
can cause; (5) privacy — a private repo's `"visibility": "private"` line and the `::error` text
carry no secret and no personal data; the `160/380` rule itself tightens confidentiality and says
honestly that a same-user machine is no partition. `/security-review` **discharged by grounds**:
it reads the session's pending diff, which here is this brief and a deleted sibling, never the
landed delta; the code surface (one HTTPS GET, one `git show`) was read by hand against the list
above. Over markdown its pass would be empty in any case.

### Standing checklist

- **V1** — one overclaim found (`RNV5`, "staged"); one premise wider than its evidence (`RNV7`).
- **V2** — every re-run line re-run (ledger below); the live API read re-driven as far as this
  machine allows and the gap named.
- **V3** — mirrors swept: `GUARDS.md`, `PROPAGATION.md`, `REPO-STANDARD.md`, the CONTRIBUTING
  template, `floor.py` docstring, `floorfleet.py`, `tools/README.md`, `CHANGELOG.md` all state the
  kind rule the same way; `create-repo` and `dispatch-brief.md` are the two mirrors missed
  (`RNV4`, `RNV8`).
- **V4** — one home each: the kind rule in `GUARDS.md`, the scratch rule in `CONCURRENCY.md`, the
  visibility rule in `floor.py`'s docstring with `REPO-STANDARD.md` pointing at it. Held.
- **V5** — cross-references checked for the rule reached: `390/020` holds the daily-check answer
  (read; the item is not barred); `REVIEW.md` rule 1 ↔ `CONCURRENCY.md` agree; `docs/sessions/
  2026-09-20-1053-…` exists (not read). One contradiction: the mandate default against the ruled
  default (`RNV2`).
- **V6** — above. **V7** — provenance stated in the brief and repeated above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `d7abac17` (`160/380`) | yes, `coldsweep --commit`, 4 files | `RNV7`, `RNV8` |
| `db2c39f9` (`160/450`) | yes, 12 files | `RNV2`, `RNV5`, `RNV6`, `RNV9` |
| `c4424324` (`260/050`) | yes, 5 files | `RNV1`, `RNV3`, `RNV4`, `RNV10` |
| `595db812` (`160/380`) | yes, 1 file | none |

### Findings

**RNV1 — MODERATE — the CI visibility check never has a token, so its designed live read is
dead for private repos.** `github_visibility()` reads `GITHUB_TOKEN` from the environment
(`tools/floor.py` 2507–2531). `.github/workflows/floor.yml`'s "scanner floor" step (lines
133–134) exports no `env:`; the only token in the file is `GH_TOKEN` on the signature step; the
child template exports none; Actions does not export the token by itself. Unauthenticated, a
private repo answers 404, so the branch the docstring calls the point ("the state NOW", defeating
a replayed payload on a re-run) falls through to the payload for every private repo, and a public
repo's read shares the runner IP's 60-per-hour limit. The result line does not say which source
answered, so "GitHub agrees" from a stale payload reads the same as a live read. The test passes a
token under a name the workflow never sets, so it stays green with the wiring absent. Rule: V1
(claim stronger than its evidence), lens 3 (a test that stays green on a broken check).
*Counsel:* add `env: GITHUB_TOKEN: ${{ github.token }}` to the floor step of the reusable
workflow (children call it, so one edit reaches the fleet); have the result say `live` or
`payload`; when a token travels, use an opener that refuses redirects.

**RNV2 — MODERATE — "an unlabelled date reads as a mandate" reads the fleet's ruled defaults as
mandates, and the labelling the acceptance pick asked for was neither done nor queued.** GUARDS.md
413–418 sets the default and its own grounding (437–441) records the one fleet date ever ruled, the
C1b horizon, as a **default**. Fleet count (direct read, 22 configs): 4 dated advisories, all
unlabelled, 0 mandate, 0 default. So the board tells each of them "reads as a mandate until the
principal says", and a child extending one gets a hook line saying it may not, for a date class he
ruled may be extended. The same subsection says such a date "has no kind on record", which the
grounding paragraph contradicts. The pick ("existing dates get labelled") is unmet; the changelog
says labelling "needs the principal" but no ask was queued and the board index has no item. Rule:
V5, the acceptance test, rule 3 (an answer applied past what was picked). *Counsel:* one board
item listing the 4 dates with their origin, asking him to label each; and, until then, have the
unlabelled reading say "kind not recorded" without a mandate reading, or keep the mandate reading
only for dates that are not C1b-derived. His call which.

**RNV3 — MODERATE — the fleet board cannot show `visibility`, so 12 of 22 repos' silence is
invisible fleet-wide.** `floorfleet.py` does not read the key (grep: no hit). `floor.py`'s
docstring (lines 138–140) says the board shows the declarations "so … is a visible board state
rather than an absence nobody can see"; `REPO-STANDARD.md` lists `visibility` among what the
config decides; the brief's re-run line assumed the fleet view reports it. Today an undeclared
repo surfaces only as one 🟡 line inside its own CI log. Counts: public 4, private 6, absent 12.
Rule: lens 3 (harvest), V4 (the board is the declarations' one view). *Counsel:* read the key in
`_read_declarations`, print it per repo, say "not declared" aloud as the kind line does.

**RNV4 — minor — `create-repo` scaffolds no `visibility`, so every new repo starts 🟡.** The
skill's instance profile already carries the remote's visibility (`instance.yaml.example` line
21; `SKILL.md` 79, 225), so the value is in hand at scaffold time. Rule: V3. *Counsel:* write the
key from the profile when the floor config is scaffolded.

**RNV5 — minor — GUARDS.md says the hook compares the *staged* `review-by` with HEAD's; the code
compares the working tree.** `moved_later` takes `cfg` from `Config.load(root)`, which reads the
file on disk (`floor.py` 2076); the delta's own test writes the new config and never stages it,
and expects the note. A date edited but not staged is reported as moving; a date staged then
reverted on disk is not. Rule: V1. *Counsel:* either read `:.atelier-floor.json` from the index
on the hook plane, or say "the working tree's" in GUARDS.md 420.

**RNV6 — minor — the empty `--also-exclude` warning does not fire in `--commit` mode.**
`coldsweep.py` 421 returns from `show_commit` before the walk at 426 where the check sits
(429–438). A brief that pairs `--commit` with a mistyped bar gets silence, the case DK9 was about.
Rule: lens 2. *Counsel:* run the check in `show_commit` too, against the tree.

**RNV7 — minor — "every agent is handed the orchestrator's own scratchpad" is true of in-process
subagents and not of headless child sessions.** Probe: a subagent spawned by this reviewer
reported the same session id and its output landed under this session's task directory
(shared); this reviewer, a headless child, has its own session id and its own spill keyed by it
(not shared). `CONCURRENCY.md` 1002–1004 says "every agent". The conclusion stands on the
same-user clause the text already carries. Rule: V1. *Counsel:* "every in-process subagent", and
keep the same-user sentence as the operative reason.

**RNV8 — minor — the recipe's mirror site exists and the delta neither updated nor named it.**
`docs/method/session-open/dispatch-brief.md` (landed 2026-11-03, `180/120`) is the copyable home of
the scratch obligation; its line 19 says "unique to this worker" and nothing of
`<orchestrator scratchpad>/<worker-name>/`. The changelog calls the mirror "owed" in the queue-run
prompt and skill, which hold no rule. Rule: V3, lens 3. *Counsel:* put the recipe on line 19 and
drop the changelog's "owed" line or point it at the skeleton.

**RNV9 — note — no test renders the hook-plane date note.** `DateKindTest` checks `date_note`
through `--json` only; the `🟡 {r.date_note}` term in `render` (`floor.py`, the `said` list) can be
removed and every test stays green. *Counsel:* one `assertIn("🟡 review-by moved later", …)` on
`render([...], "hook")`.

**RNV10 — note, formed at HEAD not against the delta — `floor.py`'s VISIBILITY docstring says
"what a public declaration tightens … is not built yet"; at HEAD `pdlistscan` and `namescan` read
the declared visibility.** True when landed; stale now. *Counsel:* for the applier, one sentence.

### Re-run ledger

All from the worktree root, `nice -n 10`, one process at a time, exit codes read explicitly:

- `cd tools && python3 -m unittest test_floor` — 255 tests, OK, exit 0 (171 s).
- `cd tools && python3 -m unittest test_floorfleet` — 127 tests, OK, exit 0.
- `cd tools && python3 -m unittest test_coldsweep` — 56 tests, OK, exit 0.
- `python3 tools/floor.py --plane ci --root .` — exit 0. `--plane hook` — exit 0.
- `python3 -m unittest discover -s tools` — started in the foreground; it outran the foreground
  limit and the harness moved it to the background on its own. Its result was not in hand when
  this act was written; it is recorded in the review log when it lands and restated in act 2.
- `gh repo view --json visibility` — `PUBLIC`, exit 0 (a read).
- Fleet, by count (direct read of each sibling's floor config, read-only; `floorfleet.py` cannot
  report visibility, `RNV3`): 22 configs; visibility public 4, private 6, absent 12; dated
  advisories 4, kinds mandate 0, default 0, unlabelled 4; legacy lists 0.
- Live visibility path with Actions variables set and no token: 🟡 "answer could not be read",
  exit 0 — the stock python on this machine fails TLS verification (environment, not code); curl
  on the same URL: 200, `x-ratelimit-limit: 60`; a nonexistent slug: 404.
- NOT RUN: nothing needed a live write.

### Follow-up checklist (the principal's to decide; nothing applied)

- [ ] `RNV1` wire the token into the floor step; name the answer's source.
- [ ] `RNV2` rule on the 4 unlabelled dates and on what an unlabelled date reads as.
- [ ] `RNV3` teach the fleet board the `visibility` key.
- [ ] `RNV4` scaffold `visibility` from the instance profile.
- [ ] `RNV5` "staged" → the working tree, or read the index.
- [ ] `RNV6` warn in `--commit` mode too.
- [ ] `RNV7` "every agent" → "every in-process subagent".
- [ ] `RNV8` the recipe onto `dispatch-brief.md`; fix the changelog's "owed" line.
- [ ] `RNV9` one render test. `RNV10` one docstring sentence.

### Reconcile (act 2, 2026-11-16 UTC)

Opened after act 1 was committed (`70359809`): the held sibling (one file, at a user-local path
outside the repo, given by the orchestrator at release), the queue pointer, the three intent
records, the two prior verdicts (`2026-09-25-0715` scratch clause, `2026-10-03-0357` date kind;
finding headings and the findings this delta applied), and the four commit bodies. The
whole-suite run landed after the act-1 save: `unittest discover -s tools` — 3,134 tests, OK, exit
0, 813 s (one run; the brief-writer saw 2,643 at `457615cc`).

**The sibling's questions.** (1) Outside Actions the check adds no line (test
`test_a_local_run_adds_no_visibility_line`, re-run green), and every surface bounds "detects" to
CI: the docstring, `REPO-STANDARD.md`, the changelog. (2) The sibling sits in `docs/reviews/` in
the tree while a brief is written and is committed there; the orchestrator removes it at claim
and holds it where the rule says. The rule names the holder's location, not its role, so a
headless brief-writer is covered; `review-drain`'s orchestrator prompt step 3 is the mechanism,
and this pass ran that way. (3) At a repo's first commit `HEAD:.atelier-floor.json` is unreadable
and `moved_later` returns nothing (test `test_no_readable_head…`, green); a shallow clone has a
HEAD and compares normally. No finding.

**The pointer's questions.** Can a reviewer still reach held-back notes: on a same-user machine,
yes by path, which the doctrine says plainly; what changed is the prompt-free `cat` from a shared
scratchpad (`RNV7` narrows "every agent" to in-process subagents). Does an unlabelled date read
as a mandate strand a child: not stranded (the line is warn-only) but misreported, for dates the
principal ruled defaults (`RNV2`). Can the cross-check pass while a repo is public: yes when it
declares public (correct), when it declares nothing (🟡), and on a re-run that replays a
pre-flip payload with no token to ask live (`RNV1`).

**Per finding against the author's account and the prior verdicts.**

- `RNV1` — **anticipated by the author, recorded only in the closed intent record:** `260/050`'s
  closing note lists "exporting the token in the floor template" among follow-ups not built; no
  board item, and none of the delta's own surfaces (docstring, changelog, `README`) qualifies the
  "live answer wins" claim. Severity unchanged: the gap was known and left unsaid where a reader
  of the code would meet it.
- `RNV2` — the mandate reading applies the prior pass's `DK11` counsel ("the meantime reads as
  mandate", pointing at the stricter-reading rule), and the pick carried "DK2–DK10 as counselled";
  `160/450`'s closing note records "labelling each child's existing dates is that child's own
  edit". Neither weighed the C1b default ruling in the same subsection, and no item queues the
  labelling. Unchanged; the ask to the principal is the same.
- `RNV3` — **anticipated:** the commit body says "Not built: … the board column"; the intent
  record lists "a fleet column". Known, not queued. Unchanged.
- `RNV4` — not anticipated. Unchanged.
- `RNV5` — the word "staged" comes from `DK2`'s counsel ("already sees the staged
  `.atelier-floor.json`"); the code built from it reads the working tree. Unchanged.
- `RNV6` — not anticipated (`DK9` was about the pattern path). Unchanged.
- `RNV7` — the expiry test's wording comes from `SK8(b)`'s counsel; the "every agent" premise is
  `SK1`'s, measured on in-process subagents. Unchanged, minor.
- `RNV8` — `SK3`'s counsel named `skills/queue-run/SKILL.md` step 5, which the delta records as
  owed; by then `180/120` had landed the skeleton that is the real mirror. Unchanged.
- `RNV9`, `RNV10` — not anticipated. Unchanged.
- The brief-writer's held facts match act 1's reading of both scope cuts (`RNV2`, and the
  "stricter checks" half of the `260/050` pick, which the brief named a non-goal and act 1 left
  there; at HEAD `pdlistscan` and `namescan` have since begun it, `RNV10`).

No finding formed at reconcile. No act-1 severity moved. The brief-writer's fleet facts of
2026-11-09 (0 kinds, 0 children declaring visibility) against this pass's (0 kinds; 10 of 22
declare) show the key being adopted by hand, repo by repo, with no board view of it (`RNV3`).

**Overall, restated: PASS-WITH-FINDINGS** — 0 MAJOR · 3 MODERATE (`RNV1`, `RNV2`, `RNV3`) ·
5 minor (`RNV4`–`RNV8`) · 2 note (`RNV9`, `RNV10`). Every finding is the principal's to decide;
nothing applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

The text below is the brief's held-back sibling,
`2026-11-09-0153-review-notes-date-kind-and-visibility-cold.deferred.md`, copied verbatim. It was
removed from the review worktree before the reviewer started, held outside the tree until act 1
was committed (`70359809`), then released to the reviewer for act 2. The orchestrator forms no
finding and has not edited it; the sibling file itself is deleted in the fold commit, so the
brief's mentions of it by name now point here.

# Deferred reading for `2026-11-09-0153-review-notes-date-kind-and-visibility-cold.md`

Open only after your act-1 findings are committed (`docs/method/REVIEW.md` rule 1). Fold into the
brief below the reconcile, then delete this file. A floor, never a fence.

## The queue pointer's questions (the author's framing, verbatim)

> whether a reviewer can still reach held-back notes; whether an unlabelled date read as a mandate
strands a child; whether the cross-check can pass while a repo is public.

## The brief-writer's questions

1. Outside Actions, what does the visibility check do, and is the "detects" claim bounded to CI in
every surface?
2. Where does the `.deferred.md` sibling actually sit in the brief-writer flow, and does the rule's
named location cover a headless brief-writer?
3. How does `floor.py`'s hook-plane comparison against HEAD behave at a repo's first commit or a
shallow clone?

## What the brief-writer held back

- The principal's answer on `260/050` says public repos get the stricter checks; the changelog names
  what a public declaration tightens as not built.
- The principal's answer on `160/450` says existing dates get labelled; the changelog says none is
  labelled by this change, each repo's own edit, and which kind needs the principal.

## Re-run results (2026-11-09 UTC, at `457615cc`)

`test_floor`: 187 tests, OK, exit 0. `test_floorfleet`: 119 tests, OK, exit 0. `test_coldsweep`: 37
tests, OK, exit 0, under `/usr/bin/python3` 3.9, and again inside the full suite under 3.14.
`floor.py --plane ci`: exit 0, with 28 `secretscan` advisories reported and not blocking. `--plane
hook`: exit 0. Full suite under `python3` 3.14: 2,643 tests, OK, exit 0, 1,228 s at a load of about
20. `gh repo view --json visibility`: PUBLIC, exit 0. `floorfleet --json`: exit 0; 23 rows, 1
parent, 21 wired children, 1 absent. `advisory_kind` set on 0 of 23 rows; `visibility` declared by 0
of 20 wired children with a config, 1 with no config.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/1180 cold pass (RNV)

Reviewer: Fable 5.1 (tier checked at selection), spawned by a headless Opus 5.5 orchestrator
started by drain session 1e053526. Platform API credit lane. Worktree:
/Users/mike/worktrees/fable/atelier-160-1180-0816/atelier (referred to below as WT).
Commands, files, evidence only. No secrets, no live captures.

## Setup (2026-11-16 08:17 UTC)
- `uptime` -> load 2.56 3.26 3.03 (16 GB laptop, several passes running). OK to proceed.
- `git -C WT status --short` -> only ` D docs/reviews/...cold.deferred.md` (expected: sibling removed on purpose).
- `git merge-base --is-ancestor 595db812 HEAD` -> exit 0 (landing commit present).
- `python3 --version` -> 3.14.6 on PATH; /usr/bin/python3 -> 3.9.6.
- Read the brief in full (lines 1-237).

## Reading (act 1)
- Read `docs/method/REVIEW.md` lines 25-300 (rules 1-4), 302-460 (lenses, re-run rule, V1-V7), 460-570 (lifecycle, method record). Verdict shape taken from there.
- `wc -l` on the 16 delta paths at HEAD (floor.py 3676, floorfleet.py 1944, coldsweep.py 559, test_floor.py 3363 ...).
- `git log --oneline 595db812..HEAD -- <16 delta paths>` -> 60 commits since the delta on those paths (the brief said 7 at 457615cc). Delta hunks checked at HEAD below, by function, not by reading 60 commits.
- Ran the brief's four `coldsweep.py --commit` lines (d7abac17, db2c39f9, c4424324, 595db812), each exit 0, output to scratch (/tmp/rnv-1180-scratch/c1..c4.diff; 191/659/427/36 lines); each footer: "message body not printed", 0 board-store files, 0 rule-2 barred files touched. Read all four diffs in full. Every commit read body-free: yes.

## Checks at HEAD (act 1)
- `grep -n` floor.py at HEAD: DATE_KINDS 309, VISIBILITIES 313, _github_get 2495, github_visibility 2507, check_visibility 2534, moved_later 2573, main ci block 3644-3660. `git diff 595db812..HEAD -- tools/floor.py tools/floorfleet.py tools/coldsweep.py | grep` on the delta's names: no +/- lines on visibility/moved_later/date_note/kind functions (one new comment at floor.py:1137, pdlistscan reads the declared visibility); the delta's code is unchanged at HEAD.
- `.github/workflows/floor.yml` lines 118-140: the "scanner floor" step runs `floor.py --plane ci --root repo --tools atelier/tools` with NO `env:`; the only token export in the file is `GH_TOKEN` on the signature step (line 182). `grep -rn GITHUB_TOKEN` over .github/, docs/build/templates/, skills/: no hit. So `github_visibility()`'s `env.get("GITHUB_TOKEN")` is always None in the house workflow. Candidate finding (RNV1).
- `tools/floorfleet.py` at HEAD: `grep -n -i visibility` -> one unrelated comment (line 617). The board does not read or show `visibility`. Candidate finding (RNV3).
- `.atelier-floor.json` (house): `"visibility": "public"`; no `advisory` block, so no dated advisory and no `kind` in the house config.
- `docs/ROADMAP.md` (index; not barred): no open item for labelling existing dates, for a house-date declaration, or for "what a public declaration tightens" (greps: label, mandate, kind, tighten, house date). 390/020's title is the always-confirm visibility rule; the item (not barred, read) records the principal's 2026-11-09 answer "Yes, add to daily check" and that the daily visibility check lives on a private board: the delta's cross-reference reaches a real rule (V5 ok).
- `docs/method/CONCURRENCY.md` 995-1035 at HEAD: the scratch clause as landed (595db812 wording). `docs/method/GUARDS.md` 383-440: the kind subsection. `docs/method/PROPAGATION.md` 390-393; `docs/build/REPO-STANDARD.md` 123-140; `docs/build/templates/CONTRIBUTING.md` 58-80; `docs/method/REVIEW.md` 92-105 (rule 1 "only where the deferred bytes never sit on a path the reviewer is given"). All four say the same rule (V4/V5 ok for the kind rule's wording; see RNV2 for its substance).
- GUARDS.md 420-421 says floor.py "compares the staged `review-by` with HEAD's"; `moved_later` takes `cfg` from `Config.load(root)`, which reads the working-tree file (test `test_the_note_is_a_report_and_never_blocks_the_hook` writes the new config and never stages it, and expects the note). "staged" is not what the code does. Candidate minor (RNV5).
- `tools/coldsweep.py` 420-440 at HEAD: the empty `--also-exclude` warning sits after `walk()`, which `--commit` mode returns before (line 421), so `--commit ... --also-exclude <typo>` is silent. Candidate minor (RNV6).
- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`: exists (ls only; barred, not read).
- urllib probe (`inspect.getsource(HTTPRedirectHandler.redirect_request)` on python3 3.14): only content-length/content-type are dropped on redirect; an Authorization header follows a redirect to any host. Note-level while no token is wired (RNV1 counsel).
- Probe of the scratch-namespacing test (CONCURRENCY.md 1015-1020): an in-process subagent (Agent tool, haiku) reported CLAUDE_CODE_SESSION_ID equal to this reviewer's and its task output landed under this session's tasks directory: "equal means shared" holds for that shape. This reviewer itself (an SDK child session, CLAUDE_CODE_CHILD_SESSION=1) has its own session id and its tool-results spill is keyed by it. The rule's test is sound; its premise ("every agent is handed the orchestrator's own scratchpad") is true of in-process subagents, not of headless child sessions. Confirmed, with that nuance recorded in the verdict. Probe marker /tmp/rnv-probe-1180 deleted at cleanup.
- Brief's coldsweep sweep command (four --also-exclude, pattern "visibility"): exit 0, stderr empty (all four bars matched files); 44 hits over 839 files, 560 excluded as barred. Sweep for "reads as a mandate": 8 hits (CHANGELOG, GUARDS, PROPAGATION, floor.py x2, floorfleet.py x2, test_floorfleet). Sweep for where deferred siblings are held: skills/review-drain/orchestrator-prompt.md step 3 puts the sibling in {HELD_DIR} "outside any temp directory" (a later commit, agrees with the rule).
- skills/create-repo: scaffolds `.atelier-floor.json` with no `visibility` key (grep: only instance.yaml's remote visibility and the CLAUDE.md template's visibility fact). Candidate minor (RNV4).
- Tests (one at a time, nice -n 10, from WT/tools): test_floor 255 tests OK exit 0 (171 s); test_floorfleet 127 OK exit 0; test_coldsweep 56 OK exit 0.
- Re-run ledger (from WT root, nice -n 10, one at a time): `floor.py --plane ci --root .` exit 0 (21 checks, declarations line 🟡 as expected); `floor.py --plane hook --root .` exit 0; `gh repo view mike548141/atelier --json visibility` -> {"visibility":"PUBLIC"} exit 0.
- Live re-drive of the CI visibility path from this machine: `env -u GITHUB_TOKEN GITHUB_ACTIONS=true GITHUB_REPOSITORY=mike548141/atelier GITHUB_EVENT_PATH=/nonexistent floor.py --plane ci --json` -> exit 0, visibility result "declared public, but GitHub's answer could not be read — not checked this run". Cause isolated: python3 3.14 on this machine fails TLS verification (URLError CERTIFICATE_VERIFY_FAILED, no local issuer); an environment limit, not the code's. `curl` unauthenticated GET /repos/mike548141/atelier -> HTTP 200, x-ratelimit-limit 60, remaining 58; GET on a nonexistent slug -> 404 (what a private repo returns without a token). The unreadable-answer branch rendered 🟡 and exit 0 as claimed.
- Fleet counts (direct read of each sibling's .atelier-floor.json under the fleet root, /usr/bin/python3, counts only): 22 repos with a floor config; visibility public 4, private 6, absent 12, other 0; dated advisories 4, kinds: mandate 0, default 0, unlabelled 4; legacy-list advisories 0. `floorfleet.py` cannot report visibility (it does not read the key), so the brief's "visibility the fleet view reports" line was met by this direct read instead.
- A one-shot in-process subagent (Agent tool, haiku) was spawned solely to report its CLAUDE_CODE_SESSION_ID and whether a scratchpad path was named to it (result: same session id as this reviewer; no path named). No finding rests on its output; it informs the RNV7 nuance only, which also rests on this reviewer's own env.
- Whole suite: `(cd WT/tools && nice -n 10 python3 -m unittest discover -s .)` started in the foreground 2026-11-16 ~08:33 UTC; it exceeded the 600 s foreground limit and the harness moved it to the background on its own. Result recorded below when it lands (not a second copy).
- Orchestrator contact (process only): a resume message after this reviewer's turn ended early, telling it to carry on in the foreground, use its own results, disclose the helper, and spawn no further background work. No question about the delta, no pointer to risk.
- Act-1 text checks on the brief: datescan clean (503 lines), leakscan clean, attribscan clean, reviewscan ok (deferred material kept out), pdlistscan whole tree clean (1263 files); spellscan and wrapscan skip docs/reviews by their ignore files (scanned nothing), so widths were checked with awk: no verdict line over 100 characters (two lines over 100 bytes are en-dash/emoji width only). The brief-writer's own lines 1-198 carry the file's pre-existing long command lines, untouched.
- Whole suite (discover) at act-1 save: still running at act-1 save
- Act 1 written to the brief below a --- divider; Status line updated to ACT 1 RUN. Verdict: PASS-WITH-FINDINGS, 0 MAJOR, 3 MODERATE (RNV1-RNV3), 5 minor (RNV4-RNV8), 2 note (RNV9-RNV10). Scratch /tmp/rnv-1180-scratch kept until act 2 for the discover output, then deleted.
- Whole suite landed after the act-1 save: `python3 -m unittest discover -s tools` -> Ran 3134 tests in 813 s, OK, exit 0 (one run only; restated in act 2, act-1 text left unrevised).

## Act 2 (2026-11-16 UTC)
- Opened after act 1 committed (70359809): the held sibling at the orchestrator-given user-local path (one file); the queue pointer (docs/roadmap/160-doctrine-review-owed/1180-...); the three intent records (160/380, 160/450, 260/050 — the answer and closing notes); prior verdicts docs/reviews/2026-10-03-0357-date-kind-rule-cold.md (finding headings; DK2 270-280, DK11 441-446) and docs/reviews/2026-09-25-0715-scratchpad-clause-cold.md (headings; SK3 420-430, SK8 468-478); `git log -1 --format=%B` of d7abac17, db2c39f9, c4424324, 595db812.
- Evidence used in the reconcile: 260/050 closing note lists "exporting the token in the floor template" and "a fleet column" as follow-ups not built (RNV1, RNV3 anticipated, not queued); c4424324 body says "Not built: ... the board column"; DK11 counsel is the source of "reads as a mandate" (RNV2); DK2 counsel is the source of "staged" (RNV5); SK3 named queue-run SKILL.md step 5 (RNV8); SK8(b) is the source of the session-id expiry test (RNV7). Sibling's three questions answered from act-1 evidence (tests re-run in act 1; review-drain orchestrator-prompt step 3).
- Whole suite: 3134 tests OK, exit 0, 813 s (landed after the act-1 save; restated in the reconcile).
- Reconcile appended beneath the verdict; act-1 text unrevised; no finding formed at reconcile; no severity moved. Scanners over the brief after act 2: see the last run. Scratch /tmp/rnv-1180-scratch deleted.
