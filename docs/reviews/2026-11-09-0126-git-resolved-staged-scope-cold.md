# Cold pass — git resolves a staged scan's positional scope, and an unknown one is refused (`160/950`, QS1 applied)

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-15 UTC under the principal's drain order of 2026-11-16 NZDT:
PASS-WITH-FINDINGS, 0 MAJOR · 2 MODERATE · 3 minor · 4 notes. Act 2 (reconcile) owed.
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
brief's sibling `docs/reviews/2026-11-09-0126-git-resolved-staged-scope-cold.deferred.md`, every
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
