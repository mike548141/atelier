# Cold pass — leakscan's rules that are off report without blocking, and the narrowed EI6 asymmetry

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a guard or a rule is
doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** VERDICT, acts 1 and 2 written 2026-11-15 UTC by a Fable 5.1 reviewer (below the
divider); the sibling is folded in by the orchestrator at the same commit. Brief written
2026-11-09 UTC by session `d4a0fcf3`, a headless Opus 5.5 brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/994-rule-4-cold-pass-queued-leakscan-reports-off-rules.md`.
**Size of this pass:** medium: about 240 lines of guard code, a design note and a doctrine
paragraph, on the personal-data boundary.
**Why it earns a review:** This is first-of-kind work on the personal-data boundary: a response tier
in leakscan, and the doctrine sentence it narrows. The worst failure is the blocking set shrinking
under cover of an additive change.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `4c65083c`,
  2026-11-03, and the Opus worker it dispatched, which wrote the code and the text (per the queue
  pointer). The author queued this pass and does not take it.
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
  account; the design note whole, every delta commit body-free through `tools/coldsweep.py
  --commit`; commit subjects through `git log`;
  `docs/reviews/2026-11-06-2027-secretscan-public-pem-spans-cold.md` whole, **including that pass's
  verdict and folded sibling** (a different subject, read for house form), the acceptance-test
  section and the status and overall verdict lines of
  `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md` (the counts only), and the opening
  30 lines of board item `160/980`; three lines of `docs/SESSIONS.md` and the opening of
  `docs/sessions/2026-11-06-2022-fable-passes-850e.md`; the results of the re-run lines below. It
  did **not** open any other prior verdict or any delta commit's message body. Its harness also
  loaded user-level and repo instruction files and a memory index, which hold private context this
  brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's answers, printed with `grep -o '"leakscan first"\|"Report-only for off rules"'
docs/roadmap/115-guardrail-architecture-mike-commissioned/090-give-every-guard-a-second-dial-mike-s-2026-07.md`.
They are labels of options he picked; the option text around them is the author's and is barred
until phase 2. `docs/method/SECRETS.md` § *The boundary's posture* states the ruling this narrows
and the narrowing's terms; `tools/leakscan.off-rules.design.md` § 1 states what the delta takes the
answer to authorise. Both are the author's claims to test. The EI6 ruling's own record is a prior
verdict: barred until phase 2 (below).

## What the work is

- **`0477462`** — `leakscan: report rules that are off without blocking`.
- **`e8614ec`** — `secrets: the advisory dial's lead says built, not "not yet built" (115/370)`.

Delta paths, read at each commit and at HEAD:

- `tools/leakscan.py`, `tools/test_leakscan.py`, `tools/leakscan.off-rules.design.md`,
  `tools/floor.py`, `tools/test_floor.py`, `tools/README.md`, `docs/method/SECRETS.md`,
  `CHANGELOG.md`

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor e8614ec HEAD; echo $?
python3 tools/coldsweep.py --root . --commit <sha> --path tools/leakscan.py --path \
  tools/test_leakscan.py --path tools/leakscan.off-rules.design.md --path tools/floor.py --path \
  tools/test_floor.py --path tools/README.md --path docs/method/SECRETS.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). The commit also touches board records; those are barred until phase 2, so always pass `--path`.

Then see what has landed on those paths since, and read anything new the same way, only as far as it
bears on this delta at HEAD: `git log --oneline e8614ec..HEAD -- tools/leakscan.py
tools/test_leakscan.py tools/leakscan.off-rules.design.md tools/floor.py tools/test_floor.py
tools/README.md docs/method/SECRETS.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "Nothing that blocks stops blocking, and a test pins that, so the blocking set cannot shrink"
  (`SECRETS.md`).
- A rule's response is `advisory` "only if it is withdrawn or named in `--disable`" (design note §
  4).
- A report-only finding past the cap is counted in `advisory_over_cap`, "never in
  `findings_over_cap`, which feeds the exit code".
- A blocking shadowed rule is shadowed only by blocking shadowers (design note § 4, the one-span
  rule).
- `clean` and `findings` keep their meaning; a consumer gating on `clean` "gates on exactly what it
  did".
- § 6's blast radius (34 runs over 30 repositories, no exit code moved).
- `e8614ec`: the dial was "built 2026-08-07 (`dcb57fa`)" and the lead said not yet built "for three
  months".

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** demotion of noisy rules (the answer excludes it); datescan's tier (pass `160/988`);
G3 and the phone guard (pass `160/990`).

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
python3 tools/leakscan.py --selftest
cd tools && python3 -m unittest test_floor
python3 tools/floor.py --plane ci --root .
nice -n 10 python3 -m unittest discover -s tools
```

Any figure the delta records from a measurement over repositories or transcripts on the machine is a
recorded proof (V2): re-run it read-only and by count. The brief-writer did not re-run those.

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
verdict in `docs/reviews/`, this brief's sibling (now folded at the end of this file; held by the orchestrator until
act 1 was committed; by count: 7 questions, 2 facts), every other item under `docs/roadmap/160-doctrine-review-owed/` beyond its
title, every delta commit's message body, and these intent records beyond their first line:

- `docs/roadmap/115-guardrail-architecture-mike-commissioned/090-give-every-guard-a-second-dial-mike-s-2026-07.md`

The EI6 ruling's record, `docs/reviews/2026-07-29-1243-e6-intent-cold.md`, is a prior verdict: phase
2 only. Until then read its statement in `docs/method/SECRETS.md`.

The delta's own docstrings, comments, README, design note and `CHANGELOG.md` entries carry the
author's account of why; they are the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/115-guardrail-architecture-mike-commissioned/090-give-every-guard-a-second-dial-mike-s-2026-07.md \
  'WITHDRAWN|advisory_over_cap|def blocks|REPORT-ONLY|BlockingSetPinned'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`LO`: `LO1`, `LO2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1, 2026-11-15 UTC

**Status:** VERDICT, act 1 written 2026-11-15 UTC; act 2 (reconcile against the sibling and the
barred records) pending the orchestrator's release.

### Provenance, repeated (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection, in a session started for
  this pass alone. Review worktree: `/Users/mike/worktrees/fable/atelier-160-994-1934/atelier`,
  read-only to me except this file.
- **Spawn chain:** a headless Opus 5.5 orchestrator, itself started by drain session `21a271a5`
  (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the context partition, form no
  finding and write no severity. The orchestrator's prompt carried the worktree, the brief path, the
  run constraints and this provenance; it framed nothing about the work. No contact with the brief's
  barred sessions (`d4a0fcf3`, `74f2b8cd`, `4c65083c` and anything it started).
- **Authority:** the principal's `/fable-drain` order of 2026-11-16 06:53 NZDT (2026-11-15 UTC),
  lapsing at the weekly reset; a pass already running may finish.
- **What I read, act 1:** this brief whole; `docs/method/REVIEW.md` § lenses, checklist and
  lifecycle; the two delta commits body-free through `tools/coldsweep.py --commit --path`
  (`0477462`: 8 files; `e8614ec`: `SECRETS.md` only, its 3 board-store files left out); the delta
  paths at HEAD (`leakscan.py`, `test_leakscan.py`, `floor.py`, `test_floor.py`, `README.md`,
  `SECRETS.md` § *The boundary's posture*, the design note, the `CHANGELOG.md` entries); the
  `git log --oneline` of later commits on those paths (subjects only); `docs/method/GUARDS.md`
  § *Ruled 2026-11-09*; `tools/pre-commit.sample`; the two acceptance-test labels through the
  brief's `grep -o`; the existence (not the content) of the three files `SECRETS.md` links. Sweeps
  ran through `coldsweep` with the brief's exclusions; `--include-barred` was not used. The
  sibling `.deferred.md` was absent from the worktree and I did not look for it elsewhere. My
  harness loaded user-level and repo instruction files and a memory index, which carry private
  context this verdict does not.
- **Review log**, open by design: `~/.claude/fable-drain/notes/atelier-160-994-1934.md`, every
  check and its evidence as it was run.

### Load-bearing assumptions, named first (lens 1)

- **A1** The exit code is a function of blocking findings alone, on every plane. Probe: CLI
  probes; mutations M5, M6; staged and floor-hook probes from a scratch repo. Confirmed.
- **A2** The only ways a rule becomes report-only are `WITHDRAWN` membership and `--disable`;
  the term list and binary gate cannot be moved. Probe: `blocks()` read; `--disable local-term`
  and `--disable binary-unlisted` both exit 2; mutations M1, M2, M9. Confirmed.
- **A3** A shadow never costs a blocking finding. Probe: `_shadow_spans` read; the MAC probe
  (ipv6 blocks, mac-address reports); mutations M3, M3b. Confirmed.
- **A4** The pin test would catch a shrinking blocking set. Probe: mutation M8 (withdraw `nz-ird`
  by name). Confirmed: killed, 3 failures and 15 errors.
- **A5** The 2026-10-16 answer authorises exactly this and nothing wider. Probe: acceptance grep;
  `SECRETS.md` and design § 1 wording; GUARDS § *Ruled 2026-11-09*. Damaged in one respect: LO1.
- **A6** `--disable` is "not a softening" of leakscan (the `floor.py` comment; the design's
  "narrows nothing at all"). Probe: GUARDS.md's lowering table and its open question `020/170`.
  Damaged: LO1.
- **A7** The blast radius is as recorded (30 repos, 34 runs, no exit code or blocking count
  moved). Probe: re-run, pre vs post tool, counts only. Confirmed in structure; counts drifted
  (LO5).
- **A8** Every scanning path carries `disabled` through, so a disabled rule reports on every
  plane. Probe: call-site read (staged, path name, metadata, messages); mutations M11, M12. Holds
  live; untested (LO3).

### Lens 1 — approach and assumptions

Right problem, right altitude, right shape, with one doctrinal loose end. The answer the delta rests
on ("Report-only for off rules") is the narrower of the two labels the acceptance grep prints, and
the delta takes exactly that: no rule is demoted, the fifteen structural rules and the term list
still block, and the two kinds of "off" (withdrawn, disabled) are the only ones made to report. The
response tier is secretscan's shape reused, the count line is the floor's existing contract, and
the exit code is computed from blocking findings alone on every path I could reach (A1–A3, A8).
The loose end is A5/A6: the delta turns `--disable` from a scope narrowing into a per-rule response
lowering (its own words: it "narrows nothing at all"), and the doctrine at HEAD has not followed
(LO1).

### Lens 2 — correctness and quality: the claims, re-driven

- *Nothing that blocks stops blocking; a test pins it* (`SECRETS.md`, README, CHANGELOG). Pin
  list at HEAD is the 15 `STRUCTURAL` names; M8 killed (3 failures, 15 errors). Holds.
- *Response is `advisory` only if withdrawn or in `--disable`* (design § 4). `blocks()` read; M1,
  M2, M9 killed; the term list and the binary gate refuse `--disable` (exit 2). Holds.
- *Report-only past the cap counts in `advisory_over_cap`, never the exit code* (design § 4).
  `take_finding_slot(blocking)` read; M4 killed. Holds.
- *A blocking shadowed rule is shadowed only by blocking shadowers* (design § 4, D5).
  `_shadow_spans` read; probe: `--disable mac-address` leaves ipv6 blocking a MAC and mac-address
  reporting; M3, M3b killed. Holds, with the § 5 duplicate as named.
- *`clean` and `findings` keep their meaning* (design § 3). JSON probe; M5, M6 killed. Holds.
- *§ 6 blast radius: 30 repos, 34 runs, no exit code moved.* Re-run pre vs post tool, counts
  only. Structure holds exactly; magnitudes drifted (LO5).
- *`e8614ec`: dial built 2026-08-07 (`dcb57fa`), lead stale "three months".*
  `git show -s --format=%h %ad %s dcb57fa`: 2026-08-07, the secretscan second-response commit.
  Holds.
- *The count line prints on every run, zero included* (design § 3). Clean-tree probe prints
  `0 finding(s)`; floor reads the last match. Holds.
- *The hook plane prints the hits on the lines a commit adds* (design § 3). Staged probe from a
  scratch repo, and floor `--plane hook` with `flags`: exit 0, block shown, board line
  `🟡 leakscan enforced`. Holds.
- *`--disable` refuses a withdrawn rule's name* (design § 2). Probe: exit 2 with the withdrawn
  message; M13 survives, so the test pins only the code (LO4). Holds; weakly tested.

No overclaim found in the delta's own text. The one statement that reads wider than its evidence is
`floor.py`'s "NOT a softening" beside `advisory_count=True`: true of the floor FORM (`advisory=None`
is unchanged), contestable of the flag (LO1).

### Lens 3 — completeness and harvest

- Surfaces that state the behaviour (V3): `SECRETS.md` (home), README § *Rules that are off*,
  `leakscan.py` module docstring and the two E6a comments, `floor.py` registry comment and module
  docstring, CHANGELOG 2026-11-03, the design note. All agree on scope ("rules that are off"; "for
  a rule that blocks"). One later mirror drifted (LO2). datescan has since copied the pattern
  (`160/988`'s subject; not read for this pass).
- Harvest: the shape is secretscan's tier, the count contract is `report.advisory_count_line`, the
  cap split is secretscan's. Nothing duplicated that already existed.
- Tests that stay green on a broken delta: M11, M12, M13 (LO3, LO4). Every other mutation I tried
  (ten) was killed, most by more than one test.

### Lens 4 — security and privacy

- **Design altitude.** The change moves hits from unseen to seen; it collects nothing new and
  blocks nothing less. What it exposes: a report-only hit is printed, redacted, on every CI run for
  as long as it stands, where a blocking hit is printed once and removed. On a public repo the
  Actions log is public; the content it describes already is, and `redact()` leaves three leading
  and two trailing characters plus a length. Bounded; accepted as designed. The surfacing question
  EI1 asked (durable, acknowledged?) is answered as secretscan's was: the CI log and the board line,
  no acknowledgement; the count never reaches the fleet view (part of LO1's evidence).
- **Code altitude**, checked against ASVS V5 (input validation) and V8 (data protection) as they
  apply to a CLI scanner: `--disable` names are validated against `STRUCTURAL` (unknown, withdrawn,
  binary and `local-term` all exit 2); excerpts pass through `redact()` on both blocks; the new
  regex has no nested quantifier and sits behind a two-part gate; `Finding.response` defaults to
  block; the JSON change is additive; no new file write anywhere in the delta. The G3 reader keeps
  `honour_markers=False`.
- **`/security-review`: discharged with grounds.** The delta is landed, not pending; the tree was
  not clean at any point of this run (the sibling's deliberate deletion, then this file), and the
  scanner reads the session's pending diff, so aiming it would have scanned the brief. The
  code-altitude read above was done by hand.

### The standing checklist

- **V1** — No claim stronger than its evidence: one, `floor.py`'s "NOT a softening" (LO1); the
  rest hold (lens 2 table).
- **V2** — Recorded proofs re-run: § 6 (structure reproduces, counts drifted, LO5); `dcb57fa`
  (holds); the brief's five lines (re-run ledger).
- **V3** — Mirror sites swept with `coldsweep`: one drifted (LO2); the rest agree.
- **V4** — One home: `SECRETS.md` § *The boundary's posture* holds the narrowing; README and the
  design note point at it. Discharged.
- **V5** — No contradiction: `SECRETS.md`'s three links reach files that exist; the EI6 record is
  pointed at, not opened (phase 2). GUARDS.md's 2026-11-09 lowering table and the delta's account
  of `--disable` do not agree (LO1). CHANGELOG 2026-11-10 contradicts CHANGELOG 2026-11-03 on the
  same page (LO2).
- **V6** — Lens 4 above; `/security-review` discharged with grounds.
- **V7** — Provenance stated above and in the brief.

### Per-commit ledger

- `0477462` leakscan: report rules that are off without blocking — read body-free, yes
  (`coldsweep --commit --path` × 8 paths; 0 barred files touched). Findings: LO1, LO3, LO4.
- `e8614ec` secrets: the advisory dial's lead says built — read body-free, yes
  (`coldsweep --commit --path docs/method/SECRETS.md`; 3 board-store files left out). None.

Later commits on the delta paths were read as subjects only, and the paths at HEAD in full.

### Findings

**LO1 — MODERATE (doctrine; lens 1, V5).** Since this delta `--disable` lowers a rule's response
from block to advisory; the doctrine at HEAD classes it as something else and leaves the question
open. The design says the flag "narrows nothing at all" and that a rule's response is advisory
"only if it is withdrawn or named in `--disable`"; `floor.py`'s registry comment says this is "NOT
a softening". `docs/method/GUARDS.md` § *Ruled 2026-11-09* says a repo may lower a check's response
"only with a written reason and an end date, visible in the fleet view", then classes `scope` /
`flags` as "not as a lowering" with no end date, on a 2026-07-28 ruling made when `--disable`
dropped hits (a narrowing), and closes with "whether narrowing counts as lowering a *response* ...
is not built or decided here (`020/170`)". At HEAD, `_load_flags` accepts `args` and `why` only,
and `floorfleet.py` carries no advisory count, so a child's `--disable` on a personal-data rule is a
lowering with a reason, no end date and no fleet-view line. The GUARDS ruling post-dates the delta
by six days, so the delta broke no rule that stood when it landed; the contradiction is at HEAD.
Nothing in the blocking set moved. *Counsel:* decide `020/170` with `--disable` named. Either (a)
it is a lowering: `flags` learns `review-by` as `advisory` and `disabled` have, and the fleet view
carries leakscan's count; or (b) the 2026-07-28 permanent-fact ruling stands for `flags` because
the hits now report (the design's own argument), stated in GUARDS's table, with `floor.py`'s "NOT a
softening" citing it.

**LO2 — minor (V3, V5).** `CHANGELOG.md` line 107 (the 2026-11-10 `leakscan --messages` entry,
`320/550` part (a)) says "`leakscan` has no advisory form, so it would block every message body",
unqualified, about sixty lines above the 2026-11-03 entry that narrows that rule. `SECRETS.md` says
"for anything that blocks". Formed against a later commit on the lane pass `160/1420` covers;
recorded here as the drift of this delta's rule, not re-reviewed. *Counsel:* qualify the sentence.

**LO3 — minor (lens 3, tests).** The staged plane (`leakscan.py` near line 3283) and the image
metadata reader (near line 2381) pass `disabled` through, and no test pins either: replacing
`disabled` with `frozenset()` at either call site leaves all 422 tests green (M11, M12). A disabled
rule would then block on the hook or inside metadata while reporting in CI: fail-closed, so not a
shrink, but "on every run" would be false on one plane. The live staged and floor-hook probes show
both currently carry it. *Counsel:* one staged and one metadata case in `DisabledClassReports`.

**LO4 — note (tests).** `test_disable_cannot_name_a_withdrawn_rule` asserts exit 2 only. With the
withdrawn-rule refusal removed (M13) the unknown-name check still exits 2, so the message the design
promises ("already reports without blocking, and `--disable` never silences a report") is untested.
*Counsel:* assert the wording.

**LO5 — note (V2).** § 6's disabled-class counts (56, 241, 2,652; 10 in-scope `diagnosis-key`) do
not reproduce on 2026-11-15 (58, 260, 6,216; 11): repo content moved in twelve days. Everything
structural reproduces: 30 repositories, 34 runs, 4 with declarations, no exit code or blocking
count moved, `diagnosis-key` whole-tree counts 1, 1, 3, 11. The note is dated; no action.

**LO6 — note (housekeeping, later commit).** `_active_rules`'s docstring (`leakscan.py` line 890)
carries a stray run of spaces mid-sentence and an over-long line, introduced after this delta.

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR · 1 MODERATE (LO1) · 2 minor (LO2, LO3) · 3 notes (LO4, LO5,
LO6). The blocking set did not shrink, under cover or otherwise: the pin holds, the exit code is a
function of blocking findings on every path reached, and the estate re-run moved nothing. The one
MODERATE is doctrinal: what `--disable` now *is* has not been ruled on, and the doctrine at HEAD
says two things about it.

### Re-run ledger

- `python3 -m unittest discover -s tools -p test_leakscan.py` — `/usr/bin/python3` (3.9): Ran
  422, OK, exit 0.
- `python3 tools/leakscan.py --selftest` — 3.9: `selftest OK`, exit 0.
- `cd tools && python3 -m unittest test_floor` (run as a subprocess with `cwd=tools`) — the PATH
  `python3` (3.14); 3.9 refuses it, the suite needs 3.11+: Ran 255, OK, exit 0.
- `python3 tools/floor.py --plane ci --root .` — 3.9: exit 0; atelier's own board line reads
  `🟡 leakscan enforced (... 3 advisory finding(s))`.
- `nice -n 10 python3 -m unittest discover -s tools` — 3.14: Ran 3134, OK, exit 0 (1,095 s).
- § 6 blast radius, pre (`0477462^`) vs post (`0477462`) tools, counts only — 3.9, `nice -n 10`,
  782 s: 34 runs over 30 repos, 0 moved.

Load: `uptime` 8.6 at start, 3.8–11.8 during; one heavy process at a time, all under `nice -n 10`.

### Follow-up checklist (the principal's to decide; nothing applied)

- [ ] LO1: rule on `020/170` with `--disable` named (a lowering with an end date, or a declared
      permanent fact), and align GUARDS's table and `floor.py`'s comment to the ruling.
- [ ] LO2: qualify CHANGELOG line 107 (or let `160/1420` carry it).
- [ ] LO3: staged and metadata cases with a disabled set.
- [ ] LO4: pin the withdrawn-refusal wording.
- [ ] LO6: tidy the docstring.
- [ ] Act 2: reconcile against the sibling (7 questions, 2 facts) and the barred records.

### Reconcile

Act 2, 2026-11-15 UTC, after act 1 was committed unrevised (`b7cd9648`). Opened then, and not
before: the sibling (7 questions, 2 facts, the brief-writer's re-run results); the intent record
`115/090` whole; the EI6 record (`EI5`, `EI6`, the rulings); `00-APEX.md` § *The principal's
authority is absolute*; the `115/090` lines of the author sessions' logs (2026-11-03 and
2026-11-06); both delta commit bodies; the queue pointer; and the status and overall lines only of
the 2026-10-17 advisory-count pass the sibling names. Nothing above the divider is revised.

**Against the sibling's questions.**

1. *Does "report" create the exposure EI6 guarded against; what is printed?* Act 1, lens 4: the
   excerpt is redacted (three leading and two trailing characters and a length), the same as a
   blocking hit's, and describes content already in the tree. EI6's object was the blocking set,
   which did not move. No finding.
2. *Is a count nobody acts on cover, not coverage; is the board the consumer EI1 asked for?* The
   design answers with the per-run board count, which act 1 confirmed on both planes, and names
   "read, not acted on" as the accepted cost (design § 5). The count never reaches the fleet view;
   that is already LO1's evidence. One declared run now reports 6,216 hits, a list nobody will read
   line by line; that is the answer's cost, not an overclaim. No new finding.
3. *Is the pin list derived or hand-kept?* Hand-kept. The suite asserts every pinned name is in
   `STRUCTURAL` and that `STRUCTURAL` and `WITHDRAWN` are disjoint, but not that every `STRUCTURAL`
   name is pinned. A rule added after 2026-11-03 and later moved to `WITHDRAWN` leaves the blocking
   set with the pin green. Not probed in act 1. **LO7, below, formed at reconcile.**
4. *Is `blocks()` the only path?* Act 1 A2 and M9: every structural finding takes its response from
   `_active_rules`, which calls `blocks()`; term-list, binary and path-name findings default to
   block, and the staged, metadata and message lanes all go through `scan_lines`. No other path.
5. *Can a child now disable a blocking rule more cheaply because it "still reports"?* This is LO1's
   substance. The intent record's first answer said a child's `--disable` of a whole class "should
   be weighed against that"; the build did not weigh it, and GUARDS left the question open. LO1
   stands, with that line as added evidence.
6. *Other double counts from the shadow asymmetry?* `SHADOWED_BY` has one entry (`ipv6` by
   `mac-address`), so the MAC is the only one. None.
7. *The authority chain against the informed-ruling test.* The intent record shows the 1501 run
   holding the build, re-briefing with EI6 stated and "keep EI6" offered, and the principal
   choosing the narrow option. `00-APEX.md`'s condition (a ruling is challengeable on whether he
   was informed) is met for the second answer; the first is not relied on, as design § 1 says.
   Holds.

**Against the author's account.** The `0477462` body matches the delta as read; it changes no
finding, and its "no exit code or blocking count moved" is the claim act 1 re-ran. The `e8614ec`
body dates the consumer to 2026-08-04 (not checked); the dates the lead itself states were. The
item record says "new report-only counts in 6 repos, the largest 2,662"; design § 6 says 2,652 for
the same run. **LO8, below, formed at reconcile.** The sibling's re-run results (395, 187 and 2,643
tests on 2026-11-09) sit below act 1's (422, 255, 3,134), as later landings would have it, and its
Python 3.9 import error on `test_floor` reproduced.

**Findings formed at reconcile.**

**LO7 — minor (lens 3, tests; formed at reconcile).** `BlockingSetPinned` pins the fifteen rules
of 2026-11-03 but does not require every `STRUCTURAL` rule to be pinned, so a rule added later and
then withdrawn would narrow the blocking set with the suite green. The design's "adding a rule is
welcome" makes the gap deliberate for additions, not for a later withdrawal of one. *Counsel:* one
assertion that the pinned names equal `STRUCTURAL`'s, so a new rule arrives with its fixture.

**LO8 — note (V5, records; formed at reconcile).** One measurement, two figures: the design note
says the largest disabled-class count was 2,652 and the item record says 2,662. Both are dated
records, so a correcting line beside the wrong one, not an erase.

**Per-finding.** LO1 stands, strengthened (question 5). LO2, LO3, LO4, LO6 stand. LO5 stands; the
sibling's "6 repos" reading matches the re-run (six repositories with a non-zero count).

**Overall, restated:** **PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE (LO1) · 3 minor (LO2, LO3,
LO7) · 4 notes (LO4, LO5, LO6, LO8).**

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`b7cd9648`); folded here
verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (a headless Claude Opus 5.5 session started by drain session `21a271a5`) formed no
finding and wrote no severity.*

### Sibling to the leakscan-off-rules cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

#### Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_leakscan.py`: exit 0 (Ran 395 tests).
- `python3 tools/leakscan.py --selftest`: exit 0 (selftest OK).
- `cd tools && python3 -m unittest test_floor`: 187 tests, OK, exit 0 (Python 3.14.6).
- `python3 tools/floor.py --plane ci --root .`: exit 0 (Python 3.14.6), `leakscan advisory: 3
  finding(s)`.
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

#### Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-07-29-1243-e6-intent-cold.md`
- `docs/reviews/2026-10-17-1010-advisory-count-per-scanner-cold.md`

#### Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. EI6 said no advisory form because a leak cannot be rotated. An off rule that now reports prints
   the matched personal data into CI logs and a board count: a public repo's log, for a rule the
   repo chose to turn off. Does "report" create the exposure EI6 was protecting against? What does
   the output print: value, redacted, or none?
2. The withdrawn `diagnosis-key` rule reports across repositories. At 11 and 2,652 findings, is a
   count nobody acts on "cover, not coverage" (EI1), and is the board's count the consumer EI1 asked
   for?
3. `BlockingSetPinned` lists fifteen rules. Is the list derived, or hand-kept so a new rule escapes
   it?
4. `blocks(rule, disabled)` is "the single decision". Is it the only path, or can a finding
   constructed elsewhere reach the report with no response?
5. `--disable` is a flag in `.atelier-floor.json`: can a child now disable a blocking rule more
   cheaply because it "still reports", so the tier makes a narrowing feel safe?
6. The MAC duplicate in § 5 is named. What other double-counts does the shadow asymmetry make?
7. The ruling's authority chain: the first answer was given before EI6 was shown. Read the question
   text at phase 2 against `00-APEX.md`'s informed-ruling test.

#### Facts held back from the brief

- At this HEAD the ci plane prints `leakscan advisory: 3 finding(s)` on this repo, all
  `diagnosis-key` shape.
- `tools/test_floor.py` fails to import on the system Python 3.9.6 here; passes on 3.14.
