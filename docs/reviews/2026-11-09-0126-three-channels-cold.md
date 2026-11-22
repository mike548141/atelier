# Cold pass — the principal speaks through three channels (`320/070`)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 2 WRITTEN 2026-11-22 UTC — PASS-WITH-FINDINGS (0 MAJOR, 3 MODERATE, 4 minor), by
a Fable 5.1 reviewer under the principal's drain order of 2026-11-23 NZDT. Act 2 (reconcile
against the sibling) done; the sibling is folded below the verdict by the orchestrator and its
file removed. Findings are the principal's to decide (rule 3).
**Sizing:** **small** — one commit, about 75 lines of doctrine, with measured figures that can be
re-derived from transcripts by count.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/1100-rule-4-cold-pass-queued-three-channels.md`.
**Why it earns a review:** Every future audit of what the principal asked for rests on this, and
later tools (`320/080`) are to be built on it. Worst failure: a negative stated with confidence ("he
never asked for that") because the audit read too few channels, or counted injected text as his.

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
- the delta body-free through `tools/coldsweep.py --commit b12c4b15` (subject, stat, diff, never the
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

The principal's pick of 2026-11-08, as the delta records it in `docs/method/RECORD.md`: *"Adopt both
rules"*. An answer to options offered, not a ruling in his own words.

## What the work is

One commit on `main`, `b12c4b15` (first confirm your tree has it: `git merge-base --is-ancestor
b12c4b15 HEAD` exits 0, or merge `origin/main` into the review branch before starting, because a
tree without the delta has nothing to review). The delta paths are in the command below.

```
python3 tools/coldsweep.py --root . --commit b12c4b15 \
  --path docs/method/RECORD.md \
  --path docs/method/GUARDS.md \
  --path docs/method/README.md \
  --path CHANGELOG.md
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). Any board record the commit touches that is not listed above is barred until phase 2, so always
pass `--path`. Review each delta path at HEAD too. Confirm what has landed since with the line
below, and read anything new the same way. The delta builds on earlier work; read it only as far as
it bears on this delta.

```
git log --oneline b12c4b15..HEAD -- docs/method/RECORD.md docs/method/GUARDS.md docs/method/README.md CHANGELOG.md
```

## What the delta claims (extracted, not evaluated)

- The principal reaches a session by three channels: opening prompt, mid-turn message, question-box
  pick, stored as three different record types.
- A mid-turn instruction counts exactly like an opening one, and one meant to stand is written down
  before the turn ends.
- An audit of what he asked says which channels it read and how it told his typing from injected
  text.
- The measured figures in the new section (24.3% mid-turn, 3,013 against 965; 43.3% of mid-turn
  records human-typed; nineteen of nineteen in one child; 3,020 messages; 1,305 records).
- `cctranscript` read only the first channel (`210/100`).

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope.

**Non-goals:** `320/080` (`quotescan`) and `320/100`, which the delta says it does not do.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Ask
whether this is the right problem, solved at the right altitude. Treat this brief's account of what
the work is as attackable.
2. **Correctness & quality.** Diff the commit; run the probes live. Record each overclaim against
the text that makes it.
3. **Completeness / harvest.** Every surface that states the same thing (V3); one home (V4); no
contradiction (V5); tests that would stay green on a broken change.
4. **Security & privacy** — mandatory. The figures come from the principal's transcripts. If you
re-derive any, read transcripts under `~/.claude/projects/` **read-only and by count**, and quote no
text. No private repo name goes in the verdict: refer to a child by type.

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
`docs/reviews/2026-11-09-0126-three-channels-cold.deferred.md` (now folded below; the file is
removed), every delta commit's message body,
and the intent record
`docs/roadmap/320-child-filed-findings-via-pointing-up/070-proposal-a-transcript-has-three-channels.md`
beyond its first line (the title).

The delta's own text carries the author's account of why; it is the delta, and reading the delta is
never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed/1100-rule-4-cold-pass-queued-three-channels.md \
  --also-exclude docs/roadmap/320-child-filed-findings-via-pointing-up/070-proposal-a-transcript-has-three-channels.md \
  '<pattern>'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Read the acceptance test; reproduce the floor first; work the lenses, your own
assumptions and the re-run list. Append your verdict below a `---` divider in THIS file: provenance
repeated (how you were spawned, your tier, what you read, the UTC day you ran on), per-lens answers,
the standing checklist V1–V7 each answered or discharged with grounds, each load-bearing assumption
damaged or confirmed with its probe, a per-commit ledger (`b12c4b15`: read body-free yes/no,
findings by id), findings with stable IDs (prefix `CN`: `CN1`, `CN2`, …) and severities (MAJOR /
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

## Verdict — act 1 (cold, before the sibling)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (CN1, CN2, CN5) · 3 minor (CN3, CN4, CN6).**
The two rules the section lands are sound and well placed; what misses is the mechanism the
section states for the third channel, the section's own compliance with the rule it imposes on
audits, and the house instrument's third-channel gap, which nothing tracks.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), tier checked at selection; the principal-named
  review tier. Ran on 2026-11-22 UTC (2026-11-23 NZDT), in review worktree
  `/Users/mike/worktrees/fable/atelier-160-1100-2236/atelier`, detached at `b1307b77`.
- **Spawn:** started by headless per-pass orchestrator session `23e95a19` (Opus 5.5), itself
  started by drain session `eca14b23` (Opus 5.5). Both are rule-4 off-tier orchestrators: they hold
  the context partition, form no finding and write no severity. Neither wrote the brief or the
  delta. The reviewer was not started or instructed by `722ac2e2` (or anything it started),
  `84e3aa7f` or `74f2b8cd`, the three the brief bars. No contact from the author or the
  brief-writer during the pass.
- **Orchestrator direction received (process only):** the paths and worktree, the barred set as
  the brief states it plus the sibling removed from the tree, the two files I may write (this
  brief and a review log at `~/.claude/fable-drain/notes/atelier-160-1100-2236.md`), the gates to
  run, the load rules, the act-1/act-2 shape and the release timing. It carried no question
  about the delta, no pointer to where a risk lives and no request about any finding.
- **Approval:** the principal's drain order of 2026-11-23 NZDT, verbatim, *"Start a fable drain
  or whatever it is called now. Target 100% of weekly budget by 11.30am NZT todat"*. It is the
  explicit Fable approval the Status line above waited for.
- **What I read, disclosed:** this brief whole; `REVIEW.md` whole; the delta body-free through
  `coldsweep --commit b12c4b15` with the four `--path`s; the later one-sentence edit to the section
  body-free through `coldsweep --commit e7370f78 --path docs/method/RECORD.md`; the four delta
  files at HEAD around the touched lines; `COMMUNICATION.md` 214–300; `GUARDS.md` 685–735;
  `PERSONAL-DATA.md` 1–80; `CONVENTIONS.md` lines 57–59; `instruments/cctranscript` 30–80 and
  555–625 plus the `searched` lines, its man page 270–320, `instruments/README.md` 350–362;
  `tools/quotescan.py` 1–25; `docs/decisions/2026-11-09-board-states-design.md` 45–60 (a decision
  record, not barred, which carries an account of `210/100`'s effect; it steered no finding);
  `docs/method/census/2026-11-16-1204-apex-autonomy-guards-propagation.md` 365–385; the
  `CHANGELOG.md` entry and its neighbours' headings; first lines (titles) only of board items
  `210/100`, `320/080`, `320/100`, `160/1250` and the open `210` items; `docs/ROADMAP.md` line
  245 as a `coldsweep` hit (this pass's index line, title only). I did **not** open
  `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, any other file in
  `docs/reviews/`, the sibling, the queue pointer, the intent record beyond its title, or any
  commit message body. My harness loaded user-level and repo instruction files and a memory
  index, which hold private context this verdict does not carry. Transcripts under
  `~/.claude/projects/` were read read-only and by count only; no text from them is quoted here.
- **Later edit noted (scope):** `e7370f78` (2026-11-10 UTC, subject `board: queue the cold pass
  on the asking doctrine (160/1250)`) added one sentence to the section ("A pick is an answer and
  not a ruling; that section holds the difference and the marks"). It belongs to `160/1250`'s
  delta by that pointer's title; I read it body-free, formed no finding on it, and note only that
  it agrees with `COMMUNICATION.md` § *Asking for a ruling*.

### Method, in order

1. Acceptance test read; `git merge-base --is-ancestor b12c4b15 HEAD` exit 0. Floor reproduced
   at HEAD on both planes (re-run ledger below).
2. Lens 1: the load-bearing assumptions named from the delta's own text (next section), before
   any probe.
3. Lens 2: the delta read body-free; each cross-reference followed to the rule it reaches at HEAD
   and at the delta commit; the arithmetic of the figures checked; the record-shape claims
   tested against the live transcript store, by count, with two scripts under my scratchpad
   (deleted at the end of the pass); the house instrument's own census of the same shapes read
   as the comparison.
4. Lens 3: `coldsweep` mirror sweep for the section's vocabulary; board titles for an item that
   tracks the instrument's third-channel gap; templates and skills for a stamped copy.
5. Lens 4: privacy of the figures and the prose (no transcript text, children by type, the
   first name within the closed list); `/security-review` discharged with grounds.
6. Standing checklist V1–V7; per-commit ledger; findings; follow-ups. The running log holds
   every command, path and count behind each line.

### Lens 1 — load-bearing assumptions, named then probed

- **A1. There are exactly three channels, and they are three record types a filter tells apart.**
  *Damaged.* Live store, 2026-11-22: every one of the 1,339 question-box answers is a
  `type == "user"` record (a `tool_result` block answering an `AskUserQuestion` call, with a
  top-level `toolUseResult`); all 11,693 mid-turn messages are `type == "attachment"` ·
  `queued_command`. Two record types, three shapes. The house instrument says the same
  (`cctranscript` header, lines 74–75: a pick "arrives as a tool_result, reachable only via
  --tools"). → **CN1.** And "three" is a closed count of live-typing record channels; his words
  also arrive relayed inside a peer session's message (1,036 `origin.kind: peer` records in main
  session files, which the section classes as injected) and through the instruction files the
  harness loads. → **CN6.**
- **A2. Authorship can be told from record fields, and the pre-field records need a rule.**
  *Confirmed.* `commandMode` + `origin.kind` separate human (2,396), origin-absent (228), peer
  (1,036) and task-notification (3,729) in main session files; the instrument's `isHumanQueued
  Command` encodes exactly this and fails closed on an unknown kind. The schema has moved since
  the census: a `humanTurn` key (983 records) and an `origin.kind` of `coordinator` (305, agent
  files) now exist. The section's "need their own rule, not a silent drop" is the right shape.
- **A3. The loss is scope, not sampling noise.** *Confirmed in direction, unrepeatable in
  magnitude.* 965 / (3,013 + 965) = 24.3% as stated. On the 2026-11-22 live store (main session
  files, the house's authorship rule on both channels) typed mid-turn is 29.4% of typed messages
  (2,628 against 6,297) and the human share of mid-turn records is 35.5% (doctrine: 43.3%). The
  2026-08-21 corpus itself is gone from the live store, which the harness prunes, so the
  historic figures cannot be re-derived by anyone later, and the section does not say what
  corpus they came from. → **CN2, CN3.**
- **A4. A pick is binding as an answer, not a ruling, and the two homes agree.** *Confirmed.*
  `GUARDS.md` 724–727 says "as binding as one in the opening prompt"; `RECORD.md` at HEAD says "an
  answer and not a ruling"; `COMMUNICATION.md` 214–300 holds the distinction and its marks.
  Binding governs acting on it; ruling governs whose words the doctrine may carry. No conflict.
- **A5. "Written down before the turn ends" is workable.** *Not probed* (no live instance to
  drive); noted as a clause a session can meet only if the instruction arrives with turn left.
  No finding.
- **The brief's account of the work** ("about 75 lines of doctrine, with measured figures that
  can be re-derived from transcripts by count"): the line count holds (76 insertions); the
  re-derivation claim holds for direction only, as A3 says. Noted against the brief, not the
  delta.

### Lens 2 — correctness and quality

- **CN1 (MODERATE).** `RECORD.md` 366–369 (delta): *"In a Claude Code transcript these are stored
  as three different record types, and a read that filters on the first (`type == "user"`) drops
  the other two silently."* The pick is itself a `type == "user"` record; the filter keeps it and
  a reader that then takes `message.content` as a string sees nothing in it. The effect the
  sentence names (the pick is lost) is right; the mechanism is wrong, and `320/080` is to build
  its corpus on this section. The instrument's own history is the accurate account: a read keyed
  on `type === 'user' && !toolUseResult` sees channel 1 only (`cctranscript` 555–562).
- **CN2 (MODERATE).** `RECORD.md` 386–395: *"Measured across the estate's transcripts
  (2026-08-21, classified identically on both channels)"*. The section's second rule is that an
  audit "says which of the three channels it read" and "states that corpus"; its own grounding
  names "both channels" in a three-channel section without saying the third was not counted,
  gives no corpus bounds (which store, which date range, which session files), and says
  "classified identically" without saying how channel 1's authorship was told (on the live store
  78% of string-content user records in main session files are harness task notifications, and
  headless sessions' opening prompts are machine text). V5: the section's evidence fails the
  section's test.
- **CN3 (minor).** `RECORD.md` 397–399: *"Only **43.3%** of mid-turn records are typed by the
  principal; the rest are task notifications, messages from other sessions and system reminders"*.
  Present tense, undated, in doctrine: on 2026-11-22 the figure is 35.5%. And neither the
  instrument's 2026-09-18 census nor the live count finds a system-reminder shape in the mid-turn
  channel (task notifications and peer messages only); system reminders arrive in channel-1
  records. V1.
- **CN4 (minor).** `CHANGELOG.md` 1717 heads the entry *"(2026-11-09 — …)"*; the commit landed
  2026-11-08 11:56 UTC (`TZ=UTC git log --date=iso-local b12c4b15`), and the entry's own body
  dates the pick "2026-11-08". `CONVENTIONS.md` line 57: UTC at rest. The three neighbouring
  headings (1702, 1736; commits 12:04–12:32 UTC) share the class; `datescan` checks the shape,
  not the frame. Mixed frames inside one entry.
- Arithmetic, cross-references, past tense for `cctranscript`'s one-channel read (`210/100` is
  closed and the instrument reads two channels at HEAD), the acceptance test's attribution
  ("Adopt both rules", marked as an answer): all sound.

### Lens 3 — completeness and harvest

- **CN5 (MODERATE).** The rule's first subject in this house is `cctranscript`, the instrument an
  audit of "what did he ask for" runs (the in-repo instance: `docs/decisions/2026-11-09-board-
  states-design.md` 50–54, a record that said he never typed two markers because the read
  predated `210/100`). At HEAD it reads channels 1 and 2 and names what it searched by *layer*
  ("searched prompts+replies…", "Tool output not searched…"), never by the section's three
  channels, and a pick is "undistinguished from other tool output" even with `--tools` (its own
  header). No board item queues the third channel (`grep` over every item naming `cctranscript`
  for pick / question-box / `AskUserQuestion`: none; the open `210` items by title: none). The
  delta's "Not done here" names `320/080` and `320/100` only. The rule landed without a home for
  the house's own compliance with it.
- **V3 mirror sites:** `GUARDS.md` pointer, `README.md` index line and `CHANGELOG.md` entry all
  present and consistent at HEAD. No copy in `docs/build/` or `skills/`, and none is owed: the
  rule is parent doctrine read on demand, not floor text. Discharged.
- **V4 one home:** the rule lives in `RECORD.md`; `GUARDS.md` carries a pointer, not a copy;
  `CHANGELOG.md` is a record. The figures are repeated in `CHANGELOG.md` as a record of what
  landed. Discharged.
- **Name collision, note only:** `tools/quotescan.py` exists at HEAD (`115/110`, `160/900` QK1)
  and reads the *form* of a commit message; its docstring defers the corpus problem to
  `320/080`, whose proposal is also called `quotescan`. Not this delta's defect; `320/080`'s
  taker should know.
- **CN6 (minor).** Lens 1's second half. The section's binary (his typing vs injected text)
  has a third case the house produces every drain: his words relayed verbatim inside a peer
  session's message (this pass's spawn prompt quotes his drain order that way). An audit built
  on the section as written classes the record as injected and the words as not his; "He never
  asked for that" can then be false for words he did say. The section's second rule (state the
  corpus) contains the fix; the text should name the case so a corpus builder does not learn it
  from a wrong count.

### Lens 4 — security and privacy

- The section carries counts, a harness field name and children by type; no transcript text, no
  private repo name, no path. "Mike" is PD4 of the closed list. Checked line by line. Clean.
- My own re-derivation: two scripts under the session scratchpad, read-only over
  `~/.claude/projects/`, printing aggregate counts and field names only; outputs held in the
  scratchpad and deleted at the end of the pass; counts only in this verdict and the log.
- `/security-review`: **NOT RUN, discharged.** The delta is landed markdown, which the scanner
  excludes, and the worktree is dirty with the sibling's removal and this brief; a clean pass
  would be definitionally empty. Weighed as nothing.
- No live write of any kind was made.

### Standing checklist V1–V7

- **V1** — CN1, CN2, CN3: three claims stronger than their evidence, one of mechanism, two of
  measurement.
- **V2** — floor re-run on both planes, exit 0 each; the figures re-derived in direction on the
  live store; the historic corpus is not recoverable (CN2 asks the section to say what it was).
- **V3** — mirrors present and consistent; no stamped copy owed. Discharged.
- **V4** — one home. Discharged.
- **V5** — cross-references reach their rules: `COMMUNICATION.md` § *Asking for a ruling* (the
  device rule and answer-vs-ruling, line 214 at HEAD, 205 at the delta); `GUARDS.md` § *A rule
  with no home is not a rule* (the homing test, 685 / 350); `210/100` exists and is closed. The
  internal contradiction is CN2: the section's own audit does not meet the section's rule.
- **V6** — lens 4 above; scanner discharged with grounds.
- **V7** — provenance above and in the brief.

### Per-commit ledger

- `b12c4b15` (the delta) — read body-free: yes, `coldsweep --commit` with the four `--path`s.
  Findings: CN1, CN2, CN3, CN4, CN5, CN6.
- `e7370f78` (later; one sentence in the section; `160/1250`'s delta by that pointer's title) —
  read body-free: yes, `coldsweep --commit --path docs/method/RECORD.md`. Findings: none; outside
  this pass.

### Re-run ledger

- `nice -n 10 python3 tools/floor.py --plane hook --root .` at HEAD `b1307b77`: exit 0; 19 of 19
  checks run, every enforced check green, warn-only checks clean.
- `nice -n 10 python3 tools/floor.py --plane ci --root .`: exit 0; 20 of 21 run; advisories only:
  secretscan 29, leakscan 3, pointerscan 10 (1 grammar, 9 queue state, on other passes' pointers),
  declarations 0 of 21 meet all five.
- 965 / (3,013 + 965) = 24.26%, printed as 24.3%. As stated.
- Live count, 2026-11-22, main session files, house authorship rule on both channels: typed
  opening 6,297; typed mid-turn 2,628 (29.4%); mid-turn human share 35.5%; picks 1,339, every one
  a `type == "user"` record.
- `/security-review`: NOT RUN — discharged, grounds in lens 4.

### Findings

- **CN1 — MODERATE.** The pick channel's record mechanics are misstated: picks are
  `type == "user"` records, so "three different record types" and "a `type == "user"` filter
  drops the other two" are both false for channel 3 (`RECORD.md` 366–369). *Counsel:* reword to
  two record types and three shapes, and name the real trap: a read keyed on user records
  without tool results sees channel 1 only; a pick lives in a `tool_result` answering
  `AskUserQuestion`.
- **CN2 — MODERATE.** The grounding paragraph does not meet the section's own second rule: no
  corpus bounds, two channels named as "both" in a section about three, no statement of how
  channel-1 authorship was told (`RECORD.md` 386–395). *Counsel:* one clause naming the store,
  the date bounds and the two channels counted, and that picks were not; the method may point at
  the intent record, which rule 2 governs.
- **CN3 — minor.** The 43.3% figure is undated present tense in doctrine and names a record kind
  (system reminders) the mid-turn channel does not carry (`RECORD.md` 397–399). *Counsel:* date it
  as the first figure is dated; "task notifications and peer sessions' messages".
- **CN4 — minor.** `CHANGELOG.md` 1717 is dated on the local day; the commit and the entry's own
  body are 2026-11-08 UTC; the class is shared with the batch's neighbours. *Counsel:* `2026-11-08`;
  a board item for the class if the principal wants the frame checked, since `datescan` reads
  shape only.
- **CN5 — MODERATE.** The house's own audit instrument reads two of the three channels, names
  layers rather than channels, and nothing on the board tracks the third; the delta's non-goals
  omit it. *Counsel:* a `210` item: `cctranscript` reads a pick as the principal's answer (not
  bare tool output) and its search footer names the three channels it read and did not.
- **CN6 — minor.** The typing-versus-injected binary misses his words relayed inside a peer
  session's message; the heading's closed count of "three" is the confident shape the section
  warns against. *Counsel:* one sentence naming the relayed case as a corpus rule, and "three
  channels in the transcript" rather than "three ways".

Every finding is the principal's to decide (rule 3); nothing is applied here.

### Follow-up checklist

- [ ] Principal rules on CN1–CN6 (each may be fixed, backlogged or rejected with grounds).
- [ ] If CN5 is accepted: a `210` item for `cctranscript`'s third channel and channel-named footer.
- [ ] `320/080`'s taker reads CN1, CN2 and CN6 before building the corpus, and knows a
      `tools/quotescan.py` already exists under that name.
- [ ] If CN4's class is accepted: a check or a habit for UTC-day headings in `CHANGELOG.md`.
- [ ] Act 2: reconcile against the sibling and the barred records; screen the commit body.

### Reconcile — act 2 (after the sibling)

Opened on 2026-11-22 UTC, after act 1 was committed unrevised as `58fefeaa` (brief file only), on
the orchestrator's release message, which named the held sibling's path and nothing else. Read in
this phase: the sibling; the queue pointer `160/1100` whole; the intent record `320/070` whole;
the commit bodies of `b12c4b15` (the delta) and `8ef6d59c` (the pointer commit); `docs/sessions/
2026-08-21-2312-three-channels-and-the-instrument-that-reads-one.md` lines 65–110 (the
measurement session) and `docs/sessions/2026-11-08-1059-ruling-round-722a.md` lines 15–30 (the
author's record); item `320/100` lines 53–56; `instruments/ccclose` 225–236 and 2625–2660; the
headline lines of the prior verdict `docs/reviews/2026-10-17-1010-harness-classification-cold.md`.
No act-1 text is revised.

**Per finding, against the sibling and the author's account.**

- **CN1** stands. The intent record states the shapes correctly at field level (opening
  `type:"user"`; mid-turn `type:"attachment"` · `queued_command`; a pick "arriving as a
  `tool_result`") and then says a `type == "user"` filter "drops the second and third silently";
  the 2026-08-21 session says the same. The delta compressed the field-level account into "three
  different record types" and carried the filter claim over. So the mechanism error originates in
  the filing and the delta inherited it; the counsel is unchanged. The pointer's second question
  ("whether the authorship caveat is stated so an audit can follow it") lands here: the record's
  account is followable, the doctrine's is not quite.
- **CN2** stands, narrowed. The intent record and the measurement session hold most of what the
  doctrine omits: "the whole live store", both channels classified the same way, the per-repo
  breakdown, and the first pass's 33.5% error. Neither counts the third channel, and neither
  gives date bounds or the authorship method for channel 1. The record also names several child
  repos by name in the per-repo breakdown, which `260/080`'s later posture (public records
  describe a private repo's state by type) would now bar; that is the record's, not the delta's,
  and is listed as a follow-up. Counsel stands: one clause in doctrine naming the corpus and the
  two channels counted, pointing at the record for the rest.
- **CN3** stands. "System reminders arrive in both records" comes verbatim from the 2026-08-21
  session and the intent record; it was the first pass's explanation of its own over-count, not
  a census of the mid-turn channel. The 43.3% is dated in the record (2026-08-21) and undated in
  the doctrine. Unchanged.
- **CN4** stands. The commit bodies and the author's record add nothing on the date frame.
- **CN5** stands, sharpened by the sibling's question 5. `ccclose` reads all three channels: a
  `queued_command` attachment (line 232), a user record without `toolUseResult` (236), and an
  `AskUserQuestion` answer as `toolUseResult.answers` (2630–2650). So the house has one instrument
  that reads the third channel as his answer and one, `cctranscript`, the search-and-audit tool,
  that does not and names no channel. The 2026-08-21 session already said of the third channel
  that "a patch that adds only `queued_command` must not claim the principal's input is covered";
  `210/100` closed with exactly that patch and nothing queued the remainder. Counsel unchanged.
- **CN6** stands, with the sibling's question 2 folded in: a slash command's typed arguments
  arrive inside a `<command-name>` wrapper in a channel-1 record (261 such records in the live
  store), and the prior verdict `2026-10-17-1010` found HC1 (MODERATE) exactly there, "`<command-
  args>` holds the principal's words, and ccclose drops them", applied by `457f374d`. That is a
  fourth shape his words take, within channel 1, that a wrapper-stripping read loses. The relayed
  peer message remains the case the section does not name.

**The sibling's remaining questions.**

- Q1 (binding versus answer): act 1's A4 — they agree; binding governs acting, ruling governs
  whose words doctrine carries. No finding.
- Q3 (3,020 and 1,305): neither figure is in the intent record, the commit body or any session
  record; both come from item `320/100` lines 53–56, the second child's corroboration. The
  doctrine cites `210/100` for the instrument and nothing for these two. Folded into CN2's
  counsel: the clause that names the corpus names `320/100` for the second repo's figures.
- Q4 (before the turn ends): act 1's A5. The pointer's first question is the same ("decidable in
  the moment"). The rule names the three kinds that stand (a rule, a ruling, a scope), which is
  decidable; the deadline binds only a turn with time left. No finding; the rule's "where later
  sessions will see it" already carries the useful half.
- Q6 (landing and pointer in separate commits): **CN7 — minor, formed at reconcile.** The delta
  is `b12c4b15`; the pointer is its child commit `8ef6d59c`, thirty-six minutes later by author
  date, with the body "a rule-4 pointer is written at the landing". `REVIEW.md` rule 4 reads
  "landing = queuing… in the same commit that lands the work", and TA9 accepted a pointer minutes
  after a series "meeting the rule's intent while its grammar named no commit". This case is the
  queue-run pattern (a worker commits, the orchestrator reads and points), so it will recur every
  run; the window is one commit and was probably closed by one push, which I cannot verify from a
  worktree. *Counsel:* either the pattern's landing step amends the pointer into the worker's
  commit, or rule 4 names the orchestrator pattern as the TA9 allowance. Principal's to decide.

**The brief-writer's re-run.** Its floor at `c132cc1c`: hook and ci exit 0, three `pathscan`
warnings. Mine at `b1307b77`: both exit 0, `pathscan` clean. Consistent; the three paths were
fixed between.

**Commit-body screen.** `b12c4b15`'s body restates the section's figures and attribution, adds no
claim the section lacks and names no private repo. `8ef6d59c`'s body says doctrine changed so the
pointer was written "at the landing"; see CN7.

**Overall, restated: PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE (CN1, CN2, CN5) · 4 minor (CN3,
CN4, CN6, CN7).** CN7 is the one finding formed at reconcile. Every finding is the principal's to
decide; nothing is applied.

**Follow-ups added at reconcile.**

- [ ] The intent record `320/070` names several child repos in its per-repo breakdown; whether
      `260/080`'s posture reaches existing board records is the principal's call.
- [ ] CN7: the queue-run landing step and rule 4's "same commit" wording, one of them to move.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (locally `58fefeaa`, the
hash the reviewer's text cites; landed as `f87c2979` when rebased before this fold); folded here
verbatim (headings demoted two levels, no line wrapped, no word changed) and the sibling file
removed, per the brief. The orchestrator, headless
Opus 5.5 session `23e95a19` started by drain session `eca14b23`, held the partition, formed no
finding and wrote no severity; drain session `eca14b23` wrote no brief and no delta and started no
brief-writer for this pass.*

### Held back — do not open before your findings are durably written

Sibling of `docs/reviews/2026-11-09-0126-three-channels-cold.md` (`REVIEW.md` rule 1). Written
2026-11-09 UTC by session `84e3aa7f`, the brief-writer, which authored none of the delta. Open this
only after act 1 is committed. Everything here is a floor, never a fence, and none of it is a
finding.

#### The queue pointer's questions (author-written, verbatim)

> whether 'meant to stand' is decidable by a session in the moment; whether the authorship caveat is
stated so an audit can follow it.

#### The brief-writer's own questions

1. `GUARDS.md` now says something he "chose in the question box" is as binding as the opening
prompt. The house also holds that a pick from offered options is an answer, not a ruling. Do the two
agree?
2. Is three the right number? A slash command's typed arguments, a Stop-hook's feedback, a pasted
message: check against what the transcripts hold, and against the later `457f374d` commit.
3. Where do 3,020 and 1,305 come from? Find each figure's source.
4. "Before the turn ends" is the homing deadline. Is it followable for a turn that is mid-work when
the instruction arrives?
5. Who else in the instruments reads a single channel today, not only `cctranscript`?
6. The landing commit and the pointer commit are separate (`b12c4b15`, then `8ef6d59c`).

#### What the brief-writer ran, and what it got

- `floor`: at c132cc1c: hook exit 0, ci exit 0. pathscan reports 3 findings, warn-only:
  docs/method/EVIDENCE.md:427, docs/method/session-open/session-open-prompt.md:13 and
  docs/method/session-open/template-history.md:10 (paths that do not exist from the repo root).

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels; three lines over 100 columns left as written
(`docs/reviews/` is outside wrapscan's reach, and wrapping would touch the reviewer's text). No
public-repo gate blocked a token, so no placeholder was needed.*

### Review log — atelier 160/1100, cold pass on 320/070 (three channels)

Reviewer: Fable 5.1 (claude-fable-5-1), spawned by orchestrator session 23e95a19 (Opus 5.5),
started by drain session eca14b23 (Opus 5.5). Worktree:
`/Users/mike/worktrees/fable/atelier-160-1100-2236/atelier`. Finding prefix `CN`.
Commands, files and evidence only. No transcript text. Public-safe.

#### Act 1

- 2026-11-22T22:38Z `date -u`; `uptime` load 7.70 11.43 14.05.
- `git merge-base --is-ancestor b12c4b15 HEAD` exit 0. HEAD = b1307b77. `git status --short`:
  only ` D docs/reviews/2026-11-09-0126-three-channels-cold.deferred.md` (orchestrator's
  partition; left alone). `python3 --version` = 3.14.6.
- Read brief `docs/reviews/2026-11-09-0126-three-channels-cold.md` lines 1–197 in full.
- Read `docs/method/REVIEW.md` lines 1–835 in full (verdict shape, rules 1–4, V1–V7).
- `python3 tools/coldsweep.py --root "$W" --commit b12c4b15 --path docs/method/RECORD.md --path
  docs/method/GUARDS.md --path docs/method/README.md --path CHANGELOG.md` exit 0: subject, stat,
  diff of 4 files (76+ / 2-), body not printed; 0 board-store files touched; 0 barred files
  touched. Delta: RECORD.md +49 (new section "What the principal said arrives three ways"),
  GUARDS.md +5 (one paragraph under "A rule with no home is not a rule"), README.md ±5 (RECORD
  line), CHANGELOG.md +19.
- `git log --oneline b12c4b15..HEAD -- <4 paths>`: ~110 commits since, mostly CHANGELOG.md.
  Next: diff the three doctrine files since the delta to see whether the section moved.
- `git diff b12c4b15..HEAD --stat -- RECORD.md GUARDS.md README.md`: all three moved since (RECORD
  +245/-, GUARDS +382, README +19). `grep -n "What the principal said arrives three ways"`: the
  section is at RECORD.md:358 at HEAD; GUARDS.md:724-727 holds the pointer paragraph; README.md:106-108
  the index line; CHANGELOG.md:1717-1735 the entry. Mirror sites intact.
- Read RECORD.md 340-420 at HEAD (the section and its neighbours). One sentence differs from the
  delta: "A pick is an answer and not a ruling; that section holds the difference and the marks."
  `git log -S'an answer and not a ruling; that section' -- docs/method/RECORD.md` = e7370f78
  (2026-11-10 01:56 +1300, subject "board: queue the cold pass on the asking doctrine (160/1250)").
  Read body-free: `coldsweep.py --commit e7370f78 --path docs/method/RECORD.md` exit 0 (+2/-1,
  that sentence only; 5 board-store files left out by default, not read). 160/1250's first line
  (title only) says it covers 320/820, 420/020 a+b, 020/270: the answer-vs-ruling doctrine. So the
  later sentence belongs to another queued pass; no finding formed on it here.
- Cross-references reached (V5): `COMMUNICATION.md` § "Asking for a ruling — the ask goes in the
  device, the account beside it" exists at HEAD (line 214) and at the delta commit (line 205);
  read 214-300 at HEAD: it holds the device rule and the answer/ruling distinction with its marks.
  `GUARDS.md` § "A rule with no home is not a rule" exists at HEAD (685) and at the delta (350);
  read 685-735 at HEAD: holds the homing test; the delta's paragraph sits at 724-727 unchanged.
- `docs/PERSONAL-DATA.md` lines 1-80: PD4 allows the first name "Mike" in doctrine. The section's
  use of "Mike" is within the closed list. Checked sound.
- Commit dates: `git log -1 --format=%ai/%ci b12c4b15` = author 2026-11-09 00:56 +1300, committer
  01:33 +1300; `TZ=UTC git log --date=iso-local` = 2026-11-08 11:56 UTC. Neighbours 7ad98503
  (260/080), 4458a157 (020/240), 920cfed1 (160/630) all landed 2026-11-08 12:04-12:32 UTC.
  CHANGELOG.md headings at 1702, 1717, 1736 all say "(2026-11-09 — …)"; 1754 says 2026-11-08.
  `CONVENTIONS.md` line 57: "UTC at rest; local on presentation"; line 59: prose stamps
  `YYYY-MM-DD`. The delta's heading date is the local day, not the UTC day, and the entry's own
  body dates the pick "2026-11-08". -> candidate CN4 (minor, class shared with the batch).
- Mirror sweep: `coldsweep.py --root W --also-exclude <pointer> --also-exclude <intent record> -i
  'three channels|three ways|question-box pick|mid-turn (message|instruction)'`: 54 hits over 936
  files, 817 excluded as barred. Hits outside the delta's four files: docs/ROADMAP.md:245 (this
  pass's index line, title only), docs/decisions/2026-11-09-board-states-design.md:52,
  docs/method/census/2026-11-16-1204-…md:375, instruments/README.md:356, instruments/cctranscript
  (comments), cctranscript.test.js, man/cctranscript.1. No hit in docs/build/ or skills/
  (`grep -rn -i "mid-turn|three channels" docs/build skills` = none). No stamped copy exists.
- Board titles read (first line only): 210/100 "[x] cctranscript never reads the principal's
  mid-turn messages…" (closed); 320/080 "[ ] PROPOSAL — quotescan…" (open); 320/100 "[ ]
  PROPOSAL — the damaging attribution carries NO QUOTATION MARKS…" (open); 160/1250 (above).
  `grep -il cctranscript docs/roadmap/*/*.md | xargs grep -il "AskUserQuestion|question-box|
  question box|pick"`: no item queues cctranscript's reading of question-box picks. Open 210
  items listed by title: none covers it either. -> candidate CN5.
- Instrument census (house's own account of the record shapes): instruments/cctranscript lines
  30-80 and 555-625. Header comment: a mid-turn message "never becomes a type:"user" record — it
  logs as type:"attachment" · attachment.type:"queued_command""; "Still NOT covered: an
  AskUserQuestion answer arrives as a tool_result, reachable only via --tools, undistinguished
  from other tool output". isHumanQueuedCommand: commandMode "prompt" + origin.kind "human" or
  origin absent = human; "peer" and "task-notification" = not human; census of ~4,100 records
  2026-09-18. Search output (lines 1367-1376) prints `searched <layers>` and "Tool output not
  searched…": layers named, the pick channel not named. man/cctranscript.1 270-320 and
  instruments/README.md 350-362 say the same: prompts, replies, mid-turn, harness; picks absent.
- tools/quotescan.py lines 1-25: a quotescan already exists at HEAD (115/110, 160/900 QK1) that
  reads the FORM of a commit message; its docstring says the corpus problem is 320/080's. Name
  collision with the delta's "320/080 (quotescan)" noted; not this delta's defect.
- docs/decisions/2026-11-09-board-states-design.md 45-60 (decision record, not barred): a record
  stated the principal "never typed" two markers; he had, in two mid-turn messages; cctranscript
  could not see them until 2026-09-18. In-repo instance of the confident negative. Disclosed read.
- docs/method/census/2026-11-16-1204-…md 365-385: notes GUARDS points at the section and slice 1
  counted no rule from it. Not this delta's defect. Disclosed read.
- CHANGELOG.md 2705-2720: the 210/100 entry ("cctranscript reads the principal's mid-turn
  messages without moving any published ref"). Consistent with the section's past tense.

##### Transcript re-derivation (lens 4 terms: read-only, by count only, no text printed)

- `du -sh ~/.claude/projects` = 9.9G; 5,534 .jsonl files (live store; Claude Code prunes it after
  cleanupPeriodDays, so the 2026-08-21 corpus is not recoverable from it).
- Script 1 `count_channels.py` (scratchpad; /usr/bin/python3 -I; nice -n 10; exit 0; prints
  aggregate counts and field names only). Results, 2026-11-22T22:4xZ:
  - Record `type` values: user 455,620; assistant 771,105; attachment 336,662; others (no text
    channel). queued_command attachments 11,693 of 44 attachment types.
  - AskUserQuestion tool_use 1,342 (main files); matching tool_result records 1,339, EVERY one a
    `type == "user"` record (content list of tool_result, top-level toolUseResult present).
  - queued_command by (commandMode, origin.kind), main-session files: prompt/human 2,396;
    prompt/ABSENT 228; prompt/peer 1,036; task-notification/ABSENT 2,312;
    task-notification/task-notification 1,417. Agent files add task-notification 3,982,
    None/coordinator 305, None/peer 17. New keys seen: `humanTurn` (983 records), origin.kind
    `coordinator` (305). No `system-reminder` shape in this channel.
  - type:"user" string-content, not isMeta, main files: 5,645, of which 4,402 open with
    `<task-notification`, 261 with `<command-name`, 245 `<local-command`, 737 plain.
- Script 2 `count_ratio.py` (same terms; exit 0): main-session files, non-sidechain records.
  typed opening (plain + slash) 6,297; harness-led 5,187; typed mid-turn (house rule) 2,628;
  other mid-turn: peer 1,036, not-prompt 3,732; picks 1,339. Share mid-turn 29.4% (doctrine:
  24.3% at 2026-08-21); mid-turn human share 35.5% (doctrine: 43.3%, undated). Direction of both
  claims confirmed on the 2026-11-22 store; magnitudes moved. `opening.typed` still includes
  machine-written opening prompts of headless sessions, so it overstates his typing: the
  channel-1 authorship problem the section says it handled ("classified identically") without
  saying how.
- Arithmetic: 965 / (3,013 + 965) = 24.26% -> 24.3% as stated. Sound.

##### Re-run ledger

- `nice -n 10 python3 tools/floor.py --plane hook --root W` exit 0 (19 checks run / 19 listed;
  every enforced check green; warn-only checks clean). Output in scratchpad floor-hook.txt.
- `nice -n 10 python3 tools/floor.py --plane ci --root W` exit 0 (20 run / 21 listed; secretscan
  29 advisory, leakscan 3 advisory, pointerscan 10 advisory: 1 grammar, 9 queue state, on other
  passes' pointers by path; declarations 0/21 meet all five, advisory). floor-ci.txt.
- `/security-review`: NOT RUN, discharged: landed markdown delta; the worktree is dirty with the
  sibling's deletion and this brief; the scanner excludes markdown. Weighed as nothing.
- `uptime` before each heavy command: load 7.70 / 16.60 / 76.94 / 31.05 / 9.79 (other passes).

##### Candidate findings formed (act 1)

- CN1 MODERATE — RECORD.md:366-369 (delta) "stored as three different record types, and a read
  that filters on the first (type == "user") drops the other two silently". Live: picks are
  type:"user" records (1,339 of 1,339). Two record types, three shapes. Instrument's own
  comment agrees (cctranscript:555-562, 74-75). Breaks V1 / lens 2.
- CN2 MODERATE — RECORD.md:386-395 grounding paragraph: names no corpus bounds, two channels
  ("both channels") in a three-channel section without saying the third was unread, and no
  method for channel-1 authorship. Breaks the section's own rule 2 (V5), V1.
- CN3 minor — RECORD.md:397-399 "Only 43.3% of mid-turn records are typed by the principal"
  undated present tense; names system reminders in that channel, unsupported by either census.
- CN4 minor — CHANGELOG.md:1717 heading dated 2026-11-09, commit 2026-11-08 UTC; CONVENTIONS
  UTC at rest; the entry's body says 2026-11-08. Class shared with three neighbours.
- CN5 MODERATE — harvest: the house audit instrument reads two of three channels, names layers
  not channels, no board item queues the third channel; the delta's "Not done here" omits it.
- CN6 minor — lens 1: "three" is a closed count; his words also arrive relayed inside a peer
  message (origin.kind peer, 1,036 records, classed "injected") and by instruction files; the
  heading's confident count is the shape the section warns against.
- Checked sound: GUARDS "as binding" vs RECORD "an answer and not a ruling" (binding ≠ ruling,
  COMMUNICATION 214-300 holds the distinction); "Mike" within PD4; cross-refs reach their rules;
  no private name or transcript text in the delta; child repos by type only; wrapscan/spellscan/
  datescan green at HEAD on both planes.

##### Act 1 written and gated

- 2026-11-22T22:59Z–23:03Z: Status line updated (ACT 1 WRITTEN, PASS-WITH-FINDINGS 0/3/3); verdict
  appended below a `---` divider in the brief (provenance, method, lenses, V1–V7, ledgers, CN1–CN6
  with counsel, follow-ups). Tables converted to lists so no new line exceeds 100 characters; the
  only lines over 100 are the brief-writer's own paths and commands (lines 11, 82, 162, 172, 173).
- Gates: `floor.py --plane hook --root W` with the edited brief in the tree: exit 0, no finding on
  the brief. Individually on the brief: datescan exit 0 (454 lines read), leakscan exit 0 (454
  lines), linkscan exit 0 (no internal links), reviewscan exit 0 (deferred material kept out),
  wrapscan and spellscan exit 0 but "scanned nothing" (docs/reviews is in .wrapscanignore and
  .spellscanignore); widths and NZ English checked by hand instead.
- Scratch deleted: both count scripts and their outputs, the three floor outputs. Nothing left in
  the scratchpad. `git status --short`: ` D …deferred.md` (orchestrator's) and ` M …cold.md` (the
  brief). No commit, no push, no live write.
- Act 1 ends here. Act 2 waits for the orchestrator's release message naming the held sibling.

#### Act 2

- 2026-11-22T23:04Z: release received from the orchestrator; act 1 committed as 58fefeaa (brief
  file only), verified by `git log -1 HEAD`. Sibling read at the released path (its questions:
  pointer Q×2, brief-writer Q1–Q6; its floor at c132cc1c hook/ci exit 0, 3 pathscan warnings).
- Read whole: queue pointer 160/1100; intent record 320/070 (names several child repos by name in
  a per-repo breakdown; not repeated in the verdict). Commit bodies: b12c4b15 (restates the
  section; nothing new), 8ef6d59c (pointer commit, parent = b12c4b15, "a rule-4 pointer is
  written at the landing"). `git rev-parse 8ef6d59c^` = b12c4b15.
- `grep -n "3,020|3020|1,305|1305" docs/sessions/*.md`: no source (one unrelated hit). Whole-store
  grep: both figures come from item 320/100 lines 53–56 only.
- docs/sessions/2026-08-21-2312-… lines 65–110: "Measured across the whole live store"; first
  pass 4,433 vs 2,237 (33.5%) over-counted injected text; corrected 3,013 vs 965; "system
  reminders arrive in both records" is the over-count's explanation; third channel named as a
  tool_result and "a patch that adds only queued_command must not claim the principal's input is
  covered". docs/sessions/2026-11-08-1059-ruling-round-722a.md 15–30: 320/070 among the items
  applied; no further account.
- instruments/ccclose 225–236 (reads queued_command and user-without-toolUseResult) and
  2625–2660 (reads AskUserQuestion answers via toolUseResult.answers): ccclose reads all three
  channels; cctranscript does not. Sharpens CN5.
- Prior verdict 2026-10-17-1010-harness-classification-cold.md headline lines: HC1 MODERATE
  "<command-args> holds the principal's words, and ccclose drops them"; applied by 457f374d.
  Folded into CN6 as a channel-1 sub-shape.
- Reconcile written beneath the act-1 verdict: CN1–CN6 stand (CN2 narrowed, CN5 and CN6
  sharpened); CN7 minor formed at reconcile (landing and pointer in separate commits; the
  queue-run pattern makes it recur; TA9 precedent). Overall restated 0/3/4. Status line updated
  to ACT 2 WRITTEN. No act-1 text revised. Sibling not folded, nothing deleted.
- Gates after act 2: floor hook plane exit 0 (no finding on the brief); datescan, linkscan,
  leakscan, reviewscan each exit 0 on the brief; widths checked by hand (only the brief-writer's
  five path/command lines exceed 100). Scratch outputs deleted. `git status --short`: ` D
  …deferred.md`, ` M …cold.md`. No commit, no push, no live write.
