# Cold pass — `ccclose --identifiers` credits commits on evidence, not the window

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass. The principal's current standing ruling is that no Fable work runs
without his explicit permission, so this pass waits for that permission as well as for a
reviewer.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-26 UTC by an Opus 5.5
brief-writer subagent of session 5070f22b; the pass waits for a cold Fable session that neither
the delta's authors nor session 5070f22b (nor any of its subagents) started or instructed.
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
