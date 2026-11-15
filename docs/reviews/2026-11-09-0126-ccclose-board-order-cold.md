# Cold pass — `ccclose` lists board ids in number order

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** VERDICT 2026-11-15 UTC, both acts written under the principal's weekly Fable drain
order: PASS-WITH-FINDINGS (0 MAJOR, 0 MODERATE, 1 minor, 1 note), unchanged at reconcile. The
sibling and the review log are folded below the verdict; each finding awaits the principal's
decision.
**Sizing:** **small** — one commit, 16 lines. The pointer says it is small enough to take with
`160/1010`. Separate briefs, because the deltas are separate commits.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1020-rule-4-cold-pass-queued-ccclose-board-order.md`.
**Why it earns a review:** The identifiers block is pasted into records as fact, and its board lists
are read as a catalogue of what a session touched. Worst failure is small: a wrong or unstable
order, or a claim of parity with `board.py` that does not hold.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `deeac927`,
  2026-11-03, which wrote it inline (per the queue pointer). The author queued this pass and does
  not take it.
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
  that passes rule 4's criterion. **Barred from reviewing:** session `deeac927` and everything it
  started; session `84e3aa7f` (this brief-writer); session `74f2b8cd`. Whoever takes the pass states
  the spawn in the verdict (V7).
- **The principal's approval:** none yet for the pass. His request above covers this brief only. The
  pass waits for his explicit permission for Fable work.

⚠️ **Brief-writer's exposure, disclosed** (rule-2 and author-account material met before writing):

- its dispatch text; `skills/review-brief/SKILL.md` whole; `docs/method/REVIEW.md` whole; the
  house-form brief `docs/reviews/2026-11-06-2027-secretscan-exempt-private-keys-cold.md` through
  line 728, including its verdict (read for shape, another surface); the top of one sibling brief;
- the queue pointer whole; the intent record whole;
- the delta body-free through `tools/coldsweep.py --commit 5f7c2b0c` (subject, stat, diff, never the
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

No intent record for this delta carries a ruling of the principal's. Judge it against what the delta
claims: each digit run compares as a number, as `board.py` does since `010/200`.

## What the work is

One commit on `main`, `5f7c2b0c` (first confirm your tree has it: `git merge-base --is-ancestor
5f7c2b0c HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit 5f7c2b0c \
  --path instruments/ccclose \
  --path instruments/ccclose.test.js \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline 5f7c2b0c..HEAD -- instruments/ccclose instruments/ccclose.test.js CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- The board lists sort with `boardOrder`, numeric collation, so `160/986` comes before `160/1000`.
- This matches `board.py`'s own sort since `010/200`.

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** The rest of `ccclose`, including `160/1010`'s loop reading.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. No new input and no new output beyond the order of ids.
Discharge in one line with grounds if you confirm that, or say what you found.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line below once on 2026-11-09 UTC, from the worktree
root, in the foreground or niced; its results are held in the sibling. Read exit codes explicitly.
Use the `python3` on `PATH` (3.14 on this machine): `/usr/bin/python3` (3.9) cannot import
`tools/test_floor.py`.

- `node --test instruments/ccclose.test.js`

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
`docs/reviews/2026-11-09-0126-ccclose-board-order-cold.deferred.md`, every delta commit's message
body, and the intent record
`docs/roadmap/210-instruments-open-features/370-ccclose-sorts-board-ids-as-text.md` beyond its first
line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1020-rule-4-cold-pass-queued-ccclose-board-order.md \
  --also-exclude docs/roadmap/210-instruments-open-features/370-ccclose-sorts-board-ids-as-text.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`5f7c2b0c`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `CO`: `CO1`, `CO2`, …) and severities (MAJOR /
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

## Verdict — act 1 (cold pass, 2026-11-15 UTC)

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection.
- **Spawn:** a headless per-pass orchestrator (Opus 5.5), itself started by drain session
  `21a271a5` (Opus 5.5). Both are rule-4 off-tier orchestrators: they held the context partition,
  formed no finding and wrote no severity. Neither wrote this brief or the delta. The orchestrator's
  direction was process only: the worktree and brief paths, the finding prefix, the load rules, the
  shape of the deliverable, and that act 2 waits for its release message. It carried no question
  about the delta and no pointer to where risk lives.
- **Barred sessions:** `deeac927` (author) and everything it started; `84e3aa7f` (brief-writer);
  `74f2b8cd` (its coordinator). This reviewer was started and instructed by none of them, and had no
  contact with any of them.
- **Permission:** the principal's weekly Fable drain order, `/fable-drain` invoked 2026-11-16 06:53
  NZDT (2026-11-15 UTC).
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1020-2131/atelier`, HEAD `529c886e`,
  read-only to this pass except this file. `git merge-base --is-ancestor 5f7c2b0c HEAD` exited 0.
- **Partition:** the sibling `.deferred.md` was removed from the worktree by the orchestrator before
  the pass began (`git status` shows it deleted); it was not sought in git history or anywhere else.
- **What was read:** this brief whole; `docs/method/REVIEW.md` whole; the delta body-free through
  `tools/coldsweep.py --commit 5f7c2b0c --path …` (the three delta paths; three board-store files
  left out, no rule-2 file touched); `instruments/ccclose` at HEAD lines 1490–1600 and
  1870–1930;
  `instruments/ccclose.test.js` header, the board assertions and the new test; `tools/board.py`
  740–790; `tools/test_board.py` 80–100 and 895–915; `CHANGELOG.md` 1580–1612;
  `instruments/README.md` lines naming ccclose; `instruments/ccclose.design.md` 384–400 and
  494–512;
  `instruments/man/ccclose.1` 462–492; `docs/method/RECORD.md` 112–120; `--help` of `coldsweep`,
  `datescan`, `spellscan`, `wrapscan`. Not opened: the session log, `docs/sessions/`,
  `docs/ROADMAP-DONE.md`, any prior verdict, the queue pointer, the intent record, any commit body.
- **Sweep exposure, disclosed:** two `coldsweep` sweeps (both with the brief's two `--also-exclude`
  paths; 571 files excluded) printed one line of `docs/ROADMAP.md` (this pass's pointer, title only)
  and two lines of the `160/987` pointer (the `010/200` pass, not this delta). Neither carried an
  account of this delta. No `--include-barred` run.
- **Harness note:** the harness loaded user-level and repo instruction files and a memory index
  before the brief; nothing in them concerns this delta.

### Load-bearing assumptions (lens 1), named before the code was read

- **A1** — numeric collation of the two digit runs orders every board id as `board.py` does.
  **Confirmed on ids**; the tie case is CO2. Probe: a scratch comparator run over 13 ids including
  `160/986`, `160/1000`, `1000/010` and leading-zero variants.
- **A2** — every member of a sorted set is a `\d+/\d+` id. **Partly false, harmless:**
  `reviewElsewhere` holds item-store paths (`f.path`) and is sorted with `boardOrder` too; the
  order is deterministic and numeric on the path's digits.
- **A3** — the Node running ccclose has ICU, so `numeric: true` is honoured. **Confirmed here:**
  v24.18.0, ICU 78.3, `Intl.Collator.supportedLocalesOf(['en'])` → 1. Without ICU the comparator
  degrades to text order and the new test fails loudly.
- **A4** — the comparator is a consistent total order. **Confirmed:** 0 inconsistent pairs or
  triples over all 13² and 13³ combinations of the probe ids.
- **A5** — the new test fails if the wiring is reverted. **Falsified** by mutation (CO1).
- **A6** — "as `board.py` does since `010/200`" holds at HEAD. **Holds in outcome, mechanism
  differs:** `board_order` is `(0, int(leading), name)`; see CO2.
- **A7** — no other id list in ccclose or its docs sorts as text. **Confirmed:** every other
  `.sort(` in ccclose orders file names, statuses or PR numbers; README, design doc, man page and
  RECORD.md describe the lists and state no id order.
- **A8** — before the delta `.sort()` put `160/1000` before `160/986`. **Confirmed:**
  `['160/1000','160/986'].sort()` → `160/1000 160/986`.

Right problem, right altitude: a one-line comparator at the one point the lists are built, exported
for the test. The brief's account of the work matches the diff; its sizing (one commit, 16 lines)
matches the stat (+16/−2).

### Per-lens answers

1. **Approach & assumptions.** Sound. `localeCompare` with `numeric: true` is the idiomatic Node
   way to collate digit runs, deterministic given ICU, and the ids it meets are regex-captured ASCII
   digits. The one design choice worth naming: it relies on ICU being present. On a Node built
   without Intl the comparator silently becomes a text sort, and the new test is what would catch
   it. Acceptable; noted, not a finding.
2. **Correctness & quality.** The change does what it claims: the CHANGELOG example reproduces
   (A8) and the fix reproduces (A1). The one overclaim is a wording one: "each digit run compares as
   a number, as `board.py` does" likens two different mechanisms whose outcomes agree on real ids
   (CO2, note). `reviewElsewhere` paths are now locale-collated too; harmless and unmentioned.
3. **Completeness / harvest.** V3: no mirror site states the order (README, design doc, man page,
   RECORD.md each describe the lists, none their order), so nothing was owed a sweep. V4: one home,
   the comparator, with a code comment and a CHANGELOG entry; no second source. V5: no
   contradiction between the code, the comment, the test and the CHANGELOG. **Tests that stay green
   on a broken change:** yes, one — the wiring (CO1, minor).
4. **Security & privacy (V6).** Discharged: the delta adds no input and no output beyond the order
   of ids already printed; the comparator runs over regex-captured digits and item-store paths from
   `git log`, with no interpretation of either. `/security-review` reads a pending diff: the delta
   is landed and the worktree is not clean (the deleted sibling), so it could not be aimed at the
   work and was not run.

### Standing checklist

- **V1** — one claim slightly stronger than its evidence (CO2). Everything else states what the
  probes show.
- **V2** — the brief's one re-run line re-run:
  `nice -n 10 node --test instruments/ccclose.test.js` → exit 0, 111 tests, 111 pass, 0 fail,
  113.5 s. Reproduces.
- **V3** — swept; no mirror site states the order (lens 3).
- **V4** — one home (lens 3).
- **V5** — no contradiction; the cross-reference `010/200` reaches `board.py`'s `board_order`,
  which does hold the rule it is cited for (leading number as a number).
- **V6** — discharged with grounds (lens 4).
- **V7** — provenance above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `5f7c2b0c` ccclose: list board ids in number order | yes, `coldsweep --commit` | CO1, CO2 |

Commits on the delta paths since (`5f7c2b0c..HEAD -- instruments/ccclose`): `457f374d`,
`4e3b3984`, `1bc89816`, `6890e9db`, `50547442`; none touches `boardOrder` or `sorted`. The delta
stands at HEAD as landed.

### Findings

**CO1 — minor — the wiring of `boardOrder` into the lists is untested; the suite stays green with
the old text sort.** The new test sorts a literal array with the exported comparator, so it pins
`boardOrder`'s semantics and nothing else. Every test that reads the rendered or JSON board lists
uses same-width ids (`010/010` … `010/060`), where text and numeric order coincide. Probe: a scratch
copy of `instruments/` with line 1558 reverted to `const sorted = (x) => [...x].sort();` and
`node --test --test-name-pattern="board"` → 6 tests, 6 pass, including the `210/370` test. The
lens 3 question in this brief, "tests that would stay green on a broken change", is answered yes
for the one line that makes the fix real. Judged against lens 3 and `REVIEW.md` § *What a review
actually checks* (test code reviewed on the same footing as code).
*Counsel:* one end-to-end `--identifiers` case whose fixture board carries a three- and a four-digit
item in one section (say `010/986` and `010/1000`), asserting the rendered `created:` order; the
comparator test can stay as the unit pin.

**CO2 — note — "each digit run compares as a number, as `board.py` does since `010/200`" overstates
the parity.** `board.py`'s `board_order` compares the *leading* number as a number and the rest of
the name as text; ccclose's comparator compares *every* digit run numerically. On the board's
two-run ids the two orders agree, so the claim holds in outcome. One measurable difference: on
leading-zero variants of one number (`160/1` vs `160/01`) the comparator returns 0 and leaves the
pair in input order, where `board.py` breaks the tie by name — a case `board.py` itself reports as a
number collision, so it never reaches a clean board. Judged against V1. No change needed; if the
wording is touched, "lands a four-digit item after a three-digit one, as `board.py` does" is what
the probes support.
*Counsel:* none beyond the optional reword.

### Overall

**PASS-WITH-FINDINGS** — 0 MAJOR, 0 MODERATE, 1 minor (CO1), 1 note (CO2).

### Re-run ledger

- `nice -n 10 node --test instruments/ccclose.test.js` — worktree, foreground, load 8.33 at
  start → exit 0; 111/111 pass; 113.5 s.
- `python3 tools/coldsweep.py --root . --commit 5f7c2b0c` with the three `--path` arguments —
  worktree → exit 0; subject, stat and diff printed, body not printed.
- `git merge-base --is-ancestor 5f7c2b0c HEAD` — worktree → exit 0.
- Scratch comparator probe (13 ids; consistency; the old sort) → as in the assumptions list.
- Scratch mutation (wiring reverted) with `--test-name-pattern="board"` → exit 0; 6/6 pass;
  see CO1.

### Follow-up checklist

- [ ] CO1: the principal's decision; if taken up, add the end-to-end order test (counsel above).
- [ ] CO2: the principal's decision; no change needed unless the wording is revisited.
- [ ] Act 2: open the sibling on the orchestrator's release, reconcile, restate the overall line.
- [ ] Scratch (`probe_order.js`, `suite.txt`, `mut/`, `mut_suite.txt`) deleted by the reviewer at
      the end of act 1.

### Reconcile

Act 2, 2026-11-15 UTC, after act 1 landed on `main` as `fcce3da1`, unrevised. The orchestrator's
release message named one file, the held sibling, and opened the barred records; it carried no
question about the delta and asked for no revision. Opened at this step: the sibling (whole), the
queue pointer `160/1020`, the intent record `210/370`, the delta commit's message body, and the
`docs/SESSIONS.md` index line of the 2026-11-03 queue run (the session record itself was not
needed). No act-1 text above was changed.

**Against the sibling's three questions.** Each was already answered in act 1, formed before the
sibling was opened:

1. *Leading zeros and ties against `board.py`'s key.* Answered by A1, A6 and CO2: on the board's
   ids the two orders agree; on leading-zero variants the comparator ties (returns 0) where
   `board.py` breaks by name, a case `board.py` reports as a number collision. The sibling's
   example `010/200` against `10/200` is that tie.
2. *Is `sorted` the only place the lists are ordered; any text sort of ids in ccclose or its
   siblings?* Answered by A7 for ccclose. Extended at reconcile for the siblings: every `.sort(` in
   `cclive`, `ccrepo`, `cctranscript` and `ccarchive` orders directory entries, ages, months, days,
   object keys or paths, and none of those instruments parses a `\d+/\d+` board id. No finding.
3. *Does anything pin the order through the printed block?* No; that is CO1.

**Against the brief-writer's run.** It saw 105 tests pass in 284 s under load on 2026-11-09; this
pass saw 111 pass in 113.5 s. The six added tests arrived with the later commits on the file
(`457f374d`, `4e3b3984`, `1bc89816`, `50547442`); none bears on the sort. Consistent.

**Against the author's account.** The commit body, the intent record and the pointer agree with
the diff and with act 1: display only, nothing miscounted (consistent with the lens 4 discharge);
"the order board.py has used since 010/200" (the wording CO2 notes); "pinned in
`instruments/ccclose.test.js`" (the pin is the comparator alone, which is CO1). The intent record's
chosen shape, "every digit run compares as a number", confirms the comparator's mechanism was
deliberate, so CO2 stays a note on the parity wording only, not on the design. The pointer's spawn
and permission text matches the provenance stated in act 1.

**Per finding.** CO1 — stands, minor; nothing in the author's account addresses the wiring test.
CO2 — stands, note; the same phrase appears in the commit body and CHANGELOG, so a reword, if the
principal wants one, has two sites. No finding was formed at reconcile.

**Overall, restated: PASS-WITH-FINDINGS** — 0 MAJOR, 0 MODERATE, 1 minor (CO1), 1 note (CO2).
Every finding is the principal's to decide; nothing was applied.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-15)

*Released to the reviewer only after its act-1 findings were committed (`fcce3da1` on `main`);
folded here verbatim (headings demoted two levels) and the sibling file removed, per the brief. The
orchestrator (a headless Opus 5.5 session started by drain session `21a271a5`, itself Opus 5.5)
held the partition, formed no finding and wrote no severity.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-ccclose-board-order-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

#### The brief-writer's own questions

1. Does `localeCompare` with `numeric: true` agree with `board.py`'s key on leading zeros (`010/200`
against `10/200`) and on ties? Run both on the same list.
2. Is `sorted` the only place the board lists are ordered? Look for another text sort of ids in
`ccclose` and its siblings.
3. The new test calls the comparator directly. Does anything pin the order through the printed
block?

#### What the brief-writer ran, and what it got

- `ccclose`: Node 24: 105 tests, 105 pass, 0 fail, 284 s under load.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*The reviewer's work log, kept outside the worktree while the pass ran and read by no other session
until act 2 was saved; appended here verbatim at the fold (headings demoted two levels, form only)
and the working file deleted.*

### Work log — atelier 160/1020, ccclose board-order cold pass (prefix CO)

Reviewer: Fable 5.1 (claude-fable-5-1), tier checked at selection. Spawned by a headless per-pass
orchestrator (Opus 5.5) started by drain session 21a271a5 (Opus 5.5); both rule-4 off-tier
orchestrators holding the partition, forming no finding. Permission: the principal's weekly Fable
drain order (`/fable-drain`, 2026-11-16 06:53 NZDT). Not started or instructed by deeac927,
84e3aa7f or 74f2b8cd.

Worktree: /Users/mike/worktrees/fable/atelier-160-1020-2131/atelier (HEAD 529c886e; the brief's
`.deferred.md` sibling removed from the worktree by the orchestrator; not sought elsewhere).
Run day: 2026-11-15 UTC (date -u at start: Sun Nov 15 21:33:41 UTC 2026). Load at start: 7.52.

#### Act 1 — reads and commands

- READ docs/reviews/2026-11-09-0126-ccclose-board-order-cold.md lines 1–188 (the brief, whole).
- READ docs/method/REVIEW.md (whole, via cat; 46 KB) for rules 1–4 and V1–V7.
- RAN `git -C <wt> merge-base --is-ancestor 5f7c2b0c HEAD` → exit 0 (delta is in HEAD).
- RAN `git -C <wt> status --short` → only ` D docs/reviews/...deferred.md` (the partition).
- `which python3` → /Library/Frameworks/Python.framework/Versions/3.14/bin/python3 (3.14.6), as
  the brief requires for repo tools.
- RAN `git -C <wt> log --oneline 5f7c2b0c..HEAD -- instruments/ccclose instruments/ccclose.test.js CHANGELOG.md`
  → exit 0, ~70 subjects (mostly CHANGELOG); the per-path list for instruments/ccclose is read next.
- RAN `python3 <wt>/tools/coldsweep.py --root <wt> --commit 5f7c2b0c --path instruments/ccclose
  --path instruments/ccclose.test.js --path CHANGELOG.md` → exit 0; subject "ccclose: list board ids
  in number order (210/370)", 3 files, +16/−2; body not printed; 3 board-store files left out
  (ROADMAP.md, the 1020 pointer, the 370 intent record); 0 rule-2 files touched.
- Delta content: `const boardOrder = (a, b) => a.localeCompare(b, 'en', { numeric: true })`;
  `sorted = (x) => [...x].sort(boardOrder)` in boardReduce; boardOrder exported; one test sorting a
  five-element literal array with cc.boardOrder; a CHANGELOG "Fixed" entry.

#### Load-bearing assumptions named before further reading (lens 1)
- A1 Numeric collation of two digit runs gives the same order as board.py's sort for every id shape
  the board holds (NNN/NNN, NNN/NNNN).
- A2 Every member of the sets reaching `sorted()` is a plain `\d+/\d+` id, so letter collation never
  decides an order.
- A3 The Node that runs ccclose has ICU (`Intl`) so `numeric: true` is honoured; without ICU the
  comparator degrades to text order silently.
- A4 The comparator is a consistent total order (sort is deterministic across runs and platforms).
- A5 The new test would fail if the wiring (`sorted` using boardOrder) were reverted. (Suspect: it
  tests the exported comparator, not the rendered list.)
- A6 The CHANGELOG's "as board.py does since 010/200" is true of board.py at HEAD: same per-run
  numeric comparison, same result on the real ids.
- A7 No other id list in ccclose (or its docs/man page) still sorts as text (V3/V4).
- A8 Before the delta, `.sort()` did put 160/1000 before 160/986 (the CHANGELOG's claim).
- RAN `git log --oneline 5f7c2b0c..HEAD -- instruments/ccclose` → 5 commits (50547442, 6890e9db,
  1bc89816, 4e3b3984, 457f374d); same minus 6890e9db for the test file. None touches the sort.
- RAN `grep -n "\.sort(\|localeCompare\|boardOrder" instruments/ccclose` → boardOrder at 1505, used
  at 1558 (sorted), exported at 2108; other sorts are agent file names (1387, 1646), status order
  (1405), scratch entries by name (1430), numbered items by number (1797), marks (320): none a
  board-id list.
- RAN `node --version; node -p process.versions.icu …` → v24.18.0, ICU 78.3, Intl present, 'en'
  supported. A3 confirmed on this machine.
- READ instruments/ccclose 1490–1600 at HEAD (boardLog, boardOrder, boardReduce, boardChanges).
  reviewElsewhere holds PATHS (f.path), not ids, and is sorted with boardOrder too (A2 partly
  false: harmless, see verdict). unconfirmed/viaSquash/claimedMoved are filters of sorted lists.
- READ tools/board.py 740–790 (board_order: `(0, int(leading), name)`; unnumbered last).
- READ tools/test_board.py 80–100, 895–915 (010/200 tests: 130 < 990 < 1000; both planes agree).
- READ CHANGELOG.md 1580–1612 (the 210/370 entry; the 010/200 entry beneath).
- RAN coldsweep for `010/200` and for `210/370|boardOrder|number order|numeric collation|board
  order` with the two --also-exclude paths → 10 and 11 hits; 571 files excluded; hits only in
  CHANGELOG, the code, the test, board.py, test_board.py, ROADMAP.md's pointer line, and
  160/987 (the 010/200 pointer).
- RAN probe `<scratch>/probe_order.js` (comparator on 13 ids incl. leading zeros and a
  four-digit section): numeric order as expected; 0 inconsistent pairs/triples over all
  pairs/triples (A4 confirmed); `160/1` vs `160/01` → 0 (tie, where board.py breaks by name);
  old `.sort()` gives 160/1000 before 160/986 (A8 confirmed).
- grep instruments/README.md for ccclose: a table row and § "ccclose — the close-out, read fresh"
  (392–423); no statement of id order. instruments/ccclose.design.md: grep sort|order|board; no
  statement of the identifiers' id order (checked lines listed below).
- RAN (re-run obligation) `uptime` (load 8.33) then `nice -n 10 node --test
  <wt>/instruments/ccclose.test.js` → exit 0; tests 111, pass 111, fail 0; 113.5 s. Output in
  scratch `suite.txt` (deleted at finish).
- READ instruments/ccclose 1870–1930 (renderIdentifiers): the Board block joins `b.review` then
  `b.reviewElsewhere`; unconfirmed/viaSquash parts are filters of the sorted lists; no re-sort.
- READ instruments/ccclose.test.js 10–40 (require('./ccclose'), SCRIPT from __dirname) and the idRun
  definition (1088); grep for board assertions: every rendered-list test uses same-width ids
  (010/0x0), so text and numeric order coincide there.
- READ instruments/ccclose.design.md 384–400 and 494–512 (board reduce; no statement of id order).
- MUTATION PROBE (A5): copied instruments/ (1.7 MB) to scratch `mut/`, replaced
  `[...x].sort(boardOrder)` with `[...x].sort()` (one occurrence), ran
  `nice -n 10 node --test --test-name-pattern="board" <scratch>/mut/ccclose.test.js` → exit 0;
  6 tests, 6 pass, 0 fail, including "board ids sort as numbers, so a four-digit pointer follows
  999 (210/370)". A5 FALSIFIED: the test pins the exported comparator, not its use in boardReduce;
  the wiring has no test. → CO1.
- Man page instruments/man/ccclose.1: grep board|sort|order; line 373 is the field order of the
  identifiers block, not id order; Board paragraph read at 462–492 (below).
- READ instruments/man/ccclose.1 462–492 (Board paragraph: describes the lines, names ids "by
  section and item number", states no order within a list). READ docs/method/RECORD.md 112–120
  ("Board: by number, the items…": identification, not order). Neither is a mirror of the rule.
- Checked (not raised): V3 — no mirror site states the id order, so no sweep owed. V4 — one home
  (the comparator), a code comment and a CHANGELOG entry. V5 — code, comment, test and CHANGELOG
  agree; `010/200` reaches board.py's board_order, which holds the cited rule. V6 — no new input
  or output; comparator over regex-captured digits and git-log paths; /security-review not aimable
  (delta landed, worktree dirty with the deleted sibling) → discharged by grounds.
- Checked (not raised): the ICU reliance (A3). Without Intl the comparator degrades to text order;
  the new unit test would fail there, so the failure is loud. Noted in lens 1, no finding.
- Checked (not raised): reviewElsewhere paths are locale-collated now (A2). Deterministic and
  harmless; mentioned in lens 2, no finding.

#### Findings
- CO1 minor — wiring untested. Evidence: mutation run above (6/6 pass with text sort restored);
  every rendered-list test uses same-width ids. Criterion: brief lens 3 "tests that would stay
  green on a broken change"; REVIEW.md scope (test code reviewed as code).
- CO2 note — "each digit run … as board.py does" overstates mechanism parity. Evidence: board_order
  = (0, int(leading), name) vs numeric collation of every run; probe tie `160/1` vs `160/01` → 0
  where board.py breaks by name (a case board.py's number_collisions reports). Criterion: V1.

#### Act 1 close
- WROTE the verdict below a `---` divider in the brief; Status line updated to ACT 1 WRITTEN
  2026-11-15 UTC, PASS-WITH-FINDINGS (0 MAJOR, 0 MODERATE, 1 minor, 1 note), act 2 pending.
- RAN `python3 <wt>/tools/datescan.py --root <wt> <brief>` → clean, exit 0 (1 file, 335 lines).
- RAN spellscan and wrapscan the same way → exit 0 but "scanned nothing": docs/reviews is in
  .spellscanignore and .wrapscanignore. Column rule held by hand: `awk 'length($0) > 100'` over my
  lines → none after rewrapping (the two tables became lists). Lines 10, 37, 162, 174 over 100
  are the brief-writer's verbatim text, left as is.
- Scratch deleted: probe_order.js, suite.txt, mut/, mut_suite.txt (claim.log there is the
  orchestrator's, untouched). `git status --short` → only the brief modified and the sibling's
  deletion. No commit, no push, no gh.
- Verdict: PASS-WITH-FINDINGS — 0 MAJOR, 0 MODERATE, 1 minor (CO1), 1 note (CO2). ACT 1 SAVED.
- Column check redone in characters (awk's length counts bytes; `…`, `—`, `→` are multi-byte):
  `/usr/bin/python3` over the verdict lines → none over 100 characters. Brief is 349 lines.

#### Act 2 — reconcile (released by the orchestrator after act 1 landed as fcce3da1)
- READ the held sibling (whole; 3 questions and one re-run result: 105 tests, 105 pass, 284 s).
- READ the queue pointer 160/1020 (whole), the intent record 210/370 (whole), the delta commit's
  message body (`git log -1 --format=%B 5f7c2b0c`), and the SESSIONS.md index line for the
  2026-11-03 queue run (grep for 210/370; the session record itself not opened: not needed).
- RAN `git log -1 --format='%h %s' fcce3da1` → "reviews 160/1020: act 1 of the ccclose board-order
  cold pass" (act 1 on main, unrevised).
- RAN grep `\.sort(` over instruments/cclive, ccrepo, cctranscript, ccarchive and grep for a
  `\d+/\d+` id regex in them → sorts are of dir entries, ages, months, days, keys and paths; no
  sibling parses board ids. Sibling Q2 extended to siblings: no finding.
- Reconciled: Q1 ↔ A1/A6/CO2; Q2 ↔ A7 (+ siblings); Q3 ↔ CO1. Brief-writer's 105/105 (284 s) vs
  my 111/111 (113.5 s): six tests added by the later commits, none on the sort. Author's account
  (commit body, intent record, pointer) agrees with the diff; "pinned in the test" is the
  comparator only (CO1); "the order board.py has used" is CO2's phrase, also in the commit body.
  No finding formed at reconcile. Overall unchanged: PASS-WITH-FINDINGS (1 minor, 1 note).
- WROTE `### Reconcile` beneath the act-1 verdict; Status line updated to VERDICT 2026-11-15 UTC.
- Gates after act 2: datescan on the brief (result in the next line of this log once read); column
  check in characters over the verdict lines; `git status --short` → the brief modified and the
  sibling's deletion only. No commit, no push, no gh; sibling untouched, fold left to the
  orchestrator. Scratch holds only the orchestrator's claim.log. ACT 2 SAVED.
- datescan after act 2: clean, exit 0 (the exit was read from the tool's own ✓ line; the shell
  pipeline swallowed the status). Column check: no verdict line over 100 characters; brief 391
  lines.
