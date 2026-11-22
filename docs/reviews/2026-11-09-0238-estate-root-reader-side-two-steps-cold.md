# Cold pass — the estate root as an ordinary private repo, independence fixed at the reader, the account before the device

**Pass type:** code and doctrine cold pass, per `docs/method/REVIEW.md` rule 4 (a rule, a template
and a tool that fixes how reviewers read are doctrine by function, rule 3).
**Tier:** Fable 5.1, the principal-named review tier, checked at selection by whoever takes the
pass. A session that cannot run on it stops (rule 4).
**Status:** RUN 2026-11-22 UTC, both acts written (act 1 committed before the sibling opened,
locally as `81356fbd`, landed as `feafc1e6`; reconcile beneath it; sibling and review
log folded in below by the orchestrator). PASS-WITH-FINDINGS, restated at reconcile: 1 MAJOR /
2 MODERATE / 3 minor / 4 note. Findings await the principal's ruling (rule 3); nothing applied. Brief written
2026-11-09 UTC by session `9bb1b984`, a headless Opus 5.5 brief-writer. Run under the principal's
drain order of 2026-11-23 NZDT (drain session `eca14b23`, orchestrator `ec57023b`).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/1210-rule-4-cold-pass-queued-estate-root-reviewer-side-two-steps.md`.
**Size of this pass:** medium: about 670 changed lines, half of them `tools/coldsweep.py` and its
tests, the rest doctrine across eleven files, three stamped or mirrored.
**Why it earns a review:** The delta withdraws a boundary rule, moves a review-independence duty
from every writer to one reader, and changes the rule for every ask put to the principal. Each of
those propagates to every child. The worst failure is a reviewer who believes it is cold and is
not, with the record saying it was.

## Spawn provenance

- **Author of the work under review:** a principal-opened Opus 5.5 queue run, session `722ac2e2`,
  2026-11-09, in its ruling round, and the Sonnet worker it dispatched for each commit (per the
  queue pointer). The author queued this pass and does not take it.
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
  item whole; the first line, last nine lines and every `MAJOR` line (verdict counts and finding
  IDs) of `020/050`, `160/910`, `160/930`, `160/270`; the `MAJOR` and answer lines of `020/030`;
  every delta commit body-free through `tools/coldsweep.py --commit`, `e76250cf` whole, the others
  by their prose hunks; commit subjects through `git log`;
  `docs/reviews/2026-11-09-0207-leakscan-off-rules-cold.md` whole (an unrun brief, read for house
  form). It opened **no prior verdict and no delta commit's message body**. Its harness also loaded
  user-level and repo instruction files and a memory index, which hold private context this brief
  does not carry. Everything evaluative it formed is in the sibling.

## The acceptance test

The principal's answers, printed by these lines. They are labels of options he picked; the option
text around them is the author's and is barred until phase 2.

```
grep -o '"Treat like any private repo"' \
  docs/roadmap/020-policy-as-code-programme-five-tracks-mik/050-the-join-c5-guards-was-written-twice-more-on-2.md
grep -o '"Fix the reviewer.s side"' \
  docs/roadmap/160-doctrine-review-owed/910-rule-4-cold-pass-queued-deferral-side-doors.md
grep -o '"Always, as two steps"' \
  docs/roadmap/160-doctrine-review-owed/270-rule-4-cold-pass-queued-decision-asks.md
```

All three are recorded as answers, not rulings in his own words. `docs/method/REVIEW.md` rule 2,
*the reviewer's start-up reading*, `docs/method/RECORD.md` § *The record is public* and
`docs/method/COMMUNICATION.md` § *Asking for a ruling* state what the delta takes them to authorise.
Those are the author's claims to test.

## What the work is

Three commits on `main`, landed 2026-11-09:

- **`e76250cf`** — `method: the estate-root repo is named like any private repo (020/050, 020/030)`.
- **`0ba1ba03`** — `method: an ask's account always arrives as its own message, before the device (160/270)`.
- **`47e8345f`** — `review: independence is fixed at the reader; coldsweep --commit defaults to the safe view (160/910, 160/930)`.

Delta paths, read at each commit and at HEAD:

- `docs/method/PROPAGATION.md`, `RECORD.md`, `REVIEW.md`, `COMMUNICATION.md`, `00-APEX.md`,
  `TOOLBOX.md`, `AUTONOMY.md`, `GUARDS.md` (all under `docs/method/`)
- `docs/build/templates/CLAUDE.md`, `CLAUDE.md`, `skills/review-brief/SKILL.md`
- `tools/coldsweep.py`, `tools/test_coldsweep.py`, `tools/README.md`
- `docs/decisions/2026-08-05-1233-estate-internal-context-in-public-records.md` (a dated correction)
- `CHANGELOG.md`

`tools/README.md` is outside the pointer's path list and inside `47e8345f`, so it is named here.
`e76250cf` also edits two board files the default read leaves out:
`docs/roadmap/020-policy-as-code-programme-five-tracks-mik/250-the-cost-to-weigh-honestly-because-it-is-what.md`
and `docs/roadmap/110-estate-duplication-exception-audit-mike/README.md`. They are outside the
pointer's path list. Name one with `--path` only if your own judgement needs it, and disclose that
you did.

First confirm the tree holds the delta, then read each commit body-free:

```
git merge-base --is-ancestor 47e8345f HEAD; echo $?
python3 tools/coldsweep.py --root . --commit e76250cf
python3 tools/coldsweep.py --root . --commit 0ba1ba03
python3 tools/coldsweep.py --root . --commit 47e8345f
```

Plain `git show` is barred: it prints the message body before the diff, and reading is atomic (rule
1). `tools/coldsweep.py --commit` is itself part of this delta. With no `--path` it leaves the board
store out, so the three lines above never show the intent records.

Then see what has landed on those paths since, and read anything new the same way, only as far as
it bears on this delta at HEAD:

```
git log --oneline 47e8345f..HEAD -- docs/method/PROPAGATION.md docs/method/RECORD.md \
  docs/method/REVIEW.md docs/method/COMMUNICATION.md docs/method/00-APEX.md docs/method/TOOLBOX.md \
  docs/method/AUTONOMY.md docs/method/GUARDS.md docs/build/templates/CLAUDE.md CLAUDE.md \
  skills/review-brief/SKILL.md tools/coldsweep.py tools/test_coldsweep.py tools/README.md
```

**This is an application review.** Rule 2 cannot be fully honoured: the delta's `CHANGELOG.md`
entries and commit subjects carry finding IDs and decision stamps from the passes it applies (DS,
BF, DR, C5R, RR, CH). Review the edited doctrine at HEAD and commit findings first; open those
verdicts after. The residual exposure is named here, not denied (`REVIEW.md` § *Applying decisions
to doctrine*).

## The claims the delta makes

Extracted from the delta, not evaluated here. They are the author's claims to test, not settled
scope. Name your own load-bearing assumptions first (lens 1).

- The estate root "is a private repo like any other: it may be named, in a private or a public
  tree, and what it holds and the condition it is in go by type only in a public record"
  (`PROPAGATION.md`).
- "The name is in pushed history for good either way, so the harm was never the name; it was the
  name beside what the repo holds, and that join stays barred."
- The withdrawal is "forward only" and "the idea of putting the name on the leak scanner's term
  list is dropped with the rule".
- `TOOLBOX.md` and `AUTONOMY.md` "no longer lean on the old rule"; the floor bullet's template copy
  is "kept identical".
- The account "always goes in a finished message of its own, ahead of the device, in every view;
  that message ends its turn, and the device opens the next and carries the choice alone", at "one
  extra turn on every ask" (`COMMUNICATION.md`); "a session cannot see which display mode the
  principal's harness is in".
- A cold reviewer "skips the session-log step" (`CLAUDE.md` step 4, the child template's step 3),
  "whatever its spawn prompt says, and its spawn prompt and the brief say so too".
- The writer-side duty is withdrawn "because it bound writers by role, and no check could see
  whether it was kept"; the fix "cannot be forgotten by a writer".
- The channels listed as "accepted, not closed" and "also accepted" are the whole of what remains
  (`REVIEW.md` rule 2).
- The three recorded occurrences (2026-08-02, 2026-08-17, 2026-10-18) ground the fix.
- `coldsweep --commit` prints "the message's first line only", leaves the board store out with no
  `--path`, exits 1 when nothing is in scope, refuses a `--root` below the repository top and a
  shallow clone's boundary commit (`tools/README.md`).
- "`coldsweep` is not a floor check: no repo's build changes" (`CHANGELOG.md`).

## Scope

The widest the work admits: intent, decisions, assumptions, design, docs, code, test code and live
behaviour. The lenses organise it; they do not bound it. Anything not named a non-goal is in scope,
and a non-goal that fences off the risk is a finding.

**Non-goals:** the thirteen-fix list (pass `160/1220`), including `db8c44b7`'s later hunks on
`REVIEW.md` and the skill; `DR2`, the floor's confirm bullet, which the delta says is routed to
other work; whether the principal's three picks were the right ones, as distinct from whether the
delta does what they authorised.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself, before anything else. Is
   this the right problem, solved at the right altitude and in the right shape, against the
   acceptance test?
2. **Correctness & quality.** Re-drive the claims above. Record each overclaim against the text that
   makes it.
3. **Completeness / harvest.** Every surface that states these behaviours (V3); one home (V4); no
   contradiction (V5). Find tests that would stay green on a broken delta by mutating a scratch
   copy.
4. **Security & privacy**, mandatory: at design altitude what this exposes, over-collects or leaks
   by weakness of design; at code altitude the likely vectors for its class, checked against an open
   catalogue (OWASP ASVS or the domain's equivalent). Aim `/security-review` at code only from a
   clean tree, as *House rules* says; weigh a clean pass over markdown as nothing.

Run the standing checklist V1–V7 unasked (`REVIEW.md` § *The standing checklist*).

## Re-run obligation

Re-run, do not read. The brief-writer ran each line once, on 2026-11-09 UTC, from the worktree root,
except the `cd tools` line, and its results are held in the sibling. Read exit codes explicitly.
Check `uptime` first and run the heavy lines under `nice -n 10`. Use the `python3` first on the
machine's `PATH` (3.14.6 when written); CI pins 3.12.

```
python3 tools/coldsweep.py --selftest
cd tools && python3 -m unittest test_coldsweep test_templates; cd ..
python3 tools/floor.py --plane ci --root .
nice -n 10 python3 -m unittest discover -s tools
```

`PROPAGATION.md` keeps a measurement ("63 times across 19 files … 2026-07-28") and the `CHANGELOG.md`
entries record proofs. Any such figure you rely on is a recorded proof (V2): re-run it read-only and
by count. The brief-writer did not re-run those.

## House rules for this run

- **Live systems:** read-only reads of live systems as needed; no live writes. A check that needs a
  write is marked NOT RUN, with why. No push, no write to GitHub, no network service changed.
- **Never print a secret** or any personal data. Probes use scratch copies and synthetic fixtures
  under your scratchpad, deleted when you finish.
- Name your own review worktree in the verdict. It is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and scratchpad. Child
  repos are read-only and reported by count only, never by name or path.
- **Skip the session-log step of the read order** (`CLAUDE.md` step 4; `REVIEW.md` rule 2). If you
  read it anyway, disclose what you met.
- One heavy process at a time, foreground, with a long timeout. Never run an installed tool by bare
  name from `PATH`: use `python3 tools/<x>.py` or `instruments/<x>` from your worktree.
- `/security-review` reads the session's pending diff, not this delta. Aim it at the code by
  reproducing the diff in a scratch clone, or discharge it by grounds and do the code-altitude read
  by hand, never with this brief or its sibling dirty.
- This pass is pending while you run it: anything you write to the session log, the pointer or a
  commit subject before phase 2 names the sibling by file and count only.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. This repo is
  PUBLIC: quote no secret, email address, private repo name or path, and do not join the estate
  root's name to what it holds.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content; the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every prior
verdict in `docs/reviews/`, this brief's sibling
`docs/reviews/2026-11-09-0238-estate-root-reader-side-two-steps-cold.deferred.md` (now folded below;
by count: 16 questions, 3 facts), every other item under `docs/roadmap/160-doctrine-review-owed/`
beyond its title, every delta commit's message body, and these intent records beyond their first
line:

- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/050-the-join-c5-guards-was-written-twice-more-on-2.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/030-c5-re-ruling-owed-the-composed-term-list-execu.md`
- `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/250-the-cost-to-weigh-honestly-because-it-is-what.md`
- `docs/roadmap/280-cross-session-channel-mike-commissioned/030-rule-4-cold-pass-queued-the-channel-section.md`

`160/910`, `160/930`, `160/270` and `160/230` are under the barred folder above. The delta's own
docstrings, comments, README and `CHANGELOG.md` entries carry the author's account of why; they are
the delta, and reading the delta is never barred.

Sweep with `coldsweep`, never a hand-written exclusion:

```
python3 tools/coldsweep.py --root <your-worktree> \
  --also-exclude docs/roadmap/160-doctrine-review-owed \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/050-the-join-c5-guards-was-written-twice-more-on-2.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/030-c5-re-ruling-owed-the-composed-term-list-execu.md \
  --also-exclude docs/roadmap/020-policy-as-code-programme-five-tracks-mik/250-the-cost-to-weigh-honestly-because-it-is-what.md \
  --also-exclude docs/roadmap/280-cross-session-channel-mike-commissioned/030-rule-4-cold-pass-queued-the-channel-section.md \
  'estate.root|session-log step|side door|finished message of its own'
```

`--include-barred` only with disclosure in the verdict.

## Process

**Phase 1 (act 1).** Reproduce the floor first; work the lenses, your own assumptions and the re-run
list. Append your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, any orchestrator, what you read, the UTC day), per-lens answers, V1–V7 each
answered or discharged with grounds, each load-bearing assumption damaged or confirmed with its
probe, a per-commit ledger (read body-free yes/no, findings by id), findings with stable IDs (prefix
`RW`: `RW1`, `RW2`, …) and severities (MAJOR / MODERATE / minor / note), an overall PASS /
PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger and a follow-up checklist. Then STOP:
act 1 is committed, unrevised, **before** the sibling is opened. Edit no other file.

**Phase 2 (act 2).** Open the sibling and the barred records; screen the delta's commit bodies;
append `### Reconcile` beneath your verdict, with per-finding notes against the sibling's questions
and the author's account, any finding formed at reconcile marked as such, and the overall line
restated. Never revise act-1 text. Then fold the sibling in below the reconcile and delete it.

The work is doctrine by function, so every finding is the principal's to decide (rule 3): record
all, apply nothing. Counsel per finding is welcome, labelled as counsel and kept beneath it.

---

## Verdict — act 1 (2026-11-22 UTC)

**Overall: PASS-WITH-FINDINGS — 1 MAJOR, 2 MODERATE, 3 minor, 3 note (RW1–RW9).** The delta
does what the three picks authorised, and its code half holds under probe; the MAJOR is a
sentence the delta added to `REVIEW.md` that contradicts the same file's rule 4 and declares
duty-free the one author-written record every reviewer of this pass was pointed at.

### Provenance (V7)

- **Reviewer:** Fable 5.1 (`claude-fable-5-1`), the principal-named tier, checked at selection.
  A subagent started for this pass alone.
- **Orchestrator:** headless per-pass session `ec57023b` (Opus 5.5), started by drain session
  `eca14b23` (Opus 5.5). Both off-tier; both hold the partition, form no finding and write no
  severity. Disclosed in the claim (`9d95ebf3`), the pointer and here. Neither wrote the brief
  or the delta; neither is barred by the brief. I was not started or instructed by `9bb1b984`,
  `74f2b8cd` or `722ac2e2`.
- **Approval:** the principal's drain order of 2026-11-23 NZDT, quoted in the pointer's claim.
- **The orchestrator's reviewer-facing instructions** (rule 4, RR2): the spawn prompt is in the
  appended review log, § *Spawn prompt*, verbatim save re-wrapping and one elided machine fact.
  It was process only: paths, tools, the barred set (the brief's own, unchanged), the shape of
  the deliverable, release timing. No question about the delta, no pointer to a risk, no request
  about a finding. No release message had arrived when this act was written.
- **Worktree:** `/Users/mike/worktrees/fable/atelier-160-1210-2047/atelier`, HEAD `9d95ebf3`,
  read-only to me except this file and the log. The `.deferred.md` sibling is absent from it by
  the partition (shows as deleted); I did not look for it anywhere.
- **Scope pin:** the pointer names a moving bound ("the commits that close those items … and
  the commit that closes `320/830`"). Pinned here: `0ba1ba03`, `e76250cf`, `47e8345f` (the
  brief's three) and `0b29bf4e` (the `320/830` widening of 2026-11-09, which the brief predates
  and does not list; see RW5). All four read body-free with `tools/coldsweep.py --commit`; so
  were the two later commits that reversed part of the delta at HEAD, `2a6d7a41` and `978008c7`.
  The edited doctrine was then read at HEAD.
- **What I read, in order:** the brief whole; `REVIEW.md` whole; the queue pointer whole
  (author-written; it carries two seeded questions, RW1); `tools/README.md` §§ 1–903 and
  *coldsweep*; the six commits above body-free; HEAD text of every edited section; the tool's
  source and tests whole; `pointerscan.py` in part. Skipped: `docs/sessions/`, `docs/ROADMAP.md`
  save two index lines (256–257) read to check the index projection, every barred record, every
  commit body, every prior verdict.
- **Exposure, disclosed.** (1) The harness loaded user-level instruction files and a user memory
  index before I read a line; the index names other passes' verdict states and finding ids (not
  this delta's) and the estate root's identity, which is where the name for the V2 count came
  from. The brief-writer disclosed the same load. (2) The brief's sweep printed 146 hits whose
  text I read truncated at 150 columns; non-barred board items appear in it by path and snippet.
  (3) A count-only `grep -l | wc -l` over the barred `160/` folder for one phrase (RW1): 43 of
  188 files; no content read. (4) Commit subjects via `git log --format='%h %s'`. (5) The
  machine-local leak-scanner term list, read for one count, nothing printed. The tool I used to
  read the delta is itself part of the delta (A4).
- **Interpreter:** PATH `python3` 3.14.6 for the re-run lines, as the brief says;
  `/usr/bin/python3` 3.9.6 for the body-free commit reads and the sweep. CI pins 3.12.

### Lens 1 — approach and assumptions, named by me first

- **A1. A reader-side skip closes the log door only if the brief and the spawn prompt say so.**
  Confirmed here (both did) and mechanised nowhere: a spawn prompt that says "read the repo
  first" reopens it. The delta accepts this honestly in `REVIEW.md` rule 2.
- **A2. The channels the delta lists as "accepted, not closed" are the whole of what remains.**
  Damaged twice: the pointer (RW1) and the harness-loaded memory (RW2).
- **A3. "Treat like any private repo" is safe because the name is already public.** Confirmed
  by count: 19 files / 63 lines at the last commit of 2026-07-28 (exact reproduction); 72 files
  and 4 path names at HEAD; 0 in `docs/method`. The join rule is the only control left and it
  is discipline plus sweeps (`RECORD.md`). Probe for a new join since the delta: none found
  (two paths added since carry the letters; both false positives on inspection).
- **A4. `coldsweep --commit` shows me the delta without the author's account.** Confirmed by
  its own tests, by mutation (m2: a subject that leaks the body fails 10 tests) and by the two
  later commits touching only comments and one `BARRED` entry (`git diff --stat 47e8345f HEAD`).
- **A5. "Always, as two steps" meant two turns.** That reading was the delta's; the principal
  corrected it on 2026-11-12 and HEAD now says "text then device, not two turns" (RW3). Right
  problem, wrong altitude: a four-word pick was built into a rule with a stated cost without
  being re-briefed.

Right problem (three real doors, one false branch, one rule that did not hold), right shape
for two of three; the independence fix is at the right altitude for the log and the wrong one
for the board, where a writer-side ceiling still exists and is neither kept nor guarded (RW1).

### Lens 2 — correctness: the claims re-driven

Each claim in the brief's § *The claims the delta makes*, re-driven:

- **Estate root "may be named … by type only".** Stated at HEAD in `PROPAGATION.md` 323–326 and
  338–351, `RECORD.md` 565–572, the floor bullet and its stamped copy (identical, `stampscan`),
  the ADR note, `AUTONOMY.md` 55–61. Consistent.
- **"The harm was never the name".** Grounded: 63/19 reproduced; the name is also in 4 tracked
  path names at HEAD.
- **Forward only; term-list idea dropped.** The term list carries the name 0 times; no scrub in
  the delta. Holds.
- **`TOOLBOX.md` / `AUTONOMY.md` no longer lean on the old rule.** `TOOLBOX.md` 142 drops the
  estate-root clause; `AUTONOMY.md` re-grounds on `RECORD.md`. Holds.
- **Template copy "kept identical".** `stampscan`: `[identical]`, 109 lines. Holds.
- **Account "always … a finished message of its own … one extra turn".** Overturned at HEAD by
  `2a6d7a41` and `978008c7`: same turn, never end the turn between. RW3.
- **"a session cannot see which display mode".** Not falsified; stated above its evidence. RW7.
- **Cold reviewer "skips the session-log step … spawn prompt and brief say so".** `CLAUDE.md`
  34, template 148 (step 3), `SKILL.md` 76–80, `RECORD.md` 76–79, rule 2. Holds; the mirrors
  point at one home.
- **Writer-side duty withdrawn; the fix "cannot be forgotten by a writer".** Withdrawn (one
  live mention, the withdrawal itself). "Cannot be forgotten" is true of the skip and false of
  the board. RW1.
- **The accepted channels "are the whole of what remains".** Overclaim: RW1, RW2.
- **Three occurrences ground the fix.** Two ground the onramp skip; the third was a sweep door.
  RW6.
- **`coldsweep --commit`: first line only, board out by default, exit 1 on nothing, root and
  shallow refusals.** Each confirmed live and by a mutant that fails its test (m1–m6, m9–m12).
- **"not a floor check: no repo's build changes".** Not in the registry; `floor.py --plane ci`
  lists it nowhere. Holds.

### Lens 3 — completeness and harvest

- Mirror sweep (V3): the three behaviours each have one canonical home and stamped or pointing
  copies; `stampscan` and the `file and count` / `estate.root` sweeps found no stale mirror.
  The brief's own house rules still practise the withdrawn duty ("by file and count only") —
  that is the brief-writer's habit, not a repo surface; noted, not a finding.
- The delta as landed carried a dangling section citation (`RECORD.md` → a heading that exists
  only inside the floor's fenced block) and a miscount; `0b29bf4e` fixed both. At HEAD the
  citation reaches the rule (`PROPAGATION.md` § *The standard child doctrine block*, lines
  84–357 with the fence at 133–243). RW5 records the brief-scope gap it exposed.
- Tests that stay green on a weakened tool: two (RW8). Tests that stay green on a broken one:
  none found in 12 mutants.
- Not harvested: the `CHANGELOG.md` reversal entry (RW3); a pointerscan family for the
  "Questions worth…" shape (RW1).

### Lens 4 — security and privacy

- **Design altitude.** The withdrawal widens what a public tree may say (the name) and keeps the
  join barred by discipline alone. The threat is reconnaissance by inference: a public tree that
  says both "the estate root holds credentials and the inventory" (generic, `PROPAGATION.md`
  229–239) and, in 72 files, which repo the estate root is. The delta names this as the harm
  model ("the name beside what the repo holds") and accepts the inference risk implicitly; the
  evidence that the stricter rule did not hold (63/19) is sound, and I found no new join since.
  Stated at strength: the control is now write-time discipline, and the one guard adjacent to it
  (`namescan`) reads the same term list, which does not carry the name. Accepted as the
  principal's answer; recorded, not re-argued.
- **Code altitude** (`coldsweep.py`, class: a local CLI wrapping `git`; ASVS V5 input handling,
  V8 data protection in spirit). Subprocess list arguments, no shell; `--end-of-options` on the
  rev; `--no-ext-diff --no-textconv --no-color` on every diff; `--no-notes` on the message read;
  tests for an external diff driver, textconv, colour, notes, option-shaped revs, a failed git.
  Vectors covered. Residual, stated by the tool itself: the body is requested (`%B`) and never
  printed; `log.showSignature` is not disabled, so a signed commit could put a signature line
  where the subject goes (cosmetic, not a leak; untested).
- **`/security-review`: NOT RUN.** It reads the session's pending diff; mine is this brief and
  the partitioned sibling's deletion, which lens 4 says never to scan before findings are
  committed. Discharged by grounds; the hand read above stands in. No secret, personal datum or
  private path was printed by any probe; probes ran on scratch copies and are deleted.

### Standing checklist V1–V7

- **V1:** three overclaims, RW3 (the two-turn cost), RW6 (three occurrences), RW7 ("cannot").
- **V2:** 63/19 re-run, reproduced exactly; re-run lines 1–3 reproduced (ledger). "At least
  five times" not re-run: it counts barred records.
- **V3:** every mirror swept; none stale. The `CHANGELOG.md` is stale on the reversed rule (RW3).
- **V4:** one home per rule; copies stamped or pointing. `RECORD.md` holds the estate-root rule,
  `PROPAGATION.md` the account, each naming the other: acceptable, two roles not two sources.
- **V5:** one contradiction inside `REVIEW.md` (RW1); one between `CHANGELOG.md` and HEAD
  doctrine (RW3); the delta's dangling citation, fixed since (RW5).
- **V6:** lens 4 above.
- **V7:** provenance stated in the brief and repeated above.

### Per-commit ledger

| Commit | Read body-free | Findings |
|---|---|---|
| `0ba1ba03` two steps | yes (exit 0, 5 files) | RW3, RW7 |
| `e76250cf` estate root | yes (exit 0, 8 files; 2 board files left out, named) | none |
| `47e8345f` reader side + coldsweep | yes (exit 0, 9 files) | RW1, RW2, RW6, RW8, RW9 |
| `0b29bf4e` 320/830 (widening) | yes (exit 0, 2 files; 2 board files left out) | RW5 |
| `9485b577` pointer (handoff) | subject only | RW4 |
| `2a6d7a41`, `978008c7` (later, reversing) | yes (exit 0) | bear on RW3 |

### Findings

Every finding is the principal's to decide (rule 3); counsel is labelled and kept beneath.

**RW1 — MAJOR. The delta declares the board reads duty-free while rule 4's pointer ceiling still
binds, is breached in this pass's own pointer, and is unguarded for the shape it takes.**
`REVIEW.md` rule 2 (new text, line 167–170): the onramp's other reads "(the board index, recent
commit subjects) are not on the barred list and carry no writer-side duty now". Rule 4, same
file, line 218–224: the pointer is "a ceiling as well as a floor: refs only, no evaluative
account". The pointer for this pass (`160/1210`, lines 16–18) carries "Questions worth the
pass's time: whether a reviewer that skips the log can still be primed another way; whether any
text still leans on the withdrawn rule": two seeded questions, written by the delta's author,
read whole by the brief-writer (its disclosure) and by me when the orchestrator named the board
file. `tools/pointerscan.py` passed it clean: its grammar check fires on a literal `?` or three
phrase families (lines 279–290, 425–435), and this shape has neither. By filename-count only, 43
of the 188 items in the owed folder contain the same phrase. So the fix "cannot be forgotten by a
writer" for the log and leaves the board door open with a false sentence over it; the mechanism
`REVIEW.md` names as the point of rules 1–2 (framing leaks through the ask) ran through it here.
*Counsel:* strike "and carry no writer-side duty now" and say the pointer ceiling is the duty
that remains; add the "Questions worth the pass's time" family to `_STEER` (the docstring's own
rule: a family is added when a real instance shows it must, and there are 43); move such
questions to the intent record or the deferred sibling.

**RW2 — MODERATE. The "accepted, not closed" inventory omits the harness-loaded memory and
instruction files, a door no reader step reaches.** Evidence: this session's load, before any
file was opened, carried a user memory index naming other passes' verdict states and finding
ids and the estate root's identity; the brief-writer disclosed the same (brief § *Spawn
provenance*). Rule 2 bars prior verdicts; this channel delivers fragments of them to every
session on the machine. The claim "the whole of what remains" (brief's reading of lines
167–174) is therefore an overclaim. *Counsel:* name the channel as accepted-not-closed with the
same disclosure duty the rule gives the board index; where the harness allows, start reviewer
sessions with auto-memory off and record that choice in the spawn prompt.

**RW3 — MODERATE. The two-step rule the delta wrote was overturned three days later and the
`CHANGELOG.md` does not say so.** `0ba1ba03` read "Always, as two steps" as two turns and wrote
"that message ends its turn … one extra turn on every ask" into `COMMUNICATION.md`, the floor
bullet and its stamped copy. On the principal's 2026-11-12 words `2a6d7a41` and `978008c7`
replaced it with "text first, then the device … in the same turn; never end the turn between".
HEAD is consistent across `COMMUNICATION.md` 263–279, `PROPAGATION.md` 167–169, template 52–55.
`CHANGELOG.md` line 942 still states the two-turn rule as the change made, and no later entry
records the reversal (grep "same turn", "two turns", "no longer ends its turn": 0; headings
exist for 2026-11-20 and 2026-11-22, none for 2026-11-12). The delta's own removed text called
`CHANGELOG.md` a current-truth record. Lens 1: the pick was built into a costed rule without the
re-brief rule 3 asks for on an answer that is not in his words. *Counsel:* a dated `CHANGELOG`
entry for the reversal pointing at `420/040`; and a one-line note on the 2026-11-09 entry.

**RW4 — minor. The pointer landed in the next commit, not the landing commit.** `9485b577`
(01:26:28Z) queued `160/1210`; `47e8345f` (01:26:26Z) landed the work. Rule 4: "in the same
commit that lands the work — landing = queuing" (AWA2). The gap is two seconds and the pointer's
bound is unpinned ("the commits that close those items"), pinned above. This repeats the TA9
shape the rule already records as "meeting the intent while its grammar named no commit": twice
is a rule whose grammar the queue run does not follow. *Counsel:* either the rule accepts "the
same push" or the queue run's landing step writes the pointer into the landing commit.

**RW5 — minor. The pointer's delta was widened after the brief and the brief was not.**
`729cae4c` (2026-11-09 12:53Z) added `320/830`'s commit to the pointer; the brief (02:38Z) lists
three commits. `0b29bf4e` fixes a dangling citation the delta itself introduced (`RECORD.md`
pointed at "§ *Doctrine — inherited from atelier*", a heading that exists only inside the floor's
fenced block at `PROPAGATION.md` 133–243) and a miscount. Read and covered here. *Counsel:* the
review-brief skill says a widened pointer re-opens its brief's *What the work is*.

**RW6 — minor. "Grounded in three recorded occurrences" overstates by one.** The 2026-08-02
instance "reached a reviewer mid-pass through a sweep": a sweep door, closed by `coldsweep`
(2026-08-17), not the onramp step the skip removes. Two instances ground the skip.

**RW7 — note. "a session cannot see which display mode the principal's harness is in" is
stated above its evidence.** The environment exposes presentation flags to a session
(`CLAUDE_CODE_QUESTION_PREVIEW_FORMAT`, `CLAUDE_CODE_SESSION_ATTENDED`, `CLAUDE_CODE_ENTRYPOINT`
seen here); none names a focus or display mode, so the claim is not falsified. "No known way"
is the evidenced strength; the rule no longer branches on it, so the stakes are low.

**RW8 — note. Two of the tool's guard tests pass without the guard.**
`test_a_rev_spelled_like_an_option_is_a_rev_not_a_flag` passes with `--end-of-options` removed:
`git rev-parse --verify --quiet '--all^{commit}'` (and `-h`, `--output=…`) exits 1 unaided, so
the inputs cannot tell the guard from its absence. `test_a_notes_ref_never_reaches_the_output`
passes with `--no-notes` removed from the `%B` call, which never carries notes. Both guards are
belt-and-braces; the tests do not show them load-bearing. *Counsel:* say so in the test
docstrings, or find a rev the flag alone saves.

**RW9 — note. `coldsweep --selftest` prints six lines of exercised-run output before its verdict
line**, including "bad pattern" and "a PATTERN is required", against `tools/README.md`'s opening
contract ("one verdict line and nothing else", `320/690`) for scanners. coldsweep is not a floor
check, so the contract may not bind; a reader of the brief's re-run line meets what look like
failures. Pre-dates the delta.

### Re-run ledger

| Line | Result |
|---|---|
| `git merge-base --is-ancestor 47e8345f HEAD` | exit 0 |
| `coldsweep --commit` ×6 | exit 0 each; exclusions named each run |
| `python3 tools/coldsweep.py --selftest` | exit 0, `selftest OK` (3.14.6) |
| `unittest test_coldsweep` (via `discover -s tools -p`) | 56 tests, OK, exit 0 |
| `unittest test_templates` | 55 tests, OK, exit 0 |
| `floor.py --plane ci --root .` | exit 0; ⚠ pointerscan advisory 6, none on this delta |
| full `unittest discover -s tools` | 3382; 1 FAIL (`test_wrapscan` timeout, load 22); alone OK |
| brief's sweep line | exit 0, 146 hits / 746 files, 1015 barred files excluded and named |
| V2 "63 times across 19 files" | reproduced exactly at `7422f2af` (last commit ≤ 2026-07-28 UTC) |
| `stampscan`, `pointerscan` (on the pointer) | clean; the pointer clean is RW1's evidence |
| 12 mutants of `coldsweep.py` | 10 killed, 2 equivalent (RW8) |

### Follow-up checklist (for the principal's decision, not applied)

- [ ] RW1: fix the rule 2 sentence; add the `_STEER` family; decide where pointer questions go.
- [ ] RW2: name the harness-memory door; decide whether reviewer sessions load memory.
- [ ] RW3: `CHANGELOG.md` entry for the 2026-11-12 reversal.
- [ ] RW4: rule 4's grammar or the queue run's landing step.
- [ ] RW5: the skill's line on a widened pointer.
- [ ] RW6, RW7: wording.
- [ ] RW8, RW9: test docstrings; `--selftest` output shape.

### Open questions for the principal

1. RW1: is a "Questions worth the pass's time" line in a pointer a breach of the ceiling you set
   on 2026-07-15 (refs only), or an allowed routing note? Forty-three pointers turn on it.
2. RW2: should a cold reviewer's session run with the harness's auto-memory off, where that is
   possible, or is disclosure enough?

### Reconcile (act 2, 2026-11-22 UTC)

Act 1 was committed unrevised as `81356fbd` before the orchestrator released the sibling's path
by message (process only: the path, the barred records now open, the shape of this section).
**Opened in act 2:** the held sibling (16 questions, 3 facts); the message bodies of `0ba1ba03`,
`e76250cf`, `47e8345f`, `0b29bf4e` and the pointer commit `9485b577`; the eight barred intent
records (`160/910`, `160/930`, `160/270`, `160/230`, `020/050`, `020/030` to its line 400,
`020/250`, `280/030`), read as lines cut at 200 columns; and, in the prior verdicts, only the
finding paragraphs the delta applies (DS1, DS5, DS9, DS11, DS12; BF1–BF5, BF9, BF10, BF15; DR1,
DR3, DR9; C5R3, C5R9; RR2; CH1). Nothing in act 1 is revised; the overall line is restated at
the end.

**Against the sibling's questions.**

- *Q1–Q2 (the pointer's own).* Yes, a reviewer that skips the log is still primed another way:
  by the pointer itself (RW1), by the harness-loaded memory (RW2) and, formed here, by hand-up
  PR titles (RW10). No live text still leans on the withdrawn rule: the only "never by name" at
  HEAD is the withdrawal note (`PROPAGATION.md` 336).
- *Q3.* Swept `docs/method`, `docs/build`, `skills`, `tools/README.md`, `instruments` for
  "never by name" and "by local-path convention": one hit, the withdrawal note. The
  session-open README's `[estate-root repo]` is a redaction placeholder, not the old rule.
- *Q4.* "Bind the property, not the role" now closes a paragraph whose rule is gone; it reads as
  the programme's general lesson and is true of nothing specific in that section. Wording for
  the principal's round; not raised as a finding.
- *Q5.* No guard sees the join: `RECORD.md` 547–550 says so in terms, and `namescan` reads the
  same term list, which carries the name 0 times (act 1). Prose only, by the principal's pick.
- *Q6.* A child's stale copy says the stricter thing, so a child session in the window
  under-names rather than over-names: the safe direction. `AUTONOMY.md`'s pre-flip scrub keeps
  an object: "those lines", the ones joining the name to what it holds (HEAD 55–61).
- *Q7.* Step numbers hold at HEAD: `CLAUDE.md` step 4 (line 34), template step 3 (line 148);
  `3312cdbd` added step 6, after both.
- *Q8.* "read everything first" appears only in the skill's instruction not to say it. The
  queue-run and session-open skills carry no such line. A private harness is out of reach here.
- *Q9.* Agreed, and said in act 1 (A1): "its spawn prompt and the brief say so too" is a
  writer-side duty under another name, on two writers instead of every writer.
- *Q10.* Not on the list, and a real door: `CLAUDE.md` step 6 reads open hand-up PR titles
  before the brief. **RW10 — note (formed at reconcile).** An author's hand-up title can carry
  an account of the delta; the inventory names neither it nor the memory load (RW2). Same class
  as RW2; counsel is the same disclosure duty.
- *Q11–Q12.* RW7 covers the display-mode claim. A headless run asks in prose
  (`COMMUNICATION.md` 281–283). The interrupted-turn and scaling cases are moot at HEAD: the
  rule is one turn again (`2a6d7a41`).
- *Q13.* Probed six `--path` spellings against `978008c7`, whose only barred file is a
  `.deferred.md`: `docs/reviews/*`, `:(glob)docs/**`, `:/`, `:(top)docs`, `:!tools`, `docs`.
  None showed it; every closing line named it as left out; the glob exits 1 (nothing in
  scope). `diff.noprefix=true` (via `GIT_CONFIG_PARAMETERS`) only drops the `a/` `b/`
  prefixes. External diff drivers and multi-line subjects are pinned by the suite (act 1, m2).
  A merge commit is first-parent by design and documented.
- *Q14.* `436273ba`: raw `git diff --stat` shows 12 files; `--commit` shows 2, exits 0 and
  names the 10 board files left out. The design works and the risk the question names is real:
  the only cue that a delta's subject was hidden is a closing line a reader may skim. Kept as
  the ruled BF1 shape; RW1's counsel on pointers is the adjacent fix.
- *Q15.* `git diff 0ba1ba03^1 0ba1ba03` and the `--commit` diff section are byte-identical
  after blank lines are dropped. The instrument did not shape what I read (A4 confirmed).
- *Q16.* C5R9 (minor) said the grant-date requirement "is Mike's 2026-08-09 restatement" and
  should bind; the applied `GUARDS.md` text says exactly that and labels it "not verbatim";
  `attribscan` passes it. Grounded on a recorded answer, weakness disclosed; carried in the
  naming commit because `020/050` decided `020/030` too. Adequate.

**Against the author's account (commit bodies, records).**

- RW1: `47e8345f`'s body says the text "names what stays accepted (DS5)". DS5 named four doors
  the writer-side rule could not close; "carry no writer-side duty now" is the applier's own
  sentence, not DS5's, and no body or record weighs it against rule 4's ceiling. RW1 stands,
  MAJOR.
- RW2: no body or record considers the harness load. Stands.
- RW3, corrected in part: the option the principal picked carried the cost in its text
  (`160/270`: "at the cost of one extra turn"), so the two-turn reading was before him when he
  chose, not supplied after. The lens-1 remark in act 1 is therefore too strong: he was told
  the cost and reversed on experience (`420/040`, 2026-11-12). The finding's substance is
  unchanged: `CHANGELOG.md` records the two-turn rule and not its reversal. Stands, MODERATE.
- RW4: `9485b577`'s body shows the shape is the queue run's design (the worker lands the work,
  the orchestrator lands the board); so the rule's grammar and the run disagree by design, not
  by slip. Stands, minor.
- RW5: `0b29bf4e`'s body says the owning pass "has its delta widened"; the brief was not
  reopened. Stands, minor.
- RW6: the body says the three dates answer DS12 (grounding was not the first occurrence). The
  dates were added for that; one of the three is still a sweep door. Stands, minor.
- RW7–RW9: nothing in the bodies or records bears on them. Stand.
- The brief-writer's held facts: its full suite was 2,718 tests OK in about 647 s on
  2026-11-09; mine was 3,382 with one load timeout that passes alone (ledger). Its `3.9.6`
  `TypeError` note concerns `test_floor`/`test_floorfleet`, which I did not run under 3.9.
- The `e76250cf` body's "failed at least five recorded times" matches `020/050`'s own count
  ("recorded that finding five times"); the figure is the item's, now read, not re-counted.

**Overall, restated: PASS-WITH-FINDINGS — 1 MAJOR (RW1), 2 MODERATE (RW2, RW3), 3 minor
(RW4–RW6), 4 note (RW7–RW10; RW10 formed at reconcile).** Every finding is the principal's to
decide; nothing is applied. Open questions 1 and 2 from act 1 stand.

## Deferred sibling, folded below the verdict (orchestrator, 2026-11-22)

*Released to the reviewer only after its act-1 findings were committed (locally `81356fbd`, the
hash the reviewer's text cites; landed as `feafc1e6` when rebased before this fold); folded here
verbatim (headings demoted two levels, one line over 100 columns wrapped at word boundaries,
no word changed) and the sibling file removed, per the brief. The orchestrator, headless Opus 5.5
session `ec57023b` started by drain session `eca14b23`, held the partition, formed no finding and
wrote no severity; drain session `eca14b23` wrote no brief and no delta and started no
brief-writer for this pass.*

### Held back — the estate root, the reader-side fix and the two-step ask

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer, session `9bb1b984`, which did not author the delta.

#### The pointer's own questions

1. Can a reviewer that skips the log still be primed another way?
2. Does any text still lean on the withdrawn rule?

#### The brief-writer's questions

3. Sweep for the withdrawn rule across every surface, not only the eight files the delta touched:
   the child template's other blocks, skills, `docs/method/session-open/`, the instruments' docs,
   and the floor's own guards. What still says "never by name"?
4. The sentence `Bind the property, not the role` lost its `— public —`. With the rule it summarised
   gone, what does it now bind, and is it still true of anything?
5. The join ("the name beside what the repo holds") is said to stay barred, and the idea of a term
   list is dropped. Is any guard able to see that join, or is it now prose only? Compare with the
   account of why the stricter rule failed: the same text says a rule of that shape was breached at
   least five times.
6. A child's stamped copy of the floor bullet says the old thing until its next pin bump. Does the
   old copy now contradict the parent in a way that makes a child session do the wrong thing in the
   window? `AUTONOMY.md`'s pre-flip scrub: does it still have an object, now the name is allowed?
7. `REVIEW.md` cites `CLAUDE.md` step 4 and the child template's step 3 by number. `3312cdbd`, in
   the same day's landings, added a step to `CLAUDE.md`'s read order. Do the numbers still point at
   the step they name, in every copy?
8. Which spawn prompts exist that say "read everything first": the queue-run prompt, the
   session-open
   prompt, the review-brief skill's template, the API pass harness a private repo holds (by type
   only)? Does the reader-side rule reach each, or only the ones the delta edited?
9. The fix "cannot be forgotten by a writer". Rule 2 also says the spawn prompt and the brief say
   so. Is that a writer-side duty returning under another name?
10. The accepted residuals (board index, commit subjects, queue-run opening prompt, branch names):
    is the list complete? A hand-up PR title, read at open under the step `3312cdbd` added, is a
    further read before the brief. Is it on the list?
11. "A session cannot see which display mode the harness is in": does any harness expose it? What
    happens to the two-step rule in a headless run, where there is no device, and in a turn the
    principal interrupts between the account and the device?
12. The apex now points at the scaling sentence. Is the scaling sentence compatible with "always, in
    every view" for a one-line clarification?
13. `coldsweep --commit`: `--path` accepts git pathspec magic. Can `:(top)`, `:/`, `:!` or a glob
    reach a barred path, with the closing line still reporting it as left out? What about a rename
    out of a barred directory, a merge commit (first parent only), a commit whose subject paragraph
    spans lines, and a repository with an external diff driver or `diff.noprefix` set?
14. Does the board-store default hide a delta whose subject IS a board file, with exit 0 and a
    closing line a reader skims? Compare its output for `436273ba` with raw `git diff`.
15. `tools/coldsweep.py` is the instrument the brief tells you to read the delta with, and it is in
    the delta. Cross-check one of the three commits with `git diff <sha>^1 <sha>`, which prints no
    message body.
16. `GUARDS.md` gains a "when it was granted" clause on a restatement "as the board records it, not
    verbatim". Is that grounded enough for a doctrine change, under the repo's ground-everything
    rule? It is a C5 finding, carried in a commit about naming.

#### Facts held back

- **Re-run lines, 2026-11-09 UTC, machine load about 9 at the start, run from the worktree root
  (the `cd tools` line from `tools/`).** `python3` was 3.14.6. `coldsweep --selftest` exit 0;
  `test_coldsweep test_templates` 104 tests, exit 0; `floor.py --plane ci --root .` exit 0, with
  `pathscan` warn-only findings; the full `unittest discover -s tools` under `nice`: 2,718 tests in
  about 647 s, OK, exit 0.
- **Interpreter:** under `/usr/bin/python3` (3.9.6) `test_floor` and `test_floorfleet` exit 1 with
  `TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'`; the other named test files
  and every `--selftest` exit 0 there. The brief's lines use the `PATH` interpreter for that reason.
  The brief-writer did not trace the source of the error.
- **Not re-run by the brief-writer:** the 2026-07-28 name census and any figure in `CHANGELOG.md`.

## Review log (reviewer, verbatim; private while the pass ran, opened at the fold)

*Form fixes only: headings demoted two levels; no line wrapped (the only lines over 100 columns
are two single path tokens inside the quoted spawn prompt, left as they are); one datescan
allow-marker added where finding IDs read as slash-dates. No public-repo gate blocked a token, so
no placeholder was needed.*

### Review log — atelier 160/1210, Fable 5.1 cold pass

Reviewer: Fable 5.1 subagent. Orchestrator: session ec57023b (Opus 5.5, off-tier,
forms no finding), started by drain session eca14b23. Worktree:
/Users/mike/worktrees/fable/atelier-160-1210-2047/atelier (HEAD 9d95ebf3).
Approval: the principal's drain order of 2026-11-23 (quoted in the board item).
Interpreter used: /usr/bin/python3 = Python 3.9.6 (brief says 3.14.6 on PATH when
written; I used the system interpreter per the orchestrator's load instruction).

#### Act 1

- 20:49Z `uptime` — load 7.52 13.21 12.20, 16 GB laptop, several passes running.
  `git status --short` shows only ` D` on the .deferred.md sibling (expected, the
  partition). HEAD 9d95ebf3.
- Read in full: the brief (273 lines); docs/method/REVIEW.md (836 lines, verdict
  shape, rules 1–4, V1–V7, method-record ruling); the queue pointer
  docs/roadmap/160-doctrine-review-owed/1210-*.md (35 lines); tools/README.md
  lines 1–903 (then grep for coldsweep and gate sections). Skipped docs/sessions/
  entirely per the brief and REVIEW.md rule 2. Did not open docs/ROADMAP.md.
- 20:52Z `git merge-base --is-ancestor 47e8345f HEAD` → exit 0 (delta in tree).
  `git log --oneline 47e8345f..HEAD -- <14 delta paths>` → 70 later commits; on
  tools/coldsweep.py + test only 2 (b68cf410 sessions index retired; b9d86e32
  archivecut). Commit order by CHANGELOG nesting: 0ba1ba03 → e76250cf → 47e8345f
  (all three stamped 2026-11-09 01:26:26Z).
- 20:53Z Body-free reads, `/usr/bin/python3 tools/coldsweep.py --root <wt> --commit
  <sha>` → scratch files; exits 0/0/0; 256, 151, 859 lines; closing lines: e76250cf
  left out 2 board-store files by default (020/250 item, 110/ README), 0 rule-2
  barred; 0ba1ba03 and 47e8345f touched neither. Read all three in full. The tool
  I used to read the delta is itself part of the delta (assumption A4 below).
- Observations while reading (to probe, not yet findings):
  (a) 47e8345f's closing line reports 0 board-store files → the queue pointer
      160/1210 was NOT written in the landing commit (rule 4: landing = queuing).
  (b) The pointer carries "Questions worth the pass's time: …" (two seeded
      questions) — rule 4 says a pointer is refs only, no evaluative account.
  (c) The pointer names "the commit that closes 320/830" as part of the delta;
      the brief lists three commits and does not mention 320/830.
  (d) The brief's own House rules and the pointer still practise the withdrawn
      writer-side duty ("by file and count only"; "by count: 16 questions, 3
      facts") — check whether the skill at HEAD still carries it (V3).
  (e) RECORD.md hunk says "a closing entry carries no duty about deferred
      material" — consistent with (d)'s withdrawal; check SKILL.md mirrors.
  (f) coldsweep: `top != root` comparison — check how root is resolved at HEAD
      (symlinked roots, e.g. /tmp → /private/tmp on macOS).
  (g) The three grounding occurrences: 2026-08-02 was a SWEEP door, not an onramp
      door; the reader-side skip does not address it (V1 strength of grounding).
  (h) The "accepted, not closed" inventory omits the harness-loaded memory and
      user-level instruction files, which the brief-writer itself disclosed as
      private context; this session's own harness load carried prior finding ids
      (other passes, not this delta's) before I read a line of the brief.
- 20:58Z Later commits on the delta's paths: read body-free (coldsweep --commit) 0b29bf4e
  (320/830: RECORD.md § citation fixed, PROPAGATION "Three"→"Four boundaries"),
  2a6d7a41 (2026-11-12: the ask no longer ends its turn; also cclive at open, GUARDS
  allow-marker paragraph, leakscan comment) and 978008c7 (2026-11-17: floor Asking
  bullet says same turn). Each exit 0; board files left out by default and named
  (9 / 3 / 2); 978008c7 also left out one rule-2 barred .deferred.md (named only).
- Pointer provenance: `git log --diff-filter=A -- docs/roadmap/160-…/1210-*.md` →
  9485b577 2026-11-09 01:26:28Z, two seconds AFTER 47e8345f (01:26:26Z), a separate
  commit "board: land …; queue 160/1210". 729cae4c (2026-11-09 12:53Z) widened the
  pointer's delta to 320/830; the brief (02:38Z) predates it and lists 3 commits.
- Subjects naming 320/830 (git log --format='%h %s' | grep; subjects only): 0b29bf4e,
  729cae4c, f7d26241, 84f710d0.
- grep "file and count" over skills/, docs/method, docs/build, CLAUDE.md, tools/README:
  one hit, REVIEW.md:164 (the withdrawal sentence). The withdrawn writer duty has no
  live mirror. grep "Questions worth" in skills/, docs/method, docs/build: none.
- HEAD state read: COMMUNICATION.md 240–310; PROPAGATION.md 160–240, 308–357;
  RECORD.md 66–81, 540–573; templates/CLAUDE.md 48–62, 113–124, 140–150; AUTONOMY.md
  52–64; TOOLBOX.md 22–32 (+grep "reconnaissance" → line 142, no estate-root clause);
  GUARDS.md grep "when it was granted" → 394; 00-APEX.md 143–156; CLAUDE.md step 4
  (skip clause present, line 34); SKILL.md 40–89; tools/coldsweep.py whole (565 lines);
  tools/pointerscan.py 1–60, 262–292, 420–445; tools/README.md 3190–3258.
- `git diff --stat 47e8345f HEAD -- tools/coldsweep.py tools/test_coldsweep.py` → 7+/2−
  in coldsweep.py only, all docstring/comment and one BARRED entry
  ("docs/roadmap/990-done-before-the-split"); the --commit logic I ran is the delta's.
- Brief's sweep line (coldsweep, 5 --also-exclude, pattern as given): exit 0, 146 hits
  over 746 files, 1015 excluded as rule-2 barred, every exclusion named. Hits read as
  path:line:text truncated to 150 chars; non-barred board items appear (titles/snippets
  only). No barred file was shown.
- pointerscan on the 1210 pointer: "✓ clean" although lines 16–18 carry two seeded
  questions ("Questions worth the pass's time: whether …; whether …"). pointerscan's
  grammar check (lines 425–435) fires on a literal "?" or three _STEER phrase
  families; this shape has neither. Count of items in docs/roadmap/160-* whose text
  contains "Questions worth": 43 of 188 (`grep -l | wc -l`; contents not read —
  disclosed as a count-only sweep of a barred folder).
- stampscan --root . → clean, 1 block, template copy [identical] to canonical 'floor'
  (109 lines).
- env var NAMES matching focus|display|mode|claude printed; values of three
  presentation flags read: CLAUDE_CODE_QUESTION_PREVIEW_FORMAT=markdown,
  CLAUDE_CODE_SESSION_ATTENDED=0, CLAUDE_CODE_ENTRYPOINT=claude-vscode. None names a
  display/focus mode.
- Acceptance-test greps (brief § The acceptance test): all three labels print.
- Re-run 1: `python3 tools/coldsweep.py --selftest` (PATH python3 = 3.14.6) → exit 0,
  "selftest OK", preceded by 6 lines of exercised-run output.
- Re-run 2: `python3 -m unittest discover -s tools -p test_coldsweep.py` → Ran 56, OK,
  exit 0 (32.7 s); `… -p test_templates.py` → Ran 55, OK, exit 0. (Run via discover
  with -s, not `cd tools`, per the orchestrator's no-cd instruction.)
- Re-run 3: `nice -n 10 python3 tools/floor.py --plane ci --root .` → exit 0; every
  check ✓ except ⚠ pointerscan advisory: 6 findings (1 grammar on 160/1640, 5 queue
  state), allowmarker warnings on three malformed markers (not in the delta),
  "declarations: 21 checks, 0 meet all five" (advisory).
- Re-run 4: `nice -n 10 python3 -m unittest discover -s tools` → started 21:10Z,
  moved to background by the harness at 600 s; result recorded below when known.
- V2 count script ($S/v2count.sh; the root's name taken from the harness-loaded user
  memory and never printed): last commit on main ≤ 2026-07-28T23:59:59Z = 7422f2af;
  `git grep -c -w [-i] <root-name> 7422f2af` → 19 files, 63 lines (both cases) —
  the delta's "63 times across 19 files" REPRODUCES exactly. HEAD: docs/method 0
  files; whole tree 72 files (word, any case); tracked paths with the name as a
  segment: 4 (a plain substring count of 10 included "finished"/"published").
  Machine-local leakscan term list: 0 lines carry the name (read-only, count only).
- Lens-4 join probe: the one 390/ item whose filename joins the root's name to a
  posture statement was added 2026-09-12 (before the delta). Tracked paths naming the
  root added since 2026-11-09: two by substring, both false positives on inspection
  ("finished"; an archive cut of a 2026-07-18 record). No new name↔posture join found.
- Mutation probes ($S/mutate.py; scratch copies of coldsweep.py + test_coldsweep.py
  under $S/mut/<m>/, tests run by `discover -s <dir>`): 12 mutants, 10 killed (m1 board
  cut, m2 subject=whole message, m3 nothing-in-scope exit 0, m4 shallow off, m5 root
  below top, m6 absolute --also-exclude unanchored, m9 ROADMAP.md off BOARD, m10
  unmatched --path silent, m11 --no-textconv off, m12 board_shown silent). Survivors:
  m7 (--no-notes dropped from the %B call) and m8 (--end-of-options dropped). Probe for
  m8: `git rev-parse --verify --quiet '<rev>^{commit}'` for --all, -h, --output=… each
  exits 1 without the flag, so the tested inputs cannot distinguish; m7: %B carries no
  notes by git's format contract (not probed live: would write a notes ref).
- RECORD.md HEAD citation "§ The standard child doctrine block": PROPAGATION.md
  headings 84 (## The standard child doctrine block) … fence 133–243 containing a
  literal "## Doctrine — inherited from atelier" at 134 … next ## well after 357. The
  withdrawal account (338) is under § 84, so HEAD's citation reaches the rule and the
  delta's original citation (to the fenced heading) was dangling until 0b29bf4e.
- CHANGELOG.md at HEAD: grep "same turn|no longer ends its turn|two turns" → 0; headings
  exist for 2026-11-20/22, none for the 2026-11-12 reversal. The delta's two-step entry
  stands (line 942) unannotated.
- Gates baseline on the brief: datescan advisory 0; wrapscan and spellscan exempt
  docs/reviews (scan nothing); linkscan clean (0 links).
- NOT RUN: `/security-review` — it reads the session's pending diff; my worktree's
  pending diff is the brief itself plus the partitioned sibling's deletion, which
  REVIEW.md lens 4 says never to scan pre-verdict; the subject is a landed delta.
  Discharged by grounds; code-altitude read done by hand (subprocess list args, no
  shell; --end-of-options; --no-ext-diff/--no-textconv/--no-color; --no-notes; tests
  for ext-diff, textconv, colour, notes, option-shaped revs).
- Left out: the "at least five times" breach count (barred records); live exercise of
  focus mode (no harness control from here); pointerscan's 5 queue-state findings
  (other items, not this delta).

#### Spawn prompt (verbatim; whitespace re-wrapped to 100 columns; one phrase elided and marked)

> You are the cold reviewer (Fable 5.1) for one rule-4 cold review pass in the `atelier` repo,
> which is PUBLIC.
>
> ## Who you are and what you review
> - Item: `atelier:160/1210` (board file
>   `docs/roadmap/160-doctrine-review-owed/1210-rule-4-cold-pass-queued-estate-root-reviewer-side-two-steps.md`).
> - Your review worktree: `/Users/mike/worktrees/fable/atelier-160-1210-2047/atelier`. Use absolute
>   paths and `git -C "/Users/mike/worktrees/fable/atelier-160-1210-2047/atelier"`; never `cd`
>   (where the brief's commands use `cd tools`, run the equivalent with absolute paths or
>   `-s`/path arguments instead). Paths may contain spaces: double-quote every path in every
>   shell command.
> - The brief:
>   `/Users/mike/worktrees/fable/atelier-160-1210-2047/atelier/docs/reviews/2026-11-09-0238-estate-root-reader-side-two-steps-cold.md`.
>   Read it in full first and follow it: its scope, lenses, re-run list, house rules, barred
>   reading and two-act process. Read `docs/method/REVIEW.md` for the verdict shape. Skip the
>   session-log step of the read order (`docs/sessions/`), as the brief says.
>
> ## Provenance (repeat it in your verdict)
> - You are Fable 5.1, the principal-named review tier, checked at selection.
> - You were spawned by headless per-pass orchestrator session `ec57023b` (Opus 5.5), itself
>   started by drain session `eca14b23` (Opus 5.5). Both are off-tier orchestrators: they hold
>   the context partition, form no finding and write no severity. Neither wrote the brief or the
>   delta; `eca14b23` wrote no brief and started no brief-writer for this pass.
> - The brief bars sessions `9bb1b984`, `74f2b8cd` and `722ac2e2` (with everything `722ac2e2`
>   started). You were not started or instructed by any of them.
> - You run under Mike's drain order of 2026-11-23, verbatim: "Start a fable drain or whatever
>   it is called now. Target 100% of weekly budget by 11.30am NZT todat". It is the approval the
>   brief and item say the pass waits for.
>
> ## The partition
> The brief's `.deferred.md` sibling was removed from your worktree on purpose (it shows as a
> deleted file in `git status`; that is expected, do not restore it). Do not look for it in git
> history (`git show`/`git log -p`/`git cat-file` on that path or its blobs), other checkouts or
> worktrees, scratchpads, `/tmp`, or `~/.claude`. Do not open the other barred records the brief
> lists before act 1 is saved. The orchestrator gives you the held copy's path after act 1 is
> committed.
>
> ## Live systems
> Read-only reads of live systems are allowed as the review needs them (Mike, 2026-11-09,
> verbatim: "reads of live systems is fine as needed, Reviews that need writes should be
> de-priortised"). A read means nothing on the target changes; if a verb's effect is unsure,
> treat it as a write. NO live writes of any kind: no push, no write to GitHub, no network
> service changed. A check that would need one is marked NOT RUN with the reason. Allowlist
> fields before printing (provider reads can carry credentials); never dump a user, key or
> certificate object raw; leave no captures in scratch.
>
> ## Load (Mike's instruction: keep this [machine size elided] laptop from crashing; several
> passes run at once)
> Check `uptime` first. Run any test suite under `nice -n 10`, one suite at a time, single
> process (no xdist, `-n auto` or parallel runners), foreground with a long timeout. Prefer the
> targeted tests a finding actually needs over the whole suite; run the brief's full-suite line
> once, niced. Use `/usr/bin/python3` where you have no reason to use another (macOS has no
> `timeout`); the brief's re-run list names `python3` on PATH, so note which interpreter and
> version you used. Never run an installed tool by bare name from PATH: use `tools/<x>.py` or
> `instruments/<x>` from your worktree. Probes use scratch copies and synthetic fixtures under
> your own scratchpad, deleted when you finish.
>
> ## Review log (required)
> Mike, 2026-11-16, verbatim: "The main reason I prompted this earlier in the session is a
> review must have irrefutable integrity to promote trust in the reviwers verdict. So its
> reasoning and methdology are as important as its verdicts. Within the realms that calude will
> allow noting the model extraction limitations". And: "Once a review is complete all its work
> should be open and readable if it could be useful or affect the integrity or quality of the
> review".
>
> Keep a running work log at `/Users/mike/.claude/fable-drain/notes/atelier-160-1210-2047.md`,
> the one file outside the brief you may write. Commands, files and evidence only. As you work,
> append: each step you took (the command run, or the file and line range read) and what it
> showed; each candidate finding with that evidence and the rule or requirement it breaks; and
> each item you checked and found sound, with that evidence. Record the method too: what you
> examined, in what order, for which lens, and what you left out and why. Enough detail that
> someone else could repeat the steps and reach the same verdict. It is the audit trail of the
> review and what you read first if you are interrupted; the verdict itself goes only in the
> brief. No secrets or live captures in it. Write act 1 entries before the sibling is released.
> The log stays private while the pass runs and is appended verbatim to the review at the fold,
> so it is public then: same public-repo rules as the brief (below). Where the harness or model
> will not let part of the method be written, say so in the log as `AUTONOMY.md` § *A limit the
> tooling imposes is managed, never fatal* describes, and carry on.
>
> ## What you may write
> Only the brief file (plus the log above):
> - Act 1 below a `---` divider, in the shape the brief's Process section sets (finding prefix
>   `RW`).
> - Update the brief's Status line to say the pass ran (never "fold-in owed").
> - Keep the file's own column width (≤ 100), absolute ISO 8601 dates from `date -u`, NZ
>   English. Verbatim source text that a gate would flag takes a `datescan:allow` or similar
>   marker; never edit a quote. Before finishing each act, run the repo's own commit gates on the
>   brief from your worktree (`tools/datescan.py`, and the spell/wrap/link scanners if present,
>   the way `tools/README.md` says) and fix your own text until clean. The sibling link will show
>   as broken while the partition holds; that is expected.
>
> ## What you must not do
> No commit, no push, no `git add`, no edits to any other file. No GUI apps. Never print a
> secret or personal data. Exercise tools on scratch copies or fixtures only.
>
> ## Public repo
> atelier is public: a push cannot be retracted. Refer to orchestrators by session id only.
> Never write a session NAME, a private repo's name or path, a worktree path under the home
> folder that names a private repo, or any estate fact. Child repos are reported by count only.
> Do not join the estate root's name to what it holds (the brief's own rule).
>
> ## Rulings are not yours, and you never wait
> The work is doctrine by function: record every finding, apply nothing; every finding is the
> principal's to decide (rule 3). Counsel per finding is welcome, labelled as counsel. Do not ask
> anyone questions; if something needs the principal, record it as an open question in the
> verdict and carry on.
>
> ## How to finish
> Act 1: append the verdict, save, then end your reply with: verdict, tally, the brief path, and
> the exact line "ACT 1 SAVED". Then STOP and wait; the orchestrator commits act 1 and then
> messages you with the held sibling's path. Act 2 (only after that message): read that one file
> and the barred records, write `### Reconcile` beneath your verdict as the brief says (never
> revise act-1 text), update the log, and end with "ACT 2 SAVED". Do not fold the sibling into
> the brief or delete anything yourself; the orchestrator does the fold. If you hit a
> usage-limit error, stop and say so.

The barred-set choice was the brief's own (its *Deferred reading* list), unchanged by the
orchestrator. No release message had arrived when act 1 was written.

- 21:27Z Act 1 appended to the brief below a `---` divider; Status line updated to "PASS RAN".
  Gates on the brief: datescan clean (545 lines read); wrapscan/spellscan exempt docs/reviews;
  linkscan clean; every line of my text ≤ 100 characters (the claims table was converted to a
  list to keep the width). Scratch probes deleted ($S/mut, mutate.py, v2count.sh); the
  coldsweep --commit captures and sweep.txt kept in scratch until the pass ends.
- Verdict: PASS-WITH-FINDINGS — 1 MAJOR (RW1), 2 MODERATE (RW2, RW3), 3 minor (RW4–RW6),
  3 note (RW7–RW9).
- 21:27Z Re-run 4 result: `nice -n 10 python3 -m unittest discover -s tools` → Ran 3382 tests
  in 1068 s, FAILED (failures=1): test_wrapscan.BoundedMemory
  .test_peak_memory_does_not_scale_with_many_line_file_size, "scan did not finish in time"
  (a wall-clock timeout; load average 22.8 during the run, several passes on the machine).
  Re-run alone, niced: `… -p test_wrapscan.py -k BoundedMemory` → Ran 2, OK, exit 0 (33 s).
  wrapscan is not in the delta; recorded as load, not a defect. Ledger row updated before
  act 1 was handed over (act 1 not yet committed).

#### Act 2

- 21:3xZ Orchestrator message: act 1 committed as 81356fbd; sibling released at
  ~/.claude/fable-held/atelier--2026-11-09-0238-estate-root-reader-side-two-steps-cold.deferred.md.
  Read it whole (16 questions, 3 facts). Read `git log -1 --format=%B` for 0ba1ba03, e76250cf,
  47e8345f, 0b29bf4e, 9485b577. Read the eight barred intent records (cut at 200 cols; 020/030 to
  line 400). Read only the finding paragraphs DS1/5/9/11/12, BF1–5/9/10/15, DR1/3/9, C5R3/9, RR2, <!-- datescan:allow: finding IDs, not dates (verbatim log) -->
  CH1 in their verdict files (grep -A3/-A4).
- Probes for the sibling's questions: Q3 grep "never by name|by local-path convention" over live
  surfaces → PROPAGATION.md:336 only. Q8 grep -i "read everything" → SKILL.md:77 only. Q13 six
  --path spellings against 978008c7 → barred .deferred.md never shown, closing line names it each
  time; GIT_CONFIG_PARAMETERS="'diff.noprefix=true'" → prefixes dropped only. Q14 436273ba → 2 of
  12 files shown, 10 board files named as left out, exit 0. Q15 diff of coldsweep's diff section
  vs `git diff 0ba1ba03^1 0ba1ba03` (blank lines removed) → identical.
- Reconcile written beneath the verdict: RW1–RW9 stand; RW3's lens-1 remark corrected in part
  (the picked option carried "one extra turn"); RW10 note formed at reconcile (hand-up PR titles
  at CLAUDE.md step 6 are a pre-brief read not on the inventory). Overall line restated:
  PASS-WITH-FINDINGS, 1 MAJOR / 2 MODERATE / 3 minor / 4 note. Nothing of act 1 revised.
- Gates: datescan clean; every line of my text ≤ 100 characters. Scratch captures
  (commit-*.txt, sweep.txt, ut-*.txt, raw/cs diffs) remain in the session scratchpad only.
