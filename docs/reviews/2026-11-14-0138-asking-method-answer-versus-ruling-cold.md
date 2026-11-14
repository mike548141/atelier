# Cold pass — the principal's method for asking, and an answer is not a ruling

**Board:** `docs/roadmap/160-doctrine-review-owed/1250-rule-4-cold-pass-queued-asking-method-and-answer-versus-ruling.md`
**Status:** BRIEF ONLY, not run. Written 2026-11-14 UTC by a headless Opus 5.5 brief-writer
(`cclive` lists it as session `43c70bbb`). Queued, waiting on the principal's explicit approval of
Fable work; this brief is not that approval.

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
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-14-0138-asking-method-answer-versus-ruling-cold.deferred.md` (a held-back
file; by count: 14 questions, 7 facts), every item under `docs/roadmap/160-doctrine-review-owed/`
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
