# Cold pass — G3 records who and when on every manifest line, runs before the ignore file, and reports unreadable metadata (`160/980` applied)

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-15 UTC under the principal's drain order of 2026-11-16 NZDT:
PASS-WITH-FINDINGS (0 MAJOR, 0 MODERATE, 5 minor, 3 notes). Act 2 (reconcile) pending the
sibling's release. Brief written 2026-11-09 UTC.
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
