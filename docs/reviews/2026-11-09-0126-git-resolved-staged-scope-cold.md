# Cold pass — git resolves a staged scan's positional scope, and an unknown one is refused (`160/950`, QS1 applied)

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF WRITTEN 2026-11-09 UTC. The pass has NOT run and waits for the principal's
explicit approval for Fable work.
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
