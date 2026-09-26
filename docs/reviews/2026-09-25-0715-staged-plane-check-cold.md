# Cold pass — the staged-plane board check and its doctrine sweep

**Pass type:** code + doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/390-rule-4-cold-pass-queued-the-staged-plane-check.md`.
**Why it earns a review:** the board check is the hook's guard against a claim
commit that carries a stale or absorbed index; reading the wrong plane is
exactly the defect (BS1) it was funded to close, and the doctrine sweep is what
every claimer reads about it.

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

- `4412be8` / `18c155f` (2026-09-20) — `board.py` checks the staged plane and
  rebuilds from it
- `b2a54f1` (2026-09-20) — the registry wiring at the hook, and the five interim
  doctrine surfaces swept

Delta paths:

- `tools/board.py` — the `--staged` / `--from-index` planes and the two
  `_*_sections` readers
- `tools/test_board.py` — the `StagedPlane` class
- `tools/README.md` § *board*
- `tools/floor.py` — the `board` Scanner's hook argv
- `docs/method/CONCURRENCY.md` §§ *On a split board* and *Claiming at a dirty
  primary checkout*
- `docs/roadmap/README.md` — the preamble
- `docs/decisions/2026-08-15-0610-board-store-per-item-files.md` — the
  2026-09-20 amendment

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

The plane question, driven not read: in a scratch clone with the hook installed,
construct a merge in progress, a partial `git add -p`, an intent-to-add file, a
renamed item file, a deleted item, and a sibling's unstaged state-line edit
beside your staged claim, and record what `--check --staged` says for each
against what the worktree check says. Whether `board.py` importing `harvestscan`
at module scope works for a child resolving tools through `$ATELIER_TOOLS`
(drive it from a scratch child). Whether the hook argv the registry passes is
the one the tool expects, on both planes. Whether the swept surfaces now agree
with each other and with the code. **Non-goal:** the BS1 ruling that funded the
work.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   check presumes "the index on both sides" is the hook's right question — find
   the state where it is the wrong one, or show there is none. Ask whether a
   registry wiring that a previous run refused as unsafe on 2026-09-19 is safe
   now, from the code, not the comment.
2. **Correctness & quality.** Read all of `board.py` and the `board` entry in
   `floor.py`. Run `--selftest`, `tools.test_board`, the full suite. Drive every
   state in *Scope*. Check `--from-index` rebuilds are byte-identical to
   worktree rebuilds on a clean tree.
3. **Completeness / harvest.** The interim surfaces the sweep claims to have
   covered: list every surface that described the hook's guarantee before
   2026-09-20 (`160/260`'s five, plus any others) and check each at HEAD. Does
   `CHANGELOG.md` carry it?
4. **Security & privacy** — mandatory. The tool reads the git index via
   subprocess; check its argument handling against a path with spaces or a
   leading `-`, and that a rebuild from the index can never write a sibling's
   *staged but private* text into the generated file. The house scanner is
   discharged by grounds (landed delta; pending = other passes' drafts) — say
   so, and deliver the code-altitude read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/board.py --selftest`; `python3 -m unittest tools.test_board
  tools.test_floor tools.test_precommit`; the full Python suite once
- the floor on both planes at HEAD, and the hook driven live in a scratch clone
  through every state in *Scope*
- `--from-index` vs worktree rebuild byte comparison

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
`docs/roadmap/160-doctrine-review-owed/390-rule-4-cold-pass-queued-the-staged-plane-check.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md` (⚠️ head and tail
  read by the brief-writer; the `010/020` section not opened)
- the verdict `docs/reviews/2026-08-17-1321-bs1-wording-cold.md` (BW — where
  BS1's fund was ruled)
- the board items `docs/roadmap/010-*/020-*.md`, `docs/roadmap/115-*/080-*.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/390-rule-4-cold-pass-queued-the-staged-plane-check.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `SG`: `SG1`, `SG2`, …) and severities (MAJOR / MODERATE
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

# Verdict — phase 1, written 2026-09-25 (07:11–07:55 UTC)

## Provenance, repeated

- **Reviewer:** a fresh subagent on `claude-fable-5-1` (the principal-named tier,
  checked at spawn), spawned by the batch orchestrator with this brief as its only
  framing. It is not the author's session, was neither started nor instructed by
  the author, and edited none of the delta's paths. It formed every finding and
  severity below; the orchestrator formed none.
- **Shape:** reviewer-plus-orchestrator, both seats Fable; the `.deferred.md`
  sibling was held outside the worktree and had not been seen when this section
  was written. Phase 2 follows on receipt.
- **Where it ran:** the shared review worktree read-only (this file the only
  write), and a scratch clone of it at `c4b9cd0` under the session scratchpad,
  with the tracked hook installed there (`core.hooksPath .githooks`). Every
  mutation, merge, hook-driven commit, scratch child and scratch linked worktree
  ran in that clone or beside it. No git command that writes ran in the worktree.
- **What it read (delta and doctrine):** `docs/method/REVIEW.md`, `00-APEX.md`;
  `tools/board.py`, `tools/test_board.py` in full; `tools/floor.py` (docstring,
  `Scanner`, the `board` entry, `_render`, `plan`, scanner path resolution,
  argparse); `tools/harvestscan.py` (`git_show`, `list_markdown`, the plane
  constants); `.githooks/pre-commit` and `tools/pre-commit.sample`;
  `tools/README.md` § *board*; `docs/method/CONCURRENCY.md` §§ *On a split
  board* and *Claiming at a dirty primary checkout*; `docs/roadmap/README.md`;
  the board-store ADR from *Consequences* down; `CHANGELOG.md` (head and the
  2026-08-17 board entries); `.atelier-floor.json`; the three landing commits'
  messages and diffs; the board items `010/160` (created in `b2a54f1`),
  `320/120` and the head of `030/140` (open items on the same CF3 clause, not
  barred); excerpts of `tools/test_floor.py`.
- ⚠️ **Exposure, disclosed.** (1) The brief cites "`160/260`'s five"; I read
  that item in full to get the list, and it carries a paragraph summarising the
  prior BW verdict's findings (BW1–BW4) — rule-2 material, met before my findings
  were written. I have kept BW's questions out of my lenses as far as one can,
  and note it here rather than deny it. (2) My first `coldsweep` run excluded
  only the queue pointer, as the brief's command does, so six hits inside the
  barred `010/020` item printed — cut to ~60 characters each by my own `cut`;
  later sweeps added `--also-exclude` for `010/020` and `115/080`. (3) The S12
  probe output listed the file names of every `⏳` pointer on the board (names
  only, no content).

## Lens 1 — approach and assumptions

The load-bearing assumptions, named by me and each driven rather than read:

| # | Assumption the check rests on | Holds? | Probe |
|---|---|---|---|
| A1 | The git index *is* what the commit will contain | Yes, including the temporary index `git commit -a` / pathspec commits build (`GIT_INDEX_FILE`), in the clone and in a linked worktree | S9, S9b |
| A2 | `git ls-files` prints one plain path per line | **No** — non-ASCII names are C-quoted under the default `core.quotePath` | S11 → SG1 |
| A3 | `git show :path` output is UTF-8 | Only when the locale says so; the worktree reader pins UTF-8, the index reader does not | S12 → SG5 |
| A4 | A failing `git ls-files` means "no board here" | No — it can mean git failed | S13 → SG6 |
| A5 | Every index entry is a stage-0 blob with content | No — unmerged and intent-to-add entries exist | S3b, S5 → SG4 |
| A6 | A sibling's "dirt" at the primary checkout is *unstaged* | The tool never assumes it; the *doctrine's* relaxation ask does | S2b → SG3 |
| A7 | The registry wiring cannot skew flag against parser | Yes — `floor.py` resolves `tools/<name>.py` beside itself (line 1601) and the hook passes that one dir; a child's CI fetches one checkout | code read, S10 |

**Is "the index on both sides" the hook's right question?** For everything the
hook can see, yes, and the states that could make it wrong were driven: partial
staging (S4), staged and unstaged renames and deletes (S6, S7), a merge with the
index file conflicted (S3), `-a` and pathspec commits (S9). In each the staged
plane answered "what is this commit about to make true" and the worktree plane
answered a different question, as the design says. The two states where the
index is *not* what the commit makes true are intent-to-add entries — listed in
the index, silently excluded by `git commit` (S5) — and unmerged entries, which
`git commit` refuses before any hook runs (S3b). Neither is a wrong question;
both are misdiagnosed by the reader (SG4). The state where a right answer is
still not enough is a sibling's **staged** edit (S2b): the index plane correctly
reports agreement, `--from-index` absorbs the sibling's line, and the claim
commit ships the sibling's hunk. There the guard is doctrinal (CF3), and the
delta's doctrine text weakens it (SG2) and proposes to relax it on a premise the
probe falsifies (SG3).

**The 2026-09-19 refusal, answered from the code:** the skew that refusal named
cannot arise for `board`, because the hook and the CI plane each invoke one tools
directory and every scanner is loaded from it — a child never carries its own
`board.py`. The wiring is safe on that ground, not on the comment's. The
non-goal (the BS1 ruling) fences off nothing this pass needed.

## Lens 2 — correctness and quality

- `--selftest` OK; `tools.test_board tools.test_floor tools.test_precommit` exit
  0 (2 m 44 s); full suite **1,564 tests OK** (6 m 26 s), once, in the clone.
- Floor at `c4b9cd0`, both planes, in the clone: exit 0; `board ✅ enforced` on
  each; the hook renders `--check --staged --root <root>` (no positional in
  staged mode — `_render` drops the whole-repo scope, which `board` ignores) and
  CI renders `--check --root <root> <root>`. `pathscan`'s one warn-only finding
  is pre-existing and not board's.
- Rebuilds on a clean tree: HEAD's index, the worktree rebuild and the
  `--from-index` rebuild are byte-identical (one SHA-256 for all three).
- Both BS1 slips reproduced and caught **at the hook, live** (S1, S2): slip (a)
  passes the worktree check and blocks the commit under `--staged`, with the
  `rebuild --from-index` remedy printed; slip (b) — a sibling's unstaged claim
  line — is absorbed by the plain rebuild (1 line) and not by `--from-index`
  (0), and the claim commit carries exactly two files.
- The doctrine's "after a merge conflict on the index, rebuilding *is* the
  resolution" holds live (S3): mid-merge `--check --staged` reds with the
  `--from-index` remedy, the rebuild resolves the conflicted `docs/ROADMAP.md`,
  and the merge commit passes the hook with both claims present.
- Child geometry (S10): via `hooks.atelierTools` and via `ATELIER_TOOLS`, the
  hook blocks a stale index and passes a current one; the remedy prints the
  child spelling; `board.py` run from a symlinked tools dir with the cwd at `/`
  imports `harvestscan` fine; a monolithic child is out of scope on the staged
  plane; a newly-split child with nothing staged is out of scope on the staged
  plane and stale on the worktree plane — consistent with the plane semantics.
- The "not fail-open" sentence in the docstring is true of the no-board case and
  false of the git-error case (SG6). The rest of the docstring, README and the
  swept doctrine match the code as driven.

## Lens 3 — completeness and harvest

Surfaces that described the hook's guarantee before 2026-09-20, checked at HEAD:
`tools/board.py` docstring ✔, `tools/README.md` § *board* ✔, `CONCURRENCY.md`
§ *On a split board* ✔ (but see SG2), CF3 ✔ (flag named; the 🎯 paragraph), the
board-store ADR by appended amendment ✔, `docs/roadmap/README.md` preamble ✔.
Sweep of `docs/method`, `docs/build`, skills and the ADR for any other board-hook
description: none. Still carrying the interim wording at HEAD: `320/120` (an
open child-filed item quoting "until the staged-plane check lands", now landed)
and the historical records, which is correct for records. `CHANGELOG.md` does
**not** carry the change (SG7). The new ruling item `010/160` neither cites nor
reconciles the two open items already asking the principal about the same
clause (SG8).

## Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending
diff, which in the shared worktree is other passes' unstaged drafts, and this is
a landed-delta review. The code-altitude read by hand, checked against the OWASP
Top 10 (2021) categories that reach this class:

- **Injection (A03):** none. Every git call is a list argv with no shell; the
  pathspec follows `--`; `git show` targets carry the `:` prefix, so a leading
  `-` cannot read as an option. Driven: an item named with a leading dash and
  one with a space both survive both planes (S11); a root path with a space is
  fine.
- **Integrity of the check (A08):** two ways the gate can pass on nothing — a
  C-quoted name silently dropped (SG1) and a git error read as "no board" (SG6).
- **Environment-dependent behaviour (A05):** the staged reader's result depends
  on `core.quotePath` and the process locale (SG1, SG5); the worktree reader
  depends on neither.
- **Diagnostics (A09):** unmerged and intent-to-add entries produce a wrong
  remedy (SG4).
- **Privacy / design altitude:** the brief asks whether a rebuild from the index
  can write a sibling's *staged but private* text into the generated file. It
  can, and the claim commit then ships it — probed (S2b): three files in "my"
  commit, the sibling's claim text inside it. That is not a tool defect: the
  index is one shared plane and staged content is, by definition, about to be
  committed by whoever commits next. The defence is doctrinal — CF3's stop on a
  dirty sibling item, where "dirty" must include *staged* — and the delta both
  removes that rule's operative sentence (SG2) and proposes relaxing it on the
  unstaged case alone (SG3). Committing `--only` your own paths does not rescue
  it: the hook then reds, because the index carries the sibling's line (S2c).
- Symlinks: the index plane reads a tracked link's blob, never its target; the
  worktree plane reads through it. The new plane is the safer of the two here.
- No network, no secrets, no writes outside `<root>/docs/ROADMAP.md`; memory
  growth pinned linear by the existing test.

## Findings

**SG1 — MODERATE (code).** A non-ASCII item file name vanishes from the staged
plane without a word. With `core.quotePath` at its default, `git ls-files`
C-quotes the path (S11: `"…/952-m\304\201ori.md"`); `_index_sections` slices the
prefix off the quoted string, splits it into three parts, and drops it as "deeper
than section/file". `rebuild --from-index` then writes an index missing the item
and exits 0; `--check --staged` passes against it while the worktree check reds;
the hook passes a stale index and CI catches it — the funded class, reopened for
one name class. Not MAJOR because `slug()` strips diacritics (the estate's 329
tracked board paths are all ASCII, checked) and CI still catches it; MODERATE
because the failure is silent at the gate and macrons are the house convention.
Same pattern in `harvestscan.list_markdown` (no `-z`), so HV4's plane shares it.
*Counsel:* `ls-files -z` and a NUL split in one shared helper; a `StagedPlane`
test with a macron in the file name; recurrence prevention for the class is the
shared helper, not a fix in `board.py` alone.

**SG2 — MODERATE (doctrine; the principal's).** The sweep removed the only
imperative statement of the sibling-dirty stop. Before `b2a54f1`, § *On a split
board* said *a dirty sibling item state line is a stop for claiming from that
checkout, not a stage-yours-alone case*. At HEAD that sentence is replaced by an
italic pointer — the rule "this wording carried while the check was unbuilt … is
CF3's to restate or relax … see there" — and CF3 received no restatement: its
branch list still keys branch B on *the item's file itself*, and the 🎯 paragraph
says only "It has not been relaxed here". A rule asserted to stand has no
sentence that states it. This is `320/120`'s findability defect made worse by
the very sweep, and `320/120` is not cited. *Counsel:* one sentence in CF3's
branch list, in the imperative, until `010/160` is ruled; whichever way the
ruling goes, the rule needs a home, and the split-board pointer should point at
a sentence that exists.

**SG3 — MODERATE (doctrine; the principal's).** The relaxation put up for
ruling rests on a premise the probe falsifies. The 🎯 paragraph, `010/160` and
the ADR's "one consequence left open" all say `--from-index` closes the
mechanical cause, so "a sibling's dirty edit to a different item" could stop
being a stop. It closes the **unstaged** half only. S2b: the sibling's edit
staged in the shared index is absorbed by `rebuild --from-index` (1 line), the
staged check passes, the claim commit carries three files including the
sibling's hunk. S2c: `commit --only` your paths is blocked. So under the
relaxation as worded a claimer would commit a peer's staged work under its own
message. The account the principal rules on must say "unstaged", and the staged
case is a stop on mechanical grounds whatever is decided about peer presence.
*Counsel:* amend the three spellings to "unstaged" before the ask is put;
record S2b/S2c as the grounding.

**SG4 — minor (code).** Unmerged and intent-to-add entries are misdiagnosed.
S3b: `git ls-files` prints a conflicted item path once per stage, so the check
reports "item number 160 is used 3 times" naming one file thrice, plus three
"no state line" lines, and `rebuild --from-index` drops the item from the disk
index. S5: an `add -N` entry reads as "no state line" while `git commit` silently
leaves the file out. Both fail closed; both print a remedy that cannot resolve
the state. *Counsel:* read `ls-files --stage`, and name unmerged / intent-to-add
entries as such ("resolve the item file first"); one test each.

**SG5 — minor (code).** The staged reader decodes with the process locale; the
worktree reader pins UTF-8. Under a Latin-1 locale (S12) every `⏳` item reads
"no state line" and `rebuild --from-index` rewrote the disk index with mojibake
(236 insertions, 256 deletions) before returning 1. Exposure is low — Python
coerces the C/POSIX locale to UTF-8, and a Latin-1 shell is rare — but the two
planes disagree by construction. Shared cause: `harvestscan.git_show` passes no
`encoding`. *Counsel:* `encoding="utf-8"` in the one helper.

**SG6 — minor (code).** A git failure reads as "no board". S13: with a corrupt
`GIT_INDEX_FILE`, `rev-parse` still answers true, `ls-files` exits 128, and
`--check --staged` prints "✓ board not in scope" and exits 0. The docstring's
"it is not fail-open" is false for this branch. Unreachable through `git
commit` (git reads the index before the hook), reachable by hand and by any
other caller; `harvestscan.list_markdown` returns `[]` the same way. *Counsel:*
exit 2 when `ls-files` fails; the "not in scope" verdict only on a clean empty
listing.

**SG7 — minor (completeness).** `CHANGELOG.md` carries nothing for `--staged`,
`--from-index` or the hook wiring. The 2026-09-20 section mentions `board` only
under the bounded-memory item. A fleet-wide change to what the hook checks, with
a changed printed remedy, is the log's purpose.

**SG8 — minor (harvest).** `010/160` ignores two open items on the same
clause: `320/120` (child-filed, whose options (ii)/(iii) are this decision, and
which quotes the interim wording as interim) and `030/140` (the yield branch on a
monolithic board). Three open items now ask the principal to rule on CF3 from
three framings with no cross-reference. *Counsel:* one ruling ask, `010/160`
pointing at both; SG2 and SG3 land on the same ask.

**SG9 — note (tests).** `test_floor` pins `--staged` on `harvestscan`'s hook
template and not on `board`'s; the `StagedPlane` class exercises `board.main`,
not the registry. A registry edit dropping `--staged` from `board`'s hook line
passes the suite. One assertion closes it.

**SG10 — note (doctrine hygiene).** The 🎯 paragraph in `CONCURRENCY.md`
restates `010/160`'s content inside standing doctrine — a ruling ask in two
homes. On ruling, one of them must be swept; the safer home for the ask is the
board item, with the doctrine carrying the rule.

**Overall: PASS-WITH-FINDINGS — 0 MAJOR / 3 MODERATE / 5 minor / 2 note.**
The code does what it claims for every state driven, and both BS1 slips are
caught at the hook live; the MODERATEs are one silent gap in the new reader's
input handling and two defects in the doctrine text that must be right before
the principal rules on CF3.

## Re-run ledger

| Command (clone at `c4b9cd0` unless stated) | Result |
|---|---|
| `python3 tools/board.py --selftest` | `board selftest OK`, exit 0 |
| `python3 -m unittest tools.test_board tools.test_floor tools.test_precommit` | exit 0, 2 m 44 s |
| `python3 -m unittest discover -s tools` (once) | `Ran 1564 tests … OK`, exit 0, 6 m 26 s |
| `floor.py --plane hook --root . --tools tools` | exit 0, `board ✅ enforced`, 22 s |
| `floor.py --plane ci --root . --tools tools` | exit 0, `board ✅ enforced`, 38 s |
| `_render` of the `board` entry, both planes | hook `--check --staged --root R`; CI `--check --root R R` |
| `--check`, `--check --staged`, `--rebuild`, `--rebuild --from-index` on the clean clone | all exit 0; three index files one SHA-256 |
| S1 slip (a) | worktree 0 · staged 1 · hook BLOCKED by board · after `add` hook passes |
| S2 slip (b), sibling unstaged claim line | plain rebuild absorbs 1 line · `--from-index` 0 · staged 0 · worktree 1 · hook passes · commit = 2 files |
| S2b sibling **staged** edit | `--from-index` absorbs 1 · staged 0 · hook passes · commit = 3 files incl. sibling's hunk |
| S2c same, `commit --only` own paths | hook BLOCKED (stale against staged) |
| S3 merge, index conflicted only | staged 1 with `--from-index` remedy · rebuild resolves · staged 0 · merge commit passes hook |
| S3b merge, item conflicted | ls-files ×3 · "used 3 times" + 3× "no state line" · rebuild drops item, exit 1 |
| S4 partial staging (i)/(ii) | (i) staged 0, worktree 1 · (ii) staged 1 → rebuild → 0, worktree 0 |
| S5 intent-to-add | ls-files lists empty blob · staged "no state line" 1 · `git commit` excludes the file |
| S6 rename staged / unstaged | 1,1 → rebuild → 0,0 · unstaged: staged 0, worktree 1 |
| S7 delete staged / unstaged | 1 → rebuild → 0,0 · unstaged: staged 0, worktree 1 |
| S9 `commit -a` / `commit -- item` | passes / BLOCKED while the real index was clean |
| S9b same in a linked worktree | BLOCKED / passes |
| S10 child via `hooks.atelierTools`, then `ATELIER_TOOLS` | seed passes · stale BLOCKED with child-spelling remedy · fixed passes · symlinked tools + cwd `/` exit 0 · monolithic out of scope · newly-split: staged out of scope, worktree stale |
| S11 names: space, leading dash, macron; root with space | space/dash fine · macron C-quoted, dropped on the staged plane (rebuild exit 0, 497 vs 498 lines) · staged 0, worktree 1 · root-with-space exit 0 |
| S12 `LC_ALL=C` / `LC_ALL=en_US.ISO8859-1` | C: exit 0 · Latin-1: 20× "no state line", rebuild rewrote index (236+/256−), exit 1 |
| S13 corrupt `GIT_INDEX_FILE` | ls-files 128 · rev-parse true · `--check --staged` "not in scope" exit 0 |
| `coldsweep` for interim wording / new flags / board-hook descriptions | 17 / 180 / 21 hits; rule-2 bar on; `010/020` + `115/080` excluded from the second and third sweeps |

## Follow-up checklist

- [ ] SG1 — `ls-files -z` in the shared helper; macron-name test; check HV4's
      `list_markdown` with the same fixture.
- [ ] SG2 — one imperative sentence for the sibling stop in CF3's branch list
      (the principal's; pending `010/160`).
- [ ] SG3 — "unstaged" in the three spellings of the relaxation before the ask
      is put; S2b/S2c cited as grounds.
- [ ] SG4 — unmerged / intent-to-add named as such; two tests.
- [ ] SG5 — `encoding="utf-8"` in `harvestscan.git_show`.
- [ ] SG6 — exit 2 on a failing `ls-files`; docstring's "not fail-open" made
      true.
- [ ] SG7 — CHANGELOG entry under 2026-09-20.
- [ ] SG8 — `010/160` cross-referenced with `320/120` and `030/140`; one ask.
- [ ] SG9 — assert `--staged` in `board`'s hook template in `test_floor`.
- [ ] SG10 — on ruling, sweep the duplicated ask out of one home.
