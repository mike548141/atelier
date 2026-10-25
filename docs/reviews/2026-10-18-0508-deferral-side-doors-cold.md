# Cold pass — the deferral's side doors, in REVIEW rule 1 and RECORD

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** RAN 2026-10-25 UTC, both phases — PASS-WITH-FINDINGS: 1 MAJOR, 4 MODERATE,
5 minor, 2 notes (DS1–DS12; DS11–DS12 formed at reconcile), by a Fable 5.1 reviewer under session
52e11d15's context partition. Sibling fold-in owed. Brief written 2026-10-18 UTC by an Opus
brief-writer.
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

---

# Verdict — PASS-WITH-FINDINGS (1 MAJOR, 3 MODERATE, 4 minor, 2 notes)

Phase 1, written 2026-10-25 between 21:36 and 21:47 UTC. Findings DS1–DS10 below; the reconcile
(phase 2) is not yet written and nothing here was formed with the sibling open.

## Provenance (rule 4; the 2026-08-17 ruling)

- **Reviewer:** a Claude Fable 5.1 subagent (model id `claude-fable-5-1`), the tier the principal
  names for cold review passes; the tier was checked at selection and is stated here as rule 4
  asks. It read the delta, answered the lenses, assigned every severity and wrote every line
  below this divider.
- **Arrangement:** reviewer-plus-orchestrator. The orchestrator is session `52e11d15` (Claude
  Opus 5.5). It holds the context partition — the brief's `.deferred.md` sibling was removed
  from this worktree on purpose and stays with it until these findings are saved — forms no
  finding and writes no severity. It authored neither the delta nor the brief, and was not
  started or instructed by session `e1d4097c` (the delta's author) or session `8e498ef1` (the
  run whose subagent wrote the brief). It was launched under the principal's approval of Fable
  work for the week ending 2026-10-25 23:00 UTC. The arrangement is disclosed in the claim, in
  the queue pointer's index line and here.
- **Worktree:** `/Users/mike/worktrees/atelier-cold-160-910`, branch `atelier-cold-160-910`,
  at `23c84fc` (origin/main at claim time). Read-only to this pass except for this file. No
  scratch clone was needed; scanner output went under `/private/tmp`.
- **What was read (rule 2 honoured; nothing barred opened):** this brief in full;
  `docs/method/REVIEW.md` whole and `docs/method/RECORD.md` lines 1–120 at HEAD plus
  `git diff adf75a4..HEAD` on it; the delta through `coldsweep --commit adf75a4 --path …` (the
  message body was not read, and the tool's last line says so); `CLAUDE.md` lines 1–60;
  `docs/build/templates/CLAUDE.md` and `docs/method/CONCURRENCY.md` by grep only; the
  `session-onramp`, `queue-run` and `review-brief` skills by grep only; `docs/roadmap/README.md`
  by grep and the head of `160-doctrine-review-owed/README.md`; grep hits across the open `160/`
  pointers with `910` excluded (the hits included one-line leading fragments of closed passes'
  verdict summaries on other surfaces, e.g. a finding id and its severity word — disclosed, none
  on this delta); `tools/coldsweep.py --help`, `tools/reviewscan.py`, `tools/board.py` and
  `tools/floor.py` by grep; `.githooks/pre-commit` whole; `.github/workflows/ci.yml` by grep;
  `CHANGELOG.md` lines 1–61 and grep. `docs/ROADMAP.md`: the tree sweep printed line 321 (this
  item's own index line, carrying the claim and the arrangement disclosure — no deferred
  content) and I printed line 323 (`160/930`) for its shape; the index lines of the two barred
  board items were **measured by length only and never printed**. Harness-loaded at spawn: my
  global instruction files and a memory index belonging to a different repo's project; nothing
  in them concerns this pass and nothing from them enters this file. The orchestrator's spawn
  prompt named the item's title and the intent item's number only.
- **Not opened:** `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any file under
  `docs/reviews/` other than this one, the `160/910` pointer, the `320/720` and `130/030` item
  files (existence confirmed with `test -f` only), the sibling, and the landing commit's body.
  No `--include-barred` sweep was run.

## Lens 1 — approach and assumptions

Load-bearing assumptions, named first, then tested:

1. *A reviewer reads the session-log tail, the board pointer and recent commit subjects before
   the brief.* True of the written onramp (`CLAUDE.md` step 4 and 5; the child template's
   step 3) — and the session-log read is already **barred to a reviewer by rule 2**: the brief's
   rule-2 list names `docs/SESSIONS.md`, and `coldsweep` bars it by default. The premise
   therefore describes a reviewer breaching rule 2 at onramp, because the bar is met only after
   the read. The paragraph does not say so. → DS1.
2. *A rule on what record-writers may say is the right control.* It is a control, and it reaches
   the surfaces a reviewer genuinely must read (the pointer, the index). But the cheaper control
   for the grounding leak — the reviewer's own read order — is never weighed. → DS1.
3. *The parties who write those records while a pass is pending are the author and the
   brief-writer.* Not so under the arrangement rule 1 itself calls structural: the orchestrator
   that holds the deferred bytes writes the claim line, the session entry and the spawn prompt.
   → DS2.
4. *One grounding instance carries the rule.* It carries the duty for the session log, where the
   leak ran. It does not by itself show the pointer or commit subjects have leaked; the rule
   extends to them by reasoning, not evidence, and says so honestly enough ("a door this rule
   did not watch"). No finding on that alone; the extension is sound in direction.
5. *"By file and count only, never by topic" is a test a reader can apply the same way twice.*
   Partly. → DS7.

## Lens 2 — correctness and quality

- Diffed `adf75a4` on the two paths body-free: 13 lines added to `REVIEW.md` between *What the
  split buys* and *Split for the duration*; one sentence appended to the `SESSIONS.md` bullet of
  `RECORD.md`. No later commit touches `REVIEW.md` (`git diff --stat adf75a4..HEAD` on it is
  empty). Five later commits touch `RECORD.md` — the brief lists four; the fifth is `bdb1aba`
  (2026-10-18 05:06 UTC, `210/300`) — and none moves or rewords the sentence. → DS10 (note).
- Cross-references: `320/720` and `130/030` both resolve to item files; `RECORD.md`'s pointer
  `REVIEW.md rule 1, *side doors*` resolves to the heading **The deferral has side doors**. The
  hand-off sentence resolves to a file whose landed fix covers a different door. → DS3.
- Door list, built from the onramp before reading the paragraph closely (`CLAUDE.md` steps 1–5,
  `CONCURRENCY.md` § Surviving an interrupted session, the `queue-run` skill's session-open
  prompt, the harness): `git status` and branch/worktree names · `00-APEX.md` and `README.md`
  (static) · the `SESSIONS.md` tail · `docs/ROADMAP.md`, which since `010/170` (2026-10-18)
  carries each item's bold title and claim text, not only the pointer's · recent commit subjects
  · the principal's or orchestrator's opening prompt · the harness-loaded memory index · the
  cross-session channel · the brief's own barred-path list, whose slugs are headlines. The
  paragraph names three. → DS4, DS5.
- The "no scanner" sentence is an impossibility claim with a cheaper truth available. → DS6.

## Lens 3 — completeness and harvest

Surfaces that state the deferral or tell a writer what a pending-review record may hold, at
HEAD: `REVIEW.md` rule 1 (the home), rule 4's refs-only ceiling for the pointer,
`docs/roadmap/README.md` line 56 (the same ceiling, restated), `RECORD.md` (the one stamp),
`docs/build/templates/docs/reviews/README.md` (the split, not the side doors),
`PROPAGATION.md` line 798 (the split). Silent: `skills/review-brief/SKILL.md` (its only
pending-review line is the body-free command, 51–52), `skills/queue-run/SKILL.md`,
`docs/build/templates/docs/SESSIONS.md`, `docs/build/templates/CLAUDE.md` step 3, `ccclose`'s
checks, and `CHANGELOG.md`, which records four sibling 2026-10-18 doctrine changes and not this
one. → DS8, DS9.

## Lens 4 — security and privacy

The paragraph cites the grounding as "a child, 2026-10-18 (`320/720`)": no repo name, host,
account or person; the two parties are roles ("a brief-writer", "the cold reviewer"). The
`RECORD.md` sentence names nothing. The `320/720` filename names no private thing. `leakscan`
is clean on both paths (exit 0). `/security-review` is discharged by grounds: the work is a
landed prose delta in markdown, which the scanner excludes, and the scanner reads the pending
diff — this brief, dirty in the worktree — which is the SL2 exposure rule 1 warns against. No
secret, placeholder, address or personal detail appears in the delta or in this verdict.

## Findings

Severities: MAJOR / MODERATE / minor / note. Counsel is labelled as counsel; nothing is applied
(rule 3 — the decisions are the principal's).

### DS1 (MAJOR) — the premise is a rule-2 breach, and the cheaper control is never weighed

The paragraph's first sentence — a reviewer's onramp reads the session-log tail before the
brief — is true of `CLAUDE.md` step 4 (and the child template's step 3, which stamps the same
step into every repo) and false to rule 2 as the house applies it: the brief's rule-2 list bars
`docs/SESSIONS.md`, and `coldsweep` bars it by default (its own output: "rule-2 barred
(docs/SESSIONS.md, docs/sessions, docs/ROADMAP-DONE.md, docs/reviews)"). The grounding leak
happened because the bar arrives *after* the read: a session meets step 4 before it reaches
`REVIEW.md` or any brief. The delta answers that sequencing defect with a standing duty on
every record-writer in every inheriting repo, enforced by nobody ("no scanner checks this"),
and never mentions the one-line alternative at the reader's end — a cold reviewer skips step 4,
written into `CLAUDE.md` step 4, the child template, and the spawn prompt the `review-brief`
skill shapes (this pass's own spawn prompt did exactly that: "read the brief in full first").
That is the brief's named worst case in a different coat: the rule reads as closing the leak
while the door that leaked — the onramp's order — stays as written. V5 as well: rule 1 now
treats as given a read rule 2 forbids, without naming the conflict.
*Counsel:* keep the writer-side rule as defence in depth (the pointer and the index are read by
every session and cannot be skipped) and add the reader-side carve-out where the reader meets
it; reword the premise to say the onramp reads a file rule 2 bars, so the two rules agree.

### DS2 (MODERATE) — the rule binds by role, and misses the party that holds the bytes

"Written by the author or brief-writer" omits the orchestrator that holds the context partition
— the arrangement rule 1 calls the only structural one, and the one this pass runs under. That
orchestrator writes the claim line (which `board.py` projects into `docs/ROADMAP.md` line 321,
read at onramp step 5, as prose well beyond the `(claimed …)` fragment), the session entry, the
commit subjects and the spawn prompt, and it is the party most certain to have the deferred
material to hand. The principal and any peer that widens the pointer are outside the wording
too. `RECORD.md`'s stamp says "an entry written while a review is pending" — any writer — so
the two surfaces disagree in reach (V5), and the stamp is wider than its home (V4).
*Counsel:* bind by knowledge, not role — anyone who has read, or holds, the deferred material —
and align the stamp.

### DS3 (MODERATE) — the `130/030` hand-off covers a different door than the one listed

The paragraph's own door list reads "recent commit subjects", which is what the onramp sees
(`git log --oneline`). Its last sentence hands "the commit-message door" to `130/030`. From the
landed artefacts only: that item's filename scopes it to the commit *body* ("the brief bars the
commit body but names no command that avoids it"), and its landed fix — `coldsweep --commit`
(`review-brief` skill lines 51–52) — prints the subject and withholds the body. So the body door
is closed by a command, the body is not an onramp door at all (rule 2 and every brief bar it),
and the subject door is handed to an item that does not touch it. The binding sentence ("any of
those … names deferred material by file and count only") still reaches subjects, so the duty
exists; the hand-off misleads a reader about what remains open and whose it is.
*Counsel:* "the commit *body* read is `130/030`'s; subjects are bound here."

### DS4 (MODERATE) — two writer-side doors the list does not name

(a) **The board index.** `docs/ROADMAP.md` is onramp step 5 and is not rule-2 barred. Since
`010/170` (2026-10-18, the delta's own day) `board.py` builds each index line from the item's
logical first paragraph: the bold title (to 70 characters) and the claim text. Every item's
title is therefore read before the brief — an author's intent-record title, or a follow-up item
a brief-writer files for a fact it held back, is a headline in the index. The paragraph names
"the board pointer"; the writer-side duty does not reach other items' titles or claim prose.
(b) **The harness-loaded memory index.** Auto-loaded into every session in the project before a
single file is opened, written by whichever session last saved it, and outside the repo. The
brief discloses its own load of it (line 69). No doctrine surface names it as an onramp read
(grep for memory in `CLAUDE.md`, `CONCURRENCY.md`, `RECORD.md`, `REVIEW.md`: no such sense).
Both are "records a reviewer reads before the brief" under the paragraph's own definition.
*Counsel:* name both; for (a) bind item titles and claim text the same way as the pointer; for
(b) a memory note written while a pass is pending follows the same file-and-count rule.

### DS5 (note) — structural exposures worth naming as accepted, not closed

Four more doors are not writer-side records and cannot be closed by this rule, but a reader of
"every record a reviewer reads" should find them named: the cross-session channel (`280/040`
open; this brief discloses one contact, lines 38–44); the opening prompt the `queue-run` skill
says to follow as the principal's brief (line 26), written by the principal or the orchestrator;
branch and worktree names carried in claims (`wt: …`); and the brief's barred-path list itself,
which must name the intent record to bar it, and whose slug is a headline of its thesis.

### DS6 (minor) — "no scanner checks this" overclaims; the mention's shape is checkable

The sentence is true as a statement of current fact and false as an impossibility. A guard need
not judge meaning: in a `SESSIONS.md` tail entry or a claim line, a sentence that mentions
`.deferred.md`, "sibling" or "held back" can be required to match `<file> with N question(s)
and M fact(s)` and end there; anything after the count is a finding. That covers the canonical
shapes and not every one — exactly the honest form `REVIEW.md` lines 118–121 already give for
`reviewscan`'s heading check. V1.
*Counsel:* "no scanner checks this yet; one could key on the mention's shape, not its meaning."

### DS7 (minor) — "file and count only" has no test at its one boundary

Applied to real records: every open `160/` pointer note examined (`090`–`980`, `910` excluded)
names the file ("the `.deferred.md` sibling") and none a count; this brief says "five questions
and three facts" (line 77); the exemplar says "four questions and two facts". Is the *kind* a
topic? "two facts" is plainly fine; "two provenance facts" or "two facts about the author" is
plainly not; "a wording question" sits on the line, and the rule gives one example and no test.
Two readers will draw that line on different sides. The pointer already carries a second,
differently worded test for the same surface — rule 4's "refs only, no evaluative account",
restated at `docs/roadmap/README.md` line 56 — so one record now answers to two phrasings (V4).
*Counsel:* state the test: the file's name, a number, and the words "questions" or "facts",
nothing else in the sentence.

### DS8 (minor) — the `RECORD.md` sentence is not where a closing session meets it

It joins the *append-only index* bullet, after a 2026-07-14 parenthetical about rotation — a
bullet about the index's shape. A session writing its close reads *Finish the sequence, then
declare the close* and runs `ccclose`, and neither carries the duty (`ccclose` has no such
check). Home and stamp are the right way round (`REVIEW.md` holds it; the stamp points), but
the stamp sits where the shape of the log is explained, not where an entry is written.
*Counsel:* a one-line pointer in the close bullet, or in `ccclose`'s checks.

### DS9 (minor) — surfaces that now owe a stamp or an entry (V3)

`skills/review-brief/SKILL.md` — the brief-writer's instruction set — says nothing about the
close entry, the pointer note or the claim line; `skills/queue-run/SKILL.md` — the
orchestrator's — nothing about pending reviews; `docs/build/templates/docs/SESSIONS.md` and the
child `CLAUDE.md` template step 3 nothing. `CHANGELOG.md` records four other 2026-10-18 doctrine
changes (lines 49–96) and earlier `REVIEW.md` changes (lines 239, 528, 542) and not this one; by
the file's own practice an entry is owed.

### DS10 (note) — the brief's later-commit count is stale, not wrong in effect

Five commits touch `RECORD.md` after `adf75a4`, not four: the fifth is `bdb1aba` (2026-10-18
05:06 UTC). None moves the sentence.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR (DS1), 3 MODERATE (DS2, DS3, DS4), 4 minor (DS6–DS9), 2 notes
(DS5, DS10).** The rule's direction is right and its grounding is honest; what it is built on —
a reviewer reading a barred file — is the defect it should have named, and its door list is
short by the two surfaces that cannot be skipped.

## Re-run ledger

All from the worktree root at `23c84fc`, `/usr/bin/python3`, exit codes read explicitly.

- `coldsweep.py --root . --commit adf75a4 --path docs/method/REVIEW.md --path
  docs/method/RECORD.md` — exit 0; its last lines say the message body was not read and that no
  barred file was touched.
- `linkscan.py --root . .` — exit 0, clean; 4 suppressed by allow-marker.
- `pathscan.py --warn --root . docs` — exit 0 (advisory); 63 findings, none on a delta path (one
  names `REVIEW.md` as a path quoted inside `320/010`'s text).
- `wrapscan.py --root . docs/method/REVIEW.md docs/method/RECORD.md` — exit 0, clean.
- `spellscan.py`, same paths — exit 0, clean.
- `leakscan.py`, same paths — exit 0, clean.
- `git log --oneline adf75a4..HEAD -- docs/method/REVIEW.md docs/method/RECORD.md` — five
  commits, all on `RECORD.md`: `089fcdc`, `1adf398`, `46320f8`, `6810b64`, `bdb1aba`;
  `REVIEW.md` untouched.
- `floor.py --plane hook --root .` — exit 0; 12 checks enforced and green, 4 warn-only.
- `floor.py --plane ci --root .` — exit 0 at HEAD; the non-zero exit the brief saw at `f0d6238`
  did not reproduce. secretscan reported 23 advisory findings and pathscan 3, none naming a
  delta path.

## Follow-up checklist

- [ ] DS1 — principal's ruling on the reader-side carve-out (`CLAUDE.md` step 4, the child
      template, the spawn-prompt shape) and the premise's rewording.
- [ ] DS2 — bind by knowledge; align `RECORD.md`'s reach with `REVIEW.md`'s, in one direction.
- [ ] DS3 — correct the `130/030` hand-off sentence to the body.
- [ ] DS4 — name the index (titles and claim text) and the memory index as doors.
- [ ] DS5 — name the four structural exposures as accepted.
- [ ] DS6 — soften the impossibility claim, or queue the shape check.
- [ ] DS7 — state the file-and-count test; reconcile with rule 4's refs-only wording.
- [ ] DS8 — pointer in the close bullet or `ccclose`.
- [ ] DS9 — stamps on the two skills and two templates; a `CHANGELOG.md` entry.
- [ ] DS10 — none owed; the brief's count stands corrected here.

### Reconcile (act 2, 2026-10-25 21:47–21:49 UTC)

Opened after act 1 was saved and the orchestrator released it: the held sibling (three facts,
five seeded questions), then the two items rule 2 barred until this phase, `320/720` (the
intent record) and `130/030`, and the two prior verdicts the sibling names by filename
(`2026-08-02-2348-deferral-delta-cold.md`, `2026-08-17-1000-coldsweep-cold.md`), read to
reconcile, not to anchor. Phase-1 text above is unrevised. Agreement between a seeded question
and an act-1 finding is noted as agreement only; every act-1 finding was formed before the
sibling was opened. **Fold-in:** the brief and the sibling both say the sibling is folded in
below this reconcile and deleted; the orchestrator instructed that it not be copied into the
worktree, so the fold-in is owed and left to the orchestrator, which holds the file.

**Held-back facts.** (1) The intent record is now read; its account matches the paragraph and
adds two things the paragraph omits: the child's reviewer ran with **no orchestrator**, on the
child's own onramp (step 3 there is the session-log tail), and the child's suggested shape
included *a `reviewscan` line, if the scanner can see session logs* — the author closed it
"minus the scanner" with the reason that no pattern can tell "two facts" from what the facts
say. (2) `160/930` shares this brief-writer; noted, no bearing on any finding here. (3) The two
prior verdicts: see DS12.

**Seeded questions, against the act-1 findings.**

- *Q1 subjects versus bodies* — agrees with DS3, formed in act 1. `130/030` as now read
  confirms it: its subject is the body read *during* the review (`git show` printing the body
  before the diff), its fix is `coldsweep --commit`, and nothing in it concerns subjects read at
  onramp. Answer: the subject door is covered by this paragraph's own binding sentence, not by
  `130/030`; the hand-off sentence misassigns. DS3 stands, MODERATE.
- *Q2 the scope sentence* — a point act 1 missed. → DS11, formed at reconcile.
- *Q3 unnamed writers; the index line* — agrees with DS2 and DS4(a), both formed in act 1 (the
  index line was measured: title to 70 characters plus claim text). No change.
- *Q4 `RECORD.md` placement; a session-close skill* — agrees with DS8. There is no session-close
  skill in this repo (`skills/`: create-repo, queue-run, review-brief, session-onramp); the close
  is `RECORD.md`'s close bullet plus the `ccclose` instrument, and neither carries the duty
  (DS8, DS9). No change.
- *Q5 one instance; `PROPAGATION.md` § When a rule keeps breaking* — act 1 (lens 1, assumption 4)
  took the paragraph at its word that the grounding was one instance and found nothing on that
  alone. The prior verdicts show the house's own record holds more. → DS12, formed at reconcile,
  and the grounds of DS1 and DS6 strengthen (severities unchanged).

**Changes to act-1 findings, stated openly.** No severity changes. DS1's grounds strengthen:
the 2026-08-17 brief already told its taker *"a taker whose own onramp has already read the
`SESSIONS.md` tail discloses that in the verdict"* — the house named the reader-side door two
months before this delta and chose disclosure over a carve-out; the delta neither cites that nor
revisits it. DS3 is confirmed by the item itself. DS6's target is now the author's stated reason,
read in `320/720`: the shape check does not need to tell "two facts" from what the facts say;
it rejects anything in the sentence after the count, which is exactly what leaked in the
grounding instance (a parenthetical naming both facts' topics).

### DS11 (minor, formed at reconcile from Q2) — the duty sits under a scope sentence that
### excludes its own grounding case

`REVIEW.md` lines 56–59 bind rules 1–2 "whenever the brief is written by, or on the framing of,
the work's author". The grounding case's brief-writer was a non-author, and the paragraph binds
"the author or brief-writer" explicitly, so a reader of the paragraph is bound; a reader of the
umbrella sentence finds the non-author case outside rule 1 altogether. The scope sentence
predates the delta and has lagged practice for months — every `160/` pointer since August
carries a non-author brief-writer's sibling — so the contradiction is inherited, not created;
the delta is the first text to lean on it for a non-author case. V5.
*Counsel:* widen the umbrella to "whenever a brief carries deferred material, whoever wrote it".

### DS12 (MODERATE, formed at reconcile from Q5) — the grounding is not the first recorded
### occurrence, and the house's own threshold for a check was already met

The paragraph says "Grounded in a child, 2026-10-18" and the intent record treats it as one
instance. The repo's own verdicts record two earlier passages of author- or brief-writer-side
content to a reviewer through the session log: 2026-08-02 (an author's `SESSIONS.md` entry with
an account of the delta reached a reviewer mid-pass, via a sweep) and 2026-08-17 (the
brief-writer read the `SESSIONS.md` tail at onramp, before the brief, and the brief instructed
its taker to disclose the same). The shapes differ — a sweep, an onramp read by the brief-writer,
an onramp read by the reviewer — and that difference matters for the rung test, so this is not
"thrice the same"; but `PROPAGATION.md` § *When a rule keeps breaking* makes **recurrence, not
severity**, what earns a check, and tests each rung against *all* recorded occurrences. Applied:
rung 1 (findable from where the reader stood) names the reader-side carve-out of DS1, which
would have prevented both onramp reads; rung 2 (mechanise at the moment of failure) names the
shape check of DS6, which would have caught the 2026-08-02 entry and the 2026-10-18 entry and
not the 2026-08-17 one. The delta stops at a reworded duty — the move the section says "feels
like progress and reliably is not" — and declines the check on an impossibility claim. Harvest
(lens 3) as well: the earlier verdicts were not cited, and the 2026-08-17 disclosure rule was not
reconciled with the new duty.
*Counsel:* cite the three occurrences by date in the grounding; take rung 1 (DS1) and queue rung
2 (DS6) as a warn-only `reviewscan` or `pointerscan` line over `SESSIONS.md` tails and claim
lines.

### Overall, restated after reconcile

**PASS-WITH-FINDINGS — 1 MAJOR (DS1), 4 MODERATE (DS2, DS3, DS4, DS12), 5 minor (DS6, DS7, DS8,
DS9, DS11), 2 notes (DS5, DS10).** Act-1 severities unchanged; two findings added at reconcile
and labelled so. Follow-ups added: DS11 — widen rule 1's umbrella sentence; DS12 — cite the
earlier occurrences and run the rung test on the record.

---

## Deferred sibling, folded below the verdict (orchestrator, 2026-10-25)

*Released to the reviewer only after its act-1 findings were saved; folded here verbatim and
the sibling file deleted, per the brief. The orchestrator (session `52e11d15`, Claude Opus 5.5)
formed no finding and wrote no severity.*

### Sibling to the deferral-side-doors cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-18-0508-deferral-side-doors-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-18 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Facts held back

1. **Intent and commissioning record:** `320/720` (the hand-up item whose path the brief bars) —
   **not opened by the brief-writer**. The landing commit's message body was not read either, so
   this sibling carries no account of the author's reasons; read both at reconcile.
2. **The neighbouring pass.** The paragraph's last sentence hands the commit-message door to
   `130/030`. That item's fix landed the same day as `8132805` (`tools/coldsweep.py --commit`)
   and `30aa8dc` (`skills/review-brief/SKILL.md`), and is queued for its own cold pass at
   `160/930`, briefed in the same sitting by this same brief-writer. The two passes share a
   brief-writer's framing; neither was told what the other found.
3. **Prior verdicts on these surfaces** (named by filename only, not opened, not exhaustive):
   the passes on rule 1's split (2026-07-29 and the DF series, 2026-08-02) and on the coldsweep
   ruling (2026-08-17) are the nearest; find them with
   `ls docs/reviews | grep -iE 'defer|split|coldsweep|cold-sweep'` at reconcile.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. **Subjects versus bodies.** The paragraph lists "recent commit subjects" as a door read at
   onramp, then says "the commit-message door is `130/030`'s". As landed, `130/030`'s fix is a
   body-free read of a landing commit *during* the review; it does nothing about subjects read at
   onramp by `git log --oneline`. Is the subject door covered by this paragraph's own "file and
   count only" duty, by `130/030`, or by neither?
2. **Scope sentence.** Rule 1 sits under a scope sentence binding rules 1–2 "whenever the brief
   is written by, or on the framing of, the work's author". The grounding case was a non-author
   brief-writer. Does placing the side-door duty inside rule 1 leave a non-author brief-writer
   (the grounding case's own writer) outside the rule's stated reach?
3. **Unnamed writers.** A queue-run orchestrator that dispatches a brief-writer writes the pointer
   claim, the index line in `docs/ROADMAP.md`, the session entry and commit subjects, and may
   relay the brief-writer's hand-back into its own records. It is neither "the author" nor "the
   brief-writer". Is it bound? The same question for the generated `docs/ROADMAP.md` line, which
   repeats the pointer's headline.
4. **The `RECORD.md` placement.** The sentence is appended to a bullet about keeping the index
   short and about a size-budget grounding. Will a session writing its close entry meet it there,
   and does the session-close skill (or its template) carry the same duty?
5. **One instance.** The paragraph is grounded in one episode ("Neither steered a finding").
   `PROPAGATION.md` § *When a rule keeps breaking* sets when a lesson becomes doctrine. Is this a
   gap closed in existing doctrine (no threshold owed) or a new rule minted on one instance, and
   does the text say which?
