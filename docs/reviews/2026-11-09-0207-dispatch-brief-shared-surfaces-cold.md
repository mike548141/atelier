# Cold pass — the dispatch brief, the pathspec and leaver's rules for the shared index, the long-check poll, the shared process table and load, worktree names, brief reading, the stop triage and the device at close

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is doctrine
by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN, 2026-11-22 UTC, by a Fable 5.1 cold reviewer under off-tier orchestrator
`7968f851` (started by drain session `eca14b23`): PASS-WITH-FINDINGS, MAJOR 0 · MODERATE 2 · minor 4
· note 3. Act 2 (reconcile) follows the orchestrator's release of the sibling. The brief was written
2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5 brief-writer; the pass ran under the
principal's drain approval of 2026-11-23 NZDT (quoted in the verdict's provenance).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/995-rule-4-cold-pass-queued-dispatch-brief-and-shared-surfaces.md`.
**Size of this pass:** medium: about 140 lines of doctrine in three files, nine items' rules at
once.
**Why it earns a review:** This is standing concurrency doctrine every queue run and child reads.
The worst failure is a rule that cannot be followed as written, or a copied skeleton that drops or
contradicts the rule it points at.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Opus worker it dispatched, which wrote the text (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** session `d4a0fcf3` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-09 UTC by coordinating session `74f2b8cd` (Opus 5.5), on the principal's request to brief
  every owed pass. Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model. `74f2b8cd` built none of these subjects and forms no finding; its launch
  prompt is the brief-writer's only instruction.
- **Barred from running this pass:** session `d4a0fcf3` and session `74f2b8cd` (whoever writes a
  brief does not run it, the principal's rule), and the author session named above with everything
  it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  item numbers, the rules of the run, and the statement that it built none of these subjects. It
  carried no framing of the work. The brief-writer had no contact with the author session or its
  workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the board
  item whole; the intent records' opening part and every line naming the principal or a landing
  account; every delta commit body-free through `tools/coldsweep.py --commit`; commit subjects
  through `git log`; `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole,
  **including that pass's verdict and folded sibling** (a different subject, read for house form),
  the acceptance-test section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words where they exist: the span command below prints `180/150`'s. The first two
spans are the words of the run brief and its close (the record says so), the third is his, and the
fourth is an assistant's sentence the record quotes. Everything else is judged against the standing
doctrine these paragraphs extend: `docs/method/CONCURRENCY.md` §§ *The trigger*, *Orchestrated queue
runs*, *Integration hygiene*; `docs/method/COMMUNICATION.md` § *Asking for a ruling*.

Print only the quoted spans, before phase 1:

```
python3 -c 'import re, sys
for p in sys.argv[1:]:
    t = " ".join(l.strip() for l in open(p, encoding="utf-8"))
    for m in re.findall(r"\*\"(.+?)\"\*", t): print("-", m)' \
  docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/150-close-decisions-not-put-through-the-device.md
```

## What the work is

- **`9f6cc7c`** — `concurrency: give dispatch prompts a copyable skeleton and close five
  shared-surface gaps`.

Delta paths, read at each commit and at HEAD:

- `docs/method/CONCURRENCY.md`, `docs/method/session-open/dispatch-brief.md`,
  `docs/method/session-open/README.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 9f6cc7c HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path docs/method/CONCURRENCY.md --path \
  docs/method/session-open/dispatch-brief.md --path docs/method/session-open/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 9f6cc7c..HEAD -- docs/method/CONCURRENCY.md
docs/method/session-open/dispatch-brief.md docs/method/session-open/README.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "A worktree is the only index of one's own"; `git commit -- <paths>` "takes only the paths named
  and leaves a peer's staged entries staged".
- "A refused commit leaves its paths staged", and the leaver unstages before investigating.
- "Run the gate in the foreground asks for something the harness will not do"; the worker redirects
  output to a file ending in an exit line and polls it.
- Worktree names carry the session's short id, `<repo>-qr-<id>-<slug>`.
- "The fixed obligations are copied, not recalled": `session-open/dispatch-brief.md` "holds no rule
  of its own" and each line points at its grounding.
- A kill is scoped by PID or worktree cwd; the load average, not only free memory, sizes a wave, and
  "this sets no ceiling".
- "A stop other than economics or session cap is claimed on a triage", and the triage's categories.
- The orchestrator "reads every brief in full before it lands".
- Each open decision goes through the device, and "a 🎯 line in the closing message is not the
  device".

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the pointer paragraph `6e610dd` (pass `160/986`); the loose-end close rule `1569e64`
(pass `160/996`); later edits to these files, except as they bear on HEAD.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states this behaviour (V3); one home (V4); no
   contradiction (V5). Find tests that would stay green on a broken delta by mutating a scratch
   copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design; at code altitude the likely vectors for its class, checked against an open
   catalogue (OWASP ASVS or the domain's equivalent). Aim `/security-review` at code only from a
   clean tree, as *House rules* says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root,
in the foreground or under `nice`; its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH`.

```
python3 tools/pathscan.py --root . docs/method/session-open/dispatch-brief.md
nice -n 10 python3 -m unittest discover -s tools
```

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0207-dispatch-brief-shared-surfaces-cold.deferred.md` (a held-back file; by
count: 7 questions, 1 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/120-dispatch-prompts-drop-the-scratch-and-marker-obligations.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/130-briefs-landed-on-scanner-results-not-read.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/140-the-run-stopped-by-judgement-with-work-untriaged.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/150-close-decisions-not-put-through-the-device.md`
- `docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/160-worktree-names-do-not-say-which-session.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/350-a-peer-can-stage-into-the-shared-index-while-your-commit-hooks-run.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/630-a-refused-commit-leaves-its-work-staged-for-the-next-committer.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/680-a-dispatched-worker-cannot-keep-a-long-check-in-the-foreground.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/700-the-process-table-is-a-shared-surface-and-a-pattern-kill-crosses-sessions.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/120-dispatch-prompts-drop-the-scratch-and-marker-obligations.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/130-briefs-landed-on-scanner-results-not-read.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/140-the-run-stopped-by-judgement-with-work-untriaged.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/150-close-decisions-not-put-through-the-device.md \
  --also-exclude docs/roadmap/180-orchestrated-queue-runs-from-hand-carrie/160-worktree-names-do-not-say-which-session.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/350-a-peer-can-stage-into-the-shared-index-while-your-commit-hooks-run.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/630-a-refused-commit-leaves-its-work-staged-for-the-next-committer.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/680-a-dispatched-worker-cannot-keep-a-long-check-in-the-foreground.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/700-the-process-table-is-a-shared-surface-and-a-pattern-kill-crosses-sessions.md \
  'dispatch-brief|pathspec|leaver|long check|process table'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`DB`: `DB1`, `DB2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (cold pass, Fable 5.1, 2026-11-22 UTC)

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Every finding, severity and lens answer below is this session's.
- **Orchestration, disclosed:** spawned by a headless per-pass orchestrator, session `7968f851`
  (Opus 5.5), itself started by drain session `eca14b23` (Opus 5.5). Both are off-tier
  orchestrators: they hold the context partition, form no finding and write no severity. Neither
  wrote this brief or any of the delta. The spawn prompt was process only: paths, the worktree,
  the brief, the barred set, the deliverable's shape, the review-log path, live-system and load
  rules, release timing. It carried no question about the delta and no pointer to where a risk
  lives. Its text is in the orchestrator's transcript; the parts that bound this pass are restated
  in the review log, appended at the fold.
- **Barred sessions, honoured:** `d4a0fcf3` (brief-writer), `74f2b8cd` (its coordinator) and the
  author session `4c65083c` with everything it started. This session was started and instructed by
  none of them, and neither was `7968f851` nor `eca14b23`. No contact from any of them during the
  pass.
- **Approval:** the principal's drain order of 2026-11-23 NZDT, verbatim: *"Start a fable drain or
  whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-995-2249/atelier` at `24b8e2b7` (the claim
  commit). Read-only to me except this file. The sibling `.deferred.md` shows as deleted in
  `git status`: the orchestrator removed it on purpose for the partition; I did not look for it in
  history, other checkouts or any held location. The user-local review log is
  `~/.claude/fable-drain/notes/atelier-160-995-2249.md`, outside the repo.
- **What I read before writing (rule 2):** this brief; `docs/method/REVIEW.md` whole; the delta
  commit `9f6cc7c` body-free through `tools/coldsweep.py --commit --path` (the three delta paths;
  11 board-store files left out by default, 0 rule-2 files touched); the three delta files at
  HEAD (`CONCURRENCY.md` §§ *The trigger*, *Claiming work* lines 400–412, *The substrate*,
  *Orchestrated queue runs* whole); `COMMUNICATION.md` § *Asking for a ruling*; `GUARDS.md`
  120–165; `EVIDENCE.md` 362–382; two census records of 2026-11-16 at the sweep's hit rows;
  `tools/sweepscan.py`, `tools/board.py`, `tools/floor.py` and `instruments/ccfleet`,
  `instruments/cclive` at the lines named in the log; `skills/review-drain/orchestrator-prompt.md`
  whole; `skills/*/SKILL.md` by grep; the first line of the acceptance-test spans. I skipped the
  session-log onramp step. I did not open the sibling, any prior verdict, `docs/sessions/`,
  `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`, board item `160/995` beyond its title, the nine
  barred intent records beyond their first line, or any commit body. Intent records `180/190` and
  `180/200` (not barred) were read at the sweep's hit lines only.
- **Harness context, disclosed:** the harness loaded user-level and repo instruction files and a
  memory index before the brief; none of it names this delta. One system note at start-up listed
  live sessions' command lines when I read the process table (`pgrep`, read-only); I used nothing
  from it beyond "two other passes' suites were running".
- **UTC day:** 2026-11-22 (written between 22:52 and the time of the Status line).

### The acceptance test, applied

The span command printed four spans (log). Spans 1–2 are the run brief's words (*"Ask me with
AskUserQuestion when you need a decision"*, *"Walk me through any open decision … one at a
time"*),
span 3 the principal's (*"did not use askuserquestion for its questions"*), span 4 an assistant's
sentence. The device paragraph at HEAD (CONCURRENCY 1288–1295) answers all three of his: each open
decision through the device, one at a time, and prose only where the harness has none. The other
eight items are judged against §§ *The trigger*, *Orchestrated queue runs*, *Integration hygiene*
and `COMMUNICATION.md` § *Asking for a ruling*, as the brief says.

### Load-bearing assumptions, named first (lens 1), and what the probes did to them

| # | Assumption the delta rests on | Probe | Result |
| --- | --- | --- | --- |
| A1 | `git commit -- <paths>` commits only the named paths and leaves a peer's staged entries staged | scratch repo, probe 1 | **Confirmed.** Commit held `M` only; `N`, `P` still staged after |
| A2 | The `git diff --cached` read before the commit sees what the pathspec commit will carry | probe 2 | **Damaged.** The commit carries the *working-tree* content of the named paths (`v2`), not the staged `v1` the read showed → DB1 |
| A3 | A refused commit leaves its paths staged | probes 3–4 | **Confirmed for the prescribed flow** (explicit `git add` then commit); a bare pathspec commit of a tracked path refused by the hook leaves nothing staged (git rolls the real index back) → DB8 |
| A4 | The harness caps a foreground command and moves it to the background by itself, and the notice then goes to the orchestrator, not the worker | this pass's own re-run of the suite | **Half confirmed live:** at 600 s the tool moved `unittest discover` to the background with a notice, then killed it at its background limit; both notices reached me, the worker. The cap half holds; the notice half did not here → re-run ledger, DB7 |
| A5 | A copyable skeleton in the tree fixes "a prompt written from memory dropped them" | the house's next dispatching skill (review-drain, 2026-11-14) | **Damaged.** It does not start from the skeleton and drops three of its bounds; one of them (foreground gate) reproduced the `320/680` failure in this pass → DB2 |
| A6 | Each skeleton line points at a rule that grounds it ("holds no rule of its own") | each table row read to the rule it names | **Confirmed for eight rows; damaged for one clause:** `Do not push … or open pull requests` has no grounding sentence in QR3, and § *Teardown* treats a pushed worker branch as the normal case → DB3 |
| A7 | The 15-minute load average is the right figure to size a wave on | `instruments/ccfleet` `gate_ok`; this session's `uptime` readings | **Damaged.** The house's own gate tests the 1- and 5-minute figures and ignores the 15-minute one; at 23:56Z the box read 7.81 / 17.25 / 18.72 on 12 cores → DB4 |
| A8 | `lsof -p <pid> -d cwd` scopes a kill "by the worktree cwd it owns" | read-only run of both forms | **Damaged.** That form reports one known PID's cwd; `lsof -a -d cwd -- <worktree>` (or teardown's `lsof +D`) is what finds processes by cwd → DB5 |

Right problem, right altitude: yes. Every one of the nine rules answers a recorded incident in the
run of 2026-11-03, and the shape (one grounded paragraph per gap in `CONCURRENCY.md`, one copyable
block pointing back at them) is the right one for a house whose remedy for prose-only rules is a
stamped copy at the point of use (`PROPAGATION.md`). Where the altitude slips is that the copy is
itself reachable only through prose (DB2) and that two of the nine rules name a check or a command
that does not do what the sentence says (DB1, DB5).

### Lens 2 — correctness: the claims, re-driven

- *"A worktree is the only index of one's own"; pathspec commit "takes only the paths named and
  leaves a peer's staged entries staged."* True (A1) and incomplete: it takes the working tree's
  content of those paths (A2). DB1.
- *"A refused commit leaves its paths staged."* True through the explicit `git add` the same
  paragraph prescribes; not a property of the pathspec commit itself (A3). DB8.
- *"Run the gate in the foreground asks for something the harness will not do."* True on this
  harness today (A4). The next clause, "the completion notice then goes to the orchestrating
  session, not the worker", and the skeleton's "the completion notice will not reach you", did
  not hold here: both the move and the kill notices reached this worker. The paragraph hedges the
  cap ("the tool's in that session, not a constant") and not the routing. The poll rule is right
  either way; its form leaves one trap (DB7).
- *Worktree names `<repo>-qr-<id>-<slug>`.* Consistent with § *The substrate*'s generic
  `<repo>-<feature>` as a specialisation of it; the only other house worktree naming found
  (review-drain: basename = repo, for per-repo billing) is a different pattern and says so. No
  finding.
- *"The fixed obligations are copied, not recalled"; the skeleton "holds no rule of its own."*
  Eight of nine rows reach the rule they name (log). One clause overclaims (DB3).
- *Kill scoped by PID or worktree cwd; load as well as memory; "this sets no ceiling."* The rule
  is sound; the parenthetical command and the chosen load figure are not (DB5, DB4). "Sets no
  ceiling" is honest.
- *A stop other than economics or session cap is claimed on a triage.* The five categories map
  onto the selection rules above them (idea-only, ruling-bound = 🎯, review-tier-bound = ⏳).
  Sound.
- *The orchestrator reads every brief in full before it lands.* Consistent with rule 4's
  orchestrator clause (it forms no finding) and with QR2 (a brief a dispatched writer wrote is the
  run's authorship). Sound.
- *Each open decision through the device; a 🎯 line is not the device.* Matches
  `COMMUNICATION.md` § *Asking for a ruling* at HEAD, including the 2026-11-12 "same turn"
  wording landed later (`2a6d7a41`). Sound.
- The `README.md` sentence ("house text, not the principal's") was kept true through
  `8ef055ee`. Sound.

### Lens 3 — completeness and harvest

- The hook already nudges toward the pathspec form: `sweepscan.py` reads `GIT_INDEX_FILE` and warns
  on a whole-index commit where sibling worktrees exist (`next-index-<pid>.lock` = pathspec, no
  warn). The delta did not cite it; a reader of § *The trigger* does not learn the hook agrees.
  Note only, folded into DB1's counsel.
- `GUARDS.md` § *The pathspec caveat is not detachable* (approved 2026-11-09, after the delta)
  states the precondition the delta's paragraph relies on (the other staged paths are
  *identified*). It names the index plane only; DB1 is the working-tree plane it leaves out.
- No test pins the skeleton to the section it copies, nor the skeleton's lines to the rules its
  table names (census CON67 says the same). A test that would stay green on a broken skeleton: all
  of them. DB6 counsel.
- Mirror sites swept (V3): `skills/`, `tools/`, `instruments/`, `docs/build/`, `CLAUDE.md`,
  `README.md`. The only dispatching text outside `CONCURRENCY.md` is review-drain's, and it does
  not carry the skeleton (DB2).

### Lens 4 — security and privacy (V6)

- **Design altitude.** The delta adds an instruction channel: text copied verbatim into the prompt
  of the least-vetted seat (QR4 names that seat). Its sibling file in the same directory carries a
  stated threat section (who can change what runs, what catches a hostile commit, what is not
  guarded); the skeleton carries none, and the README's threat section is scoped to the command's
  prompt. REVIEW.md lens 4: absent enumeration is the finding. DB6.
- **Over-collection / leakage.** None. The placeholders are filled at dispatch time with local
  paths that live in transcripts, not in the repo. The example worktree name carries a session id's
  first four characters, which `RECORD.md` already puts in every record. No personal data entered
  the delta; `docs/PERSONAL-DATA.md`'s closed list is untouched.
- **Code altitude.** No code in the delta. `/security-review` NOT RUN: the delta is markdown, which
  the scanner's own exclusions bar (an empty pass weighs as nothing), and my worktree is not clean
  while I write (the deleted sibling; this brief), the SL2 shape the house rules forbid aiming it
  in. The code-altitude read was done by hand on the two commands the delta prescribes (A2, A8).

### Standing checklist V1–V7

- **V1** No claim stronger than its evidence: two claims are (DB1, DB3); "sets no ceiling" and
  "the cap's figure is the tool's in that session" are honest hedges.
- **V2** Re-run: all three brief lines re-run (ledger below); the two prescribed commands re-driven
  in a scratch repo and read-only on this box.
- **V3** Swept to every mirror: `README.md` yes; the hook agrees by construction; the house's own
  later dispatch prompt does not carry it (DB2).
- **V4** One fact, one home: the skeleton is a stamped copy with a grounding table, which is the
  right shape; the worker-push step has two pictures in one file (DB3).
- **V5** No contradiction: the read and the commit in § *The trigger* act on different planes
  (DB1); the load figure named differs from the house gate's (DB4); the kill-scope command does
  not match its clause (DB5). Cross-references: every skeleton row reaches the rule it names (log,
  lines cited), so none dangles.
- **V6** Done above; DB6.
- **V7** Provenance stated in the brief and repeated above.

### Per-commit ledger

| Commit | Read body-free | Findings |
| --- | --- | --- |
| `9f6cc7c` — concurrency: give dispatch prompts a copyable skeleton and close five shared-surface gaps | yes (`coldsweep --commit --path` × 3) | DB1, DB3, DB4, DB5, DB6, DB7, DB8, DB9 |
| later commits on the delta paths (25, subjects only) | not read as commits; their effect read at HEAD | DB2 rests on `4bfb4e16` (review-drain, 2026-11-14), read as a file at HEAD |

### Findings

Every finding is the principal's to decide (REVIEW.md rule 3); nothing is applied. Counsel is
labelled.

**DB1 — MODERATE.** *The read the doctrine prescribes and the commit it prescribes act on
different planes.* § *The trigger* (CONCURRENCY 93–104) says the check that sees a shared index
is `git diff --cached` "immediately before every commit", then adds "commit by pathspec too". A
pathspec commit does not commit the index: it commits the working-tree content of the named paths
("without recording the changes already added to the index", git-commit(1)). Probe 2: staged `v1`,
working tree edited to `v2` after the read, `git commit -- M` landed `v2`, and the staged diff never
showed it. In the shared primary checkout, the one place the paragraph says this commit is used (an
orchestrator's claim on `main`), a peer's unstaged edit to a path you name rides your commit unseen
by the read that is said to make the technique safe; the doctrine itself names the uncommitted
working tree as the thing nothing protects. `GUARDS.md`'s caveat ("the paths are identified")
covers the other staged paths, not the content of your own. V1, V5.
*Counsel:* say in § *The trigger* that the pathspec commit takes the working tree, and pair it
with the read that sees that plane, `git diff HEAD -- <paths>`, kept beside `git diff --cached`
(which still answers "what else is staged here"). Mention that `sweepscan.py` already recognises
the form at the hook.

**DB2 — MODERATE.** *"Every dispatch prompt carries the same bounds … a dispatch starts from it"
is unmet by the house's own next dispatch prompt, and a dropped line reproduced the grounding
incident in this pass.* `skills/review-drain/orchestrator-prompt.md` (added 2026-11-14, eleven days
after the delta) dispatches a per-pass orchestrator and tells it how to dispatch a reviewer. It
carries the worktree, absolute paths, explicit staging, the pathspec commit and a terminal marker;
it carries no scratch directory, no long-check poll and no kill scope, and says "foreground" for
test suites. This pass's spawn prompt said "foreground with a long timeout"; the brief's
`unittest discover` crossed the 600 s cap and the harness moved it to the background by itself,
the exact failure `320/680` records. The remedy for "rules that lived only in this prose" is a
block whose use is itself directed only by prose (census CON67: directive-only, no test). Stated
honestly: the delta's author could not have swept a file that did not exist; the finding is on the
rule's reach at HEAD and on its mechanism. V3.
*Counsel:* either the review-drain prompts start from the skeleton (its three missing lines added,
"foreground" replaced by the poll), or the rule says which dispatches it binds. A cheap check:
`ccclose` or a dispatch-time grep that the prompt text contains the skeleton's binding lines.

**DB3 — minor.** *The skeleton's "holds no rule of its own" overclaims by one clause, and the
worker-push step has two pictures.* `Do not push, merge or open pull requests` is grounded on QR3,
which reserves the merge to `main` and the floor for the orchestrator and says nothing of a branch
push or a pull request. § *Teardown* (1058–1066) treats a pushed worker branch as the normal case
("merge from the pushed branch"; "a worker that never pushed is the one case …"). Under the
skeleton every worker is that one case. Not a contradiction in effect (teardown handles it), but a
reader meets two pictures of one step. V1, V4, V5.
*Counsel:* ground the clause on the sentence already there ("a push is publication on a public
repo") and make the worktree-path merge the stated default in § *Teardown*.

**DB4 — minor.** *The 15-minute load average is the slowest figure to react, and the house's own
gate does not use it.* "Read the 15-minute load average before adding one" (1227–1229). A wave
added quickly reads a stale low figure while the 1-minute figure is already past the cores; after a
spike it holds a wave for a quarter hour the box no longer needs. `instruments/ccfleet` `gate_ok`
tests the 1- and 5-minute figures and ignores the 15-minute one; `cclive` prints all three with
the core count. This session: 23:56Z read 7.81 / 17.25 / 18.72 on 12 cores. V5.
*Counsel:* "read the load averages against the core count: the 1-minute figure gates adding, the
15-minute shows the trend", which is what the gate already does.

**DB5 — minor.** *The kill-scope parenthetical names a command that answers a different
question.* "scoped by … the worktree cwd it owns (`lsof -p <pid> -d cwd`)" (1224–1225) prints
the cwd of a PID you already have; it cannot find the processes whose cwd is your worktree. Teardown
leg 3 uses `lsof +D <worktree>`; `lsof -a -d cwd -- <worktree>` lists exactly the processes the
clause means (run read-only here). A worker that has lost a PID follows the parenthetical and
finds nothing. V5.
*Counsel:* name `lsof -a -d cwd -- <worktree>` for "find mine", keep `-p <pid> -d cwd` as "check
this one is mine".

**DB6 — minor.** *A new instruction channel with no threat stated.* The skeleton is copied
verbatim into every worker prompt; the sibling prompt in the same README carries a threat
section (who can change what runs, what catches a hostile commit, what is not guarded); the
skeleton has none, and nothing pins its lines (census CON67). A hostile or careless working-tree
edit reaches every worker without a commit, because the orchestrator copies from its checkout.
The exposure is bounded by who can write that checkout, which is why this is minor. Lens 4
design altitude: absent enumeration is the finding. V6.
*Counsel:* one bullet in the README's threat section naming the skeleton; a test pinning the
skeleton's binding lines to `CONCURRENCY.md`, as `test_templates.py` pins the prompt.

**DB7 — note.** *The poll line gives the exit line's shape, not its form, and states the notice
routing as a constant.* "append an exit-code line (exit=<code>)": written as
`<cmd> > <file> && echo exit=$? >> <file>`, the line appears only on success, so a failing gate
leaves the poller waiting, which is the incident the rule cures. And a command the harness moves
to the background can also be killed at a second limit before the exit line is ever written (it
happened here, about twenty minutes in), so the poller needs an end too. On this harness both
notices reached the worker (A4); the skeleton says the notice "will not reach you" as fact while
the paragraph hedges only the cap's figure. V1, at note weight. *Counsel:* give the form in the
block, `<cmd> > <file> 2>&1; echo "exit=$?" >> <file>`; say the notice "may not reach you";
and say a long check is started as a background command with its own limit, not left to be
moved.

**DB8 — note.** *The leaver's rule holds through the explicit `git add`, not through the pathspec
commit.* Probe 3: a tracked path committed by pathspec without a prior add, refused by the hook,
leaves nothing staged (git rolls the real index back); probe 4: with the prior add it stays staged.
The paragraph prescribes both steps, so it is right as written; one clause would stop a reader
generalising "a refused commit leaves its paths staged" to the pathspec form.

**DB9 — note.** *An unanchored "two days later".* "(2026-11-03, `320/350`: a child's hook run …
and two days later a resuming session found …)". The delta is dated 2026-11-03 07:46 UTC, so "two
days later" must count from the hook incident, not from the date in the bracket; the sentence does
not say. Checked against the intent record at reconcile.

### Overall

**PASS-WITH-FINDINGS** — MAJOR 0 · MODERATE 2 (DB1, DB2) · minor 4 (DB3–DB6) · note 3
(DB7–DB9).
The nine rules each answer a real incident and are followable as written; none of the findings
makes a rule unfollowable. Two reach the altitude of a check that does not see what its act does
(DB1) and a rule the house itself did not carry to its next dispatch (DB2).

### Re-run ledger

| Line | How run | Result |
| --- | --- | --- |
| `git merge-base --is-ancestor 9f6cc7c HEAD` | from the worktree, `git -C` | exit 0 |
| the span command (acceptance test) | PATH `python3` (3.14.6), absolute path to the record | 4 spans, as the brief describes them |
| `python3 tools/pathscan.py --root . docs/method/session-open/dispatch-brief.md` | PATH `python3`, `--root <worktree>` | ✓ clean, 1 reference checked, exit 0 |
| `nice -n 10 python3 -m unittest discover -s tools` | PATH `python3`, from the worktree root, `nice -n 10`, single process, output to a scratch file ending in `exit=`; load 7.81 / 17.25 / 18.72 at start, two other passes' suites live | `Ran 3382 tests in 1581.136s` · `OK` · `exit=0`, read from the file. First attempt (foreground) was moved to the background at the 600 s cap and killed by the harness at its background limit before finishing; second attempt ran as a background command with a one-hour limit |
| `/security-review` | NOT RUN | markdown-only delta; dirty worktree by design (grounds in lens 4) |

### Follow-up checklist

- [ ] Principal rules on DB1–DB9 (doctrine by function; nothing applied here).
- [ ] If DB1 is accepted: § *The trigger* names the plane and the `git diff HEAD -- <paths>` read.
- [ ] If DB2 is accepted: decide whether the skeleton binds review-drain dispatches; add the three
      lines or narrow the rule.
- [ ] DB4/DB5: one-line wording fixes, each with its command verified on the house's instruments.
- [ ] DB6: README threat bullet; a pinning test (counsel).
- [ ] Reconcile (act 2): the sibling's 7 questions and 1 fact; the nine intent records; DB9's
      anchor; the delta's commit body.
