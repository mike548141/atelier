# Cold pass — `cclive`, a machine-wide view of live work

**Board:** `docs/roadmap/160-doctrine-review-owed/1290-rule-4-cold-pass-queued-cclive-instrument.md`
**Status:** ACT 1 RUN, 2026-11-22 UTC, by a Fable 5.1 reviewer under the principal's drain order of
2026-11-23 NZDT: **FAIL** (2 MAJOR, 4 MODERATE, 3 minor, 2 notes; `LV1`–`LV11`), verdict below the
divider. Act 2 (reconcile against the held sibling and the barred records) not yet run. Brief written
2026-11-14 UTC by a headless Opus 5.5 brief-writer (`cclive` lists it as session `c4d93896`).

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

---

## Verdict — act 1, Fable 5.1 cold pass, run 2026-11-22 UTC

**Overall: FAIL — 2 MAJOR, 4 MODERATE, 3 minor, 2 notes (`LV1`–`LV11`).** The view's central
promise fails on the machine it was built for: every claim held by the Fable drain running during
this pass (six items on this repo's board, this item among them) reads as *undated* and *quiet*, and
the default text view folds all six into one `+6 more` line. The `--json` output, the form "for
tools", is cut at 64 KiB when piped, so the man page's own example fails. Sessions and worktrees
were read correctly throughout, and no path through the tool writes; the repo looked busy, but a
reader could not learn *which items* are held. Rule 3 applies: nothing was applied, counsel sits
beneath each finding, and the decision is the principal's.

### Provenance (rule 4; V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Spawned as a subagent by a headless per-pass orchestrator, session `35fdc260` (Opus
  5.5), itself started by drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier
  orchestrators: they hold the context partition and commit the records, form no finding and write
  no severity. Session `eca14b23` wrote no brief and no delta and started no brief-writer for this
  pass. The reviewer was not started or instructed by `c4d93896`, `58027096` or `d0ca5d24`.
- **Authority:** the principal's weekly drain order of 2026-11-23 NZDT, verbatim: *"Start a fable
  drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*.
- **The spawn prompt (orchestrator direction, process only):** the item number, the worktree and
  brief paths, this file as the only writable file plus a review log outside the tree, the rule-2
  barred set as the brief prints it, the sibling's removal from the tree and the bar on finding it
  elsewhere, the deliverable's shape (act 1 below a divider; `### Reconcile` in act 2; the
  orchestrator folds the sibling), the live-systems terms (reads allowed, no writes, no quoting),
  load rules, and the release terms (act 2 starts on a message naming one file). It carried no
  question about the delta, no pointer to where risk lives, and no request to revise a finding.
  The log it asked for is `~/.claude/fable-drain/notes/atelier-160-1290-2013.md` (user-local,
  folded at the fold), the audit trail of every command below.
- **Review worktree:** `/Users/mike/worktrees/fable/atelier-160-1290-2013/atelier`, HEAD
  `3cf4041d`, containing `origin/main`. Only this file was written in it.
- **Exposure, disclosed:** the harness loaded user-level and repo instruction files and a memory
  index before the brief (private context this verdict does not carry; none of it is an account of
  this delta). `cclive`'s live output showed me the clipped first-paragraph text of every atelier
  claim; I withheld `160/1290`'s from my own inspection (field-level reads only). I read one
  board-store file by `--path`: the claim commit `c4bc074b` touched `docs/ROADMAP.md` and item
  `160/1280`; I read that item's claim paragraph (lines 1–4 and 18–26) for the current drain's
  stamp grammar, and lines 22–27 of `160/1000` and 28–33 of `160/1120` for the earlier drain's.
  None is barred by this brief; `160/1290` and `360/020` were not opened. No `git show` was used;
  every commit was read with `coldsweep --commit --path`. The session-log step was skipped.
- **Barred set honoured:** `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
  verdict in `docs/reviews/`, the pointer `160/1290`, the sibling, every delta commit's message
  body, the intent record `360/020`. `coldsweep` reported the sibling exclusion matched no file,
  which is the partition working. `--include-barred` was not used.

### What I read and ran

The three commits body-free (`2c6df437`, `6890e9db`, `6197df86`) and the one later commit that
touched a delta path (`1568acce`, one line: `readRepo` added to the exports); `instruments/cclive`,
`cclive.test.js`, `cclive.design.md` and `man/cclive.1` whole at HEAD; `ccclose`'s `board()`,
`CLAIM_LINE`, `CLAIM_TIME`, `FRESH_MS` and exports; `tools/board.py`'s `CLAIM_RE`; `pins.py
discover`'s docstring; every mirror site of `cclive` in the tree (`CLAUDE.md`, the child template,
`PROPAGATION.md`, `CONCURRENCY.md`, `CHANGELOG.md`, `instruments/README.md`, `skills/fleet-sweep`,
sibling man pages, `ccopen`); the CI workflow. Live, read-only: `cclive` from the worktree (text,
`--json`, `--all`, error paths, pipes) against the real estate and transcript store; counts of the
store's layout and record types. In scratch (a scratch `HOME`, scratch repos and worktrees, mutation
copies of the instruments): eleven probes and nine mutation runs. Both test suites and the man lint.

### The acceptance test

The question the design puts (§ 1, *what is any session, anywhere on this machine, doing, holding
or claimed on right now?*) is the right one at the right altitude: a read-only view over state that
already exists is the cheapest honest answer to the principal's 2026-09-12 ask, and the design's
rejection of an index, a lease and process inspection stands up (each adds shared state or a slow,
platform-bound source). The risk the altitude carries is the one found: the view depends on a
claim-stamp grammar it does not own and does not check, so when the writers moved, the reader fell
silent on the "claimed on" leg while still answering "doing" and "holding". The design does not
enumerate that threat (lens 4 at design altitude: what it trusts), and it should have.

### Lens 1 — approach and assumptions

My own load-bearing assumptions, then the brief's six:

- **A0 (mine): the claim grammar the tool reads is the grammar the estate's writers write.**
  DAMAGED. Three regexes in three homes: `board.py` `CLAIM_RE` `\(claimed [^)]*\)` (the index),
  `ccclose` `CLAIM_TIME` (`claimed <date> <time>`), `cclive` `CLAIM_STAMP` (`claimed <date>`, time
  optional). The live drain writes `🔒 <date>: claimed for the Fable pass by …` as a separate
  indented paragraph at item line 18 (`160/1280`); the earlier drain wrote `🔒 CLAIMED <date> UTC
  for the cold pass, in …` at line 22 (`160/1000`) and 28 (`160/1120`), wrapping over five or more
  lines. None is in the item's first paragraph; the current form puts the date before the word.
  No check on either side says so. → `LV1`.
- **A1: transcript mtime within ten minutes is a sound liveness test, and its last recorded `cwd`
  is where it is working.** CONFIRMED as far as it goes. Live store: `cwd` rides on every user,
  assistant and attachment record; `ai-title` records exist; one of the five newest transcripts had
  more than one distinct `cwd`, so the *last* one is the right read; my own session and five peers
  were located in their drain worktrees by their own `cwd`, agents included. The idle-at-prompt and
  slow-agent limits are printed every run. Unprobed and unprovable from here: a session that has
  moved by `cd` within one record's window.
- **A2: the newest of four refs by committer date is where every live claim has landed.** DAMAGED
  (probe P2). Local `main` carrying a newer unrelated commit hides a claim that sits only on
  `origin/main`: `ref main`, `claims 0`, while the claiming session was live. The limits line
  implies the opposite (*a claim not yet in a ref here is unseen*). → `LV3`.
- **A3: a claim's session id and worktree name, matched by first 8-hex token and by basename,
  identify the right session and worktree.** DAMAGED twice. (i) The id is read from the stamp
  *line* only (`cclive:290`); a stamp wrapped so the id lands on the next line gives `session
  null` and `quiet` while that session is live (P1, item `010/040`). (ii) Basenames collide: the
  drain's layout `<repo>-<item>-<hhmm>/<repo>` gives every worktree of a repo the same name (live:
  six named for this repo, three for another); a claim naming that basename marks every one of them
  live (P8), and the rows are indistinguishable. → `LV4`, `LV5`.
- **A4: longest-prefix matching never credits a session to the wrong repo.** CONFIRMED for the
  cases that matter (P5): a sibling directory sharing the repo's name as a prefix goes to
  *elsewhere*; the `/` boundary holds. A git repo nested inside a scanned repo is credited to the
  outer one — the documented one-level walk, not a finding. No test guards the boundary (`LV8`).
- **A5: no path through the tool writes.** CONFIRMED (P4): 89 files under scratch `.git` dirs,
  working trees and the transcript store, identical in size, mtime and sha1 across three runs
  (text, `--json`, `--all`). `ccclose` loads with no side effect (`require.main` guard); every git
  call is `execFile`/`spawnSync` with an argument array under `--no-optional-locks`; the four
  verbs (`for-each-ref`, `grep <ref>`, `worktree list`, `log --no-walk`) are reads.
- **A6: the quiet line and its footnote say only what is true of the repos on it.** DAMAGED (P7):
  a repo whose only branch is `develop`, with a board and a held claim, is listed quiet and starred,
  and the footnote says *no board*; the reason the JSON carries is *no main or master ref*, and
  the held claim is invisible. Latent on this estate (all 30 repos had a candidate ref). → `LV7`.

### Lens 2 — correctness and quality

What it claims, it mostly does: read-only (A5), no new shared state, roots and skips and known
zeros printed, `?` with a reason, stable fields in `--json` (every repo carries the same keys),
`FRESH_MS` and `board` shared by `require`, the agent walk bounded, caps counted. The failures are
in the two outputs a reader depends on: the claim list (`LV1`, `LV3`, `LV4`) and the piped JSON
(`LV2`). Overclaims against the text that makes them: the man page's *a stamp may sit on any line
of the item's first paragraph* (five physical lines, `-A 4`); the design's *one spawn per repo* for
claims (two: `for-each-ref` then `grep`); the design's status line still reads *build follows this
note*; *as `tools/pins.py discover` walks* (pins skips symlinks and hidden folders, `cclive` follows
symlinked directories); the onramp sentences' *every live session, claim and worktree on this
machine* (roots only; `main`/`master` only; ten minutes) — `LV9`. The `--fresh`, `--root`, exit
codes, help and `CCLIVE_ROOTS` behave as documented.

### Lens 3 — completeness and harvest

Nothing in `instruments/` or `tools/` duplicated the view; the reuse of `ccclose` is real (two
exports, `require`d, confirmed by `grep` and by `ccopen` now requiring both). What the work should
have covered and did not: the live claim grammars of the estate's own writers (it generalised one
board's eleven queue-run claims, design § 5); a writer-side check that a `[~]` carries a stamp some
reader can read; an end-to-end test of a wrapped stamp through real git (six mutations survive the
suite, `LV8`). Mirror sites all agree with each other (V3); the claim grammar has no single home
(V4); the census figures (3,602 logs, 0.2 h, 367 → 39 ms) are copied into the design, the code
comment and the man page — three explanatory copies, noted, not a finding.

### Lens 4 — security and privacy

Threat model, right-sized: inputs are the operator's own arguments and environment, directory and
ref names under the roots, board text at a ref, and other sessions' transcript tails; the sink is a
terminal read by an agent (and JSON for tools); the spawn surface is git. Checked against OWASP
ASVS 4.0.3 (fetched from the project's repository at the v4.0.3 tag, not recalled): **5.1.3**
positive validation — `parseArgs` allow-lists flags, bounds `--fresh` (ok); **5.3.8** OS command
injection — argument arrays, no shell, the ref from four fixed candidates, the board path from
`ccclose`, `--` before it (ok); **12.3.1** path handling — roots are the operator's, transcript
paths come from `readdir` (ok); **5.2.2 / 5.3.1** sanitisation and output encoding for the
interpreter — `printable` strips C0/C1 controls and bidi marks from transcript fields, branches,
worktree names, errors and skipped names, but **not from the repo's own directory name** in the
repo header (`cclive:672`) and the quiet line (`:690`): a name carrying `ESC [31m` and U+202E
printed raw (P3). → `LV6`, with its recurrence step. Privacy at design altitude: the view prints
other sessions' `aiTitle` (clipped to 56), `cwd` paths and branch names to any session on the
machine; same user, same machine, and the title is what makes a row recognisable — accepted, and
it is why this repo's rule (quote no transcript title) binds on every reader of the output. JSON
exposes the same fields plus full paths; no secret-bearing field exists. `/security-review`:
**discharged with grounds** — it reads the session's pending diff, and in this worktree the only
pending change is the deletion of the held sibling, so aiming it here before act 1 would have put
the sibling's text in front of me; a scratch clone with the delta as pending changes is not where
this session's cwd is. The manual ASVS pass above stands in its place.

### Standing checklist V1–V7

- **V1** no claim stronger than its evidence: `LV1`, `LV2`, `LV3`, `LV9`.
- **V2** re-run every live-proven claim: all of the brief's lines re-run (ledger below); every one
  reproduced except the man page's own `--json | jq` example, which fails (`LV2`).
- **V3** swept to every mirror site: the four onramp/doctrine sentences agree with each other; all
  are wider than the tool (`LV9`). No stamp copy was stale.
- **V4** one fact, one home: `FRESH_MS` and `board` are single-sourced (confirmed). The claim
  stamp grammar is not — three readers, three regexes, no writer-side home (`LV1`, counsel).
- **V5** no internal contradiction: the limits line vs A2 (`LV3`); the footnote vs the reason
  (`LV7`); man page "any line" vs `-A 4`, design "one spawn" vs two, "as pins.py walks" vs symlink
  handling (`LV9`). Cross-references checked for the rule reached: `CONCURRENCY.md:205` points at
  `instruments/cclive` and says what it shows; the man page's `NOTES` reaches the design note;
  `ccclose(1)` is the home of the ten-minute bound. All reach the rule they name.
- **V6** security and privacy: lens 4 above; `/security-review` discharged with grounds; `LV6`.
- **V7** provenance: stated in the brief and above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `2c6df437` design note | yes (`coldsweep`) | `LV9` (status line; spawn count; pins walk) |
| `6890e9db` tool, tests, man, design hunks, ccclose export | yes | `LV1`–`LV8`, `LV10`, `LV11` |
| `6197df86` README, CONCURRENCY, CHANGELOG | yes | `LV9` (onramp wording) |
| `1568acce` one export line (later, in scope by the since-log) | yes | none |

### Findings

**LV1 — MAJOR. Live claims read as undated and quiet, and the default view hides them.** On this
repo at 2026-11-22T20:22Z the view printed `claims 6 (0 dated, 6 undated)` for items `160/1190`,
`1280`, `1290`, `1440`, `997`, `999` — the six Fable passes of the running drain, every one held
by a live session in a live worktree — and, in the default text view, no claim line at all, only
`claim +6 more (0 dated, 6 undated; --all lists them)`. With `--all` each prints `undated quiet`.
Cause, two-fold and proven in scratch (P1 `010/030`): the stamp sits in a later paragraph of the
item, outside the five physical lines `git grep -A 4` and the paragraph rule read; and the current
form puts the date before the word (`🔒 2026-11-22T20:10Z: claimed for …`), which `CLAIM_STAMP`
(`claimed <date>`) never matches wherever it sits. The design's premise (§ 5: *on a real board all
eleven claims in one repo carried the stamp on line two*; undated lines are *most of them old*) is
one writer's grammar generalised, and it fails on the writer the principal runs every week. Estate-
wide the view counted 3 dated and 53 undated claims. This is the brief's worst failure named: a
held claim marked quiet — six of six. *Counsel:* read the stamp anywhere in the item (the whole
item file, not `-A 4`), accept `<date>: claimed` and `CLAIMED <date>` as well as `claimed <date>`;
list undated `[~]` lines by default as *undated* rather than fold them, since undated now means
"unreadable stamp" as often as "old"; and, at altitude, give the claim stamp one home (`board.py`'s
`CLAIM_RE`, which the index already relies on) with a writer-side check in `pointerscan` or
`board.py --check` so an off-grammar claim fails noisily at the commit that writes it. Three readers
(`board.py`, `ccclose`, `cclive`) should then import one regex. *Principal's to decide:* it changes
what the view says, and the writer-side half touches the drain's claim form.

**LV2 — MAJOR. `--json` is truncated at 64 KiB when written to a pipe.** `main()` calls
`console.log(JSON)` then `process.exit(0)` (`cclive:723-725`); on macOS a pipe is written
asynchronously and `exit` drops the unflushed tail. Live: `cclive --json | wc -c` gave 65536,
70241, 70240 on three runs against 70242 to a file; the man page's example `cclive --json | jq
'.totals'` failed with `jq: parse error: Unfinished string at EOF` (exit 5). Control: `node -e
'console.log("x".repeat(1e6)); process.exit(0)' | wc -c` → 131072. The text view (4 KB here) is
under the buffer and unaffected; `ccopen`, which `require`s the module, is unaffected; any tool
that pipes the JSON on this machine is broken intermittently. *Counsel:* set `process.exitCode` and
return instead of `process.exit(0)` after the write (mutation control m9: the suite stays green),
or write with a callback and exit inside it; add a test that pipes a >64 KiB `--json` through a
child process and parses it.

**LV3 — MODERATE. A claim present in a ref on this machine can be invisible.** Claims are read at
one ref, the newest of four by committer date (A2). When local `main` carries a newer commit that
lacks a claim pushed to `origin/main` from a worktree — the two-sessions moment the tool
exists for — the claim is unseen (P2: `ref main`, `claims 0`), and the limits line says the
opposite. *Counsel:* grep the local and remote tips of `main`/`master` and union the claims by id
(two spawns, still no fetch), or at least make the limits line say *at one ref, the newest of …*.

**LV4 — MODERATE. The session id and worktree are read from the stamp line only.** `cclive:290`
slices `after` from the stamp *line*; a stamp wrapped at the house width so the id or `wt:` lands
on the next physical line yields `session null` / `worktree null`, so a live session's claim reads
`quiet` (P1 `010/040`). Real stamps on this board wrap exactly so (`160/1000:22`, `160/1120:28`).
*Counsel:* search the rest of the paragraph (the joined text from the stamp onward), not the line.

**LV5 — MODERATE. Worktree identity is the basename, and basenames collide.** Under the drain's
layout every worktree of a repo is named for the repo: the live view printed six `wt atelier (no
branch) … live [detached]` rows and six sessions at `atelier (HEAD)`, indistinguishable; P8 shows
a claim naming the shared basename marks every same-named worktree live (`cclive:554`) and
`liveNames` (`:546`) is a machine-wide set, so the match crosses repos. *Counsel:* name a worktree
by the path segments that distinguish it (the parent directory when basenames collide, or the path
under the common parent), and match `wt:` against a worktree's full path segments, scoped to its
repo; print `(detached)` rather than `(HEAD)` for a detached branch read from the transcript.

**LV6 — minor, security (ASVS 5.2.2, 5.3.1). The repo's directory name is printed raw.** Every
other printed field passes through `printable`; the repo header (`cclive:672`) and the quiet-line
names (`:690`) do not, so a directory name carrying terminal controls or a bidi override reaches
the terminal unchanged (P3). Exploitability is low: the name is chosen by whoever clones under the
operator's own root — which sets the severity. *Recurrence prevention:* encode at the sink, once:
route every string `render` emits through `printable` (or build lines from already-sanitised
fields), and add one fixture with a hostile directory name. Mutation control m8 shows the fix is
test-neutral. No disclosure route is needed; the tool is not yet shipped to adopters as a package.

**LV7 — minor. The quiet line's footnote is wrong for one class of repo.** `*` marks
`claimCount === null`, and the footnote says *no board*; a repo with a board whose claims are
unknown because it has no `main`/`master` ref is starred with the same words, its held claim
unseen (P7). *Counsel:* print the reason per starred repo (`no board`, `no main/master ref`, `git
grep failed`), or read the repo's `HEAD` branch as a fifth candidate.

**LV8 — MODERATE. The tests stay green on six broken changes.** Scratch-copy mutations, each 32
pass / 0 fail: a claim naming a *quiet* worktree reads live (m1); the `/` boundary in `locate`
removed (m2); `--no-optional-locks` removed (m3); `git grep -A 4` → `-A 0`, so no stamp wrapped to
line 2 is ever read end to end (m5 — the `LV1` class; the wrapped-stamp tests use synthetic rows
and never real git); the longest-path-first index sort removed (m6: the `<repo>/.claude/worktrees/
<name>` shape has no fixture); `quiet` ignoring read errors (m7). *Counsel:* end-to-end fixtures
through real git for a wrapped stamp, a sibling-prefix `cwd`, a nested worktree, a repo whose git
read fails, a claim naming a quiet worktree, and a piped `--json` over 64 KiB (`LV2`).

**LV9 — minor. Overclaims and drift between the design, the man page, the code and the onramp.**
Man page § *What counts as a claim*: *a stamp may sit on any line of the item's first paragraph*
— the code reads five physical lines. Design § 5 table: claims cost *one spawn per repo* — two.
Design status line: *build follows this note* — the build landed in the next commit and the line
was not updated. Design § 5: repos found *as `tools/pins.py discover` walks* — `pins.py` names a
symlink or hidden folder as skipped; `cclive` follows symlinked directories and scans hidden ones.
`CLAUDE.md:24`, the child template, `PROPAGATION.md:178`: *every live session, claim and worktree
on this machine* — repos under the roots, claims at `main`/`master`, transcripts in ten minutes;
the tool's own limits say so, the onramp sentence does not. *Counsel:* one pass over the five
texts; the onramp sentence can say *under the estate roots*.

**LV10 — note. The transcript store is hard-coded to `~/.claude/projects`** (`cclive:712`, as
`ccclose:137`). `ccfleet` and `install` honour `CLAUDE_CONFIG_DIR`; a machine that sets it would
show *N sessions, 0 fresh* — a blank that reads as nothing. Consistent with `ccclose`; worth one
shared helper when either is next touched.

**LV11 — note. `lastWrittenAgoMs` can be negative in `--json`** (−1 ms for my own session, whose
transcript was written after `now` was taken). `ago()` clamps the text view. Clamp the field too.

### Re-run ledger (from the worktree root, foreground, `nice -n 10` for the suites)

| Line | Result |
|---|---|
| `node --test instruments/cclive.test.js` | 32 pass, 0 fail, 16.4 s, exit 0 (load 10.9, 12 cores) |
| `nice node --test instruments/ccclose.test.js` | 153 pass, 0 fail, 395 s, exit 0, load 5.7–7.4 |
| `mandoc -T lint -W style instruments/man/cclive.1` | silent, exit 0 |
| `instruments/cclive; echo $?` | view printed in 2.0 s, exit 0 |
| `instruments/cclive --json > <scratch>/v.json; echo $?` | 70,234 B, exit 0, parses |
| `instruments/cclive --root /nonexistent-dir; echo $?` | `UNREADABLE (ENOENT)` header, exit 0 |
| `instruments/cclive --fresh 0; echo $?` | usage error, exit 2 |
| `instruments/cclive --json \| jq '.totals'` (man page) | **parse error, jq exit 5** (`LV2`) |

### Follow-up checklist

- [ ] `LV1` and `LV4`: the principal rules on the reader's grammar and on a writer-side check for
      the drain's claim form (rule 3; changes what the view says and what the drain writes).
- [ ] `LV2`: one-line fix plus a piped-JSON test; ordinary code, no ruling needed beyond the
      bulk approval of this verdict.
- [ ] `LV3`, `LV5`, `LV7`: the principal rules (each changes what the view says).
- [ ] `LV6`: encode at the sink; add the hostile-name fixture; record the recurrence step.
- [ ] `LV8`: the six end-to-end fixtures.
- [ ] `LV9`: one wording pass over the design note, man page, `CLAUDE.md`, the child template and
      `PROPAGATION.md`; `LV10`, `LV11` when the files are next touched.
- [ ] Act 2: reconcile against the held sibling and the barred records; screen the commit bodies.
- [ ] Scratch deleted at the end of act 1: the scratch estate, scratch `HOME`, mutation copies and
      the live captures under the reviewer scratch directory.
