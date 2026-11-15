# Cold pass — the ladder gains a floor: framing always, a mechanism by value (`020/240`)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 2 WRITTEN 2026-11-15 UTC — PASS-WITH-FINDINGS (0 MAJOR · 2 MODERATE · 3 minor ·
2 notes). Act 1 landed `fa7a0306`; reconcile appended; sibling folded by the orchestrator.
**Sizing:** **small** — one commit, one 27-line passage plus a changelog entry; no code.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1110-rule-4-cold-pass-queued-ladder-floor.md`.
**Why it earns a review:** This sets what every rule in the house is owed and when a rule gets a
check, so it decides where guard work goes. Worst failure: an obligation on every rule that no
session can meet, so the record reads as if weighing had happened when it had not.

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
- the queue pointer whole; the intent record whole;
- the delta body-free through `tools/coldsweep.py --commit 4458a157` (subject, stat, diff, never the
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

The principal's pick of 2026-11-09, as the passage quotes it: *"Written always, checker by value"*,
an answer to options offered and not a ruling in his own words; and his words of 2026-11-08 on
`115/170`, quoted there: *"This sounds like yet another artifical limit that is not helpful. It is
about balancing importance and priority to do the work that is most valuable"*.

## What the work is

One commit on `main`, `4458a157` (first confirm your tree has it: `git merge-base --is-ancestor
4458a157 HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 4458a157 \
  --path docs/method/PROPAGATION.md \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 4458a157..HEAD -- docs/method/PROPAGATION.md CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- Framing is owed by every rule up front: rung 1 made a design obligation, not a remedy.
- A mechanism is owed only where its value beats its cost, ranked against all other work; recurrence
  is the usual evidence, not the only one.
- The ladder's climbing rule is unchanged.
- A check not built is a decision with its reason recorded, not silence.
- No blanket check-building follows.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** The census (`020/220`) and the framing obligation's review-time check (`020/230`),
which the delta says it does not do.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. No security or privacy surface in the passage itself.
Discharge in one line with grounds, or say what you found.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- the floor at HEAD: `nice -n 10 python3 tools/floor.py --plane hook --root .` and `--plane ci`

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
`docs/reviews/2026-11-09-0126-ladder-floor-cold.deferred.md`, every delta commit's message body, and
the intent record
`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/240-the-posture-change-this-implies-stated-so-it-i.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1110-rule-4-cold-pass-queued-ladder-floor.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/240-the-posture-change-this-implies-stated-so-it-i.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`4458a157`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `LF`: `LF1`, `LF2`, …) and severities (MAJOR /
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

## Verdict — act 1, written cold on 2026-11-15 UTC

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 1 note** (LF1–LF6 below).
The passage says what it set out to say, labels the status of the principal's words honestly, and
contradicts no ruling I could find. What it leaves unhomed is the record its own floor demands.

### Provenance (V7, rule 4)

- **Reviewer tier:** Fable 5.1 (`claude-fable-5-1`), the principal-named review tier, checked at
  selection. The judgement that forms every finding and severity below is this session's alone.
- **Spawn:** a subagent started by orchestrator session `bb3a9a14` (Opus 5.5), itself started by
  drain session `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the
  context partition, form no finding and write no severity. Neither is, nor was started or
  instructed by, any session on the brief's barred list (`722ac2e2` and everything it started,
  `84e3aa7f`, `74f2b8cd`).
- **The principal's approval:** the weekly Fable drain order. On 2026-11-16 06:53 NZDT
  (2026-11-15 17:53 UTC) he invoked `/fable-drain`, the command the drain skill names as his order
  to spend the weekly Fable budget on briefed cold passes; approval lapses at the reset
  (2026-11-15 23:00 UTC) and a pass already running then may finish. This pass started at
  2026-11-15 21:54 UTC.
- **Orchestrator direction, disclosed:** process only — the worktree and brief paths, the finding
  prefix, the barred list restated from this brief, the deliverable's shape (act 1 below a
  divider, then `### Reconcile` on release), the log file to keep, the load, live-system and
  no-write rules, and that the orchestrator does the fold and the sibling deletion. It contained
  no question about the delta, no pointer to where risk lives, and no request about any finding.
  The verbatim spawn prompt sits in the orchestrator session's transcript; the orchestrator may
  attach it at the fold. The release message will be recorded in act 2.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1110-2152/atelier` at HEAD `6cf077af`,
  read-only to me except this file. The sibling `.deferred.md` was removed from the worktree by
  the orchestrator before I started (the partition); the only dirty path is that deletion.
- **UTC day run:** 2026-11-15 (`date -u` at start: 21:54 UTC).
- **Work log:** a step-by-step log of commands, files read and what each showed was kept outside
  the repo during the run; the orchestrator appends it to this file at the fold.

**What I read (exposure, disclosed):** this brief whole; `docs/method/REVIEW.md` whole;
`docs/method/PROPAGATION.md` 987–1100 at HEAD; the delta body-free through `coldsweep --commit
4458a157 --path … --path …` (subject, stat, diff; body not printed); commit subjects of
`4458a157..HEAD` on the two delta paths and on `docs/method/GUARDS.md`; `docs/method/GUARDS.md`
151–213, 350–382, 648–691; `docs/method/RECORD.md` 478–496; `CHANGELOG.md` 1366–1388; grep hits in
`ECONOMICS.md`, `00-APEX.md`, `CONVENTIONS.md` (lines 57, 59), `PRINCIPLES.md`; board items
`115/170`, `020/220`, `020/230` whole (none barred; `020/230` is the author's own framing of
track (b), read as a cited source and weighed as a claim); `docs/roadmap/200-…/README.md` 18–30
and 70–80; the first line of `020/240` (its title). The CI floor run printed two barred paths with
14-character redacted snippets (`docs/SESSIONS.md:87`; a 2026-08-02 verdict, line 29) — no account
of this delta reached me through them. The harness loaded user-level instruction files and a
memory index that hold private context; none of it concerns this delta and none is carried here.

**What I did not read, and why:** the sibling, the queue pointer `160/1110`, `020/240` beyond its
title, `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior verdict in
`docs/reviews/`, and the delta commit's message body — all rule-2 barred until act 2. No live
system was read: the delta is doctrine prose with no live surface. `/security-review` was NOT RUN
(grounds under lens 4).

### Method — what I examined and how

1. Confirmed the tree holds the delta: `git merge-base --is-ancestor 4458a157 HEAD` → exit 0.
2. Read the delta body-free with `coldsweep --commit` (exit 0; "0 board-store file(s) … none
   touched"), then the passage in place at HEAD and the section around it (rungs 1–3, the
   countable-trigger and mining paragraphs that follow it).
3. Checked whether any of the 20 later commits touching `PROPAGATION.md` altered the passage:
   `git diff 4458a157 HEAD -- docs/method/PROPAGATION.md` has no hunk containing "What is owed",
   "Written always", "beats its cost" or "is never skipped" (count 0). The passage at HEAD is the
   passage that landed.
4. Verified the quoted words against their source: the `115/170` item's ANSWERED paragraph carries
   *"This sounds like yet another artifical limit that is not helpful. It is about balancing
   importance and priority to do the work that is most valuable"* character for character with
   `PROPAGATION.md` 1066–1068. The `020/240` pick cannot be verified until act 2 (barred).
5. Swept mirrors with `coldsweep` and the brief's two `--also-exclude` paths, ten patterns, each
   exit 0 over 841 files with 569 excluded as barred (hits under V3/V5 and LF3).
6. Read the sibling doctrine the passage must agree with: GUARDS.md's evidence window and
   rule-with-no-home test, RECORD.md's "recurrence, not severity" ruling, ECONOMICS and APEX.
7. Dated the delta: author `2026-11-09T01:04:49+13:00` = `2026-11-08T12:04:49Z`; committer
   `2026-11-08T12:33:17Z`. Checked CONVENTIONS.md's at-rest rule.
8. Re-ran both floor planes, niced, one at a time, `uptime` first (ledger below).
9. Looked for a test, skill, template or index that pins or points at the passage (none).

### Lens 1 — approach and assumptions, named first

- **A1 — The ladder's climbing rule is unchanged by the floor.** Probe: rung 2 at HEAD still reads
  *"Recurrence, not severity, is what earns a check"* (1027), while the floor says recurrence is
  *"the usual way a rule qualifies, not the only one"* (1056–1057). The *climbing* rule (stop at the
  first rung that would have prevented the recorded occurrences) is indeed unchanged; the
  *earning* rule is changed in substance and the old sentence was not touched. **Partly damaged
  → LF3.**
- **A2 — The principal's words bear the weight put on them.** Probe: `115/170` records his words
  verbatim as an answer to "cap guard work at about half / no limit / freeze", and the item's own
  reading is "every item, guard or not, is ranked by its value against the rest". The floor's
  second bullet is that reading applied to checks, and the passage labels both the 2026-11-09
  pick and the 2026-11-08 words correctly (an answer; his words). The step from "ranked by value"
  to *"no rule is owed one by existing"* is the author's inference, and the text presents it as the
  answer's consequence, not his words. **Confirmed, with that caveat noted; no finding.**
- **A3 — The framing obligation is stated here as doctrine, and the work of `020/230` remains.**
  Probe: `020/230`'s whole text asks for one thing, that rung 1 become *"a design obligation on
  every rule, up front"*; the passage's first bullet states exactly that, in near-identical words.
  The changelog says `020/230` is *"not done by this change"* and the item stays open with no
  remainder written. The brief's gloss ("the framing obligation's review-time check") appears
  nowhere in the item. **Damaged → LF2.**
- **A4 — "A check not built is a decision with its reason recorded, not silence" can be met.**
  Probe: the passage names the census (`020/220`, open, unrun) as where *"each rule stands"*. For
  the stock of rules at census time that is a home; for a rule written after it, no surface, no
  moment and no record shape is named, and GUARDS.md § *A rule with no home is not a rule* gives
  the test the obligation fails (*"name the surface a future session reads it on"*). **Damaged →
  LF1.** This is the brief's own stated worst failure, and it is partly present.
- **A5 — The floor is homed where a rule-writer will stand.** Probe: it sits inside a section
  titled *When a rule keeps breaking — climb, never restate*, whose first sentence says it is
  *"for a rule that has broken"*; `docs/method/README.md` names the file in one line and neither
  the ladder nor the floor; no writer-facing surface points at it. A rule-writer deciding what a
  new rule owes is not the reader this section is keyed to — rung 1's own defect, applied to the
  floor. **Damaged, low weight → LF6 (note).**
- **A6 — Dates are in the at-rest frame.** Probe: the pick is dated 2026-11-09 three times (the
  subsection title, the body, the changelog heading) and the commit carrying it was authored at
  2026-11-08T12:04Z, so the pick was made on 2026-11-08 UTC at the latest; the same paragraph
  dates the `115/170` words 2026-11-08. CONVENTIONS.md: *"UTC at rest; local on presentation"*.
  **Damaged → LF5** (confirmation against the pointer and `020/240` owed at act 2).
- **Right problem, right altitude?** Yes to the problem: the programme's aim needed the prior
  question answered before any census could label a rule "unenforceable, accepted". Altitude is
  right for a two-part answer and one paragraph; what is under-built is the record half (LF1).
  The brief's account of the work (one commit, two paths) is accurate: `git show --stat` lists
  exactly those two files.

### Lens 2 — correctness and quality

Each claim the brief extracted, checked against the text that makes it:

- *Framing is owed by every rule up front* — stated at 1049–1052; consistent with `020/230`'s ask;
  overclaim only in the changelog's "not done" line (LF2).
- *A mechanism is owed only where its value beats its cost* — stated at 1053–1057; consistent with
  the `115/170` answer; reads as the whole test where GUARDS.md's evidence window is the prior,
  feasibility test (LF4).
- *The climbing rule is unchanged* — true of climbing; the earning sentence at rung 2 is now an
  overstatement left in place (LF3).
- *A check not built is a decision with its reason recorded* — stated at 1061–1062 with no record
  surface for post-census rules (LF1).
- *No blanket check-building follows* — stated at 1068–1069; nothing in the tree since contradicts
  it (the later `115/120` and GUARDS work is declaration and reporting, not new blocking checks).
- The passage's labels are honest: the pick is called *"an answer and not a ruling in his own
  words"*; the `115/170` quote is verbatim; the census is named as the output, not claimed done.
- Dates: local-frame in an at-rest record (LF5).

### Lens 3 — completeness and harvest

- Every surface that states the ladder: `PROPAGATION.md` (home), `REVIEW.md` 612–615 (a stamped
  pointer to rung 1 — reached, holds the rule), `docs/roadmap/200-…/README.md` 23 and 74 (a board
  README restating rung 2's exclusion and the three rungs). The delta swept none of the mirrors;
  only the board README now disagrees in wording (LF3). `GUARDS.md` gained a sibling gate the day
  after (LF4).
- One home for "when is a check owed": not yet — the floor (value), the evidence window
  (feasibility) and the census (record) sit in three files with no cross-pointers (LF1, LF4).
- Tests that would stay green on a broken change: none exist for this text and none are owed; the
  floor is prose. The floor planes pass at HEAD and would pass with the passage deleted, so
  "green" here means only that the surface is clean, not that the rule holds (noted, no finding).
- Harvest: the delta duplicated nothing; the pre-existing material it should have reconciled with
  is the `200/` README's wording and (post hoc) GUARDS.md.

### Lens 4 — security and privacy (mandatory)

Discharged with grounds: the delta is 45 lines of doctrine prose in two Markdown files; it adds no
code, no data path, no credential, no personal data beyond the author identity the closed list
names (`Mike`, already used throughout the file), and no live surface. `/security-review` NOT RUN:
the worktree is dirty with the sibling's deletion so the scanner's pending diff is not the delta,
and `/security-review`'s exclusions bar Markdown, so a clean pass would weigh as nothing. The
floor's secretscan, leakscan, pdlistscan and attribscan ran clean over the tree on the CI plane
(exit 0). No security or privacy finding.

### Standing checklist V1–V7

- **V1 — No claim stronger than its evidence.** Two: the changelog's *"the framing obligation
  (`020/230`) [is] not done by this change"* against a passage that states its ask (LF2); and a
  2026-11-09 date for an act the commit timestamp bounds to 2026-11-08 UTC (LF5). The `115/170`
  quote is verbatim; the pick's status is labelled honestly.
- **V2 — Re-run every recorded claim.** Both re-run lines re-run; both reproduce clean at HEAD
  (ledger below). The brief's own claim that `/usr/bin/python3` cannot import the tests was not
  needed and not exercised.
- **V3 — A changed rule is swept to every mirror.** Swept with `coldsweep` (ten patterns). Mirrors
  found: `REVIEW.md` 612–615 (stamped pointer, correct); `docs/roadmap/200-…/README.md` 23 and 74
  (restates rung 2's exclusion; not swept — LF3). No skill, template, README index or test carries
  the ladder's text.
- **V4 — One fact, one home.** "When a check is owed" now has a value test here and a feasibility
  test in GUARDS.md, neither naming the other (LF4); "where a decision not to build is recorded"
  has no home for post-census rules (LF1).
- **V5 — No internal contradiction.** Rung 2's *"not severity"* against the floor's *"not the
  only one"* (LF3). Cross-references checked for the rule reached, not the file found:
  `REVIEW.md` → `PROPAGATION.md` § *When a rule keeps breaking* rung 1: reached, the rule is there.
  Passage → `020/220`: reached, the item states the per-rule output the passage attributes to it.
  Passage → `115/170`: reached, the words are there verbatim. Passage → `020/240`: barred until
  act 2. `RECORD.md` 488's 2026-08-04 ruling on *"recurrence, not severity"* is grounds for one
  rule's promotion, not a general ruling on what earns a check, so the floor does not contradict a
  ruling of his.
- **V6 — Security and privacy.** Lens 4, discharged with grounds.
- **V7 — Spawn provenance.** In the brief (§ Spawn provenance) and again above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `4458a157` | yes — `coldsweep --commit`, two `--path`s, body not printed | LF1, LF2, LF3, LF5, LF6; LF4 is a HEAD-state finding whose other half (`dd3d60d4`, 2026-11-10) post-dates this commit |

### Findings

Every finding is the principal's to decide (rule 3); nothing is applied. Counsel is labelled and
kept beneath each.

**LF1 — MODERATE — "a check not built is a decision with its reason recorded, not silence" names
no surface, moment or record shape for the decision, so for any rule written after the census the
obligation cannot be met or seen to be met.** Evidence: `PROPAGATION.md` 1061–1062 states the
obligation; 1069–1070 names the census (`020/220`) as *"where each rule stands"*; `020/220` is
open and describes one pass over the existing stock with a per-rule state as output. Nothing says
who records the decision for a new rule, where a future session reads it, or when it is owed.
GUARDS.md § *A rule with no home is not a rule* (648–668) supplies the test — *"name the surface a
future session reads it on"* — and the obligation fails it. This is the brief's named worst
failure in part: not an obligation no session can meet, but one whose meeting leaves no trace, so
the record cannot tell weighing from silence. Rule broken: V4 (one home) and GUARDS.md's own
test; the floor's second half is directive-only with no record to point to.
*Counsel:* either narrow the sentence to what is true (*the census records, per rule, whether a
check is built and why; a rule written after it carries the same line in its intent record*) or
name the surface and shape — the same move REVIEW.md made for *"review: not warranted — grounds"*,
which exists because *"omission is the bug … neither can disagree with a blank"*. Low cost: one
clause here and one line in the census item.

**LF2 — MODERATE — the record disagrees with itself about `020/230`: the passage states track
(b)'s whole ask as doctrine, the changelog says (b) is not done, and the item stays open with no
remainder written.** Evidence: `020/230`'s text (whole item, 11 lines) ends *"This makes it a
design obligation on every rule, up front"*; `PROPAGATION.md` 1049–1052 says *"Framing is owed by
every rule, up front … rung 1 made a design obligation, not a remedy held back until the third
breakage"*; `CHANGELOG.md` 1386–1387 says *"the framing obligation (`020/230`) [is] not done by
this change"*; `020/230` is `[ ]` with no text saying what remains. The brief's non-goal reads
(b) as *"the framing obligation's review-time check"*, words the item does not contain, so a
reader of the board sees an open item whose stated ask is already in doctrine, and a reader of
the changelog sees a denial that the passage did it. Rule broken: V1 (the changelog's claim is
weaker than the text), V5 (board and doctrine disagree), and the board's own grammar — an open
item states work that exists.
*Counsel:* decide which is true and make the other say so. If (b)'s doctrine half is done by this
passage, tick `020/230` citing it and open a narrower item for whatever check or review-time test
the author meant; if (b) is more than the sentence, write the remainder into the item so it is
not re-done.

**LF3 — minor — rung 2's flat exclusion *"Recurrence, not severity, is what earns a check"* was
left unqualified while the floor beneath it says recurrence is the usual earner, *"not the only
one"*; a board README mirrors the old exclusion.** Evidence: `PROPAGATION.md` 1027 against
1055–1057; `docs/roadmap/200-…/README.md` 23 (*"Recurrence — not severity — is the trigger"*).
Outcome is unchanged — rung 2 already calls a severe-but-once failure *"a judgement call"*, which
is what the floor's value test is — but the text now says both "not severity" and "not the only
one" within thirty lines, and the changelog's *"climbing rule is unchanged"* is true of climbing
only. Rule broken: V5, V3.
*Counsel:* one clause at rung 2 (*recurrence is the usual earner; the floor below names the
test*) and the same at the `200/` README, so the exclusion and the floor read as one rule.

**LF4 — minor — two "the check is not built" gates in two files, neither naming the other: the
floor's value test here (*"owed only where its value beats its cost"*) reads as the whole test,
while `GUARDS.md` § *Before building a check: the evidence window* holds the prior test (*can* it
be built; *"If neither is possible, the check is not built"*).** Evidence: `PROPAGATION.md`
1053–1057; `GUARDS.md` 151–175; `git log -S` dates the evidence window to `dd3d60d4`, 2026-11-10,
one day after this delta, so the author could not have cited it and the later commit did not
point back. The finding is on the surface at HEAD, which is what a reader meets. Rule broken: V4,
V5 (sibling docs it must reconcile with).
*Counsel:* a one-line pointer each way, ordered: the evidence window decides whether a check
*can* enforce a rule; the floor decides whether one *is worth* building; the census records the
outcome per rule.

**LF5 — minor — the pick is dated 2026-11-09 in an at-rest record whose landing commit is
2026-11-08T12:04Z.** Evidence: `PROPAGATION.md` 1044 (*"(2026-11-09)"*) and 1062 (*"Mike,
2026-11-09, `020/240`"*); `CHANGELOG.md` 1371 heading and 1382; `git log -1 --date=iso-strict
4458a157` → author `2026-11-09T01:04:49+13:00`, committer `2026-11-09T01:33:17+13:00`; the pick
preceded the commit, so its UTC date is 2026-11-08. The same paragraph dates the `115/170` words
2026-11-08, so two frames sit in one passage. `CONVENTIONS.md` 57: *"UTC at rest; local on
presentation, labelled where doubtable"*. Rule broken: CONVENTIONS time row; V1. Act 2 will check
the pointer and `020/240` for the pick's own stamp.
*Counsel:* re-date the three sites to 2026-11-08, or label the frame; a one-line fix in the
application commit.

**LF6 — note — the obligation on every rule is homed inside a section keyed to a rule that has
broken, with no index or writer-facing surface pointing at it.** Evidence: section title at 1002
and its opening (*"The ladder above is for a rule that has broken"*, 1044–1045); `docs/method/
README.md` 114 describes the file in one line and names neither ladder nor floor; grep for
writer-facing rule guidance across `docs/method/` and `docs/build/` finds no pointer. This is
rung 1's own test (*"was the rule findable from where the reader stood?"*) applied to the floor.
Low weight because the house has no single rule-writer surface yet; the census (`020/220`) is the
natural place to decide where one lives.
*Counsel:* when LF1 is decided, give the floor a one-line entry wherever a rule-writer is pointed
(the method README, or a *Writing a rule* note), rather than moving the passage.

### Re-run ledger

| Line | Where | Result |
|---|---|---|
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | worktree root, foreground, load 3.61 | exit 0; nothing staged so staged scanners "scanned nothing"; linkscan 1255 files / 1635 links clean; pdlistscan 1274 files clean; 2 pointerscan advisories on other items (`160/1420`, `160/994`) |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | worktree root, foreground, load 4.69 | exit 0; 28 secretscan entropy advisories and 3 leakscan report-only advisories, none in the delta; reviewscan "253 review brief(s) keep deferred material out of the brief"; attribscan clean; "declarations: 21 checks, 0 meet all five" |
| `/security-review` | — | NOT RUN (lens 4 grounds) |
| `git merge-base --is-ancestor 4458a157 HEAD` | worktree | exit 0 |
| `coldsweep --commit 4458a157 --path … --path …` | worktree | exit 0, body not printed |

### Follow-up checklist (for the principal's decision; nothing applied)

- [ ] LF1 — name the surface and shape of "a check not built is a decision recorded", or narrow
      the sentence to the census.
- [ ] LF2 — settle `020/230`: tick it against this passage, or write its remainder into the item;
      correct the changelog line either way.
- [ ] LF3 — qualify rung 2 in place and at `200/` README 23.
- [ ] LF4 — cross-point the floor and GUARDS.md's evidence window.
- [ ] LF5 — re-date the pick to 2026-11-08 UTC or label the frame (pending act-2 confirmation).
- [ ] LF6 — one index line for the floor where a rule-writer looks (after LF1).
- [ ] Act 2: verify the *"Written always, checker by value"* quote and the pick's date against the
      pointer and `020/240`; record the release message; reconcile against the sibling.

**Owed ask to the principal, as counsel:** none blocks this verdict. All six are his to rule on
under rule 3; LF1 and LF2 are the two worth a plain-language briefing before the application
commit, because each changes what a future session is told it owes. My recommendation is to take
LF1's narrowing (say what the census records and stop there) over building a new per-rule line,
until the census has run and shows whether such a line would be used.

### Reconcile — act 2, 2026-11-15 UTC

**Release, recorded by the receiver (rule 4):** after act 1 was committed (`cbe9e023`, local), the
orchestrator session `bb3a9a14` sent: *"Act 2 is released: you may now read this one held file,
the brief's deferred sibling"*, giving the held copy's path outside the worktree and its
pre-partition repo path `docs/reviews/2026-11-09-0126-ladder-floor-cold.deferred.md`, and opening
*"the brief's other rule-2-barred records and the delta's commit body"*. Direction was process
only: append `### Reconcile`, never revise act-1 text, record the release, update the log, re-run
the gates, do not commit. No question about the delta and no request about any finding.

**Opened at act 2:** the sibling (whole); the queue pointer `160/1110` (whole); the intent record
`020/240` (whole); the commit body of `4458a157` (`git log -1 --format=%B`); `034ecd70`'s stat and
dates. Not opened: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, other prior
verdicts — nothing in the sibling or the records sent me there, and none bears on the delta.

**The sibling, in sum:** the pointer's two author-written questions (does the passage contradict
any rung or the >2 promotion rule; is "value beats cost" followable) and five brief-writer
questions: where the not-built decision is recorded for existing rules; whether `115/170`'s words
carry the weight; where else the house states when a rule earns a check; the "usual way" wording
against a threshold stated elsewhere; and that the landing and pointer commits are separate. Plus
its floor run at `c132cc1c` (hook and ci exit 0; three pathscan warn-only findings).

**Per finding, against the sibling and the author's account:**

- **LF1 (MODERATE) — stands.** The sibling's question 1 is the same gap from the other side ("for
  the rules that already exist?"). The author's account answers that side: `020/240`'s close note
  says *"`020/220` can run now"* and the passage names the census as where each rule stands. The
  post-census side, the one act 1 found, is answered nowhere in the sibling, the pointer, the
  intent record or the commit body. The pointer's "is 'value beats cost' followable" is answered
  the same way: followable as a ranking act on the board, not auditable, because the decision it
  produces has no named record. Severity unchanged.
- **LF2 (MODERATE) — stands, with the author's account added.** `020/240`'s close note reads
  *"`020/230` needs only a home for its review-time check"*. So the author did hold a remainder
  for (b), and the brief's gloss came from here. But that sentence lives in `020/240`'s close
  note, not in `020/230`, whose text still asks only for the design obligation the passage states.
  A reader of the open item does not see the remainder; a reader of the changelog and commit body
  (*"the framing obligation (`020/230`) [is] not done by this change"*) is told the obligation is
  not done when its wording is. The counsel narrows: write the remainder into `020/230` itself
  (*"the obligation is stated in `PROPAGATION.md` § …; what remains is a home for its review-time
  check"*), and let the changelog line say that. Severity unchanged: the board still disagrees
  with the doctrine on its face.
- **LF3 (minor) — stands; the sibling's question 4 is the same comparison.** The commit body says
  *"The climbing rule and the >2 promotion rule are untouched"*, which is true: the >2 promotion
  rule (`PROPAGATION.md` 1079–1083) governs promoting a pattern into doctrine, not when a check is
  owed, and the passage does not touch it. Act 1 answered the pointer's contradiction question in
  the same place: no rung is contradicted in outcome; rung 2's earning sentence is left as a flat
  exclusion the floor qualifies. The author's intent and the wording differ, which is the
  sibling's own instruction ("compare wording, not intent").
- **LF4 (minor) — stands.** The sibling's question 3 asked for the sweep act 1 ran; `GUARDS.md`'s
  evidence window is the one sibling statement found, and it post-dates the delta, which the
  author's account could not have known. `ECONOMICS.md`, `PRINCIPLES.md` and the skills state no
  rule on when a check is earned.
- **LF5 (minor) — confirmed against the records.** `020/240` dates the answer *"2026-11-09"* and
  the pointer says *"2026-11-09"* too; the landing commit is `2026-11-09T01:04:49+13:00`, that is
  `2026-11-08T12:04:49Z`, and the pointer commit `2026-11-09T01:32:39+13:00`. Every record carries
  the local date, consistently with each other and against `CONVENTIONS.md`'s at-rest rule. The
  fix, if taken, sweeps `020/240` and `160/1110` as well as the three sites act 1 named, or
  labels the frame once. Severity unchanged.
- **LF6 (note) — stands; nothing in the sibling or records speaks to it.**
- **A2 (no finding) — the sibling's question 2 is the assumption act 1 confirmed.** `020/240`
  records the offered option's text: *"an automatic check is added only where it is worth its
  cost, ranked like any other work, in line with his own words of 2026-11-08 on `115/170`"*. So
  the step from "ranked by value" to "a check only where worth it" was in the option he was
  offered, not only the author's inference afterwards; the passage's labelling (an answer, not a
  ruling) is confirmed. The quote *"Written always, checker by value"* is verbatim in `020/240`.

**Formed at reconcile, prompted by the sibling's question 5:**

**LF7 — note (formed at act 2) — the review pointer landed in a second commit, not the landing
commit.** Evidence: `4458a157` touched only the two delta files (`git show --stat`, 0 board files);
`034ecd70`, *"board: land 020/240's ladder floor; close it; queue 160/1110"*, 28 minutes later,
carries the pointer and the intent record's close. Rule 4 says the pointer goes *"in the same
commit that lands the work"* (AWA2); the TA9 allowance is for a series whose last commit completes
the work. Here the two commits are adjacent in history with one committer timestamp
(`2026-11-09T01:33:17+13:00` on both), so they were pushed as one series and the window the rule
closes, landed doctrine sitting unpointed into the next session, did not open. The brief and the
pointer both pin the delta to `4458a157`, and the delta list a reviewer runs on the two paths
misses nothing, because the pointer commit touched only board files. A note because the rule's
intent held; the letter did not. *Counsel:* none beyond what the house already says; the record
shows the pattern was safe this once, not that it is safe.

**The brief-writer's floor run:** at `c132cc1c` it saw three pathscan warn-only findings; at HEAD
`6cf077af` pathscan is clean with ten allow-marker suppressions. Later commits resolved them;
nothing for this pass.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 3 minor · 2 notes** (LF1–LF6 from
act 1 unchanged in severity; LF7 added at reconcile as a note). The cycle closes on this pass
(no MAJOR): decided findings go to the backlog and their application earns no further ceremony
beyond the application commit's own pointer, per `REVIEW.md` § *Applying decisions to doctrine*.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`cbe9e023`, local; it
landed on `main` as `fa7a0306` after the rebase onto newer commits, and the reconcile and log
below cite the pre-rebase hash verbatim); folded here verbatim (headings demoted two levels) and
the sibling file removed, per the brief. The orchestrator (headless Opus 5.5 session `bb3a9a14`,
started by drain session `21a271a5`, itself Opus 5.5) held the partition, formed no finding and
wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ladder-floor-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

#### The queue pointer's questions (author-written, verbatim)

> whether the passage contradicts any rung of the ladder or the >2 promotion rule; whether 'value
beats cost' is followable.

#### The brief-writer's own questions

1. "A check not built is a decision with its reason recorded": recorded where, by whom, for the
rules that already exist?
2. `115/170`'s words answered a different question (capping guard work). Do they carry the weight
the passage rests on them?
3. Where else does the house state when a rule earns a check (`GUARDS.md`, `ECONOMICS.md`,
`PRINCIPLES.md`, a skill)? Sweep for mirrors (V3).
4. The passage says recurrence is "the usual way", while a sentence elsewhere states a threshold.
Compare wording, not intent.
5. The landing commit and the pointer commit are separate (`4458a157`, then `034ecd70`).

#### What the brief-writer ran, and what it got

- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*The reviewer's work log, kept outside the worktree while the pass ran and read by no other session
until act 2 was saved; appended here verbatim at the fold (headings demoted two levels, form only)
and the working file deleted.*

### Review log — atelier 160/1110, ladder-floor cold pass (`020/240`)

Reviewer: Fable 5.1 subagent, spawned by orchestrator session bb3a9a14 (started by drain session
21a271a5). Worktree: /Users/mike/worktrees/fable/atelier-160-1110-2152/atelier. Brief:
docs/reviews/2026-11-09-0126-ladder-floor-cold.md. Commands, files and evidence only.

#### Act 1

- 2026-11-15T21:54Z `date -u` → Sun Nov 15 21:54:06 UTC 2026. `uptime` load 5.57/5.33/6.14.
- Read the brief whole (lines 1–193). Barred until act 2: ROADMAP-DONE.md, SESSIONS.md,
  docs/sessions/, prior verdicts in docs/reviews/, the queue pointer 160/1110, the sibling
  .deferred.md, delta commit message bodies, intent record 020/240 beyond its title.
- `git status --short` → only ` D docs/reviews/2026-11-09-0126-ladder-floor-cold.deferred.md`
  (the partition; expected). HEAD = 6cf077af.
- `git merge-base --is-ancestor 4458a157 HEAD` → exit 0: the delta is in the tree.
- `git log --oneline 4458a157..HEAD -- docs/method/PROPAGATION.md CHANGELOG.md` → 67 commits,
  nearly all changelog-only; PROPAGATION.md-specific ones separated below.
- `which python3` → /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 (3.14.6), as
  the brief requires for tools/.
- Read docs/method/REVIEW.md whole (lines 1–699) for the verdict shape, rules 1–4, lenses, V1–V7,
  and the 2026-11-15 method-record requirement (lines 503–516).
- `python3 tools/coldsweep.py --root <wt> --commit 4458a157 --path docs/method/PROPAGATION.md
  --path CHANGELOG.md` → exit 0; subject, stat (2 files, +45) and diff printed; body not printed;
  "0 board-store file(s)… none touched; 0 file(s) left out as rule-2 barred: none touched".
  Delta = CHANGELOG.md +18 (entry "Changed (2026-11-09 — … ladder gains a floor, 020/240)") and
  PROPAGATION.md +27 (subsection "What is owed, and what is earned (2026-11-09)").
- `git log --oneline 4458a157..HEAD -- docs/method/PROPAGATION.md` → 20 later commits touch the
  file. `git diff 4458a157 HEAD -- docs/method/PROPAGATION.md | grep -c "What is owed\|Written
  always\|beats its cost\|is never skipped"` → 0: no later hunk touches the passage. Passage at
  HEAD = lines 1044–1070; read the whole section 987–1100 (enforcement clause, ladder rungs 1–3,
  the passage, the countable-trigger and mining paragraphs).
- `git show --stat --format='%h %s' 4458a157` → only the two files above.
- `grep -n` headings in PROPAGATION.md → section "When a rule keeps breaking — climb, never
  restate" starts line 1002; subsection at 1044; next paragraph 1071; next section 1100.
- Read board items (not barred; disclosed): docs/roadmap/115-…/170-the-guard-layer-is-consuming
  -the-programme.md whole (its ANSWERED 2026-11-08 paragraph carries the quoted words verbatim:
  "This sounds like yet another artifical limit that is not helpful. It is about balancing
  importance and priority to do the work that is most valuable" — matches PROPAGATION.md 1066–1068
  character for character); docs/roadmap/020-…/220-a-the-census-nobody-has-run….md whole (open
  `[ ]`; output "per-rule state: enforced · directive-only · unenforceable, accepted — the last
  reasoned and dated to the GUARDS.md bar"); docs/roadmap/020-…/230-b-the-half-with-no-owner….md
  whole (open `[ ]`; its text: rung 1 "only as remediation, after recorded breakage. This makes
  it a design obligation on every rule, up front" — no mention of a review-time check).
- `head -1 docs/roadmap/020-…/240-…md` → title only: "The posture change this implies — stated so
  it is ruled, not …" (rest of the item barred until act 2).
- Sweep script (scratchpad sweep.sh) running coldsweep with the brief's two --also-exclude paths,
  patterns "Written always", "checker by value", "earns a check", "climb, never restate", "beats
  its cost", "design obligation", "not silence", "first rung", "not severity", "What is owed".
  Each: exit 0, 841 files scanned, 569 excluded as rule-2 barred. Hits of note:
  PROPAGATION.md:1027 "Recurrence, not severity, is what earns a check"; RECORD.md:488 "(Ruled by
  the principal 2026-08-04 on **recurrence, not severity**" (grounds for one describe-not-quote
  rule, read 478–496: not a general ruling on what earns a check); docs/roadmap/200-…/README.md:23
  "Recurrence — not severity — is the trigger for promotion to an always-on check" and :74 the
  three rungs restated (read 18–30, 70–80); 110/010:7, 110/090:40, 200/030:3 cite rung 2;
  EVIDENCE.md:169 "don't stop at the first rung" is a different ladder (acquisition).
  "Written always" / "checker by value" occur only in the delta's two files.
- `grep -rn "keeps breaking\|What is owed\|rung 1\|never restate" tools instruments skills
  docs/build README.md docs/method/README.md` → no hits: no test, skill or template pins the text.
- `grep -n "PROPAGATION" docs/method/README.md` → line 114 only, a one-line file description; no
  index entry names the ladder or the floor. `grep -rn -i "writing a rule|write a rule|new rule|
  rule is written|when you add a rule" docs/method docs/build` → no writer-facing surface points
  at the floor (hits are unrelated uses of the words).
- Read docs/method/GUARDS.md 151–213 (§ Before building a check: the evidence window — "If
  neither is possible, the check is not built"; "Adopted on Mike's 2026-11-09 answer"), 350–382
  (§ Acceptance and deferment), 648–691 (§ A rule with no home is not a rule — "name the surface
  a future session reads it on"). `git log -S'Before building a check: the evidence window' --
  docs/method/GUARDS.md` → dd3d60d4 2026-11-10: the evidence window landed AFTER the delta.
- `grep -n` ECONOMICS.md value/cost/cheapest lines (10–299) and 00-APEX.md answer/ruling lines
  (68–218): the "cheapest model that does the job" rule and the informed-ruling section; nothing
  there states when a check is owed; no contradiction with the floor found.
- `git log -1 --format='%h %ad %s' --date=iso-strict 4458a157` → author 2026-11-09T01:04:49+13:00
  (= 2026-11-08T12:04:49Z); `%cd` → 2026-11-09T01:33:17+13:00 (= 2026-11-08T12:33:17Z).
  Neighbour 3312cdbd (changelog entry dated 2026-11-08) → 2026-11-09T13:42:25+13:00
  (= 2026-11-09T00:42:25Z). CONVENTIONS.md line 57 "UTC at rest; local on presentation", line 59
  "prose stamps are YYYY-MM-DD + HHMM UTC".
- Re-run line 1: `uptime` (load 3.61) then `nice -n 10 python3 tools/floor.py --plane hook --root
  <wt>` → exit 0; nothing staged so the staged scanners report "scanned nothing"; linkscan 1255
  files / 1635 links clean; pointerscan 2 advisories on OTHER items (160/1420, 160/994: queue-state
  glyph), not this delta; pdlistscan 1274 files clean.
- Re-run line 2: `uptime` (load 4.69) then `nice -n 10 python3 tools/floor.py --plane ci --root
  <wt>` → exit 0. secretscan 28 entropy advisories (workflows, tests, tools; none in the delta);
  leakscan 3 report-only diagnosis-key advisories; the same 2 pointerscan advisories; reviewscan
  "253 review brief(s) keep deferred material out of the brief"; attribscan clean (1 file read);
  "declarations: 21 checks, 0 meet all five". EXPOSURE: leakscan's advisory lines printed
  `docs/SESSIONS.md:87` and `docs/reviews/2026-08-02-2348-deferral-delta-cold.md:29`, each with a
  14-character redacted snippet ("Dia…ne", "dia…he"); barred paths, no delta account read.
- Brief line widths: `awk` max=130, 90 lines over 85; `.wrapscanignore` exempts docs/reviews/ as a
  safety net and the CI gate never walks it; `wrapscan --help` default limit 85. Verdict prose is
  held at ≤ 100 columns per the brief.
- /security-review: NOT RUN. Grounds: the worktree is dirty (the sibling's deletion) so the
  scanner's pending diff is not the delta, and the delta is Markdown, which the scanner's
  exclusions bar, so a clean pass would weigh as nothing (REVIEW.md lens 4; brief § House rules).
- Act 1 verdict written to the brief below its `---` divider; Status line updated.
- Verdict appended to the brief (lines 194–504 at this point); Status line changed to "ACT 1
  WRITTEN 2026-11-15 UTC — PASS-WITH-FINDINGS (0 MAJOR · 2 MODERATE · 3 minor · 1 note)".
- Line widths checked in characters (/usr/bin/python3): every prose line ≤ 100; only three table
  rows (391, 481, 482) exceed it, as the brief's own tables do.
- Gates after writing, `uptime` first (load 3.49): `floor.py --plane hook` → exit 0 (staged set
  empty, so it saw none of the edit; same 2 pointerscan advisories on other items); `floor.py
  --plane ci` → exit 0 (reviewscan 253 briefs, attribscan 1 file read). Scanners aimed at the brief
  by path: leakscan, datescan, attribscan, reviewscan ("1 review brief(s) keep deferred material
  out of the brief"), secretscan — each 1 file / 504 lines, exit 0. pdlistscan takes no path; it ran
  tree-wide on the ci plane, exit 0. spellscan by file path opened 0 files (docs/reviews/ is in its
  ignore list, checked below); the tree-wide ci run was clean.
- Findings recorded in the brief: LF1 MODERATE (no record surface for "a check not built is a
  decision recorded" after the census), LF2 MODERATE (020/230 open while the passage states its
  ask; changelog says not done), LF3 minor (rung 2 "not severity" left flat vs the floor's "not
  the only one"; 200/README mirror), LF4 minor (floor's value test and GUARDS.md evidence window
  do not name each other; the latter landed 2026-11-10), LF5 minor (pick dated 2026-11-09 against
  a 2026-11-08T12:04Z landing commit; CONVENTIONS "UTC at rest"), LF6 note (floor homed in a
  section keyed to broken rules; no index or writer-facing pointer).
- Sound and checked: the 115/170 quote is verbatim; the pick is labelled an answer, not a ruling;
  the census is named as output, not claimed done; no later commit edited the passage; no test or
  template pins the text; REVIEW.md 612–615's pointer reaches rung 1; RECORD.md 488's 2026-08-04
  ruling is grounds for one rule, not a general bar on severity earning a check; both re-run
  lines reproduce at HEAD with exit 0.
- Scratch: only `sweep.sh` (a zsh loop over coldsweep patterns) in the session scratchpad; no
  captures. ACT 1 complete; waiting for the orchestrator's commit and release message.

#### Act 2

- 2026-11-15T22:09Z release received from orchestrator bb3a9a14 (act 1 committed cbe9e023):
  the held sibling's path, the pre-partition repo path to use, the other barred records and the
  commit body opened; process direction only (append Reconcile, no act-1 revision, log, gates,
  no commit).
- Read: the sibling whole (pointer's two questions; five brief-writer questions; its floor run at
  c132cc1c); docs/roadmap/160-doctrine-review-owed/1110-…md whole; docs/roadmap/020-…/240-…md
  whole ("Written always, checker by value" verbatim; close note: "020/220 can run now; 020/230
  needs only a home for its review-time check"); `git log -1 --format=%B 4458a157` (body repeats
  the changelog's "020/230 not done"; "climbing rule and the >2 promotion rule are untouched").
- `git log -1 --date=iso-strict 034ecd70` → author 2026-11-09T01:32:39+13:00, committer
  2026-11-09T01:33:17+13:00 (same committer stamp as 4458a157); `show --stat` → ROADMAP.md,
  020/240, 160/1110 only; `git log --oneline 4458a157..034ecd70` → one commit (adjacent).
  `show --stat 4458a157 | grep -c 1110` → 0: the landing commit carried no pointer.
- Reconcile appended: LF1–LF6 stand at their severities (LF2 counsel narrowed by 020/240's close
  note; LF5 confirmed against 020/240 and the pointer, both dated 2026-11-09 local); A2 confirmed
  by 020/240's option text; LF7 note formed at reconcile (pointer in a second commit, same push).
  Overall restated: 0 MAJOR · 2 MODERATE · 3 minor · 2 notes.
- Status line → "ACT 2 WRITTEN 2026-11-15 UTC …". Reconcile prose lines ≤ 100 characters.
- Scratch sweep.sh deleted from the session scratchpad.
- Gates after act 2, `uptime` first (load 6.75): `floor.py --plane hook` exit 0; `floor.py --plane
  ci` exit 0 (only the same 2 pointerscan advisories on 160/1420 and 160/994); aimed at the brief:
  leakscan, datescan, attribscan, reviewscan ("1 review brief(s) keep deferred material out of
  the brief"), secretscan — each 1 file / 594 lines, exit 0. Tree: ` M` the brief, ` D` the
  sibling (partition); no other change. ACT 2 complete; the orchestrator folds and commits.
