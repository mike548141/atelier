# Cold pass — the DA rulings applied — reached-him wording, pointer-ised copies, one folded paragraph

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/270-rule-4-cold-pass-queued-decision-asks.md`.
**Why it earns a review:** this is the rule every session follows before asking
the principal to decide anything; the DA cycle found the previous wording
produced the exact extracted-approval shape it forbids, so the application is
the fix to a live governance defect.

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

- `2b21a56` (2026-08-23) — the landing commit

Delta paths:

- `docs/method/COMMUNICATION.md` — § *Asking for a ruling* moved below the
  worked example; the reached-him wording; the pointer-ised opener; the folded
  *Make the ask valuable* paragraph carrying the principal's verbatim
  calibration
- `docs/method/00-APEX.md` — the withholding clause, pointer-ised
- `docs/method/AUTONOMY.md` — the floor-stop sentence, pointer-ised
- `docs/method/REVIEW.md` — rule 3's duty spelling, pointer-ised
- `docs/method/EVIDENCE.md` — the scanner-delta measurement line (⚠️ the scanner
  that line measures, `plainscan`, was **removed** on 2026-09-18 by
  separately-queued work; whether the line still describes a runnable
  measurement at HEAD is in scope)

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the four pointer-ised copies now say *less* than the canonical section
and point at it, or whether any still carries a second original (count the
duty's parts on every surface at HEAD — the DA cycle's MODERATE was a
three-vs-five mismatch). Whether "reached him" is a condition a session can
verify in the harness it actually runs in — test it against the display modes
you can observe in this session, and say what you could and could not observe.
Whether the folded paragraph carries the principal's calibration *verbatim* or
paraphrased. **Non-goal:** the DA rulings themselves.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   applied wording rests on a claim about what a session can *know* about
   whether its account reached the principal — attack that: is the rule now
   satisfiable, or has it traded a false claim for an unverifiable one? Consider
   whether moving the section below the worked example changed what a first-time
   reader meets first.
2. **Correctness & quality.** Diff `2b21a56`. For each pointer-ised surface,
   check the pointer resolves (`linkscan`), names the right section, and that
   the surface's remaining text does not contradict the canonical one. Check the
   EVIDENCE line against the tree at HEAD.
3. **Completeness / harvest.** Search for every other statement of the duty's
   parts — `skills/`, `docs/build/templates/CLAUDE.md`,
   `docs/method/PROPAGATION.md`'s inlined child floor, `session-open-prompt.md`.
   The 2026-08-22 work (`160/290`) and the 2026-09-18 work (`160/310`) touched
   neighbouring bullets in the same files; review this delta's surfaces at HEAD
   and name where a neighbour's edit changed the reading.
4. **Security & privacy** — mandatory. Doctrine prose; no code surface. The
   privacy question is whether the folded verbatim calibration or the worked
   example carries anything personal into a PUBLIC repo — read them for that.
   Discharge the house scanner by grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/linkscan.py --root . docs/method` and `python3
  tools/pathscan.py --root . docs/method` at HEAD (lift the exact floor
  invocations from `tools/floor.py`)
- the floor on both planes at HEAD
- the EVIDENCE measurement line: attempt to reproduce it verbatim and record
  what happens

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
`docs/roadmap/160-doctrine-review-owed/270-rule-4-cold-pass-queued-decision-asks.md`
(it carries the author's own lens hints), and:

- the verdict `docs/reviews/2026-08-22-0031-decision-asks-cold.md` (DA; its §
  *Rulings — 2026-08-23* is this delta's intent record)
- `docs/sessions/2026-08-19-0257-asking-for-a-ruling-the-device-and-the-verified-basis.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/270-rule-4-cold-pass-queued-decision-asks.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `DR`: `DR1`, `DR2`, …) and severities (MAJOR / MODERATE
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

# Verdict — phase 1 (written 2026-09-25T07:15Z)

## Provenance, repeated

- **Spawned by:** the batch orchestrator (`claude-fable-5-1`), with this brief as my only
  framing. I am not the author's session; the author neither started nor instructed me. The
  orchestrator held the `.deferred.md` sibling outside the worktree and formed no finding.
- **Tier:** Fable, `claude-fable-5-1`, checked at spawn against the tier the principal names.
- **Read, in order:** this brief; `docs/method/REVIEW.md` and `00-APEX.md` at HEAD; the
  landing commit's diff restricted to the five doctrine paths (the pointer hunk unopened);
  the five paths at HEAD; `tools/floor.py` templates, `.githooks/pre-commit`,
  `.github/workflows/ci.yml`, `.atelier-floor.json`, `tools/blockscan_map.json`;
  `docs/method/PROPAGATION.md`'s floor region and `docs/build/templates/CLAUDE.md`'s stamp
  region; `docs/method/session-open/session-open-prompt.md`; `skills/` (grep only);
  `CHANGELOG.md` lines 95–130 (the entry for this delta — not a barred store); board item
  `320/250` (surfaced by `coldsweep`, not the queue pointer, read in full — it carries a
  child's framing and quotes the delta's own wording, disclosed below).
- ⚠️ **Exposure, disclosed — a rule-2 breach of my own making.** My first `plainscan`
  sweep used a hand-written record exclusion instead of `coldsweep`; its `./` prefix did not
  match what `grep -r` emits on this platform, so the sweep ran wide open and printed eight
  `docs/SESSIONS.md` index entries (2026-08-09 to 2026-09-18, including the DA run's own
  one-paragraph summary and the 2026-08-19 session's) and one line of the barred queue
  pointer. This is the exact class REVIEW rule 2 records three prior instances of. What it
  handed me beyond the brief's own disclosures: the DA pass's finding counts, its
  scanner-delta figure, and a board reference for an unwatched-channel item. My findings
  below were formed from the delta and my probes; the reader should weigh DR1 and DR2 with
  that margin in view. Every sweep after it went through `coldsweep` with the brief's
  `--also-exclude` list (347 files barred).
- ⚠️ **Context I arrived with:** the harness loaded a user-level auto-memory index whose one-line
  entries include a 2026-08-19 note that the decision device is a standing rule and that
  "focus mode hides mid-turn text". That is the delta's own premise, met before the brief.
- **A harness-documentation probe** ran as a `claude-code-guide` subagent, instructed to read
  none of this machine's repos. Its report is data; I corroborated its central claims myself
  (re-run ledger, items 9–10).

## Per-lens answers

### Lens 1 — approach & assumptions

Load-bearing assumptions, named by me: (a) a session can tell which branch of the corrected
rule it is in — plain case or "display mode hides mid-turn text"; (b) "a completed message
before the ask" is a thing a session can produce and still put the device; (c) the
pointer-ised copies say strictly less than the apex; (d) the apex list is the *only*
original of the duty's parts on every surface, including the ones that leave the repo.

**(a) is false, and it is the one the fix rests on — DR1.** Verified against the harness's
own documentation: `/focus` "shows only your last prompt, a one-line summary of tool calls
… and the final response" and "persists across sessions"; the model has no runtime access to
that state (an open issue asks for it to be exposed even to the statusline). So the rule as
written offers two branches and no way to choose between them from inside the session. A
session that follows the text as printed takes the plain case, and under focus mode that is
DA1's shape — a device on screen with its account somewhere the principal cannot see.
The false claim ("on screen while he decides") is gone, which is a real improvement; what
replaced it is a *conditional* the session cannot evaluate. Satisfiable, yes — but only by
treating the exception branch as the rule, which the text does not say.

**(b) holds, with a cost the rule does not name.** The only "completed message" a session
can produce is the turn's final message; the device then goes in the *next* turn, which
exists only after the principal sends something. That is a two-turn ask, and nothing in the
paragraph says so. A second harness fact bears on the plain case too: in the VS Code
extension the question dialog covers the assistant message beneath it with no way to read
that text while the dialog is open (open issue, re-run ledger item 10) — so "in the same
reply, ahead of the device" is not reliably visible even outside focus mode.

**(c) holds on the four surfaces the delta touched** — each carries zero parts and a pointer
(count under lens 2). **(d) does not hold — DR2.** The child floor's *Always stop and
confirm* bullet still restates the account as three parts, and it is the copy every child
stamps.

**Moving the section below the worked example** (DA6, ruled — a non-goal as a decision):
what a first-time reader meets first is unchanged (the calibration practice), and "the visual
axis above" still resolves upward. The one effect worth naming: the italic *Bearing* line
that closed the file is now mid-file, and the ruling-ask section reads as an appendix after
a closing note (DR5, note).

### Lens 2 — correctness & quality

Diffed `2b21a56` on the five paths. **Parts of the duty counted on every surface at HEAD:**

| Surface | Parts stated | Form |
| --- | --- | --- |
| `00-APEX.md` list (lines 135–147) | 5, plus the verified-basis paragraph | canonical |
| `00-APEX.md` withholding clause (line 106) | 0 — "the account owed below" | pointer |
| `AUTONOMY.md` floor stop (lines 112–117) | 0 — "the full account that section owes" | pointer |
| `REVIEW.md` rule 3 (line 139) | 0 — "the apex's full plain-language account" | pointer |
| `COMMUNICATION.md` opener (lines 207–209) | 0 — link + section name | pointer |
| `COMMUNICATION.md` *Make the ask valuable* | principal's verbatim quote + scaling clause | see DR3 |
| `PROPAGATION.md` floor, *Asking* bullet | options with pros/cons/impacts/risks/costs, recommendation, verified basis | aligned 2026-09-18 (`a134270`) |
| `PROPAGATION.md` floor, *Always stop and confirm* | **3** — what, why, likely impact | **second original — DR2** |
| `docs/build/templates/CLAUDE.md` stamp | identical to the two rows above | same |
| `session-open-prompt.md` line 99 | none — names the device only | principal's own prompt |
| `skills/` | no statement of the duty found | — |

Pointers resolve: `linkscan` clean in both the brief's form and the registry's whole-tree
form; the section names quoted on AUTONOMY and REVIEW are the exact heading; COMMUNICATION
quotes the heading's first clause only, which still resolves by eye and by `blockscan`'s map
(`--check` clean at HEAD). No remaining text on the four pointer-ised surfaces contradicts the
apex. **EVIDENCE line:** it names no scanner, so it still describes a runnable shape at HEAD;
its grounding instance is archived (DR4, with the reproduction in the ledger). **Quality:** the
landing commit widened `00-APEX.md:106` to 87 columns and the gate passed it — a scanner
false negative, not a doctrine defect (DR6).

### Lens 3 — completeness / harvest

Every other statement of the duty's parts, found by `coldsweep` over 510 files: the two
child-floor copies (DR2) and nothing else — `skills/` carries none, the session-open prompt
names the device without the account (DR7). **Where a neighbour's edit changed the reading:**
`1d19729` (2026-08-22, `160/290`) wrote the *Asking* bullet into the child floor one day
before this delta; the delta then reworded the canonical section without moving that
bullet, so for 26 days the propagating copy carried the wording DA1 overturned —
`320/250` filed it from a child on 2026-08-26 and `a134270` (2026-09-18) aligned it.
`blockscan` did not exist at the landing; run at `2b21a56` with a map trimmed to the bullets
that existed then, it reports three co-change violations for this commit (ledger item 7) —
two on the *asking* bullet, since fixed, and one on *stop-and-confirm*, still open. `c38b7da`
(2026-09-20) touched REVIEW's preamble and AUTONOMY's who-acts list only; neither changed the
reading of a pointer-ised sentence. Harvest: the delta's own paragraph carries a content rule
the apex lacks (DR3). One surface the doctrine's examples do not name: a spawned subagent has
no device at all (DR8).

### Lens 4 — security & privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff, which in
this shared worktree is other passes' unstaged drafts, and this is a landed-delta review of
markdown — a file class its exclusions bar anyway, so its clean pass would be definitionally
empty. Hand read, design altitude: the delta is doctrine prose with no code surface, input
path or trust boundary; OWASP catalogue classes do not apply. Privacy: the folded verbatim
calibration is one sentence of the principal's working preference with a spelling slip
preserved — no health, family, financial or estate detail; the worked example names the
*categories* it scrubbed (health, workload, household), not their content, under ADR 0005's
named-worked-example framing; `leakscan` clean on both planes (structural + local on the
hook plane). Nothing personal travels. The one privacy-adjacent observation is mine, not
the delta's: the exposure disclosed under provenance.

## Findings

### DR1 · MAJOR — the corrected rule conditions on a display mode the session cannot observe

`COMMUNICATION.md` lines 229–234: "in the plain case it goes in the same reply, ahead of the
device — and where the harness's display mode hides mid-turn text … it goes in a completed
message *before* the ask". The two child-floor copies (`PROPAGATION.md` lines 133–137 and
the template) carry the same conditional. Verified: focus mode shows only the final
response and persists across sessions; the model has no way to read that state at runtime
(ledger 9–10). A session cannot pick the branch, so the printed default is the plain case,
and under focus mode the plain case is the extracted-approval shape DA1 rated MAJOR. The
fix removed a false claim and installed an unevaluable condition. Two aggravations: the
"completed message" branch is a two-turn ask the text does not describe, and in the VS Code
extension the dialog covers the preceding message even in normal mode (open issue, ledger
10), so the plain case is unreliable there too.

*Counsel (the principal's call):* make the completed-message form the rule whenever the
account outgrows the device — "the account goes in a completed message; the device goes in
the next turn and carries the choice alone" — and drop the display-mode condition, or keep
it only as the *reason*. State the two-turn cost plainly. Land the same wording in the
child block and the template in the same commit (`blockscan` now guards that pairing on the
CI plane).

### DR2 · MODERATE — the child floor's *stop-and-confirm* bullet still restates the duty as three parts

`PROPAGATION.md` floor region, *Always stop and confirm*: "the agent puts what it wants to
do, why, and the likely impact in plain language first … an approval given without that
account is open to challenge"; `docs/build/templates/CLAUDE.md` stamps the identical text.
That is the what/why/impact spelling this delta retired from `00-APEX.md` and `AUTONOMY.md`,
surviving on the one surface copied into every child. DA2's class — a duty's sibling
spellings drifting when one is corrected — for the fourth time, and `320/250` (2026-08-26)
already showed the propagating copy is where this class is hardest to see. `blockscan` run
against the landing commit flags exactly this bullet (ledger 7).

*Counsel:* pointer-ise it the way the four in-repo surfaces were — "give the full account
`00-APEX.md` owes, in plain language, first" — in both files, one commit.

### DR3 · minor — a content rule lives on the channel surface, with no apex counterpart

*Make the ask valuable*: "the account scales to the decision, so a small clarification owes
only the parts that exist for it". That is a rule about what an ask must **contain** — the
half the section's own opener assigns to the apex — and the apex has no scaling clause (its
only narrowing is "where only one option is real, say that"). A reader of the apex alone owes
five parts on every clarification; a reader of COMMUNICATION owes a scaled set. Reconcilable
("parts that exist"), so minor, but it is a second original on the surface the delta was
meant to clear of them. The same paragraph's "outranks a tool's own more conservative usage
notes" is a precedence claim about an unnamed note I could not verify — the device is absent
in this harness (DR8).

*Counsel:* keep the verbatim quote here; move the scaling sentence to the tail of the apex
list, or point at it from there.

### DR4 · note — the EVIDENCE measurement line survives as a shape; its grounding instrument is archived

`EVIDENCE.md` lines 187–189 name no scanner, so the line is true at HEAD for any `--json`
scanner. Reproduced verbatim with the archived engine (ledger 8): totals 163 → 167 (+4), and
the per-finding view shows −1/+5 — one finding *swapped* on the rewritten APEX clause, which
the total hides. The line's claim demonstrated on the commit that wrote it. Two notes: the
line carries no grounding pointer, against EVIDENCE's own convention; and the delta's new
paragraphs added three long sentences and one bracketed aside under the scanner that was
then warn-only — a gate nobody read, which is why it was removed on 2026-09-18.

### DR5 · note — the *Bearing* closer is now mid-file

After DA6 the italic "*Bearing: the live instance is …*" line sits between the worked
example and the ruling-ask section, so the section reads as an appendix after a closing
note. Placement is ruled; this records the reading effect only.

### DR6 · note — wrapscan passed the delta's 87-column line (tool finding, off-delta)

`00-APEX.md:106` is 87 columns since `2b21a56`; `wrapscan` reports clean at a limit of 85
because `_is_single_unbreakable_token_overflow` exempts any line whose final *word* straddles
the limit — here the "unbreakable token" is "the". A raw count finds 50 lines over 85
columns on the scoped surface with zero reported (ledger 11); part of that is headings and
marker padding, the single-token share not separated. Points at `tools/wrapscan.py`.

### DR7 · note — the queue-run prompt names the device without the account

`docs/method/session-open/session-open-prompt.md:99` (the principal's own prompt) says to
ask "with AskUserQuestion … mid-turn or between turns". A mid-turn ask is DA1's shape under
focus mode. Not a defect of this delta — the principal's text — recorded so he knows the
last thing a queue-run session reads before working carries no reached-him clause. The
`pathscan` advisory on that file's line 15 predates this delta and is unrelated.

### DR8 · note — a spawned subagent has no device at all

Observed in this session: `AskUserQuestion` is not among my tools (ToolSearch found nothing).
The doctrine's "where no device exists" examples name a non-interactive run and a scheduled
batch; the subagent — the commonest shape under queue-run orchestration — is unnamed, and its
ask travels *through an orchestrator*, which neither branch describes.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR / 1 MODERATE / 1 minor / 5 note.** Per `REVIEW.md` § *Applying
decisions to doctrine*, a MAJOR keeps the cycle open: the application of DR1 earns its own
queued pointer. Nothing applied here; every finding is the principal's to decide.

## Re-run ledger

1. `python3 tools/floor.py --plane hook --root <worktree>` — exit 0; advisories: sizescan ×2,
   pointerscan ×1 (`160/380`, not this delta), pathscan ×1 (session-open prompt line 15).
2. `python3 tools/floor.py --plane ci --root <worktree>` — exit 0; the same advisories plus
   secretscan's 22 entropy advisories, none on the delta's paths; leakscan structural-only on
   this plane by design.
3. `python3 tools/linkscan.py --root <worktree> docs/method` — clean, exit 0; registry form
   (`--root <worktree> <worktree>`) — clean, 4 allow-markers, exit 0.
4. `python3 tools/pathscan.py --root <worktree> docs/method` — 1 finding (session-open prompt
   line 15), exit 1; registry form with `--warn` and the six scoped paths — same finding,
   exit 0. Not on the delta.
5. `python3 tools/coldsweep.py <pattern> --root <worktree> --also-exclude ×3` — eleven
   patterns (duty parts, device names, "focus mode", "reached", "on screen while",
   "per-finding"); 347 files barred each run. Hits summarised under lens 2's table.
6. `python3 tools/blockscan.py --check --warn --root <worktree>` — clean at HEAD, exit 0.
7. `blockscan --against 2b21a56^ --warn` in the scratch clone at `2b21a56`, HEAD's tool, map
   trimmed to the five bullets that existed then (the sixth, added 2026-08-24, made the
   untrimmed map exit 2 config-stale) — 3 co-change violations: `asking` ×2 (APEX section,
   COMMUNICATION section), `stop-and-confirm` ×1. Same tool at `a134270` — clean.
8. EVIDENCE line reproduced verbatim: archived engine from tag `archive/plainscan-2026-09-18`
   over the five paths at `2b21a56^` and `2b21a56` (control: all five snapshot files differ;
   a first attempt compared a directory with itself and was discarded) — 163 → 167 findings;
   per-finding −1/+5, keyed on path, rule and excerpt.
9. Harness documentation, primary: `code.claude.com/docs/en/fullscreen.md` — `/focus` "shows
   only your last prompt, a one-line summary of tool calls with edit diffstats, and the final
   response … persists across sessions".
10. `gh api repos/anthropics/claude-code/issues/{95368,50894,67509}` — all exist: #95368 open
    (expose focus-mode state to the statusline — i.e. not exposed); #50894 closed (focus mode
    hides substantive assistant messages); #67509 open (VS Code dialog covers the assistant
    message it refers to).
11. `awk` count of >85-column non-code, non-table lines on wrapscan's scoped surface — 50;
    `wrapscan` on `00-APEX.md` alone and on the isolated line 106 — clean, exit 0.
12. `ToolSearch select:AskUserQuestion` in this session — no such tool.
13. Not run: the full Python suite (no code changed in the delta; the floor's selftests and
    scanners were exercised instead).

## Follow-up checklist

- [ ] DR1 — ruling on the reached-him wording: unconditional completed-message form, or keep
      the branch with the two-turn cost stated; apply to `COMMUNICATION.md`, the child block
      and the template in one commit; queue the rule-4 pointer for the application.
- [ ] DR2 — pointer-ise the *stop-and-confirm* account clause in `PROPAGATION.md` and the
      template.
- [ ] DR3 — decide the home of the scaling clause.
- [ ] DR4 — add a grounding pointer to the EVIDENCE line, or leave as a shape (note).
- [ ] DR6 — board item on `tools/wrapscan.py`'s final-word exemption.
- [ ] DR7, DR8 — the principal's awareness; a one-clause addition for the subagent case if
      he wants it.
- [ ] Reviewer's own: the rule-2 sweep breach above is a fourth instance of the class REVIEW
      rule 2 counts; it belongs in the record even though `coldsweep` was available and the
      brief said to use it.

### Reconcile

Written 2026-09-25T07:20Z, after phase 1 was committed unrevised (`d317681`). Opened, in
this order: the sibling's text (by message from the orchestrator), then the DA verdict
`docs/reviews/2026-08-22-0031-decision-asks-cold.md` from § *Findings* to the end, including
§ *Rulings — 2026-08-23*, then the intent record
`docs/sessions/2026-08-19-0257-asking-for-a-ruling-the-device-and-the-verified-basis.md`.
Phase-1 text above is unrevised.

**The seeded question** — *does the applied wording tell a session in the final-message-only
mode what to do, or does it still assume the account is visible beside the device?* Both,
and that is DR1. The wording tells a session that *knows* it is in that mode what to do (a
completed message before the ask); it does not tell a session how to know, and no session
can (ledger 9–10). So the plain case still assumes visibility, and the plain case is the
printed default. DR1 was formed from the harness documentation before the sibling was
opened; the seeded question is narrower than the finding — it asks about the mode-aware
session, where DR1's point is that no session is mode-aware — and the convergence
strengthens rather than seeds it. The applied wording is a **faithful** application of the
DA1 ruling as recorded: *"reached-him wording … same-reply stays the plain case where the
harness shows it"*. DR1 is therefore a finding on the ruled shape, not on the applier's
fidelity, and it takes the rule-3 form the apex allows: a challenge on the **briefing**, never
on the authority. DA1's counsel — the briefing the ruling rested on — proposed "keeping the
current same-reply shape as the plain case and naming display modes as instance detail"
without stating that the session cannot observe the mode; the DA verdict does not carry
that fact anywhere. The challenge is raised to the principal by re-briefing (this verdict)
and asking again. Two points from the DA record bear on severity and stay it at MAJOR: (i)
DA-R2 already noted that the widget is "the one surface guaranteed visible at decision time
in every display mode", and the applied paragraph does mark the owed recommendation inside
it — so the *recommendation* survives focus mode, but what/why/impacts/options and the
verified-or-assumed marks (the DA sibling's Q4, folded into DA1) do not; (ii) the principal's
verbatim steer asks for the device "rather than leaving question in the session text alone
(easy to miss)" — DR1's counsel is one branchless rule, which is the less engineered shape,
consistent with that steer.

**Per finding against the intent records:**

- **DR1** — not anticipated; not ruled against. See above. The DA verdict's Q1 (its own
  sibling) asked whether the fix was "a wording change (send the account, *then* end the
  turn / confirm receipt) or a rule the harness cannot currently honour" — the applied
  wording is the first; DR1 says the branch that keeps the second alive is the defect.
- **DR2** — not anticipated. DA2 named three copies and recorded its sweep as "confirmed
  complete by coldsweep over live surfaces"; the ruling pointer-ised exactly those three.
  The child-floor *stop-and-confirm* wording dates from `dce5078` (2026-07-14) — it existed
  at DA2's sweep and was missed, most likely because its spelling ("what it wants to do,
  why, and the likely impact") does not match the "what/why/impact" shape DA2 searched.
  A sweep gap in the prior pass, not a rejection; the ruling's intent (one original, four
  pointers) plainly extends to it. DA2's own reconcile records the class as the
  2026-07-14 pass's AS8/F4 recurring — DR2 makes it the fourth occurrence.
- **DR3** — partly anticipated. The scaling sentence is DA-R5's ruled application ("every
  clarification formally owes a five-element account — over-ceremony"), and its home in one
  COMMUNICATION paragraph is the course-set ruling ("corrections plus one paragraph … not
  five scattered clauses"). So the placement is ruled; the second-original consequence
  was not weighed. Counsel revised to fit the ruling: leave the paragraph whole, and add a
  four-word pointer at the apex list's tail ("scaled per COMMUNICATION § *Make the ask
  valuable*") rather than moving the sentence. The "outranks a tool's own usage notes"
  clause is DA3's application, and DA3 quotes the tool's guidance verbatim — grounded in
  the record; my "could not verify" stands only for this harness, where the tool is absent.
- **DR4** — DA-R3 ruled "one line in the evidence practice"; applied faithfully. My
  reproduction confirms the line's claim on the commit that wrote it. One count noted, not
  a finding: the intent record's 48 (23/14/11) is 49 (24/14/11) at `2b21a56^` because
  `1d19729` (2026-08-22) widened the apex list between the two — the DA-R3 "unchanged since
  landing" reads as true at its HEAD.
- **DR5** — DA6 ruled the move; DA6 itself was placement-only. DR5 records the effect of the
  ruled move on the closer line; no change to counsel (none was given).
- **DR6** — not anticipated; off-delta tool finding; unchanged.
- **DR7** — not anticipated. The commission's own words assumed visibility ("give the
  supporting information in the session so its visible while using AskUserQuestion"), which
  is the assumption DA1 falsified; the prompt's "mid-turn or between turns" is the same
  assumption in the principal's standing prompt. Awareness, unchanged.
- **DR8** — adjacent to DA-R4 (the no-device protocol), which the principal ruled **no
  change** with his steer as the answer of record. DR8 stays a note for awareness only;
  counsel withdrawn in deference to that ruling.

**The verbatim question the brief put in scope.** Checked against § *Rulings*: the folded
paragraph's quoted clause is character-for-character the steer's "e.g." tail, spelling slip
included — verbatim, not paraphrased. Dated correctly to 2026-08-23.

**DR9 (formed at reconcile) · note — the paragraph quotes the calibration's tail and calls it
the whole.** *Make the ask valuable* introduces its quote as "the principal's calibration of
this whole rule, verbatim". The steer of record is longer, and its omitted head carries the
two things the tail does not: the *channel* rationale ("rather than leaving question in the
session text alone (easy to miss)") and the anti-ceremony calibration ("over-thinking and/or
over-engineering") that the ruling round made the governing instruction for the whole
application. Both now live only in a review file's rulings section. Accurate excerpt; the
word "whole" overstates it. *Counsel:* either quote the steer in full or say "from the
principal's calibration".

**Prior verdicts on these surfaces**: the DA verdict is the only one the brief named; its
reconcile records the 2026-07-14 informed-principal pass as the origin of DA2's class, which
DR2 continues. No prior verdict anticipates DR1's unobservability point.

**Overall, restated: PASS-WITH-FINDINGS — 1 MAJOR / 1 MODERATE / 1 minor / 6 note** (DR9
added at reconcile). The cycle stays open on DR1; nothing applied.

## Deferred material — folded in at reconcile

# Deferred material — da-rulings-applied (open only after your findings are durably written)

Sibling of `docs/reviews/2026-09-25-0715-da-rulings-applied-cold.md` under
REVIEW.md rule 1's split; held by the orchestrator outside the worktree. Folded
into the brief below the verdict when the verdict lands.

## Intent records

- `docs/reviews/2026-08-22-0031-decision-asks-cold.md` § *Rulings — 2026-08-23*
  — DA1–DA6 and DA-R1–DA-R5 dispositions, including the principal's verbatim
  over-engineering steer. **Not opened by the brief-writer.**
- `docs/sessions/2026-08-19-0257-…` — the delta's original intent record. **Not
  opened.**

## Prior verdicts and barred items on the same surfaces

- the verdict `docs/reviews/2026-08-22-0031-decision-asks-cold.md` (DA; its §
  *Rulings — 2026-08-23* is this delta's intent record)
- `docs/sessions/2026-08-19-0257-asking-for-a-ruling-the-device-and-the-verified-basis.md`

## The queue pointer's own lens hints — the author's seeded questions, verbatim

The pointer carries no lens paragraph — refs only.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

1. The brief-writer's own harness note: this batch runs under a display mode
   that shows the principal only a turn's final message. Does the applied
   wording tell a session in that mode what to do — or does it still assume the
   account is visible beside the device?
