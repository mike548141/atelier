# Cold pass — `ccclose --identifiers` credits commits on evidence, not the window

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well as for a
reviewer.
**Status:** PASS RAN 2026-11-01 UTC, phases 1 and 2 — **PASS-WITH-FINDINGS, 14 findings: 1 MAJOR
· 7 MODERATE · 5 minor · 1 note** (verdict and `### Reconcile` below the divider; the sibling
was released to the reviewer after act 1 was committed and is folded in by the orchestrator).
Reviewer: Fable 5.1 under off-tier Opus 5.5 orchestrators (sessions
`0d67673f` and `c87c4ee0`), disclosed in the verdict's provenance. Brief written 2026-10-26 UTC
by an Opus 5.5 brief-writer subagent of session 5070f22b; the pass was taken by a cold Fable
session that neither the delta's authors nor session 5070f22b (nor any of its subagents) started
or instructed.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md`.
**Why it earns a review:** the identifiers block is designed to be pasted into session records
and closing messages as fact (`docs/method/RECORD.md`, the identifiers-block rule). This delta
changes which commits and which board movement the block credits to a session. The worst
failure is silent: a block that credits a session with commits it did not make (over-credit), or
drops ones it did make (under-credit), with nothing in the output that tells the reader so. A
wrong block is copied into a durable record and then read as the record's own evidence.

## Spawn provenance

- **Authors of the work under review:** a Mike-opened Opus 5.5 queue run, session `8e498ef1`,
  2026-10-18, in worktrees `atelier-qr-210-290` and `atelier-qr-210-310`, and the worker it
  dispatched, which wrote the code (the pointer says so). The same session widened the delta to
  `e78b6f1`. Git cannot name a session; this attribution is the pointer's and the intent
  records'.
- **Who wrote this brief:** an Opus 5.5 subagent (`claude-opus-5-5`) dispatched on 2026-10-26 by
  session `5070f22b`, a headless Opus 5.5 brief-writing session started on the principal's
  instruction of that day. Neither authored any of this delta: its three commits are dated
  2026-10-18, and the dispatching session's claim commit, `2f6dbf6`, is dated 2026-10-26
  (git cannot name a session; this is the dispatcher's account). **Off-tier
  for review, disclosed: the brief-writer forms no finding and writes no severity**, and stops
  after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, rule 4's off-tier conditions apply and are
  disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance in
  its verdict.
- **Barred from taking this pass:** session `8e498ef1` and its workers; session `5070f22b` and
  its subagents, this brief-writer included.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing):
  - its dispatch prompt and a common-rules file from `5070f22b` (form and house rules, no view
    of the delta); `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` lines 20–230
    and 320–450; `docs/method/RECORD.md` lines 93–125;
  - as shape examples: `docs/reviews/2026-10-18-0511-template-history-privacy-cold.md` and its
    sibling, whole (another pass, on other surfaces), and
    `docs/reviews/2026-10-18-0508-body-free-commit-read-cold.md` above its first divider,
    whose status line states that pass's verdict counts (another pass, on `coldsweep`);
  - the pointer `160/960` whole; the first 600 bytes of the `160/920` pointer (its state line
    and the start of its claim) and a grep that printed its brief's path; the recent commit
    subjects shown at session start, which include the headline verdict lines of `160/920` and
    `160/930`;
  - **both intent records, read in full** (`210/290` and `210/310`, the author's accounts; held
    in the sibling, not here);
  - the three delta commits body-free through `tools/coldsweep.py --commit`: `0462173` lines
    1–330 of its output (the code hunks) and a grep of its test names, and the stat, first
    lines and closing line of `621d18b` and `e78b6f1`, lines 60–80 of `e78b6f1`'s output (a
    path helper), and a grep of `e78b6f1`'s test names.
    **No commit message body was read;**
  - the heading list of `instruments/ccclose.design.md`, `ccclose --help`, four lines of the man
    page, `.github/workflows/ci.yml` lines 110–130, the head of `.wrapscanignore`, and the
    re-run outputs below (exit codes and counts);
  - one live run of the tool on the authoring session's transcript, reading the JSON for
    aggregate counts only; no transcript text was opened or quoted.

  It did **not** open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, the
  `160/920` brief or verdict, or any other prior verdict. Its harness also loaded user-level and
  repo instruction files and a memory index, which hold private context this brief does not
  carry. Everything evaluative it formed is in the sibling, by count in its header.

## The acceptance test

Neither intent record quotes the principal, so there is no verbatim test there. The test is the
rule the block serves, in doctrine and not barred: `docs/method/RECORD.md` lines 95–123, the
identifiers-block rule, with the principal's own words at lines 118–123 (*"commit ID's created
by the session"*, and the board work completed and created). Judge the block against that: every
commit the session and its workers landed, and no other, with anything the tool cannot derive
said so. The delta's own statements of its contract are the delta, and are to be tested, not
believed: design note §15.1 (`instruments/ccclose.design.md` lines 350–420 at HEAD), the man
page's `IDENTIFIERS` section and `--identifiers` entry, the `instruments/README.md` paragraph,
and the code comments.

## What the work is

All on `main`, delta scoped to `instruments/ccclose`, `instruments/ccclose.test.js`,
`instruments/ccclose.design.md` (§15.1), `instruments/man/ccclose.1` and `instruments/README.md`:

- `0462173` (committed 2026-10-18 05:46 UTC) — instruments: ccclose --identifiers credits
  commits on evidence, not the window. `instruments/ccclose`, `instruments/ccclose.test.js`.
- `621d18b` (committed 2026-10-18 05:46 UTC) — instruments: document ccclose's evidence-based
  commit attribution. `instruments/README.md`, `instruments/ccclose.design.md`,
  `instruments/man/ccclose.1`.
- `e78b6f1` (committed 2026-10-18 06:45 UTC) — instruments: ccclose reads a commit message from
  a file the session wrote. All five paths. This is the pointer's widening (`210/310`).

No later commit touches any delta path at `2f6dbf6`; confirm it at your HEAD. Review the paths
at HEAD and diff each commit. **Read the commits body-free:** `python3 tools/coldsweep.py --root
. --commit <sha>` for each. Plain `git show` is barred: it prints the message body before the
diff, and reading is atomic (rule 1).

**Boundary against `160/920`.** That queued pass reviews *earlier* commits to these same files;
this pass does not. Its brief and verdict,
`docs/reviews/2026-10-18-0506-close-covers-subagents-cold.md`, is a prior verdict, barred until
your phase 2 under rule 2, and so is its pointer. Your scope is the hunks of the three commits
above and the behaviour they produce. Pre-delta code is read only where the delta's behaviour
depends on it (the window, the transcript reader, `ghPrCommands`, the subagent directory); a
defect you meet there that the delta did not introduce is recorded as a note against the
out-of-delta surface, never a finding on this delta, and reconciled against `160/920` in
phase 2.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Probe, at least:

- **Ground truth, by table.** In throwaway repos under your scratchpad, with synthetic
  transcripts (the test file's helpers show the transcript shape), build sessions whose true
  authorship you know, then record for each commit: truly the session's or not, and what the
  block printed (credited, unconfirmed, left out). Count over-credits and under-credits
  separately. Cover at least: two sessions on one repo at once, on `main` and on branches;
  identical or near-identical subjects across sessions; a commit command that ran but made no
  commit; amend, rebase, cherry-pick, revert and merge commits; `git -C`, `-c`, aliases and
  `commit -a`; every message form (`-m`, repeated `-m`, `--message=`, heredocs, `-F -`,
  `-F <path>`, `--file=`, a variable); a squash merge by `gh pr merge`, by another route, and a
  `(#n)` subject that is not a squash merge; subagents and separately dispatched worker
  sessions.
- **The file tier (`e78b6f1`).** Path resolution against cwd and `git -C`, the ordering of a
  write against the commit that reads it, parent and subagent ordering, and the limits §15.1
  states. Say whether each stated limit errs towards under-credit or over-credit.
- **Board movement.** The confirmed and unconfirmed board lines: is any movement dropped,
  double-listed or moved between tiers wrongly? Check the `⏳` state-line reading against
  `tools/board.py`'s own grammar, which the code says it mirrors.
- **The block as pasted.** Read the rendered block and `--json` as a reader who pastes it. Does
  every line that reads as fact rest on evidence, and does every heuristic line say it is one?
  Does the output meet `RECORD.md`'s field list?
- **Silent paths.** Every `catch {}` or skipped line on the evidence path: can a malformed or
  unreadable transcript, subagent file or git failure shrink the evidence and so move commits to
  "unconfirmed" or out of the block without saying so?
- **The docs against the code.** §15.1, the man page, the README paragraph and the code comments
  against the behaviour your table shows, and against each other.
- **The tests.** Do they fail when the guarantee breaks? Mutate the evidence check (for example,
  credit every window commit, or match subjects by prefix) and re-run the file; a suite that
  stays green is a finding.

**Non-goals:** the pre-delta behaviour of `ccclose` (`160/920`'s), the window heuristic as used
by the other checks, and the field set `RECORD.md` asks for. Whether the delta serves that field
set is in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first, then the ones
   below. Ask whether matching on the command text is the right evidence at all, set against
   other evidence a session leaves.
2. **Correctness & quality.** Diff all three commits; run the probes live; record each
   overclaim against the text that makes it.
3. **Completeness / harvest.** Every message form and merge route a session in this house uses;
   every surface that documents the block (the three docs, `--help`, `RECORD.md`); any
   changelog or stamped copy owed.
4. **Security & privacy** — mandatory. The tool reads the principal's session transcripts and
   shells out to git. Check by hand against the OWASP catalogue: whether any transcript-supplied
   string reaches a git argument, a filesystem read or a regex that can be made to run long
   (A03 Injection, and ReDoS); whether a path named in a transcript is ever opened from disk;
   and what transcript text, beyond commit subjects already in git, can reach the block's
   output. Check the test fixtures build no real identity. Aim `/security-review` at the code
   diff only from a clean tree or a scratch clone (see *House rules*), or discharge it in one
   line with grounds.

## Load-bearing assumptions to attack

Each is a falsifiable claim; damage it with a probe or confirm it by re-driving.

- A1. A window commit whose subject equals a subject in one of the session's commit commands was
  made by that session.
- A2. A commit the session made always leaves its subject readable in the session's (or a
  subagent's) command text or in a file the session wrote, except for the forms §15.1 names.
- A3. A commit on the integration branch's first-parent line whose subject carries a PR number
  is a squash merge of that PR, and repeats commits already counted elsewhere.
- A4. The session's `gh pr merge` commands identify every PR merge the session made.
- A5. Board movement belongs to the session exactly when the commit that made it is confirmed.
- A6. An item's first line is its state line, and `board.py`'s grammar for it is the one the
  code applies.
- A7. Nothing in the evidence path fails silently.
- A8. The docs (§15.1, man page, README) describe the behaviour the code has.

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, from the worktree root at `2f6dbf6`,
in the foreground; its results are held in the sibling, not offered here. Read exit codes
explicitly. In zsh, list the five paths by name: a variable holding them does not split.

- `python3 tools/coldsweep.py --root . --commit <sha>` for `0462173`, `621d18b`, `e78b6f1`
- `nice -n 10 node --test instruments/ccclose.test.js`
- `nice -n 10 node --test instruments/*.test.js` (the CI form)
- `mandoc -T lint -W style instruments/man/ccclose.1` and the CI form `mandoc -T lint
  instruments/man/ccclose.1`; then `awk 'length > 80' instruments/man/ccclose.1`, and for any
  line it prints, `git blame` it to say whether this delta wrote it
- `python3 tools/wrapscan.py --root .`, `python3 tools/spellscan.py --root .` and `python3
  tools/leakscan.py --require-terms --root .`, each over the five delta paths; `instruments/` is
  outside the floor's wrapscan path, so blame any line flagged before weighing it
- `git log --oneline e78b6f1..HEAD -- <the five paths>` — empty, or name each commit
- `nice -n 10 python3 tools/floor.py --plane ci --root .`
- `node instruments/ccclose --help`
- the live re-drive, where the principal's transcript store is on the machine: `node
  instruments/ccclose --identifiers --json --session <path to session 8e498ef1's .jsonl> --root
  .`, read-only. Report aggregate counts only (confirmed, unconfirmed, left out, board lines),
  and check them against ground truth you derive from git yourself. Quote no transcript text,
  and name no other session or repo. From a session without the store, state the impossibility
  with its grounds.

## House rules for this run

- Name the worktree you work in. Run no git command that writes there beyond committing THIS
  file at the end of each phase (or handing it to your orchestrator); read-only git is fine.
  Probe repos, synthetic transcripts and mutated copies go under your session scratchpad, named
  by your prefix, and are deleted when you finish. Never mutate the worktree's `instruments/`.
- One heavy process at a time on a shared machine; check `uptime` first; run test suites in the
  foreground under `nice`. Never run an installed tool by bare name from `PATH`; use the
  worktree's `node instruments/…` and `python3 tools/…`.
- The principal's transcripts are private and this repo is PUBLIC. Use synthetic transcripts
  and the test fixtures for every probe that needs text. If you touch the real store, read it
  only through the tool, report counts only, and quote nothing: no subject, path, command or
  message text from it, in the verdict, a commit message, the pointer or a session log. Where
  the adopting child repos on the machine would add evidence, report them by count, never by
  name.
- Recent commit subjects on `main` carry other passes' headline verdicts, `160/920`'s among
  them. If your onramp meets one, disclose it in your provenance.
- This pass is pending while you run it: anything you write to the session log, the pointer or
  a commit subject before phase 2 names the sibling by file and count only.
- `/security-review` reads the session's pending diff, not this delta. Never run it with this
  brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/` (the `160/920` file named above among them), the queue pointer
`docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md`,
the `160/920` pointer
`docs/roadmap/160-doctrine-review-owed/920-rule-4-cold-pass-queued-close-covers-subagents.md`,
this brief's sibling `docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.deferred.md`,
the message bodies of `0462173`, `621d18b` and `e78b6f1`, and both intent records, whole:

- `docs/roadmap/210-instruments-open-features/290-ccclose-identifiers-over-credits-overlapping-sessions.md`
- `docs/roadmap/210-instruments-open-features/310-ccclose-cannot-read-a-commit-message-from-a-file.md`

`RECORD.md` and the delta itself, its comments and §15.1 included, are not barred.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/960-rule-4-cold-pass-queued-identifiers-credit-on-evidence.md
--also-exclude
docs/roadmap/160-doctrine-review-owed/920-rule-4-cold-pass-queued-close-covers-subagents.md
--also-exclude docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.deferred.md
--also-exclude
docs/roadmap/210-instruments-open-features/290-ccclose-identifiers-over-credits-overlapping-sessions.md
--also-exclude
docs/roadmap/210-instruments-open-features/310-ccclose-cannot-read-a-commit-message-from-a-file.md
<pattern>`; `--include-barred` only with disclosure in the verdict.

## Process

**Phase 1.** Reproduce the floor first; work the lenses, the scope probes, the assumptions and
the re-run list; run the standing checklist V1–V7 unasked, each answered or discharged with
grounds. Append your verdict below a `---` divider in THIS file: provenance repeated (how you
were spawned, your tier, what you read), per-lens answers, the per-assumption result (A1–A8),
the ground-truth table's totals (over-credit and under-credit counted separately), findings with
stable IDs (prefix `IE`: `IE1`, `IE2`, …) and severities (MAJOR / MODERATE / minor / note), an
overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger (commands and
results) and a follow-up checklist. Then STOP and commit phase 1 unrevised before opening the
sibling. Edit no other file.

**Phase 2.** Open the sibling, the intent records, the three commit bodies and the `160/920`
verdict. Append `### Reconcile` beneath your verdict: per-finding notes against the sibling's
questions, the authors' accounts and `160/920`'s findings (which of yours it already holds, and
which of its it bears on), any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. Then fold the sibling in below the reconcile and delete it.

The pass was queued as a doctrine pass, and the block it reviews is pasted into records as fact:
record all findings and apply nothing (rule 3); the principal decides. Counsel per finding is
welcome, labelled as counsel and kept beneath it.

---

## Verdict — phase 1, cold pass ran 2026-11-01 UTC

**Overall: PASS-WITH-FINDINGS — 13 findings: 1 MAJOR · 7 MODERATE · 4 minor · 1 note.** The
delta does what its headline says on the suite's own cases and on the live re-drive, and both
mutants die. It does not hold on the case the design dismissed: a concurrent session that
commits with the same subject is credited as fact (IE1), and three further ways the evidence
set grows larger than the commits actually made compound it (IE2–IE4). Nothing is applied
(rule 3); counsel sits beneath each finding.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection, the principal-named
  review tier. I run under the principal's 2026-11-02 drain approval for Fable work.
- **Spawned by** session `0d67673f`, a headless Opus 5.5 orchestrator, itself started by
  session `c87c4ee0` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context
  partition, form no finding and write no severity. This arrangement is disclosed here, in the
  claim and in the pointer.
- **Not** started or instructed by the barred sessions: `8e498ef1` and its workers (the
  delta's authors), or `5070f22b` and its subagents (the brief-writer).
- **Worktree:** `atelier-160-960-1245`, HEAD `947d86f`. The sibling `.deferred.md` was removed
  from the worktree by the orchestrator before I started (it shows as a deleted file); I did
  not look for it anywhere. I made no git write.
- **Onramp exposure, disclosed:** the recent commit subjects at session start carried the
  headline verdicts of `160/940` ("PASS-WITH-FINDINGS (0 MAJOR)") and `160/970` ("0 MAJOR").
  Neither is `160/920`'s, and neither steered a finding. My harness also loaded user-level and
  repo instruction files and a memory index, as the brief-writer's did.
- **What I read:** this brief whole; `docs/method/REVIEW.md` (rules, checklist, lifecycle);
  `docs/method/RECORD.md` lines 93–125; the three commits body-free through
  `tools/coldsweep.py --commit` (no message body read); `instruments/ccclose` whole at HEAD,
  `instruments/ccclose.test.js` helpers and the delta's tests, `instruments/ccclose.design.md`
  lines 340–425, `instruments/man/ccclose.1` lines 270–300, 309–400 and 475–495,
  `instruments/README.md` lines 384–400; `tools/board.py` lines 150–175, 218–250, 270–310,
  399–425; `.github/workflows/ci.yml` lines 108–132; `CHANGELOG.md` lines 1–22, 74–90 and its
  `ccclose` entries; `docs/method/CONCURRENCY.md` lines 944–952; `skills/review-brief/SKILL.md`
  lines 98–110. I did **not** open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`,
  any prior verdict, the two pointers or the two intent records.
- **The one live read:** `ccclose --identifiers --json` on the authoring session's transcript,
  read through the tool only; aggregate counts below, no text quoted. Its JSON was deleted from
  my scratch at the end of the pass.

### Lens 1 — approach and assumptions, mine first

My own load-bearing assumptions, named before the brief's list:

- **M1. A `git commit` string in a Bash tool_use is a commit the session made.** False in
  three ways the code does not distinguish: the command may have failed (IE2), run in another
  repo (IE3), or never run at all because the text is a heredoc body, a grep pattern or an
  echo (IE4). The regex reads text, not execution.
- **M2. Equal subject ⇒ same commit.** False whenever a peer in the window uses the same
  subject. This house's subjects are templated (`board: rebuild`, `board: claim …`,
  `records: session close`); the public repo's own history since 2026-09-01 has 806 commits,
  8 subjects used more than once, and 5 of those repeated within 8 hours of a prior use
  (IE1).
- **M3. Evidence that is absent is absent for a benign reason.** Not always: an unreadable
  subagent file (IE9) and a worker session's separate transcript (IE8) both leave commits
  unconfirmed with nothing on the Commits line saying why.
- **M4. The "left out" tier is a peer's work.** The reason line asserts it; three probed cases
  show it false (IE6).

**Is matching on command text the right evidence at all?** It is the right *kind* (positive
evidence from the session's own record) but the wrong *binding*. A session leaves stronger
evidence the tool already holds and does not use: each `git commit` tool_use has a timestamp,
its tool_result has a timestamp and an `is_error` flag, and the record carries a `cwd`. A
window commit whose committer time falls between the tool_use and its result, from a command
whose cwd (or `-C`) resolves into this repo, and whose result is not an error, is the
session's with near certainty; subject equality then disambiguates the rare collision rather
than carrying the whole claim. With `git commit -q` the result text is empty, but its
timestamp is not. Counsel, not applied.

### Ground truth, by table

Throwaway repos and synthetic transcripts under my scratchpad (`IE-probe.js`, deleted with
its worlds at the end of the pass); the worktree's `node instruments/ccclose` run read-only.
Truth is what I built; "printed" is the tier the block gave.

| scenario | truth rows | over-credit | under-credit |
|---|---|---|---|
| S1 two sessions, same subject on main, peer branch commit | 3 | 1 | 0 |
| S2 commit command failed (`is_error`), peer used the subject | 1 | 1 | 0 |
| S3 session committed the subject in another repo (cwd there) | 1 | 1 | 0 |
| S4 amend by `-m`, amend `--no-edit` | 2 | 0 | 0 |
| S5 rebase of the session's branch onto a peer's main commit | 3 | 0 | 0 |
| S6 cherry-pick, revert, default-message `--no-ff` merge | 6 | 0 | 3 |
| S8 multi-line first paragraph (git folds it into one subject) | 1 | 0 | 1 |
| S9 squash routes: peer-merged own PR, issue-number subjects, own no-number merge | 4 | 0 | 2 |
| S10 subagent's failed `gh pr merge 14` (+ parent control) | 2 | 1 | 0 |
| S11 board: confirmed claim, peer's unconfirmed close | board only | — | — |
| S12 heredoc body quoting a commit command, peer made the commit | 1 | 1 | 0 |
| S13 unreadable subagent transcript | 1 | 0 | 1 |
| S14 `-F` tier: Write, heredoc + `git -C`, printf, `/tmp` vs `/private/tmp` | 4 | 0 | 2 |
| S15 separately dispatched worker session (own transcript) | 2 | 0 | 1 |
| **totals** | **31** | **5** | **10** |

S7 (unit, `commitSubjectsIn`, 14 forms): 9 read correctly; 5 missed (`git -C "/path with
space"`, an alias, `-qmfoo`, `--file=-` heredoc, `--git-dir=`); 3 produced evidence from text
that runs no commit (a heredoc body, a grep pattern, an echo).

**Live re-drive** (aggregate only): window 2026-10-18 04:58–12:20 UTC; 34 credited (range
broken), 21 unconfirmed, 0 left out; board credited: 6 completed, 11 created, 0 claimed, 5
⏳; board unconfirmed: 4 completed, 12 created. Git's own count of window commits across
`--branches --remotes` is 55 = 34 + 21 + 0; the three tiers partition it with no overlap;
the one first-parent `(#N)` commit in the window is credited; the three delta commits are
credited; no two credited commits share a subject. Which of the 21 unconfirmed were the
session's, git cannot say and I did not read the transcript to find out.

### Assumptions A1–A8

- **A1 — damaged.** S1: a peer's same-subject commit two minutes later is credited, and the
  range `first^..last` then spans the peer's commit. §15.1's "a repeated subject cannot cross
  sessions in practice" is contradicted by this repo's history (5 repeats within 8 h since
  2026-09-01). IE1.
- **A2 — damaged, with the gaps undocumented.** S6/S8/S7: cherry-pick, revert, a default
  merge message, a folded multi-line subject, `--git-dir`, a `-C` path with a space, an alias
  and `-qmfoo` all leave no readable subject; §15.1 names only variables, files written other
  ways and script commits. IE10.
- **A3 — damaged.** S9: a direct commit whose subject ends `(#9)` is "left out" as a "squash
  merge of PR #9"; the session's own branch work, squash-merged by a peer who deleted the
  branch, is left out as repeating "someone else's" commits. IE6.
- **A4 — damaged.** S10: a subagent's failed `gh pr merge` confirms a peer's squash merge; the
  parent control leaves it out. IE5. And a session's own no-number merge (S9 #11) is left out
  with a reason that states the opposite of what happened. IE6.
- **A5 — damaged.** S11: a claim the session confirmed and a peer closed prints as "claimed
  (still open)" and as "unconfirmed: completed" at once. IE7.
- **A6 — holds live, latent gap.** The regex mirrors `STATE_RE` and code spans are stripped as
  `board.py` does; all 444 item files in this repo have the state line on line 1. But
  `board.py`'s `item_state` skips leading blank and `<!-- -->` lines and ccclose reads line 1
  only: probed, `board.py` read `[x]` and the ⏳ flag from line 2, ccclose read neither. IE13.
- **A7 — damaged.** S13: an unreadable subagent file drops its commits to unconfirmed with
  nothing on the Commits line; the agents line misdescribes the cause. IE9. S2/S10: a failed
  command is not silent in the transcript, but the tool does not read the failure.
- **A8 — partly false.** §15.1 says a failed merge counts for nothing (false for subagents,
  IE5); the README says *a peer's* squash merges are left out (the session's own can be, IE6);
  the "Not solved" list omits the S6/S8 forms (IE10). The man page, README and §15.1 agree
  with each other on what they do say.

### Lens 2 — correctness and quality

Diffed all three commits body-free. The window/evidence split, the `-F` tier's ordering rule
(latest earlier write wins; cross-transcript writes unordered and accepted), path resolution
against cwd and `git -C`, variable literals, appends skipped, the state-line ⏳ read and the
per-tier board reduce all behave as the comments say on the suite's cases and on mine (S4, S5,
S14 first two rows). Overclaims against the text that makes them: §15.1 "cannot cross sessions
in practice" (IE1); §15.1 "a failed command counting for nothing" (IE5); the rendered reason
"squash merge of PR #N, merge not run by this session" (IE6); the rendered "claimed (still
open)" (IE7). The `(#N)` heuristic and the "left out" tier are printed as fact with no
"heuristic" marker on the line, while the unconfirmed lines do carry "check before pasting".

### Lens 3 — completeness and harvest

Message forms: the house forms (`-m`, repeated `-m`, `--message=`, `-m "$(cat <<EOF`,
`-F - <<EOF`, `-F path` by Write or heredoc) are read. Not read: `--file=-`, `-qmfoo`, a
folded multi-line subject (S8), `--git-dir`, a `-C` path with spaces, aliases. Merge routes:
`gh pr merge <n>` is read; a no-number merge, a web-UI merge and a peer's merge of the
session's PR all land as "left out" (IE6). Worker sessions are not read at all (IE8). Surfaces
that document the block: §15.1, man page, README and `--help` are consistent with each other;
`RECORD.md` (not a delta path) still defines Commits as "every commit the session landed, its
workers' included", which the block cannot now meet for the queue-run pattern (IE8).
`CHANGELOG.md` records the 2026-10-18 identifiers block but not this change to what it credits
(IE12). No stamped copy exists; the README names the design note as the record.

### Lens 4 — security and privacy (V6)

Checked by hand against the OWASP catalogue. **A03 injection:** no transcript-supplied string
reaches a git argument: `attributeCommits`, `firstParentShas` and `boardLog` take refs and
paths from `repoFacts` and the board config; subjects and resolved `-F` paths are compared in
memory only. **Filesystem:** `resolvePath` output is matched against other resolved paths and
never opened; the only files read are the transcript, its `subagents/` directory and the
repo. **ReDoS:** every new regex (`GIT_MSG`, `LITERAL_ASSIGN`, `HEREDOC_AT`, `REDIRECT_OUT`,
`TEE_OUT`, the heredoc and variable patterns) has disjoint alternatives at each repetition
boundary (`\S+` against `\s+`, character classes that exclude the delimiter), so backtracking
is linear; `fileSubjects` is quadratic in writes × file commits per transcript, bounded by the
transcript. **What reaches the block from the transcript:** nothing new; subjects come from
git, PR numbers from git subjects, reasons are templated. **Fixtures:** a one-letter local
part on the reserved `.invalid` domain, assembled from a character code so no address string
sits in the source, name `T`, `example/demo.git`; no real identity. **`/security-review`:**
discharged — it reads the session's pending diff, which in this worktree is this brief and
the removed sibling, not the delta; the hand check above stands in for it.

### Standing checklist V1–V7

- **V1** — bites: IE1, IE5, IE6, IE7 (claims stronger than their evidence, two of them printed
  as fact into records).
- **V2** — re-run ledger below; every claim the brief listed reproduced except the design
  note's "cannot cross sessions in practice" (IE1) and "failed command counting for nothing"
  (IE5).
- **V3** — the block's definition lives in `RECORD.md`; the delta changed the block's meaning
  without a sweep there or in `CHANGELOG.md` (IE8, IE12). `CONCURRENCY.md` line 947 names the
  block generically and needs nothing.
- **V4** — discharged: §15.1 is named as the record by the README; the man page is the
  reference by convention for instruments; no second home states a different rule.
- **V5** — bites: §15.1 vs subagent merges (IE5); README "a peer's squash merges" vs code
  (IE6); the printed reason vs §15.1's own no-number cost (IE6).
- **V6** — lens 4 above; no finding.
- **V7** — provenance above and in the brief; the brief-writer's and the orchestrators'
  arrangements are disclosed at the top of both.

### Findings

**IE1 — MAJOR. Subject equality credits a concurrent session's same-subject commit as fact
(A1 false).** S1: the session committed `board: rebuild index` once; a peer committed the same
subject two minutes later on `main`; the block credited both and printed an unbroken range
spanning the peer's commit. §15.1 dismisses this ("a repeated subject cannot cross sessions in
practice because the window still bounds the candidates"), but the window is exactly where
concurrent sessions meet, and this repo's own history shows 5 subjects repeated within 8 h of
a prior use since 2026-09-01, four of them templated board hand-ups. The failure is the one
the brief names as worst: silent over-credit pasted into a record as fact.
*Counsel:* bind each confirmed commit to a specific commit command: committer time within the
command's tool_use→tool_result span (the record has both timestamps), cwd or `-C` resolving
into this repo, result not an error; at minimum, credit no more commits per subject than
matching commands, and demote the surplus to unconfirmed with "subject reused in the window".

**IE2 — MODERATE. A `git commit` command whose result is an error still counts as evidence
(A7).** S2: the session's only commit command failed ("nothing to commit", `is_error`); a peer's
commit with that subject was credited. The same file checks `is_error` for worktree adds and
PR merges through `pend`/`resolvePending`; commit subjects are added at command time and
never resolved. *Counsel:* route commit subjects through `pend` like merges, so a failed
command adds nothing.

**IE3 — MODERATE. Evidence is not scoped to this repo.** S3: a commit command run with cwd in
another repo (the record's `cwd`; a `git -C other` would do the same) confirmed a peer's
same-subject commit here. The block is per repo and its "Other repos" line says sessions write
to several; a session's own `board: rebuild` elsewhere is routine. *Counsel:* keep a command's
subject only when its `-C` or cwd resolves under `repo.root` (or a linked worktree of it).

**IE4 — MODERATE. Command text that runs no commit is evidence.** `GIT_MSG` matches anywhere
in the command string. S12: a `cat > notes.md <<'EOF'` body quoting `git commit -q -m "docs:
example subject"` credited a peer's commit of that subject; S7: a grep pattern and an echo
string yield subjects too. *Counsel:* skip heredoc bodies and quoted strings that are not the
`-m` argument of a `git commit` in command position (after a line start, `;`, `&&`, `||`, `|`
or `(`), the way `GH_PR` already anchors `gh pr`.

**IE5 — MODERATE. A subagent's failed `gh pr merge` confirms a peer's squash merge (A4; V5).**
S10: the subagent's `gh pr merge 14 --squash` returned an error; the peer's `Peer work (#14)`
was credited "merge run"; the parent control with the same failed command left it out. §15.1
says "a failed command counting for nothing"; `commitEvidence` reads subagent merges straight
from `ghPrCommands` with no result check. *Counsel:* apply the parent's pend/resolve path to
subagent transcripts, or say in §15.1 that subagent merges are not result-checked.

**IE6 — MODERATE. The "left out" reason is printed as fact and is false in three probed cases
(A3, A4; V1).** The line reads `(PR #N squash merge, merge not run by this session)`. S9: (#7)
the session's own branch work, squash-merged by a peer who deleted the branch — the content is
the session's, the branch commits are unreachable, and the session's whole contribution now
appears nowhere credited; (#9) a direct commit whose subject names an issue is not a squash
merge at all; (#11) the session ran the merge itself (no number, a cost §15.1 acknowledges)
and the block says it did not. The README's "a peer's squash merges as left out" assumes the
same. *Counsel:* print the tier as the heuristic it is ("on the first-parent line with a PR
number; this session ran no numbered merge for it") and, before leaving one out, check whether
its subject minus the `(#N)` suffix is one of the session's own subjects — the house's squash
title is usually the PR's first commit — and credit it "via squash of own PR".

**IE7 — MODERATE. "claimed (still open)" is judged over confirmed commits only, so a claim a
peer closed prints as open (A5).** S11: the session claimed `010/010`, the orchestrator closed
it in a commit this session did not make; the block prints "claimed (still open): 010/010"
and "unconfirmed, from window-only commits: completed 010/010" — the same item on two lines,
and the first is false (the file is `[x]` at the end of the window). The pre-delta window read
got this case right. The worker-claims, orchestrator-closes pattern is this house's queue-run
shape. *Counsel:* compute "still claimed at the end" over the whole window's final state
(`both`), and list a confirmed claim whose release or close is unconfirmed as "claimed; closed
by an unconfirmed commit".

**IE8 — MODERATE. Separately dispatched worker sessions are structurally unconfirmed, and no
doc says so.** `RECORD.md` lines 101–102 define Commits as "every commit the session landed,
its workers' included". The evidence is read from the parent transcript and its `subagents/`
directory only; a worker dispatched as its own headless session has its own transcript in the
same store. S15: the worker's commit prints unconfirmed. Every orchestrator's block under the
queue-run pattern will list its workers' commits as "check before pasting", with no way to
confirm them, and §15.1, the man page and the README do not mention worker sessions.
*Counsel:* either read the transcripts the parent launched (a `claude -p … --session-id` or
`--resume` command, or an `Agent` tool_use, names them) as further evidence transcripts, or
state the limit in §15.1 and `RECORD.md` so the reader knows the unconfirmed line is expected
there.

**IE9 — minor. Evidence shrinkage is silent on the Commits line (A7).** S13: a subagent
transcript that cannot be read (`EISDIR`; a permissions error would do the same) is swallowed
by `catch {}` in `commitEvidence`; its commit prints unconfirmed, and the agents line says
"stops short of end_turn", which is not the cause. *Counsel:* count unreadable evidence files
and print "evidence incomplete: N subagent transcript(s) unreadable" beside the unconfirmed
line.

**IE10 — minor. Under-credit forms the docs do not name (A2, A8).** S6: cherry-pick, revert and
a default-message `--no-ff` merge made by the session are unconfirmed; S8: a `-m` message whose
first paragraph spans two lines is folded by git into one subject (`%s`) while the reader keeps
the first line only; S7: `--git-dir=`, `git -C "/path with space"`, aliases, `-qmfoo`,
`--file=-`. Each errs towards under-credit, which the design accepts, but §15.1's "Not solved"
list names none of them, so a reader cannot predict the unconfirmed line. *Counsel:* add them
to "Not solved"; fold the first paragraph as git does (join lines up to the first blank).

**IE11 — minor. No test has a peer commit with an identical or near-identical subject.** The
prefix mutant (match on the first 8 characters) kills 2 of 65 tests and survives "a peer's
commits in the window are unconfirmed", whose subjects differ from the first character. The
"credit everything" mutant kills 7. *Counsel:* add S1's shape to the suite: a peer commit whose
subject equals the session's, expected unconfirmed, range broken.

**IE12 — minor. `CHANGELOG.md` entry owed.** The log records the identifiers block (2026-10-18)
and `ccclose` itself (2026-10-16); the change to what the Commits and Board lines credit, and
the two new sub-lines a reader will meet in every block, have no entry. No commit in
`0462173^..e78b6f1` touched the file for this change.

**IE13 — note. ccclose reads the item's line 1; `board.py` reads the first non-blank,
non-comment line (A6).** Probed: an item whose line 1 is an allow-marker comment and whose
state line is line 2 — `board.py` read `[x]` and the ⏳ flag; ccclose read neither (created
only). No live file in this repo has that shape today (444 of 444 start on the state line),
so this is latent, and the code comment's "board.py's own grammar" is true of the regex, not
of where the line is looked for.

**Notes against out-of-delta surfaces** (for the `160/920` reconcile, not findings here):
commits are windowed on committer time across `--branches --remotes`, so a commit in a
detached-HEAD worktree is invisible to every tier; the window's `--since` slack and `%ct`
filter behave as commented. Nothing in the delta changes them.

### Re-run ledger

All from the worktree root at `947d86f`, foreground, `nice -n 10` for the suites; load averages
8–14 throughout, one heavy process at a time.

| command | result |
|---|---|
| `python3 tools/coldsweep.py --root . --commit 0462173` / `621d18b` / `e78b6f1` | exit 0 each; 604 / 209 / 455 lines; "message body not read" |
| `git log --oneline e78b6f1..HEAD -- <five paths>` | empty |
| `nice -n 10 node --test instruments/ccclose.test.js` | exit 0 · 65 pass · 0 fail · 104.6 s |
| `nice -n 10 node --test instruments/*.test.js` (CI form) | exit 0 · 492 pass · 0 fail |
| mutant A, credit every window commit, same suite on a scratch copy | exit 1 · 58 pass · 7 fail |
| mutant B, 8-char prefix match, same suite on a scratch copy | exit 1 · 63 pass · 2 fail |
| `mandoc -T lint -W style instruments/man/ccclose.1` | exit 0, no output |
| `mandoc -T lint instruments/man/ccclose.1` (CI form) | exit 0, no output |
| `awk 'length > 80' instruments/man/ccclose.1` | one line, 418 (143 bytes); blame `4eda680`, 2026-10-17, not this delta |
| `python3 tools/wrapscan.py --root . <five paths>` | exit 1, 6 findings (README 338, 454; design 83, 97, 220, 267); blame `cea247e`, `dcdf40b`, `4142efb`, `cea247e`, `4eda680`, `a738f85` — none this delta; `instruments/` is outside the floor's wrapscan path |
| `python3 tools/spellscan.py --root . <five paths>` | exit 0, clean |
| `python3 tools/leakscan.py --require-terms --root . <five paths>` | exit 0, clean |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | exit 0, every enforced check green |
| `node instruments/ccclose --help` | exit 0; lists `--identifiers` |
| live re-drive, `--identifiers --json --session <store path> --root .` | exit 0; counts in *Ground truth* above |
| ground-truth harness, 14 scenarios + 14 unit forms | 31 rows · 5 over · 10 under (table above) |
| A6 probe, comment on line 1 | `board.py` reads the state; ccclose does not |
| item files' line 1 vs `STATE_RE`, this repo, barred four excluded | 444 read, 0 not a state line |
| repeated subjects, this repo, `--all --since=2026-09-01` | 806 commits, 8 repeated subjects, 5 within 8 h |

### Follow-up checklist (for the principal; nothing applied)

- [ ] IE1–IE4: decide whether the commit tier binds to command execution (time, cwd, result)
      or stays subject-only with its limits written into §15.1 and the block's attribution line.
- [ ] IE5: result-check subagent merges, or document that they are not.
- [ ] IE6: reword the "left out" line as a heuristic; consider the own-PR squash check.
- [ ] IE7: judge "still open" over the whole window's final state.
- [ ] IE8: worker sessions — read them as evidence, or say in `RECORD.md` and §15.1 that the
      block cannot confirm them.
- [ ] IE9–IE13: the minor items and the note, as one follow-ups item if taken.
- [ ] Phase 2: reconcile against the sibling, the two intent records, the three commit bodies
      and `160/920`'s verdict (orchestrator releases them).

### Reconcile — phase 2, 2026-11-01 UTC

Opened after act 1 was committed (`9a13262`): the sibling (released by the orchestrator from
its held copy; 16 seeded questions, 9 held re-run results, two intent-record summaries), the two
intent records `210/290` and `210/310` whole, the three commit message bodies (plain `git show
-s --format=%B`), the `160/920` verdict (`docs/reviews/2026-10-18-0506-close-covers-subagents-
cold.md`, lines 455–543, 642–661 and 795–895) and both pointers. Phase-1 text above is
unrevised. Four further probes ran under my scratchpad for questions 4, 5, 8 and 12 and were
deleted with their worlds.

**The sibling's re-run results against mine.** All nine reproduce: coldsweep exit 0 ×3; 65/65;
492/492 (the authors' 489 at `e78b6f1` differs by one later commit to another instrument's test
file, `5139d68`, outside this delta — now checked, not assumed); mandoc both forms exit 0 and the
same one 143-byte line blamed outside the delta; the same six wrapscan lines, all outside the
delta; spellscan and leakscan exit 0; the empty later-commit list; floor exit 0; `--help` exit 0;
and the live re-drive by path gives the same counts to the unit (34 / 21 / 0; board 6, 11, 0, 5;
unconfirmed 4, 12; 7 agents reported). I did not run the id-prefix form the brief-writer found
wanting (result 9, "no transcript found" from a worktree root): `locateTranscript` predates this
delta, so it is out of scope here, but it decides whether a session following `RECORD.md` from a
worktree gets any block at all, and no finding of mine or `160/920`'s names it — carried to the
follow-ups as a question for the `160/920` or a `210/` item, not charged here.

**The seeded questions, one by one.**

1. Yes and yes: IE1 (S1). Two commits with one subject are both credited and the range spans
   the peer's.
2. Yes: IE2 (S2), and it is an over-credit path only in combination with 1 or 3.
3. Yes for a heredoc body, a grep pattern and an echo: IE4 (S7, S12). A commit message's own
   text is not scanned (subjects come from git), so that half is clean.
4. The first-paragraph fold: yes, under-credit, IE10 (S8). Probed now in addition: leading
   whitespace is fine (git strips, `normSubject` trims); a `#` first line given by `-m` is kept
   by git and read the same way, so it matches; `$'…'` quoting is not understood by `shellWords`
   and yields a subject with a leading `$` that no commit carries — one more under-credit form
   for IE10's list.
5. Probed now: with the pre-rebase copy still on a ref, both copies are credited (`Commits (4)`
   for two pieces of work, no range). Every one of the four SHAs is the session's, so this is
   not an over-credit of a peer; it is a count a reader may misread. Note, not a finding.
6. Yes: IE6 (S9 #7, #11). `--auto` completing later and `gh api` were not driven; they take the
   same path as the web UI (no `gh pr merge <n>` command), so the reason line reads as fact for
   them too.
7. Yes: IE6 (S9 #9) — and the brief-writer's framing is the sharper one: it is an under-credit
   hidden behind a stated reason, because "left out" is terminal where "unconfirmed" invites a
   check.
8. Probed now and yes: an item created on the session's branch, squash-merged by a peer who
   deleted the branch, appears on no board line at all — not created, not unconfirmed — with
   only the commit tier's "left out" entry as a trace. IE14 below, formed at reconcile.
9. Yes: IE8 (S15), and the doctrine's queue-run shape does make it the common case.
10. Yes: IE7 (S11), exactly as suspected.
11. The regex and the code-span strip match `board.py`'s (A6 holds there); the where-to-look
    differs (IE13). A re-queued ⏳ (flag on both old and new first line) is not counted, by the
    design's own "gained" rule; agreed, no finding.
12. Probed now: a Write, then an Edit tool change to the file's first line, then `-F` leaves the
    stale draft as the evidence and the real commit unconfirmed. The design's "Not solved" names
    `sed -i` but not the Edit tool, which is this house's usual editor — added to IE10.
13. Yes: IE9 (S13).
14. Both discharged in lens 4: the nested quantifier's alternatives are disjoint at each boundary
    (linear); the resolved path is compared, never opened.
15. The three docs agree with each other on what they state; the README's "the squash merge of a
    PR the session merged" omits the first-parent condition the man page and §15.1 state, and
    "a peer's squash merges as left out" is the assumption IE6 falsifies. V5 as recorded.
16. Pre-delta; carried as a question above, not charged.

**Against the authors' accounts.** `210/290`'s close note is faithful to what was built: first-
parent rejected as the rule and kept to recognise squash merges, positive evidence taken, the
window demoted. Its probe on its own session (10 credited, 9 unconfirmed: the peer's 8 and one of
its own committed by a worker with `-F`) is the honest shape and already shows IE8's class — a
worker's commit the orchestrator could not confirm — which `210/310` then narrowed to the `-F`
form and fixed for subagents only. `210/310`'s "this errs the safe way: nothing is
over-credited" is true of the `-F` gap it describes; phase 1 shows the subject tier beneath it
does not err the safe way (IE1–IE4). The record's "shapes to weigh" named "resolve a literal
`-F <path>`", "say so on the unconfirmed line" and "prefer `-F -` with a heredoc"; the first was
built, the second is the attribution-line sentence, the third is doctrine not taken. Neither
record considers binding evidence to the command's time, cwd or result, which is where my
counsel sits. The 290 note's "the session's own SHAs cannot come from its transcript when it
commits with `-q`" is true and is the premise the whole design rests on; the timestamps can.

**Against the commit bodies.** `0462173`'s body matches §15.1 and the code; its "as board.py
reads it" is true of the regex and not of the line looked for (IE13). `621d18b`'s body says the
man page and README were brought "into line with the three commit tiers"; they were, and they
inherited the overclaims (IE6's "a peer's", IE5's "failed command"). `e78b6f1`'s body states the
same limits as §15.1, names the one-line `S=… && cat > $S/m` fix with its test, and says "the
JSON field set is unchanged" — relative to `0462173`, which had already changed it; no
contradiction with phase 1. None of the three bodies mentions worker sessions, failed commit
commands, repo scoping or quoted text.

**Against `160/920` (CV1–CV19; CL1–CL24 through it).**

- *Which of mine it already holds:* none as a finding. Its CL18 line ("test gaps by mutation —
  the pattern continues") is the class IE11 adds one more member to. Its CV15 (a `[x]` → `[x]`
  first-line rewrite guard unprotected) is a board test gap beside IE7's board defect; S11 did
  not drive CV15's shape, so it stands untested by me.
- *Which of its this delta bears on:* **CV19 / CL1** (the `--since` walk truncates, MAJOR under
  `160/870`, undecided). This delta adds a third `--since` walk, `firstParentShas`, beside
  `windowCommits` and `boardLog`. A first-parent walk is linear, so it truncates only when a
  back-dated commit sits on the first-parent line inside the window — rarer than CL1's case but
  the same mechanism, and a truncated first-parent set would move a squash merge from "left
  out" to "unconfirmed" silently. On the live window there is no truncation to see: the
  `--branches --remotes` count is 55 with and without `--since`, and origin/main's first-parent
  count is 236 both ways. Not charged here: the root is open at MAJOR and `160/920` already
  charged the identifiers form once; recorded so the fix to CL1 is swept to all three call
  sites.
- CV2 (descriptions pasted), CV3 (`gh` timeout read as absence), CV12 (`0 · none launched` for
  two facts) sit in the block's other fields; not this delta's hunks, unchanged, no overlap.
- `160/920`'s reconcile notes that at HEAD its CL1 throwaway repo printed `(0): none` because
  this delta "now credits commits only on transcript evidence" and left that unassessed; phase
  1 assesses it (IE1–IE4, IE10).

**Findings formed at reconcile (marked as such).**

**IE14 — minor (formed at reconcile; seeded question 8). Board movement that reaches the
integration branch only through a left-out squash merge is dropped from the block entirely.**
Probed: an item file added on the session's branch, squash-merged by a peer who deleted the
branch; the block prints `created: none` and `unconfirmed … : none`, and the only trace is the
commit tier's "left out" entry, whose reason (IE6) says the work is someone else's. §15.1 says a
left-out squash "contributes to neither" by design, written for the case where the peer's branch
commits are still on a ref; when they are not, the movement is gone with no line saying so.
*Counsel:* when a left-out squash merge is the only reachable carrier of a board diff, list that
movement on the unconfirmed board line with "via a squash merge this session did not run".

**IE10 widened (not re-charged):** `$'…'`-quoted messages (question 4) and a Write followed by an
Edit tool change before `-F` (question 12) join the under-credit forms §15.1 does not name.

**Note (reconcile; question 5):** a rebase whose pre-rebase copy survives on a ref credits both
copies; all are the session's, so no over-credit, but the count doubles. Worth a sentence in
§15.1 beside the amend case.

### Overall, restated

**PASS-WITH-FINDINGS — 14 findings: 1 MAJOR (IE1) · 7 MODERATE (IE2–IE8) · 5 minor (IE9–IE12,
IE14) · 1 note (IE13).** Changes from act 1, all stated above: IE14 new; IE10 widened at the
same severity; no phase-1 finding contradicted by the sibling, the authors' accounts, the commit
bodies or `160/920`. Every finding is on a tool whose output is pasted into records as fact, so
all are the principal's to decide (rule 3); counsel sits beneath each and nothing was applied.

**Follow-up checklist, act 2 additions**

- [ ] IE14: a left-out squash's board movement on the unconfirmed line.
- [ ] CL1/CV19 sweep: when the `--since` walk is fixed, fix `firstParentShas` with
      `windowCommits` and `boardLog`.
- [ ] Question 16 (pre-delta): does `--session <id>` find the transcript from a worktree root?
      For the `160/920` follow-ups or a `210/` item.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-01)

*Released to the reviewer only after its act-1 findings were committed; folded here
verbatim (headings demoted two levels to sit under this one) and the sibling file removed,
per the brief. The orchestrator (session `0d67673f`, Claude Opus 5.5, started by session
`c87c4ee0`) formed no finding and wrote no severity.*

### Sibling to the identifiers credit-on-evidence cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-26-0917-identifiers-credit-on-evidence-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-26 UTC by the Opus 5.5 brief-writer named in the brief's
provenance; it forms no finding and writes no severity. Fold this file in below the reconcile
and delete it at phase 2.

#### Intent records

Both read in full by the brief-writer. Neither quotes the principal.

- `docs/roadmap/210-instruments-open-features/290-ccclose-identifiers-over-credits-overlapping-sessions.md`
  — lines 2–16: the problem as found by the session that shipped the identifiers block (counts
  from its first real block against its own commits, a concurrent cloud session's branch
  commits and squash merge, a board item wrongly credited, a `⏳` read from a close note), and
  the shapes to weigh. Lines 17–31: the authors' closing account (what was built, one shape
  weighed differently and why first-parent was rejected, the probe on its own session with
  counts, the test count, the residue filed as `210/310`).
- `docs/roadmap/210-instruments-open-features/310-ccclose-cannot-read-a-commit-message-from-a-file.md`
  — lines 2–15: the `-F <path>` gap, said to err the safe way, with shapes to weigh. Lines
  16–27: the closing account (the write-matching rule, path equality, the `$VAR` rule, latest
  write wins, the stated limits, one commit moved by the probe, test counts).
- The three commit bodies — not read by the brief-writer.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-10-26, from its worktree root at `2f6dbf6`, in the
foreground, on this machine (12 cores, load near 7 at the time):

1. `coldsweep --commit` on each of the three commits: exit 0 each, closing "message body not
   read" line present, 0 barred files touched.
2. `node --test instruments/ccclose.test.js`: exit 0, 65 tests, 65 pass.
3. `node --test instruments/*.test.js`: exit 0, 492 tests, 492 pass. (The `210/310` record
   gives 489 at `e78b6f1`; later instruments commits outside this delta may account for the
   difference. Not checked.)
4. `mandoc -T lint -W style instruments/man/ccclose.1`: exit 0, no output. The CI form at
   default level: exit 0. `awk 'length > 80'` prints one line (line 418, 143 bytes, inside a
   `.nf` example block); `git log -L418,418` names `4eda680` as its last change, outside the
   delta.
5. wrapscan over the five paths: exit 1, 6 findings (2 in `instruments/README.md`, 4 in
   `instruments/ccclose.design.md`); `git blame` puts all 6 on commits outside the delta.
   spellscan: exit 0. leakscan `--require-terms`: exit 0, local term list present.
6. `git log --oneline e78b6f1..HEAD -- <five paths>`: empty.
7. Floor, ci plane: exit 0 (secretscan 23 advisories, leakscan cover not guaranteed on this
   plane, four warn-only scanners), as designed.
8. `ccclose --help`: exit 0.
9. Live re-drive on the authoring session's transcript, counts only:
   - by id prefix (`--session 8e498ef1`) from the worktree root: exit 0, but "no transcript
     found", so every field fell to "by hand";
   - by the transcript's path: exit 0. Commits confirmed 34 (not unbroken), unconfirmed 21,
     left out 0. Board, confirmed: completed 6, created 11, claimed 0, `⏳` review 5.
     Board, unconfirmed only: completed 4, created 12. Agents 7, all reported.
   The authoring session's window covers its whole queue run, not only this delta's work.
   The brief-writer derived no ground truth and forms no view on these counts.

#### Prior verdicts on nearby surfaces (named by filename, not opened, not exhaustive)

- `docs/reviews/2026-10-18-0506-close-covers-subagents-cold.md` — `160/920`, the earlier
  commits to the same files.
- `docs/reviews/2026-10-17-1010-ccclose-close-checker-cold.md` — named in a shape example; the
  name suggests the original close checker.

#### The pointer's own lens hints

It names the worst failure (a block pasted as fact) and the boundary against `160/920`.
Nothing else.

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. Subject equality is the whole key. House subjects recur (`board: …`, `docs: session
   record …`). Does a peer's commit with a subject the session also used get credited, and
   are two commits with one subject both credited?
2. A commit command that made no commit (hook refusal, nothing to commit) still adds its
   subject to the evidence. Combined with question 1, is that an over-credit path?
3. The command regex scans the whole command string. Does `git commit -m "x"` inside an
   `echo`, a heredoc being written to a file, a `grep` pattern or a commit message's own text
   yield evidence?
4. Git's `%s` is the first *paragraph* joined with spaces, while the tool takes the first
   *line* of the message. A message whose first paragraph spans two lines would then never
   match: an under-credit the "errs the safe way" framing does not cover. Same question for
   leading whitespace, comment cleanup, `$'…'` quoting and escaped quotes.
5. Rebased or cherry-picked copies carry the same subject. With a pre-rebase branch still in
   `--branches --remotes`, are both copies credited?
6. Merge routes other than `gh pr merge` (`gh pr merge --auto` completing later, `gh api`, the
   web UI, a separate worker session): are their squash merges left out with a reason line
   that reads as fact ("merge not run by this session")?
7. A session commit whose subject ends `(#n)` for another reason, on the first-parent line and
   without readable evidence, is "left out" as a squash merge rather than "unconfirmed". Is
   that an under-credit hidden behind a stated reason?
8. A left-out squash merge counts for nothing on the board, even on the unconfirmed line. If
   the peer's branch commits are gone from all refs, is that board movement dropped from the
   block entirely, with no line saying so?
9. `RECORD.md` asks for commits "its workers' included". Workers dispatched as separate
   sessions, not subagents, leave no subagents-directory evidence. Do their commits fall to
   unconfirmed, and does the doctrine's queue-run shape make that the common case?
10. The confirmed-only board reduce computes the final state from confirmed commits only. An
    item the session claimed and a peer then closed would read as "claimed and left open".
11. The `⏳` reading: `STATE_LINE` and code-span stripping against `tools/board.py`'s
    `STATE_RE` and `CODE_SPAN_RE`, and a re-queued `⏳` (flag on both old and new first line)
    not counted.
12. The file tier ignores Edit-tool changes and `sed` rewrites after the last Write, and the
    "parent's unordered use" of a subagent's file credits regardless of time order.
13. Silent paths: the subagent reader's `catch {}` and skipped unparseable lines shrink the
    evidence with no note in the block.
14. Security: whether `GIT_MSG`'s nested quantifier can be driven to long backtracking by a
    crafted command, and whether a path the file tier resolves from a transcript (it expands
    `$VAR` from literal assignments) is ever used to read from disk.
15. The README says a squash merge counts when "the session merged" it; the code also requires
    the first-parent line and treats a true `Merge pull request #n` commit the same way. Do the
    three docs agree with each other and with the code on that?
16. The id-prefix lookup found no transcript from a worktree root (result 9). Pre-delta
    behaviour, probably, but it decides whether a session following `RECORD.md` from a
    worktree gets any block at all.
