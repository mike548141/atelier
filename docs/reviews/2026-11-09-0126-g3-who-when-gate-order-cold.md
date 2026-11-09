# Cold pass — G3 records who and when on every manifest line, runs before the ignore file, and reports unreadable metadata (`160/980` applied)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF WRITTEN 2026-11-09 UTC. The pass has NOT run and waits for the principal's
explicit approval for Fable work.
**Sizing:** **large** — one commit, about 950 lines across 13 files, a guard that goes blocking on a
fixed date, with binary-format and hook-plane behaviour to re-drive. ⏳ The 2026-11-18 grace end is
the reason to prefer it early.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1080-rule-4-cold-pass-queued-g3-who-when-and-gate-order.md`.
**Why it earns a review:** A blocking guard in every child changes what it reads and what it
accepts, with its grace ending 2026-11-18. Worst failures: a binary carrying personal data passes on
a line that records nothing true, or a legitimate line goes red in a child on the day the grace
ends.

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
- the delta body-free through `tools/coldsweep.py --commit e269f594` (subject, stat, diff, never the
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

The principal's answers of 2026-11-08, as the intent record holds them (answers to options offered,
not rulings in his own words): *"Firm; queue fixes now"*, 2026-11-18 stands for every child, and
*"Yes, all as recommended"*, whose offered picks read: raw `xmp` the gate cannot read is reported as
unreadable, never as clean; each manifest line records who allowed it and when, per his 2026-10-03
words, not a reason alone; the gate runs before the ignore file for binaries, so no ignore glob
skips it. The grace is `BINARY_GRACE_UNTIL` in `tools/leakscan.py`.

## What the work is

One commit on `main`, `e269f594` (first confirm your tree has it: `git merge-base --is-ancestor
e269f594 HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit e269f594 \
  --path tools/leakscan.py \
  --path tools/allowmarker.py \
  --path tools/floor.py \
  --path tools/test_leakscan.py \
  --path tools/test_floor.py \
  --path tools/test_report.py \
  --path tools/README.md \
  --path docs/method/SECRETS.md \
  --path docs/method/GUARDS.md \
  --path CHANGELOG.md \
  --path docs/roadmap/020-policy-as-code-programme-five-tracks-mik/150-e7-residue-g3-binary-media-funded-as-its-own-i.md \
  --path docs/roadmap/020-policy-as-code-programme-five-tracks-mik/410-adoption-assumes-advisory-first.md \
  --path docs/roadmap/300-posture-recover-cheaply-mike-commissioned/020-re-rank-the-guard-board-against-the-test.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline e269f594..HEAD -- tools/leakscan.py tools/allowmarker.py tools/floor.py tools/test_leakscan.py tools/test_floor.py tools/test_report.py tools/README.md docs/method/SECRETS.md docs/method/GUARDS.md CHANGELOG.md docs/roadmap/020-policy-as-code-programme-five-tracks-mik/150-e7-residue-g3-binary-media-funded-as-its-own-i.md docs/roadmap/020-policy-as-code-programme-five-tracks-mik/410-adoption-assumes-advisory-first.md docs/roadmap/300-posture-recover-cheaply-mike-commissioned/020-re-rank-the-guard-board-against-the-test.md
```

## What the delta claims (extracted, not evaluated)

- Each `.leakscanbinaries` line can carry `by=` `session=` `on=`; a malformed one is a config error.
- A line with a reason only still loads and prints a warning naming its line; it never blocks.
- `--binary-entries` prints the provenance on every line, `by=agent` plus the session id in a Claude
  session, `by=CHOOSE` otherwise, which is refused until a person picks.
- A `.leakscanignore` glob no longer skips the gate for a tracked binary, on the hook plane too.
- A PNG `Raw profile type xmp` chunk is decoded and scanned; a raw profile that does not decode is
  reported UNREADABLE and blocks as `<set>:unknown`.
- The hook reads the manifest the commit holds.
- A manifest path that is absolute or climbs out with `..` is a config error.
- `floor.py` refuses `--root`, `--terms` and `--staged` in `flags`, and abbreviations of them.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** The child-side fixes the principal asked to be queued, which live on each child's own
board; the original G3 build except as this delta changes it.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. `leakscan` is the personal-data boundary for binary files.
The delta decodes untrusted image profiles, so check it by hand for resource exhaustion and
fail-open paths, and check a catalogue (CWE-400, CWE-409) for the decompression class. Fixtures are
a privacy surface in this PUBLIC repo; use synthetic images, and quote no metadata from any real
file.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane hook --root .` and `--plane ci`
- `cd tools && python3 -m unittest test_leakscan test_allowmarker test_floor`
- the manifest lines below, on a throwaway repo under your scratchpad

The scratch lines:

```
SCR=<scratchpad>/g3; rm -rf "$SCR"; git init -q "$SCR"
# write a 1x1 PNG to $SCR/a.png with Python's struct and zlib; git -C "$SCR" add a.png
python3 tools/leakscan.py --root "$SCR" --binary-entries "$SCR"
D=$(shasum -a 256 "$SCR/a.png" | cut -c1-64)
printf '%s  a.png  # synthetic fixture, reason only\n' $D > "$SCR/.leakscanbinaries"
python3 tools/leakscan.py --root "$SCR" "$SCR"; echo "reason-only exit $?"
printf '%s  a.png  # by=agent session=abcd1234 on=2026-11-09 synthetic fixture\n' $D > "$SCR/.leakscanbinaries"
python3 tools/leakscan.py --root "$SCR" "$SCR"; echo "full exit $?"
printf '%s  a.png  # by=nobody session=abcd1234 on=2026-11-09 synthetic fixture\n' $D > "$SCR/.leakscanbinaries"
python3 tools/leakscan.py --root "$SCR" "$SCR"; echo "unknown-kind exit $?"
rm "$SCR/.leakscanbinaries"; printf '# synthetic fixture for the probe\n*.png\n' > "$SCR/.leakscanignore"
python3 tools/leakscan.py --root "$SCR" "$SCR"; echo "glob-only exit $?"
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
`docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md`. the queue pointer above, this brief's
sibling `docs/reviews/2026-11-09-0126-g3-who-when-gate-order-cold.deferred.md`, every delta commit's
message body, and the intent record
`docs/roadmap/160-doctrine-review-owed/980-rule-4-cold-pass-queued-g3-grace-and-metadata-sets.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred. This pass reviews the application of an earlier pass's findings, so the delta's own
text carries that verdict's finding identifiers and decision stamps: `REVIEW.md` § *Applying
decisions to doctrine* names this as a residual exposure that cannot be closed. Review the edited
text at HEAD and commit your findings first.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1080-rule-4-cold-pass-queued-g3-who-when-and-gate-order.md \
  --also-exclude docs/roadmap/160-doctrine-review-owed/980-rule-4-cold-pass-queued-g3-grace-and-metadata-sets.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`e269f594`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `WM`: `WM1`, `WM2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run
ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling
is opened.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body; append
`### Reconcile` beneath your verdict: per-finding notes against the sibling and the author's
account, any finding formed at reconcile marked as such, and the overall line restated. Never revise
act-1 text. Then fold the sibling in below the reconcile and delete it.

Every finding is the principal's to decide (rule 3): record all, apply nothing. Counsel per finding
is welcome, labelled as counsel and kept beneath it.
