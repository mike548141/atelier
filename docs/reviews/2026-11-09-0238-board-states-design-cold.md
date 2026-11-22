# Cold pass — the two-tier board states design

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4 and § *Review the design, not
only the build*. A file format every repo's board is read through is doctrine by function (rule 3).
Nothing is built, and that is no reason to shrink the verdict.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** RUN 2026-11-22 UTC on Fable 5.1, acts 1 and 2 written and folded:
PASS-WITH-FINDINGS, 0 MAJOR · 3 MODERATE · 4 minor · 3 note (two formed at reconcile). Brief written
2026-11-09 UTC by session `9bb1b984`, a headless Opus 5.5 brief-writer; the pass ran under the
principal's drain order of 2026-11-23 NZDT.
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
(folded below the verdict at the fold; a held-back file; by count: 15
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

---

## Verdict — Fable 5.1 cold pass, 2026-11-22 UTC

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 3 minor · 2 note.** The design's hard
claims hold where they matter most: his mid-turn words exist and are his, the 2026-07-23 pick is
an answer with the condition the design quotes, and the census reproduces in direction on every
row. What does not hold is narrower: two measurements the model leans on do not reproduce under the
tool the model would be built on, and the reader and mirror census is short. Every finding is the
principal's to decide (rule 3); counsel is labelled and kept beneath each.

### Provenance (V7)

- **Reviewer:** this session, Fable 5.1 (`claude-fable-5-1`), the principal-named review tier,
  checked at selection. It read the delta, answered the lenses, assigned every severity and wrote
  this text. Review worktree: a linked worktree of this repo made for this pass alone, named
  `atelier-160-1230-2240`, at HEAD `c8d776d0` (the claim commit).
- **Spawn:** started by headless per-pass orchestrator session `fce21971` (Opus 5.5), itself
  started by drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold
  the context partition, form no finding and write no severity; neither wrote the brief or any of
  the delta. Disclosed here before the findings, as rule 4 requires. The orchestrator's spawn
  prompt was process only: the item, the worktree and brief paths, the barred set (the brief's,
  plus the partitioned sibling), load rules for a shared machine, the live-systems posture, what
  may be written (this file and a review log outside the repo), the deliverable's shape, and the
  release timing (the sibling's path arrives after act 1 is committed). It carried no question about
  the delta, no pointer to where the risk lives and no request about any finding. Its text is in
  the review log, verbatim, which the fold appends to this file.
- **Approval:** the pass runs under the principal's drain order of 2026-11-23 NZDT, verbatim:
  *"Start a fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT
  todat"*. That is the explicit Fable approval the brief's Status line waited for.
- **Barred sessions:** `9bb1b984`, `74f2b8cd`, and `722ac2e2` with everything it started. This
  session was started and instructed by none of them. No contact with any of them, or with the
  author, during the pass.
- **Partition:** the sibling `.deferred.md` was removed from the worktree before I started (it
  shows as a deleted path in `git status`); I did not look for it in any ref, checkout, scratchpad or
  user directory. Not opened. No prior verdict, no session log, no `ROADMAP-DONE.md`, no commit
  message body opened; the three delta commits were read with `coldsweep --commit`.
- **Exposure, disclosed:** the brief whole; `REVIEW.md` whole; the design at `e36cedcb`, at
  `16ee3f09` and at HEAD; `README.md`'s one line; the two acceptance ranges of `310/060` and
  nothing else of it; `310/070`, `310/080`, `010/100`, `420/020` whole (the brief allows them; read
  to test what the design says of them); the first 900 characters of `210/100`; the first three lines
  of `010/190`; the pointer `160/1230` by title only; grep hits in `COMMUNICATION.md`,
  `CONCURRENCY.md`, `RECORD.md`, `GUARDS.md`, `PROPAGATION.md`, the ADR of 2026-08-05, the two
  READMEs under `tools/` and `instruments/`, the roadmap legend, the template board and
  `CHANGELOG.md`; the readers' source around their state regexes. Transcript searches returned
  excerpts into scratch files, including hits in the author session `722ac2e2`; I printed and read
  only session ids, roles, timestamps and yes/no flags, never the excerpts. The harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this
  verdict does not carry.
- **Scope pin:** the brief names `e36cedcb` and says to read the paths at the commit and at HEAD.
  Two later commits touch them: `16ee3f09` (the design, revised to his three answers) and
  `dd3d60d4` (README only, an unrelated line). The design at HEAD says *"The re-review is queued as
  `160/1230` and runs on this revised text"*, so the subject of this pass is the design at HEAD
  (347 lines), with the first version read for what changed.

### Load-bearing assumptions, named first (lens 1)

1. **A1 — The vocabulary is atelier's to set, and he asked for two tiers.** Confirmed by the two
   acceptance ranges: his 2026-08-18 ruling and his 2026-11-09 commission, read from `310/060` by
   the brief's `sed` lines and nothing else.
2. **A2 — His words on states are as the design quotes them, and `310/080` is wrong.** Confirmed,
   by re-run: `cctranscript --search` finds session `1b189e23` ref `8+1` (role `you-mid`,
   2026-07-22T06:35:40Z) and ref `8+2` (`you-mid`, 2026-07-22T06:38:45Z, three minutes later)
   carrying `[-]` and `[^]`. `310/080` verified turn 6 only, before `210/100` made the mid-turn
   channel visible. The timestamps are UTC, so the design's *When (UTC)* column holds.
3. **A3 — The 2026-07-23 "tri-state ruling" is an answer, with the condition the design quotes.**
   Confirmed: with `--tools`, session `64f68104` ref 14 holds the option text (role `tool`,
   2026-07-23T02:06:19Z) containing *"Revisit only if"*, and the pick (role `result`,
   02:16:54Z). A pick from a session's options is an answer by `420/020` and `COMMUNICATION.md`
   § *The record marks*. The legend's "ruling" wording is a correction owed, as the design says.
4. **A4 — The census supports the model.** Confirmed in direction on every row, not in figure
   (BT6); two rows that carry model weight do not reproduce as stated (BT1, BT2).
5. **A5 — Every change is additive, so no child goes red unannounced.** Holds for the box set: the
   readers are regex-anchored and `harvestscan` drops an unmatched line silently (lines 255–290).
   `[/]` and `[-]` are unused as state lines across the fleet (0 and 0), so the namespace is clean.
   The one tightening that would red live items is step 5, which is dated and announced; BT2 says
   what it would red today.
6. **A6 — The readers table names every reader.** Not confirmed: BT3.
7. **A7 — The right altitude.** The design keeps one list and one state line, puts the "why" in a
   required word and the parent in a declared `children:` line, and withdraws its own earlier
   reading of a register quote when his later words were plain. That is the right shape against
   the commission: the general class is the bracket's, the sub-class is the word's, and his
   "mixed" lands as a roll-up rather than a state, with the departure (in-progress is not terminal)
   said plainly. No finding at this altitude.

### Per-lens answers

**Lens 1 — approach.** Right problem, right altitude (A7). The one framing I would attack is the
design's reading of "lived experiences": it mined boards and transcripts well, but two of its three
hand-read samples are the evidence for two model rules, and a 16-item sample is thin for a rule
that tells tools to ignore every checkbox in a body (BT1).

**Lens 2 — correctness.** Claims re-driven, in the order the brief lists them:

| Claim | Result |
|---|---|
| Additive; no child reds unannounced | Holds (A5); step 5's red would hit live claims (BT2) |
| `board --check` blocks, no advisory form; step 4 warns | Holds: `board.py` 946–957 prints a count that is always 0; a warn path is new work BT3 names |
| Children get it at their next run | Holds for CI readers on `floor.yml@main`; not for a child's own legend copy or the private queue tool, which the design says itself |
| Census 2,494 in twelve boards; each row | Direction holds on every row; figures do not reproduce (BT6) |
| `[x]` means five things; `[~]` two; `⏳` two | Holds: 66 `[x]` carry a non-delivery word; 42 of 43 fleet `[~]` carry no `(claimed …)`; 91 `[ ]` heads carry `⏳`, 28 with a review word |
| Readers table names every reader | Overclaims (BT3) |
| His words quoted exactly; `310/080` wrong; tri-state is an answer | Holds (A2, A3) |
| The 2026-07-23 condition is met; he accepted a further status | Holds: the condition is machine-separable dispositions; 66 items carry one in prose today |
| Parent declared and checked; only named items count | Holds as a rule; its stated ground does not (BT1) |
| Shape A "Low" risk | Holds; the word grammar is under-specified (BT8) |

**Lens 3 — completeness.** BT3 (readers and mirrors), BT4 and BT5 (two stale cross-references),
BT8 (grammar). One home (V4): the design is the only home for the model; the README line is a
stamped summary that has drifted (BT5).

**Lens 4 — security and privacy.** No code is in the delta, so `/security-review` is discharged on
those grounds in this line. At design altitude: the new fields put two things on a public index
that the old grammar never did, a repo name beside `moved to` and `(waiting: <repo>)`, and the
design is silent on posture C (BT7). Nothing else over-collects or leaks; `(waiting: him)` names
the principal by pronoun only, which the public board already does.

### The standing checklist

- **V1** — BT1, BT3 (an overclaim each); the rest of the design's claims are no stronger than their
  evidence, and three of its strongest were re-driven and held (A2, A3, A4).
- **V2** — Re-run ledger below. The two recorded proofs (census, transcript search) were re-run
  read-only by count; BT2 and BT6 are what the re-run found.
- **V3** — BT3: the sweep list misses mirror sites and readers.
- **V4** — BT5: the README summary is a drifting copy.
- **V5** — BT4 (a cross-reference to a retired grace); the design otherwise agrees with itself and
  with `420/020`, `COMMUNICATION.md` § *The record marks*, `310/070` and `010/100`, each checked for
  the rule reached, not only the file.
- **V6** — lens 4 above; BT7.
- **V7** — provenance above, repeated from the brief and extended with the orchestrator chain.

### Findings

**BT1 — MODERATE. The sample behind "a checkbox is not a child" does not reproduce, and the rule
built on it leaves the fleet's ticked-with-open-children items as false ticks.** The design reads
16 of 132 `[x]` items with an open indented box and finds *"3 are real open work; 13 are prose
bullets that happen to carry a box"*; on that it rejects computing a parent from sub-lines and tells
tools to ignore every body checkbox. Re-drawn at seed 1230 over the 94 such items on the 22 fleet
boards (175 on all 24), 12 items: 9 read as real open work (a decision owed, an owner action, a
live-proof step, a renewal date, an escrow copy owed, a config defect, an ordered to-do list) and 3
as prose carrying a box. Under the model those 94 parents stay `- ✅` with no roll-up, because no
`children:` line exists and the body is ignored; the migration corrects the 45 (now 66) that say so
in a word and no others. Breaks V1 (*Problems* 5 and the *Rejected* entry rest on a sample that a
re-draw contradicts) and the design's own outcome, *"the tick means done"*. *Counsel: keep the
`children:` rule for parents, and add one migration step that lists every `[x]` whose body holds an
open box for a one-time read, the same "judgements, not a migration" shape as the 36 `[~]`; or
re-draw the sample at a size that settles it before he rules.*

**BT2 — MODERATE. The `(claimed …)` fragment the model keys `[~]` on is not where live claims sit,
so the measurement does not reproduce under `board.py`'s paragraph and step 5 would red every live
claim.** The design counts *"16 of 52"* `[~]` with `(claimed …)` *"on the state paragraph"*. Under
`board.item_state`, the paragraph the generator reads a claim from, 0 of 44 `[~]` items hold the
fragment; 15 hold it lower in the file, after a block start, and the generated index of this repo
shows a claim fragment on 0 of its 6 live `- [~]` lines. This repo's own six live claims, written
on 2026-11-22 UTC by the house's drain, carry the word "claimed" in the paragraph and no
parenthesised fragment at all. So the model's Tier 1 row (*"Held now by a live session, with `(claimed …)`"*), the
`ccclose` row (*"Tighten to the claim fragment"*) and step 5 (*"`[~]` without a claim … a red never
arrives unannounced"*) key on a grammar the boards do not write, and the figure that grounds
*Problems* 2 was counted another way. Breaks V2 (a recorded measurement that does not re-run) and
V1. *Counsel: define the claim fragment the check reads, where on the item it must sit, and measure
the boards against that definition; then say what step 5 would red on the day, by count.*

**BT3 — MODERATE. The readers table and the legend list are not complete, and the design says they
are.** *"The readers table and the Tools must change list name every reader of an item state."*
Not named, each read by grep and source: `instruments/cclive` (imports `ccclose`'s `CLAIM_LINE`,
its own `STATE_MARK` at line 232, counts dated claims only), `instruments/ccopen` (line 356, acts
on cclive's dated claims), `tools/archivecut.py` (line 665, `marker != "[x]"`),
`skills/review-drain/orchestrator-prompt.md` lines 21 and 26 and `fold-prompt.md` line 13 (flip
`[ ]`/`⏳` → `[~]` → `[ ] 🎯`), `skills/fleet-sweep/worker-prompt.md` line 22 (`⏳` state lines are
reviews pending). Mirror sites not in the legend list: `RECORD.md` line 488 and `tools/README.md`
line 1304 state the harvest-integrity gate's live set (`[ ]`/`[~]`/`⏳`) that `[/]` joins;
`REVIEW.md` (seven `⏳` lines), `GUARDS.md`, `instruments/README.md`, the template `CLAUDE.md`. And
the warn-only form step 4 needs is new: `board.py`'s advisory line is fixed at zero (lines 946–957)
and `floor.py` reads it, so *Tools must change* owes a warn channel it does not list. Breaks V3 and
V1. *Counsel: make the readers table a census by grep, state the command, and add the warn channel
to the tools list; the design's "children point at the legend" needs `stampscan`'s stamp named.*

**BT4 — minor. Migration step 6 hangs on a grace that has already been retired.** *"Land it after
`010/190` retires the 2026-11-18 grace, on that same accept-both-forms mechanism"*. `010/190` is
`[x]`; `734930ef` removed both 2026-11-18 graces, and `ddc868ff` added a different full-form grace
to 2026-12-04 (`board.py` line 976, legend line 32). The mechanism survives; the reference does not.
Breaks V5. *Counsel: name the current grace and its date, or name the mechanism without a date.*

**BT5 — minor. `docs/decisions/README.md` line 50 still summarises the first version.** It says
*"waiting is a field, never a state"*; the revision says a real blocker is a field and a maybe-later
item gets no mark, by his words. The index line is the one stamped copy of the model and it has
drifted. Breaks V4. *Counsel: one-line edit when the next revision lands.*

**BT6 — minor. The census is labelled a census but its method is not recorded, so it re-runs in
direction only.** No script, word set, paragraph definition or sample seed is in the delta. Re-run
on 2026-11-22 over the 22 boards that float on `floor.yml@main`: 2,733 items; `[ ]` 1,194 · `[x]`
1,489 · `[~]` 43 · `⏳` 7; 66 `[x]` with a non-delivery word; 91 `[ ]` with `⏳`; 293 with 🎯; 98
whose paragraph says DONE/FIXED/BUILT; 91 of 234 sections mixed; 402 files with an indented box; 94
`[x]` holding an open one; RULED 327 · ⚖️ 25 · 💬 53. Twenty-four local boards hold `docs/roadmap/`
now (the design measured twelve), and `cctranscript --list --all` sees 1,620 sessions (1,208). The
one figure that reproduced to the digit: the closed set is 7.57 MB, about 1.9 M tokens (*"about 7
MB, around 2 million tokens"*). Breaks V2 in form, not substance. *Counsel: put the census script,
or its regexes and frame, in the design or beside it, so the next pass re-runs the same thing.*

**BT7 — note (lens 4). Two new fields put a repo name on a public index, and the design does not
say what they may carry.** `[-] moved to X` requires *"the repo and item it moved to"* and
`(waiting: <repo>)` names a repo; on this public board either can name a private child and its
item number. The ADR of 2026-08-05 (posture C) allows a private repo's name for an act or role and
bars its internal state; a `moved to <repo> 020/381` is both. `leakscan`'s local term list is the
mechanical catch today. *Counsel: one sentence in the design: on a public board the target of
`moved` and `waiting` is a repo's type or a public name, never a private item.*

**BT8 — note. The Tier 2 word grammar is under-specified for the check it promises.** The outcome
lists four words; the table adds *"also declined or dropped"* as aliases; the render table uses
`superseded by X`, `duplicate of X`, `moved to X` with no form for a cross-repo target; Shape A says
*"an unknown word fails loud at check"* while step 4 says the check only warns. None of this is
wrong; none of it is yet a grammar a parser can be written to. *Counsel: one table of the accepted
words, their aliases, the target form in-repo and cross-repo, and which phase reds an unknown word.*

### Re-run ledger

| Line | Result |
|---|---|
| `uptime` before each heavy line | load 11–30 on a shared machine; every heavy line ran under `nice -n 10`, one at a time |
| `git merge-base --is-ancestor e36cedcb HEAD` | exit 0 |
| `git log --oneline e36cedcb..HEAD -- <delta paths>` | `16ee3f09`, `dd3d60d4` |
| `coldsweep.py --root . --commit e36cedcb` / `16ee3f09 --path <design>` / `dd3d60d4 --path README` | exit 0 each; body not printed |
| `coldsweep.py` with the brief's three `--also-exclude` and its pattern | hits in the four readers, `ccclose`, `CHANGELOG.md`, the design, 6 board files (titles not read) |
| `board.py --check --root .` | exit 0, index current, advisory 0 |
| `python3 -m unittest test_board` from `tools/` | Ran 109 tests, OK, exit 0 |
| Census over 24, 22 and 12 boards (read-only, count only) | figures in BT6 |
| Sample re-draw, seed 1230, 12 of 94 | 9 real work, 3 prose (BT1) |
| `cctranscript --list --all --json` | 1,620 sessions |
| `cctranscript --search` `supersceeded`, `superceeded`, `work declined`, `machine-separable` (and `--tools`) `--all --json` | ids, roles and timestamps only (A2, A3); 1,621–1,622 sessions swept each |
| `/security-review` | discharged: no code in the delta |
| `310/060` option numbering ("option 1", "option 2") | NOT RUN: the record is barred beyond the acceptance lines |
| The 50-item `[x]` and 40-item open samples | NOT RE-DRAWN: each needs a hand read of 40–50 child items; the 16-item sample was re-drawn instead because a model rule rests on it |

### Follow-up checklist

- [ ] 🎯 BT1–BT3 are his to rule: whether the parent rule gets a one-time read of ticked parents
      with open bodies, how a claim is written and checked, and whether the readers census is
      redone before any tool changes.
- [ ] BT4, BT5, BT6: form corrections for whoever next revises the design.
- [ ] BT7, BT8: one sentence and one table in the design, before a parser is written to it.
- [ ] The corrections the design already says are owed (`310/080`'s text, the legend's "ruling"
      wording) stand confirmed by this pass's re-runs and can be applied on his word.
- [ ] Act 2: open the sibling (15 questions, 2 facts) and the barred records, screen the delta
      commits' bodies, reconcile below.

### Reconcile

Written 2026-11-22 UTC after act 1 was committed as `1235389b`, unrevised. Opened at this step: the
sibling (15 questions, 2 facts), the bodies of `e36cedcb` and `16ee3f09`, `310/060` and `310/160`
whole, and the pointer `160/1230`. Act-1 text above is unchanged.

**The author's account.** Both commit bodies restate the design and add no claim the text does not
make. `310/160`'s drafted and revised notes and his three answers match the design's *Decided by
him* table word for word. `310/060`'s option list confirms the design's "option 1" is the renderer
reading prose and "option 2" the disposition field, which closes the one line my ledger marked NOT
RUN. The pointer discloses the orchestrator arrangement, as rule 4 requires.

**The sibling's facts.** The brief-writer's re-runs (`board --check` exit 0, `test_board` exit 0)
match mine. It confirmed the five regex names and tested none; testing them is what BT3 found.

**Per finding, against the sibling's questions:**

- **BT1** meets Q2 and Q12. Q12 asks what stops a parent not declaring its children: nothing, and
  the check sees only a contradiction in a declaration that exists. That is the same gap as BT1 seen
  from the rule's side; the 94 ticked parents with open bodies are the measured case of an
  undeclared parent. BT1 stands.
- **BT2** meets Q2 and Q7. Q7 asks whether `[~]`-as-part-done is one child's habit: the census says
  42 of 43 fleet non-claims sit in one board, but `310/070` and `010/100` record two children that
  reached for `[~]` independently, so it is a vocabulary gap with one heavy user. BT2's point is
  narrower and unchanged: whatever the box means, the fragment the check reads is not where the
  boards write it.
- **BT3** meets Q3 in part. Stands.
- **BT4** is Q14. The sibling asked whether the 2026-11-18 date was realistic; it had already passed
  and the grace it named was already removed. Stands as written.
- **BT5**, **BT6** — not raised by the sibling; Q9 asked for a fresh census and BT6 holds its
  figures. Stand.
- **BT7** is Q13. The sibling points at `RECORD.md` § *The record is public*, which I had not cited:
  it says naming a private sibling is not itself the harm; the harm is the name coupled to its
  sensitive posture, and the test is whether the name is load-bearing for the lesson. That sharpens
  BT7 rather than changing it: `moved to <repo> <item>` couples a private name to that repo's board
  state, and the design should say which join is allowed on a public board. Stands, with that
  section added to its grounds.
- **BT8** meets Q11. How a check knows which work is his: the design's own *Basis* column (his words
  or his answer, recorded) gives the trace, a ⚖️ or 💬 beside the `[-]`, but the design does not
  say the check requires it. That belongs in the grammar table BT8 asks for. Stands.
- **Q4, Q5, Q6, Q8, Q15** — read and discharged, no finding: step 2 is explicit that only a line a
  child marks anew renders differently, so a tool update alone stales no committed index (Q4);
  `board.py` squeezes the title to the room the prefix leaves (`WRAP_COLS` 85, `TITLE_MIN` 24,
  `_fit_title`), so a longer prefix shortens the title and fits (Q5); *Problems* 3 keeps its
  "about half" tied to the 40-item sample and the revised question says so again, so it is a sample
  proportion stated as one, though it is the sample I did not re-draw (Q6); 8 is `⏳` as the marker
  and 162 is `⏳` as a flag on `[ ]` lines, which the table's row names, and the re-run gives 7 and
  91 (Q8); the word and the field sit on the state line beside the box and are checked against it,
  so they are not the second home the 2026-08-15 decision refused, which was a field duplicating the
  box elsewhere in the file (Q15).

**Formed at reconcile, from the sibling's questions (marked as such):**

**BT9 — note, formed at reconcile (Q3). "Additive" is proven for CI, not for a local checkout
behind `main`.** A child's session or pre-commit hook runs whichever atelier checkout its links
point at. A `[-]` written while that checkout predates step 1 reds the writer's own `board --check`
(`STATE_RE` no match, "no state line", exit 1) while CI on `floor.yml@main` passes. The red lands on
the hand that wrote the box, so it is not unannounced; it is a pin-lag the design does not mention.
*Counsel: one sentence in step 1 naming it, and the pin-bump step that closes it.*

**BT10 — minor, formed at reconcile (Q10). The one departure from his words is argued, not asked.**
His commission puts *"a mixed status or an in-progress"* inside the no-more-work class; the design
splits it (in-progress is live, a mixed parent is closed with a roll-up) and says so plainly, but
the point is not among the questions he was asked, and the three he answered did not touch it. For
doctrine he commissioned, a departure from his words is his to confirm, not the author's to settle
by argument (`REVIEW.md` rule 3). Breaks lens 1's "honestly framed" test for the questions.
*Counsel: add it to the open question as a confirmation: "your 'mixed' class becomes a roll-up, not
a state, for this reason; confirm or say otherwise".*

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 4 minor · 3 note** (act 1's 0 ·
3 · 3 · 2, plus BT10 minor and BT9 note formed at reconcile). No act-1 finding was changed by the
sibling or the author's account; two gained grounds (BT7, BT8).

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (`1235389b` on `main`);
folded here verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (headless session `fce21971`, Opus 5.5, started by drain session `eca14b23`, itself
Opus 5.5) held the partition, formed no finding and wrote no severity.*

### Held back — the board-states design

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer, session `9bb1b984`, which did not author the delta.

#### The pointer's own questions

1. Does the migration keep every child green?
2. Do the measurements support the model?

#### The brief-writer's questions

3. "Additive" rests on children reading atelier's tools at `floor.yml@main`. What about the local
   hook's copy, a child with an older checkout of atelier, or a `[-]` written while a sibling
   session's tools predate step 1? `board --check` exits 1 on an unknown box: is there a window in
   which a new box reds a run?
4. Step 1 says "nothing renders differently". The rendering table gives `[/]`, `[-]` and a waiting
   field new index text. Which step actually changes the index, and does that stale a committed
   index in a child that takes a tool update and no item change?
5. A longer index-line prefix (`- [ ] ⏸️ him`, a roll-up count): does it still fit `wrapscan`'s
   width, and `sizescan`'s hot-path rules?
6. The design says the table's samples are "not extrapolated". Problem 3 says "about half … is not
   takeable", and the outcome rests on it. Is that extrapolation?
7. Problem 2 is a house-wide claim on `[~]`. The table says 35 of the 36 non-claim `[~]` sit in one
   child. Is that a state vocabulary problem or one child's habit?
8. The census shows `⏳` as a first-line state 8 times and on 162 open items' state lines. Reconcile
   the two counts: what is the 162 counting that the 8 is not?
9. 1,245 + 1,189 + 52 + 8 = 2,494 and 1,189 − 45 = 1,144. Those two add up. Do the other figures
   survive a fresh census at a fresh date, and how much have the boards moved?
10. The design departs from his two-tier words on "mixed", and says so "plainly". It is not among the
    three questions put to him. Should it be? Are the three questions the ones that are really his?
11. "Who may set what": `[-] not-required` is "Mike only" on "work Mike commissioned". How does a
    session or a check know which work that is, across 2,494 items that do not record it?
12. A parent is "declared and checked". What stops a parent simply not declaring its children? Does
    the check catch the absence, or only a contradiction in a declaration that exists?
13. `(waiting: <repo>)`, `[-] moved to X` and the roll-up put a repo name on a public index line.
    What does `RECORD.md` § *The record is public* say about a private repo's name beside its
    state, and does the design's grammar invite exactly that join in a public tree?
14. Phase 2's grace is tied to `010/190` and 2026-11-18. Is that date realistic given this draft is
    not ruled, and what happens to two graces if it slips?
15. Rejected shape C cites a 2026-08-15 store decision. Does `(waiting: …)` plus `children:` plus the
    tier-2 word amount to the second state vocabulary that decision refused, on the item's first line
    rather than in frontmatter?

#### Facts held back

- **Re-run lines, 2026-11-09 UTC, run from the worktree root (the `cd tools` line from `tools/`).**
  `python3` was 3.14.6. `board.py --check --root .` exit 0; `test_board` exit 0.
- The brief-writer confirmed `STATE_RE` is in `tools/board.py`, `_MARKER` in `tools/pointerscan.py`,
  `ITEM_RE` in `tools/harvestscan.py`, `_COLD_ITEM` and `_LIVE_ITEM` in `tools/sizescan.py`, and
  `ITEM_STATE`/`STATE_LINE`/`CLAIM_LINE` names in `instruments/ccclose`. It did not test what each
  does. It re-ran no census and no transcript search.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*The reviewer's work log, kept outside the worktree while the pass ran and read by no other session
until act 2 was saved; appended here verbatim at the fold (headings demoted two levels, form only)
and the working file deleted. One form fix at the fold: a `secretscan` allow-marker on one script
line, a print label the scanner read as an assigned secret.*

### Review log — atelier 160/1230, two-tier board states design cold pass

Reviewer: Fable 5.1 (claude-fable-5-1), spawned by orchestrator fce21971 (Opus 5.5), itself by drain
session eca14b23. Worktree: /Users/mike/worktrees/fable/atelier-160-1230-2240/atelier
Brief: docs/reviews/2026-11-09-0238-board-states-design-cold.md

#### Act 1 steps

- 2026-11-22T22:42Z `uptime`: load 11.39 14.03 14.78 (shared laptop; heavy lines under nice -n 10).
  `git status --short`: only ` D docs/reviews/...deferred.md` (partition, expected). HEAD c8d776d0.
- Read the brief whole (214 lines).
- Read `docs/method/REVIEW.md` whole (rules 1-4, lenses, standing checklist V1-V7, lifecycle).
- Acceptance test: ran the brief's two `sed -n` ranges on `310/060` (only those ranges; the file is
  otherwise barred). Ruling 1 (2026-08-18): vocabulary is atelier's to set, child repos propose.
  Commission 2 (2026-11-09): two tiers/classes, general class "no more work to be done on this item
  and any children" with child classes done / not required / superseded / duplicate / mixed or
  in-progress; "Run a design exercise based on the lived experiences of our past sessions".
- `git merge-base --is-ancestor e36cedcb HEAD` -> exit 0 (delta is in the tree).
- `git log --oneline e36cedcb..HEAD -- <delta paths>`: two later commits touch the paths:
  16ee3f09 "decisions: revise the board-states draft to his answers (310/160)" (design only, +87/-59)
  and dd3d60d4 "doctrine: land the evidence-window rule and the declaration standard's design"
  (README.md only, adds an unrelated line; the board-states README line is unchanged).
- `python3 tools/coldsweep.py --root . --commit e36cedcb` -> exit 0, subject+stat+diff only (319-line
  design + 1 README line). Then `--commit 16ee3f09 --path <design>` and `--commit dd3d60d4 --path
  README` -> exit 0 each; no message body read. The revision retitles "waiting as a field" to "a
  blocker as a field", adds "Decided by him, 2026-11-09" (3 answers), narrows (waiting:) to real
  blockers, drops `(waiting: fable)`, withdraws the register quote, leaves ONE question (does a real
  blocker get a mark). Design says "The re-review is queued as 160/1230 and runs on this revised text".
- CANDIDATE (V4/V5): `docs/decisions/README.md:50` still summarises v1 ("waiting is a field, never a
  state"); the revised design says a blocker is a field and maybe-later gets no mark. Stale summary
  at the index, one fact two homes drifting. Severity to settle: minor.
- Pointer title read by `ls` only: 1230-rule-4-cold-pass-queued-board-states-design.md (body barred).
- coldsweep pattern search (brief's line, 3 --also-exclude) -> hits in CHANGELOG.md, the design,
  tools/board.py:204 STATE_RE, tools/harvestscan.py:174 ITEM_RE, tools/pointerscan.py:250 _MARKER,
  tools/sizescan.py:309/338, instruments/ccclose:2086-2098; 6 roadmap hits (titles not read).
- Readers grep (`[~]|[x]|[ ]|⏳` across tools/ instruments/ skills/): the design's table names
  board.py, pointerscan, harvestscan, sizescan, ccclose, a private child's queue tool, floor/floorfleet
  (none). NOT in the table but reading state: instruments/cclive (STATE_MARK /^\s*[-*]\s+\[~\]\s*/,
  line 232; imports CLAIM_LINE from ccclose, line 32; distinguishes dated claims), instruments/ccopen
  (line 356, uses cclive's dated claims), tools/archivecut.py:665 (board.item_state(...).marker !=
  "[x]"), skills/review-drain/orchestrator-prompt.md:21,26 and fold-prompt.md:13 (flip `[ ]`/`⏳` ->
  `[~]` -> `[ ] 🎯`), skills/fleet-sweep/worker-prompt.md:22 (`⏳` state lines = reviews pending).
  floorfleet.py:1334 uses ⏳ as a run-status glyph only: design's "reads no item state" holds.
- Mirror sites (grep count of state-glyph lines): CONCURRENCY.md 20, roadmap/README.md 22,
  tools/README.md 10, RECORD.md 7, REVIEW.md 7, GUARDS.md 2, template ROADMAP.md 2, instruments/README
  2, PROPAGATION.md 1, templates/CLAUDE.md 1, REPO-STANDARD.md 1, README.md 1. The design's legend
  list names roadmap/README.md, template ROADMAP.md, children's copies, CONCURRENCY § Claiming work
  only. RECORD.md:488 and tools/README.md:1304 state the harvest-integrity gate's live-marker set
  (`[ ]`/`[~]`/`⏳`) which `[/]` would join: mirror sites not named.
- board.py:946-957 ADVISORY_COUNT_PREFIX / advisory_count_line: "Every board finding blocks, so for
  the board the count is always 0" -> design's "board --check blocks and has no advisory form" is
  accurate for findings; a warn channel exists in form (the count line), unused. Confirmed.
- pointerscan.py:415 `[x]` never a pointer; :241 QUEUED="⏳"; _MARKER accepts [ xX~]. Confirmed.
- ccclose:1201 CLAIM_LINE = /^\s*[-*]\s+\[~\]/ counts every [~] bullet (indented too) as a claim ->
  design's claim about ccclose confirmed. cclive (232, 286) and ccopen (356) count DATED claims only,
  so the "36 non-claims read as claims" cost is ccclose's, not cclive's: design silent on both.
- Legend docs/roadmap/README.md:35-49 read: "work-owed tri-state, never a disposition (Mike's
  ruling, 2026-07-23 ...)", "never a fourth bracket". The design calls the 2026-07-23 pick an
  answer (420/020). Tension to test: 420/020 (read, allowed) defines ruling = his words verbatim,
  answer = pick from options; 310/080 (read, allowed) records the 2026-07-23 pick "Keep three
  (Recommended)" as a *ruling* and says he never typed [-]/[^]; design says 310/080 is wrong on the
  typing (mid-turn messages invisible to cctranscript before 2026-09-18, 210/100) -> to verify by a
  read-only transcript search, count/existence only.
- 310/070 read (allowed): a child's `[~]` = part-done OR claimed; `⏳` = waiting on the owner; options
  (a)-(d). 010/100 read (allowed): 38 `[~]` in one child without claims; "38 judgements, not a
  migration". Design's citations of both hold.
- `python3 tools/board.py --check --root .` (nice) -> exit 0, "board index current", advisory 0.
- Local census frame: 24 repos under the pets root have docs/roadmap/; 22 float on floor.yml@main;
  1 has a single-file board only. Design measured "twelve split boards (atelier and eleven
  children)" on 2026-11-09. Reported by count only.
- `( cd tools && nice -n 10 python3 -m unittest test_board )` -> "Ran 109 tests in 23.884s OK", exit 0.
- Census re-run (read-only, every repo under the pets root with docs/roadmap/, items = `<section>/*.md`
  minus README.md, state via board.item_state imported from this worktree's tools/board.py).
  Frames: all 24 split boards; the 22 that float on floor.yml@main; the 12 largest.
  floor.yml@main 22: items 2,733; `[ ]` 1,194 · `[x]` 1,489 · `[~]` 43 · `⏳` 7; no-state 0;
  `[x]` with a non-delivery word in the first 260 chars of the paragraph 66 (word set: supersed|not
  required|not needed|no longer required/needed/wanted|duplicate|moved to|declined|dropped|
  withdrawn|retracted|closed as); `[~]` with "(claimed" in board.py's paragraph 0, anywhere in the
  file 15 of 44 (all frames), word "claimed" in paragraph 11; non-claim `[~]` per board sorted
  [42,1,0,...] (one child dominates, as the design says of 35); `⏳` on a `[ ]` head 91 (144 in the
  12 largest, 149 in all 24), with a review word 28; 🎯 on `[ ]` head 293; `[ ]` with
  DONE/FIXED/BUILT/LANDED/SHIPPED/RAN in first 260 chars 98; sections 234, mixed 91; files with an
  indented checkbox 402; `[x]` files holding an indented `[ ]`/`[~]`/`⏳` 94 (175 in all 24);
  RULED 327 files · ⚖️ 25 · 💬 53 (all 24: 378 · 54 · 149). Design (2026-11-09, 12 boards): 2,494
  items; 1,245/1,189/52/8; 45; 16 of 52; 162; 412; 60; 96 of 172; 491/132; 337/44/66. Direction
  reproduces on every row; exact figures do not (two weeks' growth, unstated word sets, and the
  "state paragraph" the design counted claims on is not board.py's).
- Claim-position debug (counts only): across the 44 `[~]` items the first line carrying "claimed"
  is line index 0 once, else 3-10 (after a block start), so board.py's paragraph never holds the
  fragment. Atelier's own 6 live `[~]` items: "(claimed" nowhere in the file, word "claimed" in the
  paragraph for all 6; the generated index's 6 `- [~]` lines carry no `(claimed` fragment.
- `[x]` set size (22 boards): 1,489 items, 7.57 MB, ~1.89 M tokens at 4 bytes/token: design's "about
  7 MB, around 2 million tokens" holds.
- State lines already using `[/]` or `[-]` across the 22 boards: 0 and 0 (clean namespace). One
  atelier file mentions `[/]`: 310/160, the barred intent record (not read).
- Sample re-draw (seed 1230, random.sample over the 94 fleet `[x]` items with an open indented
  box; 12 drawn; judged on the first open sub-line's first 110 chars, printed to my context only):
  9 read as real open work (a decision owed, an owner action, a live-proof step, a renewal date, an
  escrow copy, a config defect, ordered to-dos), 3 as prose carrying a box (a "what is left open"
  note, a pattern note, a struck-through line). Design's sample: 3 of 16 real work, 13 prose.
- `instruments/cctranscript --list --all --json`: 1,620 sessions (design: 1,208 on 2026-11-09).
- `cctranscript --search 'supersceeded' --all --json` (layers prompts+replies): swept 1,621, matched
  8, hits 16. Session 1b189e23 hits: ref 6 role=you 2026-07-22T04:31:07Z; ref 8+1 role=you-mid
  2026-07-22T06:35:40Z. Timestamps are Z (UTC): design's "When (UTC)" column holds. Hits also in
  the author session 722ac2e2 (harness/claude roles, 2026-11-09): not read.
- `--search 'superceeded'`: swept 1,622, matched 2, hits 3; 1b189e23 ref 8+2 role=you-mid
  2026-07-22T06:38:45Z, excerpt carries `[^]`. `--search 'work declined'`: 1b189e23 ref 8+2 excerpt
  carries `[-]`, `[^]`, `[~]`, `[ ]`. => He typed `[-]` and `[^]` in his own mid-turn channel, three
  minutes after 8+1: the design's correction of 310/080 is CONFIRMED (310/080 verified turn 6 only).
- `--search 'machine-separable' --all --json` (prompts+replies): 1 session (a child, 2026-08-18
  harness), the 2026-07-23 option text not reached. With `--tools`: 64f68104 ref 14, role=tool
  2026-07-23T02:06:19Z and role=result 2026-07-23T02:16:54Z, excerpt carries "Revisit only if":
  the condition sat in the option text and the pick is a tool result => an answer under 420/020,
  as the design says. 310/080's 02:16:54 UTC matches.
- 010/190 head (3 lines): `[x]` "Remove the two adoption graces once 2026-11-18 has passed";
  `git log -S` shows 734930ef removed them and ddc868ff added the current full-form grace to
  2026-12-04 (board.py:976; roadmap/README.md:32; tools/README.md:110). Design migration step 6
  says "after 010/190 retires the 2026-11-18 grace": stale reference.
- ADR 2026-08-05 lines 174-175, 261 read: posture C (private repo's internal state by type only in
  a public record; naming for an act/role allowed). COMMUNICATION.md 363-386 read: ⚖️/💬 marks; the
  design's "Answer or ruling" paragraph agrees. CHANGELOG 2350-2360 read (grace notice).
- harvestscan.py 255-290 read: an unmatched line ends the current item silently (no red), so a
  `[-]` line before readers change is dropped from the fingerprint, not red.

#### Scripts used (scratch, deleted at finish; reproduced here for the record)
```
import sys, re, os, glob
from pathlib import Path
sys.path.insert(0, "/Users/mike/worktrees/fable/atelier-160-1230-2240/atelier/tools")
import board
PETS = Path("/Users/mike/.pets")
CODE = re.compile(r"`[^`]*`")
NONDELIV = re.compile(r"supersed|not required|not needed|no longer (?:required|needed|wanted)|duplicate|moved to|declined|dropped|withdrawn|retracted|closed as", re.I)
DONEW = re.compile(r"\b(DONE|FIXED|BUILT|LANDED|SHIPPED|RAN)\b")
SUB = re.compile(r"^\s+[-*]\s+(\[[ x~]\]|⏳)")
SUBOPEN = re.compile(r"^\s+[-*]\s+(\[[ ~]\]|⏳)")
REVW = re.compile(r"review|pass|brief|verdict|fable", re.I)
def floats(repo):
    wf = repo / ".github" / "workflows"
    if not wf.is_dir(): return False
    for f in wf.glob("*.yml"):
        if "atelier/.github/workflows/floor.yml@main" in f.read_text(errors="ignore"): return True
    return False
rows = []
for repo in sorted(PETS.iterdir()):
    b = repo / "docs" / "roadmap"
    if not b.is_dir(): continue
    c = dict(repo=repo.name, fleet=floats(repo), items=0, none=0, st={"[ ]":0,"[x]":0,"[~]":0,"⏳":0},
             x_nondeliv=0, tilde_claim=0, tilde_noclaim=0, tilde_released=0, hour_open=0, hour_open_review=0,
             tgt_open=0, open_done_word=0, sections=0, mixed=0, files_sub=0, x_with_open_sub=0,
             ruled=0, scales=0, speech=0)
    for sec in sorted(p for p in b.iterdir() if p.is_dir()):
        c["sections"] += 1
        has_x = has_live = False
        for f in sorted(sec.glob("*.md")):
            if f.name == "README.md": continue
            t = f.read_text(encoding="utf-8", errors="replace")
            c["items"] += 1
            st = board.item_state(t)
            if st is None:
                c["none"] += 1; continue
            m = st.marker; c["st"][m] += 1
            head = CODE.sub(" ", st.head); rest = st.rest
            if m == "[x]":
                has_x = True
                if NONDELIV.search(CODE.sub(" ", rest)[:260]): c["x_nondeliv"] += 1
            else:
                has_live = True
            if m == "[~]":
                if "(claimed" in CODE.sub(" ", rest): c["tilde_claim"] += 1
                else: c["tilde_noclaim"] += 1
                if re.search(r"released|stale", rest, re.I): c["tilde_released"] += 1
            if m == "[ ]":
                if "⏳" in head:
                    c["hour_open"] += 1
                    if REVW.search(rest[:260]): c["hour_open_review"] += 1
                if "🎯" in head: c["tgt_open"] += 1
                if DONEW.search(rest[:260]): c["open_done_word"] += 1
            lines = t.splitlines()
            if any(SUB.match(l) for l in lines): c["files_sub"] += 1
            if m == "[x]" and any(SUBOPEN.match(l) for l in lines): c["x_with_open_sub"] += 1
            if "RULED" in t: c["ruled"] += 1
            if "⚖️" in t: c["scales"] += 1
            if "💬" in t: c["speech"] += 1
        if has_x and has_live: c["mixed"] += 1
    rows.append(c)
def tot(rs, k):
    if k == "st":
        o = {"[ ]":0,"[x]":0,"[~]":0,"⏳":0}
        for r in rs:
            for kk in o: o[kk] += r["st"][kk]
        return o
    return sum(r[k] for r in rs)
def report(label, rs):
    print(f"== {label}: {len(rs)} boards ==")
    for k in ["items","none","st","x_nondeliv","tilde_claim","tilde_noclaim","tilde_released","hour_open","hour_open_review","tgt_open","open_done_word","sections","mixed","files_sub","x_with_open_sub","ruled","scales","speech"]:
        print(f"  {k}: {tot(rs,k)}")
    print("  items per board (sorted, anonymous):", sorted((r["items"] for r in rs), reverse=True))
    print("  non-claim [~] per board (sorted):", sorted((r["tilde_noclaim"] for r in rs), reverse=True))
report("all split boards", rows)
report("floor.yml@main boards", [r for r in rows if r["fleet"]])
big = sorted(rows, key=lambda r: -r["items"])[:12]
report("twelve largest boards", big)
```

```
import sys, re, random
from pathlib import Path
sys.path.insert(0, "/Users/mike/worktrees/fable/atelier-160-1230-2240/atelier/tools")
import board
PETS = Path("/Users/mike/.pets")
SUBOPEN = re.compile(r"^\s+[-*]\s+(\[[ ~]\]|⏳)")
def floats(repo):
    wf = repo / ".github" / "workflows"
    return wf.is_dir() and any("atelier/.github/workflows/floor.yml@main" in f.read_text(errors="ignore") for f in wf.glob("*.yml"))
cands = []; xbytes = 0; xn = 0; slash = dash = 0
for repo in sorted(PETS.iterdir()):
    b = repo / "docs" / "roadmap"
    if not b.is_dir() or not floats(repo): continue
    for f in sorted(b.glob("*/*.md")):
        if f.name == "README.md": continue
        t = f.read_text(encoding="utf-8", errors="replace")
        if re.search(r"^- \[/\]", t, re.M): slash += 1
        if re.search(r"^- \[-\]", t, re.M): dash += 1
        st = board.item_state(t)
        if st is None: continue
        if st.marker == "[x]":
            xbytes += len(t.encode()); xn += 1
            subs = [l.strip() for l in t.splitlines() if SUBOPEN.match(l)]
            if subs: cands.append(subs)
print(f"[x] items: {xn}; total bytes: {xbytes/1e6:.2f} MB; ~tokens at 4 bytes/token: {xbytes/4/1e6:.2f} M")  # secretscan:allow:assigned-secret: a print label (bytes per token), no secret
print(f"state lines already using [/]: {slash}; [-]: {dash}")
random.seed(1230)
pick = random.sample(cands, 12)
for i, subs in enumerate(pick, 1):
    print(f"--- sample {i}: {len(subs)} open sub-line(s); first: {subs[0][:110]}")
```

#### Act 1 written
- 2026-11-22T22:57Z appended the verdict below a `---` divider in the brief (file now 458 lines);
  Status line updated to RUN / act 1 / PASS-WITH-FINDINGS 0 MAJOR · 3 MODERATE · 3 minor · 2 note.
  `awk 'length > 100'` on the brief: every over-width line is in the brief-writer's own text
  (lines 43-190: paths and an allow-marker), none in the verdict.
- Findings: BT1 MODERATE (sub-line sample does not reproduce: 9/12 real work vs design's 3/16;
  94 fleet `[x]` with open bodies stay ✅), BT2 MODERATE (`(claimed …)` fragment: 0/44 in
  board.py's paragraph, atelier's own 6 claims carry none; step 5 would red live claims), BT3
  MODERATE (readers/mirrors census short: cclive, ccopen, archivecut, two skills' prompts,
  RECORD.md/tools README gate sets, warn channel unbuilt), BT4 minor (step 6 names a retired grace),
  BT5 minor (decisions/README.md:50 stale), BT6 minor (census method unrecorded; direction only),
  BT7 note (public-index surface of `moved to`/`(waiting: <repo>)`, posture C), BT8 note (word
  grammar under-specified).
- Scratch files (census.py, sample.py, claimdbg.py, atclaims.py, s1-s5.json with transcript
  excerpts, test_board.out) deleted after the scanners ran; scripts are reproduced above.

#### Orchestrator spawn prompt, verbatim (rule 4: what the orchestrator told the reviewer)
```
You are the cold REVIEWER for one rule-4 design cold pass in the atelier repo (PUBLIC repo).

WHO YOU ARE
- Item: atelier board `160/1230` (Rule-4 cold pass: the two-tier board states design).
- Review worktree (absolute; use `git -C "<path>"` and absolute paths, never `cd`; double-quote
  every path in every shell command, since paths may hold spaces):
  "/Users/mike/worktrees/fable/atelier-160-1230-2240/atelier"
- Brief: "/Users/mike/worktrees/fable/atelier-160-1230-2240/atelier/docs/reviews/2026-11-09-0238-board-states-design-cold.md"
- Read the brief in full first and follow it, plus `docs/method/REVIEW.md` (in the worktree) for
  the verdict shape. The brief's `cd tools && ...` and `cd ..` lines: run them as `python3 -m
  unittest test_board` with the tools directory as an absolute `-s`/path argument, or a subshell
  `( cd "<worktree>/tools" && nice -n 10 python3 -m unittest test_board )`; that is equivalent.

PROVENANCE (state it in your verdict)
- You are Fable 5.1, the principal-named review tier, checked at selection.
- You were spawned by headless per-pass orchestrator session fce21971 (Opus 5.5), itself started
  by drain session eca14b23 (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold the
  context partition, form no finding and write no severity. Neither wrote the brief or any of the
  delta.
- Barred sessions named by the brief: 9bb1b984, 74f2b8cd, and 722ac2e2 with everything it
  started. You were not started or instructed by any of them.
- You run under Mike's (the principal's) weekly drain order of 2026-11-23, verbatim: "Start a
  fable drain or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat".
  That is the explicit Fable approval the brief says this pass waits for.

THE PARTITION
The brief's `.deferred.md` sibling was removed from the worktree on purpose (it shows as a deleted
file in `git status`; that is expected and is not yours to restore). Do not look for it in git
history, `git show`/`git cat-file` of any ref, other checkouts or worktrees, scratchpads, /tmp, or
`~/.claude`. Honour every other rule-2 bar in the brief's "Deferred reading" section. The
orchestrator will hand you the sibling's path after act 1 is committed.

LOAD (the laptop is shared with several running passes on 16 GB; Mike's instruction is to keep it
from crashing)
Check `uptime` first. Run any test suite or heavy command under `nice -n 10`, one at a time,
single process (no xdist, `-n auto` or parallel runners), foreground with a long timeout. Prefer
the targeted tests a finding actually needs over the whole suite. Use the census and
transcript-search re-runs the brief asks for, but one at a time.

LIVE SYSTEMS
Read-only reads of live systems are allowed as the review needs them (Mike, 2026-11-09, verbatim:
"reads of live systems is fine as needed, Reviews that need writes should be de-priortised"). A
read means nothing on the target changes; if a verb's effect is unsure, treat it as a write. NO
live writes of any kind: no push, no write to GitHub, no network service changed. A check that
would need a write is marked NOT RUN with the reason. Allowlist fields before printing, because
provider reads can carry credentials; never dump a user, key or certificate object raw. Never
print a secret or personal data. Leave no captures in scratch: probes use scratch copies and
synthetic fixtures under your scratchpad, deleted when you finish. Child repos are read-only and
reported by count only, never by name or path. Transcripts are private: quote only what the design
already quotes. Use `/usr/bin/python3` for your own scripts (macOS has no `timeout`); for the
repo's tools use `python3 tools/<x>.py` / `instruments/<x>` from the worktree, never an installed
tool by bare name from PATH. No GUI apps.

WHAT YOU MAY WRITE
1. The brief file above, and only it, inside the repo: act 1 appended below a `---` divider;
   update its **Status:** line (never "fold-in owed"). Keep the file's column width (prose wrapped
   at <= 100 columns), absolute ISO 8601 dates from `date -u` only, NZ English. This repo is
   PUBLIC: no secret, email address, private repo name or path, session NAME, or estate fact; refer
   to orchestrators by session id only. Before finishing each act, run the repo's own scanners over
   the brief from the worktree root, e.g. `python3 tools/leakscan.py --root "<worktree>" "<brief>"`
   and any datescan/spellscan/wrapscan equivalents under `tools/` (check `--help`), and fix your
   own text so the commit gate passes; a verbatim quote that trips a gate gets an allow marker,
   never an edit to the quote.
2. Your REVIEW LOG at "/Users/mike/.claude/fable-drain/notes/atelier-160-1230-2240.md": the one
   file outside the brief you may write. Commands, files and evidence only. As you work, append:
   each step you took (the command run, or the file and line range read) and what that showed;
   each candidate finding with that evidence and the rule or requirement it breaks; and each item
   you checked and found sound, with that evidence. Enough detail that someone else could repeat
   the steps. It is the audit trail of the review, and it is what you read first if you are
   interrupted and resumed. The verdict itself goes only in the brief. No secrets or live captures
   in it. Write your act 1 entries before the sibling is released.

WHAT YOU MUST NOT DO
No commit, no push, no git writes of any kind (no add, stash, checkout, reset). Edit no other repo
file.

HOW TO FINISH
- Act 1: per the brief's Phase 1. When act 1 is fully written in the brief, end your reply with:
  the overall verdict line, the tally by severity, the brief path, and the literal words "ACT 1
  SAVED". Then stop and wait; the orchestrator commits act 1 and then sends you the sibling's held
  path.
- Act 2 (only after you receive that message): read that one file, the barred records and the
  delta commit's body as the brief's Phase 2 allows, then append `### Reconcile` beneath your
  verdict with per-finding notes, any finding formed at reconcile marked as such, and the overall
  line restated. Never revise act-1 text. Do NOT fold the sibling into the brief or delete
  anything: the orchestrator does the fold. End with the restated verdict, tally, and "ACT 2
  SAVED".
```
(Reproduced from the reviewer's context; line-wrapped at 100 columns, words unchanged.)

#### Scanners over the brief (act 1)
- leakscan --root . <brief>: clean, exit 0 (459 lines).
- datescan: 1 finding at :370 "this week" (my text) -> replaced with "on 2026-11-22 UTC"; re-run
  clean.
- spellscan, wrapscan: the file is excluded by .spellscanignore / .wrapscanignore (scanned
  nothing); `awk 'length > 100'` shows no verdict line over 100 columns.
- reviewscan: in scope as a brief; "1 review brief(s) keep deferred material out of the brief", ok.
- pathscan: 3 findings, all in the brief-writer's lines 171 and 173 (docs/ROADMAP-DONE.md and
  docs/SESSIONS.md, named as rule-2 barred conventions and absent in this repo; the sibling
  .deferred.md, absent only by the partition). Not my text; left for the orchestrator's fold (the
  fold prompt fixes the sibling link). Flagged in the act-1 hand-back.
- `git status --short` after writing: only ` M <brief>` and the partition's ` D` sibling.

#### Act 2
- Release message received from orchestrator fce21971: act 1 committed as 1235389b, unrevised;
  sibling path given (user-level held folder). Read the sibling whole: 15 questions, 2 facts, as
  the brief said. Read `git log -1 --format=%B` for e36cedcb and 16ee3f09 (author's accounts).
  Read 310/160 whole, 310/060 whole, 160/1230 whole (now unbarred).
- Author's account vs delta: both bodies restate the design; nothing in them contradicts the text or
  adds a claim the design does not make. 310/160's DRAFTED/REVISED notes and his three answers match
  the design's "Decided by him" table. 310/060's options list confirms the design's "option 1" =
  renderer from prose, "option 2" = disposition field (closes my NOT RUN line).
- Sibling facts: brief-writer's re-runs (board --check exit 0, test_board exit 0) match mine; it
  confirmed regex names only, tested none (BT3 is what testing them found).
- Sibling Q3 (local checkout behind main reds a new box): not in act 1; forms BT9 note at reconcile.
  Q10 ("mixed" departure argued, not asked): not in act 1; forms BT10 minor at reconcile.
  Q5 (index width): board.py WRAP_COLS 85, TITLE_MIN 24, _fit_title squeezes the title to the room
  the prefix leaves (lines 233-234, 496-500): fits by construction, no finding.
- Appended `### Reconcile` beneath the verdict (brief now 532 lines): author's account, sibling
  facts, per-finding notes BT1-BT8 against Q1-Q15, Q4/Q5/Q6/Q8/Q15 discharged with grounds, BT9
  note and BT10 minor formed at reconcile and marked so. Overall restated: PASS-WITH-FINDINGS,
  0 MAJOR · 3 MODERATE · 4 minor · 3 note. RECORD.md § The record is public (line 527) read for
  BT7's grounds.
- Width check in characters (python, tables excluded): act-2 line re-wrapped (BT9, no words
  changed). Three ACT-1 prose lines run 101-114 characters (lines 250, 256, 371 at this point; the
  BT2 paragraph and two provenance bullets); act 1 is committed unrevised, so left for the
  orchestrator's form-only fix at the fold. wrapscan ignores this path, so no gate reds on them.
- Scanners after act 2: leakscan clean; datescan clean (532 lines); reviewscan ok. pathscan's 3
  brief-writer findings (lines 171, 173) unchanged, not mine.
- Status line updated: acts 1 and 2 written; tally 0 · 3 · 4 · 3; "the fold is the orchestrator's".
- Scratch: empty of my files. No git command other than reads was run in either act.
