# Cold pass — the two-tier board states design

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4 and § *Review the design, not
only the build*. A file format every repo's board is read through is doctrine by function (rule 3).
Nothing is built, and that is no reason to shrink the verdict.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** BRIEF ONLY, not run. Written 2026-11-09 UTC by session `9bb1b984`, a headless Opus 5.5
brief-writer. The pass is held for the principal's explicit approval of Fable work; this brief is
not that approval.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1230-rule-4-cold-pass-queued-board-states-design.md`.
**Sequencing:** the queue pointer says the pass is best run after the principal answers the design's
three questions. Whether to wait is his and the taking session's to settle; a pass can run on the
draft either way. If answers have landed, read them as phase-2 material.
**Size of this pass:** medium: a 320-line design with no code, but its measurements span twelve
boards and about 1,200 sessions, and re-running them is most of the work.
**Why it earns a review:** The design sets a format about ten repos build to, and it reads every
existing board through a new set of meanings. The worst failure is a design whose migration reds a
child unannounced, or whose measurements do not support the model it recommends.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, and the Opus worker it dispatched, which wrote the draft (per the queue pointer and
  the design's own record). The author queued this pass and does not take it.
- **Who wrote this brief:** session `9bb1b984` (`claude-opus-5-5`), a headless brief-writer started
  2026-11-09 UTC by coordinating session `74f2b8cd` (Opus 5.5), on the principal's request to brief
  every owed pass. Neither wrote any of this delta. **Off-tier for review, disclosed: the
  brief-writer forms no finding and writes no severity**, and stops after writing. It ran no review
  and used no Fable model. `74f2b8cd` built none of these subjects and forms no finding; its launch
  prompt is the brief-writer's only instruction.
- **Barred from running this pass:** session `9bb1b984` and session `74f2b8cd` (whoever writes a
  brief does not run it, the principal's rule), and session `722ac2e2` with everything it started.
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
  item whole; the design whole; `310/160` whole (ten lines, including its drafted-note line); the
  first 1,200 characters of `310/060` and lines 76–88; the stat of `e36cedcb` and `628e2d26`;
  `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md` whole (an unrun brief, read for house
  form). It opened **no prior verdict and no delta commit's message body**. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's words, printed by these lines. The first is his ruling that the house decides the
vocabulary; the second is the commission. The parenthesis at the start of the second range is the
board's, not his.

```
sed -n '/changing the standard on the roadmap/,/not at all/p' \
  docs/roadmap/310-pointing-up-the-child-to-parent-route/060-the-board-state-vocabulary-is-too-narrow-to-index-by.md
sed -n '/in his own words/,/Design exercise/p' \
  docs/roadmap/310-pointing-up-the-child-to-parent-route/060-the-board-state-vocabulary-is-too-narrow-to-index-by.md
```

## What the work is

- **`e36cedcb`** — `decisions: draft the two-tier board state model (310/160)`.

Delta paths, read at the commit and at HEAD:

- `docs/decisions/2026-11-09-board-states-design.md` (whole)
- `docs/decisions/README.md` (one line)

First confirm the tree holds the delta, then read the commit body-free:

```
git merge-base --is-ancestor e36cedcb HEAD; echo $?
python3 tools/coldsweep.py --root . --commit e36cedcb
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). See what has landed on those paths since: `git log --oneline e36cedcb..HEAD --
docs/decisions/2026-11-09-board-states-design.md docs/decisions/README.md`.

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- "Every change is additive, so no child goes red unannounced."
- `board --check` "blocks and has no advisory form", and step 4 of the migration has it "warn,
  never red, on old shapes".
- Children "get this at their next run with no change of their own".
- The census: 2,494 items in twelve split boards, and each row of the *What the boards show* table.
  Counts are "censuses unless marked **sample**".
- "`[x]` means five things"; "`[~]` means two things"; "`⏳` means two things".
- The readers table and the *Tools must change* list name every reader of an item state.
- His words are quoted exactly, and "if he recalls more, they sit outside what this search can
  reach". `310/080`'s record "is wrong"; "the 'tri-state ruling' is an answer".
- The condition on the 2026-07-23 answer is met by the measurements, and he "accepted a further
  status in terms".
- A parent's state is "declared and checked, not computed", and only named board items count.
- Shape A carries "Low" risk against shapes B, C and D.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs and the measurements that
ground it. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the principal's choice among the three questions' options, as distinct from whether
each question is honestly framed; building or trialling any of it, which this pass must not do.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every reader of a state, every legend, every mirror (V3); one home
   (V4); no contradiction (V5). Check the proposed grammar against the real tools by reading them.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design, including what a state line would newly publish in a public repo's index.
   No code is in the delta: `/security-review` is discharged in one line on those grounds.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root,
except the `cd tools` line, and its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH` (3.14.6 when written); CI pins 3.12.

```
python3 tools/board.py --check --root .
cd tools && python3 -m unittest test_board; cd ..
```

The design's census and its transcript search are recorded proofs (V2): re-run them read-only, by
count, and name no child repo. The transcript search is
`instruments/cctranscript --search --all` with the design's term set. The brief-writer did not re-run
those. A sample the design marks as one read by its author is a claim you may re-draw at your own
seed.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish. Transcripts are private: quote in the verdict only
  what the design already quotes.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0238-board-states-design-cold.deferred.md` (a held-back file; by count: 15
questions, 2 facts), every item under `docs/roadmap/160-doctrine-review-owed/` beyond its title, every
delta commit's message body, and these intent records beyond the acceptance lines above:

- `docs/roadmap/310-pointing-up-the-child-to-parent-route/060-the-board-state-vocabulary-is-too-narrow-to-index-by.md`
- `docs/roadmap/310-pointing-up-the-child-to-parent-route/160-design-exercise-how-we-manage-work-on-the-board.md`

The other records the design cites as prior analysis (`310/070`, `310/080`, `010/100`, `420/020`)
are not intent records and you may read them, disclosing that you did, to test what the design says
of them. The design's own text carries the author's account of why; it is the delta, and reading the
delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/060-the-board-state-vocabulary-is-too-narrow-to-index-by.md \
  --also-exclude docs/roadmap/310-pointing-up-the-child-to-parent-route/160-design-exercise-how-we-manage-work-on-the-board.md \
  'STATE_RE|_MARKER|ITEM_RE|_COLD_ITEM|_LIVE_ITEM|board --check'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, findings with stable IDs (prefix `BT`: `BT1`, `BT2`, …) and severities (MAJOR / MODERATE /
minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a
follow-up checklist. Then STOP: act 1 is committed, unrevised, **before** the sibling is opened.
Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta commit's body; append
`### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions and the
author's account, any finding formed at reconcile marked as such, and the overall line restated.
Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.
