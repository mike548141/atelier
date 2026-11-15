# Cold pass — `ccclose` expands a `for` loop's literal word list and counts the worktree adds it cannot resolve

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS RAN 2026-11-15 UTC — act 1 committed before the sibling opened, act 2
reconciled; verdict **FAIL** (1 MAJOR, 2 MODERATE, 3 minor, 2 notes). The sibling is folded
below the verdict. Brief written 2026-11-09 UTC.
**Sizing:** **medium** — one commit, about 120 lines of shell-reading logic in a 1,800-line
instrument, no live system, but the parsing has many edge shapes to probe.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1010-rule-4-cold-pass-queued-ccclose-loop-made-worktrees.md`.
**Why it earns a review:** `ccclose --identifiers` prints a block that sessions paste into their
records as fact. This delta teaches it to read a shell loop out of a transcript. Worst failure: the
block lists a worktree that was never made, or miscounts one that was, and the error is pasted into
the permanent record with nothing to show it was inferred.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `deeac927`,
  2026-11-03, and the Sonnet worker it dispatched, which wrote the code (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** session `84e3aa7f` (`claude-opus-5-5`), a headless brief-writer started
  on 2026-11-09 by coordinating session `74f2b8cd` (Opus 5.5). Neither authored any of this delta,
  and neither was started or instructed by the author. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing its briefs. It ran
  no review and used no Fable model. The principal's rule: whoever writes a brief does not run it.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  list of board items, the run constraints, and the principal's request verbatim, "Check all the
  repo's, any work that requires a fable review but does not have a brief written yet I want you to
  write those briefs then finish this session when thats all done". It carried no framing of the
  work. The brief-writer had no contact with the author or its workers.
- **Who reviews:** a fresh Fable 5.1 session or subagent started for this pass alone, from a spawner
  that passes rule 4's criterion. **Barred from reviewing:** session `deeac927` and everything it
  started; session `84e3aa7f` (this brief-writer); session `74f2b8cd`. Whoever takes the pass states
  the spawn in the verdict (V7).
- **The principal's approval:** none yet for the pass. His request above covers this brief only. The
  pass waits for his explicit permission for Fable work.

⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):

- its dispatch text; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` whole; the
  house-form brief `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` through
  line 728, including its verdict (read for shape, another surface); the top of one sibling brief;
- the queue pointer whole; the intent record whole;
- the delta body-free through `tools/coldsweep.py --commit 03d8503d` (subject, stat, diff, never the
  message body), `--help` of `coldsweep`, `board`, `leakscan` and `reviewscan`, commit subjects
  through `git log`, and file names under `docs/reviews/` and
  `docs/roadmap/160-doctrine-review-owed/`;
- the last three index lines of `docs/SESSIONS.md` and one earlier session record, read for the
  format of its own closing record; and the results of the re-run lines below, held in the sibling.

It did **not** open `docs/ROADMAP-DONE.md`, any other session record, any other prior verdict, or
any delta commit's message body. Its harness also loaded user-level and repo instruction files and a
memory index, which hold private context this brief does not carry. Everything evaluative it formed
is in the sibling.

## The acceptance test

No intent record for this delta carries a ruling of the principal's. Judge it against the standard
the instrument states for this block: a path that cannot be resolved is dropped, not guessed
(`instruments/ccclose.design.md`, `instruments/man/ccclose.1`), and `docs/method/RECORD.md` § *The
session log* on what the identifiers block is for.

## What the work is

One commit on `main`, `03d8503d` (first confirm your tree has it: `git merge-base --is-ancestor
03d8503d HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 03d8503d \
  --path instruments/ccclose \
  --path instruments/ccclose.test.js \
  --path instruments/ccclose.design.md \
  --path instruments/man/ccclose.1 \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 03d8503d..HEAD -- instruments/ccclose instruments/ccclose.test.js instruments/ccclose.design.md instruments/man/ccclose.1 CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- An add inside a `for` loop over plain words (no glob, brace, variable or command substitution) is
  expanded once per word; nested literal loops multiply.
- A loop over anything else leaves its variable unset, so the add is dropped.
- Every add still unresolved is counted, and the Worktrees field prints one line, "N worktree adds
  not resolved"; the line is absent when every add resolved.
- `--json` carries `worktrees.unresolved`.
- A `-b` branch holding an unresolvable variable is counted, not listed under its raw name.
- No path is ever guessed.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** `ccclose`'s `210/330` variable reading in its own right (pass `160/993`), and the
later `ccclose` changes `457f374d` and `4e3b3984` (their own passes). The board-order change
`5f7c2b0c` is pass `160/1020`, and the same reviewer may take it separately.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. The instrument reads transcripts, which hold text a session
or a tool wrote. Check what hostile or merely unusual transcript text can make it do: pathological
backtracking in the new patterns, unbounded expansion from nested loops, and any path printed that a
reader would take as fact. Quote no transcript content.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- `node --test instruments/ccclose.test.js`

## House rules for this run

**Live systems:** read-only reads of live systems as needed, no live writes. A check that would need
a write is marked **NOT RUN**, with what it would have checked. No push and no `gh` call that
writes, except committing this one file as the process below says.

- Never print a secret, and quote no key body, fixture bytes, personal data, private repo name or
  private path. This repo is PUBLIC; a child is referred to by type only.
- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Scratch
  repos, mutated copies and fixtures go under your session scratchpad and are deleted when you
  finish.
- No git command that writes in the worktree beyond committing this one file at the end of each
  phase (or handing it to an orchestrator to commit). Never mutate the worktree's `tools/` or
  `instruments/`.
- One heavy process at a time, foreground, long timeout, `uptime` first. Never run an installed tool
  by bare name from `PATH`: run it from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it only from a clean tree
  at a scratch clone of the code, or discharge it by grounds; never with this brief or its sibling
  dirty. A clean pass over markdown is weighed as nothing.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content —
the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only
after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, the queue pointer above, this brief's sibling
(its `.deferred.md` file, now folded below the verdict), every delta commit's message
body, and the intent record
`docs/roadmap/210-instruments-open-features/360-ccclose-drops-a-loop-made-worktree-without-saying-so.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1010-rule-4-cold-pass-queued-ccclose-loop-made-worktrees.md \
  --also-exclude docs/roadmap/210-instruments-open-features/360-ccclose-drops-a-loop-made-worktree-without-saying-so.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`03d8503d`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `CW`: `CW1`, `CW2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling
is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (cold pass, 2026-11-15 UTC)

**Overall: FAIL — 1 MAJOR (CW1), 2 MODERATE (CW2, CW3), 3 minor (CW4, CW5, CW6), 2 notes (CW7,
CW8).** The loop expansion does what its tests say for a loop that runs clean; what fails is the
case the brief names as the worst one. A loop is one command with one result, and the delta lets
that one result stand for every worktree the loop names: when one iteration fails and the last
succeeds, a worktree that was never made is listed as "put away"; when the last fails, every
worktree the loop did make is dropped and not counted, which is the silence `210/360` set out to
end. Reasoning and probes are under each finding; every check below can be re-run from the
commands given.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. Session started 2026-11-15 ~21:43 UTC for this pass alone.
- **Spawn:** a headless orchestrator session (Opus 5.5), itself started by drain session
  `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition,
  form no finding and write no severity. Neither wrote the brief or the delta. I was not started
  or instructed by `deeac927` or anything it started, by `84e3aa7f`, or by `74f2b8cd`.
- **The principal's approval:** his weekly drain order, `/fable-drain`, invoked 2026-11-16 06:53
  NZDT (2026-11-15 17:53 UTC), as relayed in the spawn prompt. The brief's "waits for the
  principal's explicit approval" is met by that order.
- **Orchestrator direction, disclosed.** Process only: the item id, the worktree path, the brief
  path, the barred set (the brief's "Deferred reading" list plus the held sibling, held outside
  any path given to me), the work-log path, the deliverable's shape (`CW` prefix, act 1 below a
  divider, Status line, ≤ 100 columns, `date -u`, NZ English), load rules (`uptime` first,
  `nice -n 10`, one suite at a time, bounded fixtures), live-system rules ("read-only reads of
  live systems are allowed … NO live writes"), publication rules (session ids only, no private
  repo name or path, no estate fact), and the stop words for each act. It contained no question
  about the delta, no pointer to where the risk lives, and no request to form or revise a
  finding. The release message for act 2 had not arrived when this act was written.
- **Barred-set choice:** the brief's list, unchanged, plus the two `--also-exclude` paths the
  brief prints. I opened none of: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
  any other file under `docs/reviews/`, the queue pointer, the intent record past its first line
  (its title and state line only, `head -1`), the sibling, or any commit message body.
- **Exposure, disclosed:** my harness loaded user-level and repo instruction files and a memory
  index before the brief, which carry private context and standing rules; none describes this
  delta. The `git log --oneline` line the brief gives printed 68 commit subjects because
  `CHANGELOG.md` is a delta path; subjects are not barred and none reads as an account of this
  delta beyond its own. I ran one `coldsweep` tree sweep (14 hits over 841 files, 571 excluded);
  no `--include-barred`.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1010-2141/atelier` at `53f25fa4`
  (`main`), read-only to me except this file. Scratch under the session scratchpad only; probe
  copies and fixtures deleted at the end of the act.
- **Work log:** `~/.claude/fable-drain/notes/atelier-160-1010-2141.md`, written as I went;
  published verbatim at the fold.

### Method record — what was examined, how, and what was not

**Examined.**

- The delta, body-free: `python3 tools/coldsweep.py --root <wt> --commit 03d8503d --path
  instruments/ccclose --path instruments/ccclose.test.js --path instruments/ccclose.design.md
  --path instruments/man/ccclose.1 --path CHANGELOG.md`. Footer: subject, stat and diff of 5
  files printed; message body not printed; 3 board-store files left out (I named none).
- Tree check: `git merge-base --is-ancestor 03d8503d HEAD` → exit 0. Commits on
  `instruments/ccclose` since the delta: `50547442`, `1bc89816`, and the non-goals `457f374d`,
  `4e3b3984`. None touches `worktreeAdds`, `loopsAround`, `notePending`, `resolvePending`,
  `identifiersWorktrees` or the worktrees render beyond line drift (read at HEAD, below).
- At HEAD: `instruments/ccclose` 236–395 (`shellWords`, `resolveFrom`, `WT_ADD`, `FOR_HEAD`,
  `LOOP_OPEN`, `LOOP_CLOSE`, `loopsAround`, `worktreeAdds`), 540–572 (`LITERAL_ASSIGN`,
  `assignmentsIn`, `expandVars`), 715–855 (`notePending`, `resolvePending`, the `readTranscript`
  loop), 1630–1670 (the second `worktreeAdds` call in `commitEvidence`, stats discarded),
  1802–1835 (`identifiersWorktrees`), 1920–1941 (the worktrees render).
  `instruments/ccclose.design.md` 385–419; `instruments/man/ccclose.1` 490–519;
  `docs/method/RECORD.md` 95–137 (the identifiers block, the acceptance standard);
  `instruments/README.md` 392–424; `CHANGELOG.md` 1847–1858; `docs/method/REVIEW.md` whole.
- Grep over the instruments: `worktreeAdds` and `loopsAround` are called from `ccclose` only
  (two sites) and its tests; `spawnSync` is the pre-existing git/gh wrapper; nothing executes
  transcript text.
- The re-run line (ledger below) and three probe scripts on a scratch copy of `ccclose` and
  `cctranscript` (never the worktree's files): `probe1.js` (27 parsing shapes through
  `cc.worktreeAdds`), `probe2.js` (five fixture transcripts through `cc.readTranscript`, written
  and deleted in a temp dir), `probe3.py` (`/usr/bin/python3 -I`; each timing case its own
  `node --max-old-space-size=1536` process under `nice -n 10`, 60 s timeout, smallest first,
  stop at the first timeout). One scratch git repo to confirm git's own output and exit status
  for a partly failing loop; removed after.

**Attacked, and how.** The load-bearing assumptions I named before reading the tests (lens 1
below), each with a probe; the brief's claims list, each against the text that makes it; the
brief's framing ("about 120 lines … no live system") as itself attackable; lens 4's three
named vectors (backtracking, unbounded expansion, a printed path a reader takes as fact) with
bounded fixtures.

**Not examined, and why.**

- A run of `ccclose --identifiers` against a real session transcript: **NOT RUN**. The fixture
  transcripts drive the same `readTranscript` → `resolvePending` → `identifiersWorktrees` path
  the tests use, and a real transcript would print other sessions' paths and text into this
  record for no added evidence.
- `/security-review`: **discharged with grounds**. It reads the session's pending diff; this
  tree's pending diff is the brief (this file) and the removed sibling, which it must not read,
  and the delta is landed, so there is nothing it can be aimed at. Lens 4 was run by hand
  instead (below).
- The harness's rule for `is_error` on a non-zero exit was not re-verified against the harness;
  the instrument already rests on it (`resolvePending`'s own comment), and the fixtures set the
  flag as the tests do. CW1 holds under that rule and is stated against it.
- `cctranscript` internals (`classifyUserRecord`, `extractText`): out of the delta; relied on
  through the tests only.

### Lens 1 — approach and the load-bearing assumptions, named first

The problem is real and the altitude is right: a worktree put away leaves no trace in git, so
the transcript is the only source, and a loop is a common way sessions make several at once. The
chosen remedy, a small literal-only expansion plus a count of what was not read, matches the
instrument's stated posture (read the common forms, miss rather than guess). The assumptions it
rests on:

- **A1 — the words of a literal `for` list are the worktrees made.** Confirmed as far as the
  shell goes (P26, P29, P30e, P32 behave as `bash` would). **Damaged** where the body decides:
  `[ -d /w/$n ] && continue` lists all three (P24), and a failing iteration is invisible to the
  expansion (P2). The expansion is a model of the command, not of what ran. → CW1.
- **A2 — one `tool_result` can stand for every add in the command.** True for a single add
  (exit status = the add's); **false for a loop**, whose exit status is its last iteration's
  (`bash` manual; confirmed in a scratch repo: `wt-a` existed, loop printed `fatal:` for it and
  made `wt-b`, `loop exit=0`). → CW1.
- **A3 — `for|while|until|select` and `done` can be paired by scanning words.** Holds for code,
  **fails for prose inside the command**: the scanner knows no quotes, so " for " in a commit
  message opens a loop that never closes (P1a), and `echo done` closes one early (P1c, safe
  direction). → CW2.
- **A4 — the head pattern is cheap on any input.** **Damaged**: three overlapping whitespace
  consumers make it cubic on a whitespace run with no `; do` after it (P3). → CW3.
- **A5 — nested literal loops are small.** Unbounded, with a quadratic de-duplication;
  216,000 combinations do not finish in 60 s (P4). → CW4.
- **A6 — "a loop over anything else" drops the add.** Holds for every `for VAR in <non-plain>`
  shape probed (P5a, P8, P27, P28, P30b, P30d), **fails for `for ((…))`**, which the head
  pattern never sees and whose init `i=0` the assignment reader takes as a literal (P30a). → CW5.
- **A7 — "N worktree adds not resolved" tells the reader how short the list is.** It tells them
  how many *commands* were not read; a loop command is one (P5a, P5b). → CW6.

The brief's framing: "no live system" is right (the instrument reads files and runs `git`
read-only); "about 120 lines" undersells the reach, since the expansion changes what every
later field (present/put away, branch state) asserts about each listed path. Its non-goals fence
nothing this delta carries.

### Lens 2 — correctness and quality, claim by claim

Each claim from the brief's § *What the delta claims*, with its result:

- *Literal `for` list expanded once per word; nested literal loops multiply.* Holds (tests;
  P28b, P29). Over-expands when the body skips or fails (CW1) or when prose opens a loop (CW2).
- *A loop over anything else leaves its variable unset, add dropped.* Holds for `for VAR in …`
  shapes; **fails** for `for ((…))` (CW5).
- *Every unresolved add counted; one line; absent when all resolved.* Holds for commands whose
  result is not an error (tests). **Not counted** when the command's result is an error, even
  where the loop made worktrees (CW1, case B).
- *`--json` carries `worktrees.unresolved`.* Holds (test `sess-id-14`).
- *A `-b` branch with an unresolvable variable is counted, not listed raw.* Holds (P5b; test
  `$(mktemp -u)`).
- *No path is ever guessed.* **Fails** in two shapes: CW1 case A lists a path whose add failed;
  CW2 lists a path the shell never built.

Quality: the code is small and readable; `stats` as an out-parameter is a reasonable fit to the
existing shape; the render handles the three states (none, none listed + count, list + count).
The second call site (`commitEvidence`, line 1665) passes a throw-away `stats`, so unresolved
adds in a subagent's transcript reach neither the count nor the list — consistent with the
block's stated scope (parent transcript only), not a defect of this delta.

### Lens 3 — completeness and harvest

- **V3 mirrors:** the statement lives in the code comment, `ccclose.design.md`, `man ccclose.1`
  and `CHANGELOG.md`; `instruments/README.md`'s `ccclose` section describes neither the `$VAR`
  reading nor loops, so no mirror is owed there; `RECORD.md` describes the block at field level
  ("a field it cannot derive says so"), which the count line satisfies. Sweep: `coldsweep
  'worktree adds? not resolved|210/360|plain words \(no glob|loopsAround'` → 14 hits, all in
  the five delta files and their tests. No mirror missed.
- **Tests that would stay green on a broken change:** none of the shipped tests exercises a
  loop whose result is an error or whose text shows a `fatal:`, a body holding the word `for`,
  an arithmetic `for`, or a long whitespace run. All four broken behaviours above pass the
  suite (111/111). The tests pin what the author meant, not what a shell does.
- **Harvest:** `shellWords` already tracks quotes; `loopsAround` does not reuse it for the
  body scan (CW2 counsel).

### Lens 4 — security and privacy (mandatory)

The input is Bash `tool_use` text from a transcript: written by a session or its tool, not by
the principal, and read by a tool whose output is pasted into a public record. Threats checked:

- **Pathological backtracking** — present, cubic (CW3). Measured, not recalled.
- **Unbounded expansion** — present, quadratic de-duplication, no cap (CW4).
- **A printed path a reader takes as fact** — CW1 and CW2 both produce one; the record then
  states "put away" for a path that never existed.
- **Execution of transcript text** — none: `spawnSync` runs `git`/`gh` with argument arrays;
  no shell is invoked on command text.
- **Leak surface** — the count line prints no path or variable name (test asserts
  `doesNotMatch /NEVER_SET|ALSO_UNSET|nowhere/`); listed paths go through `tildePath`.
- `/security-review`: discharged, grounds above.

### The standing checklist

- **V1** — three claims stronger than their evidence: "a dropped one is counted" (CHANGELOG
  1848; false under an error result, CW1 B), "No path is ever guessed" (CHANGELOG 1857; CW1 A,
  CW2), "a loop over anything else … dropped" (code comment 298–299, design 406–407; CW5).
- **V2** — the one re-run line reproduces: 111/111, exit 0 (ledger below). No other
  "live-proven" claim in scope.
- **V3** — swept; no mirror missed (lens 3). CW7 notes the four surfaces understate the
  exclusion class the code applies.
- **V4** — one home for the rule (`ccclose.design.md`); the man page and CHANGELOG are stamped
  copies at the point of use. Satisfied.
- **V5** — no contradiction between surfaces; the understatement in CW7 is the same statement
  told shorter, not a conflict. Cross-references reached: design §*Worktrees and branches* holds
  the rule the man page restates; `RECORD.md` 119–121 holds the block's purpose the acceptance
  test cites.
- **V6** — lens 4 above; scanner discharged with grounds.
- **V7** — provenance stated above, repeating the brief's.

### Per-commit ledger

- `03d8503d` — read body-free: yes (`coldsweep --commit`, five `--path`s, no board file).
  Findings: CW1, CW2, CW3, CW4, CW5, CW6, CW7.
- Pre-existing code the delta's field reaches — read at HEAD. Findings: CW8 (note; not this
  delta's).

### Findings

**CW1 — MAJOR. One result stands for every worktree in a loop: a failed iteration lists a
worktree that was never made, and a failing last iteration hides every one that was.**
`instruments/ccclose` 736–749 (`resolvePending`): `if (b.is_error) return;` then every
expanded add is pushed and `unresolved` added. A `for` loop's exit status is its last
iteration's, so a single `tool_result` cannot say which of N adds ran.
*Probe (P2, fixture transcripts through `readTranscript`):* A — `for n in a b; do git worktree
add -b wt-$n /w/wt-$n; done`, result text shows `fatal:` for `wt-a` and success for `wt-b`,
`is_error: false` → both listed, `unresolvedAdds 0`. B — same loop, `wt-a` made, `wt-b` fails,
`is_error: true` → nothing listed, `unresolvedAdds 0`. E — the loop followed by `&& echo ok`
behaves as A. *Shell fact confirmed in a scratch repo:* a pre-existing `wt-a` branch →
`fatal: a branch named 'wt-a' already exists`, `wt-b` made, `loop exit=0`.
*Consequence:* `identifiersWorktrees` (1819) then prints case A's phantom as `worktree put
away; branch kept, …` — a creation that never happened, pasted into the record as fact. Case B
is the exact silence the intent record's title names, now reachable through the fix itself.
Before the delta, one command was one add and the gate was sound; the delta widened the command
to N facts and left the gate at one. Same class: a body that `continue`s or tests before adding
(P24) lists every word.
*Reasoning to severity:* the brief's acceptance standard (RECORD 119–121: "each one the session
created") and its named worst failure are both met head-on; the trigger — a branch or path
already existing for one word of a loop — is an ordinary thing in a repo that makes worktrees
weekly; the record is permanent and public.
*Counsel (not applied):* a loop command's expansion is a hypothesis to check against the
result text, which git fills per iteration: count `fatal:` lines (and `HEAD is now at` lines,
one per success — note `Preparing worktree` prints before a `fatal:`, so it is not a success
mark) against the expansion; where the counts disagree, or where `is_error` is set on a command
that expanded to more than one add, list nothing from it and count it unresolved. Add the two
fixtures above to the tests.

**CW2 — MODERATE. The loop scanner reads no quotes, so a plain word opens or closes a loop;
an unclosed loop expands an add that ran after `done` into every word.** `LOOP_OPEN`
(`ccclose` 305) counts ` for `, ` while `, ` until `, ` select ` wherever a separator or space
precedes them; `LOOP_CLOSE` (306) likewise for `done`. A loop whose body never closes has
`doneAt = Infinity` (321–326) and every later add is "inside" it.
*Probe (P1a):* `for n in a b; do git commit -m "fix for $n"; done; git worktree add --detach
/w/$n` → listed `/w/a` and `/w/b`, unresolved 0. Control P1b (body without the word "for") →
nothing listed, unresolved 1. A shell makes `/w/b` only (the variable keeps its last word), so
`/w/a` is a guessed path. P1c (`echo done` in the body) closes the loop early and drops the
in-loop add after it, counted — the safe direction, and the same cause. A `for X in Y; do`
inside a quoted string opens a loop the same way.
*Reasoning to severity:* the shape (an add after a loop, reusing its variable) is less common
than CW1's, but the result breaks the acceptance standard outright, and the word "for" is the
most ordinary English in a commit message. MODERATE, not MAJOR, on frequency.
*Counsel:* count an opener only at command position (after `;`, `&&`, `||`, `|`, `(`, `{`, a
newline, or the keywords `do`/`then`/`else`) or scan the body with `shellWords`' quote tracking;
and when a loop never closes, treat its variable as unknown (drop and count) rather than
expand — fail toward the count, as the rest of the function does.

**CW3 — MODERATE. `FOR_HEAD` backtracks in cubic time on a whitespace run that is not followed
by `; do`.** `ccclose` 304: `in\s+([^;\n]*?)\s*(?:;|\n)\s*do\b` — `\s+`, `[^;\n]*?` and `\s*`
all consume spaces, so a failing match retries every split.
*Probe (P3, each case its own process, 60 s timeout):* command `for n in ` + N spaces + `x git
worktree add --detach /w/$n`: N = 1,000 → 310 ms; N = 4,000 → 19.3 s; N = 16,000 → did not
finish in 60 s. Growth ≈ N³. With a `\ndo` present every N up to 64,000 → 1 ms. Alternating
` \t` runs: 32 KB → 1.2 s (≈ N²).
*Reasoning to severity:* the pattern runs on every Bash command in a transcript that contains
`worktree`, in the parent's and each subagent's transcript (`commitEvidence`, 1665); a 16 KB
line of whitespace is small for a tool result pasted into a heredoc, and it stalls the close-out
tool for minutes. Reach by accident is low, by a hostile command trivial; the brief names the
vector. The fix is one character class, so MODERATE rather than minor on the cost of a hang
in a tool every close runs.
*Counsel:* make the list non-overlapping with its neighbours, e.g. require the list to start
and end on a non-space (`in[ \t]+(\S(?:[^;\n]*\S)?)?[ \t]*(?:;|\n)\s*do\b`), and add a bounded
timing test (a 16 KB whitespace run must finish under a second).

**CW4 — minor. Nested literal loops expand without a cap, and the path de-duplication is an
array scan, so the cost is quadratic in the paths produced.** `ccclose` 357–361 builds one
`Map` copy per combination; 384 `site.includes(wtPath)` is O(paths) per path; 370 reruns the
`cd` regex per environment.
*Probe (P4):* depth 3 × 10 words → 1,000 paths, 11 ms; × 30 → 27,000 paths, 1.3 s; × 60 →
216,000 paths, >60 s. Depth 4 × 10 → 10,000, 300 ms; × 20 → 160,000, >60 s.
*Reasoning:* a session that writes three nested loops of 60 words each to make 216,000
worktrees is not a real session, so this is a robustness gap, not a live defect. minor.
*Counsel:* a `Set` for `site`; hoist the `cd` scan out of the per-environment loop; cap the
combinations (a few hundred is generous) and count the add as unresolved above it.

**CW5 — minor. An arithmetic `for ((…))` loop is neither expanded nor dropped: its init is
read as a literal assignment and one path is listed, the rest lost silently.** `FOR_HEAD`
needs `for NAME in`; `LITERAL_ASSIGN` (543) accepts `i=0` after `(`, and the `;` inside the
parentheses satisfies the separator test (354).
*Probe (P30a):* `for ((i=0;i<2;i++)); do git worktree add --detach /w/$i; done` → listed `/w/0`
only, unresolved 0. The claim "a loop over anything else leaves its variable unset, so the add
is dropped" (code 298–299, design 406–407, CHANGELOG) does not hold for this loop form.
*Counsel:* let `loopsAround` recognise `for\s*\(\(` as a loop with `words: null` over the
variable its init names, or let `assignmentsIn` skip an assignment inside `((…))`.

**CW6 — minor. The count line says "N worktree adds", a reader hears N worktrees, and the
parenthetical names two of its causes.** The count is per command (`dropped` is set once per
`WT_ADD` match, 362–391). *Probe (P5a, P5b):* `for n in $(ls); do git worktree add …` → 1;
`for n in a b c; do git worktree add -b $n-$X …` → 1 for three worktrees. The render (1930)
explains "(a variable with no literal assignment, or a loop over something other than plain
words)"; an unknown commit-ish (P7) and an unknown `cd`/`-C` base (380) also count and are not
named. The man page's "so the list is known to be short" is the honest version; CHANGELOG's "so
the reader knows to fill them in" overstates what N tells them.
*Counsel:* "N add commands not resolved (a loop among them may stand for several worktrees)";
drop or widen the parenthetical.

**CW7 — note. The four prose surfaces understate the exclusion the code applies.** Code 328
excludes `$ \` * ? [ ] { } ( ) < > ~ \`; the comment (297), design (405), man (507) and
CHANGELOG (1851) say "no glob, brace, `$` or backtick" or "variable or command substitution".
A list holding `~` or an escaped space (P26) is dropped and counted, which the prose does not
predict. Same statement told shorter; not a contradiction (V5). The design.md hunk (405–409)
also loses the list item's two-space indentation; it renders, and reads oddly in source.

**CW8 — note, pre-existing, in scope but not this delta's.** Two behaviours of the branch
field the delta touched: (a) `git worktree add /w/x origin/main` lists branch `origin/main`
(P7b), where git detaches at a commit-ish that is not a local branch, so the record's branch is
wrong; (b) `git worktree add /w/x $REF` with `$REF` unknown is now dropped and counted (P7)
although the path is known — before the delta the branch was guessed as the basename, which was
worse, but listing the path with an unknown branch would keep the true fact. Recorded for the
owner to weigh with CW6; no severity against this delta.

### Re-run ledger

- `nice -n 10 node --test instruments/ccclose.test.js` — from the worktree root, foreground,
  2026-11-15 21:47–21:49 UTC → exit 0; tests 111, pass 111, fail 0; 143.7 s.

### Follow-up checklist (for the owner; nothing applied — rule 3)

- [ ] CW1: cross-check a loop's expansion against its result text; two fixtures (A, B) as tests.
- [ ] CW2: openers at command position only, or quote-aware body scan; unclosed loop → unknown.
- [ ] CW3: non-overlapping `FOR_HEAD`; bounded timing test.
- [ ] CW4: `Set`, hoisted `cd` scan, combination cap.
- [ ] CW5: arithmetic `for` recognised as a non-literal loop.
- [ ] CW6: count-line wording and causes; CHANGELOG sentence.
- [ ] CW7: exclusion class stated once, fully, in the design; the copies follow; indentation.
- [ ] CW8: owner's call on the branch field for a non-branch commit-ish and an unknown one.

### Owed asks for the principal

None that blocks a decision on the findings. One for his awareness: CW1's counsel reads git's
result text, which this instrument has so far done only for `EnterWorktree`; it widens what the
block treats as evidence, and that is a design choice rather than a bug fix.

ACT 1 SAVED 2026-11-15 UTC.

### Reconcile (act 2, 2026-11-15 UTC)

Opened after act 1 was committed (`dc243522`, this file only), on the orchestrator's release
message naming the sibling's held path: the sibling, the delta's commit message body, the queue
pointer `160/1010` and the intent record `210/360`, each whole. `docs/SESSIONS.md`,
`docs/sessions/`, `docs/ROADMAP-DONE.md` and other verdicts stayed unopened; nothing here needed
them. Act-1 text above is unrevised. No finding was formed at reconcile.

**Against the sibling's questions** (the brief-writer's floor, 2026-11-09; none was read before
act 1):

- Q1 (text patterns and quoted or prose words) ↔ **CW2**. Both directions occur: a false listing
  when a prose opener leaves the loop unclosed (P1a), a false drop when `echo done` closes it
  early (P1c). Act 1 graded the listing direction MODERATE and the drop direction safe.
- Q2 (one failing add in a loop, whole-command result) ↔ **CW1 case A**: yes, listed as made.
- Q3 (`break`, `continue`, an `if` guard) ↔ **CW1**, probe P24: listed once per word.
- Q4 (bound on the product, cost of a long list) ↔ **CW4**: no bound; the cost is quadratic in
  the paths produced through `site.includes`, measured to a timeout at 216,000 combinations.
- Q5 (unit of "N worktree adds") ↔ **CW6**: per command, which the sentence does not say.
- Q6 (`site.includes` de-duplicates two words resolving to one path) — checked at reconcile,
  P32: one entry is listed. A shell's second add fails on the existing path, so one entry is the
  true record. Not a finding.
- Q7 (precedence of `br === null && branch !== null` in the `||` chain; a positional commit-ish
  holding an unknown variable) — checked at reconcile: `&&` binds before `||`, so line 368 reads
  as intended; the unknown commit-ish is dropped and counted, recorded as **CW8(b)**.

The sibling's re-run shows 105/105 on 2026-11-09; mine shows 111/111. The suite grew by six tests
with `50547442` and `1bc89816` after the brief was written; the delta's own tests are among both
counts. Not a discrepancy.

**Against the author's account** (the commit body of `03d8503d`, and the intent record):

- The motive holds: a queue run's own close listed 5 worktrees of 13 made through a literal
  loop, with nothing saying so. The delta builds both shapes the item names.
- "A loop over anything else leaves its variable unset, so the add is dropped as before and
  never guessed" — **CW2** and **CW5** stand against it as written: an unclosed loop expands a
  later add into guessed paths, and an arithmetic `for` is neither expanded nor dropped.
- "Tests: … add after the loop" — the shipped test covers the safe direction only (loop closed,
  variable unknown, counted); the unsafe one (CW2) has no test.
- "A -b branch (or commit-ish) holding an unresolvable variable now counts as unresolved too" —
  confirmed (P5b, P7); the body states the commit-ish case the CHANGELOG leaves out.
- The intent record's shape 1 wording, "N worktree adds not resolved (a variable with no
  literal assignment)", is where the render's parenthetical comes from; **CW6** stands: the
  causes grew and the sentence did not.
- Nothing in the body or the intent record addresses a loop whose result is an error, so
  **CW1** is not a point the author weighed and decided; it is unaddressed.

**Against the queue pointer:** its provenance matches act 1's (barred sessions, orchestrator,
tier, the drain order as the approval, the sibling held out of the worktree). Nothing to
reconcile.

**Overall line restated: FAIL — 1 MAJOR (CW1), 2 MODERATE (CW2, CW3), 3 minor (CW4, CW5, CW6),
2 notes (CW7, CW8).** Every finding is the principal's to decide (rule 3); nothing applied.

ACT 2 SAVED 2026-11-15 UTC.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`4a7b13a3` on `main`,
`dc243522` before the rebase); folded here verbatim (headings demoted two levels) and the sibling file
removed, per the brief. The orchestrator (a headless Opus 5.5 session started by drain session
`21a271a5`, itself Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ccclose-loop-worktrees-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

#### The brief-writer's own questions

1. `LOOP_CLOSE` and `LOOP_OPEN` are text patterns over the whole command: what do `git commit -m
"all done"`, `echo for you`, a heredoc body or a quoted word do to the depth count? Which direction
is the error: a false listing or a false drop?
2. A command that adds one worktree per word and fails on one of them: `resolvePending` works from
the whole command's result. Is an add that failed listed as made?
3. `break`, `continue` or an `if` guard in the loop body: is the add listed once per word although
the real loop did not run it for every word?
4. Nested literal loops multiply: is there a bound on the product, and what does a long word list
cost?
5. `dropped` counts a site once though several of its expansions may be dropped. What unit is "N
worktree adds", and does it match what the sentence tells the reader?
6. `site.includes(wtPath)` silently de-duplicates. Is that right when two words resolve to one path?
7. The operator precedence of `br === null && branch !== null` inside the `||` chain, and the case
of a positional commit-ish holding an unknown variable.

#### What the brief-writer ran, and what it got

- `ccclose`: Node 24: 105 tests, 105 pass, 0 fail, 284 s under load.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*The Fable 5.1 reviewer's own work log, kept while it ran and unread by any other session until
act 2 was saved; appended verbatim (headings demoted two levels). Form fixes only, if any, are
listed here: none beyond the heading demotion.*

### Work log — atelier 160/1010 cold pass (ccclose loop-made worktrees)

Reviewer: Fable 5.1 (claude-fable-5-1), spawned by a headless Opus 5.5 orchestrator under drain
session 21a271a5. Worktree: /Users/mike/worktrees/fable/atelier-160-1010-2141/atelier at
53f25fa4. Brief: docs/reviews/2026-11-09-0126-ccclose-loop-worktrees-cold.md. Sibling
`.deferred.md` absent from the worktree by design (git status shows ` D`); not sought.

#### Act 1

- 2026-11-15T21:43Z: started. uptime load 4.60. Read the brief in full (203 lines).
- Partition: I will not open docs/ROADMAP-DONE.md, docs/SESSIONS.md, docs/sessions/, other
  docs/reviews/ verdicts, the queue pointer 160/1010, the intent record 210/360 beyond its title,
  or any delta commit message body. Sweeps via tools/coldsweep.py.
- Tree check: `git merge-base --is-ancestor 03d8503d HEAD` exit 0. Later commits on the delta
  paths listed with the brief's `git log --oneline` line (subjects only; the list is long because
  CHANGELOG.md is a delta path). On `instruments/ccclose` since the delta: 50547442, 1bc89816,
  457f374d (non-goal), 4e3b3984 (non-goal).
- Read docs/method/REVIEW.md whole (698 lines): verdict shape, V1–V7, the method record rule.
- Read the delta body-free: `python3 tools/coldsweep.py --root <wt> --commit 03d8503d --path` x5.
  Subject, stat, diff only; coldsweep footer confirms the body was not printed and 3 board files
  were left out. I did not pass --path for any board file.
- Read at HEAD: instruments/ccclose 236–395 (shellWords, resolveFrom, WT_ADD, FOR_HEAD,
  LOOP_OPEN, LOOP_CLOSE, loopsAround, worktreeAdds), 540–572 (LITERAL_ASSIGN, assignmentsIn,
  expandVars), 715–855 (notePending, resolvePending, readTranscript loop), 1630–1670 (the second
  worktreeAdds call site in commitEvidence, stats discarded), 1802–1835 (identifiersWorktrees),
  1920–1941 (renderIdentifiers worktrees). instruments/ccclose.design.md 385–419; man/ccclose.1
  490–519; docs/method/RECORD.md 95–137 (the identifiers block); instruments/README.md 392–424;
  CHANGELOG entry at 1847. Intent record 210/360: first line only (title + state).
- Hook: .githooks/pre-commit runs tools/floor.py's registry; will run the gates on the brief at
  the end of the act.
- Re-run obligation: `cd <wt> && nice -n 10 node --test instruments/ccclose.test.js` → exit 0,
  tests 111, pass 111, fail 0, 143.7 s (21:47–21:49 UTC). Output kept in scratch only.
- Probes run on a scratch COPY of instruments/ccclose + cctranscript (scratchpad/probe/), via
  `node probe1.js`, `node probe2.js` (fixture transcripts through cc.readTranscript, deleted at the
  end of the run) and `/usr/bin/python3 -I probe3.py` (each timing case in its own node process,
  `nice -n 10`, 60 s timeout, 1.5 GB heap cap, smallest first, stop at first timeout).
  - P1a `for n in a b; do git commit -m "fix for $n"; done; git worktree add --detach /w/$n` →
    listed /w/a and /w/b, unresolved 0. Control P1b (no word "for" in the body) → listed none,
    unresolved 1. Cause: LOOP_OPEN counts the plain word " for " as an opener, the loop never
    closes (doneAt = Infinity), the add after `done` is read as inside the loop. Real shell makes
    /w/b only. A guessed path → candidate finding (acceptance standard: never guessed).
  - P1c `echo done` inside the body closes the loop early → the in-loop add after it is dropped
    and counted (safe direction). Not raised beyond the P1a finding's text.
  - P2 (readTranscript fixtures): A: loop of two adds, first fails, last succeeds, is_error
    false → BOTH listed, unresolved 0. B: first succeeds, last fails, is_error true → NOTHING
    listed, unresolved 0 (a made worktree dropped and not counted). C: single failed add →
    dropped, as before the delta. D: unresolved add with an error result → not counted. E: loop
    followed by `&& echo ok` → same as A. Cause: resolvePending gates the whole expansion on one
    tool_result's is_error and returns before counting. Candidate finding, the brief's named
    worst failure in both directions.
  - P3 FOR_HEAD timing, `for n in ` + N spaces, no `;`/newline before the add: N=1000 → 310 ms;
    N=4000 → 19.3 s; N=16000 → >60 s (timeout). Growth ≈ N³ (three overlapping whitespace
    consumers: `in\s+`, `[^;\n]*?`, `\s*`). With a `\ndo` present (spaces-done) every size ≤ 64000
    → 1 ms. ` \t` runs: 32 KB → 1.2 s (≈ N²). Candidate finding (lens 4, named in the brief).
  - P4 expansion: depth 3 × 10 words → 1,000 paths, 11 ms; 30 words → 27,000 paths, 1.3 s;
    60 words → 216,000 paths, >60 s timeout. Depth 4 × 10 → 10,000, 300 ms; × 20 → 160,000,
    timeout. Growth ≈ paths² from `site.includes(wtPath)` (array scan per path) plus a `cds`
    regex rerun and a Map copy per env. No cap on combinations. Candidate finding (minor).
  - P5 unit of the count: `for n in $(ls); do git worktree add …` → 1; `for n in a b c; do git
    worktree add -b $n-$X …` → 1 for three worktrees. The line says "N worktree adds"; a reader
    takes N as worktrees. Candidate (minor).
  - P7 `git worktree add /w/x $REF` ($REF unknown) → dropped, counted 1, though the path is
    known. Before the delta the branch was guessed as the basename. Note.
  - P7b `git worktree add /w/x origin/main` → branch "origin/main". git detaches at a non-branch
    commit-ish, so the branch field is wrong; pre-existing (not this delta). Note.
  - P30a `for ((i=0;i<2;i++)); do git worktree add --detach /w/$i; done` → listed /w/0 only,
    unresolved 0: FOR_HEAD does not match, LITERAL_ASSIGN reads `i=0` as an assignment, so one
    path is listed and the other dropped silently. Contradicts "a loop over anything else leaves
    its variable unset, so the add is dropped". Candidate (minor).
  - P30c `for n in ""` → /w/ listed; P6 `for n in a #b` → /w/#b listed (bash reads `#b` as a
    comment). Notes; contrived.
  - P8, P13, P26, P27, P28, P29, P30b, P30d, P30f, P30g, P31: all dropped and counted (safe).
    P28b, P29, P30e, P32: listed as a shell would. Not raised.
  - P24 `[ -d /w/$n ] && continue` in the body → all three listed; folded into the P2 finding
    (one result stands for many adds).
- Git fact check in a scratch repo (deleted after): branch `wt-a` pre-existing; `for n in a b; do
  git worktree add -b wt-$n ../wt-$n; done` printed `Preparing worktree (new branch 'wt-a')`
  then `fatal: a branch named 'wt-a' already exists`, made `wt-b`, `loop exit=0`. So
  "Preparing worktree" prints before a failure and is not a success mark; `fatal:` and
  `HEAD is now at` are the per-iteration marks.
- Other callers: `worktreeAdds`/`loopsAround` are used by instruments/ccclose only (two sites) and
  its tests; `spawnSync` is the git/gh wrapper; no transcript text is executed.
- Mirror sweep: `python3 tools/coldsweep.py --root <wt> --also-exclude <pointer> --also-exclude
  <intent record> 'worktree adds? not resolved|210/360|plain words \(no glob|loopsAround'` → 14
  hits over 841 files, 571 excluded as barred; all hits in the five delta files and the tests.
- 2026-11-15T22:0xZ: act 1 verdict appended to the brief below a `---` divider; Status line
  updated. Findings CW1 MAJOR (one result gates a loop's whole expansion; probes P2 A/B/E),
  CW2 MODERATE (quote-blind loop scanner; P1a/P1b/P1c), CW3 MODERATE (cubic FOR_HEAD; P3),
  CW4 minor (uncapped expansion, quadratic dedupe; P4), CW5 minor (arithmetic for; P30a), CW6
  minor (count unit and causes; P5a/P5b), CW7 note (prose understates the exclusion class;
  design.md indentation), CW8 note (pre-existing branch-field behaviour; P7/P7b). Overall FAIL.
- Gates run on the brief from the worktree: datescan exit 0 (clean), spellscan exit 0 (file is
  in .spellscanignore, scanned nothing), wrapscan exit 0 (in .wrapscanignore, scanned nothing;
  my own lines checked by awk: none over 100 columns after reflowing three tables to lists),
  reviewscan exit 0 (brief keeps deferred material in a sibling), attribscan exit 0, leakscan
  exit 0, linkscan exit 0 (no markdown links), pdlistscan tree-wide exit 0, pathscan 1 finding:
  the held sibling's path at brief line 166, expected until the fold.
- Scratch cleaned: probe copies, fixtures and the test-run capture removed.

#### Act 2

- 2026-11-15T22:1xZ: orchestrator released the sibling (act 1 committed as dc243522, brief file
  only). Read: the held sibling (7 brief-writer questions; its re-run: 105/105 on 2026-11-09),
  the delta's commit body (`git log -1 --format=%b 03d8503d`), the queue pointer 160/1010 whole,
  the intent record 210/360 whole. Did not open docs/SESSIONS.md, docs/sessions/,
  docs/ROADMAP-DONE.md or other verdicts: nothing in the reconcile needed them.
- Sibling Q1 ↔ CW2; Q2 ↔ CW1 (case A); Q3 ↔ CW1 (P24); Q4 ↔ CW4; Q5 ↔ CW6; Q6 (dedupe of two
  words to one path) checked: P32 lists one entry, a shell's second add fails on the existing
  path, so one entry is the true record; not a finding. Q7: `target === null || target === '' ||
  br === null && branch !== null` — `&&` binds before `||`, so the clause reads as intended
  (line 368); the unknown positional commit-ish case is CW8(b). No finding formed at reconcile.
- Test count 105 (sibling, 2026-11-09) vs 111 (mine): the suite grew with 50547442 and 1bc89816
  after the brief; not a discrepancy.
- 2026-11-15T22:06Z: `### Reconcile` appended beneath the act-1 verdict; act-1 text untouched;
  overall line restated FAIL (1 MAJOR, 2 MODERATE, 3 minor, 2 notes). Gates on the brief from the
  worktree: datescan, attribscan, leakscan, reviewscan, linkscan exit 0; pathscan 1 finding, the
  held sibling's path (expected until the orchestrator's fold); no line over 100 columns in the
  reconcile. No git write by me: status shows ` D` sibling (orchestrator's removal) and ` M` brief.
  Sibling not folded, nothing deleted; the fold is the orchestrator's.
