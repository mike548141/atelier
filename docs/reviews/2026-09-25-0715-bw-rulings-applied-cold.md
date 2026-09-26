# Cold pass — the BW rulings applied — the hook-plane condition said straight on five surfaces

**Pass type:** doctrine cold pass (with the code docstring it governs), per
`docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md`.
**Why it earns a review:** five surfaces once asserted a guarantee the board
tool did not provide; the applied wording is what every claimer now reads before
committing a claim from a dirty checkout, so a misnamed condition here silently
re-opens the original defect.

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

- `80e6fc0` (2026-08-23) — the landing commit
- `8c67893` / `29904ca` (2026-09-18) — the widening: `tools/board.py` argv and
  the § *On a split board* parenthetical respelled `--rebuild`
- ⚠️ `4412be8` / `18c155f` / `b2a54f1` (2026-09-20) — later,
  **separately-queued** work (`160/390`) rewrote § *On a split board* and §
  *Claiming at a dirty primary checkout* again, and `tools/board.py` gained
  `--staged` / `--from-index`. Review the five surfaces **as the BW application
  left them and as they now stand at HEAD**, and say per surface which wording
  survives, which was superseded, and whether the superseding kept the BW-ruled
  condition true

Delta paths:

- `tools/board.py` — the hook clause in the module docstring; § *STATED
  RESIDUAL* merged to one account
- `tools/README.md` § **board** — the headline condition
- `docs/method/CONCURRENCY.md` § *On a split board* — subject and condition
  corrected; CF3's queue test widened to sibling state lines
- `docs/roadmap/README.md` — the preamble qualified
- `docs/decisions/2026-08-15-0610-board-store-per-item-files.md` — the
  2026-08-23 amendment at the foot
- the unwind list in `docs/roadmap/010-*/020-*.md`

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the five spellings now name **one** condition, the same condition, and
the condition the tool actually checks — probe the tool, do not read the prose:
in a scratch clone, construct (a) worktree and index agreeing with a stale
index, (b) a staged item edit with an unstaged index rebuild, (c) an unstaged
sibling state-line edit beside your own staged claim, and run `board.py
--check`, `--check --staged`, and the hook, recording what each catches. Whether
CF3's widened queue test and the § *On a split board* stop rule agree with each
other at HEAD. **Non-goal:** the principal's BW rulings are not under review —
only their application; the later `160/390` code is reviewed by its own pass,
but its effect on these five surfaces is in scope here.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   applied wording rests on a claim about *which plane the hook reads* — test
   that claim against the tool at HEAD, not against the docstring. Ask whether
   five surfaces stating one mechanism is the right shape at all, or whether
   four should point at one.
2. **Correctness & quality.** Diff the surfaces across `80e6fc0`, `8c67893` and
   the 2026-09-20 commits. For each surface at HEAD: is the condition stated
   true, complete, and in the same words as its neighbours? Does the § *STATED
   RESIDUAL* account in `board.py` still describe a residual the tool has, or
   one that the 2026-09-20 work closed?
3. **Completeness / harvest.** Search every other surface that tells a claimer
   what the hook guarantees: `CLAUDE.md`, `skills/session-onramp/SKILL.md`,
   `skills/queue-run/SKILL.md`, `docs/build/templates/CLAUDE.md`,
   `tools/pre-commit.sample`, `CONTRIBUTING.md`. A sixth surface still carrying
   the pre-BW wording is a finding.
4. **Security & privacy** — mandatory. The board tool reads the git index and
   the worktree; no network, no secrets. Confirm there is no path by which
   `--from-index` writes anything other than the generated index, and that a
   rebuild from the index cannot bake a sibling's *staged* private text into the
   generated file it commits (the case the wording was written to close).
   Discharge the house security scanner by grounds (landed-delta review; pending
   = other passes' drafts) in one explicit line.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/board.py --selftest`; `python3 -m unittest tools.test_board`;
  the full Python suite once
- the three constructed states in *Scope*, in a scratch clone under the session
  scratchpad — never in the shared worktree — with the hook installed the way
  `.githooks/pre-commit` documents
- the floor on the hook plane at HEAD, via the invocation the hook uses

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
`docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md`
(it carries the author's own lens hints), and:

- the verdict `docs/reviews/2026-08-17-1321-bs1-wording-cold.md` (BW; its §
  *Rulings — 2026-08-23* is this delta's intent record)
- the board item `docs/roadmap/290-*/050-*.md` (the BS1 ruling wording)
- `docs/sessions/2026-09-18-0114-queue-run-hand-up-fixes.md` and
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/260-rule-4-cold-pass-queued-bs1-wording.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `BA`: `BA1`, `BA2`, …) and severities (MAJOR / MODERATE
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

## Verdict — phase 1, written 2026-09-25 UTC (prefix BA)

### Provenance, repeated

- **Spawned by:** the batch orchestrator of review-batch-0925, not by any session that
  authored `80e6fc0`, `8c67893`/`29904ca` or the 2026-09-20 commits. This reviewer was
  neither started nor instructed by those sessions and has edited none of the delta's paths.
- **Tier:** `claude-fable-5-1`, checked at spawn; the orchestrator is the same tier, so the
  off-tier clause is not invoked. Shape: reviewer-plus-orchestrator, orchestrator forms no
  finding; the `.deferred.md` sibling was not in the tree and has not been opened.
- **Read, in scope:** this brief; `docs/method/REVIEW.md` and `00-APEX.md` at HEAD; the six
  delta paths at HEAD (`c4b9cd0`); `git show` of the landing commits restricted to the delta
  paths (`80e6fc0`, `8c67893`, `b2a54f1`, and `4412be8` for `tools/README.md`), including
  their commit messages; the `board.py` docstring at `80e6fc0`; `tools/floor.py` lines
  1–1135 (registry and planes), `tools/harvestscan.py` `git_show`/`read_source`,
  `tools/test_board.py` `StagedPlane`, `.githooks/pre-commit`, `.github/workflows/ci.yml`
  (floor steps), `.atelier-floor.json`; the lens-3 surfaces (`CLAUDE.md`,
  `skills/session-onramp/SKILL.md`, `skills/queue-run/SKILL.md`,
  `docs/build/templates/CLAUDE.md`, `docs/build/templates/CONTRIBUTING.md`,
  `tools/pre-commit.sample` — no root `CONTRIBUTING.md` exists); `docs/method/RECORD.md`
  § *The roadmap*, `docs/method/PROPAGATION.md` lines 140–160 and 580–622; board items
  `010/020`, `010/160`, `320/120` (opened **after** BA1 was formed, when a sweep hit it),
  `030/140` lines 76–92, `010/030` lines 62–76; `CHANGELOG.md` lines 8–125 and 176–186.
- **Barred material honoured:** `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`,
  every prior verdict in `docs/reviews/`, the queue pointer `160/260`, item `290/050`, and
  every other `2026-09-25-0715-*` brief — none opened. `coldsweep.py` was the sweep tool.
- ⚠️ **Exposure disclosed:** my first sweep passed `--also-exclude` for `160/260` only, so
  the hit list printed one-line fragments of the barred `290/050` (its lines 4, 5, 8, 13) and
  of `010/050` (the closed BS1-pass pointer; its lines 17, 32, 33) before I re-ran with
  `290/050` excluded. Neither file was opened. The landing commits' messages (author
  narrative, not on the barred list) were read in full via `git show`.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named by me and tested against the tool at HEAD:

1. *The hook reads the index plane.* **True.** `floor.py --list --plane hook` renders the
   board line enforced; the hook's own invocation at HEAD prints `matches the staged
   docs/roadmap/` (probe S0), and CI renders the plain form.
2. *"Index on both sides" equals "what this commit is about to make true".* **True for every
   commit form probed**, including one the surfaces never mention: a pathspec commit
   (`git commit -- <paths>`) runs the hook against git's temporary index, which `git show
   :path` honours, so the hook still answers for that commit's content (probe S4(i)).
3. *`git ls-files` enumerates every staged item file.* **False for a path git quotes** —
   non-ASCII filenames come back double-quoted with octal escapes and `_index_sections`
   drops them silently (probe S5) — **BA2**.
4. *"A sibling's dirty line" means an unstaged one.* The tool's guarantee is exactly and
   only the unstaged case; a sibling's **staged** line is baked by `rebuild --from-index`
   and accepted by `--check --staged`, by construction (probe S4) — **BA3**. The brief's
   lens-4 framing ("the case the wording was written to close") is attackable on this
   point: the wording closed the unstaged case; the staged case is the shared-index rule's.
5. *The 2026-09-20 superseding kept the BW-ruled condition true.* The BW condition was
   time-bound ("until the staged-plane check lands") and is correctly gone from every live
   surface; its successor is true on all five except for the hole in 3 and the blur in 4.
   But the CONCURRENCY rewrite dropped the interim **stop rule** and pointed at CF3, which
   does not carry it — **BA1**.
6. *Five surfaces should each state the mechanism.* After the sweep each restates the full
   account; the drift that pattern invites is already visible (BA3, BA4) — **BA6**.

### Lens 2 — correctness and quality, per surface at HEAD

| Surface | BW wording (`80e6fc0`) | At HEAD | True? |
|---|---|---|---|
| `tools/board.py` hook clause | superseded by `4412be8` | staged plane, both sides | yes, less BA2 |
| `tools/board.py` § STATED RESIDUAL | superseded (retired) | closed case + tautology | yes; live residuals unstated (BA7) |
| `tools/README.md` § board | superseded by `4412be8` | full staged-plane account | yes, less BA2/BA3; bare-word spelling (BA4) |
| `CONCURRENCY.md` § On a split board | superseded by `b2a54f1` | mechanism true; stop rule replaced by "see CF3" | mechanism yes; **stop rule absent** (BA1); `--rebuild` respelling of `8c67893` lost (BA4) |
| `CONCURRENCY.md` CF3 (BW4 widening) | survives verbatim | branch A excludes any state line; branch B keys on the item itself | the sibling case is in neither branch (BA1) |
| `docs/roadmap/README.md` preamble | superseded by `b2a54f1` | staged plane at the hook, `--from-index` at a dirty checkout | yes |
| ADR 2026-08-23 amendment | survives (append-only), superseded by the 2026-09-20 amendment | — | the 2026-09-20 amendment's CF3 sentence is inaccurate (BA1) |
| `010/020` unwind list | survives; all five swept | ticked | yes — every listed surface was changed |

The five spellings now name **one** condition (the index plane on both sides) and the tool
checks that condition (probes S1–S3, S6). Where they still differ is vocabulary ("dirty"
vs "unstaged", BA3) and the rebuild spelling (BA4), not the condition.

### Lens 3 — completeness and harvest

No sixth live surface carries pre-BW or interim wording: `CLAUDE.md` names only the
rebuild command (flag form); the two skills and the child block (`templates/CLAUDE.md`,
`PROPAGATION.md`) carry the shared-index rule and no hook-plane claim; `tools/pre-commit.sample`
names no scanner; the CONTRIBUTING template lists `board` as unsoftenable; `RECORD.md`
§ *The roadmap* says "enforced by the `board` floor check" with no plane claim; the
`floor.py` registry comment matches the code. What is stale sits in records and open items:
the CHANGELOG records the 2026-08-17 and 2026-08-23 interim wording and never the
2026-09-20 closure; `010/030`'s gate note still says both slips "ride in nine children";
`320/120`'s "the house does answer it thirty lines earlier" no longer holds (BA5). Existing
work the delta should have met: `320/120` (filed 2026-08-24) already recorded that CF3's
branch list does not answer the sibling case — the 2026-09-20 rewrite removed the one
sentence that did, without citing it.

### Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending diff, which in
the shared worktree is other passes' unstaged drafts, and this is a landed-delta review.
Code-altitude read by hand, checked against the OWASP Top 10 classes that can apply to a
local CLI: **injection** — every git call is an argv list with no shell, paths come from
`git ls-files`; **path handling** — the board location is the fixed `docs/roadmap/` under an
operator-supplied `--root`, no traversal from content; **secrets/network** — none;
**writes** — one non-test write site in the module (`index.write_text`, line 559), and
probes S3(ii)/S6 show `rebuild --from-index` touches `docs/ROADMAP.md` only, or nothing.
Design altitude: a rebuild from the index **can** bake a sibling's *staged* text — that text
is the commit's own content by definition (S4) — so the privacy defence for the shared index
is `CONCURRENCY.md` § *The trigger*'s whole-`git diff --cached` read, not this tool; the
hook additionally blocks a pathspec commit that would carry a baked line without its source
(S4(i)). Threats named at design time: absorbing an unstaged peer line (closed), a quoted
path invisible to the index plane (BA2, a fail-open the design did not enumerate). No
finding rises to a security severity.

### Findings

**BA1 — MAJOR (doctrine; the principal's).** *The dirty-sibling stop has no operative home
at HEAD, while four records say it stands.* `b2a54f1` deleted the sentence that carried it
(§ *On a split board*: "a dirty sibling item state line is a stop for claiming from that
checkout") and replaced it with "is CF3's to restate or relax … see there". CF3's branch
list (lines 331–337) answers the case in neither branch: branch A is excluded because BW4
widened "the queue" to *any* item's state line, and branch B fires only when "the item's
file **itself** is dirty". The 🎯 paragraph beneath says "It has not been relaxed here"
but never states the stop. Meanwhile the ADR's 2026-09-20 amendment (lines 173–176),
`010/020`, `010/160` and the landing commit's message all describe CF3 as stopping a claim
on a dirty sibling item. `320/120` (a child's filing, 2026-08-24, verified there against
`origin/main`) had already found the branch list silent and located the only answer in the
parenthetical this delta removed; its own history shows the same clause lost the rule once
before, when the split-board rename narrowed branch B. Rule lost by rewrite, twice, on one
clause — and the delta's records claim the opposite. *Counsel:* fold `010/160` and `320/120`
into one ruling; whichever posture Mike picks, put one operative sentence for the sibling
case **in CF3's branch list** (320/120's option (iii)); correct the three records to say
the stop lived in § *On a split board*'s interim sentence, not in CF3.

**BA2 — MODERATE (code; ordinary fix, may route to 160/390's pass).** *The index plane
silently omits any staged item whose path git quotes.* `_index_sections` parses
`git ls-files` text; with `core.quotePath` at its default a non-ASCII filename returns as
`"…/045-tohut\305\215-probe.md"`, the prefix strip fails and the entry is skipped with no
problem reported. Probe S5: a staged item named with a macron is rendered by the worktree
rebuild, dropped by `rebuild --from-index`, `--check` reds and `--check --staged` passes —
so the hook accepts a commit whose staged index is stale and CI reds it after the push.
atelier has zero such paths (`slug()` is ASCII-only) but children hand-name item files and
the house writes tohutō. *Counsel:* `git ls-files -z` split on NUL (or `-c
core.quotePath=false`), plus a regression test with a macron filename; state it as a
residual on the surfaces until fixed.

**BA3 — minor (wording, the surfaces).** "Dirty" and "unstaged" are used interchangeably
(`CONCURRENCY.md` 299, `docs/roadmap/README.md` 11, ADR 129/158, `board.py` 41/80,
`tools/README.md` 90–91). The guarantee is the *unstaged* one; a peer's *staged* line is
baked and accepted (S4) and is guarded by a different rule. *Counsel:* say "unstaged" where
the guarantee is meant, and add one sentence to the docstring and README: a staged line is
this commit's content whoever staged it — `git diff --cached` is the check for that.

**BA4 — minor (spelling drift).** `8c67893` respelled § *On a split board* to
`tools/board.py --rebuild`; `b2a54f1` rewrote the paragraph back to the bare word. The
`rebuild_cmd` docstring claims the flag form is the spelling "everywhere a human reads it
(CLAUDE.md, tools/README.md, --help)" — `tools/README.md` § board uses the bare word only.
Both spellings run, so no behaviour is affected; the claim is stale.

**BA5 — minor (harvest).** The CHANGELOG has no entry for the 2026-09-20 closure of BS1's
residual (its 2026-08-17 and 2026-08-23 entries stand alone); `010/030` (open, 🎯) still says
both slips ride in nine children "until BS1 is ruled"; `320/120`'s findability paragraph is
false at HEAD (feeds BA1).

**BA6 — note (shape).** After the sweep all five surfaces restate the whole mechanism
(docstring ≈30 lines, README ≈22, ADR amendment ≈35, CONCURRENCY ≈13, roadmap README ≈7).
BA3 and BA4 are the cost of five copies. *Counsel:* docstring canonical; README and
CONCURRENCY one clause each plus a pointer; the roadmap README one clause; ADR amendments
stay full, being records.

**BA7 — note (residual account).** `board.py` § STATED RESIDUAL is headed RETIRED and names
only the tautological case. Live residuals it could state: BA2, and the hand-run remedy —
at a dirty checkout the worktree `--check` reds and prints the plain `rebuild` remedy
(S3(ii)), which if run absorbs the sibling's line; the hook then catches it (S3(i)), so the
loop self-corrects but the printed advice is wrong for that state.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR (BA1), 1 MODERATE (BA2), 3 minor (BA3–BA5), 2 notes
(BA6–BA7).** The applied condition is one condition, true on all five surfaces, and the
tool checks it; the MAJOR is the claimer's stop rule that the rewrite orphaned.

### Re-run ledger (scratch clone of the worktree at `c4b9cd0`, hook installed via
`core.hooksPath .githooks`; nothing run against the shared worktree but read-only git and
`coldsweep.py`)

| Command | Result |
|---|---|
| `python3 tools/board.py --selftest` | `board selftest OK`, rc 0 |
| `python3 -m unittest tools.test_board` | Ran 43 tests, OK |
| `python3 -m unittest discover -s tools -p 'test_*.py'` (once) | Ran 1564 tests in 463.7 s, OK |
| `python3 tools/floor.py --plane hook --root . --tools tools` (the hook's own line) | rc 0; board ✅ enforced, "matches the staged"; one warn-only pathscan advisory (a session-open prompt path, not this delta) |
| `floor.py --list --plane hook` / `--plane ci` | board enforced on both |
| S0 clean HEAD | `--check` 0 · `--check --staged` 0 |
| S1 item staged, no rebuild | `--check` 1 · `--staged` 1 · hook BLOCKED by board |
| S2 item staged, rebuild on disk unstaged | `--check` 0 · `--staged` 1 · hook BLOCKED; after `rebuild --from-index` + stage: 0 · 0 · commit lands (2 files) |
| S3(i) sibling unstaged line, plain rebuild staged | sibling text in index: yes · `--check` 0 · `--staged` 1 · hook BLOCKED |
| S3(ii) same, `rebuild --from-index` | sibling text: no, my claim: yes · `--check` 1 · `--staged` 0 · commit lands (2 files); sibling file still dirty on disk |
| S4 sibling **staged** line | baked by `--from-index`: yes · both checks 0 · pathspec commit BLOCKED by board (HEAD unchanged) · plain commit lands 3 files |
| S5 macron filename staged | worktree rebuild lists it, index rebuild does not · `--check` 1 · `--staged` 0 (BA2) |
| S6 write footprint at a dirty checkout | `rebuild --from-index` touched no path |
| `coldsweep.py` patterns | interim phrases (`worktree and index agree`, `only when worktree`, `cannot vouch`, `until the staged-plane check lands`, `stage-yours-alone`, `reads the worktree`) hit only CHANGELOG entries, the ADR's earlier amendments, `320/120` and the two closed pointers — no live surface |

### Follow-up checklist

- [ ] BA1 — to the principal with `010/160` and `320/120` as one ruling; restore an
      operative sibling-case sentence in CF3's branch list; correct the three records.
- [ ] BA2 — code fix + macron-filename regression test; state the residual until then;
      route with 160/390's code pass or queue under `010`.
- [ ] BA3, BA4, BA7 — wording; doctrine lines wait on the ruling, docstring/README ordinary.
- [ ] BA5 — CHANGELOG closure entry; `010/030` gate note; `320/120` findability note.
- [ ] BA6 — shape decision, the principal's; no edit until ruled.
