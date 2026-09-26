# Cold pass — the scratch-space clause — a worker's worktree isolates the repo and not the scratchpad

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/380-rule-4-cold-pass-queued-the-scratchpad-clause.md`.
**Why it earns a review:** every orchestrated run in the fleet dispatches
workers under this clause; if the obligation is unenforceable or the measurement
it rests on is wrong, parallel workers keep colliding in the one place no check
can see.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `e9a6aae` (2026-09-20) — the clause landed
- `df2d4e7` (2026-09-20) — the attribution corrected

Delta paths:

- `docs/method/CONCURRENCY.md` § *Orchestrated queue runs* — the paragraph
  following *What a worker inherits is bounded*

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the clause's claim about the harness is true **now, on this machine**:
this batch is itself an orchestrated run with several subagents live, so the
reviewer can measure it — note what scratch directory *you* were given, whether
it is namespaced per agent, and what the orchestrator's is (ask via your report
if you cannot see it). Whether the clause tells a dispatching session something
it can do (what must the dispatch prompt say, exactly) or only something to
worry about. Whether the stated expiry is a condition a future reader can
evaluate. Whether the clause's provenance note earns its place after the
attribution was corrected once. **Non-goal:** the measurement item's commission.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   clause rests on one measurement on one harness on one day; the reviewer's own
   session is a second measurement — take it, and say whether the clause's width
   survives it.
2. **Correctness & quality.** Diff both commits. Check the corrected attribution
   against what the two commits' own diffs show was actually written by whom;
   the pointer discloses the first version rested on an error, so treat the
   correction as a claim.
3. **Completeness / harvest.** Search for every other surface that tells an
   orchestrator what a worker inherits: `skills/queue-run/SKILL.md`,
   `ECONOMICS.md`'s sub-agent criteria, `docs/build/templates/`. Does the
   queue-run skill's dispatch template carry the obligation the clause says the
   prompt must?
4. **Security & privacy** — mandatory. The scratch space holds whatever workers
   write — including, in a review batch, deferred material. Say what the shared
   scratch means for the rule-1 context partition this very batch relies on, as
   counsel. Discharge the house scanner by grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the measurement: record your own scratch path and the presence or absence of
  per-agent namespacing, with `ls` evidence, without reading other agents' files
- `linkscan`, `pathscan`, `wrapscan` over `docs/method/CONCURRENCY.md` at HEAD;
  the floor on both planes

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/380-rule-4-cold-pass-queued-the-scratchpad-clause.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` — ⚠️ the
  brief-writer read its **first 30 lines** (the tier line, onramp, selection,
  and the opening of the `020/390` measurement paragraph — which is this
  clause's evidence) and its last ~3,000 characters (an unrelated PR section)
  during the interrupted-session sweep at onramp. That exposure is disclosed
  here and in the sibling; the reviewer forms its own measurement first
- the board item `docs/roadmap/020-*/390-*.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/380-rule-4-cold-pass-queued-the-scratchpad-clause.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `SK`: `SK1`, `SK2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.

---

## Verdict — phase 1 (written 2026-09-25, 07:10–07:40 UTC)

### Provenance, repeated

- **Spawn.** I am a Fable subagent (`claude-fable-5-1`) spawned by the batch
  orchestrator of `review-batch-0925`, with this brief as my only framing. I am
  not the author's session (the 2026-09-20 queue run, Co-Authored-By a Claude
  Opus 5 session) and was not started or instructed by it. The shape is
  reviewer-plus-orchestrator as the brief discloses; both seats are Fable, so
  the off-tier clause is not invoked. I formed every finding and severity here;
  the orchestrator formed none.
- **Tier at claim:** Fable, checked against the brief's *Tier* line.
- **What I read, in scope:** this brief above the divider; `REVIEW.md` and
  `00-APEX.md` at HEAD; `CONCURRENCY.md` §§ *Integration hygiene*, *Re-run,
  don't reason*, *Orchestrated queue runs* at HEAD `c4b9cd0`; the two landing
  commits' messages, `--stat` file lists (names only) and their
  `CONCURRENCY.md` hunks — `git show` path-filtered so no record hunk was
  shown; `skills/queue-run/SKILL.md`; `ECONOMICS.md` §§ *Sub-agents* and *The
  orchestrated-run tier split*; `EVIDENCE.md` §4; `tools/floor.py` registry;
  `.githooks/pre-commit`; `.github/workflows/ci.yml`; `.atelier-floor.json`;
  `tools/test_templates.py` `QueueRunSkillTest`; the `docs/build/templates/`
  listing. Not opened: the `.deferred.md` sibling, the queue pointer, the
  `020/390` item, any session record, `ROADMAP-DONE.md`, any prior verdict or
  sibling `2026-09-25-0715-*` brief, any other agent's scratch files, the
  orchestrator's scratch files. `--include-barred` was never used.
- ⚠️ **Rule-2 exposure, disclosed in full.** My first tree sweep was a hand
  `grep -rn … | grep -v '^\./docs/(sessions|reviews|roadmap|…)'`, not
  `coldsweep`. On this machine `grep -r … .` emits paths **without** the `./`
  prefix (verified: `grep -rl … .` printed `CHANGELOG.md`), so the exclusion
  matched nothing and the sweep ran wide open — the exact class REVIEW.md rule 2
  records three prior instances of. Single lines containing "scratch" reached
  me from: `docs/SESSIONS.md` (9 index titles); `docs/ROADMAP-DONE.md` (6
  lines); the barred `020/390` item (11 lines: its title and fragments of its
  measurement narrative, which echo the landing commit messages); the barred
  `160/380` pointer (5 lines: its title and two lens-hint fragments — one is
  this brief's own *Scope* question on the expiry, the other echoes *Why it
  earns a review*); `docs/sessions/2026-09-20-1053-…` (11 fragment lines of its
  `020/390` section); ~25 lines across other session records; ~90 lines of
  prior verdicts (mostly "scratch clone" boilerplate) and ~40 identical
  house-rules lines from sibling briefs. Nothing I saw carried a finding or a
  severity about this delta. Two further, smaller exposures: the brief's own
  sanctioned `coldsweep` command excludes `160/380` but not `020/390`, so it
  surfaced four more `390` lines (32, 54, 57, 63 — see SK9); and the floor's
  `pointerscan` prints the first line of the `160/380` pointer on both planes
  (its title, truncated). I formed lens 1 before any of the `380` fragments
  were read back; I record them so the reader weighs them rather than
  discovers them.
- **Scratch discipline.** All writes under my named directory
  `<scratchpad>/SK/` (created empty at 07:09 UTC; nothing else was needed —
  no probe clone, because the delta is prose and every re-run was read-only).
  No git command that writes was run. `/security-review` was not run.

### The measurement — the reviewer's own session as the second data point

Taken at 2026-09-25 07:09 UTC, `ls` names only, no other agent's file opened.

- **What the harness gave me.** My system prompt's *Scratchpad directory* line
  names `<tmp>/<user>/<project>/<session-uuid>/scratchpad` and calls it
  "session-specific, isolated from the project". The `<session-uuid>` in that
  path equals `CLAUDE_CODE_SESSION_ID` in my environment, and
  `CLAUDE_CODE_CHILD_SESSION=1` is set — so a subagent **inherits its parent's
  session id and therefore its parent's scratchpad**, labelled as its own.
- **What the orchestrator's is.** The same directory: its files sit at that
  root beside the reviewers' subdirectories (`gen.py`, `passes.py`,
  `baseline.txt`, five `pre-*scan.txt`, `claim-msg.txt`, `briefs-msg.txt`, a
  `__pycache__/`, and a `siblings/` directory of 20 entries). The orchestrator
  told me in its dispatch message that my area was `<that root>/SK/` — the
  clause's obligation, applied.
- **Per-agent namespacing: none in the scratchpad; some elsewhere.** Seven
  prefix-named subdirectories (`AK DR NP PV RU SK TR`) exist at the root, one
  per live reviewer, all created by the dispatch convention, not the harness.
  The harness *does* key other stores per agent: the session's `tasks/`
  directory holds seven `a<id>.output` symlinks to
  `subagents/agent-<id>.jsonl` transcripts. Per-agent identity exists
  upstream; the scratchpad is not keyed on it. The harness also spills long
  tool outputs into a shared per-session `tool-results/` store (8 files at
  07:12 UTC) — a scratch-class write the worker never chooses a path for.
- **The wider radii, names only.** The per-project parent held only session
  directories (7). The per-**user** parent one level up held ~95 loose files
  dated 2026-09-21 and 2026-09-24 in numbered runs — `commit1…13`,
  `deliverables2…16`, `render2…16`, `c9…c16.log`, `makecheck…` — a session
  hand-disambiguating with numeric suffixes inside a namespace shared by every
  project on the machine: the clause's `msg`/`msgB` pattern, reproduced at
  scale four days after it was written, one level wider than the clause names
  (SK6). The two bare-`/tmp` files the correction rests on (`floor_old.txt`,
  `prop_new.md`) no longer exist at 2026-09-25.

**Does the clause's width survive the second measurement?** Its core claim —
workers get no scratch directory of their own; a named, unique, absolute path
is what separates them — is **confirmed on this harness at 2026-09-25**, and
the naming recipe was followed by seven concurrent reviewers without incident
that I can see. What the second measurement adds is the part the clause does
not say (SK1): the shared directory is a *read* surface as well as a write
one, and this batch keeps its deferred material in it.

### Lens 1 — approach & assumptions

Load-bearing assumptions, named by me before any barred text was met:

| # | Assumption the clause rests on | Status after this pass |
|---|---|---|
| A1 | Subagents share the orchestrating session's scratchpad, unnamespaced | ✅ confirmed 2026-09-25 (measurement above) |
| A2 | Naming a path binds; forbidding writes does not | ✅ supported (7/7 reviewers used their named dir); the forbidding side is n=1 and mechanism-free — SK8 |
| A3 | A "dispatch prompt obligation" reaches the session writing the prompt | ❌ nothing a dispatcher is holding at dispatch time carries it — SK3 |
| A4 | The cwd hazard that grounds *absolute* is recorded at § *Integration hygiene* | ❌ that section carries no such hazard; no live doctrine surface does — SK2 |
| A5 | The harm class is collision and hijack (write/execute) | ⚠️ incomplete: read/confidentiality omitted, and it is the one that bears on rule 1 — SK1 |
| A6 | The expiry ("if the harness namespaces scratch per agent") is evaluable by a future reader | ⚠️ the condition is real; the *test* is unwritten — SK8 |

Right problem, mostly the right instrument: a prompt obligation is the honest
shape while the path is the harness's to allocate, and this batch shows it is
followable. The mis-build is in what the clause leaves out (A5) and in a
grounding that does not resolve (A4).

### Lens 2 — correctness & quality

- **Both diffs read at the CONCURRENCY.md hunks.** `e9a6aae` (2026-09-20
  11:02 UTC) added the clause; `df2d4e7` (11:22 UTC, same session) replaced
  the second bullet and the rule paragraph and added the provenance note. The
  `--stat` lists show both commits also touched the `020/390` item, the
  `160/380` pointer and the 2026-09-20 session record (not opened).
- **The corrected attribution, treated as a claim.** The correction is
  internally consistent with what it removed: the "three files, two into the
  shared parent" instance and the "no diagnosis of why" hedge are gone; the
  "five files, four into bare `/tmp`" instance and "the cwd explanation is
  dead" replace them. Its evidence chain is a transcript check I cannot re-run
  from the tree (transcripts are records outside the repo and I did not open
  them), and the four `/tmp` files are absent at 2026-09-25 — so the corrected
  instance stands on the commit message and the barred records, not on
  anything re-runnable. That is acceptable for a grounded record and I note it
  rather than count it; the two commits agree on who wrote what (the same
  Opus-authored session, twenty minutes apart), which is what the lens asked.
- **One thing the correction changed without saying so:** the level at which
  loose files accumulate moved from "the shared parent directory every
  project's scratchpad hangs off" (per-user, `e9a6aae`) to "that per-project
  parent" (`df2d4e7`, twice at HEAD). My measurement matches the earlier
  wording — SK6.
- **Honesty about done vs stubbed:** good. The clause names its own expiry,
  says what its rule does *not* rest on, and marks the provenance as a
  correction. No overclaim found in the clause's own text.
- **Landing = queuing:** satisfied — the `160/380` pointer file was created in
  `e9a6aae` itself. But the pointer breaks the refs-only ceiling — SK4.

### Lens 3 — completeness / harvest

- `skills/queue-run/SKILL.md` step 5 (*Execute* — the dispatch step) carries
  "worker in its own worktree" and "never overrides doctrine", and nothing
  about scratch. It has no dispatch template. `docs/build/templates/` has no
  dispatch template either, and `QueueRunSkillTest` pins stop conditions, the
  two canonical pointers, the rule-4 phrase and the chain pin — nothing that
  would notice the obligation missing. So the answer to the brief's question is
  **no**: nothing a dispatching session holds at the moment it writes the
  prompt carries the obligation — SK3.
- `ECONOMICS.md` § *Sub-agents* says a sub-agent "buys context isolation";
  consistent with the clause and not duplicated by it.
- The provenance lesson already exists in the same file: § *The channel*, *Re-
  run, don't reason* — "Agreement is not corroboration when the second party
  never opened the source" (line 539 at HEAD) — and `EVIDENCE.md` §4 carries
  the general rule; board item `200/090` is already collecting this class.
  The clause restates it at line 813 — SK5.
- Coldsweep over the live surfaces (`dispatch prompt`, `worker inherits`,
  `cwd`): the obligation lives in exactly one place, and the cwd hazard in
  none but the clause's own two lines — SK2.

### Lens 4 — security & privacy

**`/security-review` is discharged by grounds:** it reads the session's pending
diff, which in this shared worktree is other passes' unstaged drafts, and this
is a landed-delta review of doctrine prose with no code surface. The
code-altitude read is therefore empty by construction — the delta has no
input path, no execution, no secret handling; OWASP categories do not attach.
Design altitude is where the lens bites:

- **Threats enumerated for the class "shared scratch directory":** (T1) a
  worker *reads* material the run is holding from it; (T2) a worker executes a
  peer's same-named script; (T3) a worker stomps a peer's file; (T4)
  harness-side shared stores the prompt cannot reach (`tool-results/`); (T5)
  bare `/tmp` is machine-wide. The clause answers T2, T3 and T5. It does not
  name T1 or T4. T1 is the finding: **SK1**.
- **Counsel on the rule-1 partition this batch relies on** (asked for by the
  brief): on this harness the deferred siblings are held in the directory the
  harness hands every reviewer as its own, with no permission prompt between a
  reviewer and `cat siblings/<file>`. The partition therefore holds by the
  reviewers' discipline plus the transcript's audit trail — the same strength
  REVIEW.md rule 1 assigns to the file split, not the "structural" strength it
  assigns to the orchestrator-held shape. Nothing in this batch breached it
  that I can see (I did not open the directory); the point is what it *is*.
- **Privacy of the delta itself:** the two `/tmp` file names are generic; no
  path with a username, no person, no secret enters the clause. Clean.
- **Privacy of this verdict:** scratch paths are described generically; no
  session id, username or machine path is quoted.

### Findings

**SK1 — MAJOR — The shared scratch space is a read surface, and the doctrine's
"structural" context partition sits inside it.** Evidence: my harness-given
scratchpad is the orchestrator's; it contains `siblings/` (20 entries) — the
deferred material for this batch's twenty passes — readable by any reviewer
with no prompt. REVIEW.md rule 1 calls the orchestrator-held partition "the
one arrangement that may honestly be called structural"; on the harness the
clause measures, it is not. The clause under review is the doctrine's account
of what the scratch space is, and its harm model stops at write and execute
collisions ("one worker committing another's work"); the omission is the
threat that bears on the doctrine's own highest-stakes review shape, in the
very run that reviews it. *Counsel:* (a) one sentence in the clause — the
shared scratch is a read surface too, so an orchestrator holding material a
worker must not see does not hold it under the scratchpad it hands out; (b)
REVIEW.md rule 1's "structural" qualified: structural only where the deferred
bytes never sit on a path the reviewer is given — otherwise "strong default
with an audit trail", which is the honest name for every disk-held shape on a
same-user machine; (c) this batch's record says where the siblings were held.

**SK2 — MODERATE — The *absolute* leg cites a section that does not carry its
grounding.** The clause grounds *absolute* "on the independently-observed cwd
hazard (§ *Integration hygiene*)". That section at HEAD holds sync bookends,
verify-the-act, append-tail conflicts, record identifiers, value absorption
and worktree hygiene — nothing about a working directory reverting under a
session. A coldsweep of the live doctrine surfaces for the hazard finds only
the clause's own two lines. The landing commit says the hazard was "recorded
three times here"; wherever those records are, they are not doctrine, and a
section-name cross-reference is invisible to `linkscan` and `pathscan` (both
clean). *Counsel:* either land the hazard as a bullet under § *Integration
hygiene* with its instances, or drop the cross-reference and ground *absolute*
on the argument that needs no incident: a relative path resolves against a cwd
the worker does not control.

**SK3 — MODERATE — The obligation reaches no dispatching hand.** "The dispatch
prompt says so" — but the queue-run skill's dispatch step does not say so, no
dispatch template exists, and no test would notice. The clause also gives
properties (explicit, unique, absolute) and no recipe, so each orchestrator
re-derives one. This batch's recipe worked and is one line:
`<orchestrator scratchpad>/<worker-name>/`, the worker creates it, the
orchestrator uses a named subdirectory of its own. *Counsel:* add the sentence
to `skills/queue-run/SKILL.md` step 5 (its header permits compressing the
parent, never contradicting it) and the recipe to the clause; a parity pin in
`QueueRunSkillTest` is optional and cheap.

**SK4 — MODERATE — The pass's own queue pointer breaks rule 4's refs-only
ceiling, and the floor only warned.** `pointerscan` flags
`160/380` line 1 "[grammar] instructs the reviewer" on both planes at HEAD;
`df2d4e7`'s message says the correction commit made "160/380's review lenses
now tell the reviewer" what to treat as a claim; the brief-writer records that
the pointer carries the author's lens hints and moved them to the sibling. I
did not open the pointer — the scanner, the commit message and the brief are
the evidence. Rule 4 makes the pointer "a ceiling as well as a floor: refs
only"; the author's framing rode it from 2026-09-20 until a non-author
intercepted it. *Counsel:* fix the pointer's grammar in the application
commit; and for the class, a landing session runs `pointerscan` on the pointer
it writes — warn-only is the right wiring, but the author is the one reader
who can act on the warning for free, and did not.

**SK5 — minor — The provenance paragraph does not earn its nine lines.** Its
lesson is already doctrine in the same file (§ *The channel*, line 539) and in
`EVIDENCE.md` §4, and the class has a board home (`200/090`). A dispatching
orchestrator — the clause's reader — needs none of it. The correction *is*
worth a trace. *Counsel:* one line — "the attribution was corrected once
(2026-09-20); the lesson is § *The channel*'s *agreement is not
corroboration*" — and the instance moves to `200/090` or `EVIDENCE.md`.

**SK6 — minor — The accumulation radius is named one level too narrow.** HEAD
says "per-project parent" twice; the loose files I observed (~95, numbered
runs, two dates) sit in the per-**user** parent, and the per-project parent
held only session directories. `e9a6aae` had the wider wording; `df2d4e7`
narrowed it in passing. *Counsel:* restore "the per-user parent every
project's scratchpad hangs off"; it is the wider surface and the true one.

**SK7 — minor — The orchestrator half of the obligation was not met by this
batch's orchestrator.** Its scratch sits at the scratchpad root — the same
root every worker is handed — while workers got subdirectories. A worker that
writes at root, or runs Python there, shares that `__pycache__` and those
files. The clause says an orchestrator "uses one too" without saying that the
root it already owns does not count once it is shared. *Counsel:* "under a
named subdirectory of its own, never the scratchpad root".

**SK8 — note — Two claims stated at more strength than their evidence.**
(a) "Naming binds; forbidding does not" rests on one forbidden worker; and a
named path does not reach the writes a worker never chooses — `mktemp`,
Python's `tempfile`, and the harness's own `tool-results/` spill — so the
honest reading is "naming reduces; nothing eliminates". (b) The expiry is a
real condition without a written test. *Counsel:* write the test into the
clause: compare a subagent's harness *Scratchpad directory* line (or
`CLAUDE_CODE_SESSION_ID`) with its parent's — equal means shared, and at
2026-09-25 they are equal while transcripts are already keyed per agent, so
the rule is one upstream change from spent.

**SK9 — note, on the brief — The sanctioned sweep does not bar everything the
section bars.** *Deferred reading* lists the `020/390` item; the `coldsweep`
command `--also-exclude`s only `160/380`. Run verbatim, it surfaced four `390`
lines. *Counsel to the brief template:* every path the section lists gets an
`--also-exclude`; and add the `./`-prefix instance above to rule 2's count.

### Overall

**PASS-WITH-FINDINGS** — 1 MAJOR (SK1) · 3 MODERATE (SK2, SK3, SK4) · 3 minor
(SK5, SK6, SK7) · 2 notes (SK8, SK9). The clause's core claim is confirmed by a
second measurement and its recipe is followable; what is wrong is what it
omits (read surface), what it cites (a section that does not carry the
hazard), and where it lives (nowhere a dispatcher is standing).

### Re-run ledger

| Claim / obligation | Command (from the registry, hook, ci.yml) | Result |
|---|---|---|
| Measurement: my scratch path, namespacing | `ls -la` of the scratchpad root, session dir, `tasks/`, per-project and per-user parents; `env` names; names only | shared with orchestrator; 7 prefix dirs; `siblings/` = 20; transcripts per agent; parents as above |
| `/tmp` evidence files | `ls -la /tmp/floor_old.txt /tmp/prop_new.md` | both absent at 2026-09-25 07:13 UTC |
| linkscan over CONCURRENCY.md | `python3 tools/linkscan.py --root <wt> <wt>/docs/method/CONCURRENCY.md` | ✅ clean, exit 0 |
| pathscan over CONCURRENCY.md | `python3 tools/pathscan.py --warn --root <wt> <wt>/docs/method/CONCURRENCY.md` | ✅ clean, exit 0 |
| wrapscan over CONCURRENCY.md | `python3 tools/wrapscan.py --root <wt> <wt>/docs/method/CONCURRENCY.md` | ✅ clean (85-col budget), exit 0 |
| Floor, hook plane | `python3 tools/floor.py --plane hook --root <wt> --tools <wt>/tools` (`.githooks/pre-commit` line 103) | exit 0; 11 ✅ enforced; warn-only: sizescan 2 size-advisory (ROADMAP.md, SESSIONS.md), pointerscan 1 grammar (`160/380` — SK4), pathscan 1 missing-path (`session-open-prompt.md`, pre-existing, not the delta) |
| Floor, ci plane | `python3 tools/floor.py --plane ci --root <wt>` (`ci.yml` line 304) | exit 0; secretscan 22 advisory (expected tier); leakscan 🟡 structural-only (by design on ci); same three warn-only findings |
| coldsweep ×4 (`dispatch prompt`, corroboration, `worker inherits`, cwd) | `python3 tools/coldsweep.py --root <wt> --also-exclude <380> [--also-exclude <390>] <pattern>` | 347 files barred each run; hits as cited in lenses 2–3 |
| Full Python suite | not run — the delta is prose with no code or test surface; the brief's re-run list does not name it; one heavy process at a time on a shared machine | — |
| `/security-review` | not run — discharged by grounds (lens 4) | — |

`date -u` bounds: 07:09:57 UTC (scratch dir created) to 07:15:21 UTC (floor
ci plane finished).

### Follow-up checklist (for the principal's ruling; nothing applied)

- [ ] SK1 — rule on the read-surface sentence for the clause and the
      "structural" qualifier for REVIEW.md rule 1; record where this batch
      held its siblings.
- [ ] SK2 — land the cwd hazard under § *Integration hygiene* or drop the
      cross-reference.
- [ ] SK3 — one sentence in `skills/queue-run/SKILL.md` step 5; the recipe in
      the clause.
- [ ] SK4 — fix the `160/380` pointer's grammar in the application commit.
- [ ] SK5 — shrink the provenance note to a pointer; instance to `200/090`.
- [ ] SK6 — "per-user parent".
- [ ] SK7 — "named subdirectory, never the root" for the orchestrator.
- [ ] SK8 — write the expiry test into the clause; soften "binds".
- [ ] SK9 — brief template: `--also-exclude` every listed path; rule 2 gains
      the `./`-prefix instance (this pass, 2026-09-25).
- [ ] Phase 2 — reconcile against the sibling on receipt.

### Reconcile (written 2026-09-26, 14:18–14:35 UTC)

**What was opened at reconcile, and only then:** the sibling's text as sent by
the orchestrator; `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`
lines 1–107 (the `020/390` section); the `020/390` item in full; the `160/380`
pointer in full. Phase-1 text above is unrevised.

**A fact I was told, and what of it I checked.** The orchestrator reports that
on reading SK1 it moved the twenty siblings and the batch toolkit out of the
shared scratchpad into a user-local directory outside the harness's scratch
path. Verified by listing at 2026-09-26 14:18 UTC: `siblings/`, `gen.py` and
`passes.py` are absent from the scratchpad root (the other orchestrator files
remain there; the root also shows 21 prefix directories — a second wave landed
on the same shared root). Not verified: the new location's contents — the
harness set my phase-2 working directory *inside* that new siblings directory,
so I know its path without having listed it. That last detail is itself
evidence for SK1's counsel (b): a store the reviewer is not *given* can still
reach the reviewer as a path through the harness's cwd inheritance, so no
disk-held shape on a same-user machine is structural; the relocation removes
the trap of the harness labelling the store as the reviewer's own, which is
the material improvement, and leaves the arrangement a strong default with an
audit trail. The cwd change under me mid-pass is also a live instance of the
hazard SK2 says is recorded nowhere in doctrine.

#### Against the pointer's four lens hints (the author's seeded questions)

1. *Is a prompt obligation the right instrument when no check can see a
   worker's scratch writes, given `370`?* Anticipated by nothing in phase 1
   as a question; answered by SK3 and SK8 in substance. My answer: the right
   instrument **for the allocation** (the path is the harness's), the wrong
   *placement* (SK3 — nowhere a dispatcher stands), and not the only check
   available — see SK10, formed here.
2. *Is the expiry a real condition a future reader can evaluate, or an escape
   hatch?* Anticipated: SK8(b). Real condition, unwritten test; with the test
   written into the clause it is evaluable in one command and stops reading as
   a hatch.
3. *Is the grounding strong enough for the claim's width — one harness, one
   machine, one day?* Anticipated: lens 1 and the measurement. A second
   measurement five days later on the same harness, 7 then 21 concurrent
   agents, confirms the core claim; the width stays one harness, and the
   clause's own scoping ("the harness's to allocate") is honest about that.
   The intent record's "no per-agent namespacing at any depth" (line 27) is
   what I found too.
4. *Does the provenance note earn its place; treat the corrected attribution
   as a claim.* Anticipated: SK5 and lens 2. Reading the record: the full
   sequence (lines 45–106, including a real cost — two of a third session's
   files deleted on the wrong attribution, one not reconstructable) lives in
   the intent record and the item already, so the clause's paragraph is a
   *third* statement of it and § *The channel* line 539 a standing fourth.
   SK5 stands; the record is the right home and holds more than the clause
   does. The corrected attribution: the record's chain (peer's transcript
   check, third session, five files) is consistent with `df2d4e7`'s message
   and with the item; still not re-runnable from the tree; I take it as a
   claim recorded honestly, not as a fact restored — which is what the hint
   asked.

#### Against the brief-writer's question

1. *Siblings moved from the worktree into the scratchpad — from one reachable
   place to another?* **Yes**, and this is SK1 exactly, formed before the
   question was read. The move defeated the tree-wide-grep vector and created
   a worse one: the harness told each reviewer that directory was its own.
   The orchestrator's mid-batch relocation (above) closes the labelling trap;
   it does not make the partition structural, and REVIEW.md rule 1 should
   stop saying it is (SK1 counsel b).

#### Per finding, against the intent records

- **SK1** — not anticipated. The record and item treat the shared scratch as a
  collision surface only; confidentiality of what an orchestrator holds there
  does not appear. Stands, MAJOR.
- **SK2** — corroborated. The record says the cwd hazard is one "this estate
  has recorded three times" (line 84) — the estate, not this repo's doctrine
  — and that it "recurred during this very measurement"; it recurred again for
  me at phase 2. The clause's § *Integration hygiene* citation still resolves
  to nothing. Stands, MODERATE.
- **SK3** — not anticipated. The item's *Owed* line offered "say in the
  dispatch doctrine" and the run said it in `CONCURRENCY.md` alone; the skill
  was never in view. Stands, MODERATE.
- **SK4** — confirmed on opening the pointer: lines 11–23 are evaluative lens
  hints, and lines 26–36 the claim block. `df2d4e7`'s message shows the hints
  were added deliberately as a feature, not seen as a ceiling breach. Stands,
  MODERATE.
- **SK5** — anticipated as a question (hint 4), answered against the author's
  position ("kept because the correction is the lesson"). Stands, minor.
- **SK6** — confirmed by the record itself: the `msg*` files sat in "the
  directory every project's scratchpad hangs off" (line 33 — per-user), while
  the two wrongly-attributed files sat in the "per-project scratchpad parent"
  (item line 42). The clause at HEAD puts the `msg*` run in the per-project
  parent, which is the conflation `df2d4e7` introduced. Stands, minor.
- **SK7** — not anticipated; the record describes the same shape in the
  author's own run (a worker's tree "landed beside the orchestrator's own
  `claim-msg.txt`", lines 27–29) as the *measurement*, never as the
  orchestrator's own obligation unmet. Stands, minor.
- **SK8** — (b) anticipated by hint 2; (a) not. Stands, note.
- **SK9** — the sibling confirms the brief-writer never opened `020/390`; the
  omission was in the sweep command, not the intent. Stands, note.
- Checked and dropped: the record names a private child repo (lines 58, 100)
  in this public tree; a count-only grep finds the name in 51 files including
  `docs/method`, established since 2026-07-11 — no finding.

**SK10 — note — formed at reconcile — A check *can* see scratch writes, at
the orchestrator's close.** Hint 1 assumes no check can reach them. The
orchestrator owns the root every worker is handed; one `ls` of that root after
a wave, against the set of names it dispatched, shows every write that escaped
a named directory — § *Integration hygiene*'s own "verify the act, not the
absence of an error", applied to scratch. It reaches neither bare `/tmp` nor
the harness's `tool-results/`, so it is partial; but it turns the obligation
from unenforced into checked-at-close for the radius that matters most, and
`370`'s class shrinks by one. *Counsel:* one line in the clause and in the
queue-run skill's per-item close.

**Overall, restated:** **PASS-WITH-FINDINGS** — 1 MAJOR (SK1) · 3 MODERATE
(SK2, SK3, SK4) · 3 minor (SK5, SK6, SK7) · 3 notes (SK8, SK9, SK10). No
phase-1 finding withdrawn or re-graded at reconcile; one note added.

## Deferred material — folded in at reconcile

# Deferred material — scratchpad-clause (open only after your findings are durably written)

Sibling of `docs/reviews/2026-09-25-0715-scratchpad-clause-cold.md` under
REVIEW.md rule 1's split; held by the orchestrator outside the worktree. Folded
into the brief below the verdict when the verdict lands.

## Intent records

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` — the run's
  account of the measurement and of the attribution error. **Partially read by
  the brief-writer** (see the brief's barred list); the measurement's core claim
  — three workers wrote into the orchestrator's single scratchpad with no
  per-agent namespacing — was seen.
- `docs/roadmap/020-*/390-*.md` — the item that asked for the measurement. **Not
  opened.**

## Prior verdicts and barred items on the same surfaces

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` — ⚠️ the
  brief-writer read its **first 30 lines** (the tier line, onramp, selection,
  and the opening of the `020/390` measurement paragraph — which is this
  clause's evidence) and its last ~3,000 characters (an unrelated PR section)
  during the interrupted-session sweep at onramp. That exposure is disclosed
  here and in the sibling; the reviewer forms its own measurement first
- the board item `docs/roadmap/020-*/390-*.md`

## The queue pointer's own lens hints — the author's seeded questions, verbatim

**The lenses that matter most here:** whether a prompt obligation is the
right instrument at all when no check can see a worker's scratch writes,
given `370`'s own finding that an unenforced rule is the class this
estate keeps re-breaking; whether the clause's stated expiry — spent if
the harness namespaces scratch per agent — is a real condition a future
reader can evaluate, or an escape hatch; and whether the grounding is
strong enough for the claim's width, given that the measurement covers
one harness on one machine on one day; and whether the clause's retained
provenance note earns its place, given that the artefacts it rests on
were **wrongly attributed for about an hour and the first published
version of the clause rested on that error** — the reviewer should treat
the corrected attribution as itself a claim to check, not a settled fact
restored.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

1. This batch's orchestrator moved every `.deferred.md` sibling **out of the
   worktree into the session scratchpad** before spawning, on a memory that a
   reviewer's tree-wide grep otherwise reaches them. If the clause is right that
   the scratchpad is shared, that mitigation moved the siblings from one
   reachable place to another. Say whether that is so.
