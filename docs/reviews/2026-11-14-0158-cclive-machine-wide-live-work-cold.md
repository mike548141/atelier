# Cold pass — `cclive`, a machine-wide view of live work

**Board:** `docs/roadmap/160-doctrine-review-owed/1290-rule-4-cold-pass-queued-cclive-instrument.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `c4d93896`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

**Pass type:** code cold pass, first of its kind, per `docs/method/REVIEW.md` rule 4: the first
instrument that looks across every repo on the machine at live work.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** medium: three commits, about 1,400 added lines, of which 730 are the tool,
440 its tests, 171 its design note and 187 its man page; a two-line export change to `ccclose`;
index and doctrine lines in three markdown files.
**Why it earns a review:** every session in this repo now runs `cclive` at open (`CLAUDE.md` read
order step 1, `CONCURRENCY.md`), and its output decides whether a session takes a worktree, waits,
or treats a repo as idle enough for a record-store split. It is a silent-failure surface. The worst
failure is a view that reads as "nothing is happening" when a session is live: a repo filed under
the *quiet* line, a session credited to the wrong repo, or a claim marked `quiet` that is held. The
second worst is a viewer that is not read-only on some path: it runs against every repo on the
machine while other sessions are mid-commit.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `c4d93896`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be owed
  (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable review is
  required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the brief-writer
  forms no finding and writes no severity**, and stops after writing. It ran no review and used no
  Fable model.
- **Barred from running this pass:** session `c4d93896` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **the intent record
  `360/020` whole**, including the author's landing note and the later session-open note under it;
  **the message body of `6890e9db`** (met through `git show --stat`, before the body-free read);
  the delta through `tools/coldsweep.py --commit`; `instruments/cclive`, the design note and the
  test names at HEAD; ccclose's export lines; commit subjects through `git log`; the queue pointer
  for `160/1020`, the brief `2026-11-09-0126-ccclose-board-order-cold.md` and the head of its
  sibling, and the head of the unrun brief for `160/1250` (read for house form). It opened **no
  prior verdict** and no session record. Its harness also loaded user-level and repo instruction
  files and a memory index, which hold private context this brief does not carry. Everything
  evaluative it formed is in the sibling.

## The acceptance test

The principal's words that started it, in the design note's § 2 and the intent record's title
line: he asked, 2026-09-12, for ways *"to improve how parallel sessions to converse, coordinate,
share"* and *"to track, claim, and coordinate work planned and in progress"*. Offered mechanisms on
2026-11-09, he answered *"Build a machine-wide view"*: an answer to options offered, not a ruling.
No ruling of his fixes the design. Judge the work against the question the design note puts in § 1
(*what is any session, anywhere on this machine, doing, holding or claimed on right now?*) and
against its own claims below; whether that is the right question is yours to attack.

## What the work is

Three commits on `main`. First confirm your tree has them:

```
for c in 2c6df437 6890e9db 6197df86; do git merge-base --is-ancestor $c HEAD || echo "MISSING $c"; done
```

Nothing may print. If something does, merge `origin/main` into the review branch before starting,
because a tree without the delta has nothing to review. Read each commit body-free:

```
python3 tools/coldsweep.py --root . --commit 2c6df437 --path instruments/cclive.design.md
python3 tools/coldsweep.py --root . --commit 6890e9db \
  --path instruments/cclive --path instruments/cclive.test.js \
  --path instruments/cclive.design.md --path instruments/man/cclive.1 --path instruments/ccclose
python3 tools/coldsweep.py --root . --commit 6197df86 \
  --path instruments/README.md --path docs/method/CONCURRENCY.md --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic
(rule 1). Always pass `--path`: the board commits that closed `360/020` and queued this pass are
barred until phase 2. Review each delta path at HEAD too. On 2026-11-14 UTC no commit after
`6890e9db` had touched `instruments/cclive`, its test file or its man page. Confirm what has landed
since, and read anything new the same way:

```
git log --oneline 6197df86..HEAD -- instruments/cclive instruments/cclive.test.js \
  instruments/cclive.design.md instruments/man/cclive.1
```

`ccclose` is touched only by the export line; read the rest of it only as far as `cclive` depends
on it (`board()`, `CLAIM_LINE`, `FRESH_MS`).

## What the delta claims (extracted, not evaluated)

- **Read-only on every path.** It never fetches, commits or writes and uses no network; git runs
  with `--no-optional-locks`; transcripts are read a bounded tail at a time and only when fresh.
- **No new shared state.** Every source it reads is written for another reason; it asks no session
  to do anything new.
- **A blank cannot read as nothing.** It prints the roots it scanned, what it skipped and why, known
  zeros, unknowns as `?` with a reason, and three limits on every run. A repo with no board reports
  claims as unknown, never zero.
- **Claims at the newest integration ref**, the newest of `main`, `master`, `origin/main` and
  `origin/master` by committer date, not the working tree.
- **What counts as a claim:** a left-margin `[~]` line, or an indented one carrying a `claimed
  <date>` stamp found anywhere in the item's first paragraph by `board.py`'s paragraph rule; a
  released stamp dates nothing; an indented `[~]` with no stamp is a progress mark, not a claim.
- **Sessions matched by their own `cwd`**, longest-prefix against every worktree of every scanned
  repo, realpath on both sides; a subagent by its own `cwd`; a `cwd` under no repo goes to
  *elsewhere*, never dropped.
- **`live` is a positive match only** (a claim's session id or worktree name matches something
  live); `quiet` means only that no match was found.
- **`FRESH_MS` and the board adapter are shared with `ccclose`, not copied**, so the two tools
  cannot disagree.
- **The agent walk is bounded**: a session's `subagents/` is listed only when its parent was
  written in the last 24 hours, grounded in a census the design note reports.
- **Stable fields**: every repo prints the same fields in the same order; `--json` carries every
  field on every repo.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour on this machine. The lenses organise it; they do not bound it. Anything not named a
non-goal is in scope.

**Non-goals:** the rest of `ccclose` beyond what `cclive` imports; the 2026-11-12 decision that
every session runs `cclive` at open (an answer of the principal's, landed in later commits). Its
*consequence* is in scope: it is why a wrong quiet line costs what it does.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, then attack at least
   these by probe:
   - **A1.** Transcript mtime within ten minutes is a sound test for "a session is live", and its
     last recorded `cwd` is where it is working.
   - **A2.** The newest of four refs by committer date is where every live claim has landed.
   - **A3.** A claim's session id and worktree name, matched by first 8-hex token and by basename,
     identify the right session and the right worktree.
   - **A4.** Matching by longest path prefix never credits a session to the wrong repo.
   - **A5.** No path through the tool writes: not git, not the transcript store, not `ccclose`'s
     module load.
   - **A6.** The *quiet* line, and its footnote, say only what is true of the repos on it.
   Ask too whether this is the right problem at the right altitude, against what the design note
   rejected (an index, widening the channel, process inspection).
2. **Correctness & quality.** Diff each commit; drive the tool live and against scratch repos and a
   scratch transcript store you build. Record each overclaim against the text that makes it: the
   design note, the code's header comment, the help text, the man page, the README row, the
   `CHANGELOG.md` entry and the `CONCURRENCY.md` sentence.
3. **Completeness / harvest.** Every surface that states the same fact (V3), one home (V4), no
   contradiction between the design note, the man page and the code (V5). Tests that would stay
   green on a broken change: mutate the code in a scratch copy, never the worktree.
4. **Security & privacy** — mandatory. The tool reads other sessions' transcripts and prints parts
   of them, prints directory and branch names it did not choose, and spawns git against every repo
   under the roots. Check terminal-control and bidi sanitising on every printed field, not only
   transcript text; argument injection into git; what `--json` exposes; and what a hostile
   directory name or board line can make it print or run. Weigh against OWASP ASVS input-handling
   and output-encoding items, checked, not recalled. `/security-review` reads the session's pending
   diff, not this delta: aim it only at a scratch clone holding the delta as pending changes, or
   discharge it by grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-14 UTC, from the worktree
root, in the foreground, under a load average near 14 on 12 cores; its results are held in the
sibling. Read exit codes explicitly. Node is v24.18.0 and `python3` on `PATH` is 3.14.6 on this
machine.

- `node --test instruments/cclive.test.js`
- `nice node --test instruments/ccclose.test.js` (two and a half minutes under that load)
- `mandoc -T lint -W style instruments/man/cclive.1`
- `instruments/cclive; echo $?` and `instruments/cclive --json > <scratch>/v.json; echo $?`
- `instruments/cclive --root /nonexistent-dir; echo $?` and `instruments/cclive --fresh 0; echo $?`

Run the tool from your worktree, never by bare name from `PATH`: the installed `cclive` is a
symlink into another checkout.

## House rules for this run

**Live systems:** read-only. `cclive` itself reads every repo under the estate parent and the
machine's transcript store; running it is in scope and is a read. Any probe that would write to a
real repo, a real transcript or a real board is **NOT RUN**: build the case in your scratchpad
(scratch repos, a scratch `--root`, a scratch `HOME` for the transcript store) and say which
probes you could not build.

- Never print a secret, and quote no transcript text, private repo name, host, client or private
  path. This repo is PUBLIC; a repo seen in `cclive`'s live output is referred to by type only, and
  transcript titles are summarised, never quoted.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions are live on this machine: touch nothing outside your worktree and scratchpad, and delete
  your scratch repos and fixtures when you finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/` or
  `instruments/`.
- One heavy process at a time, foreground, long timeout, `uptime` first.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Skip the session-log step of the repo's read order: `docs/SESSIONS.md` is barred (below).
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
`docs/reviews/2026-11-14-0158-cclive-machine-wide-live-work-cold.deferred.md`, every delta commit's
message body, and the intent record
`docs/roadmap/360-concurrency-beyond-the-repo-mike-commissioned/020-parallel-sessions-across-different-repos-have-no-shared-view.md`
beyond its first bullet (the principal's 2026-09-12 words).

The delta's own text carries the author's account of why (the design note above all); it is the
delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1290-rule-4-cold-pass-queued-cclive-instrument.md \
  --also-exclude docs/roadmap/360-concurrency-beyond-the-repo-mike-commissioned/020-parallel-sessions-across-different-repos-have-no-shared-view.md \
  --also-exclude docs/reviews/2026-11-14-0158-cclive-machine-wide-live-work-cold.deferred.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, the
assumptions A1–A6 and your own, and the re-run list. Append your verdict below a `---` divider in
THIS file: provenance repeated (how you were spawned, your tier, what you read, the UTC day you ran
on), per-lens answers, the standing checklist V1–V7 each answered or discharged with grounds, each
load-bearing assumption damaged or confirmed with its probe, a per-commit ledger (`2c6df437`,
`6890e9db`, `6197df86`: read body-free yes/no, findings by id), findings with stable IDs (prefix
`LV`: `LV1`, `LV2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

**Who applies a finding.** `cclive` is ordinary code, but every session reads it at open under
doctrine (`CONCURRENCY.md`, the onramp), so treat a finding that changes what the view *says* as
the principal's to decide (rule 3): record all, apply nothing. Counsel per finding is welcome,
labelled as counsel and kept beneath it.
