# Cold pass — the pointing-up rulings applied — the check shows paths, and the instance is named

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/280-rule-4-cold-pass-queued-pointing-up-rulings-applied.md`.
**Why it earns a review:** the concurrency trigger's prescribed check is the
first command every session runs at a dirty checkout, and the pointing-up
section is stamped into every child at pin bump; a wrong command or a mis-named
instance propagates fleet-wide.

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

- `2489f12` (2026-08-22) — the landing commit

Delta paths:

- `docs/method/CONCURRENCY.md` § *The trigger* — the prescribed check is now
  plain `git diff --cached`, with the correction note; the *Bearing* names the
  child repo
- `docs/method/PROPAGATION.md` § *Pointing up* intro and § *The instance* — the
  veil dropped on the principal's ruling, with the class-rule-stands note
- board items `docs/roadmap/310-*/030-*.md`, `310-*/050-*.md`, `310-*/100-*.md`,
  `310-*/110-*.md`, `docs/roadmap/210-*/110-*.md` — the backlog findings
  boarded, and the shed note aligned

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether `git diff --cached` alone does what § *The trigger* now says it does
(run it in a scratch clone with staged, unstaged, untracked and intent-to-add
states and compare against what the sentence claims a reader learns). Whether
naming a private child repo by name in a PUBLIC doctrine file is the ruled
outcome or an over-application of it — the class-rule-stands note is the
author's claim about that; test it. Whether the five boarded items say what the
verdict's `[backlog]` tags say they should (compare the items' text to what the
doctrine at HEAD now promises). **Non-goal:** the PU rulings themselves.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   correction note says the old command was wrong in a specific way — reproduce
   the old command from the diff and show whether it was. Ask whether a
   *correction note* inside doctrine is the right home for history, or whether
   the record stores are.
2. **Correctness & quality.** Diff `2489f12`. Check every path and section
   reference in the delta resolves at HEAD; check the *Bearing* is dated and
   attributes the incident without quoting anything the child's privacy needs
   held back.
3. **Completeness / harvest.** Search for every other surface that still
   prescribes the pre-correction command or names the instance the old way:
   `docs/build/templates/CLAUDE.md`, the inlined child floor in PROPAGATION,
   `skills/session-onramp/SKILL.md`, `CLAUDE.md`. The 2026-08-24 work
   (`160/300`) and the 2026-09-20 work (`160/360`) later rewrote neighbouring
   paragraphs of § *Pointing up*; name where a neighbour's edit changed this
   delta's reading.
4. **Security & privacy** — mandatory. atelier is PUBLIC and the instance names
   a private child. The security and privacy lens here is exactly the veil
   question: what does the named instance now expose about that child's layout,
   tooling, or contents that the veiled form did not? Read the section for that,
   and say whether anything crosses the no-private-detail line the house holds
   for its records. Discharge the house scanner by grounds in one line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the `git diff --cached` probe in *Scope*, in a scratch clone, with each state
  recorded
- `linkscan` and `pathscan` over `docs/method` at HEAD, floor invocations
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
`docs/roadmap/160-doctrine-review-owed/280-rule-4-cold-pass-queued-pointing-up-rulings-applied.md`
(it carries the author's own lens hints), and:

- the verdict `docs/reviews/2026-08-21-0820-pointing-up-cold.md` (PU; its
  verdict and ruling tags are this delta's intent record). ⚠️ The brief-writer
  read that file's **brief section only** (lines 1–80, as a formatting template)
  — not its verdict
- `docs/sessions/2026-08-22-0107-pointing-up-rulings-applied.md` and the
  2026-08-22 entries in `docs/SESSIONS.md`
- the board section README `docs/roadmap/310-*/README.md` (carries the
  2026-08-18 ruling)

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/280-rule-4-cold-pass-queued-pointing-up-rulings-applied.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `PV`: `PV1`, `PV2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1, written 2026-09-25 UTC

### Provenance (repeated, per rule 4)

- **Spawned by:** the batch orchestrator (`claude-fable-5-1`) that wrote this brief, with
  the brief as my only framing. I am not the author of `2489f12`, was neither started nor
  instructed by that session, and have edited none of the delta's paths. Shape:
  reviewer-plus-orchestrator, both seats Fable; the off-tier clause is not invoked.
- **Tier:** `claude-fable-5-1`, checked at spawn.
- **Read before writing this:** the brief; `docs/method/REVIEW.md` and `00-APEX.md` in
  full; `CONCURRENCY.md` § *The trigger* in full (lines 26–124) and the file's headings;
  `PROPAGATION.md` § *Pointing up* in full (lines 393–689) and the file's headings; the
  diff of `2489f12` restricted to `docs/method/`, `docs/roadmap/310-*`, `210-*` and
  `docs/ROADMAP.md`; the five board items at HEAD plus the first 30 lines of `310/050`
  (its ruling summary, which is the delta); board items `320/190` (lines 100–165),
  `320/330`, `320/350`, `320/250` (lines 55–80); `CHANGELOG.md` lines 1–12 and 155–172
  plus greps; `CLAUDE.md` lines 12–30; grep lines of `docs/build/templates/CLAUDE.md`
  and `skills/session-onramp/SKILL.md`; `.githooks/pre-commit`, `ci.yml`, the registry
  entries in `tools/floor.py`; the history of `CONCURRENCY.md` (`f9eda42` and its
  parent's text) and of `PROPAGATION.md` (`5bb78f2`, `48c181f`).
- **Barred material:** none opened. Two incidental exposures, disclosed: (1) my first
  `coldsweep` run omitted `--also-exclude` for `docs/roadmap/310-*/README.md`, so three
  of its lines printed as hits (a repeat of item `040`'s quotation and the block's
  compressed phrase) — I did not open the file; (2) `git show 2489f12` printed the
  commit *body*, the author's account of the rulings. Rule 2 does not bar a commit
  message, but it is author narrative and I read it before forming findings.
- **Not run:** the full Python suite — the delta has no code surface; the registry floor
  ran on both planes instead (ledger below). No scanner was pointed outside the
  worktree or my scratch clone.

### Per-lens answers

**Lens 1 — approach & assumptions.** Load-bearing assumptions, named by me: (A) plain
`git diff --cached` shows every staged entry with its path; (B) the old pipe was wrong
*in the way the correction note says*; (C) § *The instance*'s account of the incident
still holds once the command is corrected; (D) a correction note inside doctrine is the
right home for the history. (A) holds — probe, ledger item 1: six staged entries across
content, empty-new-file, pure-rename, mode-only, binary and a stale staged-then-edited
path all print with `diff --git` path lines; intent-to-add and untracked paths do not,
and a dry-run commit confirms neither would be committed, so the sentence claims exactly
what the command delivers. (B) holds and understates: the reproduced old command
`git diff --cached -U0 | grep '^@@'` printed **two hunk headers for six staged paths and
no path at all** — four of the six entries (empty file, rename, mode change, binary)
produce no `@@` line, so the old check did not merely strip paths, it silently omitted
whole staged entries. (C) **fails** — PV1. (D) is in-style: the house already keeps
dated in-place corrections (`REVIEW.md` rule 1's "this rule previously said…",
`PROPAGATION.md`'s "the count read seven until…"), and the record stores hold the
narrative; the note's form is a house pattern, not a novelty. Its residue is PV4. One
known limit of the check itself is already boarded and not this delta's to answer:
`320/350` (2026-09-20) shows a peer can stage *during* the commit's hook window, which
"immediately before every commit" cannot close; the delta neither created nor claimed to
close it.

**Lens 2 — correctness & quality.** The diff matches the brief's account: one command
corrected with a dated note, the *Bearing* and two `PROPAGATION.md` sites named, five
board items written or aligned. Every section and path reference in the delta resolves
at HEAD: § *The trigger*, § *The channel* (`CONCURRENCY.md:437`), § *Stay in your lane*
(`:591`), § *The standard child doctrine block* (`PROPAGATION.md:75`), § *The instance*,
items `040`, `020`, `310/100`, `310/110`, `210/110`, `160/280`, `tools/floorfleet.py`,
`tools/pins.py`, and the PU brief file (exists; unopened). The *Bearing* is dated
(incident 2026-08-18, ruling 2026-08-22) and attributes the incident as a git-index event
and a destroyed session-log entry — no host, path, client or secret. The PU-2 note's
claim that item `040` quotes the principal naming the repo is true (`040` lines 3–4).
Ragged wrapping after the insertions (PV4). Honest about what is done: the three
`[backlog]` items are written as open items, not as fixes.

**Lens 3 — completeness / harvest.** The pre-correction command survives as a
*prescription* nowhere: `docs/build/templates/CLAUDE.md:72–74` and the inlined child
floor at `PROPAGATION.md:160–162` both say plain `git diff --cached` and "the paths you
did not stage"; `CLAUDE.md:22` points at § *The trigger*; `skills/session-onramp/
SKILL.md` carries no command. The old pipe appears only as history (`CONCURRENCY.md:86`,
`310/030:11`). "A private child" as the *instance's* veil survives at none of the three
sites; the phrase now appears at `PROPAGATION.md:607` as the wording of a *rule*, a
different sense. The ten children of `310/030` are outside this worktree and were not
swept; that item's hand sweep is still unrun, with one child reported clean as of
2026-08-26 (`320/250`). Neighbours: `5bb78f2` (2026-08-24, `160/300`) retitled the
section, added § *The duty* and the three filing shapes — it widened the section around
the instance without touching the instance's reading; `48c181f` (2026-09-20, `160/360`)
added the every-surface naming precedence, and that one **did** change this delta's
reading — PV2. `54201e0` (2026-09-18) applied `310/110`'s wording in step 3. The
`[backlog]` tags check out: `310/100`, `310/110`, `210/110` say what `310/050` says they
should, and all three have since closed with the fix visible at HEAD (three shapes at
`PROPAGATION.md:498–517`; step-3 wording at `:547–548`; `--git-common-dir` at
`tools/pins.py:128`). The application has no `CHANGELOG.md` entry — PV3.

**Lens 4 — security & privacy.** `/security-review` is discharged by grounds: it reads the
session's pending diff, which in this shared worktree is other passes' unstaged drafts,
and this is a landed-delta review. The delta has no code surface, so the OWASP catalogue
has nothing to bear on; the read is design-altitude only. The veil question: the commit
names one child at three doctrine sites, which the commit body and `310/050` both record
as the ruled outcome (three sites, not one) — it is the ruling applied, not
over-applied. What the naming exposes beyond the veiled form: the repo's name, and
that it runs parallel sessions in a shared checkout and keeps session logs. Nothing
else — no host, path, client, tooling or contents. The name was already in the public
tree before this commit: item `040`'s title and its quotation of the principal,
`310/030`'s ten-child list, `210/100`'s per-repo percentages, and `320/060`–`130`'s
"filed from" lines. The forge does not resolve the name under the owner's account,
consistent with `010/030`'s own note that the repo has no remote; I write nothing
further about it. Nothing in the delta crosses the no-private-detail line the house
holds for its records. What has moved since is the *rule*, not the exposure — PV2.

### Findings

**PV1 — MODERATE.** *§ The instance and the `CONCURRENCY.md` Bearing still say the house
had no gap; the corrected command says it did.* At HEAD, `PROPAGATION.md:641–651` reads:
the child "read its own block, which compresses the house rule to *read the staged hunk
headers*… The house had no gap. `CONCURRENCY.md` § The trigger says to run `git diff
--cached`, which reads the whole index… Its sibling rule was in the parent verbatim.
Nothing was owed upstream at all." The Bearing (`CONCURRENCY.md:118–120`) says the child
"concluded the house had a gap it does not have". Re-driven against history: the text in
force on 2026-08-18 (`f9eda42^`, `CONCURRENCY.md:84–85`) prescribed
`git diff --cached -U0 | grep '^@@'` and "compare the hunk headers" — so the block's
phrase was a *faithful* compression of the parent's own command, not a lossy one, and
the probe shows that command prints no path and drops four of six staged entries. The
"whole index, not your own hunks" clause the narrative leans on was added *by* `f9eda42`
on the day of the incident, in response to it. PU-1 then corrected the command on
2026-08-22 — and the same commit left the instance narrative untouched, so the two
doctrine files now disagree about one event: `CONCURRENCY.md:86` says the old sentence
"strips exactly the paths at issue"; `PROPAGATION.md:647` says the house had no gap. The
child's *route* was still wrong (a local duplicate instead of a filing) and the block's
pointer was still wrong, so the section's lesson stands; its grounding instance
overstates. Under the apex that is a rounded account in the one place the section is
"extracted from evidence".
*Counsel (the principal's to decide):* re-word § *The instance* paragraph 3 and the
Bearing's "a gap it does not have" to say the house owned the rule but prescribed a
path-blind command for it (corrected 2026-08-22, PU-1), and that what the child owed
upstream was *that finding* — which is the route the section teaches — not a duplicate
rule. Two sentences; the lesson gets stronger, not weaker.

**PV2 — minor.** *The PU-2 note's "stands unchanged" is now the seam of a live, boarded
contradiction, and the doctrine gives no reader that fact.* The note at
`PROPAGATION.md:634–635` says "the class-never-specifics rule for what a *child files
upward* stands unchanged". Since then `48c181f` (2026-09-19 ruling, `320/190`) widened
that rule to "every surface the filing creates… outranks any rule about how to name
one", and § *Report without harming the parent* now says "a private child says *'a
private child'* and nothing more" (`:607`). Ninety lines above that sentence the same
section names a private child three times. `320/330` is an open 🎯 asking whether the
precedence reaches doctrine's own prose and notes it would partly overturn PU-2. The
delta is not at fault — its note was true when written and is literally still true — but
a reader at HEAD meets the naming as settled and the rule as absolute, with no pointer
that the principal has the question in front of him. Formed on the neighbour's edit, not
on the delta.
*Counsel:* apply nothing until `320/330` is ruled. Whichever way it goes, record the
sweep list with the ruling: the three doctrine sites (`CONCURRENCY.md:114`,
`PROPAGATION.md:399`, `:632`), and — if option (a) — note that item `040`'s title and
quotation, `310/030`'s list and the generated index all carry the name too, so prose
alone would not restore a veil.

**PV3 — minor.** *The application has no `CHANGELOG.md` entry.* `CHANGELOG.md` carries
"### Fixed (2026-08-18 — the canonical child block's index rule was lossy and
mis-pointed)" at line 159, which sends a reader to `git diff --cached` "as the whole
index" — the half of the story before the command itself was corrected — and carries
entries for 2026-08-17 and 2026-08-23. Neither 2026-08-22 doctrine commit (`2489f12`,
`1d19729`) has one. A correction to the one check every session runs at a dirty
checkout is a notable change under the file's own header.
*Counsel:* one `### Fixed (2026-08-22 — …)` entry naming PU-1 and PU-2, so the
2026-08-18 entry is not the last word.

**PV4 — note.** *Residue of the correction note.* With the command now plain and the
sentence already saying "read the whole staged diff, paths included", the 2026-08-18
bold clause at `CONCURRENCY.md:88–90` ("Read it as the whole index, not as your own
hunks — the paths it shows that you never staged are the point") says the same thing a
second time in the same bullet; the parenthetical sits between the check and its "other
half", splitting a two-part rule; and the inserted text was not re-flowed — orphan lines
at `CONCURRENCY.md:115` (48 columns) and `PROPAGATION.md:636` (28 columns), and line 88 at
89 raw columns (clean under `wrapscan`'s own counting). Cosmetic.
*Counsel:* fold the note to "(corrected 2026-08-22, PU-1 — the old form is in the
record)", drop the duplicated clause, re-flow both paragraphs.

### Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 2 minor · 1 note.** The command is now
right and the sentence claims no more than the command delivers; the naming is the ruled
outcome and exposes nothing the public tree did not already hold; the boarded items say
what the ruling said and have since closed. What the application missed is its own
consequence: correcting the command falsifies the instance narrative that leans on the
old one (PV1). No MAJOR, so under `REVIEW.md` § *Applying decisions to doctrine* this is
the terminal application and the cycle closes on the principal's rulings, with no
further pointer owed.

### Re-run ledger

All runs 2026-09-25 UTC, at `c4b9cd0`, in the scratch clone
`<scratchpad>/PV/probe` unless stated. Exit codes read explicitly.

1. **Index probe** — `<scratchpad>/PV/probe_index.sh` (a throwaway repo, git 2.50.1):
   eight states — staged content edit, staged-then-edited, untracked, staged empty new
   file, staged pure rename, staged mode-only change, staged binary, intent-to-add.
   `git diff --cached`: six `diff --git` path lines (all six staged entries; rename, mode
   and binary each carry their marker line). `git diff --cached --stat`: 6 files.
   `git diff --cached -U0 | grep '^@@'`: 2 hunk headers, 0 paths. `git commit
   --dry-run --short`: the same six staged; intent-to-add and untracked not taken.
2. **Old text reproduced** — `git show f9eda42^:docs/method/CONCURRENCY.md`, lines 84–86:
   the `-U0 | grep '^@@'` pipe with "compare the hunk headers"; `git show f9eda42`
   shows the "whole index, not your own hunks" clause and the Bearing added 2026-08-18.
3. **linkscan**, floor args — `python3 tools/linkscan.py --root <probe> docs/method`:
   clean, exit 0.
4. **pathscan**, floor args — `python3 tools/pathscan.py --warn --root <probe>
   docs/method`: 1 pre-existing warn-only finding, not in the delta
   (`docs/method/session-open/session-open-prompt.md:15`, a relative sibling-checkout
   path); exit 0.
5. **Floor, hook plane** — `python3 tools/floor.py --plane hook --root <probe> --tools
   <probe>/tools`: exit 0; all enforced checks ✅; advisories: sizescan ×2 (index and
   sessions log length), pointerscan ×1 (`160/380` grammar, not this pass), pathscan ×1
   (item 4).
6. **Floor, ci plane** — `python3 tools/floor.py --plane ci --root <probe>`: exit 0;
   secretscan 22 advisory entropy findings (the standing set, none in the delta);
   leakscan structural-only 🟡 as designed, `local-term×3` in the tally; same three
   advisories as the hook plane.
7. **Cold sweeps** — `python3 tools/coldsweep.py --root <worktree> --also-exclude
   <160/280> "<pattern>"` for the old and new commands (32 hits / 510 files) and for the
   veiled and named forms; 347 files barred by default plus the pointer. README exposure
   disclosed under *Provenance*.
8. **wrapscan** on the edited file — `python3 tools/wrapscan.py --root <probe>
   docs/method/CONCURRENCY.md`: clean, exit 0 (line 88 is 89 raw columns; clean under the
   tool's counting).
9. **Reference resolution** — `ls` of every path the delta names, `grep -n '^#'` for
   every section it names: all present (lens 2).
10. **Forge** — `gh repo view <owner>/<child> --json visibility`: does not resolve under
    the owner's account; consistent with `010/030`. Nothing further recorded.

### Follow-up checklist

- [ ] PV1 — principal's ruling on re-wording § *The instance* ¶3 and the Bearing.
- [ ] PV2 — nothing until `320/330` is ruled; carry the three-site sweep list with it.
- [ ] PV3 — one `CHANGELOG.md` entry for 2026-08-22, if the principal accepts.
- [ ] PV4 — fold the note, drop the duplicate clause, re-flow; cosmetic, batch with PV1.
- [ ] Not this pass's: `310/030`'s hand sweep of the ten children remains unrun;
      `320/350`'s hook-window race is boarded and awaits its own ruling.
