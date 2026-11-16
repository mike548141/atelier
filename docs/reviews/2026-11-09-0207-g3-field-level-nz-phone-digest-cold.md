# Cold pass — G3 keeps image metadata field by field with a dated migration, and `nz-phone` skips digit runs inside hex digests

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is doctrine by
function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** VERDICT COMPLETE, 2026-11-15 UTC: PASS-WITH-FINDINGS (0 MAJOR, 1 MODERATE, 3 minor,
5 notes, one formed at reconcile), by a Fable 5.1 reviewer under the principal's 2026-11-16
drain order; act 1 committed at `464c4748`, act 2 (reconcile) appended; every finding is the
principal's to decide (rule 3), none applied. Brief written 2026-11-09 UTC by session
`d4a0fcf3`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/990-rule-4-cold-pass-queued-g3-field-level-and-nz-phone-digest-guard.md`.
**Size of this pass:** large: three commits, about 1,030 lines of binary-format parsing in a
blocking guard, on the personal-data boundary.
**Why it earns a review:** `leakscan` is a blocking guard every child runs, and a too-wide skip or a
misread tag is silent by construction. The worst failure is location or personal metadata in an
image passing because a parser read it as something a manifest line keeps.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Sonnet worker it dispatched, which wrote the code (per the queue pointer). The
  author queued this pass and does not take it.
- **Who wrote this brief:** session `d4a0fcf3` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-09 UTC by coordinating session `74f2b8cd` (Opus 5.5), on the principal's request to brief
  every owed pass. Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model. `74f2b8cd` built none of these subjects and forms no finding; its launch
  prompt is the brief-writer's only instruction.
- **Barred from running this pass:** session `d4a0fcf3` and session `74f2b8cd` (whoever writes a
  brief does not run it, the principal's rule), and the author session named above with everything
  it started.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `74f2b8cd`: the
  item numbers, the rules of the run, and the statement that it built none of these subjects. It
  carried no framing of the work. The brief-writer had no contact with the author session or its
  workers.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md` and `docs/method/REVIEW.md` whole; the board
  item whole; the intent records' opening part and every line naming the principal or a landing
  account; every delta commit body-free through `tools/coldsweep.py --commit`; commit subjects
  through `git log`; `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole,
  **including that pass's verdict and folded sibling** (a different subject, read for house form),
  the acceptance-test section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words, printed by the span command below (they are the only quoted words in
`020/450` that are his; the rest of that record is barred). Doctrine: `docs/method/SECRETS.md` §
*The boundary's posture*, and the repo's purpose-based personal-data rule in
`docs/build/REPO-STANDARD.md`. `320/470` offered three options and carries no principal ruling the
brief-writer found.

Print only the quoted spans, before phase 1:

```
python3 -c 'import re, sys
for p in sys.argv[1:]:
    t = " ".join(l.strip() for l in open(p, encoding="utf-8"))
    for m in re.findall(r"\*\"(.+?)\"\*", t): print("-", m)' \
  docs/roadmap/020-policy-as-code-programme-five-tracks-mik/450-g3-keeps-image-metadata-field-by-field-not-by-data-type.md
```

## What the work is

- **`7bc0f87`** — `leakscan: nz-phone ignores digit runs inside hex digests (320/470)`.
- **`2ba261b`** — `leakscan: G3 keeps Exif and GPS metadata field by field (020/450 part 1)`.
- **`1297df4`** — `leakscan: G3 keeps IPTC, XMP and PNG text field by field (020/450 part 2)`.

Delta paths, read at each commit and at HEAD:

- `tools/leakscan.py`, `tools/test_leakscan.py`, `tools/test_report.py`, `tools/README.md`,
  `CHANGELOG.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 1297df4 HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path tools/leakscan.py --path \
  tools/test_leakscan.py --path tools/test_report.py --path tools/README.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline 1297df4..HEAD -- tools/leakscan.py
tools/test_leakscan.py tools/test_report.py tools/README.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- Each block is "read field by field (names only, never the values)" for Exif and IPTC; XMP and PNG
  text values "are matched by the text rules" (README).
- What the reader cannot walk is `<set>:unknown`, "which blocks until it is named".
- A packet with a DOCTYPE or entity, an out-of-skeleton element, no prefix, or over 1,024 properties
  is `xmp:unknown`.
- `TYPE_LEVEL_UNTIL` is 2026-12-18 UTC: a type-level line keeps the whole set and warns until then,
  keeps nothing from that day, and "no flag or setting moves the date".
- `_phone_inside_hex_digest`: "a spaced, dashed or bracketed phone is never skipped"; the guard
  needs a separator-free digit match in a 16+ hex run.
- Over 1,024 distinct fields adds `<set>:unknown`; JPEG extended XMP is joined before it is read.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the G3 grace and metadata sets as reviewed under `160/980`; the application `e269f59`
and its pass `160/1080`, except as it bears on HEAD; the off-rule tier (pass `160/994`).

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states this behaviour (V3); one home (V4); no
   contradiction (V5). Find tests that would stay green on a broken delta by mutating a scratch
   copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design; at code altitude the likely vectors for its class, checked against an open
   catalogue (OWASP ASVS or the domain's equivalent). Aim `/security-review` at code only from a
   clean tree, as *House rules* says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root,
in the foreground or under `nice`; its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH`.

```
python3 -m unittest discover -s tools -p test_leakscan.py
python3 -m unittest discover -s tools -p test_report.py
python3 tools/leakscan.py --selftest
nice -n 10 python3 -m unittest discover -s tools
```

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0207-g3-field-level-nz-phone-digest-cold.deferred.md`
(folded below the verdict at phase 2; the file is removed) (a held-back file; by
count: 9 questions, 2 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond
its title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/450-g3-keeps-image-metadata-field-by-field-not-by-data-type.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/470-leakscan-nz-phone-matches-digit-runs-inside-hex-digests.md`

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/450-g3-keeps-image-metadata-field-by-field-not-by-data-type.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/470-leakscan-nz-phone-matches-digit-runs-inside-hex-digests.md \
  '_phone_inside_hex_digest|TYPE_LEVEL_UNTIL|exif_fields|iptc_fields|xmp_fields|png_text_field'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`GF`: `GF1`, `GF2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict (act 1), 2026-11-15 UTC

### Provenance

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection.
  Review worktree `/Users/mike/worktrees/fable/atelier-160-990-1955/atelier`, HEAD `3709c307`.
- **Spawn:** started by a headless Opus 5.5 orchestrator session, itself started by drain
  session `21a271a5` (Opus 5.5), under the principal's weekly Fable drain order of 2026-11-16
  06:53 NZDT (`/fable-drain`). Both orchestrators are rule-4 off-tier orchestrators: they hold
  the context partition, form no finding and write no severity. Neither wrote this brief or any
  of the delta. I was not started or instructed by sessions `d4a0fcf3` or `74f2b8cd` (the
  brief-writer and its coordinator) or by author session `4c65083c` or anything it started.
- **Orchestrator direction received** (process only, summarised; no question about the delta,
  no pointer to a risk): the item id, the worktree path, the brief path, the barred set (the
  sibling removed from the worktree and not to be sought in history or elsewhere), the shape of
  the deliverable (act 1 below a divider, prefix `GF`, column width, dates), the review-log
  file I may write, no commit or push, load and live-system rules, and the release timing (the
  sibling's path is sent after act 1 is committed).
- **Partition:** the sibling `.deferred.md` is deleted in this worktree (`git status` shows the
  deletion). I did not open it, look for it in git history, other checkouts or elsewhere, and I
  did not open `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior verdict,
  any commit message body, or the two intent records beyond their first line. The session-log
  step of the onramp was skipped (rule 2).
- **What I read:** this brief whole; `docs/method/REVIEW.md` whole; `docs/method/GUARDS.md`
  380–430; the three delta commits body-free through `coldsweep --commit`, scoped with `--path`
  to the five delta paths (no board file named; `coldsweep` reported 2 board-store files left
  out of `7bc0f87`); `tools/leakscan.py` at HEAD, the nz-phone rule and validators, the G3 block
  comment and dates, the manifest grammar, every field reader and walker, `check_binary`,
  `--binary-entries`, the renderers and the selftest; `tools/README.md` 350–585;
  `CHANGELOG.md` 1723–1812; `tools/test_leakscan.py` 2561–3410 and the nz-phone test class;
  board item `320/810` lines 70–85 and `320/850` line 14 (not barred; both reached by the
  sweep). Three `coldsweep` sweeps, default exclusions plus the brief's three, no
  `--include-barred`. The orchestrator's spawn prompt also carried the acceptance-test spans,
  which I re-printed myself with the brief's command.
- **Review log, open by design:** `~/.claude/fable-drain/notes/atelier-160-990-1955.md` holds
  every check, probe and non-finding with its evidence, written as act 1 ran.
- **Live systems:** none read, none written. **Child repos:** none read (0).
- **Scratch:** synthetic fixtures and a mutated scratch copy of `tools/` under my scratchpad,
  deleted at the end of act 1; no capture of real data was made.

### Load-bearing assumptions, named first (lens 1)

- **A1. A field's name is enough for the human to judge; the value is never needed in the
  gate's output.** Confirmed as design and in behaviour: `test_no_value_reaches_any_output`
  passes, and the only packet-controlled text in any output is a field *name* (an XMP local
  name ≤ 64 characters, a PNG keyword ≤ 79 bytes percent-encoded), which is also run through
  the text rules. Residual: a name is attacker-chosen text (GF8, note).
- **A2. `<set>:unknown` is a fail-closed floor, not a hatch.** Half confirmed. It blocks until
  named, so nothing passes silently. But naming it keeps the whole block whatever it holds, so
  every legitimate shape the reader cannot walk becomes a reason for a child to write the one
  wildcard the design refuses. One such legitimate shape found (GF3).
- **A3. The dated flip is the principal's.** Damaged. The G3 grace date is his ("Firm", 160/980
  GM7, quoted in the code); the type-level date is the author's pick, carried with the same
  firmness and no attribution (GF1).
- **A4. The manifest grammar is unambiguous: a token means one thing.** Damaged in one corner:
  the bare `unknown` after a field is the `unknown` set (GF2).
- **A5. The hex-digest guard skips only separator-free digit runs glued inside a
  digest-length hex run.** Confirmed by probe at the boundary: 16 skipped, 15 flagged; a
  spaced, dashed, `+64` or bracketed phone is never skipped (`isdigit` gate). The narrowing is
  the author's pick of three options on a guard (GF7, note).
- **A6. Every read is bounded.** Confirmed: IFDs ≤ 16, entries ≤ 1,024 and cut to the block,
  IPTC datasets ≤ 4,096 and resources ≤ 1,024, XMP properties ≤ 1,024, one segment ≤ 1 MiB (64
  KiB for JPEG), inflate capped, extended XMP total capped, fields per set ≤ 1,024. Memory for
  the gathered `texts` of one file is bounded only by the file (pre-existing, GF8 note).

### The acceptance test

The two quoted spans were printed with the brief's command: fields "as in GPS versus the camera
model", and one reason may cover several fields "e.g. fields A, B, and C allowed because of X".
The design meets both: a line keeps `exif:Make,Model,LensModel` and the GPS tags beside them
block, naming each (`test_the_camera_model_kept_blocks_the_gps_beside_it`); several fields of
one or more sets sit under one reason on one line, or on several lines with their own reasons,
and `gps` alone is refused. Whether a reason is *specific* stays the person's call, and the
README says so. The remaining question is not whether the fields are read but who set the day
the old whole-set lines stop working (GF1).

### Per-lens answers

1. **Approach & assumptions.** Right problem, right altitude: the gate names what the bytes
   carry and makes the human keep it by name. The one design choice I would put back to the
   principal is the dated flip (GF1): a warn-until-ruled posture, which this same README
   already takes for the who/when warning, was available and is the house's default for an
   agent's date. Fields as the unit is sound; the `unknown` field as a keepable name is the
   honest fail-closed answer but it is also the hatch a legitimate legacy shape forces open
   (GF3).
2. **Correctness & quality.** Every claim in the brief's list re-drove true: names only, never
   values; `<set>:unknown` blocks until named; the XMP skeleton, DOCTYPE, entity and 1,024
   rules; the 2026-12-18 flip with no flag; the separator rule of the hex guard; the per-set
   cap and the joined extended XMP. Overclaims found: the `inspect_media_fields` docstring
   (GF4), the README's continuation-grammar sentence (GF2). Two edge shapes behave worse than
   the text promises (GF3, GF6).
3. **Completeness / harvest.** One home for the behaviour (`tools/README.md`) with a dated
   CHANGELOG copy; no mirror in `docs/method`, skills or templates states the date, so V3/V4
   hold. Tests are strong: of five mutations on a scratch copy, three were caught at once
   (GPS pointer dropped, attribute-form XMP ignored, the grace never ending); two survived
   (the hex floor lowered to 12, and `>` for `>=` at the floor), so the one number the guard
   turns on is unpinned (GF5).
4. **Security & privacy.** Design altitude: the gate collects nothing new; it prints names and
   blocks on presence. Threats enumerated for the class (untrusted binary parsed in a hook):
   entity expansion and external entities (DOCTYPE and entity declarations fail the packet,
   parameter entities never parsed, bomb test present), decompression bombs (inflate capped),
   unbounded counts and pointer loops (bounded, loop-tested), memory (per segment bounded; per
   file not, pre-existing), output leakage (names only, test present). ASVS V5 input handling
   and V12 file handling classes checked by hand. `/security-review` NOT RUN: it reads the
   session's pending diff, which in this worktree is the removed sibling and then this brief
   (the SL2 exposure); the delta is landed, not pending. Weighed as nothing; the hand read
   stands in. Nothing MAJOR or MODERATE in this lens; GF8 is a note.

### The standing checklist

- **V1** No claim stronger than its evidence: GF4 (docstring says Exif and GPS "so far", a
  3-tuple for a 4-tuple), GF2 (README's continuation sentence). The rest hold.
- **V2** Re-run every recorded proof: the four lines re-run, ledger below; all green.
- **V3** Swept to every mirror: one home plus CHANGELOG; the ADR `2026-10-03-0641` and items
  `020/150`, `020/440`, `320/810` mention the field-level work and the date without restating
  the rule. Clean.
- **V4** One fact, one home: `TYPE_LEVEL_UNTIL` is one constant, read by one predicate; the
  README prints it once. Clean.
- **V5** No internal contradiction: README, CHANGELOG and code agree on "strictly before keeps,
  from the day blocks". One governance contradiction inside the README (GF1: the who/when
  warning's block date is "Mike's to rule"; the type-level block date is the author's). The
  cross-reference to `GUARDS.md` reached the rule it names (mandate or default dates).
- **V6** Security and privacy: lens 4 above; scanner discharged with grounds.
- **V7** Provenance stated in the brief and repeated above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `7bc0f87` nz-phone hex-digest guard | yes (`coldsweep --commit`, 124 lines) | GF5, GF7 |
| `2ba261b` Exif and GPS fields, part 1 | yes (1,335 lines) | GF1, GF2, GF4, GF6 |
| `1297df4` IPTC, XMP and PNG text, part 2 | yes (1,357 lines) | GF2, GF3, GF8 |

Since the delta, about 50 commits touched the four tool paths (93 with `CHANGELOG.md`); the
ones that bear on it at HEAD are `e269f594`
(the 160/980 application: provenance, raw XMP read, gate before the ignore file; a non-goal,
read only where `check_binary` meets it) and `57719bfa` (the sibling byte-field guard beside
`_phone_inside_hex_digest`). Neither changes a finding below.

### Findings

**GF1 — MODERATE.** *The type-level cut-off, 2026-12-18, is an agent's date carried as a
mandate, with no surface saying whose it is.* `TYPE_LEVEL_UNTIL` blocks every child's
whole-set `exif`, `iptc`, `xmp` and `png-text` lines from that day. The code comment says "Like
the grace it is one constant ... no flag, env var or config key to move it", the README "no flag
or setting moves the date", the CHANGELOG "a month after the G3 grace ends ... with no flag or
setting to move it". The grace date beside it is the principal's, quoted ("Firm; queue fixes
now", 160/980 GM7); this one has no word of his behind it on any surface a child reads, and
`GUARDS.md` § *Who may move a deferment's date* says an unlabelled fleet date reads as a
mandate, the strictest kind. The same README, twelve lines up, takes the opposite posture for
the who/when warning: *"No date turns that warning into a block: whether and when it should is
Mike's to rule."* Board item `320/810` already names the pattern for later flips ("the dates
are the run's choice, not his") and lists 2026-12-18 among the existing ones. Rule 3: a
blocking date in a guard is doctrine by function and his to decide.
*Counsel:* put the date to him with the two live options (confirm 2026-12-18 as a mandate, or
warn-only until he rules, as the who/when warning does); record who and what kind on the
constant's comment, the README and the CHANGELOG; the fix is one line in each once he has
spoken. Possibly answered in the barred records; reconciled in act 2.

**GF2 — minor.** *The continuation grammar has one ambiguous token.* README 436–437: "After one
`set:Field`, bare names continue the same set". Probe: `parse_scope("exif:Model,unknown")`
returns `['exif:Model', 'unknown']`, the whole `unknown` *set*, because `tok in METADATA_SETS`
is tested before the continuation branch, and `unknown` is the one name that is both a set and
a field of every read set. The same holds for `iptc:City,unknown`. It fails closed later (the
`unknown` line is stale and `exif:unknown` is still unkept, two findings), so nothing passes,
but a child following the README's rule is sent round a loop the text does not explain.
*Counsel:* in `parse_scope`, when `cur` is set and the token is `unknown`, read it as
`<cur>:unknown`, or refuse it as ambiguous and ask for the full spelling; one test.

**GF3 — minor.** *A legitimate legacy XMP root reads as the wildcard.* Probe: a packet whose
root is `x:xapmeta` (the older Adobe spelling, which as I recall the XMP specification part 1
asks readers to accept beside `x:xmpmeta`; verify before fixing) returns `['xmp:unknown']`
while the same packet under `x:xmpmeta` returns its fields. A child with such a file can keep
it only by naming `xmp:unknown`, which keeps the whole packet, GPS properties included, under
one name: the whole-set keep the delta exists to end, reached through a shape the format
allows. The text rules still scan the packet's values, so a bare phone or email in it is
caught; a GPS coordinate is not. NUL-padded packets also read as unknown (padding is meant to
be whitespace, so that one is defensible).
*Counsel:* accept `(adobe:ns:meta/, xapmeta)` as a second root role; one line and one test.

**GF4 — minor.** *A docstring overclaims by omission.* `inspect_media_fields` (leakscan.py
2295–2303) still says `fields` is "(Exif and GPS so far, 020/450)" and that the function
returns "`(None, [], [])` for anything else"; it returns a 4-tuple and reads IPTC, XMP and PNG
text since part 2. The README and CHANGELOG are right; the code's own account lags.

**GF5 — note.** *The hex guard's one number is unpinned by its tests.* On a scratch copy,
`_HEX_RUN_MIN = 12` and `>` for `>=` both left `PhoneInsideHexDigest` green (the fixtures are a
64-character digest, a 43-character run and an 11-character run). The boundary holds at HEAD
(my probe: a 16-character run is skipped, 15 flags), so this is coverage, not behaviour.
*Counsel:* one 15/16 pair of assertions.

**GF6 — note.** *A type-level line over an Exif block with no entries has a remedy nobody
prints.* Probe: before the date the warning says "it carries no fields"; from the date the block
says "name its fields: it carries none"; `--binary-entries` prints nothing for the file. The
file is clean with the set line deleted (control: exit 0), and no message says to delete it.
Rare shape (most strippers remove the segment), fails closed.

**GF7 — note.** *A privacy guard's reach was narrowed on the author's pick.* `320/470` offered
three options with no principal ruling; the delta took option 1. The narrowing is tight (a
separator-free 9–10-digit run glued inside a 16+ hex run) and the false positive it ends is
real, so I would not hold it; under rule 3 it is still his call, and a one-line confirmation
closes it. Possibly answered in the barred records; reconciled in act 2.

**GF8 — note (lens 4).** *Names come from the packet, and per-file memory is unbounded.* An XMP
prefix bound to two URIs in two `rdf:Description` elements yields two properties spelled with
one prefix (`xmp:q:Thing`, `xmp:q:Other`); a packet that binds `dc` to a foreign URI yields an
`xmp:dc:creator` a line meant for Dublin Core would keep. No privilege is gained (the committer
controls both the packet and the line) and the values are scanned regardless. The `texts`
gathered for one file grow with its text segments (a JPEG of thousands of 64 KiB XMP segments
holds them all before scanning); 160/980 GM14 named the walker's time, this is its space.
Pre-existing, disclosed here so nobody infers a bound that is not there.

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 1 MODERATE (GF1) · 3 minor (GF2, GF3, GF4) · 4 notes
(GF5–GF8). The field-level reader does what it says, names only, fails closed everywhere I
pushed it, and its tests catch the breaks that matter. The one thing owed is a ruling, not a
fix: whose date 2026-12-18 is.

### Re-run ledger (2026-11-15 UTC, worktree root, `python3` first on PATH)

Each line is the brief's, run as written; the first two are abbreviated here to fit.

| Line | Result |
|---|---|
| `... discover -s tools -p test_leakscan.py` (under `nice -n 10`) | exit 0, Ran 422 tests, OK |
| `... discover -s tools -p test_report.py` (under `nice -n 10`) | exit 0, Ran 110 tests, OK |
| `python3 tools/leakscan.py --selftest` | exit 0, "selftest OK" |
| `nice -n 10 python3 -m unittest discover -s tools` | exit 0, Ran 3134 tests in 1118 s, OK |
| `python3 tools/datescan.py <this brief>` | run after act 1 was written; result in the review log |

Load at start 9.89 (1 min), several reviews running; every suite ran one at a time, single
process.

### Follow-up checklist

- [ ] GF1: the principal rules on 2026-12-18 (mandate as built, or warn-only until he rules);
      record who and what kind on the constant, README and CHANGELOG.
- [ ] GF2: `parse_scope` reads or refuses a bare `unknown` after a field; test.
- [ ] GF3: verify the spec's word on `x:xapmeta`; if confirmed, accept it as a root; test.
- [ ] GF4: fix the `inspect_media_fields` docstring.
- [ ] GF5: pin the hex floor with a 15/16 pair.
- [ ] GF6: the empty-set message says "delete the line"; `--binary-entries` notes it.
- [ ] GF7: one-line confirmation of the nz-phone narrowing.
- [ ] GF8: no action; recorded.
- [ ] Act 2: reconcile against the sibling and the barred records; the orchestrator folds the
      sibling and commits.

### Reconcile (act 2), 2026-11-15 UTC

Act 1 was committed unrevised at `de0ec3ef` before anything below was opened. The orchestrator's
release message named one file, the held sibling at a path under the user's configuration
directory (nine questions, two facts, and the brief-writer's re-run results), and opened the
rest of the phase-2 material. I then read: the sibling whole; the three delta commits' message
bodies; `020/450` and `320/470` whole; board items `160/980` and `160/990` whole; the prior G3
verdict `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` where it names the dates
(GM7) and `020/450`; the author session's log `docs/sessions/2026-11-03-0630-queue-run-4c65.md`
and the two later logs that repeat its hand-off lines; and the grep hits for `2026-12-18`,
`type-level` and `320/470` across the records. Three more probes ran on synthetic bytes.

**Against the author's account (commit bodies, `020/450`, the session log).** The bodies claim
what act 1 found: names only; `<set>:unknown` blocks until named; the type-level migration; the
digest guard's separator rule; "whole-tree scan exit 0 before and after". That last claim re-ran
at HEAD: `nice -n 10 python3 tools/leakscan.py --root . .` exit 0 (allow-marker notes only).
The brief-writer's held re-runs (395, 102 and 2,643 tests at `b1f9499`) are consistent with
mine at HEAD (422, 110 and 3,134); the growth is later commits. The held fact that `29021b9` is
a pre-rebase hash and `2ba261b` the landed one matches what I read; `e269f594` was handled as a
non-goal in act 1.

**Per finding.**

- **GF1 (MODERATE) stands, sharpened.** The records confirm the date is the author's: `020/450`
  framed the migration as a choice to "weigh" ("landing before the cut-off, or accepting
  type-level lines with a warning for one more grace"); part 1's body says "a month after the
  2026-11-18 grace ends"; the author's log hands it on as a cleanup ("G3's type-level warnings
  end 2026-12-18; delete that path after it"), and two later session logs carry the same line
  as "unchanged". The one ruling round on these dates (`160/980`, Mike's answers of 2026-11-08)
  put 2026-11-18 to him and he made it firm; 2026-12-18 was never put to him, on any record I
  found. Sibling Q8 asks what happens to the children on the day: by count only, `160/980`'s
  round named three wired children with owed lines at the earlier cut-off; whether any holds a
  type-level line for a read set I did not probe (child repos are read-only to this pass and
  were not opened). The warning prints on every scan from the day a child's pin reaches this
  code, so an affected child is told; who chose the day it is told to meet is the open point.
  *Counsel unchanged:* one ask, two live options, recorded on the constant, README and
  CHANGELOG.
- **GF2 (minor) stands.** `020/450`'s own decisions repeat the README's sentence ("a bare name
  after a `set:Field` continues that set"), so the author's account carries the same gap.
  Sibling Q9 asked exactly whether a parse slip can widen a line to another set: this is the
  one case, and it widens to the `unknown` set, failing closed.
- **GF3 (minor) stands.** No record mentions the legacy root; the design account ("an element
  outside xmpmeta/RDF/Description is `xmp:unknown`") was written without it in view.
- **GF4 (minor) stands.** Documentation only; nothing in the records bears on it.
- **GF5 (note) stands.** Sibling Q1 is the same suspicion at the other end (what a 16+ run
  permits a number to sit in): act 1's probe answers both; the floor is right and unpinned.
- **GF6 (note) stands.** Not in any record.
- **GF7 (note) stands.** The body and `320/470` record the pick ("option 1 ... options 2 and 3
  not taken: the guard removes the cause") with the measured instance (3 of 88 digests in a
  child's record). Sibling Q1 names the same residual. The pick is well-grounded and still his
  to confirm.
- **GF8 (note) confirmed on Q6.** Probe: a packet that binds the prefix `dc` to a foreign URI
  yields `xmp:dc:creator`. Sibling Q6's question ("can that make a hostile URI read as `dc`")
  is answered yes, with the same assessment: no privilege gain, values still scanned.

**Sibling questions not already covered.** Q2 (`_HEX_CHARS` defined after its user): a module
global read at call time; no import cycle exists (`leakscan` is imported, it imports nothing
that imports it back); harmless. Q3 (Exif walker): endianness, offsets, loops and caps are
tested (`ExifFieldParsing`), and a GPS IFD reached twice is walked once (`seen`); what cannot be
walked is `exif:unknown`. Q5 (a nested value under a benign top-level XMP name): the keep is as
wide as the top-level property by the recorded decision ("a property's value, structure
included, is one field"); the name still says what the property is, the values are run through
the text rules, and naming sub-paths would be unbounded. No finding. Q7 (`%XX` injective): yes.
Every byte outside the safe set, `%` included, encodes as `%XX`, so the literal keyword
`%75nknown` encodes as `png-text:%2575nknown` while `unknown` encodes as `png-text:%75nknown`;
no two keywords share a key, and neither collides with the parse-failure field.

**Formed at reconcile, on sibling Q4:**

**GF9 — note (formed at reconcile).** *GPS tag numbers in a chained IFD are named in Exif
vocabulary.* The walker names a tag by the IFD *kind* it was reached through: behind the GPS
pointer (0x8825) tags 0x0002 and 0x0004 are `gps:GPSLatitude` and `gps:GPSLongitude` (probe,
control); the same numbers in an IFD reached by IFD0's next-IFD chain are
`exif:InteroperabilityVersion` and `exif:0x0004` (probe). That is the format's own reading too
(a chained IFD is IFD1, the thumbnail directory, not GPS), so no ordinary tool writes GPS there
and no consumer would read it as GPS; a committer who moved bytes there could as well put them
anywhere. The point is only that a human reading `exif:0x0004` cannot tell from the name what
the value is, which is already the README's stated residual for every by-number tag.
*Counsel:* none beyond the README's existing line on by-number tags; recorded so Q4 has an
answer with evidence.

**Overall, restated: PASS-WITH-FINDINGS** — 0 MAJOR · 1 MODERATE (GF1) · 3 minor (GF2, GF3,
GF4) · 5 notes (GF5–GF9, GF9 formed at reconcile). Every finding is the principal's to decide
(rule 3); nothing has been applied. The orchestrator folds the sibling in below this and
commits; I touched no file but this brief and the open review log.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`de0ec3ef`, landed on
`main` as `464c4748`); folded here verbatim (headings demoted two levels) and the sibling file
removed, per the brief. The orchestrator (a headless Opus 5.5 session started by drain session
`21a271a5`, itself Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Sibling to the g3-field-level-nz-phone-digest cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-g3-field-level-nz-phone-digest-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_leakscan.py`: exit 0 (Ran 395 tests).
- `python3 -m unittest discover -s tools -p test_report.py`: exit 0 (Ran 102 tests).
- `python3 tools/leakscan.py --selftest`: exit 0 (selftest OK).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

#### Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md`

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `_phone_inside_hex_digest`: a real NZ number glued to hex letters, for example in a URL or an id
   `abcd0211234567ef`. What does a 16+ hex run permit that a person's number can sit in? Option 2
   and 3 in `320/470` were not taken.
2. `_HEX_CHARS` is defined after the function. Harmless, but the function reads a module global:
   fine under an import cycle?
3. The Exif walker: endianness, offsets past the block, IFD loops, a SubIFD or the GPS IFD reached
   twice. Does a crafted file make it report a benign field while GPS sits unread, and does unread
   map to `unknown`?
4. A tag the table does not name: named `0x....` and kept by a line that lists it. Can one manifest
   line keep a GPS tag under a hex name that a human reads as harmless?
5. XMP: "one field per top-level property" with a value and its structure as one field. A property
   that nests GPS or a person's name under a benign top-level name: is the keep too wide? The
   principal's example is GPS versus camera model.
6. The XML parse: entity expansion, a packet split across APP1 and extended XMP, duplicate
   properties in two `rdf:Description`s, a namespace prefix redeclared to look like `dc:`.
   "Well-known namespaces use their usual prefix whatever the packet declares": can that make a
   hostile URI read as `dc`?
7. PNG `%XX` keywords and the `%75nknown` escape: is the encoding injective, so one field cannot
   read as another?
8. The dated flip: on 2026-12-18 type-level lines stop keeping. What happens to the children that
   hold them, and is every affected child warned by then?
9. `bare 2:090 continues the same set` and comma-merged fields: can a parse slip widen a line to
   another set?

#### Facts held back from the brief

- The item cites `29021b9` for part 1. That hash is not on `main`; `2ba261b` is the landed commit
  with the same subject. The brief names `2ba261b`.
- `e269f59` (the G3 application) touched the same paths at 2026-11-09 UTC; the item predates it.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

Appended by drain session 21a271a5 at its close (2026-11-16): this pass ran
before the fold step that appends the log, so the log stayed in a
user-local file. Text below is the reviewer's, unedited.

# Review log: atelier 160/990, G3 field-level and nz-phone digest cold pass

Reviewer: Fable 5.1, cold pass, worktree /Users/mike/worktrees/fable/atelier-160-990-1955/atelier.
Spawned by a headless Opus 5.5 orchestrator started by drain session 21a271a5; under Mike's
2026-11-16 06:53 NZDT `/fable-drain` order. Not started or instructed by d4a0fcf3, 74f2b8cd or
4c65083c. Sibling .deferred.md removed from the worktree by the orchestrator (git status shows
it deleted); I will not look for it anywhere.

## Act 1 log (written before the sibling is released)

- 2026-11-15T19:56Z uptime: load 9.89 12.17 10.08; several reviews running. Will nice everything.
- Read the brief in full and docs/method/REVIEW.md in full.
- `git merge-base --is-ancestor 1297df4 HEAD` exit 0: the delta is in the tree.
- Acceptance-test span command run: two quoted spans printed (fields vs data types; one reason
  may cover fields A, B, C if specific). Nothing else of 020/450 read beyond its first line.
- Read only the first line of 020/450 and 320/470 (both `[x]` done 2026-11-03).
- `git log --oneline 1297df4..HEAD -- <delta paths>`: ~50 commits since, including e269f594
  (G3 cold pass application, a brief non-goal except as it bears on HEAD) and 57719bfa
  (bracketed byte fields are not phones; 320/850, 320/840), which touches nz-phone.
- Read body-free via coldsweep --commit (subject, stat, diff only): 7bc0f87 (124 lines), 2ba261b
  (1,335), 1297df4 (1,357). coldsweep left the board-store files out by default (2 in 7bc0f87).
  I named no board file with --path. The nz-phone commit did not touch test_report.py or
  README.md (coldsweep said so).
- Read at HEAD: leakscan.py 355-375 (nz-phone rule), 640-760 (validators, both hex guards),
  1120-1260 (block comment, dates), 1260-1600 (manifest grammar), 1590-2430 (parsers, walkers,
  check_binary), 2660-2775 (--binary-entries), render_type_level, JSON, selftest; README.md
  350-515; CHANGELOG.md 1723-1745, 1786-1812; test_leakscan.py 2561-3410 (every delta test class);
  GUARDS.md 380-430 (mandate/default dates); 320/810 lines 70-85 (names 2026-12-18 as an
  existing flip, not barred).
- RE-RUN 1: `nice -n 10 python3 -m unittest discover -s tools -p test_leakscan.py` exit 0,
  Ran 422 tests OK (48.6 s). Load at start 9.89.
- RE-RUN 2: test_report.py exit 0, Ran 110 tests OK (14.2 s).
- RE-RUN 3: `python3 tools/leakscan.py --selftest` exit 0, "selftest OK".
- Sweeps (coldsweep, brief's exclusions): the function-name pattern hits only leakscan.py,
  test_leakscan.py, test_report.py:691, README.md:487, CHANGELOG 1738/1806, and 320/850 (the
  later byte-field hand-up). The date/type-level pattern adds README 484-491, 578, CHANGELOG
  1723-1806, the exception-register ADR line 97/524 (mentions only), 020/150, 020/440, 320/810:78.
  No mirror in docs/method or skills states the type-level date: one home (README) plus
  CHANGELOG. V3/V4 look clean for the date; checking README 578 next.
- Candidate GF (governance): TYPE_LEVEL_UNTIL 2026-12-18 is the author's pick (CHANGELOG: "a
  month after the G3 grace ends"), fleet-wide, blocking, "no flag or setting moves the date",
  and no surface a child reads says whose choice it is or its kind (GUARDS: an unlabelled date
  reads as a mandate). Same README (382-385) has the provenance warning deferring its block
  date to Mike explicitly. 320/810:78 shows the pattern (agent-chosen flip dates) already named
  as owed to him for later flips. Will reconcile against the sibling in act 2.
- Candidate GF (doc drift): inspect_media_fields docstring (leakscan.py 2297-2303) still says
  "(Exif and GPS so far, 020/450)" and "(None, [], [])" for a 4-tuple return, after part 2.
- Checked, not raising: _HEX_CHARS defined after the function that uses it (module level, fine
  at call time). str.isdigit on Unicode digits: the hex scan stops at once, so the match is
  <16 and never skipped. Expat: DOCTYPE and entity decl both fail the packet; param entities
  never; tests cover a bomb.
- Probes (scratch, synthetic bytes only, /private/tmp scratchpad, deleted at the end):
  - XMP legacy root `x:xapmeta` -> ['xmp:unknown']; `x:xmpmeta` control -> ['xmp:exif:GPSLatitude'].
    Bare rdf:RDF root reads. NUL-padded packet -> unknown; space-padded reads.
  - XMP prefix `q` bound to two URIs in two Descriptions -> both keys spelled `xmp:q:...`; one URI
    under two prefixes -> one spelling (first declared). Names come from the packet.
  - Exif: empty IFD0 -> []; `Exif\x00\xff` pad -> exif:unknown (fails closed); SubIFD 0x014A ->
    exif:0x014A.
  - Hex guard boundary: `0212345678abcdef` (16) skipped, `0212345678abcde` (15) flagged; uppercase  <!-- leakscan:allow:nz-phone: synthetic test fixture in the reviewer's log, not a number -->
    digest skipped; plain phone flagged. Boundary holds at HEAD.
  - Mutations on a scratch copy: `_HEX_RUN_MIN = 12` -> PhoneInsideHexDigest + ByteField 15 tests OK
    (survives); `>` for `>=` -> 6 tests OK (survives). Dropping the GPS pointer -> 19 failures
    (caught). Ignoring attribute-form XMP properties -> 6 failures 2 errors (caught). Grace never
    ending -> 4 failures (caught).
  - `parse_scope("exif:Model,unknown")` -> (['exif:Model', 'unknown'], None): the bare `unknown`
    after a field is the whole `unknown` SET, not `exif:unknown`. README 436-437 says bare names
    continue the set. Fails closed later (stale `unknown` line + unkept `exif:unknown`).
  - Type-level `exif` line over an empty-IFD Exif block: before the date warns "carries no
    fields"; on the date blocks "name its fields: it carries none"; `--binary-entries` prints
    nothing for it. Control: the file with no set line is clean (rc 0). Remedy is deleting the line
    and nothing says so. Rare shape.
- Checked, not raising: main always builds a Tally (leakscan.py 3215), so the type-level warning
  living in the tally is never dropped in production. TYPE_LEVEL_UNTIL is read only by
  in_type_level_grace and for printing: "no flag moves it" holds. README/CHANGELOG/code agree on
  "strictly before the date keeps, from the date blocks".
- /security-review NOT RUN: it reads the session's pending diff, which here is the removed sibling
  (the SL2 exposure) and then this brief; the delta is landed, not pending. Code-altitude read done
  by hand against ASVS V5/V12 input-handling classes (entity expansion, decompression bomb,
  unbounded counts and loops, memory, output leakage); findings GF8 note only.
- Whole-suite re-run started 2026-11-15T20:08Z under nice, moved to background at 600 s (load
  10-13 with other reviews). Waiting for it before writing the re-run ledger.
- RE-RUN 4: `nice -n 10 python3 -m unittest discover -s tools` exit 0, Ran 3134 tests in 1118 s,
  OK (load 9-18 with other reviews; single process).
- Act 1 written into the brief below a `---` divider (469 lines total), Status line updated.
  `python3 tools/datescan.py <brief>` exit 0, clean. Width: every line I wrote is <= 100; the
  over-100 lines left are the brief-writer's (title, paths, commands).
- Verdict: PASS-WITH-FINDINGS, 0 MAJOR, 1 MODERATE (GF1 type-level date's authority), 3 minor
  (GF2 bare `unknown` continuation, GF3 x:xapmeta reads as unknown, GF4 docstring), 4 notes
  (GF5 floor unpinned by tests, GF6 empty-set remedy, GF7 nz-phone narrowing is the author's
  pick, GF8 names from the packet / per-file memory).
- Scratch probes, mutated copy and dumped diffs deleted. Nothing committed; the sibling stays
  deleted in the worktree for the orchestrator. Waiting for the sibling's path for act 2.

## Act 2 log

- Orchestrator released the sibling (one file under ~/.claude/fable-held/) after committing act 1
  at de0ec3ef. Read: sibling whole (9 questions, 2 facts, brief-writer's re-runs), the three
  commit bodies, 020/450 and 320/470 whole, 160/980 and 160/990 whole, the 160/980 prior verdict's
  GM7 lines, session log 2026-11-03-0630 (author) and the two later logs' hand-off lines, and the
  record-wide grep for 2026-12-18 / type-level / 320/470.
- GF1 sharpened: 020/450 framed the migration as a choice to "weigh"; the author's log hands the
  date on as a cleanup; 160/980's ruling round (2026-11-08) put 2026-11-18 to Mike ("Firm") and
  never 2026-12-18. No record puts the type-level date to him. Stands, MODERATE.
- Re-ran the author's "whole-tree scan exit 0" claim: `nice -n 10 python3 tools/leakscan.py
  --root . .` exit 0 at HEAD (allow-marker notes only, no finding).
- Probes for sibling Q4/Q6/Q7: GPS tag numbers behind pointer 0x8825 -> gps:GPSLatitude/
  GPSLongitude; the same numbers in a chained IFD -> exif:InteroperabilityVersion, exif:0x0004
  (new note GF9, formed at reconcile). Foreign URI bound to prefix dc -> xmp:dc:creator (confirms
  GF8 and answers Q6 yes). %XX encoding injective: literal '%75nknown' -> %2575nknown.
- Q2, Q3, Q5, Q7, Q9 answered without a new finding (reasons in the brief's Reconcile). Q8: child
  repos not opened (read-only to the pass); by count, 160/980 named three children with owed lines
  at the earlier cut-off.
- Reconcile appended, Status line updated to VERDICT COMPLETE; datescan on the brief exit 0;
  all my lines <= 100 columns. Final: PASS-WITH-FINDINGS, 0 MAJOR, 1 MODERATE, 3 minor, 5 notes.
- Scratch probes deleted; the rerun-*.txt outputs (test counts only, no secrets) deleted too.
  Nothing committed or pushed. The sibling is left for the orchestrator to fold.
