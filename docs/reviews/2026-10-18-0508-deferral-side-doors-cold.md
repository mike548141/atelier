# Cold pass — the deferral's side doors, in REVIEW rule 1 and RECORD

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-18 UTC by an Opus brief-writer;
the pass waits for a cold Fable session that neither the delta's author nor this brief-writer
(nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/910-rule-4-cold-pass-queued-deferral-side-doors.md`.
**Why it earns a review:** it widens what rule 1's deferral binds — from the brief and its
sibling to every record a reviewer reads before the brief — and puts a matching duty on whoever
writes the session log. Every brief-writer, author and orchestrator in every repo that inherits
`REVIEW.md` and `RECORD.md` now owes it. The worst failure is a rule that reads as closing the
leak while a door it does not name stays open, so later passes trust a deferral that leaked.

## Spawn provenance

- **Author of the work under review:** one authoring session — a Mike-opened Opus 5.5 queue run,
  session `e1d4097c`, record `docs/sessions/2026-10-18-0001-queue-run-the-plugin-installed.md`
  (barred to the reviewer until phase 2). That one session authored the whole of the `160/900`,
  `160/910` and `160/930` deltas; the pointer names its worktree for this delta as
  `atelier-qr-180-plugin`. The brief-writer did not read the landing commit's message body or
  the intent record, so it cannot say whether a worker drafted the text.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-18 by a
  different Mike-opened Opus 5.5 queue run, session `8e498ef1` (worktree
  `atelier-qr-briefs-1018`), which Mike started directly with a bare `/atelier:queue-run`. The
  dispatching run was **neither started nor instructed by the authoring session**, and neither
  it nor the brief-writer authored any of this delta. **Verified from git** (commit times, read
  with `git log --format='%h %cI %s'`): `adf75a4` was committed 2026-10-18 00:18 UTC; the
  dispatching run's own commits are `f0d6238` (05:00 UTC) and `a9f11ff` (05:09 UTC), both board
  claims. Git cannot name a session; the session attribution is the dispatching run's account,
  and two lines of the authoring session's record agree with it (it records the dispatching run
  as "opened by Mike" and "watched from here"). One oddity, stated as fact: that record's
  identifiers line gives its window as 2026-10-17 23:59 to 2026-10-18 04:14 UTC, while it
  records watching a run that opened after 04:14. **Off-tier for review, disclosed: it forms no
  finding and writes no severity**, and stops after this brief and its sibling.
- ⚠️ **One channel contact, disclosed for the reviewer to weigh** under roadmap `280/040` (the
  cross-session channel can contaminate review independence). After this brief-writing began,
  the authoring session sent the dispatching run's orchestrator one cross-session file-set
  notice: that `ccclose` had changed under that run's `210/290` worker, a request to rebase
  before merging, and a note that `12e6d9b` had landed and `160/900` had been widened to it. The
  orchestrator reports it carried no evaluative content about any delta. The brief-writer never
  saw the notice itself, only the orchestrator's paraphrase of it.
- **Who takes the review:** a cold Fable session, not yet started, passing rule 4's criterion. If
  it runs as reviewer-plus-orchestrator, rule 4's off-tier conditions apply and are disclosed in
  the claim, the pointer and the verdict. The reviewer repeats its own provenance in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing):
  - its two assigned pointers in full (this one and `160/930`, refs-only, each with a claim
    line); the `160/780` pointer in full as a shape example, including its claim and the summary
    of its verdict (another pass, on `EVIDENCE.md`);
  - the precedent brief `docs/reviews/2026-10-17-0930-agreement-not-corroboration-cold.md` (ask
    half and the head of its verdict) and its sibling as first committed (`b42f305`) — another
    pass's framing, on other surfaces; no other file under `docs/reviews/` was opened;
  - `docs/method/REVIEW.md` lines 25–229 at HEAD (rules 1–4, this delta included) and the whole
    of `skills/review-brief/SKILL.md` at HEAD;
  - this delta's subject, stat and diff through `tools/coldsweep.py --commit adf75a4 --path …`
    (never the message body), and the subjects and stats, no bodies, of the four later commits
    on `RECORD.md` listed under *What the work is*;
  - it also wrote the `160/930` brief in the same sitting, so it read that pass's delta
    (`8132805`, `30aa8dc`) the same way — the commit-message door this delta hands to `130/030`;
  - filename-level greps that listed the intent record's path, and scanner output that named one
    `docs/sessions/` file by path, line and rule (contents not seen);
  - it later wrote the `160/900` brief too, so it read that pointer and that delta (the same
    authoring session's queue-run, prompt and `RECORD.md` work) body-free, and the whole of
    `docs/method/session-open/README.md` at `origin/main`;
  - at its orchestrator's request, to check provenance, lines 139–145 and 159 of the authoring
    session's record (a passage on the dispatching run, and the record's identifiers line);
  - its harness-loaded memory index and instruction files, and recent `git log --oneline`
    subjects.

  It did **not** open the intent record, the `130/030` item, `docs/SESSIONS.md`, the rest of
  `docs/sessions/`, `docs/ROADMAP-DONE.md` or any prior verdict on these surfaces. Its
  orchestrator passed it an instruction set (pointers, the precedent pair, the prefix check, the
  pointer-note shape), the provenance account above and the paraphrased notice, and no
  evaluative content about the delta. Everything evaluative the brief-writer formed is in the
  sibling, which holds five questions and three facts.

## What the work is

Landing commit (diff it on the delta paths; review the paths at HEAD, `f0d6238` or later):

- `adf75a4` (2026-10-18 00:18 UTC) — review: deferred material reaches a reviewer through the
  records it reads first (320/720)

Delta paths (the pointer's own scope):

- `docs/method/REVIEW.md`, rule 1 — the one paragraph the commit adds, headed **The deferral has
  side doors: every record a reviewer reads before the brief** (13 added lines, between *What
  the split buys* and *Split for the duration*). No later commit touches `REVIEW.md`; confirm.
- `docs/method/RECORD.md` — one sentence appended to the `SESSIONS.md` bullet that keeps the
  index short. Four later commits touch this file (`089fcdc`, `1adf398`, `46320f8`, `6810b64`,
  all 2026-10-18); check whether any of them moved or reworded the sentence.

**Read the commit body-free:** `python3 tools/coldsweep.py --root . --commit adf75a4 --path
docs/method/REVIEW.md --path docs/method/RECORD.md`. Plain `git show` is barred here: it prints
the message body before the diff, and reading is atomic (rule 1). Keep the `--path` flags — the
commit also edits the intent record and this pass's pointer, which coldsweep does not bar by
default. The commit's board and index edits are not the delta.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs and live behaviour. The
lenses organise it; they do not bound it. Non-goals are the only narrowing and are themselves
reviewable.

Probe, at least:

- **Which doors exist.** Build the list yourself before you read the paragraph closely: walk
  this repo's session onramp (`CLAUDE.md` read order, `docs/method/CONCURRENCY.md` onramp and
  recovery sweep, the `session-onramp` and `queue-run` skills) and record every surface a
  reviewer meets before it opens a brief. Compare that list with the three the paragraph names.
- **Who the rule binds.** The paragraph names the parties it binds. For each door on your list,
  say who writes its content while a pass is pending, and whether the rule as placed and worded
  reaches that writer.
- **What "file and count only" permits.** Take real pending-pass records — this repo's open
  `160/` pointers and their claim lines, and the precedent's pointer note — and say whether each
  meets the test as worded. Can a reader apply "never by topic" the same way twice?
- **The hand-off to `130/030`.** The paragraph assigns one door to that item. Check, from the
  landed artefacts only (`tools/coldsweep.py --commit` and the `review-brief` skill text), what
  that item's fix covers and whether it covers the door as this paragraph describes it. The item
  itself is barred until phase 2.
- **The "no scanner" claim.** It is an impossibility claim; state its grounds or damage it with a
  probe (what could a guard key on without judging meaning?).
- **The `RECORD.md` sentence.** Is the bullet it joins the place a session writing its close
  entry will meet it? Does it agree with the `REVIEW.md` paragraph in wording and reach, and which
  is the home (`EVIDENCE.md` §9; `PROPAGATION.md` § *One statement, stamped copies*)?
- **Where it reaches.** Which other surfaces tell a session what to write while a review is
  pending — `RECORD.md` elsewhere, the session-close and queue-run skills, `CONCURRENCY.md`, the
  build templates, `README.md` summaries, `CHANGELOG.md` — and do any now disagree or owe a stamp?

**Non-goals:** rule 1's split itself (the separate sibling file), ruled 2026-07-29. Whether this
paragraph is consistent with that split, and its grounding, wording and placement, are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   rule on what record-writers may say is the right control for this leak, set against changing
   what a reviewer reads before the brief, and whether one grounding instance carries the rule.
2. **Correctness & quality.** Diff `adf75a4` on the two paths. Check every cross-reference in the
   new text resolves to a passage that says what is claimed. Record the door list from *Scope*.
3. **Completeness / harvest.** Every surface that states rule 1's deferral or tells a writer what
   a pending-review record may hold (see *Where it reaches*). Is a changelog entry owed?
4. **Security & privacy** — mandatory. The paragraph cites a child's episode in a public repo:
   check it names no private repo, person, host or account beyond the recorded exceptions.
   Describe, never quote, anything sensitive. `/security-review` is discharged by grounds (a
   landed prose delta, and markdown is in its exclusions).

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing. The brief-writer ran each line once, from the
worktree root at `f0d6238`; read exit codes explicitly.

- `python3 tools/coldsweep.py --root . --commit adf75a4 --path docs/method/REVIEW.md --path
  docs/method/RECORD.md` — exit 0, and its last lines say the body was not read
- `python3 tools/linkscan.py --root . .` and `python3 tools/pathscan.py --warn --root . docs`
- `python3 tools/wrapscan.py --root . docs/method/REVIEW.md docs/method/RECORD.md`, the same
  paths through `tools/spellscan.py` and `tools/leakscan.py`
- `git log --oneline adf75a4..HEAD -- docs/method/REVIEW.md docs/method/RECORD.md` — each commit
  named, or empty
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and `--plane
  hook`); at `f0d6238` the ci plane exited non-zero on findings outside the delta paths, so read
  which scanner and which file before you weigh it

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-18-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts and
  scratch trees go in a private clone under your session scratchpad, named by your prefix.
- One heavy process at a time, in the foreground; never point a scanner at another repo on the
  machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds,
  or keep the tree clean when you spawn it — never with this brief or its sibling dirty.
- This pass is itself pending while you run it: anything you write to the session log, the
  pointer or a commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/910-rule-4-cold-pass-queued-deferral-side-doors.md`,
the sibling `docs/reviews/2026-10-18-0508-deferral-side-doors-cold.deferred.md`, the landing
commit's message body (read subject, stat and diff only, by the coldsweep line above), and two
board items:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/720-hand-up-a-brief-writers-session-log-tells-the-next-reviewer-what-it-held-back.md`
  (the intent record)
- `docs/roadmap/130-a-closed-cycle-can-keep-its-and-pointers/030-the-brief-bars-the-commit-body-but-names-no-command-that-avoids-it.md`
  (the item the paragraph hands one door to; another pass's intent record)

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/910-rule-4-cold-pass-queued-deferral-side-doors.md
--also-exclude docs/reviews/2026-10-18-0508-deferral-side-doors-cold.deferred.md
--also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up/720-hand-up-a-brief-writers-session-log-tells-the-next-reviewer-what-it-held-back.md
--also-exclude
docs/roadmap/130-a-closed-cycle-can-keep-its-and-pointers/030-the-brief-bars-the-commit-body-but-names-no-command-that-avoids-it.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `DS`: `DS1`, `DS2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
