# Cold pass — the ladder gains a floor: framing always, a mechanism by value (`020/240`)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-15 UTC — PASS-WITH-FINDINGS (0 MAJOR · 2 MODERATE · 3 minor ·
1 note). Act 2 (reconcile against the sibling) follows once act 1 is committed.
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
