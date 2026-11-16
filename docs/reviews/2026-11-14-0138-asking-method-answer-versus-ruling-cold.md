# Cold pass — the principal's method for asking, and an answer is not a ruling

**Board:** `docs/roadmap/160-doctrine-review-owed/1250-rule-4-cold-pass-queued-asking-method-and-answer-versus-ruling.md`
**Status:** VERDICT COMPLETE 2026-11-16 UTC, PASS-WITH-FINDINGS (0 MAJOR, 3 MODERATE, 3 minor,
6 notes, two of them formed at reconcile); act 1 committed `44743bd1`, act 2 reconciled; the
sibling is folded below. Findings await the principal (rule 3). Brief written 2026-11-14 UTC by a headless Opus 5.5
brief-writer (`cclive` lists it as session `43c70bbb`). Run under the principal's drain order of
2026-11-16.

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (the section that says how
every session asks the principal, and how every record marks what he said, is doctrine by text and
by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Size of this pass:** small to medium: one commit, about 115 added lines, all markdown, in three
files (`docs/method/COMMUNICATION.md`, `docs/method/RECORD.md`, `CHANGELOG.md`); no code.
**Why it earns a review:** This section is what every session in every child repo follows when it
puts a question to the principal, and the rule every record follows when it writes down what he
said. Two failures are worst. First, a record convention that lets a session's own framing be
written up as the principal's authority, the self-affirming loop the work exists to close, or one
that strips real authority from his own words. Second, practice text that claims more than its
grounding: a single incident written as his standing method, or a diagnosis the evidence does not
support carried into doctrine every child inlines by pointer. Doctrine text is public and binds the
fleet once trusted.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `d0ca5d24`,
  2026-11-09 UTC, and the worker it dispatched (per the queue pointer). The author queued this pass
  and does not take it.
- **Who wrote this brief:** a headless brief-writer (`claude-opus-5-5`; `cclive` lists it as session
  `43c70bbb`), started 2026-11-14 UTC by an estate health sweep, orchestrator session `58027096`
  (Opus), on the principal's instruction that a brief is written for every review known to be
  owed (Mike, 2026-11-14, verbatim: *"include all briefs are written where we know a fable
  review is required"*). Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model.
- **Barred from running this pass:** session `43c70bbb` and session `58027096` (whoever writes a
  brief does not run it), and session `d0ca5d24` with everything it started. Session `d0ca5d24`
  also authored the later commit `2a6d7a41` on the same section, so it is barred twice over.
- **Contact, disclosed (rule 4):** the brief-writer's only instruction came from `58027096`: the
  item number, the pointer's opening sentence, and the rules of the sweep. It carried no framing of
  the work. The brief-writer had no contact with the author session or its worker.
- **Who reviews:** a fresh Fable 5.1 session started for this pass alone, by a session that passes
  rule 4's criterion. An orchestrator may hold the context partition and commit the records
  off-tier, only if it forms no finding, writes no severity, and is disclosed in the claim, the
  pointer and the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):
  its launch prompt; `skills/review-brief/SKILL.md`; the queue pointer whole; **the three intent
  records whole**, including the author's landing notes under each (`320/820`, `420/020`,
  `020/270`); the queue pointers `160/1440` and `160/1240` whole; the head of the unrun brief for
  `160/1210` and most of the unrun brief for `160/1240` with its sibling's opening (read for house
  form); the delta and `2a6d7a41`'s `COMMUNICATION.md` hunk through `git show --format=` and
  `tools/coldsweep.py --commit`, both body-free; commit subjects through `git log`; parts of
  `00-APEX.md`, `COMMUNICATION.md` at HEAD, `docs/build/templates/CLAUDE.md` and the `020`
  section's README. It opened **no prior verdict file and no commit's message body**. Its harness
  also loaded user-level and repo instruction files and a memory index, which hold private context
  this brief does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words, printed by these lines, from the worktree root. The first two are his own
words; the third is the label of an option he picked, an answer, and the option text around it is
a session's.

```
grep -c 'ask one question at a time' \
  docs/roadmap/320-child-filed-findings-via-pointing-up/820-hand-up-the-principals-asking-method-is-not-in-doctrine.md
sed -n '1,32p' docs/roadmap/420-when-to-ask-mike-commissioned/020-an-answer-is-not-a-ruling.md
grep -o '"Answer unless I say ruling (Recommended)"' \
  docs/roadmap/420-when-to-ask-mike-commissioned/020-an-answer-is-not-a-ruling.md
```

His 2026-11-05 method, his 2026-11-05 and 11-06 follow-ups, and his reactions to failed asks are
quoted in the hand-up as filed, which you may read whole up to its landing note:

```
sed -n '1,97p' docs/roadmap/320-child-filed-findings-via-pointing-up/820-hand-up-the-principals-asking-method-is-not-in-doctrine.md
```

Those 97 lines are a private child's report, stated class-only, written before the author's work:
they are the evidence base, not the author's account. Lines 98 onward and the other two records'
landing notes are the author's account and are barred until phase 2. The `020/270` record's first
three lines name the commission; its evidence is the `020` section's README, § on P5 (search it for
`90.6%`), which is not barred.

## What the work is

One commit on `main`, landed 2026-11-09 UTC (stamped 2026-11-10 NZDT):

- **`e7370f78`** — `board: queue the cold pass on the asking doctrine (160/1250)`. Despite its
  subject, it carries the whole doctrine change as well as the queue pointer.

Read it body-free: `python3 tools/coldsweep.py --root . --commit e7370f78` (subject, stat and diff,
never the body; board files left out). Plain `git show` prints the body before the diff, and
reading is atomic (`REVIEW.md` rule 1), so it is barred. Check first that your tree has the delta:
`git merge-base --is-ancestor e7370f78 HEAD` exits 0.

Delta paths, read at the commit and at HEAD:

- `docs/method/COMMUNICATION.md`: the unmet-term check in § *The axes a calibration covers*, the
  *Accessibility of the language* bullet (`020/270`); in § *Asking for a ruling*, the reworded
  four-question sentence, *His method, as he wrote it* with its seven practice bullets (`320/820`),
  *What comes back is an answer or a ruling* and *The record marks* (`420/020` parts a and b).
- `docs/method/RECORD.md`: one sentence added to the question-box picks entry.
- `CHANGELOG.md`: the 2026-11-09 entry for `320/820`, `420/020`, `020/270`.

**The section has moved since.** `2a6d7a41` (2026-11-12 UTC, same author session) rewrote two
places this delta touched: the two-step sentence after the four-question one (the account and the
device now go in the same turn), and the typed-replies sentence at the end of *The record marks*
(now settled as an answer unless he says ruling). Read it body-free too:
`python3 tools/coldsweep.py --root . --commit 2a6d7a41 --path docs/method/COMMUNICATION.md`. Those
two rewrites are pass `160/1440`'s subject. Here, judge this delta's text as it stands at HEAD,
including whether the rest of it still reads true beside them.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- The section "carries his written method in his words": the four-line list and the follow-up are
  quoted verbatim.
- "The four-line list is his written method. The last three bullets are his reactions to asks that
  failed, and the examples under the others are single cases." The provenance paragraph says what
  each bullet rests on.
- "An account the session has only read, from a file or tool output, has reached nobody", with the
  one-session evidence; and "That says nothing either way about what focus mode hides, so the
  two-step rule above rests on its own grounds."
- "The ceiling above is the tool's and never a target", and the four-question sentence now "states
  the tool's limit and points at the practice".
- An answer: "Work proceeds on it, because it is his decision on what was asked. It does not carry a
  ruling's weight unless he says it is one." A pick recorded as "Mike ruled X" makes a session's
  framing binding doctrine.
- The record marks: ⚖️ with his quoted words and context; 💬 with the pick quoted, who offered the
  options, and "an answer, not a ruling"; "A pick is never written as 'ruled'"; older ⚖️ lines
  prove nothing by themselves.
- The unmet-term check: "No scanner holds this. One was built on 2026-08-09 and deleted the same
  day: it fired on 90.6% of 6,764 replies".
- `CHANGELOG.md`: "Doctrine wording only; no scanner or tool changes", and its summary of each part.
- `RECORD.md`: "A pick is an answer and not a ruling; that section holds the difference and the
  marks."

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs and real-world behaviour.
There is no code. The lenses organise it; they do not bound it. Anything not named a non-goal is in
scope, and a non-goal that fences off the risk is a finding.

**Non-goals:** the two `2a6d7a41` rewrites named above (pass `160/1440`), except where they leave
this delta's surrounding text untrue; the two-step rule itself as `0ba1ba03` wrote it (pass
`160/1210`); § *When to ask* and the decision-exists test (`1db64e22`, `96b8be7b`, other passes);
`420/020` parts c and d (the sweep of old records and any guard), which the delta says stay open;
whether the principal's words and picks were the right ones, as distinct from whether the delta
records and applies them faithfully. Re-measuring the hand-up's transcript evidence is a non-goal
too: the transcripts are another repository's session records and are not to be read (see *House
rules*). Judge whether the doctrine claims more than the hand-up evidences.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved in the right home and shape? Is a public doctrine section the
   right place for one principal's practice preferences, and does it say whose they are? Does the
   answer/ruling split hold at the edges (typed replies, an answer later cited as authority, a
   ruling given inside a reply to a question)?
2. **Correctness & quality.** Re-drive each claim above against its grounding: every quote against
   its source, character for character; every count and date against the record it cites; every
   section or item pointer resolves to what it says. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states how to ask or how to record what he said
   (V3): `00-APEX.md` (*rulings conditioned*), `RECORD.md`, `REVIEW.md` rule 3,
   `docs/build/templates/CLAUDE.md` (the asking bullet every child carries),
   `skills/session-onramp/SKILL.md`, `GLOSSARY.md`, and the many "an answer, not a ruling" lines
   across `docs/method/` (find them with `coldsweep`). One home (V4); no contradiction (V5),
   including between the section's own title and the distinction it draws.
4. **Security & privacy**, mandatory: at design altitude, what publishing the principal's verbatim
   words and reactions exposes, whether the hand-up's class-only framing holds (does any line let a
   reader infer which child, session or estate it came from?), and whether anything in the delta
   falls outside `docs/PERSONAL-DATA.md`'s closed list. Code altitude: there is no code; discharge
   `/security-review` in one line with grounds (it excludes markdown, so a clean pass is empty).

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-14 UTC, from the worktree root,
and its results are held in the sibling. Read exit codes explicitly. Check `uptime` first and run
the floor line under `nice -n 10`, alone. Use the `python3` first on the machine's `PATH` (3.14.6
when written); CI pins 3.12.

```
git merge-base --is-ancestor e7370f78 HEAD; echo $?
python3 tools/coldsweep.py --selftest; echo $?
python3 tools/coldsweep.py --root . --commit e7370f78 > /dev/null; echo $?
nice -n 10 python3 tools/floor.py --plane ci --root .; echo $?
```

The delta's recorded figures are recorded proofs (V2): the 90.6% of 6,764 and the 2026-08-09 date
(against the `020` README and `git log -- tools/`), the "three times on 2026-11-05" and "asked four
times" (against the hand-up as filed; their transcripts are not re-run, by *House rules*), and the
`CHANGELOG.md` line "no scanner or tool changes" (against the commit's stat). Re-check each by the
cheapest read-only route and say which you could not re-run and why.

## House rules for this run

- **Live systems:** none is needed. No live writes, no push, no write to GitHub, no network service
  changed. A check that would need one is marked NOT RUN, with why.
- **Never read a session transcript's content** to re-measure the hand-up's evidence: they are
  another repository's records and hold private context. Never print personal data.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` from your worktree.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path, and name no child repo.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling (a held-back file, folded below the verdict at
the pass's close under *Deferred sibling, folded below the verdict*; by count: 14 questions,
7 facts), every item under `docs/roadmap/160-doctrine-review-owed/`
beyond its title, every commit's message body, and these records beyond the `sed` ranges in *The
acceptance test*:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/820-hand-up-the-principals-asking-method-is-not-in-doctrine.md`
  (lines 98 onward)
- `docs/roadmap/420-when-to-ask-mike-commissioned/020-an-answer-is-not-a-ruling.md` (lines 33
  onward), and the rest of `docs/roadmap/420-when-to-ask-mike-commissioned/`, which records the
  later answers
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/270-carry-p5-s-finding-into-part-b.md`
  (line 4 onward)

The delta's own `CHANGELOG.md` entry and doctrine text carry the author's account of why; they are
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/420-when-to-ask-mike-commissioned \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/820-hand-up-the-principals-asking-method-is-not-in-doctrine.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/270-carry-p5-s-finding-into-part-b.md \
  'not a ruling|one question at a time|reached him|⚖️|💬'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-claim ledger, findings with stable IDs (prefix `AQ`: `AQ1`, `AQ2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger and a follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the
sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit body;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (2026-11-16 UTC)

### Provenance (V7)

Reviewer: Fable 5.1 (`claude-fable-5-1`), tier checked at selection, in review worktree
`/Users/mike/worktrees/fable/atelier-160-1250-0545/atelier` at HEAD `73f1cc9a` (the claim commit;
`e7370f78` is an ancestor, exit 0). Spawned by headless orchestrator session `d9ce3020` (Opus 5.5),
itself started by drain session `1e053526` (Opus 5.5). Both are off-tier orchestrators under
REVIEW.md rule 4's reviewer-plus-orchestrator shape: they hold the context partition, formed no
finding and wrote no severity. Neither wrote the brief or any of the delta, and this session was
not started or instructed by the brief's barred sessions (`43c70bbb`, `58027096`, `d0ca5d24`).
The run is the principal's API-credit drain of 2026-11-16, not his weekly plan budget.

**The spawn prompt, as process direction only** (rule 4: what the orchestrator told the reviewer
is in the record): the item number, the worktree and brief paths, the barred set (the brief's list
plus the sibling, removed from the worktree on purpose), the deliverable's shape (act 1 below a
`---` divider in this file; a running work log at
`/Users/mike/.claude/fable-drain/notes/atelier-160-1250-0545.md`, the one other file I may write),
load and live-system rules, and the release timing (act 2 after act 1 is committed). It carried no
question about the delta, no pointer to where the risk lives, and no request to revise a finding.
No contact from any author or brief-writer session.

**What I read.** The brief whole; `REVIEW.md` rules 1–4, scope, re-run and V1–V7; the delta
through `coldsweep --commit e7370f78` and `2a6d7a41` (`--path docs/method/COMMUNICATION.md`),
both body-free; the acceptance-test ranges exactly (`320/820` lines 1–97, `420/020` lines 1–32,
`020/270` lines 1–3); the `020` README § P5; `COMMUNICATION.md`, `RECORD.md`, `00-APEX.md`,
`GLOSSARY.md`, `CONCURRENCY.md` § *The channel*, `PROPAGATION.md` § *Pointing up*,
`docs/build/templates/CLAUDE.md`, `skills/session-onramp/SKILL.md`, `docs/PERSONAL-DATA.md`, the
ADR `docs/decisions/2026-11-09-board-states-design.md` (lines 86–92, 232–240), the fleet-sweep
prompts; board items `115/270` (lines 38–50), `310/060`, `310/160`, `320/060`, `320/100` (five
lines each around their ⚖️ marks); commit subjects only via `git log`; one `--stat`. The
session-log step was skipped. No prior verdict, no session log, no commit body, no `160/` item
beyond its title, and nothing of `420/` beyond the stated range.

**Exposure, disclosed.** (1) My second `coldsweep` sweep (pattern `ruling round|four per box|up
to four`) carried the brief's excludes but not the hand-up file, so it printed one barred line:
`320/820` line 100, the author's landing note, one sentence saying the 2026-11-09 round asked up
to four questions per box. It is the author's account of the claim AQ5 tests. AQ5 was formed on
lines 1–97 and the doctrine text, which hold no evidence for the sentence; the exposure changed
nothing and is recorded here. (2) `coldsweep --commit 2a6d7a41 --path …` and the brief's sweep
printed the file names (titles) of board items left out, including `420/030`, `420/040` and
`160/1440`; titles only. (3) The harness loaded user-level and repo instruction files and a memory
index at start, which hold private context this verdict does not carry; nothing there is an
account of this delta.

### Load-bearing assumptions, named first (lens 1)

- **A1 — A public doctrine section is the right home for one principal's asking preferences, by
  name.** Confirmed. `COMMUNICATION.md` § *Two things, kept separate* makes the practice shareable
  and the instance personal, and the section already carries his dated words (2026-08-19,
  2026-08-23). The four-line list is the worked example under that framing; the practice it
  states (one at a time, long form in text, a short box that stands alone) travels to any
  principal, and `PD4` grants the first name. Probe: lines 14–33 and `docs/PERSONAL-DATA.md`.
- **A2 — The hand-up's evidence supports the practice bullets as written.** Confirmed with one
  exception. Every quote in the delta matches the hand-up or `420/020` character for character
  after whitespace normalisation (a script compared the four-line list and the 2026-10-03 quote;
  the shorter reaction quotes were compared by eye). The provenance paragraph labels the last
  three bullets as reactions and the others' examples as single cases, which is the honest
  altitude. The exception is the 2026-11-09 four-per-box example, which the hand-up does not hold
  (AQ5).
- **A3 — A record-writer can apply the answer/ruling split from the text alone.** Partly damaged.
  The provenance test is clear (his words, or his pick from a session's options). What the split
  changes for the session holding the record is not stated (AQ2), and which surfaces the marks
  bind is not stated (AQ6).
- **A4 — The delta still reads true beside `2a6d7a41`.** Confirmed for the delta's text. The
  bullet ending "so the two-step rule above rests on its own grounds" still points at a two-step
  rule (now text then device in one turn) whose ground is his 2026-11-12 words, not focus mode.
  The "goes both ways … not settled here" sentence was replaced whole, and nothing else in the
  delta depends on it. The child template, however, now states the superseded two-turn form
  beside the gap AQ1 records; that contradiction is `160/1440`'s subject and is named there, not
  rated here.
- **A5 — "No scanner holds this" is a fair reading of P5.** Confirmed. The `020` README § P5 and
  § *Why no fix exists* say the rule was built, run over 6,764 replies, fired on 90.6% and was
  deleted the same day; the delta's "one attempt on one corpus" is more careful than `020/270`'s
  "No scanner can hold this".

### Per-lens answers

**Lens 1 — approach.** Right problem, right home: the section that says how an ask reaches him is
where his method belongs, and the record-marks rule belongs beside the definition it serves.
The split holds at two of the three edges the brief names: typed replies were "the case between"
at the delta and are settled at HEAD; a ruling given inside a reply is covered by "unless he says
it is one". The third edge, an answer later cited as authority, is where the delta is thinnest:
it says what an answer is not, never what it is for (AQ2).

**Lens 2 — correctness.** Quotes verbatim; counts and dates match their records; pointers resolve
(ledger below). Three overclaims: the trimmed quote (AQ3), the "one such reply" count (AQ4) and
the uncited four-per-box example (AQ5).

**Lens 3 — harvest.** Of the surfaces the brief lists, `RECORD.md` points at the section (one
home, V4 kept), `REVIEW.md` rule 3 is unchanged and consistent, `00-APEX.md` defines reserved
decisions and challengeability without touching the split (no contradiction), the fleet-sweep
prompts (2026-11-14, after both commits) carry the split in HEAD's settled form, and
`skills/session-onramp/SKILL.md` holds nothing on asking (nothing to mirror). Two surfaces were
not swept: the child template's asking bullet and the glossary (AQ1). The ADR of the same day
defines the marks a second time (AQ6).

**Lens 4 — security and privacy (V6).** Design altitude: the delta publishes his words verbatim,
typos included, which is the house's own standard for his words and carries nothing beyond
`PD4` (his first name); no other person is named; the `[it]` redaction is kept; "several
repositories" and "one session, 2026-11-06 to 11-08" are class-only, and nothing in the delta
names a child, a host, a session id or a path. The hand-up's lines 1–97 name a harness ("VS
Code") and date ranges, which identify no repository. The board records the sweep touched carry a
session id, but they are not the delta. Nothing falls outside `docs/PERSONAL-DATA.md`'s closed
list. Code altitude: `/security-review` discharged on grounds: the delta is three markdown files
with no code, and the tool excludes markdown, so a run would be empty; not invoked.

### Standing checklist V1–V7

- **V1** — bites: AQ3, AQ4, AQ5, AQ9.
- **V2** — all four re-run lines reproduce (ledger below); the recorded figures re-checked by the
  cheapest read-only route, with the two that cannot be re-run named.
- **V3** — bites: AQ1 (template bullet, glossary). Other mirrors checked and sound (lens 3).
- **V4** — bites: AQ6 (the ADR's second definition of the marks).
- **V5** — bites: AQ6 (surface scope). Cross-references, with the rule each reaches:
  `CONCURRENCY.md` § *The channel* (line 564) holds the talk-while-working mechanism the "check
  parallel sessions" bullet relies on; the rule itself is stated in the delta, so the pointer is
  to the means, which is fine. `PROPAGATION.md` § *Pointing up* (line 475) holds the hand-up
  route. `§ When to ask` holds the away-mode rule the delta defers to. `320/110` holds the
  frame-answer rule the surrounding text cites. `115/270` line 42 is a ⚖️ line on a typed reply
  to a two-option question, as described. `310/080` and `320/510` exist with the titles the delta
  summarises. The title-versus-distinction tension is acknowledged in the delta (AQ10, note).
- **V6** — lens 4 above; clean.
- **V7** — provenance above, repeating the brief's and adding the orchestrators.

### Per-claim ledger

| Claim (brief § *The claims*) | Result |
|---|---|
| Four-line list and the follow-up quoted verbatim | Verbatim, but a fragment (AQ3); one of the hand-up's two follow-ups carried (AQ7) |
| Provenance paragraph: his method / reactions / single cases | Honest, except one example is not from the hand-up (AQ5) |
| "An account the session has only read … has reached nobody"; focus-mode agnostic | Matches hand-up § 4 (four asks, nineteen asks, no text written); sound |
| "The ceiling above is the tool's and never a target"; four-question sentence reworded | Sound at HEAD; "still asked up to four per box" uncited (AQ5) |
| An answer: work proceeds; no ruling's weight unless he says so | His words carried verbatim; the consequence of the split is undefined (AQ2) |
| The record marks; "a pick is never written as ruled"; older ⚖️ prove nothing | 💬 shape on 2026-11-09 records confirmed (about 40 lines); older ⚖️ weighed notes confirmed; "one such reply" undercounts (AQ4); surface scope unstated (AQ6) |
| Unmet-term check: no scanner; built and deleted 2026-08-09; 90.6% of 6,764 | Matches the `020` README § P5; `git log -- tools/` shows the 2026-08-09 commit with no P5 code in tools, consistent with deletion before commit; measurement itself not reproducible |
| `CHANGELOG.md`: "Doctrine wording only; no scanner or tool changes" | Stat: 3 markdown files, +115/−7; sound |
| `RECORD.md`: "A pick is an answer and not a ruling; that section holds the difference and the marks" | Present at HEAD; pointer resolves; sound |

### Findings

**AQ1 — MODERATE (V3, lens 3). The child template's asking bullet and the glossary were not
swept.** `docs/build/templates/CLAUDE.md` lines 48–61, the asking bullet every child inlines,
restates the device rule, the two-step shape, the content owed and the recommendation, and
carries neither "one question at a time" nor the answer/ruling split; it points at
`COMMUNICATION.md` § only for "how it travels". A child session reads its `CLAUDE.md` every
session and the pointed section on demand, so the practice he pasted three times reaches the
fleet by pointer only, while the parts of the rule the bullet does inline are the ones he did not
write. `GLOSSARY.md` defines *Principal* and *Authority tier* and has no entry for *ruling* or
*answer*, though the two classes now carry fleet-wide marks. The `CHANGELOG.md` line "Doctrine
wording only" is true of what changed and silent on the mirror. Beside this, outside the delta:
the same bullet still says "always as a finished message of its own … (one extra turn)", which
HEAD's same-turn rule contradicts; that is `160/1440`'s subject and is named here so the sweep is
done once.
*Counsel:* one clause in the template bullet ("one question at a time; the long form in text, the
box short, no reference IDs") and one glossary entry for the pair, stamped from the section.

**AQ2 — MODERATE (lens 1). The split is defined by where a decision came from, not by what it
changes.** The delta says an answer "does not carry a ruling's weight unless he says it is one"
and that "work proceeds on it", and nowhere says what a ruling's weight buys. In the tree, both
bind alike: `RECORD.md`'s two rules rest on an answer ("Adopt both rules", 2026-11-08) and bind;
`REVIEW.md` rule 2's reader-side rule rests on an answer ("Fix the reviewer's side", 2026-11-09)
and binds; `00-APEX.md` § *authority absolute* defines reserved decisions and challengeability
without the split. A session that holds an answer-based rule and asks "may I revise this on my
own judgement, re-ask it, or cite it to settle a dispute in a child" finds no text. The label is
kept honestly and changes nothing a session does, which is the state the brief's first worst
failure describes from the other side: not a session's framing written up as his authority, but
his authority and a session's framing given the same force under different marks.
*Counsel:* two sentences beneath the two bullets: an answer settles the question as asked, in the
session's frame, and the frame stays the session's, open to re-asking or to challenge by
re-briefing without his authority being in question; a ruling settles the matter in his words and
changes only on his word.

**AQ3 — MODERATE (V5, V1). The section's founding quote is trimmed without a mark, and the cut
removes the context the section itself demands.** The hand-up (lines 19–30) gives the paste
whole: it opens *"ask me the questions or decisions you need to finish this work. But when you
ask me a question use the method I described in the atelier doctrine i.e."* and then the four
lines. The delta quotes the four lines only, with no ellipsis, under "His method, as he wrote
it", and paraphrases the opening as "as the method they were to use". The dropped line is the
hand-up's headline fact: he said the method was already in doctrine, and it was not. Two
consequences. A reader cannot tell the list is a fragment. And the house has not found where he
first "described" it: the hand-up's grep found nothing, so either an earlier, fuller statement
exists somewhere the sweep did not reach, or he was recalling his own practice; the delta closes
that question by omission. The ⚖️ bullet forty lines below says his words are "recorded verbatim,
with the context it was given in".
*Counsel:* restore the opening line inside the quote, or mark the cut and add one sentence: he
said it was already in doctrine; the hand-up found it was not; this section is where it now
lives.

**AQ4 — minor (V1). "One such reply stands marked ⚖️ (`115/270`)" undercounts at the delta's own
commit.** Four more ⚖️ lines record typed replies to a session's question, all committed before
`e7370f78` (2026-11-09 12:56 UTC): `310/060` line 79 and `310/160` line 11 (asked by the queue
run, 2026-11-09), `320/060` line 63 and `320/100` line 92 (the same six-checks reply, recorded
twice), in commits `7d5e2f7b` (00:46 UTC) and `56e45a3b` (03:17 UTC). The same-day ADR counted
⚖️ 44 and 💬 66 across items. The sentence reads as a count, and the count sizes the open sweep
(part c) at one when it is at least five. HEAD restates it as "One older reply" (`2a6d7a41`,
`160/1440`'s subject), so the number survives the rewrite.
*Counsel:* "several replies stand marked ⚖️, for example `115/270`; the sweep counts them".

**AQ5 — minor (V1). "The ruling round of 2026-11-09 still asked up to four per box" has no
evidence in the text, and the provenance sentence does not cover it.** The hand-up as filed says
"No instance of a four-question box was traced for this filing" (§ 2). The delta's provenance
paragraph says "All of it was gathered from transcripts in several repositories, 2026-10-30 to
11-08, and handed up", which this example was not: it is an observation of the 2026-11-09 round,
made after the hand-up, by whoever wrote the delta, and nothing says so. Disclosed above: my
sweep showed me one barred line that is the author's account of it; the finding stands on the
doctrine text and the hand-up alone.
*Counsel:* either cite what the sentence rests on (the round's board records, which are in the
tree) or label it as the author session's own observation, not the hand-up's.

**AQ6 — minor (V4, V5). The marks have a second definition, and the rule does not say which
surfaces it binds.** `docs/decisions/2026-11-09-board-states-design.md` line 236 defines ⚖️ and
💬 in its own words and says "the doctrine stays `420/020`'s", a board item; the delta names the
section as the home (`RECORD.md`: "that section holds the difference and the marks") and cites
neither the ADR nor the ADR it. Separately, "A line recording his decision carries one of the two
marks" is read by the ADR as item lines, and by the fleet-sweep prompts as records a session
writes, while the delta's own neighbours in doctrine prose cite picks with no mark
(`COMMUNICATION.md` "(Approved 2026-11-09, `320/110`, as Mike's pick …)", `RECORD.md` "Mike
chose both from options …", `REVIEW.md` rule 2). Either the rule binds board and record lines
only, and should say so, or three doctrine lines beside it already break it.
*Counsel:* one clause naming the surfaces (board items and session records; doctrine prose cites
in words), and a stamp on the ADR's copy pointing at the section.

**AQ7 — note. One of the hand-up's two follow-ups is not carried.** The delta quotes the
2026-11-05 follow-up; the 2026-11-06 one (*"detailed context with impacts, risks, benefits etc in
the session transcript and using askuserquestion"*) is dropped, and `CHANGELOG.md` says "the
follow-up". Harmless in substance (the hand-up notes "benefits" is the apex's "pros"), but the
"in his words" claim is one quote short of its source.

**AQ8 — note (lens 1, home). The unmet-term check sits inside an axis bullet.** It is a
writing-time rule for the agent, placed as the third aside in the *Accessibility of the language*
bullet of § *The axes a calibration covers*, a list of what a person-level calibration covers;
the bullet now runs 24 lines. § *The meta-rules* line 102 already lists the checkable neighbours
of this class (a reference code used before it is explained, an acronym never expanded), and P5
shows this one is the un-checkable member of that family, so it may read better beside them. The
ask bullet's cross-reference ("the term check in the language axis above") resolves, so this is a
taste call, recorded and not rated.

**AQ9 — note (V1). "The self-affirming loop he named the same day" is not in his quoted words.**
`420/020` lines 1–32 quote him and the phrase is the record's own sentence attributing the naming
to him; the rest of the item is barred to me, so I could not confirm he used the words.
*Counsel:* quote the words where the record keeps them, or write "the loop the record names".

**AQ10 — note (V5). Title against distinction, acknowledged.** The section is titled *Asking for
a ruling* and `RECORD.md` points at it by that title in the sentence that says a pick is not a
ruling. The delta names the tension in one sentence and leaves the title; that is consistent and
is recorded for the sweep, not rated.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE (AQ1–AQ3), 3 minor (AQ4–AQ6), 4 notes (AQ7–AQ10).**
The delta records his words faithfully and labels its evidence at the right altitude; what it
misses is the mirror every child reads, the consequence that would make the split more than a
label, and the context line of its own founding quote. The work is doctrine by function, so every
finding is the principal's to decide (rule 3): recorded, nothing applied; counsel sits beneath
each, labelled.

### Re-run ledger

| Line (from the worktree root; `python3` = 3.14.6 on `PATH`) | Exit |
|---|---|
| `git merge-base --is-ancestor e7370f78 HEAD` | 0 |
| `python3 tools/coldsweep.py --selftest` | 0 (`selftest OK`) |
| `python3 tools/coldsweep.py --root . --commit e7370f78 > /dev/null` | 0 |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` (alone, load 3.4 before) | 0; secretscan 🟡 28 advisory, leakscan 🟡 3 advisory, every enforced check ✅ |

Recorded figures: 90.6% of 6,764 and 2026-08-09 match the `020` README § P5 and the 2026-08-09
`tools/` commit subject; the measurement itself is **not re-run** (the reply corpus is not in the
repo). "Three times on 2026-11-05", "asked four times", "four asks", "nineteen asks" match the
hand-up as filed; the transcripts are **not re-run** (house rule). "No scanner or tool changes"
matches the commit stat. Both long quotes match their sources by script.

### Follow-up checklist

- [ ] AQ1–AQ10 to the principal, as one plain-language list with the three MODERATE first.
- [ ] AQ1's template clause lands with a stamp and a `test_templates` update, in the same change.
- [ ] AQ4 and AQ6 feed `420/020` part c (the sweep): count the ⚖️ typed replies, settle the marks'
      surface scope, stamp the ADR's copy.
- [ ] AQ5: the author names what the four-per-box sentence rests on, at act 2.
- [ ] `160/1440` takes the template's "one extra turn" with its own subject (named under AQ1).
- [ ] Act 2: open the sibling and the barred records; reconcile per finding; fold.

### Reconcile (act 2, 2026-11-16 UTC)

Opened after act 1 was committed as `44743bd1`: the sibling (14 questions, 7 facts), `320/820`
line 98 onward, `420/020` line 33 onward, `420/010`, `420/030`, `420/040`, `020/270` line 4
onward, the `160/1250` pointer whole, and both commit bodies (`e7370f78`'s is the subject and a
trailer only; `2a6d7a41`'s names its seven answers and queues `160/1440`). No prior verdict was
needed. Act-1 text above is unrevised.

**Against the pointer's questions (sibling 1–2).** Q1 is answered by AQ3–AQ5 and AQ7: the
bullets' grounding is labelled honestly except the four-per-box example, and the founding quote
is a fragment. Q2: `e7370f78`'s typed-replies sentence was honest when it landed ("not settled
here"), and the author's `420/020` 🤔 sub-bullet said the same ("left open … his to say"). After
his 2026-11-12 pick nothing in the delta still says it is open: `CHANGELOG.md` names only the
sweep and the guard as open, `RECORD.md` says nothing of it, and `420/020` carries the 💬 entry.
`420/030` still lists it "as unsettled" in a list marked asked and answered, which is history,
not a live claim.

**Per finding, against the brief-writer's questions and the author's account.**

- **AQ1 (template, glossary).** Sibling Q9 asks the same. The author's landing notes say nothing
  of the template, and `2a6d7a41`'s body lists the template among the surfaces it touched for
  `cclive`, not for the ask rule, so the mirror was not swept by either commit. Q14 and
  `320/820`'s landing note settle the turn question's history: between 2026-11-09 and 11-12 the
  tree agreed with itself (section and template both said the message ends its turn, after his
  "Always, as two steps" pick); the contradiction arrived with `2a6d7a41`, which is why it is
  `160/1440`'s and not rated here. AQ1 stands as written.
- **AQ2 (consequence undefined).** Sibling Q5 asks whether "work proceeds on it" grants weight
  he did not give or rightly stops an answer being ignored. Both: it is the author's sentence,
  not his, and it is the right sentence as far as it goes, since `420/010` shows answers driving
  work the same day. What AQ2 records is that it is the only sentence about consequence. The
  author's account adds nothing on this. Stands.
- **AQ3 (trimmed quote).** Not asked by the sibling; the author's landing note says the section
  "carries his written method verbatim", which is true of the four lines and silent on the
  dropped opening. Stands.
- **AQ4 (count).** The author's `420/020` part (b) note counted "about 14 of 33 ⚖️ board lines
  concern a ruling or answer" by keyword, then wrote "one typed reply stands marked ⚖️" twice
  (the 🤔 sub-bullet and the 2026-11-12 entry). Sibling fact 5 gives the same 14-of-33. The
  keyword count already said more than one such line existed; the doctrine sentence took the one
  example the author had in hand as the count. Stands.
- **AQ5 (four per box).** The author's account is `320/820` line 100 and `420/030` ("This round
  asked up to four per box"): an observation of the 2026-11-09 round, made by the author, as act
  1 inferred. The counsel narrows: `420/030` is a board record in the tree, so the sentence can
  cite it. Sibling Q10 asks whether the dated incident belongs in a practice bullet and whether
  "ruling round" is itself the conflation: see AQ12 below. Stands, minor.
- **AQ6 (second definition; surface scope).** Sibling Q8 asks what mark a session's own weighed
  note carries after the delta. The ADR answers it ("a session's own call carries neither") and
  the delta does not, which is the second-home problem AQ6 records from the other side. Sibling
  Q7's sweep, re-run here: no doctrine line landed after 2026-11-09 calls a pick "ruled" (the two
  hits are the delta's own sentence and his verbatim "as I've ruled" in `420/040`), so the rule is
  kept in the doctrine that states it. Stands.
- **AQ7–AQ10 (notes).** Q6 (title) is AQ10: the one acknowledging sentence is enough for a
  reader who reaches it, and the title is a sweep matter. Q13 (home of the term check) is AQ8;
  on V4, "The box makes sense on its own" points at the check and does not copy it, so one home
  holds. Q11 (privacy): the author's records name session ids and a harness, the delta names
  neither; lens 4 holds. Q12 (the channel): § *Talk first* gives the means, asking the owner of
  work you meet, and no method for discovering an answer given elsewhere beyond that; the
  pointer is to a means, as act 1 read it, and the duty is satisfiable by asking peers. Q4 (the
  "rests on its own grounds" sentence): true at HEAD, as A4 found; the nineteen same-turn asks
  are evidence for same-turn text, and the bullet rightly declines to claim them either way.
- **Sibling facts.** Fact 2 corrects the brief's "three files": the commit also touched
  `docs/ROADMAP.md` and four board items, which `coldsweep --commit` left out by default. All
  markdown; the `CHANGELOG.md` line "no scanner or tool changes" holds and fact 6 confirms no
  test names the file. Facts 1, 4 and 5 match act 1's re-runs and counts. Fact 7: `160/1440` has
  no brief, so AQ1's template-turn note is the first written record of that contradiction beside
  `420/040`.

**Findings formed at reconcile, marked as such.**

**AQ11 — note, formed at reconcile (sibling Q3, V1). "One was built on 2026-08-09 and deleted
the same day" names a scanner where the record names a rule.** The `020` README § P5 says the
unintroduced-term *rule* (P5, one check inside `plainscan`) was written, measured and deleted
that day; `plainscan` itself lived from 2026-08-09 to 2026-09-18 (`f1d5b5e9`), and the
2026-08-09 commit's tools diff holds no P5 code, consistent with the rule never being committed.
"No scanner holds this. One was built …" reads as a whole scanner tried and dropped;
`CHANGELOG.md`'s "A scanner for this was measured and rejected" says the same. The measurement
and its date are right; what was tried is slightly overstated.
*Counsel:* "a rule for it was built inside the prose scanner of the day".

**AQ12 — note, formed at reconcile (sibling Q10, V5). The section calls the 2026-11-09 round a
"ruling round" in the paragraph that says what it produced were answers.** The round's own
records mark its outcomes 💬 "an answer, not a ruling" (about forty lines), and `420/030` carries
the same name. It is house vocabulary (31 hits across the tree) and no reader will mistake the
label for a classification, so a note only; the sweep in part (c) is the place to decide whether
the phrase keeps its name.

**Overall, restated.** **PASS-WITH-FINDINGS — 0 MAJOR, 3 MODERATE (AQ1–AQ3), 3 minor
(AQ4–AQ6), 6 notes (AQ7–AQ12, the last two formed at reconcile).** Nothing in the sibling or the
author's account moves a severity. Every finding is the principal's to decide (rule 3); nothing
applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-16)

The text below is the brief's `.deferred.md` sibling, verbatim, as the brief-writer wrote it. The
orchestrator (session `d9ce3020`, off-tier, forms no finding) held it outside the tree while the
pass ran, released it to the reviewer only after act 1 was committed (`44743bd1`), and folds it
here at the close so the questions and facts the reconcile answers sit beside it. Nothing in it is
a finding; the verdict and reconcile above are the reviewer's.

# Held back — the principal's method for asking, and an answer is not a ruling

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `43c70bbb`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Does any bullet claim more than its grounding?
2. Is the sentence on words he types in reply to a question honest about what is unsettled? Since
   queued, `2a6d7a41` replaced that sentence on his 2026-11-12 pick. Was `e7370f78`'s version honest
   when it landed, and does anything else the delta wrote (`CHANGELOG.md`, `RECORD.md`, the open 🤔
   sub-bullet in `420/020`) still say the question is open?

## The brief-writer's questions

3. "One was built on 2026-08-09 and deleted the same day." `git log` shows a scanner scoped on
   2026-08-10 and removed on 2026-09-18 (fact 3). Was it the P5 rule inside that scanner, not the
   scanner, that was built and deleted the same day? If so, does the sentence misstate what was
   tried?
4. The "Written to him" bullet ends: "so the two-step rule above rests on its own grounds". At HEAD
   the rule above is text then device in the same turn, and the bullet's own nineteen same-turn
   asks now read as support for it. Does the sentence still say something true?
5. "Work proceeds on it, because it is his decision on what was asked" is not in his words. Does it
   give an answer weight he did not grant, or rightly stop an answer being ignored? Does it sit
   with the apex's "rulings conditioned on being informed"?
6. The section's title, *Asking for a ruling*, and the apex's "governance ruling" use the word the
   new distinction reserves for his own words. One sentence acknowledges it. Is that enough, or is
   it a contradiction every reader meets before the definition (V5)?
7. "A pick is never written as 'ruled'." Sweep `docs/method/` for lines landed after 2026-11-09 that
   still call a pick a ruling. Is the rule followed in the doctrine that states it?
8. ⚖️ "also tag[s] a session's own weighed note" in older lines. After this delta, what mark does a
   session's own weighed note carry? If none, will the old use keep growing?
9. The child template's asking bullet (`docs/build/templates/CLAUDE.md`, lines 48–61 at
   2026-11-14) carries neither one question at a time nor the answer/ruling marks, and still says
   "(one extra turn)". Was the template a mirror site this delta owed (V3), or `160/1440`'s ground,
   or neither because it only points?
10. "The ruling round of 2026-11-09 still asked up to four per box" is a dated incident inside a
    practice bullet. Is a practice bullet its right home, and is calling it a "ruling round" an
    instance of the conflation the same section forbids?
11. Privacy: "One session, 2026-11-06 to 11-08", the four quoted replies, and "nineteen asks" come
    from one child's transcript. Does any of it let a reader with access to the estate pick out
    which child or session, against the hand-up's class-only filing?
12. "Check parallel sessions before asking, by `CONCURRENCY.md` § *The channel*". Does that section
    give a session a way to find out that he has already answered the same question in another
    session? Or is the pointer a name for a duty with no method?
13. The unmet-term check sits in § *The axes a calibration covers*, a list of what calibration
    covers. Is a writing-time rule at home there, and is it one home with "The box makes sense on
    its own", which cites it (V4)?
14. The hand-up's part 3 (whether "completed message" means "end the turn") got "no rewording" in
    the landing note. The 2026-11-12 change then reversed the reading. Did leaving part 3 alone
    leave a contradiction in the tree between 2026-11-09 and 2026-11-12, and is any of it still
    there?

## Facts read off the machine (2026-11-14 UTC, from the worktree root)

1. Re-run lines: `git merge-base --is-ancestor e7370f78 HEAD` exit 0; `coldsweep --selftest` exit
   0; `coldsweep --commit e7370f78` exit 0, 180 lines; `coldsweep --commit 2a6d7a41 --path
   docs/method/COMMUNICATION.md` exit 0, 69 lines; `floor.py --plane ci --root .` exit 0, 34.7 s
   wall clock under `nice -n 10`, Python 3.14.6. The acceptance lines: `grep -c` prints 1; the
   2026-10-03 quote is present within lines 1–32 (wrapped across lines, so a one-line `grep -o` of
   the whole sentence misses it); the option label is present.
2. `e7370f78`'s stat: `CHANGELOG.md`, `docs/ROADMAP.md`, `docs/method/COMMUNICATION.md`,
   `docs/method/RECORD.md` and four board item files. Markdown only.
3. `git log -- docs/method/COMMUNICATION.md` lists `e390382a` (2026-08-10, subject begins
   "plainscan: scope the repo plane") and `f1d5b5e9` (2026-09-18, subject "merge: plainscan removed
   on Mike's ruling; engine archived (020/360)").
4. The `020` section README's P5 account: "90.6% of 6,764 replies fired", 23,857 findings, with a
   three-row table of fixes (90.7%, 90.7%, 90.6%).
5. ⚖️ appears in 28 files under `docs/roadmap/` and in none of `docs/ROADMAP.md`'s lines. The
   author's landing note in `420/020` gives "about 14 of 33 ⚖️ board lines", by a keyword count.
6. No file matching `tools/test_*.py` or `instruments/*.test.js` names `COMMUNICATION`.
7. Neighbouring passes: `160/1210` (the two-step rule as `0ba1ba03` wrote it) has an unrun brief,
   `docs/reviews/2026-11-09-0238-estate-root-reader-side-two-steps-cold.md`; `160/1440` (the
   2026-11-12 answers, `2a6d7a41`) had no brief in `docs/reviews/` when this was written.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

# Review log — atelier 160/1250 (rule-4 cold pass: asking method; answer vs ruling)

Reviewer: Fable 5.1 (claude-fable-5-1). Worktree:
`/Users/mike/worktrees/fable/atelier-160-1250-0545/atelier`. Spawned by headless orchestrator
session `d9ce3020` (Opus 5.5), itself started by drain session `1e053526` (Opus 5.5); both off-tier,
hold the context partition, form no finding. API-credit drain, 2026-11-16.

All commands run from the worktree root with absolute paths. `python3` on PATH used for re-run
lines; version recorded below. Barred reads honoured: no session logs, no prior verdicts, no commit
bodies, no sibling, item text beyond stated ranges.

## Act 1 log

- 05:46 UTC `uptime`: load 5.90 5.78 4.91. `date -u`: 2026-11-16 05:46:53 UTC. Tree: only the
  sibling `.deferred.md` shows deleted (partition). HEAD 73f1cc9a.
- Read the brief whole (271 lines).
- Read `docs/method/REVIEW.md` lines 25-300 (rules 1-4), 300-330 (scope/lenses), 394-470 (re-run,
  V1-V7).
- Re-run lines 1-3, from worktree root, `python3` = /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 (3.14.6):
  `git merge-base --is-ancestor e7370f78 HEAD` exit 0; `coldsweep --selftest` exit 0 ("selftest OK");
  `coldsweep --root . --commit e7370f78 > /dev/null` exit 0.
- Read the delta body-free: `python3 tools/coldsweep.py --root . --commit e7370f78` (3 files, +115/-7;
  5 board files left out by default, not read via --path).
- Read `2a6d7a41` body-free with `--path docs/method/COMMUNICATION.md` (21/21 lines; the two rewrites
  the brief names: same-turn two-step; typed replies are answers).
- Acceptance test: `grep -c 'ask one question at a time'` on 320/820 -> 1; `grep -o '"Answer unless I
  say ruling (Recommended)"'` on 420/020 -> matched, exit 0; `sed -n '1,32p'` 420/020 read; `sed -n
  '1,3p'` 020/270 read; `sed -n '1,97p'` 320/820 read. Nothing beyond those ranges opened.
- Read at HEAD: `docs/method/COMMUNICATION.md` 1-33 (practice/instance split), 55-76 (language axis
  with the unmet-term check), 86-110 (meta-rules; checkable defects list), 214-303 (§ Asking for a
  ruling up to the delta's part), 304-388 via the two diffs. `docs/method/RECORD.md` 335-362.
  `docs/method/00-APEX.md` 68-108 (§ authority absolute / rulings conditioned).
  `docs/build/templates/CLAUDE.md` 46-62 (the asking bullet). `skills/session-onramp/SKILL.md`
  grep for ask/ruling/answer/device: nothing on asking. `docs/method/GLOSSARY.md` entry list and
  47-52: no entry for ruling or answer. `docs/PERSONAL-DATA.md` whole (PD1-PD4).
  `docs/method/CONCURRENCY.md` 564-582 (§ The channel exists at 564; holds the talk-while-working
  mechanism). `docs/method/PROPAGATION.md` § Pointing up exists at 475.
- Grounding of the 90.6% claim: `docs/roadmap/020-.../README.md` 390-427 and 420-445 (P5 built,
  measured, rejected 2026-08-09; 90.6% of 6,764; "Why no fix exists"). `git log` subjects on
  `tools/` 2026-08-08..11: b879b021 "plainscan: P5 built, measured, rejected" 2026-08-09; its
  `--stat` and `git show --format= b879b021 -- tools/` (no body) show only a test-isolation change
  in tools, no P5 code: consistent with the rule deleted before commit. The measurement itself
  cannot be re-run (the reply corpus is not in the repo): NOT RE-RUN beyond the record.
- Item titles (file names only) for 310/080, 320/510, 115/270, 420/040, 420/010, 160/270,
  160/1210, 160/1440 via `ls`. `115/270` lines 38-50: line 42 is a ⚖️ line on a typed free-text
  reply to a two-option question, as the delta says.
- Brief's coldsweep sweep run verbatim (173 hits over 674 files; 730 excluded). Saved by the
  harness to a tool-results file, read with grep. Found: ~40 board lines of the shape "💬 Mike's
  answer, 2026-11-09 (to options queue run ... offered; an answer, not a ruling ...)" (claim
  holds); older ⚖️ lines tagging a session's own weighed note (e.g. GUARDS.md:72, 010/110:23;
  claim holds); and four ⚖️ lines recording typed replies to a session's question, all dated
  2026-11-09: 310/060:79, 310/160:11, 320/060:63, 320/100:92. Also the ADR
  `docs/decisions/2026-11-09-board-states-design.md` lines 90 and 236 (defines the marks; counts
  ⚖️ 44 · 💬 66), and `skills/fleet-sweep/*prompt.md` carrying the answer/💬 rule.
- Dated the four ⚖️ lines by `git log --format='%h %ci %s' -S'⚖️ **Mike' -- <file>` (subjects
  only): 7d5e2f7b 2026-11-09 13:46 +1300 and 56e45a3b 2026-11-09 16:17 +1300; the delta e7370f78 is
  2026-11-10 01:56 +1300. So all four predate the delta.
- Second sweep `'ruling round|four per box|up to four'` with the brief's excludes EXCEPT the
  hand-up file (my omission): it printed one barred line, 320/820 line 100 (the author's landing
  note: "round asked up to four questions per box, against the method this item records").
  Exposure disclosed in the verdict; it changed no finding (AQ5 was formed on lines 1-97 and the
  doctrine text, which hold no evidence for the sentence).
- Mechanical quote compare (python, whitespace-normalised): the four-line list in COMMUNICATION.md
  == hand-up lines; the 2026-10-03 quote in COMMUNICATION.md == 420/020 lines 5-12. Both True.
- Floor: `uptime` load 3.38 before; `nice -n 10 python3 tools/floor.py --plane ci --root .` exit 0
  (secretscan 🟡 28 advisory, leakscan 🟡 3 advisory, all enforced checks ✅). Capture deleted.
- `fleet-sweep` prompt lines dated 4bfb4e16 2026-11-14 (after the delta and after 2a6d7a41).
- Not read: session logs, docs/sessions, docs/reviews verdicts, the sibling, 160/ items beyond
  titles, 420/ beyond 420/020 lines 1-32, 320/820 beyond line 97 (except the one line above),
  020/270 beyond line 3, any commit body. `/security-review` not invoked (no code in the delta).

## Candidate findings (act 1)

- AQ1 MODERATE V3: `docs/build/templates/CLAUDE.md` 48-61 asking bullet carries neither "one
  question at a time" nor answer-vs-ruling; GLOSSARY.md has no ruling/answer entry.
- AQ2 MODERATE lens 1: split defined by provenance, not consequence; RECORD.md two rules and
  REVIEW.md rule 2 reader-side rule rest on answers and bind the same as rulings.
- AQ3 MODERATE V5/V1: the four-line quote drops its first line ("use the method I described in the
  atelier doctrine") with no mark; the section demands context for his words.
- AQ4 minor V1: "one such reply stands marked ⚖️" undercounts by four at the delta's own commit.
- AQ5 minor V1: "ruling round of 2026-11-09 still asked up to four per box" has no evidence in the
  text; the hand-up traced no four-question box; provenance sentence claims all came from the
  hand-up.
- AQ6 minor V4/V5: marks defined in the ADR too with no pointer; the marks rule's surface scope
  unstated while neighbouring doctrine lines citing picks carry no mark.
- AQ7-AQ10 notes: 2026-11-06 follow-up dropped; term-check home; "self-affirming loop he named"
  unverifiable from permitted reads; title vs distinction acknowledged.
- Sound: all quotes verbatim; counts 6,764/90.6%/2026-08-09, three times, four times, nineteen,
  four asks match the records; CHANGELOG "no scanner or tool changes" matches the stat; 💬 shape
  on 2026-11-09 records holds; older ⚖️ weighed notes exist; 310/080 and 320/510 exist with the
  titles claimed; RECORD.md pointer resolves; APEX consistent; lens 4 clean.
- Act 1 verdict written below a `---` divider in the brief; Status line updated. Scanners on the
  brief: datescan, spellscan, wrapscan, linkscan, leakscan all exit 0 (spellscan and wrapscan
  ignore docs/reviews by their ignore files). Lines over 100 columns in my text are table rows
  only (404-412, 539). `git status`: only the brief modified and the sibling deleted (partition).
- Overall: PASS-WITH-FINDINGS, 0 MAJOR, 3 MODERATE, 3 minor, 4 notes. ACT 1 SAVED 2026-11-16 UTC.

## Act 2 log

- Act 1 committed as 44743bd1 (orchestrator). Sibling released at the held path outside the
  worktree; read whole (14 questions, 7 facts). Now opening the barred records and commit bodies.
- Read after release: 320/820 lines 98-end (landing note: part 3 "no rewording"; the 2026-11-09
  round "asked up to four questions per box"); 420/020 lines 33-end (parts a-d; "about 14 of 33
  ⚖️ board lines"; 🤔 typed replies left open; 💬 2026-11-12 "Answer unless I say ruling");
  420/010, 420/030 ("This round asked up to four per box"; the d0ca5d24 list asked 2026-11-12),
  420/040 (the turn stall, fixed by 2a6d7a41); 020/270 line 4-end; 160/1250 pointer whole;
  `git log -1 --format=%B` for e7370f78 (subject + trailer only) and 2a6d7a41.
- Sibling Q7 re-run: `git log --since=2026-11-09 -p -- docs/method/ | grep '^+.*ruled'`: hits are
  the delta's own sentences and his verbatim "as I've ruled" (2a6d7a41). No pick called "ruled".
- Sibling Q12: CONCURRENCY.md 582-640 (§ Three laws, § Talk first): the channel gives a means to
  ask peers; no discovery method beyond asking.
- Reconcile written beneath the verdict; Status updated to VERDICT COMPLETE. No act-1 text
  changed. Two notes formed at reconcile: AQ11 (rule vs scanner, Q3), AQ12 ("ruling round", Q10).
  No severity moved. Scanners on the brief: datescan, spellscan, wrapscan, linkscan, leakscan all
  clean. `git status`: brief modified, sibling deleted, nothing else.
- Overall restated: PASS-WITH-FINDINGS, 0 MAJOR, 3 MODERATE, 3 minor, 6 notes. ACT 2 SAVED
  2026-11-16 UTC.
