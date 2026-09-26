# Cold pass — the ruling-ask rule widened and pushed to the child floor

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/290-rule-4-cold-pass-queued-ask-rule-to-children.md`.
**Why it earns a review:** the child floor is stamped into every repo the
scaffold creates and every child at pin bump; a bullet that is wrong, or that
drifts from its canonical source, is the widest blast radius the operating model
has.

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

- `1d19729` (2026-08-22) — the landing commit
- `a134270` (2026-09-18) — the widening: the same bullet's
  account-before-the-ask sentence in both files (`320/250`)

Delta paths:

- `docs/method/00-APEX.md` § *The principal's authority is absolute; his rulings
  are conditioned on being informed* — the options bullet, widened to pros /
  cons / impacts / risks / costs / considerations
- `docs/method/PROPAGATION.md` § *Doctrine — inherited from atelier* — the new
  **Asking** bullet in the inlined child floor
- `docs/build/templates/CLAUDE.md` — the same bullet, which the scaffold stamps

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the stamped bullet compresses the canonical rule without narrowing it
(the house's stamped-copies rule), and whether the two copies — PROPAGATION's
floor region and the template — are byte-identical *now that a scanner checks
the floor verbatim* (`stampscan`'s floor branch, landed 2026-09-20 by
separately-queued work `160/340`): run it. Whether the widened options list is
one the principal gave verbatim or an author's gloss (the delta claims the
former; the record it cites is barred until phase 2 — form your own view from
the wording, then reconcile). **Non-goal:** the principal's ruling itself.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   bullet tells a *child* session how to ask its principal; test whether it
   makes sense in a child that has no `COMMUNICATION.md` to point at, and
   whether "pointing up" from a stamped bullet gives a child reader a resolvable
   path.
2. **Correctness & quality.** Diff both commits. Compare the three surfaces word
   by word at HEAD. Check the options list's six nouns appear in the same order
   on every surface and in the apex's canonical bullet.
3. **Completeness / harvest.** Search for every other statement of the ask rule
   that a child might read first: `skills/`, `session-open-prompt.md`,
   `CLAUDE.md`, the `create-repo` skill's stamping instructions. Does the
   scaffold stamp the template's current text, or a cached copy?
4. **Security & privacy** — mandatory. Doctrine prose, PUBLIC repo; check the
   worked wording carries nothing personal. Discharge the house scanner by
   grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/stampscan.py --root . .` at HEAD (the floor's invocation — lift
  it from `tools/floor.py`), and its `--selftest`
- `python3 tools/blockscan.py` if the registry runs it at HEAD, over the delta's
  surfaces
- the floor on both planes at HEAD

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
`docs/roadmap/160-doctrine-review-owed/290-rule-4-cold-pass-queued-ask-rule-to-children.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-08-22-0456-the-ask-rule-reaches-the-children.md` and
  `docs/sessions/2026-09-18-0114-queue-run-hand-up-fixes.md`
- the board items `docs/roadmap/320-*/250-*.md` and any
  `docs/roadmap/*/…da1-overturned.md` item (the hand-up that prompted the
  2026-09-18 widening)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/290-rule-4-cold-pass-queued-ask-rule-to-children.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `AK`: `AK1`, `AK2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1, written 2026-09-25T07:18Z

### Provenance, repeated

- **Spawn.** A fresh Fable subagent (`claude-fable-5-1`), spawned by the batch
  orchestrator with this brief as its only framing. I did not author the delta,
  was neither started nor instructed by its author, and have edited no path but
  this file. The orchestrator forms no finding and writes no severity; it holds
  the `.deferred.md` sibling outside the worktree and releases it only after this
  section is committed. Both seats are Fable, so no off-tier clause is invoked.
- **Tier at claim:** Fable, the tier the principal names (REVIEW rule 4).
- **What I read.** The delta paths at HEAD `c4b9cd0` and the two landing commits'
  diffs *scoped to those three paths only*; `REVIEW.md`, `00-APEX.md`,
  `PROPAGATION.md` §§ the standard child block and the bundled-mode variant,
  `COMMUNICATION.md` § *Asking for a ruling*; `tools/floor.py`,
  `.githooks/pre-commit`, `.github/workflows/ci.yml`, `tools/stampscan.py` and
  `tools/blockscan.py` docstrings, `tools/blockscan_map.json`, `.stampscanignore`,
  `tools/test_templates.py`; `skills/create-repo/SKILL.md`,
  `skills/session-onramp/SKILL.md`, `docs/method/session-open/session-open-prompt.md`;
  the unbarred board item `320/110` that the sweep surfaced. Commit *subjects* for
  the delta surfaces since 2026-08-21 and for `COMMUNICATION.md` 2026-08-22 to
  2026-08-25.
- ⚠️ **Exposure disclosed.** (1) `git show --stat` on both landing commits listed
  the *names* of barred files (SESSIONS.md, two session logs, the queue pointer,
  one 320 item); I opened none. (2) One hand `grep -r` before I switched to
  `coldsweep` mis-filtered on macOS grep's path spelling and its 2 KB preview
  showed three lines of `docs/ROADMAP-DONE.md` (generic 2026-07-22 "accept your
  recommendation" rulings, nothing about this delta) plus headings of unbarred
  board items. The persisted full output was never opened. Every later sweep ran
  through `tools/coldsweep.py` with the brief's `--also-exclude`; its banner
  reports 347 files excluded as barred. No `--include-barred` run was made.
- **Sibling not opened.** It is not in the tree; phase 2 waits on the
  orchestrator's message.

### Lens answers

**Lens 1 — approach and assumptions.** Load-bearing assumptions I name myself:
(a) the floor is the right tier for the ask rule, because a child session meets
the block and nothing prompts it to open `COMMUNICATION.md`; (b) a compressed
bullet with two up-pointers is an honest stand-in for the canonical rule; (c) the
harness always has a question device, or the child knows what to do when it
does not; (d) "the floor" has one stamped shape, so fixing PROPAGATION's region
and the template reaches every first-read surface. (a) holds: `session-onramp`
says the doctrine is read on demand, and only the apex and the confirm floor
bind at start. (b) mostly holds — the pointers `00-APEX.md` and
`COMMUNICATION.md` are bare file names, but so are every sibling bullet's, and
the **Source & drift** bullet three lines down names `<atelier-path>/docs/method/`
(or `<plugin-path>` in bundled mode), so the path resolves for a child; what does
not hold is the list's completeness (AK1). (c) does not hold for a headless
child run — "where one exists" says where to put the ask, not that the content
is unchanged without one; the canonical section has that clause and the bullet
dropped it (AK3). (d) is false: the plugin's `session-onramp` skill inlines its
own apex and floor and was swept for the 2026-08-15 apex change, yet carries
neither the 2026-08-17 informed-confirmation text nor the 2026-08-22 Asking
bullet, and no scanner reads it (AK2). Whether pointing up works from a stamped
bullet: the **Doctrine problems point up** bullet gives a child a resolvable
path (file in atelier's board, peer channel, or hold locally marked owed), and
`320/110` is a live proof that a child used it against exactly this bullet's
subject (AK6). Non-goal accepted: the principal's ruling is not reviewed.

**Lens 2 — correctness and quality.** Both commits diffed. `1d19729` widened the
apex bullet and added the Asking bullet to region and template identically;
`a134270` reworded the account-ordering sentence identically in both copies and
touched the apex not at all. At HEAD the region and the stamped copy are
byte-identical: `stampscan` reports `[identical]` over 91 lines in both the
floor's `--warn` form and the blocking form, and `test_templates` pins the same
fact a second way. The six-item order check the brief asks for **fails on the
sixth**: the apex reads *pros, cons, impacts, risks, costs and any other
consideration that bears on the choice*; both child surfaces read *pros, cons,
impacts, risks and costs* — the first five in the same order, the catch-all
absent (AK1). Nothing is overclaimed in the doctrine text itself; the apex's
parenthetical dates the widening and names its source.

**Lens 3 — completeness and harvest.** Every other statement of the ask rule a
child might read first, by `coldsweep`: `session-onramp/SKILL.md` — none, and
its inlined floor is behind the block (AK2); `session-open-prompt.md` line 99 —
a one-line "ask me with the device when you need a decision; don't ask when
you could find the answer yourself", consistent and thinner, and it routes the
reader to the repo's `CLAUDE.md` first (AK5); atelier's own `CLAUDE.md` — no
bullet, but `00-APEX.md` is item 2 of its read order, which is the canonical
text; `create-repo` — stamps from `$SRC/docs/build/templates/CLAUDE.md` at
scaffold time ("you do not keep a second copy"), so live mode stamps the current
template at the pinned SHA and bundled mode stamps the plugin's bundled tree at
its version (`0.2.0`) — a cached copy by design, pinned, not by accident;
`REPO-STANDARD.md`, `CONTRIBUTING.md` and `README.md` templates — no statement.
Harvest: the `320/110` hand-up already carries the lens-1 gap (AK6); nothing
else is owed a new item beyond the checklist below.

**Lens 4 — security and privacy.** `/security-review` is discharged by grounds:
it reads the session's pending diff, which in this shared worktree is other
passes' drafts, and this is a landed-delta review of Markdown, a file class its
exclusions bar anyway. Hand read: the three surfaces carry a product name
(`AskUserQuestion`), the house's gendered "the principal / him", and no name,
address, health, family or financial fact; the apex's dated parenthetical names
a date and a ruling, not a person. Floor re-run on both planes exits 0 (ledger
below); the hook plane's staged-diff scanners had nothing staged to read, which
is stated rather than counted as cover; the CI plane's 22 secretscan advisories
are the standing tally, none in the delta paths. No code surface, so no OWASP
vector applies. Clean, with that trail.

### Findings

**AK1 — MODERATE — the stamped list closes a list the apex leaves open.** The
apex bullet, which the delta says is the principal's own list, has six items and
ends *"and any other consideration that bears on the choice"*. Both child
surfaces carry the first five and stop. Probe: regex extraction of the
options-list phrase from all three surfaces (`python3` over the files at HEAD)
matches the six-item form only in `00-APEX.md`. The house's stamped-copies rule
lets atelier's canonical block *compress* its source but not contradict it; a
closed list read by a child is an instruction to stop at five, and the missing
item is the one that makes the list non-exhaustive — the same shape as
`foundation Q2` (a pull-quote listing 4 of 6 floor items), which is one of the
three findings `stampscan` cites as its reason to exist. Whether the sixth item
is the principal's or the author's gloss I cannot settle until phase 2 (the
record is barred); the finding stands either way, because the block is meant to
compress the canonical text as it is.
*Counsel:* add the catch-all to both copies in one commit (five words: "and
anything else that bears on the choice"); `stampscan` and `test_templates` will
hold them equal. If phase 2 shows the sixth item was the author's, the fix may
instead be to the apex — the principal's call.

**AK2 — MODERATE — the plugin's onramp skill is a third inlined floor and the
widening did not reach it.** `skills/session-onramp/SKILL.md` §§ 1–2 inline the
apex and the always-confirm floor as the "two things [that] bind from the
start" for a plugin-only adopter. Its § 2 lists the seven floor stops and
nothing else: not the informed-confirmation sentence, not the principal's-
authority sentence (both in the block's stop-and-confirm bullet since
2026-08-17), and not the Asking bullet (2026-08-22). Its history shows the house
treats it as a restatement that sweeps update — `31b2ed0` (2026-07-23, "sweep
in-repo restatements") and `c782e14` (2026-08-15, the dilemma clause) both
touched it — yet neither landing commit here did. It carries no `stamp:begin`
marker, so `stampscan` never reads it; `blockscan_map.json` names only the
region and the template, so `blockscan` never asks it to move. A plugin-only
adopter who follows the skill's own instruction (read the two sections, then
on demand) meets the ask rule only if they happen to open `00-APEX.md`.
*Counsel:* either stamp the skill's § 2 as a copy of the block's floor bullets
(then `stampscan` guards it), or reword §§ 1–2 as pointers to the block with
no restated floor at all. The second is the thin-anchor shape the house
prefers; the first keeps the "binds from the start" promise. Decision owed on
which.

**AK3 — minor — the bullet drops the no-device clause.** The canonical section
says: where no device exists — a non-interactive run, a scheduled batch, a
harness without one — the ask is prose and carries exactly the same content.
The bullet says only "where one exists". A child's queue run or scheduled batch
is the no-device case, and a reader of the bullet alone can conclude the rule
is device-bound. The apex's "where only one option is real, say that, and say
why the others are not" is compressed away too; that one the pointer covers.
*Counsel:* one clause — "; with no device, the same content goes in prose" —
on both copies. Cheap, and it names the case children hit most.

**AK4 — note — the guard now covers this bullet, and it cuts coarser than the
bullet.** Re-driven in my scratch clone with HEAD's `blockscan` and a map
trimmed to the five bullets that existed at the time: at the DA1 rewording
`2b21a56` (2026-08-23) the check reports the two real violations — the apex
section and `COMMUNICATION.md` § *Asking for a ruling* both changed and the
Asking bullet did not move in either copy — which is the incident `a134270`
fixed 26 days later, so the guard would have caught it. The same run also
reports a third violation, and the landing commit `1d19729` reports one of the
same kind: the `stop-and-confirm` bullet "did not move" because it and the
Asking bullet share one apex `###` section. So the next edit to the apex's
options list will red the confirm bullet as well, and needs an allow marker
with a reason. At HEAD `--check` and `--against HEAD^` both exit 0. Wiring is
CI-only, advisory, atelier-only, and `--against HEAD^` compares the tip commit
of a push only — all stated in the tool's own docstring and the workflow.
Belongs to `blockscan`'s own first-of-kind review, not this delta; recorded so
that pass has a probe to start from.

**AK5 — note — a thinner personal statement of the rule exists and does not
contradict.** `docs/method/session-open/session-open-prompt.md:99` is a launch
prompt, not doctrine; it sends the reader to the repo's `CLAUDE.md` first and
its "don't ask when you could find the answer yourself" is the whether-test
`320/110` asks for. `pathscan` warns on its line 15 (`../atelier/...` does not
resolve from atelier's own tree) — pre-existing, warn-only, unrelated.

**AK6 — note — the bullet stamps the *how* of asking and inherits the
canonical section's silence on *whether*.** `320/110` (filed 2026-08-25 from a
private child via § *Pointing up*) records a session that followed the widened
rule to the letter and manufactured decisions out of records. Live evidence
that the widening propagated a shape without a trigger; already on the board
with a candidate house rule, so no new item — the principal's decision there
will need to reach the block too, and `blockscan`'s map already binds
`COMMUNICATION.md` § *Asking for a ruling* to the Asking bullet, so it will red
if it does not. Open until phase 2: whether the five nouns are the principal's
verbatim and the sixth item plus the rationale sentence are the author's gloss —
my reading from the wording alone is that the list is his and the parenthetical
is the author's.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 2 MODERATE · 1 minor · 3 notes.** The two
copies are byte-identical and the scanner that checks that is live and green;
what the stamped bullet loses against its canonical text is one list item and
one clause, and one first-read surface was missed entirely.

### Re-run ledger (HEAD `c4b9cd0`, worktree `/Users/mike/worktrees/atelier-review-batch-0925`)

| Command (lifted from `tools/floor.py`, `ci.yml`, `.githooks/pre-commit`) | Result |
|---|---|
| `python3 tools/stampscan.py --warn --root . .` (CI form) | exit 0 · 1 block identical, 91 lines |
| `python3 tools/stampscan.py --root . .` (blocking form) | exit 0 · same |
| `python3 tools/stampscan.py --selftest` | `selftest OK`, exit 0 |
| `python3 tools/blockscan.py --check --warn --root .` (CI form) | exit 0 · clean |
| `python3 tools/blockscan.py --against HEAD^ --warn --root .` (CI form) | exit 0 · clean |
| `python3 tools/blockscan.py --selftest` | `selftest OK`, exit 0 |
| `floor.py --plane hook --root <wt> --tools <wt>/tools` | exit 0, 12 enforced, 3 warn-only |
| `floor.py --plane ci --root <wt>` | exit 0, secretscan 22 advisory (standing) |
| `unittest discover -s tools -p test_stampscan.py` | 90 tests OK, exit 0 |
| `unittest discover -s tools -p test_blockscan.py` | 20 tests OK, exit 0 |
| `unittest discover -s tools -p test_templates.py` | 44 tests OK, exit 0 |
| `coldsweep` for the five ask-rule phrases (lens 3) | 17 hits / 510 files · 347 barred, excluded |
| scratch clone at `1d19729`: `stampscan --root <clone> <clone>` | exit 0 · identical, 73 lines |
| clone at `a134270`: `stampscan` / `blockscan --against HEAD^ --warn` | exit 0 / exit 0 clean |
| clone at `1d19729`: `blockscan --against HEAD^ --warn --map <5-bullet map>` | 1 violation · AK4 |
| scratch clone at `2b21a56`: same | 3 violations (2 asking, 1 stop-and-confirm) — AK4 |

Not run: the full Python suite (the brief's re-run list does not name it, and
the shared machine allows one run; the three modules that guard this delta ran
in full). Not verified: the state of any child's stamped copy — other repos are
out of bounds for this pass; the delta's own "children are unchanged until each
bumps its pin" is taken as stated, not checked.

### Follow-up checklist (for the principal to rule; nothing applied)

- [ ] AK1 — decide whether the sixth item joins both copies, or leaves the apex.
- [ ] AK2 — decide the shape for `session-onramp/SKILL.md` §§ 1–2: stamped copy
      or pure pointer; then bring it level with the block either way.
- [ ] AK3 — the no-device clause on both copies.
- [ ] AK4 — hand the two scratch probes to `blockscan`'s own review as its
      starting evidence (section granularity; tip-only CI comparison).
- [ ] AK6 — when `320/110` is ruled, the Asking bullet moves with it.
- [ ] Phase 2 — reconcile the provenance of the six-item list against the
      intent record.
