# Cold pass — the two-tier board states design

**Pass type:** design cold pass, per `docs/method/REVIEW.md` rule 4 and § *Review the design, not
only the build*. A file format every repo's board is read through is doctrine by function (rule 3).
Nothing is built, and that is no reason to shrink the verdict.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** RUN 2026-11-22 UTC on Fable 5.1 — act 1 written: PASS-WITH-FINDINGS, 0 MAJOR ·
3 MODERATE · 3 minor · 2 note; act 2 (reconcile against the sibling) pending. Brief written
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
