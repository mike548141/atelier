# Cold pass — git resolves a staged scan's positional scope, and an unknown one is refused (`160/950`, QS1 applied)

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** VERDICT 2026-11-15 UTC, both acts written under the principal's drain order of
2026-11-16 NZDT: PASS-WITH-FINDINGS, 0 MAJOR · 2 MODERATE · 3 minor · 4 notes, unchanged at
reconcile. The sibling and the review log are folded below the verdict; each finding awaits the
principal's decision.
**Sizing:** **large** — one commit, 850 lines across 21 files, the shared reader of every staged
guard, with scratch-repo probes to drive on macOS case and Unicode behaviour.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1070-rule-4-cold-pass-queued-git-resolves-the-staged-scope.md`.
**Why it earns a review:** Every staged guard in every child reads its scope through this function,
and a clean `--staged` exit is read as "nothing barred was staged". Worst failures: a staged secret
passes because a scope spelling reads as empty, or a refusal blocks a legitimate commit in a child
with no local way past it.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched, which wrote it (per the
  queue pointer). The author queued this pass and does not take it.
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
  that passes rule 4's criterion. **Barred from reviewing:** session `722ac2e2` and everything it
  started; session `84e3aa7f` (this brief-writer); session `74f2b8cd`. Whoever takes the pass states
  the spawn in the verdict (V7).
- **The principal's approval:** none yet for the pass. His request above covers this brief only. The
  pass waits for his explicit permission for Fable work.

⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):

- its dispatch text; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` whole; the
  house-form brief `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` through
  line 728, including its verdict (read for shape, another surface); the top of one sibling brief;
- the queue pointer whole; excerpts of the intent record: the lines naming the applied findings and
  the principal's answers, which include one-line summaries of the earlier verdict's findings;
- the delta body-free through `tools/coldsweep.py --commit 6467729f` (subject, stat, diff, never the
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

The principal's answers, as the intent record holds them (answers to options offered, not rulings in
his own words): *"Fix it + take advice"*, 2026-11-08, fixing the MAJOR the way the earlier pass
counselled (let git resolve the positional); and *"Keep it"*, 2026-11-09: every staged scanner
refuses a scope git does not know, the five others included, so a typo in a repo's settings fails
loudly instead of quietly checking nothing, and a declared directory with no tracked file is the
same case.

## What the work is

One commit on `main`, `6467729f` (first confirm your tree has it: `git merge-base --is-ancestor
6467729f HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 6467729f \
  --path tools/report.py \
  --path tools/secretscan.py \
  --path tools/leakscan.py \
  --path tools/conflictscan.py \
  --path tools/floor.py \
  --path tools/README.md \
  --path CHANGELOG.md \
  --path tools/test_report.py \
  --path tools/test_secretscan.py \
  --path tools/test_leakscan.py \
  --path tools/test_conflictscan.py \
  --path tools/test_floor.py \
  --path tools/test_pins.py \
  --path tools/test_allowmarker.py \
  --path tools/test_pathscan.py \
  --path tools/test_datescan.py \
  --path tools/test_reviewscan.py \
  --path tools/test_sizescan.py \
  --path tools/test_spellscan.py \
  --path tools/test_wrapscan.py
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 6467729f..HEAD -- tools/report.py tools/secretscan.py tools/leakscan.py tools/conflictscan.py tools/floor.py tools/README.md CHANGELOG.md tools/test_report.py tools/test_secretscan.py tools/test_leakscan.py tools/test_conflictscan.py tools/test_floor.py tools/test_pins.py tools/test_allowmarker.py tools/test_pathscan.py tools/test_datescan.py tools/test_reviewscan.py tools/test_sizescan.py tools/test_spellscan.py tools/test_wrapscan.py
```

## What the delta claims (extracted, not evaluated)

- `report.resolve_staged_scope` asks git what each positional names, as one literal root-anchored
  pathspec against the index and the commit's removals.
- A positional git does not know exits 2: a typo, the wrong case, a glob, an unexpanded `~`, a
  directory the repo lacks.
- `--root` must be the repo the process runs in; a subdirectory cwd of the same repo is fine.
- No declared scope changes behaviour, because the floor already skips a softenable check whose
  scope directory is absent.
- The five other scanners with a scope option refuse the same way.
- `test_pins.py`'s 600 s bound is a hang guard, not a memory test.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** The earlier pass's findings other than as this delta applies them. Later changes to
these files (`git log` below) only as far as they alter this delta's behaviour at HEAD.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. The boundary is staged-secret detection on every child's
hook. Check what an attacker or an accident can do with a positional, a git environment variable, a
symlink or a submodule. Fixtures are a privacy surface in this PUBLIC repo: build any live-shaped
secret at run time and quote none.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane hook --root .` and `--plane ci`
- `cd tools && python3 -m unittest test_report test_secretscan test_leakscan test_conflictscan test_floor`
- the staged-scope lines below, on a throwaway repo under your scratchpad

The scratch lines:

```
SCR=<scratchpad>/staged-scope; T=<your worktree root>; rm -rf "$SCR"; git init -q "$SCR"; mkdir "$SCR/docs"
python3 -c "open('$SCR/docs/x.md','w').write('<'*7+' a\nx\n'+'='*7+'\ny\n'+'>'*7+' b\n')"
git -C "$SCR" add docs/x.md
r() { ( cd "$SCR" && python3 "$T/tools/conflictscan.py" --staged --root . "$@" >/dev/null 2>&1 ); echo "scope[$*] exit $?"; }
r docs; r Docs; r nosuchdir/; r '*.md'; r .
( cd "$T" && python3 tools/conflictscan.py --staged --root "$SCR" docs >/dev/null 2>&1 ); echo "wrong-cwd exit $?"
mkdir "$SCR/docs/sub"; ( cd "$SCR/docs/sub" && python3 "$T/tools/conflictscan.py" --staged --root ../.. docs >/dev/null 2>&1 ); echo "subdir-cwd exit $?"
```

Reproduce the floor first with the full suite: `nice -n 10 python3 -m unittest discover -s tools`.
The brief-writer did **not** run that line, because the machine was at a load average of about 14
from other live sessions while it wrote this brief; the targeted lines above it did run.

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
verdict in `docs/reviews/`, The earlier verdict is
`docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md`,
`docs/reviews/2026-10-28-1255-staged-positional-reader-topup-cold.md`. the queue pointer above, this
brief's sibling (folded below the verdict; the `.deferred.md` file is removed), every
delta commit's message body, and the intent record
`docs/roadmap/160-doctrine-review-owed/950-rule-4-cold-pass-queued-staged-positional-reader.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred. This pass reviews the application of an earlier pass's findings, so the delta's own
text carries that verdict's finding identifiers and decision stamps: `REVIEW.md` § *Applying
decisions to doctrine* names this as a residual exposure that cannot be closed. Review the edited
text at HEAD and commit your findings first.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1070-rule-4-cold-pass-queued-git-resolves-the-staged-scope.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/950-rule-4-cold-pass-queued-staged-positional-reader.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`6467729f`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `GS`: `GS1`, `GS2`, …) and severities (MAJOR /
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

## Verdict — act 1, run 2026-11-15 UTC

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 4 notes.** The reader does what
it claims where it matters: git decides what a positional names, a case or Unicode variant, a
typo, a glob, an unexpanded `~` and a directory the repo lacks all exit 2 instead of reading
clean, and every name APFS can hold (quote, tab, backslash, space, NFC) matches under a scope.
The findings are on the record's claims about the edges, on a refusal message that misdiagnoses
the one case the ruling accepted, and on five scanners the documentation covers but the code
does not.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. One subagent started for this pass alone.
- **Spawn chain:** headless orchestrator session `12fb7359` (Opus 5.5), itself started by drain
  session `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context
  partition, form no finding and write no severity. Neither wrote the brief or the delta. I was not
  started or instructed by `722ac2e2` or anything it started, `84e3aa7f` or `74f2b8cd`.
- **The principal's approval:** his `/fable-drain` invocation of 2026-11-16 06:53 NZDT, which the
  skill names as his order to drain the weekly budget. That is the approval this brief's Status
  line awaited.
- **Spawn prompt, as received (process only):** who I am and where (worktree path, brief path,
  scratchpad path); the partition (sibling removed from the worktree; do not look for it; use
  `coldsweep`); load rules (`uptime` first, `nice -n 10`, one suite at a time, single process,
  full suite only under load 12); the Python to use; live-system rules (read-only, no writes,
  allowlist fields, no secrets); what I may write (this file below a divider, and a work log at
  `~/.claude/fable-drain/notes/atelier-160-1070-2150.md`); no git command that writes; refer to
  orchestrators by session id only, no private names; how to finish each act. It carried no
  question about the delta, no pointer to where the risk lives and no request about any finding.
  Its full text is in the orchestrator's session record under the id above.
- **Release message:** none yet; act 2 waits on it.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1070-2150/atelier` at `eb13bf22`, read-only
  to me except this file. Scratch repos under my session scratchpad, deleted at the end of the act.
- **Contact:** none with the author, the brief-writer or `74f2b8cd`.

**What I read.** This brief whole; `docs/method/REVIEW.md` lines 25–300 and 302–460; the delta
through `coldsweep --commit 6467729f` with the brief's twenty `--path`s (subject, stat, diff; no
message body); at HEAD, `tools/report.py` 277–300, 330–560, 683–760 and 790–900, the staged
branches of all eight scanners and `attribscan`, `tools/floor.py` 2402–2425 and 2798–2840,
`tools/pre-commit.sample`, `tools/README.md` 612–632 and 2488–2505, `CHANGELOG.md` 1496–1524 (the
2026-11-09 entry),
`docs/build/templates/CONTRIBUTING.md` 78–96; `git log --oneline 6467729f..HEAD` on the twenty
paths (about 95 subjects, none an account of this delta beyond its own subject) and `git diff
6467729f HEAD -- tools/report.py`; `git diff-tree --name-only` for the commit (21 names).

**Disclosed exposure.** (1) The commit also touches
`docs/roadmap/115-guardrail-architecture-mike-commissioned/360-…md`; I did not open it. (2) A
`coldsweep` mirror sweep on the new wording returned one line of the queue pointer
`docs/roadmap/160-doctrine-review-owed/998-rule-4-cold-pass-queued-merge-hook-and-staged-content-scanners.md`,
and I then read that pointer's lines 1–12 and 44–58. It is not on this brief's barred list, but it
carries another pass's verdict summary (HS1–HS10 with severities), and its HS2 names the same
defect as my GS1. I read it **after** the probe that formed GS1 (the log holds the order); it
changed no severity here, and GS1 cites it so the principal rules once. (3) The harness loaded
user-level and repo instruction files and a memory index that hold private context this brief
does not carry. (4) The worktree showed the sibling as a deletion; I did not look for its content.
`--include-barred` was not used.

### Lens 1 — approach and assumptions

The problem is the right one and solved at the right altitude: the floor's `exists()` is the
filesystem's word, the guards' positionals are git's, and only git can say what a positional
names in the index, so the reader asks git. One literal, root-anchored pathspec per positional,
against `ls-files` plus the commit's removals, is the smallest honest question. The refusal for an
unknown positional is a design choice the principal made ("Keep it"), not the author's; I review
its edges, not the choice.

Load-bearing assumptions, named before any probe, then driven:

- **A1** `ls-files` + `diff --cached --diff-filter=D` under one literal top-anchored pathspec
  enumerate exactly what a positional names. **Confirmed:** directory prefix stops at `/`
  (`src` never reaches `src-extra`), a removed subtree resolves, a rename resolves under both
  names, an unborn HEAD works (`diff --cached` exits 0 on the brief's scratch repo).
- **A2** The staged dict's keys (parsed from the diff header, `unquote_c`) and `nul_paths`'s
  output spell a path identically, else a scoped scan drops a file silently. **Confirmed for every
  name APFS can hold:** quote, tab, backslash, space and NFC `é` each match under `docs` and under
  their exact name. **Open for one case I could not build here:** a non-UTF-8 name (GS6).
- **A3** `refuse_other_repo` compares two `rev-parse --show-toplevel` answers under the same
  environment, so anything that moves both passes it. **Damaged:** `GIT_DIR`+`GIT_WORK_TREE`
  naming another repo passes the check and the scan reads that repo's index (GS4).
- **A4** "No declared scope is turned away" rests on the floor's filesystem `exists()` agreeing
  with git's view. **Damaged:** a directory present on disk with no tracked file passes the floor
  and is refused by the guard, for an enforced and a softenable check alike (GS2, GS3).
- **A5** Only the three boundary guards call `refuse_other_repo`, though the README names eight.
  **Confirmed:** five scanners pass clean over another repo's index (GS1).
- **A6** `GIT_LITERAL_PATHSPECS=0` plus `:(top,literal)` neutralises environment and magic in a
  positional. **Confirmed:** `:docs`, `:(glob)docs/*`, `:/docs` are read literally and refused;
  the suite's `ICASE`/`GLOB` env test holds.
- **A7** The 600 s bound is a test-only hang guard. **Confirmed** by reading; its grounding is one
  observation (GS9).

### Lens 2 — correctness and quality

Every re-run line reproduces (ledger below). The reader at HEAD is byte-identical to the delta but
for `note_empty_scope` (RT2, `160/730`), which adds a stderr line and changes no exit code.
Overclaims, each against the text that makes it: CHANGELOG 1511–1512 "The floor never hands the
guards a missing directory (it blocks first), so no declared scope is turned away" and 1517–1519
"The floor already skips a softenable check whose scope directory is absent, so no declared scope
changes behaviour", the reader's docstring "so no floor invocation is turned away by this" (GS2);
README 2497–2500 "These exit 2: … a `--root` that is not the repo the process runs in" said of
eight scanners (GS1); README 2500 and the `refuse_other_repo` docstring "the staged diff is always
the current directory's" (GS4). The brief's own claim list repeats the first two as claims; the
brief said to treat it as attackable, and it was (GS8).

### Lens 3 — completeness and harvest

V3 mirror sweep (`coldsweep`, barred paths excluded): the new wording lives in `tools/README.md`
(two places) and `CHANGELOG.md`; the child-facing `CONTRIBUTING.md` template shows a `scope.paths`
example and says nothing of the spelling rule that now blocks a child's commit (GS5). V4: one home
for the reader (`report.resolve_staged_scope`); the three guards' comments point at it rather than
restating it. Tests that would stay green on a broken change: removing `refuse_other_repo` from any
of the five other scanners reds nothing (GS1 is the live proof); the rest of the reader's branches
each have a test that reds on removal (`--diff-filter=D`, the env drop, the unknown refusal, the
prefix boundary, the subdirectory cwd). `test_the_spelling_is_normalised_as_posix_whatever_the_host`
pins source text, not behaviour, and says why (GS9).

### Lens 4 — security and privacy (V6)

Boundary: staged-secret detection on every child's hook. Positional: magic prefixes, `..`,
absolute paths, globs, `~`, empty string (`""` reads as the whole diff, the safe direction) all
probed; none widens or silently narrows the scan. Git environment: `GIT_LITERAL_PATHSPECS`,
`GIT_GLOB_PATHSPECS`, `GIT_ICASE_PATHSPECS` neutralised (suite); `GIT_INDEX_FILE` pointing at a
foreign index fails closed (exit 2); `GIT_DIR`+`GIT_WORK_TREE` naming another repo passes the QS3
check and the scan reads that repo (GS4, a hand-run shape, not the hook's). Symlink: a scope under
a tracked symlink names nothing git lists and is refused; the index holds no file under it.
Submodule: the gitlink path resolves and its "Subproject commit" line is scanned like any other.
Fixtures: the delta assembles its secret shapes at run time and quotes none; my probes planted
conflict markers, never a key. `/security-review`: **NOT RUN**, discharged by grounds: it reads the
session's pending diff, which in this worktree is the deleted barred sibling, so running it would
feed that file's removed lines to this reviewer; and the delta is landed, so there is no pending
diff of the work to aim it at.

### Standing checklist

- **V1** Three claims stronger than their evidence (GS1, GS2, GS4); the rest hold under re-run.
- **V2** Every re-run line re-run; the ledger below. Nothing was taken on reading.
- **V3** One mirror site unswept: the child `CONTRIBUTING.md` template (GS5).
- **V4** Holds: one reader, one home, stamped pointers in the guards.
- **V5** One contradiction: README names eight scanners for a refusal three implement (GS1).
  Cross-references checked for the rule reached: `tools/README.md` 2490–2504 reaches
  `resolve_staged_scope` and describes its refusals (one false, GS1); CHANGELOG 1496 reaches
  `115/360` and `160/950` by number only (the latter barred here, so not followed).
- **V6** Worked above; the scanner discharged with grounds.
- **V7** Stated above; the brief states it too.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `6467729f` | yes (`coldsweep --commit`, twenty `--path`s; one board item left out) | GS1–GS9 |

### Findings

**GS1 — MODERATE.** `tools/README.md` 2490–2500 names eight staged scanners and says of them
"These exit 2: … a `--root` that is not the repo the process runs in"; CHANGELOG 1520–1521 states
the rule under the same heading. Only `secretscan`, `leakscan` and `conflictscan` (and the later
`attribscan`) call `report.refuse_other_repo`. Probe, cwd the worktree and `--root` a scratch
repo with five staged files, positional `docs`: `secretscan` exit 2 with the QS3 text;
`datescan`, `spellscan`, `wrapscan`, `sizescan`, `reviewscan` each exit 0 "clean" over the
worktree's index with the coverage line "scanned nothing". The five are softenable checks and the
hook always runs them with cwd = root, so the live exposure is a hand run; the record's claim is
the defect. **Already before the principal** as `998`'s HS2 (the code half; disclosed above).
*Counsel:* rule once with HS2. Either way the README sentence must match the code: add the call to
the five (one line each, as `attribscan` has) or narrow the sentence to the three guards.

**GS2 — MODERATE.** The record says no declared scope is turned away: CHANGELOG 1511–1512 ("The
floor never hands the guards a missing directory (it blocks first), so no declared scope is turned
away"), 1517–1519 ("The floor already skips a softenable check whose scope directory is absent, so
no declared scope changes behaviour"), and the reader's docstring, `tools/report.py` 410 ("so no
floor invocation is turned away by this"). Probe, floor hook plane on a scratch repo:
`.atelier-floor.json` scope
`secretscan` → `["present-untracked"]`, a directory present on disk holding one untracked file,
commit staging `src/a.py`: floor exit 1, `secretscan` state `enforced` rc 2, "name nothing git
knows". Same config on `datescan` (softenable): state `enforced` rc 2, floor exit 1 — not
skipped, blocking. The acceptance test names this very case as accepted ("a declared directory
with no tracked file is the same case"), so the behaviour is per the ruling; the three surfaces
that say it cannot happen are wrong, and the softenable half ("skips") is true only for a
directory absent from disk. *Counsel:* say what is true on all three: "a declared directory with
no tracked file is refused at the hook, enforced or softenable, by the ruling of 2026-11-09".

**GS3 — minor.** The refusal's remedy misdiagnoses the case GS2 drives: "Spell it as git does:
repo-root-relative, exact case, no glob or '~'. Pass e.g. 'src/' instead." For a directory that
exists with no tracked file the spelling is right; the fix is to track a file under it or change
the `scope` entry in `.atelier-floor.json`, which nothing in the four lines names, and on the hook
plane the floor adds no line of its own for an rc 2 (probe stderr: the guard's four lines, then
the next check). This is the brief's second worst case, "a refusal blocks a legitimate commit in a
child with no local way past it", by message rather than by mechanism. *Counsel:* one more clause
in the refusal ("or the path holds no tracked file") and, on the hook plane, the floor naming
`.atelier-floor.json` beside an rc 2 as it does for its own missing-directory block.

**GS4 — minor.** `refuse_other_repo` compares `git rev-parse --show-toplevel` run in the cwd with
the same run under `-C <root>`; both honour `GIT_DIR`/`GIT_WORK_TREE`, so an environment naming
another repo moves both and the check passes. Probe, cwd and `--root` both the worktree,
`GIT_DIR`/`GIT_WORK_TREE` the scratch repo: no refusal, exit 1 with the scratch repo's findings
read under the worktree's rules. The docstring and README 2500 say "the staged diff is always the
current directory's", which is not so under `GIT_DIR`. Not the hook's shape (git's own commit
targets the environment's repo, and the hook's `repo_root` follows it), so a hand-run exposure.
`GIT_INDEX_FILE` to a foreign index fails closed (exit 2). *Counsel:* say "the repo git's
environment selects, normally the current directory's" in both places; a stricter check is not
worth breaking the hook under a legitimate `GIT_DIR`.

**GS5 — minor (V3).** `docs/build/templates/CONTRIBUTING.md` 78–91, the one surface a child
contributor reads about `scope.paths`, shows `"paths": ["src"]` and says nothing of the rule the
delta turned on for every child: a path in git's own spelling and case, refused at the hook
otherwise. The README's "Wiring it in" gained the clause; the template did not. *Counsel:* one
clause after the example.

**GS6 — note.** `parse_added_lines` decodes a header path with `errors="replace"` (U+FFFD) and
`nul_paths` with `os.fsdecode` (surrogate escapes), so a non-UTF-8 filename would key `staged` and
`allowed` differently and drop out of a scoped scan silently; `note_empty_scope` speaks only when
every file dropped. Reasoned from the code, not probed: APFS refuses such a name, and no Linux host
was available. Unscoped runs are unaffected. *Counsel:* decode the header path with
`surrogateescape` too, or state the residual beside `nul_paths`.

**GS7 — note.** `_git_scope_names` reports a failed `git ls-files` through `git_diff_failed`, so
the line reads "git diff failed: …" for a command that was not a diff; the test pins that text.
Message accuracy only.

**GS8 — note, on the brief.** "850 lines across 21 files" counts the barred board item; the twenty
reviewable files are 827 insertions and 146 deletions. The barred list's sentence is broken ("every
prior verdict in `docs/reviews/`, The earlier verdict is … . the queue pointer above"), though
every path is present. The brief's claim list repeats the delta's overclaims (GS2) as claims, which
is its stated role.

**GS9 — note.** The 600 s hang guard in `test_pins.py` is grounded in one observation (one
loaded run, "load 14-53", about 1200 s for the suite); fine for a hang guard, and the comment says
what it is. `test_the_spelling_is_normalised_as_posix_whatever_the_host` pins the source text
(`posixpath.normpath` present, `os.path.normpath` absent) rather than behaviour, which on a POSIX
host is indistinguishable; the docstring says so. Both accepted as written.

### Re-run ledger

All from the worktree root unless said, `python3` = 3.14.6 on PATH, under `nice -n 10`, one at a
time, in the foreground; load average 3.1–4.4 at each start.

| Line | Result |
|---|---|
| `floor.py --plane hook --root .` | exit 0 |
| `floor.py --plane ci --root .` | exit 0 |
| `cd tools && python3 -m unittest test_report test_secretscan test_leakscan test_conflictscan test_floor` | Ran 1147 tests in 239 s, OK, exit 0 |
| Scratch lines (unborn HEAD, `docs/x.md` staged) | `docs` 1 · `Docs` 2 · `nosuchdir/` 2 · `*.md` 2 · `.` 1 · wrong-cwd 2 · subdir-cwd 1 |
| `python3 -m unittest discover -s tools` (full suite) | Ran 3134 tests in 793 s, OK, exit 0 (load 4.4 at start) |

Extra probes (not in the brief): special-character names under a scope; five scanners with a
foreign `--root`; floor hook plane with an on-disk untracked scope directory, enforced and
softenable; magic-looking positionals; case-variant `--root` (passes, git canonicalises);
`GIT_DIR`/`GIT_WORK_TREE`; `GIT_INDEX_FILE`. Commands and outputs are in the work log.

### Follow-up checklist (the principal's to rule; nothing applied)

- [ ] GS1 with `998` HS2: add `refuse_other_repo` to the five, or narrow README 2497–2500.
- [ ] GS2: correct CHANGELOG 1511–1512 and 1517–1519 and `report.py` 410 to the ruling.
- [ ] GS3: the refusal names the untracked-directory case and, on the hook plane, the config file.
- [ ] GS4: docstring and README say "the repo git's environment selects".
- [ ] GS5: one clause in the `CONTRIBUTING.md` template after the `scope` example.
- [ ] GS6, GS7: as counselled, or record as accepted residuals.
- [ ] GS8, GS9: no action unless he wants the brief's figures corrected at the fold.

### Reconcile

Act 2, 2026-11-15 UTC, after act 1 was committed as `aa68389e`. Read for the first time: the held
sibling; the queue pointer `160/1070`; the intent record `160/950` whole; the commit body of
`6467729f`; the prior verdicts `docs/reviews/2026-10-26-0912-staged-positional-reader-cold.md`
(QS1–QS11) and `docs/reviews/2026-10-28-1255-staged-positional-reader-topup-cold.md` (QU1–QU3);
the board item `115/360` the commit touched, through `git show` of that one path. Not opened:
`docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, nothing there bore on a finding.
No act-1 text is revised; the overall line stands.

**Against the sibling's questions.** The pointer asked whether any spelling still lets a staged
secret past (symlinks, submodules, a scope naming a removed directory) and whether refusing an
unknown scope can strand a child. Act 1 answered the first for symlinks, submodules, special
characters, magic prefixes and environment variables, and the second with the probe behind GS2.
The brief-writer's seven questions, against act 1 and against five further probes run at reconcile
(a scratch repo, deleted after): (1) answered by GS2 and GS3, and the cost to a child is one
blocked commit with a message that points at the spelling; (2) a commit that moves every file out
of a scope directory, rename detection on by default: `--no-renames` on the removals read lists the
old paths as `D`, so the old scope resolves (exit 0, nothing added under it) and the new one scans
(exit 1 on the planted marker), no refusal; (3) an intent-to-add entry resolves and its content is
absent from `diff --cached`, as it is absent from the commit; a gitlink positional resolves to
itself; a tracked symlink resolves to itself and a path under it is refused, as act 1 said;
unmerged entries and sparse checkout were not driven; (4) with `core.precomposeunicode=true`,
this platform's default, an NFD positional resolves (exit 1 on the planted marker); with it
`false` the same positional is refused (exit 2): never clean, which is the property the tests
pin, and a Linux CI run meets the refusal only on a hand-typed NFD spelling, since the floor
renders what the config holds; (5) answered under lens 4 (`:docs`, `:(glob)docs/*`, `:/docs`
refused); (6) run, and it formed GS1; (7) the brief's scratch lines run on an unborn HEAD and
act 1 recorded `diff --cached` exiting 0 there.

**Against the author's account.** The commit body says the reader "closes QS1 and QS2 together"
and lists QS3–QS11, QU1 and QU3 as applied as counselled; the intent record's APPLIED entry adds
two calls it put to the principal, that the five other scanners refuse an unknown scope too and
that "a declared scope directory that exists but holds no tracked file now blocks the commit
(exit 2)", and his answer "Keep it". That changes the reading of GS2 but not its text: the
behaviour was disclosed to him on the board before he answered, so the gap is not an uninformed
ruling; it is that the CHANGELOG, the public record a child reads, and the reader's docstring
state the opposite of what he was told and accepted. GS2 stands at MODERATE on that ground.

**Per finding.**

- **GS1** — the prior pass's QS3 counselled "refuse when the cwd's `rev-parse --show-toplevel` is
  not `root`"; the commit body claims QS3 applied and the README generalises it to eight
  scanners. The code applied it to three. `998`'s HS2 has the code half before the principal
  (its pointer's summary says so; its brief was not opened). Stands.
- **GS2** — see above. The prior QS2 held that the floor "blocks or skips first"; the sibling's
  first question suspected the same gap act 1 drove. Stands, MODERATE, on the record's text.
- **GS3** — new to this pass; no prior finding touches the refusal's wording for the untracked
  directory. Stands.
- **GS4** — the prior QS3 reproduced the cwd shape only; the sibling's fourth question asked
  about `GIT_DIR` on hooks. In the hook a set `GIT_DIR` names the committing repo, so both halves
  of the check move together and correctly; the hand-run exposure stands as minor.
- **GS5** — the prior QS5/QS6 swept `floor.py` comments and the README; neither named the child
  `CONTRIBUTING.md` template. Stands.
- **GS6, GS7, GS9** — not in any prior finding; stand as notes. GS9's second half is the prior
  QS10's `posixpath` counsel as applied; the text-pinning test is the author's choice, accepted.
- **GS8** — the brief-writer's own re-run ledger in the sibling matches act 1's exactly (the
  seven scratch exits, floor hook and ci exit 0); its full-suite count (1019 tests) is of the
  four delta modules, not the suite. Stands as a note on the brief.

No finding was formed at reconcile. The brief-writer's floor note (three warn-only `pathscan`
findings at `c132cc1c`) is outside this delta and was not pursued.

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 4 notes.**

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`aa68389e` on `main`);
folded here verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (headless Opus 5.5 session `12fb7359`, started by drain session `21a271a5`, itself
Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-git-resolved-staged-scope-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

#### The queue pointer's questions (author-written, verbatim)

> whether any spelling still lets a staged secret past (symlinks, submodules, a scope naming a
removed directory); whether refusing an unknown scope can strand a child.

#### The brief-writer's own questions

1. "A declared directory with no tracked file is the same case" sits beside the changelog's "no
declared scope changes behaviour". A directory that exists on disk but tracks nothing passes the
floor's `exists()` and then exits 2. Is the changelog's sentence true, and what does it cost a
child?
2. A commit that moves every file out of a scope directory: rename detection is on by default, so
`--diff-filter=D` does not list the old paths. Is the scope then refused, blocking a legitimate
move?
3. Unmerged index entries, `git add -N`, sparse-checkout, a gitlink positional, a tracked symlink:
what does `ls-files` answer for each?
4. Hooks set `GIT_DIR`, and `core.precomposeunicode` makes macOS normalise argv while Linux does
not. Does a scope resolve on the hook and refuse in CI, or the reverse?
5. `GIT_LITERAL_PATHSPECS="0"` and the magic prefix: what does a positional beginning with `:` do?
6. Run the five other scanners' refusals, not only the three staged-diff guards.
7. The first commit of a repo, with no `HEAD`.

#### What the brief-writer ran, and what it got

- `gs_tests`: python3 3.14: 1019 tests OK, exit 0, 417 s under load.
- `p1070`: scope docs: exit 1 (marker found). Docs: 2. nosuchdir/: 2. '*.md': 2. '.': 1. wrong cwd:
  2. subdirectory cwd: 1.
- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Headings demoted two levels; otherwise as the reviewer wrote it.*

### Review log — atelier 160/1070, git-resolved staged scope cold pass

Reviewer: Fable 5.1 subagent, spawned by headless orchestrator 12fb7359 (Opus 5.5), itself
started by drain session 21a271a5 (Opus 5.5). Worktree:
/Users/mike/worktrees/fable/atelier-160-1070-2150/atelier at eb13bf22. Act 1 entries are written
before the sibling .deferred.md is released.

#### Act 1

- 2026-11-15T21:52Z `date -u`; `uptime` load 4.33/4.93/6.13. `git merge-base --is-ancestor
  6467729f HEAD` exit 0 (delta present). `git status --short` shows only the sibling deleted.
  python3 on PATH = 3.14.6.
- Read the brief in full (docs/reviews/2026-11-09-0126-git-resolved-staged-scope-cold.md, 244 lines).
- Read docs/method/REVIEW.md: lines 25-300 (rules 1-4), 302-460 (lenses, re-run rule, V1-V7).
- `tools/coldsweep.py --help`; then the brief's `--commit 6467729f` line with its 20 `--path`s,
  saved to scratch `reviewer/delta.diff` (1575 lines) and read in full. The commit's message body
  was not printed. `git diff-tree --no-commit-id --name-only -r 6467729f` lists 21 files: the 20
  in the brief plus the board item `docs/roadmap/115-.../360-...md`, which the brief bars until
  phase 2 and which I did not open. Stat: 827+/146- over 20 files (the brief's "850 lines across
  21 files" counts the board item).
- Lens 1, assumptions named before any probe: (A1) `ls-files` + `diff --cached --diff-filter=D`
  under one literal top-anchored pathspec enumerate exactly what a positional names; (A2) staged
  dict keys (diff-header parse) and `nul_paths` output spell a path identically, else a scoped
  scan drops files silently; (A3) `refuse_other_repo` compares two `rev-parse --show-toplevel`
  answers, so anything that moves both (GIT_DIR) passes it; (A4) the claim "no declared scope is
  turned away" rests on the floor's filesystem `exists()` agreeing with git's view; (A5) only the
  three boundary guards call `refuse_other_repo`, though the README names eight; (A6)
  `GIT_LITERAL_PATHSPECS=0` plus `:(top,literal)` neutralises env and magic in a positional;
  (A7) the 600 s hang guard is a test-only bound.
- `git log --oneline 6467729f..HEAD -- <20 paths>`: ~95 later commits on these paths. `git diff
  6467729f HEAD -- tools/report.py` on scope lines: only `note_empty_scope` (RT2, 160/730) was
  added to `scope_staged`; `resolve_staged_scope`, `restrict_to_scope`, `refuse_other_repo` are
  byte-identical to the delta. Read tools/report.py 330-560 at HEAD (the reader), 683-760
  (`unquote_c`, `diff_header_path`, `nul_paths`), 790-900 (`STAGED_DIFF_CMD`, `parse_added_lines`),
  277-300 (`staged_added_by_path`, `staged_paths`).
- grep callers: `refuse_other_repo` is called by secretscan:2013, leakscan:3222, conflictscan:733
  and attribscan:457 only. datescan:932, spellscan:831, sizescan:1147, reviewscan:759,
  wrapscan:705 call `scope_staged` and never `refuse_other_repo` (read each staged branch).
- Read tools/floor.py 2402-2425 (`_render` staged branch), 2798-2840 (missing-scope block and
  guard invocation: `subprocess.run(argv)` with no `cwd=`, so the guard inherits the floor's
  cwd), tools/pre-commit.sample (runs `floor.py --plane hook --root "$repo_root"` from the hook's
  cwd, which git sets to the top level). Read tools/README.md 2488-2505 and 615-630 at HEAD.
- PROBE brief scratch lines (scratch repo, unborn HEAD, `docs/x.md` staged with a conflict
  marker): docs=1, Docs=2, nosuchdir/=2, '*.md'=2, .=1, wrong-cwd=2, subdir-cwd=1. All as the
  brief's claims predict. `core.ignorecase=true` on this APFS volume; `git ls-files --
  ':(top,literal)Docs'` prints nothing, `docs` prints `docs/x.md`: git's pathspec match is
  case-exact despite the filesystem. `git diff --cached --diff-filter=D` on an unborn HEAD exits 0.
- PROBE A2 (scratch `special`): staged files named with `"`, TAB, backslash, space and NFC é,
  each holding a conflict marker. conflictscan `--staged` with scope `docs` and with each exact
  file name exits 1 and names every file; `""` and `docs/` read as the whole diff (exit 1);
  `untracked-only` (a directory present on disk, nothing tracked) exits 2 with the "name nothing
  git knows ... Spell it as git does" text. A2 holds for every name APFS can hold.
- PROBE A5 (cwd = worktree, `--root` = scratch repo with 5 staged files, positional `docs`):
  secretscan exit 2 with the QS3 refusal; datescan, spellscan, wrapscan, sizescan, reviewscan
  each exit 0 "clean" with the coverage line "scanned nothing" (they read the worktree's index
  under the scratch repo's rules). README 2497-2500 says all eight exit 2 on that `--root`.
- PROBE A4 (scratch `hook`, floor hook plane, `--tools` = worktree tools): `.atelier-floor.json`
  scope secretscan -> ["present-untracked"] (dir exists on disk, only an untracked file; commit
  stages `src/a.py`): floor exit 1, secretscan state enforced rc 2, stderr "name nothing git
  knows: present-untracked". Same with datescan (softenable): state enforced rc 2, floor exit 1.
  So a declared on-disk directory with no tracked file IS turned away at the hook, for enforced
  and softenable checks alike, and the remedy text says to fix the spelling.
- PROBE A6/lens 4: positionals `:docs`, `:(glob)docs/*`, `:/docs` exit 2 (treated literally,
  unknown); `docs/..` and `./` read as the whole diff. `--root` spelt with a case variant of the
  real path passes (git canonicalises the case). GIT_DIR+GIT_WORK_TREE pointing at the scratch
  repo with cwd and `--root` both the worktree: `refuse_other_repo` passes (both toplevels resolve
  to the env repo) and the scan reads the scratch index under the worktree's rules, exit 1 with
  the scratch findings. GIT_INDEX_FILE pointing at another repo's index: git diff fails, exit 2.
- Mirror-site sweep with coldsweep (pattern on the new wording and `refuse_other_repo`): hits in
  CHANGELOG.md:1504,1520, tools/README.md:2492, the 115/360 item (not opened) and the queue
  pointer `docs/roadmap/160-doctrine-review-owed/998-...md:51`. DISCLOSED: I opened that pointer
  (lines 1-12, 44-58; it is not on this brief's barred list) AFTER the A5 probe above, and it
  carries another pass's verdict summary (HS1-HS10 with severities); its HS2 names the same five
  readers skipping `refuse_other_repo`. My GS finding on that was formed from the probe first;
  the pointer tells me it is already before the principal, so the finding cites it.
- Lens 4 `/security-review`: NOT RUN, discharged by grounds: it reads the session's pending diff,
  which in this worktree is the deleted barred sibling; running it would feed that file's
  removed lines into this reviewer. The lens was worked by hand with the probes above.
- Read tools/README.md 612-632 ("Wiring it in" at HEAD: carries the git-spelling clause) and
  docs/build/templates/CONTRIBUTING.md 78-96 (the child template's `scope.paths` example; no
  spelling clause). grep of docs/method/GUARDS.md, docs/build, skills for scope semantics: the
  template line 87 is the only mirror site outside tools/ and CHANGELOG.
- Hook-probe stderr read in full: on an rc 2 the floor prints only the guard's four lines and
  moves to the next check; nothing names `.atelier-floor.json` (the floor's own missing-directory
  block does). The JSON result for the refused check carries `reason: ''`.
- Tests, foreground, `nice -n 10`, single process, load 3.1 at start: `cd tools && python3 -m
  unittest test_report test_secretscan test_leakscan test_conflictscan test_floor` -> Ran 1147
  tests in 239.185s, OK, exit 0. `git status --short` after: only the sibling deletion.
- `floor.py --plane hook --root .` exit 0 (load 3.9); `floor.py --plane ci --root .` exit 0
  (load 4.4). Worktree unchanged after both.
- Full suite `python3 -m unittest discover -s tools` started under nice at load 4.4 (< 12), single
  process, output to scratch `reviewer/fullsuite.txt`; result recorded below when it finishes.
- Drafted the verdict (GS1-GS9: 0 MAJOR, 2 MODERATE, 3 minor, 4 notes) in scratch
  `reviewer/verdict-draft.md`; to be appended to the brief below a `---` once the suite line is
  known, then the repo gates run on the brief.
- Scratch repos `staged-scope`, `special`, `hook` deleted after their probes; the text outputs
  (delta.diff, targeted.txt, floor-*.txt, fullsuite.txt, verdict-draft.md) deleted at the end of
  the act.
- Full suite result: `Ran 3134 tests in 792.875s`, `OK`, exit 0 (another pass's full suite ran on
  this machine at the same time; load 4-8 throughout).
- Verdict appended to the brief below a `---` (259 lines: provenance, lenses, V1-V7, assumptions
  A1-A7, per-commit ledger, GS1-GS9, overall PASS-WITH-FINDINGS 0/2/3/4, re-run ledger, follow-up
  checklist); Status line set to ACT 1 WRITTEN 2026-11-15 UTC. Quoted line numbers re-pinned by
  grep before the append (CHANGELOG 1511-1512, 1517-1519, 1520-1521; README 2497-2500; report.py
  410).
- Gates on the brief from the worktree, each exit 0: datescan, spellscan, wrapscan (85 and 100),
  linkscan, leakscan, reviewscan, secretscan. Lines over 100 characters in the verdict: one path
  (line 295) and three table rows (485-487), no prose.
- Scratch text outputs deleted. Worktree after act 1: the brief modified, the sibling deleted,
  nothing else. ACT 1 SAVED 2026-11-15 ~22:25 UTC.

#### Act 2 (released by the orchestrator after act 1 was committed as aa68389e)

- Release message received: read the held sibling at ~/.claude/fable-held/atelier--2026-11-09-0126-git-resolved-staged-scope-cold.deferred.md
  and the records the brief bars until phase 2; append `### Reconcile` only; no fold, no delete.
- Read: the sibling whole; queue pointer 160/1070 whole; intent record 160/950 lines 25-45 and
  83-112 (prior pass summary, the APPLIED entry with its two calls to the principal, his two
  answers); `git log -1 --format=%B 6467729f` (commit body); board item 115/360's hunk via
  `git show 6467729f -- <that path>`; prior verdicts' finding headers (0912: QS1-QS11, lines
  404-479, 655-662; 1255: QU1-QU3, lines 375-529) and QS2/QS3 text (0912 lines 423-444). Not
  opened: ROADMAP-DONE.md, SESSIONS.md, docs/sessions/.
- Reconcile probes (scratch `recon`, deleted): full move of a directory with rename detection on
  -> old scope exit 0, new scope exit 1 (no refusal); `git add -N` directory -> exit 0;
  gitlink positional `sub` -> ls-files lists `sub`, exit 0; tracked symlink `lnk` -> exit 0,
  `lnk/x` -> exit 2; NFD positional with core.precomposeunicode=true -> exit 1, with =false ->
  exit 2.
- Intent record 950 shows the author told the principal "a declared scope directory that exists
  but holds no tracked file now blocks the commit (exit 2)" and he answered "Keep it": GS2's
  behaviour was disclosed; the CHANGELOG/docstring contradiction remains, severity kept.
- `### Reconcile` appended to the brief; no act-1 text changed; no finding formed at reconcile.
- Gates on the brief after the reconcile, each exit 0: datescan, spellscan, wrapscan, linkscan,
  leakscan, reviewscan, secretscan. Scratch directory empty. Worktree: the brief modified, the
  sibling deleted, nothing else. ACT 2 SAVED 2026-11-15 ~22:30 UTC.
