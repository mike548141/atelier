# Cold pass — the principal speaks through three channels (`320/070`)

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** ACT 1 WRITTEN 2026-11-22 UTC — PASS-WITH-FINDINGS (0 MAJOR, 3 MODERATE, 3 minor), by
a Fable 5.1 reviewer under the principal's drain order of 2026-11-23 NZDT. Act 2 (reconcile
against the sibling) pending; findings are the principal's to decide (rule 3).
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
`docs/reviews/2026-11-09-0126-three-channels-cold.deferred.md`, every delta commit's message body,
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
