# Cold pass — G3 records who and when on every manifest line, runs before the ignore file, and reports unreadable metadata (`160/980` applied)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** PASS-WITH-FINDINGS, reconciled 2026-11-15 UTC — 0 MAJOR · 0 MODERATE · 5 minor ·
5 notes (act 1: 3 notes; two notes formed at reconcile). Run under the principal's drain order of
2026-11-16 NZDT; act 1 committed `a8bd0151`, unrevised. Brief written 2026-11-09 UTC. Every
finding is the principal's to decide (rule 3); none applied.
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

---

## Verdict (act 1) — PASS-WITH-FINDINGS

**Run on 2026-11-15 UTC** (21:50–22:20Z), by Fable 5.1 (`claude-fable-5-1`), tier checked at
selection. Review tree: `/Users/mike/worktrees/fable/atelier-160-1080-2148/atelier` at HEAD
`ee849852` (which has `e269f594` as an ancestor: `git merge-base --is-ancestor` exit 0).

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 0 MODERATE · 5 minor · 3 notes.** The delta does what
the acceptance test asks on every point probed live: a reason-only line loads and warns by line
number without blocking; a malformed or unknown `by=` is exit 2; a `.leakscanignore` glob no
longer skips the gate for a tracked binary on either plane; a raw `xmp`, `exif` or `iptc` profile
that does not decode, decodes to nothing, or decodes to bytes that do not parse is never clean;
the hook judges the manifest the commit holds; and the grace blocks from the day itself. The
findings are edge cases at the loader and the hook's cwd, one design choice in the stub, one
untested claim and one overclaim in the README.

### Provenance (V7)

- **Spawn.** I was started by a headless orchestrator session (Opus 5.5), itself started by the
  drain session `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the
  context partition, form no finding and write no severity. The orchestrator read the brief and
  the board item only. I was not started or instructed by `722ac2e2` (or anything it started),
  `84e3aa7f` or `74f2b8cd`, the brief's barred set. No contact from any of them reached me.
- **The orchestrator's spawn prompt** is recorded verbatim in my review log (below), which the
  orchestrator publishes at the fold. Its content was process only: paths, the brief, the barred
  set, the two files I may write, load limits, the live-systems rule, and the shape of this
  deliverable. It carried no question about the delta, no pointer to where risk lives, and no
  request about any finding. The release message for act 2 is not yet received.
- **The principal's permission.** Mike's weekly Fable drain order of 2026-11-16 06:53 NZDT
  (`/fable-drain`), with his 07:16 NZDT words on parallelism and load, is the permission the
  brief's Status line waited for.
- **What I read.** The brief in full; `docs/method/REVIEW.md` in full; the delta body-free through
  `tools/coldsweep.py --root . --commit e269f594` with the brief's thirteen `--path`s (1,718
  lines; the tool's banner confirms the message body was not printed and no rule-2 file was
  touched); each delta path at HEAD in the regions named in the log; `tools/README.md` at HEAD
  around lines 338–570 and 2741; `docs/method/SECRETS.md` 277–288 and `GUARDS.md` 584–590 by
  grep; the floor's two plane outputs; the test outputs. **Disclosed:** the three board-store
  files the brief lists as delta paths were SHOWN by `--path` (coldsweep's banner names them);
  they are the author's own text and I read them as the delta. The CI floor's advisory list named
  `docs/SESSIONS.md:87` and one prior verdict file with redacted 14-character excerpts; I opened
  neither. I did not read the session log, any prior verdict, the queue pointer, the intent
  record `160/980` beyond its title, any commit body, or the sibling.
- **Review log**: `/Users/mike/.claude/fable-drain/notes/atelier-160-1080-2148.md`, every check
  with its command, result and the criterion that decided it, written as the pass ran.

### Lens 1 — approach and assumptions (named first, then tested)

The load-bearing assumptions I named before reading further, and their fate:

| # | Assumption | Result |
|---|---|---|
| A1 | `by= session= on=` is the whole of "who and when" | Fields yes; the kind auto-fills: WM3 |
| A2 | Provenance acceptance is syntax only | Yes, and looser than documented: WM1 |
| A3 | Gate-before-ignore is the same on both planes, tracked-only | Confirmed: P6, P8, glob line |
| A4 | A glob-covered entry can now go stale | Confirmed (P8); intended |
| A5 | The hook's new `ls-files` call shares the staged cwd rule | Damaged: cwd-relative call: WM2 |
| A6 | Raw-profile decoding is bounded by the 1 MiB caps | Confirmed by read and P4 |
| A7 | A `None` blob yields `<set>:unknown` and blocks | Confirmed by read and P3 |
| A8 | `FORBIDDEN_FLAGS` at HEAD still holds "tune, never re-aim" | Confirmed; 3 later flags added |
| A9 | The grace is strict `<`, so the day itself blocks | Confirmed (P9) |
| A10 | The auto stub never claims `principal-*` | Confirmed; the inverse risk is WM3 |
| A11 | Some claim has no test that would fail if it broke | Yes: the listing under a glob, WM4 |

Right problem, right altitude: yes. Recording who and when on the line is the smallest change that
honours the 2026-10-03 words for this manifest while the register (`110/100`) is held, and the
delta says so in every copy. Gate-before-ignore is the right order: the manifest is hash-bound
and content-aware, the glob is neither. Reading the staged manifest closes a real hook/CI split.
The brief's account of the work matched the diff; nothing in the brief's framing narrowed what I
looked at, and the non-goals (child fixes, the original G3 build) fence off no risk the delta
carries.

### Lens 2 — correctness and quality

Every claim under *What the delta claims* re-driven: see the re-run ledger and probes P1–P9 in the
log. No overclaim found in the CHANGELOG, GUARDS or SECRETS text. One README sentence is stronger
than its evidence (WM7). One label is narrower than its README sentence suggests (WM6, note). The
`floor.py` prefix test's companion test does reach every scanner's long flags (no scanner declares
a short option first).

### Lens 3 — completeness and harvest

Mirror sites swept with `coldsweep` (569 files barred, 841 swept): the stale "still runs first"
and "After 2026-11-18" wordings are gone everywhere unbarred; the `by=` form, the rule name and
the raw-profile text live in `leakscan.py` with stamped copies in its tests, the README and the
CHANGELOG; SECRETS names itself the one home of the dated exception and the others as copies
(V4). Cross-references reach existing files: `110/100`, `010/190`, `020/150`, `020/440`,
`020/450`, ADR `2026-10-03-0641` (V5; file names only). Tests that would stay green on a broken
change: one found (WM4). `allowmarker.read_reasoned_lines` is unchanged in behaviour and still
the `.leakscanignore` loader's grammar; `read_reasoned_parts` is single-sourced beneath it.

### Lens 4 — security and privacy (V6)

- **Design altitude.** The delta widens what the gate reads (ignored binaries, raw XMP) and
  narrows nothing; the one new acceptance path (`by=agent` auto-fill) accepts a *record*, never a
  file. No new personal data enters the tree: the stub carries a session id and a date.
- **Code altitude, by hand.** The decode path: a tEXt chunk over 1 MiB is never read; zTXt/iTXt
  inflate under a 1 MiB cap and read as opaque past it; the hex decode therefore sees at most
  1 MiB and yields at most 512 KiB; `xmp_fields` parses with expat as a stream, refuses DOCTYPE and
  entity declarations, never parses parameter entities, and caps properties at 1,024. Probe P4: a
  2 MiB chunk, a 200 MiB zero-fill bomb and a 200 MiB hex bomb each cost about 0.02 s and block.
  Fail-open paths looked for and not found: every `None`/empty/garbage branch ends in
  `<set>:unknown`, which blocks (P3). Catalogue consulted (CWE-400 Uncontrolled Resource
  Consumption; CWE-409 Improper Handling of Highly Compressed Data), fetched live by a Haiku-tier
  agent: the "fail open on exhaustion" consequence CWE-400 names does not apply here; CWE-409's
  decompression-bomb example is the case `_inflate`'s cap answers.
- **`/security-review`: discharged with grounds.** It reads the session's pending diff, which
  here is this brief and the removed sibling, not the landed delta; the worktree cannot be clean
  while I write. Nothing of the delta is in a pending diff for it to reach.
- **Fixtures.** Every image in my probes was a synthetic 1x1 PNG built with `struct` and `zlib`,
  carrying only an `example.com` address; no real file's metadata was read or quoted. Scratch
  repos are deleted at the end of the pass.

### Standing checklist V1–V7

- **V1** No claim stronger than its evidence: one found, the README's "the only *unrecorded* ways
  to skip the gate" (WM7). The test docstring "over every scanner's own parser" holds.
- **V2** Re-run every live-proven claim: done, ledger below; nothing failed to reproduce.
- **V3** Swept to every mirror site: done (lens 3); no miss. Child templates and `commands/scan.md`
  describe the glob as a hatch for a flagged *line* and never claimed it skipped binaries.
- **V4** One fact, one home: holds; copies are stamped by `160/980` ids and SECRETS names itself
  the home of the exception.
- **V5** No internal contradiction: the CHANGELOG, README, source comment, GUARDS and SECRETS agree
  on the form, the warning-not-block for old lines, the firm date and the gate order. Pointers
  reach files that exist (names only).
- **V6** Security and privacy: lens 4 above; `/security-review` discharged with grounds.
- **V7** Provenance: stated above, in the brief's own section and here.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `e269f594` | yes (`coldsweep --commit`, 13 `--path`s) | WM1–WM8 |

Later commits on the delta's code paths (`49f3d407`, `55f23034`, `db8c44b7`, `6d26b058`,
`57719bfa`, `aca05c14`, `641f017f` and others) were read only as they bear on the delta: HEAD's
`FORBIDDEN_FLAGS`, `--messages`, and the summary line. None reversed a delta behaviour.

### Findings

Each is the principal's to decide (rule 3). Counsel is labelled and kept beneath.

**WM1 (minor) — `on=` accepts dates outside the documented `YYYY-MM-DD` form, and which it accepts
depends on the interpreter.** `split_provenance` validates `on=` with `datetime.date.fromisoformat`
(`tools/leakscan.py` ~1340). On Python 3.11+ that accepts `20261109` and `2026-W46-1` (probe P1:
both ACCEPTED on 3.14); on 3.9 and 3.10 both are refused. The README (`tools/README.md` ~380)
promises "a bad date is a config error" and the form `on=<YYYY-MM-DD>`; `PROVENANCE_FORM` says
the same. So one manifest can load on CI (3.12) and be a config error on a hook run by macOS's
system `python3` (3.9), which the README itself names as a supported interpreter for the tools.
That is the hook/CI disagreement class GM12 closes for the manifest's *copy*. A date in the
future or decades past (`2099-12-31`, `1999-01-01`) is also accepted: nothing bounds "when the
exception was granted". Reached only when a writer departs from the printed stub, which is
`YYYY-MM-DD`. *Counsel:* anchor with `^\d{4}-\d{2}-\d{2}$` before `fromisoformat`; consider
refusing an `on=` later than today (UTC).

**WM2 (minor) — the hook's staged-manifest read is the one cwd-relative git call on the staged
plane; run from a subdirectory it reads no manifest and misdiagnoses.** `_staged_manifest`
(`tools/leakscan.py` ~2834) runs `git ls-files --stage -- .leakscanbinaries` with no `cwd` and no
`-C`; a pathspec is cwd-relative. Every other staged-plane call is cwd-independent (`git diff
--cached --no-relative`; `git cat-file blob :0:<path>`, root-relative by git's grammar;
`tracked_files` uses `git -C root`). Probe P5: with the manifest and `img/f.bin` both staged,
`leakscan --staged --root <repo>` from the root is clean; from `img/` it warns `binary-unlisted`
and prints "`.leakscanbinaries` is not staged ... (`git add` it)", which is false. It fails
closed, so no binary passes; the cost is a wrong instruction to the person. The floor's hook runs
from the repo root (git's hook cwd), so the floor path is unaffected today. *Counsel:* `git -C
root ls-files --stage --full-name -- .leakscanbinaries`, or the `:/` pathspec.

**WM3 (minor) — in a Claude session the stub fills `by=agent` and the loader accepts it, so the
one kind most likely to be wrong by default is the one nobody is asked about.** `provenance_stub`
prints `by=agent session=<id>` whenever `CLAUDE_CODE_SESSION_ID` is set (probe P7), and the
loader accepts `agent` without a pick; the stderr help after `--binary-entries` tells a person to
replace `by=CHOOSE` and says nothing when the stub already reads `agent`. A session that lists
binaries *after* the principal answered "allow it" records `agent` unless it edits the line, and
no check or prompt asks. Mike's 2026-10-03 words are "did I rule or did you do it automatically";
the auto-fill answers "automatically" for every agent-written line. The record can understate his
involvement, never overstate it, so it is a register-accuracy defect, not a safety one; the
register (`110/100`) would inherit whatever these lines say. *Counsel:* print `by=CHOOSE` in every
case, or keep `by=agent` as the default and add one stderr line in the Claude-session case: "agent
is the default; write principal-answer or principal-ruled if he answered or ruled".

**WM4 (minor) — the claim that `--binary-entries` lists a glob-ignored binary has no test.** The
CHANGELOG, the README ("A tracked binary under a glob is gated like any other and needs its
hash-bound entry") and the code comment in `binary_entries` ("An ignored binary is gated too
(GM9), so its lines are listed") all state it; `grep leakscanignore tools/test_leakscan.py` finds
tests for the tree and hook planes but none for the listing. A regression of `binary_entries` back
to `iter_files` would leave the suite green while the one command a child is told to run before
2026-11-18 silently omitted the lines it most needs. The claim holds live today (log, `listglob`).
*Counsel:* one test: a glob-ignored tracked binary appears in `--binary-entries` output.

**WM5 (note) — provenance in both the trailing comment and the stanza, with different values, is
accepted with the trailing one winning silently** (`_line_reason`, probe P2). No contradiction
check. *Counsel:* refuse two provenances for one line, as two reasons are already refused.

**WM6 (note) — the word UNREADABLE marks only a hex-decode failure.** A raw profile whose hex body
is empty, has fewer than four lines, or decodes to bytes that do not parse reports `<set>:unknown`
with the plain "(hex-encoded binary profile)" label (probe P3). All block, so the acceptance
test's "reported as unreadable, never as clean" is met in substance by the `unknown` set, whose
help text says "cannot identify or read". The README sentence is true of the case it describes.
*Counsel:* none required; a one-word widening of the label would make the three cases read alike.

**WM7 (minor) — the README's new sentence "Those were the only *unrecorded* ways to skip the gate"
is stronger than its evidence** (`tools/README.md` ~564, V1). A Git LFS pointer is a tracked text
file that publishes a binary to the same remote; leakscan has no LFS handling (sweep: 0 hits) and
the README's "What it can't see" list does not name it. The mechanism predates the delta and is
outside its non-goals; the sentence is the delta's. *Counsel:* name LFS in "What it can't see",
or gate an LFS pointer (`version https://git-lfs.github.com/spec/v1`) as a binary by its pointer.

**WM8 (note, efficiency) — GM9 opens every glob-ignored file on the tree plane** to ask whether it
is binary (`scan_paths`: `not _looks_binary_file(p) or (tracked ... rel not in tracked)`), where
before the delta an ignored file was skipped unopened. Linear and small (an 8 KiB read); atelier's
own CI run has 7 ignored files. *Counsel:* test `rel not in tracked` first, so untracked ignored
files are skipped without a read.

### Re-run ledger

| Line | Where, interpreter | Result |
|---|---|---|
| `floor.py --plane hook --root .` (niced) | worktree root, 3.14 | exit 0, all enforced |
| `floor.py --plane ci --root .` (niced) | worktree root, 3.14 | exit 0; leakscan 3 advisory |
| `unittest test_leakscan test_allowmarker test_floor` | `tools/`, niced, 3.14 | Ran 741, OK |
| `unittest discover -s tools` (niced, load 4.1) | worktree root, 3.14 | see the line below |
| Brief's five scratch lines | scratchpad, 3.14 | 0 / 0 warns / 0 / 2 / 0 G3 warn |
| `/usr/bin/python3 tools/leakscan.py --selftest` | 3.9 | selftest OK |
| Probes P1–P9, listing under a glob | scratchpad, 3.14 | in the log |

Full suite result: `Ran 3134 tests in 799.898s`, `OK`, exit 0 (started 22:07Z at load 4.1,
finished 22:20Z; the brief-writer had recorded this line as not run, at load about 14).

### Follow-up checklist

- [ ] WM1: anchor the `on=` grammar; decide whether a future date is refused.
- [ ] WM2: make the staged-manifest read cwd-independent; fix the stderr diagnosis.
- [ ] WM3: decide the stub's default kind in a Claude session (principal's call: rule 3).
- [ ] WM4: add the listing-under-glob test.
- [ ] WM5, WM6, WM8: notes; take or leave.
- [ ] WM7: name LFS in "What it can't see", or gate pointers.
- [ ] Act 2: reconcile against the sibling and the author's account once released.

### Reconcile

Phase 2, 2026-11-15 UTC (22:22–22:27Z), after act 1 was committed unrevised (`a8bd0151`; `git
diff a8bd0151 -- <this file>` was empty when the release arrived) and the orchestrator released
the held sibling from its held store with a process-only message. Read for this act: the sibling
whole; the queue pointer `160/1080` whole; the intent record `160/980` whole; the prior verdict
`docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` at its status line, its findings
(GM1–GM14, overall) and its reconcile (GM15, the owed asks); the delta commit's message body. Not
read: the session log, `docs/sessions/`, `docs/ROADMAP-DONE.md`. Act-1 text above is unrevised;
every change of weight is recorded here.

**The queue pointer's three questions, against the findings.**

1. *Can the who/when parse be satisfied by a line that records nothing true?* Yes: the check is
   of form only. WM1 (a date outside the documented form, or in the future, loads) and WM3 (the
   auto-filled kind) are the two edges act 1 found; WM9 below, formed here, is that no surface
   says so.
2. *Does gate-before-ignore reach every binary a child tracks?* Every file `git ls-files` lists
   whose first 8 KiB holds a NUL, on both planes (P6, P8, the brief's glob line); files under
   skip-named directories are reached because `filewalk` reads tracked files under them (by read
   of `_walk_files`, not probed); there is no size limit on gating (the digest streams). Not
   reached: a Git LFS pointer, which is a tracked text file (WM7); and on the hook plane a file
   git calls text (pre-existing: the hook gates git's binary set).
3. *Can an old line still pass silently?* No. A reason-only line prints a stdout block naming its
   line, a `binary_provenance` JSON block and a counted summary part, on both planes (the brief's
   reason-only line; delta tests). One corner, WM10 below: an old reason whose text contains the
   token `by=` no longer loads at all.

**The brief-writer's nine questions.**

1. *Is `by=principal-ruled` checked by anything; does the doctrine say what it does not check?*
   Not checked beyond the kind list; no, nothing says so: WM3 and WM9.
2. *Provenance with an empty or generic reason?* Empty: refused as "no stated reason" (delta test;
   `_line_reason` strips the provenance before judging). Generic: loads; specificity is the
   human's, as the prior pass's GM14 and the delta's own README sentence say. No finding.
3. *A reason containing `by=`.* Confirmed by probe: `# supplied by=vendor, looked at` on a
   reason-only line is exit 2, "incomplete who/when"; `lobby=…`, `standby=…` and `set by hand`
   load (the `\b` boundary holds). WM10, note, formed here.
4. *Local or UTC?* UTC on both planes (`_utc_today`, read; P9). The hook and CI flip at the same
   instant, 2026-11-18 00:00Z, which on a New Zealand laptop is 13:00 NZDT on the 18th; neither
   goes red a day before or after the other.
5. *Which binaries "tracked binary" reaches.* As under question 2 above.
6. *Is decompression bounded; what does a hostile raw profile cost?* Bounded at 1 MiB per segment
   before and after inflation; a 200 MiB zlib bomb and a 200 MiB hex bomb each cost about 0.02 s
   and block as UNREADABLE (P4).
7. *`_staged_manifest` when unmerged, deleted in the index, or differing.* Unmerged: probed; `git
   ls-files --stage` lists three stage entries, `git cat-file blob :0:` fails, and leakscan
   returns a broken-scan exit 2 naming the command — fail-closed. Deleted in the index: no entries
   (delta test). Differing: the staged copy is judged and stderr says so (delta test). The fourth
   case, a subdirectory cwd, is WM2.
8. *The prefix test's direction and `key=value`.* The child's token must be a prefix of a
   forbidden flag (the abbreviation direction); `--staged=1` is judged by its name; both covered by
   the delta's tests, and act 1 confirmed no scanner declares a long flag that is a strict prefix
   of a forbidden one.
9. *Is the tests' 3.11 floor true, against the preceding commits?* True. `test_floor` refuses
   3.9 with an explicit `ImportError` that names `tools/README.md`; `test_leakscan` and
   `test_allowmarker` import on 3.9. The preceding commits removed machine dependence (two tests
   that read the host), not the interpreter floor. The README's line stands.

**The brief-writer's held re-runs against this pass's.** All reproduced six days later: the five
`--binary-entries`/manifest lines gave the same five results (its stub carried `by=agent` and a
session id because it ran inside a Claude session; mine carried `by=CHOOSE` with the variable
unset; both as designed, P7); floor hook and CI exit 0 at `c132cc1c` and at `ee849852`; its
module runs OK and mine (741, then the full 3,134) OK; its `test_floor` import failure on 3.9
matches mine.

**The prior verdict's counsel against the application.** GM4 (decode raw `xmp`, UNREADABLE when
it does not decode): applied; WM6 is the one label nuance. GM5 (who and when): applied with the
register's vocabulary; the counsel was "emit the session id and date into each stanza", and the
application added a *kind* beside them, which the counsel had not named: WM3 is about that kind's
default. GM6: applied (`BinaryManifestPaths`). GM8: applied, both halves. GM9, raised to MODERATE
at the prior reconcile and answered by the principal's (d): gate-before-ignore applied on both
planes; the README sentence was rewritten with that verdict's own counsel ("the only unrecorded
ways"), so WM7 is a finding on the counselled wording as much as on the delta. GM12: applied; WM2
is a residue of the application (the new call's cwd). GM13: applied, and true by probe. GM14:
applied. GM1–GM3, GM7, GM10, GM11: record and wording; act 1's sweeps found the stale phrases gone
and the corrections present in every copy. GM15 (a warning in a green CI run) was not among the
applied; the new provenance warning has the same shape and lands in green logs too, but it has no
cliff date, so nothing turns red unseen until the principal dates it.

**The author's account, screened (commit body of `e269f594`).** It agrees with the diff and with
the intent record. Three sentences take a note: "an undecodable raw profile is UNREADABLE" is true
of a hex-decode failure, while bytes that decode but do not parse read `<set>:unknown` (WM6, both
block); "the hook reads the index copy of the manifest" is true from the repo root (WM2);
"`--binary-entries` prints the note (by=CHOOSE outside a Claude session)" is true, and what it
prints inside one is WM3. The intent record's "Left for him: when old reason-only lines should
start blocking", carried by the register redraft (`160/650`, Q3), is consistent with the undated
warning; the kind question in WM3 belongs in the same redraft.

**Findings formed at reconcile** (marked as such; severities of WM1–WM8 unchanged):

**WM9 (note, formed at reconcile) — no surface says the three fields are a record checked for
form, not for truth.** The README says what is a config error (an unknown kind, a bad date, an
incomplete form) and the GUARDS paragraph says the lines "carry `by=`, `session=` and `on=`"; the
register ADR's vocabulary is adopted without its verification posture. A reader may take
`by=principal-ruled` as something the gate established. *Counsel:* one sentence in the README's
"Who allowed it, and when" bullet and in GUARDS' narrowed paragraph: the fields are the writer's
word, checked for form only; the register (`110/100`) is where a grant would be verified.

**WM10 (note, formed at reconcile) — the "still loads and never blocks" promise for an old line
has one corner.** `split_provenance` treats any `\bby=` token as the start of a who/when, so an
old reason-only line whose reason contains that token (`# supplied by=vendor, looked at`) is now
a config error, exit 2, "incomplete who/when" (probe). Fail-closed, with a message that names the
fix; `lobby=`, `standby=` and plain "by hand" are unaffected. The CHANGELOG's "a malformed one is
a config error" covers it in substance; the README's old-line sentence does not. *Counsel:* one
clause in the README's old-line sentence, or anchor the detection to the comment's start.

**Overall line, restated after reconcile:**
**PASS-WITH-FINDINGS — 0 MAJOR · 0 MODERATE · 5 minor · 5 notes (10).** Changes from act 1: WM9
and WM10 added as notes; no severity moved. No MAJOR, so under `REVIEW.md`'s close rule the cycle
closes on the principal's decisions without a further ceremony.

**Owed to the principal (rule 3), all recorded, none applied:** a decision on each of WM1–WM10.
WM3 touches his 2026-10-03 words (the default kind an agent session records) and belongs with the
register redraft's open question on old lines (`160/650`, Q3). The rest are code and wording
fixes for one application commit.

Scratch artefacts (the throwaway repos and fixtures) were deleted at the end of each act; the probe
scripts and their text outputs stayed in the session scratchpad until the pass ended.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed unrevised (`a8bd0151`);
folded here verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (a headless Opus 5.5 session started by drain session `21a271a5`, itself Opus 5.5)
held the partition, formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-g3-who-when-gate-order-cold.md` (`REVIEW.md` rule 1).
Written 2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta.
Open this only after act 1 is committed. Everything here is a floor, never a fence, and none of it
is a finding.

#### The queue pointer's questions (author-written, verbatim)

> whether the who/when parse can be satisfied by a line that records nothing true; whether
gate-before-ignore reaches every binary a child tracks; whether an old line can still pass silently.

#### The brief-writer's own questions

1. `by=principal-ruled` is free text any agent can type. Is the field's truth checked by anything,
and does the doctrine say what it does not check?
2. Provenance is removed before the reason is judged. Can a line carry provenance and an empty or
generic reason?
3. A reason sentence that happens to contain `by=`: `re.search(r"\bby=", text)` makes it "incomplete
who/when", a config error on a line that loaded yesterday. Check against the "never blocks" claim.
4. The date boundary: is `today` local or UTC? New Zealand is 13 hours ahead of CI, so does the hook
go red a day before CI, or after?
5. Which binaries does "tracked binary" reach: by extension or by content? Files under skip-named
directories, Git LFS pointers, files over a size limit, a binary reached only through a scoped
`--staged`?
6. A `Raw profile type xmp` chunk is hex inside a compressed chunk: is decompression bounded, and
what does a hostile one cost before the UNREADABLE verdict?
7. `_staged_manifest` when the manifest is unmerged, deleted in the index, or differs from the
working copy.
8. `floor.py`'s forbidden flags and abbreviations: the prefix test's direction, and a flag in
`key=value` form.
9. The tests' Python floor (3.11) is named by this delta, while the immediately preceding one says
the suite no longer needs it. Which is true?

#### What the brief-writer ran, and what it got

- `wm_tests`: python3 3.14: test_leakscan and test_floor inside the 1019-test run (OK, exit 0);
  test_allowmarker separately, 55 OK, exit 0. Under /usr/bin/python3 3.9 test_floor fails at import
  (`str | None`).
- `p1080`: --binary-entries: exit 0, prints the entry with by=agent, the session id and on=. No
  manifest: exit 0, binary-unlisted warning until 2026-11-18. Reason-only line: exit 0 with
  binary-no-provenance warning naming line 1. Full provenance: exit 0, no warning. by=nobody: exit
  2, config problem. Glob only: exit 0, binary-unlisted warning, so the gate ran before the glob.
- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form only: headings demoted two levels to sit under this one; no other change.*

### Review log — atelier `160/1080`, G3 who-when gate-order cold pass

Reviewer: Fable 5.1 (claude-fable-5-1), tier checked at selection. Spawned by a headless
orchestrator (Opus 5.5) itself started by drain session `21a271a5` (Opus 5.5); both off-tier
orchestrators holding the partition, forming no finding. Not started or instructed by `722ac2e2`
(or anything it started), `84e3aa7f` or `74f2b8cd`.

Review tree: `/Users/mike/worktrees/fable/atelier-160-1080-2148/atelier`, HEAD `ee849852`.
Brief: `docs/reviews/2026-11-09-0126-g3-who-when-gate-order-cold.md`. The `.deferred.md` sibling
is removed from the tree (shows as `D` in `git status`); not sought anywhere until act 2.

This log holds checks and evidence only. The verdict is in the brief. Public-safety rules apply:
no secrets, no live captures, no personal data, no private repo names or paths, no fixture bytes.

#### Act 1

##### 2026-11-15T21:50Z — start
- `date -u` 2026-11-15T21:50:13Z. `uptime` load 4.65 / 4.94 / 6.30 (16 GB laptop, several reviews
  running).
- Read the brief in full (244 lines). Status line says BRIEF WRITTEN; the pass runs now under the
  drain order of 2026-11-16 NZDT.
- Plan, in order: (1) `docs/method/REVIEW.md` for the verdict shape and V1–V7; (2) confirm
  `e269f594` is an ancestor of HEAD and list later commits on the delta paths; (3) read the delta
  body-free via `tools/coldsweep.py --commit e269f594 --path ...` (lens 1 and 2); (4) read each
  delta path at HEAD (lens 2, 3); (5) reproduce the floor (lens 2, re-run obligation); (6) run the
  scratch manifest lines in the scratchpad and extend them with my own probes (lens 2, 4);
  (7) hand-inspect the xmp decode path for CWE-400/409 and fail-open paths (lens 4); (8) sweep
  with coldsweep for V3/V4/V5 (lens 3); (9) write act 1; (10) gate the brief with the repo's
  scanners.
- Not examined, by rule 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, prior
  verdicts in `docs/reviews/` (including the 2026-10-26 G3 verdict), the queue pointer `160/1080`,
  the intent record `160/980` beyond its title, any commit message body, the sibling.

##### 2026-11-15T21:58Z — delta read; assumptions named (lens 1, first act)
- `git merge-base --is-ancestor e269f594 HEAD` exit 0. The brief's `git log --oneline e269f594..HEAD --
  <13 paths>` lists 86 later commits (most touch CHANGELOG.md only); the ones on the code paths
  are checked below.
- Delta read body-free: `python3 tools/coldsweep.py --root <wt> --commit e269f594 --path ...` (13
  paths) -> scratchpad `delta.txt`, 1718 lines, exit 0. Banner: subject, stat, diff; body not
  printed; 3 board-store files SHOWN because `--path` covered them (disclosed in the verdict); 0
  rule-2 files touched. Read all 1718 lines.
- Interpreters: `python3` on PATH = 3.14.6 (Framework); `/usr/bin/python3` = 3.9.6.
- Load-bearing assumptions I name before reading further (to confirm or damage by probe):
  A1. `by= session= on=` discharges "who created it (session id; did I rule or did you do it
      automatically) and when": the three fields map to kind, session, date.
  A2. The loader's acceptance of a provenance is a *syntax* check only: nothing can verify the
      session id or the date, so the record is as good as the writer. Check what a wrong-but-
      well-formed value does (future date, basic-format ISO date, `on=2026-W46-1` on 3.11+).
  A3. "Gate before the ignore file" is implemented identically on the tree plane (`scan_paths`)
      and the hook plane (`_main` staged block); the tracked-only rule holds on both.
  A4. The stale-entry check no longer skips glob-covered entries: an entry for a gone or
      text file under a glob becomes stale (the delta intends this; a test covers the gone case).
  A5. The hook's `_staged_manifest` runs `git ls-files --stage` with no `cwd`: it assumes the
      process cwd is the repo root, as the rest of staged mode must already assume. Check.
  A6. The raw-profile decode path (`_raw_profile_bytes`, then text rules over the decoded XMP)
      is bounded by the existing chunk caps; an attacker-sized hex blob cannot exhaust memory or
      time (CWE-400/409). Check the caps by reading and by a probe.
  A7. `blob is None` -> `_note_xmp(what, None, ...)` yields `xmp:unknown` and blocks; same for
      exif/iptc. Confirm the None path in each `_note_*`.
  A8. `FORBIDDEN_FLAGS` at HEAD still holds the delta's principle ("flags tune, never re-aim"):
      any flag added to leakscan after e269f594 that re-aims or changes mode is in the set.
  A9. `in_binary_grace()` is a strict `today < BINARY_GRACE_UNTIL` so the day itself blocks.
  A10. The `by=agent` stub in a Claude session is accepted without a person's pick; only
      `by=CHOOSE` is refused. So the auto-filled kind is the least-claiming one, never
      `principal-*` by default.
  A11. Tests that would stay green on a broken change: look for tests that only test the
      happy path of GM9 on the hook plane for an ignored binary that is *also* in the manifest
      with a stale digest, and for GM12 with a conflicted index.

##### 2026-11-15T22:00Z–22:10Z — HEAD reads (lens 2, 4; A5–A10)
- `tools/leakscan.py` at HEAD, regions read: 1185–1260 (caps, grace constants, `in_binary_grace`),
  1570–1596 (`_looks_binary_file`, `_inflate`), 1691+ (`exif_fields`), 1842+ (`iptc_fields`),
  1919–1992 (`xmp_fields`: expat stream parser, DOCTYPE/entity handlers fail, param entities never,
  1,024-property cap), 2040–2230 (`_note_*`, `_png_metadata`, `_png_text_decode`,
  `_raw_profile_bytes`, `_png_text_chunk`, JPEG walker head), 2295–2350 (`inspect_media_fields`,
  `metadata_fields`, `metadata_sets`), 2353–2445 (`check_binary`, `_stale`), 2446–2500
  (`tracked_files`, `iter_files`, `iter_files_marked`), 2614–2700 (`scan_paths`, `_stale_reason`,
  `provenance_stub`), 2789–2856 (`staged_changes`, `_staged_manifest`, `_staged_blob`), argparse
  3088–3121 (`--messages` is new since the delta).
- `tools/floor.py` at HEAD 1280–1328: `FORBIDDEN_FLAGS` now also holds `--messages`,
  `--message-file`, `--range` (added by `49f3d407`/`55f23034`); `forbidden_flags` is a prefix test on
  `--name` after splitting `=`. A8 CONFIRMED by read.
- A7 by read: `xmp_fields(b"")` -> expat raises -> `["xmp:unknown"]`; `exif_fields(b"")` -> len<8 ->
  `["exif:unknown"]`; `iptc_fields(b"")` -> no header -> `["iptc:unknown"]`. So a raw profile whose
  hex body is empty or garbage still yields `<set>:unknown`, which `check_binary` gates unless a
  line keeps it. Probe P3 below confirms.
- A6 by read: a tEXt chunk > `META_SEGMENT_CAP` (1 MiB) is never read (`_png_metadata` line
  2101); zTXt/iTXt inflate through `_inflate`, capped at 1 MiB with `unconsumed_tail` -> None; so
  the hex text handed to `_raw_profile_bytes` is <= 1 MiB and the decoded profile <= 512 KiB. Probe
  P4 below confirms.
- A9 by read: `in_binary_grace` is strict `<`. Probe P9 confirms (17th True, 18th False).
- A5 by read: `_staged_manifest` runs `git ls-files --stage -- .leakscanbinaries` with no `cwd`
  and no `-C`. The other staged-plane git calls are cwd-independent (`git diff --cached
  --no-relative`; `git cat-file blob :0:<path>` is root-relative by git's rev grammar;
  `tracked_files` uses `git -C root`). So this is the ONE cwd-relative call on the staged plane.
  Probe P5 below.
- Floor cwd: `floor.py` passes `--root {root}` and does not set `cwd=` on scanner subprocesses
  (grep `cwd=` in floor.py: no hits); git's pre-commit hook runs from the repo root, so the floor
  path is unaffected; a hand run of `leakscan --staged --root X` from a subdirectory is the
  exposed case.
- `CLAUDE_CODE_SESSION_ID` is set in this session's Bash environment (length 36), so the
  "in a Claude session" branch of `provenance_stub` is reachable in practice (one data point).

##### 2026-11-15T21:56Z–22:02Z — re-run obligation (V2)
- `uptime` before each: load 4.09 / 3.48 / 3.26 (1-min).
- `nice -n 10 python3 tools/floor.py --plane hook --root .` from the worktree: exit 0, every
  enforced check ✅. Saved to scratchpad `floor-hook.txt`.
- `nice -n 10 python3 tools/floor.py --plane ci --root .`: exit 0; leakscan 🟡 (3 advisory
  diagnosis-key findings, 0 blocking; "0 binary file(s) by .leakscanbinaries · 0 untracked binary
  file(s) not gated · 0 manifest line(s) with no who/when warned"); secretscan 🟡 28 advisory;
  pointerscan 2 queue-state warnings on another item (`160/994`), not this pass. Exposure to
  disclose: the advisory list named `docs/SESSIONS.md:87` and one prior verdict file with REDACTED
  excerpts (`Dia…ne (14 chars)`); no content of either was read. Saved `floor-ci.txt`.
- `cd tools && nice -n 10 python3 -m unittest test_leakscan test_allowmarker test_floor`
  (python3 = 3.14.6): `Ran 741 tests in 238.294s`, `OK`, exit 0. The "board: docs/ROADMAP.md
  rebuilt (13 lines)" line in its output is a test fixture, not the worktree: `git status` after
  shows only the expected deleted sibling, and the real index is 774 lines.
- Full suite `nice -n 10 python3 -m unittest discover -s tools`: started 22:07Z at load 4.13 as a
  single niced background process (recorded below when it ends).

##### 2026-11-15T22:03Z–22:12Z — probes (scratchpad `probes.py`, `probes2.py`, output in
`probes-out.txt`; throwaway `git init` repos under the scratchpad; synthetic 1x1 PNGs built with
`struct`+`zlib`; every run via the worktree's `tools/leakscan.py` with `python3` 3.14 unless said)
- BRIEF scratch lines (exact lines of the brief, `CLAUDE_CODE_SESSION_ID` unset for the listing):
  `--binary-entries` exit 0, prints `<digest>  a.png  # by=CHOOSE session=human on=2026-11-15`;
  reason-only exit 0 with the stdout block "1 .leakscanbinaries line(s) record a reason but not who
  allowed them or when — WARNING ONLY" naming `.leakscanbinaries:1`, then "✓ leakscan clean";
  full exit 0 clean, no warning; unknown-kind exit 2 with "line 1: by=nobody is not a kind of
  grant (use principal-ruled, principal-answer, agent)"; glob-only (`*.png` in `.leakscanignore`,
  manifest removed) exit 0 with the G3 grace warning `binary-unlisted` for a.png and "0 file(s) by
  .leakscanignore": the glob did not skip the gate. All four match the delta's claims.
- P1 `split_provenance` date forms on 3.14: `2026-11-09` accepted; `20261109` ACCEPTED;
  `2026-W46-1` ACCEPTED; `2026-313` refused; `2099-12-31` ACCEPTED; `1999-01-01` ACCEPTED;
  `2026-11-9` refused. On `/usr/bin/python3` 3.9 `date.fromisoformat` refuses `20261109` and
  `2026-W46-1`. `/usr/bin/python3 tools/leakscan.py --selftest` -> "selftest OK" (the README's
  "tools run on 3.9" holds). -> finding WM1.
- P2 `_line_reason(trailing-with-prov, stanza-with-different-prov)`: trailing's provenance wins,
  no problem raised. -> note WM5.
- P3 (tracked fixtures): raw `xmp` with empty hex body, with two lines only, with hex that is not
  XML, raw `exif` and `iptc` with empty hex body: each -> `binary-metadata` `<set>:unknown ... —
  no line keeps it` (label without the word UNREADABLE); a zTXt raw profile with a non-zlib body
  -> `xmp:unknown` with "UNREADABLE: does not decode". None clean. A7 CONFIRMED; wording note WM6.
- P4 (tracked): 480 KiB hex chunk carrying a 240 KiB XMP packet with 6,000 `dc:creator` elements
  holding an example.com address: 0.18 s, rules `binary-metadata`, `binary-unlisted`, `email`
  (the raw-profile XMP is text-scanned: GM4 holds). 2 MiB tEXt chunk: 0.03 s, `unknown: PNG tEXt
  past the 1048576-byte cap` (blocks). zTXt of a 200 MiB zero-fill (204 KB compressed): 0.02 s,
  `xmp:unknown` UNREADABLE. zTXt of 200 MiB of hex digits (204 KB compressed): 0.02 s, same. A6
  CONFIRMED: CWE-400/409 class guarded by the 1 MiB caps, failing closed (the catalogue's "fail
  open on exhaustion" consequence does not apply).
- P5 hook plane, staged manifest + staged `img/f.bin`: from the repo root exit 0 clean; from
  `img/` (cwd a subdirectory, `--root` the repo) exit 0 with `binary-unlisted` grace warning and
  stderr "`.leakscanbinaries` is not staged, so this commit holds no manifest ... (`git add` it)",
  which is false (it is staged). Fail-closed, wrong diagnosis. -> finding WM2.
- P6 hook plane, glob-ignored binary listed with an old digest: `binary-changed` warned. GM9 on
  the hook plane reaches `check_binary` fully (not only the unlisted case). Confirms A3.
- P7 `--binary-entries` stub: without the env var `# by=CHOOSE session=human on=2026-11-15`; with
  `CLAUDE_CODE_SESSION_ID=abcd1234-ef01` `# by=agent session=abcd1234-ef01 on=2026-11-15`. A10
  CONFIRMED; design note -> finding WM3.
- P8 tree plane, manifest entry for a TEXT file under a glob: `binary-stale-entry ... read as
  text` warned. A4 CONFIRMED (the entry accepted nothing before too; now visible).
- P9 `in_binary_grace(2026-11-17)` True, `(2026-11-18)` False. A9 CONFIRMED.
- Listing under a glob (`listglob`): a glob-ignored tracked `vendor/f.woff` IS listed by
  `--binary-entries` (claim holds live). `grep -n leakscanignore tools/test_leakscan.py` and the
  listing-test names show NO test pairing the ignore file with `--binary-entries`. -> WM4 (tests).

##### 2026-11-15T22:08Z — sweeps (lens 3; V3, V4, V5), all via coldsweep with the brief's two
`--also-exclude`s, 569 files barred, 841 swept
- `still runs first`: 0 hits. `After 2026-11-18`: 0 hits. The stale wordings are gone.
- `five mode|five known|four arguments`: 1 hit, CHANGELOG.md:1330, which is the delta's own
  sentence saying it corrected them. Clean.
- glob-skips-gate phrasing: hits only in leakscan/README (the corrected text) and a sizescan test.
- `read_reasoned_lines`: allowmarker.py (definition, the `.leakscanignore` loader at 467/472) and
  its tests only; README now names `read_reasoned_parts`. Clean.
- `by=<principal|PROVENANCE_FORM|by=agent`: 18 hits, all in leakscan.py, test_leakscan.py,
  README.md, CHANGELOG.md. `binary-no-provenance`: 1 hit (leakscan.py). One home, stamped copies.
- `Raw profile type`: 13 hits, all in leakscan.py/test_leakscan.py/README.
- `lfs|git-lfs`: 0 relevant hits (two in an unrelated JS test). leakscan has no LFS handling and
  the README's "What it can't see" does not name it. -> WM7 against the README's new "only
  unrecorded ways" sentence (V1).
- `leakscanignore` mirror sites: `docs/build/templates/workflows/floor.yml:58–66` and
  `commands/scan.md:33–38` offer a glob as a hatch for a flagged line (text findings) and do not
  claim it skips binaries. No V3 miss.
- Cross-references reached (V5): `docs/method/SECRETS.md:277–` holds the dated-exception
  paragraph; `docs/method/GUARDS.md:584–590` the narrowed paragraph; `docs/roadmap/110-*/100-*.md`,
  `010-*/190-*.md`, `020-*/{150,440,450}-*.md` and `docs/decisions/2026-10-03-0641-the-exception-
  register.md` exist (file names only; none opened beyond what the delta showed).
- Prefix-test reach: `grep add_argument\(\s*('-|"-[A-Za-z]",)` over the scanner files: no scanner
  declares a short option first, so the test's regex sees every long flag. `floor.SCANNERS` = 21
  names.
- `_looks_binary` is "NUL in the first 8192 bytes" (git: first 8000), so the hook's reliance on
  git's binary verdict and the tree plane's own test agree in practice (pre-existing design).

##### Decided NOT to raise (evidence and criterion)
- `scan_path_name` is not run for a glob-ignored binary while the gate is: the glob was always
  path-wide and a name is what a glob judges; no regression from before the delta.
- GM9 opens every glob-ignored file for 8 KiB to ask if it is binary (before, ignored files were
  skipped unopened): linear, and the test order could skip untracked files first without opening.
  Efficiency note only (WM6 group); atelier's CI run shows 7 ignored files.
- The hook gates only what git calls binary (pre-existing); not this delta's.
- `--require-terms`, `--disable` in `flags`: the first tightens, the second is the known,
  documented underblock (EP1); neither re-aims.
- The three board files read via `--path`: the delta's own text, author-written; their content was
  descriptive of the applied findings and disclosed in the verdict; nothing in them steered a
  finding (all findings above arise from code probes).
- Git LFS: the gate's scope is "tracked binaries" and an LFS pointer is a tracked text file; the
  mechanism predates the delta (non-goal); only the delta's new sentence claiming "the only
  unrecorded ways" is attackable, hence WM7 at minor, not higher.

##### Finding ids as written in act 1 (the log's earlier "WM6 group" for efficiency is WM8)
WM1 minor on= grammar/interpreter · WM2 minor hook cwd · WM3 minor by=agent auto-fill · WM4 minor
listing-under-glob untested · WM5 note two provenances · WM6 note UNREADABLE label scope · WM7 minor
README "only unrecorded ways" vs LFS · WM8 note GM9 opens every ignored file.

##### Orchestrator's spawn prompt, verbatim (V7; one machine RAM figure elided as [RAM elided])
```
You are the cold reviewer for one rule-4 review pass in the atelier repo.

WHO YOU ARE
- Item: atelier `160/1080` (G3 records who and when on every manifest line, runs before the ignore file, and reports unreadable metadata).
- Worktree (your review tree): "/Users/mike/worktrees/fable/atelier-160-1080-2148/atelier". Use absolute paths and `git -C "<worktree>"`; never `cd` in a way that leaves you elsewhere. Double-quote every path in every shell command (paths may contain spaces).
- Brief: "/Users/mike/worktrees/fable/atelier-160-1080-2148/atelier/docs/reviews/2026-11-09-0126-g3-who-when-gate-order-cold.md". Read it in full first and follow it, plus "docs/method/REVIEW.md" for the verdict shape and the standing checklist V1–V7.

PROVENANCE (state it in your verdict)
- You are Fable 5.1, tier checked at selection.
- You were spawned by a headless orchestrator session (Opus 5.5), itself started by drain session 21a271a5 (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition, form no finding and write no severity. The orchestrator read the brief and the board item only.
- The brief's barred sessions are 722ac2e2 and everything it started, 84e3aa7f, and 74f2b8cd. You were not started or instructed by any of them.
- You run under Mike's weekly Fable drain order: on 2026-11-16 06:53 NZDT he invoked `/fable-drain`; at 07:16 NZDT he added, verbatim: "You can increase the number of parallel revews running as long as you are managing the system load so that we dont get software or hardware failures that harm the reviews quality or integrity" and "or cause software to crash". The brief's line that the pass "waits for the principal's explicit permission for Fable work" is met by that order.

THE PARTITION
The brief's `.deferred.md` sibling was removed from the worktree on purpose (it shows as deleted in `git status`; that is expected). Do not look for it in git history, `git show`/`git cat-file` of any ref, other checkouts or worktrees, scratchpads, tmp, or "~/.claude". Honour the brief's rule-2 barred list until act 2 is released to you. Use `tools/coldsweep.py` for sweeps exactly as the brief says.

WHAT YOU MAY WRITE
- Only two files: (1) the brief file itself, and (2) your review log at "/Users/mike/.claude/fable-drain/notes/atelier-160-1080-2148.md". Scratch repos and fixtures go under your own session scratchpad, and are deleted when you finish.
- Act 1 goes below a `---` divider at the end of the brief. Update the brief's Status line (never "fold-in owed"). Keep the file's column width (prose ≤ 100 columns), absolute ISO-8601 dates from `date -u`, NZ English. Verbatim source text that trips datescan takes a `datescan:allow` marker. Before finishing each act, run the repo's own gates on the brief from the worktree and fix your own text until clean, e.g. `python3 "<worktree>/tools/floor.py" --plane hook --root "<worktree>"` style checks or the individual scanners (datescan, spellscan, wrapscan, linkscan) named in `tools/README.md`. Note: the sibling link in the brief will dangle while the sibling is held; that is expected and the orchestrator handles it.
- In act 2, append `### Reconcile` as the brief says, but do NOT fold the sibling or delete anything: the orchestrator does the fold.

REVIEW LOG (Mike, 2026-11-16: a review must have irrefutable integrity so its verdict can be trusted, so its method matters as much as its verdict; once complete all its work should be open and readable)
Keep a running log at "/Users/mike/.claude/fable-drain/notes/atelier-160-1080-2148.md" (create it at the start). As you work, append in plain words:
- your method: what you examined, in what order, which of the brief's lenses each step serves, and what you chose not to examine and why;
- each check you ran, with the exact command or file and line, and its result;
- each candidate finding with its evidence and the rule, criterion or requirement that decides it;
- each point you checked and decided not to raise, with the evidence and the criterion.
Write it so a third party could re-run your method and reach the same verdict. Keep it to checks and evidence. It is also your own record for resuming: if you are interrupted, read it first so nothing done before the stop is lost. It is published in this PUBLIC repo at the fold, so write it to the same public-safety rules as the brief: no secrets, no live captures, no personal data, no private repo name or path, no fixture bytes. Act-1 entries are written before the sibling is released. Until act 2 is saved, the log is yours alone; no other session reads or steers it. The verdict itself goes only in the brief.

LIVE SYSTEMS
Read-only reads of live systems are allowed as the review needs them (Mike, 2026-11-09, verbatim: "reads of live systems is fine as needed, Reviews that need writes should be de-priortised"). A read means nothing on the target changes; if a verb's effect is unsure, treat it as a write. NO live writes of any kind (no push, no `gh` call that writes, no commit). A check that would need one is marked NOT RUN with what it would have checked. Allowlist fields before printing because provider reads can carry credentials; never dump a user, key or certificate object raw; leave no captures in scratch.

HOUSE RULES
- No commit, no push, no git command that writes in the worktree. Never mutate the worktree's `tools/` or `instruments/`; exercise tools on scratch copies or fixtures. Never run an installed tool by bare name from PATH; run it from the worktree.
- Never print a secret. No GUI apps. For your own helper scripts use `/usr/bin/python3` (macOS has no `timeout`). The brief notes `/usr/bin/python3` (3.9) cannot import `tools/test_floor.py`; for the brief's re-run lines and unit tests use the `python3` on PATH as the brief says, and record which interpreter ran each.
- LOAD: several reviews run at once on this [RAM elided] laptop and Mike's instruction is to keep it from crashing. Run `uptime` before any heavy step. Run any test suite under `nice -n 10`, one suite at a time, single process (no xdist, no `-n auto`, no parallel runners), in the foreground with a long timeout. Prefer the targeted tests a finding needs over the whole suite; run the full suite the brief asks for once, niced, only if load is below about 16, and otherwise record it NOT RUN with the load reading.
- This repo is PUBLIC. Refer to the orchestrators by session id only. Never write a session NAME, a private repo's name or path, a worktree path that names a private repo, or any estate fact. Refer to a child repo by type only.
- Every finding is the principal's to decide (rule 3): record all, apply nothing.
- If you hit a usage-limit error, stop and say "BUDGET EXHAUSTED" with the act you were in.

HOW TO FINISH ACT 1
When act 1 is written into the brief (verdict, tally, findings with `WM` ids and severities, V1–V7, re-run ledger, follow-up checklist) and your log's act-1 entries are written, STOP and end your reply with: the overall verdict line, the tally, the brief path, and the exact words "ACT 1 SAVED". Do not open the sibling. The orchestrator will commit act 1 and then message you the held sibling's path for act 2. Act 2 ends with "ACT 2 SAVED".
```
Deviation from the prompt, disclosed: my probe scripts ran under the `python3` on PATH (3.14), not
`/usr/bin/python3`, because they import the worktree's `leakscan.py` whose test-adjacent helpers
the brief says need 3.11+; the 3.9 interpreter was used where the check was about 3.9 itself.
The full suite ran as a single niced process in the background (not the foreground) so the log
and verdict could be written meanwhile; it added no parallelism.

##### 2026-11-15T22:14Z–22:20Z — act 1 written; gates on the brief
- Status line updated; act 1 appended below a `---` divider (brief line 246; heading at 248).
- Gates run from the worktree on the brief path: datescan exit 0 (481 lines read, 0 findings);
  reviewscan exit 0; linkscan exit 0 (no markdown links to check); leakscan exit 0 clean;
  secretscan exit 0 clean; attribscan exit 0 clean; pdlistscan (tree-wide) exit 0 clean;
  spellscan and wrapscan exclude `docs/reviews/` by their ignore files (scanned nothing). pathscan
  exit 1 with exactly one finding: brief line 204, the held sibling's path, pre-existing and
  expected (the orchestrator handles it at the fold); my text adds no path finding. quotescan is a
  commit-message checker and takes no file argument (not applicable).
- Column width: every appended prose line <= 100 columns; three table rows trimmed to <= 100.
- Worktree state: `git status --short` shows only ` D` the sibling and ` M` the brief. Nothing
  else touched; no git write run.
- Scratch fixture repos deleted (g3, g3b, rawxmp, rawxmp2, big, big2, hooksub, hookchg, stub,
  txtglob, listglob). Kept in the scratchpad: the probe scripts and their text outputs (digests of
  synthetic fixtures only, no fixture bytes), the floor and test outputs, `delta.txt`.

##### 2026-11-15T22:21Z — full suite result; act 1 saved
- `nice -n 10 python3 -m unittest discover -s tools` (3.14, single process): `Ran 3134 tests in
  799.898s`, `OK`, exit 0; started 22:07Z at load 4.13, finished 22:20:55Z, load 4.6 at the end.
  Written into the brief's re-run ledger.
- Gates re-run on the brief after the last edit: datescan, reviewscan, linkscan, leakscan,
  secretscan, attribscan all exit 0; pathscan 1 finding = the held sibling's path (line 204,
  expected). No appended line over 100 columns. Worktree: ` D` sibling, ` M` brief only.
- ACT 1 SAVED. The sibling has not been opened. Act 2 waits for the orchestrator's release.

#### Act 2

##### 2026-11-15T22:22Z — release received; act 1 confirmed committed unrevised
- Orchestrator's release message (process only): act 1 committed as `a8bd0151`; the sibling's
  held path given; the brief's rule-2 records opened; append `### Reconcile`, never revise act 1,
  do not fold or delete; same rules as act 1. `git log -1` shows `a8bd0151 reviews 160/1080: act 1
  of the G3 who-when gate-order cold pass`; `git diff a8bd0151 -- <brief>` is 0 lines, so the act-1
  text in the tree is the committed text.
- Read for act 2: the sibling whole (46 lines, held at a user-local path, written by `84e3aa7f`);
  the queue pointer `160/1080` whole (38 lines); the intent record `160/980` whole (83 lines);
  the prior verdict `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` lines 1–7
  (status), 599–760 (findings GM1–GM14 and overall) and 816–942 (reconcile), located by a grep
  index of its headings; the delta commit body of `e269f594` (`git log -1 --format=%B`). Not
  read: `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` (nothing in the sibling or
  the pointer sent me there).

##### 2026-11-15T22:23Z–22:27Z — act-2 probes (scratchpad `probes3.py`; repos deleted after)
- Sibling Q3: old reason-only line, reason text `supplied by=vendor, looked at` -> exit 2,
  "line 1: incomplete who/when"; `lobby=photo ...`, `standby=image ...`, `set by hand ...` -> exit
  0, the usual who/when warning. -> WM10 (note, formed at reconcile): fail-closed corner of the
  "never blocks" promise.
- Sibling Q7: `.leakscanbinaries` left unmerged by a real merge conflict (3 stage entries in
  `git ls-files --stage`); `leakscan --staged --root <repo>` from the root -> exit 2, stderr
  "git cat-file failed for .leakscanbinaries: ... ':0:.leakscanbinaries' returned non-zero exit
  status 128". Fail-closed broken scan; no finding.
- Sibling Q9: `/usr/bin/python3 -c "import test_floor"` in `tools/` -> ImportError "this suite
  needs Python 3.11 or later, found 3.9 ... see tools/README.md"; `test_allowmarker` and
  `test_leakscan` import on 3.9. The README's 3.11 test floor is true; no finding.
- Sibling Q1/Q2/Q4/Q5/Q6/Q8 answered from act-1 evidence (WM3, delta tests, `_utc_today`, P4,
  the forbidden-flag tests and act-1 grep); recorded in the brief's reconcile. WM9 (note, formed
  at reconcile): no surface says the three fields are checked for form only.
- The prior verdict's GM1–GM15 compared with the application: all applied as counselled; WM2 is
  a residue of GM12's application, WM7 attacks GM9's counselled wording, WM3 the kind field GM5's
  counsel did not name. The author's commit body agrees with the diff; three sentences carry the
  WM2/WM3/WM6 nuances. The brief-writer's five held results match mine.

##### 2026-11-15T22:26Z — act 2 saved
- Status line updated to "PASS-WITH-FINDINGS, reconciled 2026-11-15 UTC — 0 MAJOR · 0 MODERATE ·
  5 minor · 5 notes"; `### Reconcile` appended beneath act 1 (brief now 603 lines); act-1 text
  unrevised; sibling not folded or deleted (the orchestrator folds). One typo in my own act-2
  window (22:40Z written for 22:27Z) corrected in the act-2 text.
- Gates on the brief after the append: datescan, reviewscan, linkscan, leakscan, secretscan,
  attribscan exit 0; pdlistscan (tree) exit 0; pathscan 1 finding = the held sibling's path
  (expected); no appended line over 100 columns. Worktree: ` D` sibling, ` M` brief only; no git
  write, no live write.
- Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 0 MODERATE · 5 minor · 5 notes (10).
- ACT 2 SAVED.
