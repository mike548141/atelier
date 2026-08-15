# Cold pass — the board store migration (per-item files + generated index)

**Pass type:** combined doctrine + code cold pass (REVIEW.md rule 4 — the
delta carries self-authored doctrine *and* the mechanism that enforces it).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-15 (wt: `board-per-item-0815`; see *What the work is*).
- **Who wrote this brief:** a cold session Mike opened on 2026-08-15 with
  the standing instruction, verbatim: *"As a cold session please do any review
  work, any work that is fable dependent, and write briefs for any reviews
  that need them. If you write the brief then do not run the review, that
  will require another cold review session."* That session authored no part
  of this delta, was neither started nor instructed by the authoring session,
  wrote this brief from the delta and the queue pointer only (it did not open
  the intent record), and **stopped** — it did not run the review.
- **Who takes the review:** the next cold session that meets rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in
  the verdict: how it was spawned, and its non-involvement with both the
  authoring session and the brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling file
  `2026-08-15-1030-board-store-migration-cold.deferred.md` (rule 1's split):
  the intent-record reference, the prior-verdict references, and the
  brief-writer's seeded questions. Recommended: the taker runs the review
  under an orchestrator that holds the sibling's bytes and hands them to the
  reviewer only after its findings are durably written — the one shape
  honestly called structural. A taker reviewing by hand opens the sibling as
  a deliberate second act after its findings are written, and says so in the
  verdict. Either way the sibling is folded in below the verdict and deleted
  when the verdict lands.

## What the work is

Landed 2026-08-15 on `main` as the series `da6ba70` (claim) → `8ce1bb7`
(toolchain) → `a9abc26` (store migration) → `15d3de2` (doctrine, ADR,
changelog) → `10354e3` (records + this review's queue pointer) → `2f07ee8`
(merge). Reviewed at HEAD:

1. [`tools/board.py`](../../tools/board.py) and
   [`tools/test_board.py`](../../tools/test_board.py) — the generator for
   `docs/ROADMAP.md` and its `check`/`rebuild` modes.
2. [`tools/floor.py`](../../tools/floor.py) — the new `board` entry in the
   floor registry, wired enforced on both planes.
3. [`tools/harvestscan.py`](../../tools/harvestscan.py),
   [`tools/test_harvestscan.py`](../../tools/test_harvestscan.py) and
   [`tools/pointerscan.py`](../../tools/pointerscan.py) — the reach changes
   that let the two item-grammar scanners read a split store and skip the
   generated index. [`tools/README.md`](../../tools/README.md) catalogue rows.
4. The store itself: [`docs/roadmap/`](../roadmap/) — the preamble
   `README.md`, one `README.md` of narrative per section, one file per item;
   and [`docs/ROADMAP.md`](../ROADMAP.md), now a generated index. The
   pre-migration `docs/ROADMAP.md` is the parent of `a9abc26`.
   [`docs/ROADMAP-DONE.md`](../ROADMAP-DONE.md) gained a frozen-store note.
5. Doctrine moved with the mechanism: [`docs/method/RECORD.md`](../method/RECORD.md)
   § *The roadmap*, [`docs/method/CONCURRENCY.md`](../method/CONCURRENCY.md)
   § *Claiming work* (the split-board paragraphs), the repo
   [`CLAUDE.md`](../../CLAUDE.md) read-order line, and the decision record
   [`docs/decisions/2026-08-15-0610-board-store-per-item-files.md`](../decisions/2026-08-15-0610-board-store-per-item-files.md).
6. The `CHANGELOG.md` entry that landed with them.

## Scope

Widest the work admits (REVIEW.md § *What a review actually checks*): the
intent the split claims to serve, the decision as recorded, the store layout,
the generator and check, the two scanners' reach changes, the tests (a wrong
test verifies nothing), the fidelity of the migration itself, and the doctrine
as it will bind future sessions and child repos. **Non-goals — one, and it does
not fence the risk:** the reviewer does not decide any finding. Doctrine here
is self-authored; findings are the principal's to rule on (rule 3). Counsel may
be recorded, labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is one-file-per-item with a committed, checked, generated index the
   right shape for the three problems the ADR names? What does the store now
   assume about how sessions and scanners find work?
2. **Correctness & quality** — run the tools live: `check`, `rebuild`,
   the floor on both planes, harvestscan and pointerscan over the split store,
   the suites. Does the generator's grammar match every item state the
   scanners already speak? Is the index a faithful projection?
3. **Completeness / harvest** — what should the migration have carried and
   did not? Is every line of the pre-migration board accounted for in the
   store? What existing doctrine now says the monolithic thing while the
   mechanism says the split thing?
4. **Security & privacy** — mandatory. atelier is PUBLIC: 118 item files and
   27 narratives were re-homed in one commit — check whether the move surfaced
   or re-linked anything that joins a private repo's name to its posture, and
   what the new store causes future records to carry. If the lens genuinely
   has no surface beyond that, discharge it in one explicit line with grounds.
   The house security scanner reads pending diffs; this is a landed-delta
   review, so state the reach case that applied.

## Re-run obligation

Re-run, do not read: the full suites (house invocations live in
[`.githooks/pre-commit`](../../.githooks/pre-commit) — lift them, do not
guess); the test-count claims at the landing commits; the board check in both
its passing and its drifted state (edit an item file, run `check`, restore);
the migration fidelity claim (4,063 lines → 27 sections / 118 items, index at
253 lines) by comparing the pre-migration board against the store; harvestscan
and pointerscan on the split store; and the claim mechanics on a split board
described in CONCURRENCY (make a claim in a scratch clone and observe what
collides).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/`, and the intent record for this delta.
The sibling `.deferred.md` holds those references and the brief-writer's seeded
questions; open it after your findings are committed. Reconcile after, never
anchor before. A taker whose own session onramp has already read the
`SESSIONS.md` tail discloses that in the verdict.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `BS`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/010-board-store-migration-per-item-files-mik/050-rule-4-cold-pass-queued.md`)
and rebuild the index in the same commit.

---

# Verdict — cold pass on the board-store migration (per-item files + generated index)

**Provenance, repeated.** Reviewer: a cold rule-4 reviewer on the Fable tier, spawned by this pass's orchestrator — a Fable session Mike opened on 2026-08-15 at about 1120 UTC under his standing cold-session instruction (do any review work, any Fable-dependent work, write briefs for reviews that need them; a brief-writer never runs its own brief) and pointed at the review queue. The orchestrator authored no part of this delta and was neither started nor instructed by the authoring session or by the brief-writing session (a separate cold session earlier on 2026-08-15); the reviewer likewise. The `.deferred.md` sibling was withheld under the orchestrator's context partition — moved out of the worktree before this reviewer was spawned — so nothing below this line was written with it, the intent record, or any prior verdict in hand. Orchestrator's disclosure: its own session onramp read the tail of `docs/SESSIONS.md`, whose index entries summarise these deltas; the reviewer did not, and received only the brief and this preamble.

Reviewer's own reading, disclosed. (1) I read the pre-migration `docs/ROADMAP.md` at `a9abc26^` in full — it is the delta's source and it carries every item's author account; the brief authorised this and I say so here. (2) Board items read beyond my own pointer: all six files of `docs/roadmap/010-board-store-migration-per-item-files-mik/`, `docs/roadmap/README.md`, the generated index, and lines 340–368 of `docs/roadmap/020-policy-as-code-programme-five-tracks-mik/README.md` (to trace a pointer that lives in narrative — BS3). Nothing else under `docs/roadmap/` was opened beyond `head -1` and grep counts. (3) The `/security-review` skill, invoked for lens 4, printed the shared worktree's pending diff — which at that moment was *another* pass's brief and its `.deferred.md` sibling (the reply-gate pass, prefix RG) plus commit messages on `main` after my HEAD. None of it concerns this delta; I read no further into it and ran none of the skill's sub-tasks over it. It is the SL2 class REVIEW.md warns about, and it is disclosed here rather than hidden. My own sibling was not exposed. (4) Not read at any commit: `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` (its `a9abc26` hunk included), any other file under `docs/reviews/`, the intent record.

**The delta reviewed.** `da6ba70` (claim) → `8ce1bb7` (toolchain) → `a9abc26` (store migration) → `15d3de2` (doctrine, ADR, changelog) → `10354e3` (records + queue pointer; its `docs/SESSIONS.md` and `docs/sessions/` hunks not read) → `2f07ee8` (merge). Worktree HEAD was `3d0df11` when the pass began and `fe4908b` when this verdict was written (the orchestrator committed an unrelated brief into the shared worktree mid-run); `origin/main` had moved on to `1b46d05` and beyond. Surfaces that moved after landing and are **out of scope** here: the six item files added or edited under `docs/roadmap/` by `4ea0a8f`, `35ce01d`, `3d0df11` and the post-`3d0df11` commits — cited below only as *evidence of how the landed doctrine behaves in use*, never reviewed as work. Scratch clones: `bs-clone` (suite runs at each landing commit) and `bs-clone2`/`bs-clone3` (mutation and claim probes, hooks enabled via `core.hooksPath`), both under this session's scratchpad; nothing pushed.

## Load-bearing assumptions, named first

1. **State is the item file's first line and nothing else; the index derives from it.** — Held for the state glyph; **fails** for the claim fragment and the eye-flags in the shape this house actually writes items (BS2), and fails outright for the pointer and ruling asks that landed inside section READMEs (BS3).
2. **A stale index cannot reach `main`: the `board` check on both planes makes forgetting the rebuild impossible.** — Held on CI. **Fails on the hook plane** in the two easiest slips (rebuild done, index unstaged; a sibling's dirty item absorbed by rebuild), one of them the sequence CONCURRENCY prescribes (BS1).
3. **The index is a short, faithful projection read every session.** — Short today (259 lines). Faithful for glyphs; **fragmentary for titles** on 52 of 124 items (BS2). **Unbounded**: nothing retires ✅ lines, and the only signal that would fire prints a retired remedy (BS4).
4. **Same-item claims still collide; different-item claims never do; an index conflict is resolved by regenerating.** — **Held**, exercised live in three claim shapes (lens 2).
5. **The migration is lossless.** — **Held**: line-multiset comparison old board vs store, only the preamble differs, by design (lens 3).
6. **The board's binding rules still reach every session at open.** — Weakened: the legend and claim rules moved off the ordered read to a linked file (BS5).
7. **A `docs/roadmap/` directory means the repo has adopted the split.** — Assumed, not declared; the consequence is an unsoftenable block on a name collision (BS8).

## Lens 1 — approach & assumptions

Is one-file-per-item plus a committed, checked, generated index the right shape for the three problems the ADR names? For two of the three, yes, and the evidence is good: contention at file grain is genuinely fixed (P5: different-item claims touch different files; the only shared write surface is the index and its conflict resolves mechanically — observed), and provenance-by-`git log` is real (each item file's history is exactly its state history). For the third — read cost — the shape fixes today's number and removes the only mechanism that bounded it (BS4). The design also silently traded a fourth property away: the legend and the claim rules that were the top of the hot-path file are now one link away from it (BS5).

The framing I attacked hardest: "state lives in the first line". The generator reads the first *physical* line; the house writes items as an 80-column-wrapped logical line with the bold title, flags and claim fragment spread over three to five physical lines (0 of 124 item files are single-line; da6ba70's own claim sat on its fifth). The mechanism and the fixtures assume a shape the store never had. That is a projection-fidelity defect (BS2), and it also means the mechanism cannot enforce the claim grammar at all — a `[ ]` item with a claim appended in its body passes `check` green (P2b), which is exactly the shape the first post-split claim took (`4ea0a8f`, out of scope, cited as evidence).

The migration script "lives in the session's scratch space by design" (ADR, Consequences). I accept that the artefact under review is the tree, and the tree passes the fidelity test — but one call the script made is not named anywhere: 58 top-level bullets that were not checkbox-grammar (17 of them 🎯 ruling asks, one a live ⏳ pointer) became narrative, not items (BS3). The ADR names "position within narrative" as the accepted cost; it does not name "some asks and one pointer are no longer items".

Threat enumeration at design altitude (REVIEW.md lens 4's build-time obligation): none recorded in the ADR. For this class (local file generation, no network, no untrusted input) the honest enumeration is short — a stale index asserting a wrong state, and a rebuild absorbing another session's hunks — and both are exactly the two live findings here (BS1). Absent enumeration is the finding-shape REVIEW.md names; folded into BS1 rather than raised twice.

## Lens 2 — correctness & quality (everything re-run, nothing read)

- **Suites at each landing commit** (scratch clone, `python3 -m unittest discover -s tools -p 'test_*.py'`): `da6ba70` 1298 OK · `8ce1bb7` 1321 OK · `a9abc26` 1321 OK · `15d3de2` 1321 OK · `10354e3` 1321 OK · `2f07ee8` 1321 OK · `3d0df11` 1321 OK. `tools/test_board.py` alone: 14 tests. `tools/test_harvestscan.py`: 26 → 35 (+9, of which 3 are the new `SplitBoardTest` methods and **6 are `GitBackedTest`'s methods run a second time by inheritance** — BS6). Node instruments: `node --test instruments/*.test.js` at HEAD → 235 tests, 235 pass, 0 fail, exit 0.
- **Selftests**: `python3 tools/board.py --selftest` → `board selftest OK`; `python3 tools/floor.py --selftest` → `ok (15 scanners, 0 failure(s))`.
- **Floor at HEAD (worktree, read-only)**: `--plane ci` exit 0 with `✅ board enforced`; `--plane hook` exit 0 with `✅ board enforced`. Steady-state 🟡/👁️ lines present as expected. CI on `2f07ee8` (full SHA): `floor` success.
- **Board check, passing and drifted** (`bs-clone2`, P1): flip an item's first line `[ ]`→`[~]` with the claim fragment on that line → `check` exit 1 with the remedy printed; `rebuild` → 259 lines; `check` exit 0; index shows `[~]` and the fragment. Restore → clean.
- **Hook live** (`bs-clone2`, `core.hooksPath=.githooks`, P3): item edit staged, index not rebuilt → hook blocks (`❌ board enforced`), HEAD unchanged. Rebuild + stage index → commit lands, `check` exit 0. **P6**: item staged, index *rebuilt but not staged* → hook **passes** (`✓ board index current`), commit lands **without** the index; `check` on the committed tree → exit 1. **P4**: a sibling item's state line dirty and unstaged; my claim + `rebuild` + stage my item and the index → hook passes; the committed index carries the sibling's `✅` while the sibling's file on `main` still says `[ ]`; `check` on the committed tree → exit 1. → BS1.
- **Projection probes** (P2): claim fragment on a continuation line → `[~]` shown, fragment not (P2a); claim appended, no glyph flip → `check` green, index unchanged (P2b); 🎯 on line 2 only → not lifted (P2c); multi-line leading HTML comment → "no state line" defect (P2d, BS9); a title containing `[…]` → renders as a CommonMark-legal nested-bracket link that `linkscan` does not parse, so a broken target there would go unseen (P2e, note).
- **Census over the real store**: 124 item files; 52 whose bold title does not close on line 1 (fragment titles in the index); 10 eye-flags present only on a continuation line; 3 of 3 real claim fragments on continuation lines. → BS2.
- **Claim mechanics** (P5/P5b, two clones): different-item claims on adjacent index lines → `CONFLICT` on `docs/ROADMAP.md` only; `rebuild` + `add` + `rebase --continue` → clean, `check` exit 0, both `[~]` lines present. Same-item claims → `CONFLICT` on the item file in all three shapes (fragment on the state line; bare flip + fragment appended; fragment appended with no flip). Doctrine holds here.
- **harvestscan on the split store**: at `a9abc26` (clone checkout) `--against a9abc26^` → clean, 0 findings; `--only-bulk-deletes` → not in scope (net −226, a *gain*, because `docs/roadmap` now sits in `GATE_RECORDS`). `pointerscan --root . .` at HEAD → clean, 0 suppressed. `linkscan --root . .` → clean. `sizescan --root . .` → the ROADMAP advisory is gone (one unrelated advisory remains).
- **Index line claims**: 253 lines at `a9abc26` and `15d3de2`, 257 at `2f07ee8` (holds). 118 index items / 27 sections at `a9abc26` (holds).
- **Convention slips**: `python3 tools/board.py --root . .` (the house scanner invocation) → argparse usage error, exit 2; the docstring calls the mode `--check`, the CLI is positional `check` (BS7).

## Lens 3 — completeness / harvest

- **Fidelity**: multiset of non-blank lines, old board (3,740) vs concatenated store at `a9abc26` (3,749): every non-preamble line of the old board is present verbatim (link lines identical after `../` re-basing); the only lines missing are the old preamble (rewritten as `docs/roadmap/README.md`) and 27 `##` headings (now `#` in section READMEs). "All 4,063 lines accounted for" holds in substance; the preamble was *rewritten*, not moved, and that doctrine edit landed in the migration commit rather than the doctrine commit (BS11, note).
- **What the migration carried and did not name**: 58 top-level non-checkbox bullets became README narrative; among them 17 🎯 asks (12 of the form "REVIEWED … PASS-WITH-FINDINGS", i.e. rulings owed) and one live ⏳ pointer. The index shows 30 🎯 where the old board's top level carried 47, and 8 ⏳ where the store holds 9 (BS3).
- **What existing doctrine now says the monolithic thing**: `tools/sizescan.py` still prints "harvest completed [x] items to ROADMAP-DONE.md" as the ROADMAP.md remedy and budgets the index at ~300 lines (BS4); `harvestscan --records` help still names the two-file default (BS7); `docs/method/CONCURRENCY.md` line 581 "the roadmap harvest" (queued under the 040 sweep item — fine); `tools/floor.py` docstring's non-softenable set omits `board` and `tools/test_floor.py` does not pin it (BS7); `docs/decisions/README.md` indexes 16 of 17 ADRs — this one is missing (BS7).
- **Follow-ups the delta queued** (020 staged-plane seam, 030 fleet rollout, 040 wording sweep) are the right three; 020 names only one direction of the seam (BS1).
- **CHANGELOG**: present and accurate except the test count (BS6).

## Lens 4 — security & privacy

Design altitude: the store re-homes verbatim text under new file names; the slugs are the first 46 characters of each item's first line, so nothing appears in a filename that was not already on the public board. No new join of a private repo's name to its posture was found in the moved text (grep over the store, records excluded). One note: the new fleet-rollout item names three private repos with their board line counts in a public record — a line count is not posture, but the ADR itself cites the *open* estate-internal-context ruling as grounds to reject GitHub Issues, so this belongs in front of that ruling (BS10, note). Code altitude: `board.py`, `harvestscan.py`, `pointerscan.py` are stdlib Python; every subprocess call is a list-form `git` invocation (no shell); paths come from `--root` (a trusted CLI flag) and the fixed `docs/roadmap` prefix; the only write is `docs/ROADMAP.md` under root. No injection, deserialisation, or traversal surface. `/security-review` reach case: **landed-delta; the scanner reads the pending diff, and the shared worktree's pending diff held none of this delta** — it held another pass's material (disclosed above), over which I ran nothing. Its markdown exclusion would have made a clean pass over this delta's doctrine definitionally empty in any case. Weight: nothing; discharged with those grounds.

## Findings

**BS1 (MAJOR)** — The hook-plane guarantee is asserted in four places and does not hold; one failing path is the sequence CONCURRENCY prescribes.
- *What.* `board.py` docstring ("a commit whose index does not match its item files fails"), `tools/README.md`, the ADR (Decision) and `docs/method/CONCURRENCY.md` § *On a split board* ("the `board` floor check makes forgetting it impossible"; CF3: "stage and commit the claim alone … safe because it stages only your own hunks") all state that a stale index cannot be committed. The check compares worktree to worktree, so at the hook plane it passes whenever the two agree on disk regardless of what is staged.
- *Where / evidence.* P6 (`bs-clone2`, hook enabled): `- [ ]`→`- [~]` in an item, `rebuild`, `git add <item>` only → hook prints `✓ board index current`, commit lands with the item and **not** the index; `board.py check` on the committed tree → exit 1. P4: a sibling item's state line dirty and unstaged (`[ ]`→`[x]`), my claim + `rebuild` + `git add <mine> docs/ROADMAP.md` → hook passes; `git diff HEAD~1 HEAD -- docs/ROADMAP.md` shows the sibling's line flipped to `✅` while its file is unchanged on `main`; `check` on the committed tree → exit 1. In P4 the alternative — not rebuilding — is blocked (P3), so under CF3 the claimer's only moves are "commit a wrong index" or "abandon the claim"; `git add -p` on the index is nowhere written.
- *Why it matters.* The index asserting a state the item files do not hold, landed on `main` under a green hook, is the exact defect class the ADR names as the split's third motivation ("state asserted, not derived"). CI catches it after the push, so `main` is wrong for the window and the next `pull` hands every session a lying index. The 020 follow-up names the seam in the item-staged-index-not-rebuilt direction only; the doctrine text names no residual at all.
- *Counsel (the reviewer decides nothing).* (a) Bring `check` to the staged plane (harvestscan's HV4 shape: build the index from `git show :path` of each staged/HEAD item file and compare to the *staged* index), so P6 and P4 both block; (b) give `rebuild` a source flag so a claimer at a dirty primary can regenerate from the index rather than the worktree, and name that in CF3; (c) until then, CONCURRENCY should say the residual plainly — a dirty sibling *item state line* is a stop for claiming from that checkout, not a "stage yours alone" case — and the four "cannot drift" sentences should say "on CI; at the hook only when worktree and index agree".

**BS2 (MODERATE)** — The index projects the first *physical* line; the house writes items as wrapped logical lines, so titles are fragments and claims and flags go missing.
- *What.* `item_state()` returns the remainder of the first non-comment line; `index_line()` lifts title, flags and the claim fragment from that string only. The store's items are 80-column wrapped: 0 of 124 files are single-line; 52 have a bold title that closes on a later line (index shows the fragment before the wrap, e.g. "B4 — the roadmap-deletion guard: BUILT, MEASURED, and deliberately"); 10 eye-flags and all 3 real claim fragments sit on continuation lines and do not surface. `board.py` line 84 promises "who has this is one glance"; for every claim this repo has actually made (da6ba70 pre-split, `4ea0a8f` and the 180 pointer post-split — the latter two out of scope, cited as evidence) it is not.
- *Where.* `tools/board.py` `item_state`, `index_line`, `TITLE_RE`; the selftest and `tools/test_board.py` fixtures are all one-line items — the suite pins a shape the store never has. P2a/P2c reproduce.
- *Why it matters.* The index is now the session-start read; ~40 % of its titles are truncated mid-phrase, and the claimed-by fragment — the one fact CONCURRENCY says a session must see before taking an item — is invisible for the house claim shape. It also means the check cannot see a claim that leaves the glyph alone (P2b), which is what the first post-split claim did.
- *Counsel.* Define the "state line" as the logical line — from the glyph to the first blank line, sub-bullet, or end of file — and lift title/flags/claim from that; add a fixture shaped like a real item (wrapped title, claim on line 4). Optionally have `check` warn on a body-resident `(claimed …)` under a `[ ]` glyph.

**BS3 (MODERATE)** — Ruling asks and one live review pointer migrated into narrative and are invisible to the index and to the one-file-per-item promise.
- *What.* The migration's item test was "top-level line matching the checkbox grammar". 58 top-level bullets that were not (17 carrying 🎯, one carrying an embedded ⏳ pointer — the plainscan repo-plane rescope, `docs/roadmap/020-…/README.md` lines 342–368) became section-README narrative. The index renders 30 🎯 where the old top level carried 47, and 8 ⏳ where the store holds 9. Claims on that pointer edit the shared section README (`35ce01d`, `3d0df11` — out of scope, cited as evidence), which is the collision surface the split was meant to remove.
- *Why it matters.* The ADR's own grounding for the split includes "a whole duplicated Fable review pass run off a stale ⏳"; a ⏳ that the index cannot show is the same hazard from the other side. And 17 of the "~67 items awaiting Mike's ruling" the ADR counts are not items on the board that is meant to drain them. Neither the ADR's Consequences nor the migration record names this cost.
- *Counsel.* Either promote each such bullet to an item file with a state line (`- [ ] 🎯 …` / `- ⏳ …` — a one-off, mechanical), or teach the generator to render README-resident ⏳/🎯 lines under the section with a distinguishing glyph; and add the cost to the ADR's Consequences either way. `pointerscan` already reads the READMEs (it is clean), so the pointer grammar is not at risk — the visibility is.

**BS4 (MODERATE)** — Read cost, the ADR's strongest fact, is now unbounded, and the one signal that would fire prints a retired remedy.
- *What.* The harvest step is retired; a done item stays `[x]` in its file and `✅` in the index forever. Nothing bounds either. `tools/sizescan.py` still budgets `ROADMAP.md` at ~300 lines and its printed remedy is "harvest completed [x] items to ROADMAP-DONE.md (keep only what's open)" — the step RECORD.md and the board README now say does not exist. The index was 253 lines at landing and 259 five hours later (+6 items); the advisory is roughly 40 items away.
- *Where.* `tools/sizescan.py` `SIZE_REFERENCE`, remedy strings; ADR Consequences (silent on this); `docs/method/RECORD.md` § *The roadmap* ("current-truth files stay lean; history relocates" — no longer owned by any mechanism for the board).
- *Why it matters.* The split was justified on read cost and then removed the only lever that bounded it, without a replacement or a statement that none is needed. When the advisory fires it will tell the reader to do a thing the doctrine forbids.
- *Counsel.* Decide what bounds the index — e.g. the generator renders open/claimed/⏳ items and a per-section done count (or a second generated done index), so ✅ lines never accumulate on the hot path — and re-word sizescan's ROADMAP remedy for the split case. If "unbounded is fine" is the ruling, the ADR should say so and sizescan's budget for a generated index should be grounded accordingly.

**BS5 (MODERATE)** — The legend and the claim rules left the ordered read.
- *What.* The old board's preamble (checkbox tri-state, `[~]` means don't start, refs-only pointer, landing = queuing, inline-claim close) was the top of the file every session read. It is now `docs/roadmap/README.md`, reached by one link from the index; `CLAUDE.md` read-order step 5 names the index only. The generator declines to inline it on the grounds that relative links break at two depths — true, and solvable (rewrite the two links at generation time, or emit a link-free one-line legend).
- *Evidence.* First post-split claim on `main` (`4ea0a8f`, out of scope) appended a claim fragment without flipping to `[~]` — the legend's rule; causation not proven, consistent with the rule having dropped off the read path.
- *Counsel.* Name `docs/roadmap/README.md` in the read order beside the index, or have the generator emit the legend line without links.

**BS6 (minor)** — Test-count claims disagree with each other and with the suite; the harvest test class re-runs six inherited tests.
- Commit `8ce1bb7`: "suite +17". CHANGELOG: "+13 tests" (board) and "+3" (harvestscan) = 16. Migration item: "suite +20". Measured: 1298 → 1321 = **+23** at `8ce1bb7`, of which 14 board + 3 harvestscan are new and **6 are `GitBackedTest` methods executed again under `SplitBoardTest(GitBackedTest)`** (`unittest -v` lists nine `SplitBoardTest.*` cases). Also `test_bare_tree_exits_zero_and_says_why` asserts the exit code only — the module docstring says the test pins that it "says so". Counsel: make `SplitBoardTest` inherit a helper mixin, not the test class; assert on stdout; correct the three counts (the ADR's "+13" is the same figure).

**BS7 (minor)** — Catalogue and convention mismatches around the new check.
- `board.py --root . .` (the house scanner form) exits 2 with a usage error — `action` is a positional with choices, so the first path is parsed as the mode; the docstring says `--check`. `harvestscan --records` help still says the default is the two files. `tools/floor.py` docstring's list of checks with no advisory form omits `board`, and `tools/test_floor.py::test_boundary_and_integrity_checks_cannot_be_softened` does not pin it. `docs/decisions/README.md` indexes 16 of 17 ADRs — the board-store ADR is absent. Counsel: default the action to `check` when the first positional is not a mode; update the two help texts; add `board` to the pin and the ADR to the index.

**BS8 (minor)** — Adoption is inferred from a directory name and the block is unsoftenable.
- `run_check` treats any `docs/roadmap/` directory as the split board: missing preamble → problem (exit 1), missing index → stale (exit 1); `advisory=None` means a child cannot soften it. Fail-closed is the right direction, but a child with a `docs/roadmap/` folder for any other reason is blocked with no declared way out short of renaming. Not exercised on the fleet (private repos, not opened). Counsel: key adoption on the GENERATED marker in `docs/ROADMAP.md` or a declaration in `.atelier-floor.json`, and say in the not-in-scope message what would put the repo in scope.

**BS9 (note)** — A multi-line leading HTML comment defeats `item_state()` (P2d): only lines *starting* with `<!--` are skipped, so the second line of a wrapped allow-marker reads as prose and the file is reported stateless. Counsel: skip until the closing `-->`.

**BS10 (note, lens 4)** — The fleet-rollout item names three private repos with their board line counts in a public record, in the same delta whose ADR cites the still-open estate-internal-context ruling to reject GitHub Issues. Not a posture join; flagged so the open ruling sees its own class arriving.

**BS11 (note)** — The preamble was rewritten (correctly, as split-board doctrine) inside the migration commit `a9abc26`, whose message says "every line moved" and "narrative … verbatim"; the doctrine commit `15d3de2` does not mention it. Fidelity of every other line holds. A one-line correction to whichever record next touches it.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR / 4 MODERATE / 3 minor / 3 note.** The mechanism is sound where it was designed to be (different-item claims, index conflicts, lossless migration, CI enforcement) and the doctrine overstates it where it was not (hook-plane guarantee, first-line projection, bounded read cost). What an author must do: nothing on its own — this is self-authored doctrine and every finding above is the principal's to rule (REVIEW.md rule 3); the author may record its position beneath each. The cycle does not close on this pass (one MAJOR); the application of whatever is ruled earns its own cold pass per REVIEW.md, queued in the applying commit.

## Follow-up checklist

- [ ] BS1 — staged-plane `check` (and/or a rebuild-from-index source) — tested against P4 and P6 re-run in a hook-enabled clone: both must block; CONCURRENCY's four "cannot drift" sentences re-worded — tested by re-reading them against the residual as built.
- [ ] BS2 — logical-line projection — tested against the census (`bold closes on line 1` reaches 124/124 in the index; 0 hidden flags; the three real claim fragments render) and a new wrapped-item fixture in `test_board.py`.
- [ ] BS3 — README-resident asks/pointers promoted or rendered — tested by counting 🎯/⏳ in the index against the store's top-level total (47/9 today) and by `pointerscan` staying clean.
- [ ] BS4 — a decided bound for the index and a corrected sizescan remedy — tested by rebuilding with 40 synthetic ✅ items and reading what sizescan prints.
- [ ] BS5 — legend on the read path — tested by opening `CLAUDE.md` step 5 or the generated index head and finding the tri-state rule without following a link.
- [ ] BS6 — counts corrected, mixin instead of inheritance, stdout asserted — tested by `unittest -v` listing three `SplitBoardTest` cases and the suite delta matching the record.
- [ ] BS7 — CLI default, two help texts, floor pin, ADR index — tested by `board.py --root . .` exiting 0 and `test_floor` pinning `board`.
- [ ] BS8 — adoption keyed on marker or declaration — tested by a bare repo with an unrelated `docs/roadmap/` folder passing as out-of-scope with the reason printed.
- [ ] BS9 — multi-line comment skip — tested by P2d passing.
- [ ] BS10 — surfaced to the estate-internal-context ruling — tested by that ADR's record naming it.
- [ ] BS11 — one-line record correction — tested by reading it.

## Reconcile — post-verdict, against the intent record and the deferred questions

*Interruption disclosed:* this reconcile was begun after phase 1 landed (`b4fe720`), cut by an API session limit before anything was appended, and resumed on 2026-08-15 by the same reviewer with the same material; nothing was appended in between and the phase-1 text above is untouched.

Opened after phase 1 was committed (`b4fe720`), and only what the sibling names: `docs/sessions/2026-08-15-0610-board-store-migration.md` and its `docs/SESSIONS.md` line (257); items `010-…/020-…`, `030-…`, `040-…` (already read in phase 1 as board items — disclosed there); the three prior verdicts `2026-07-29-1306-b4-harvestscan-cold.md` (HV), `2026-08-05-1238-pointer-grammar-b4-wiring-cold.md` (PG), `2026-07-19-0407-review-trigger-sizescan-combined-cold.md` (F1–F9). Nothing in phase 1 above is revised; amendments are marked as such.

### Applied as ruled?

Yes. Mike's ask (verbatim in the record: three problems — concurrent corruption, file size, premature "done" — and "SQLite or something else") and his ruling ("I accept your recommendation. Proceed") match the ADR's Decision: weekly ruling sitting + option B, atelier first. The record's account of the second-pass corrections (a committed index must resolve conflicts by regeneration; `closed_by: <sha>` cannot survive landing-equals-bookkeeping) is what the build did, and P5 confirms the first of those live. The record's verification list (linkscan, harvestscan, sizescan advisory gone, datescan, suite green, every commit through the hook) reproduces in full — see lens 2. The ruling was applied as put.

### What the record resolves from the checklist

Nothing closes. The record names the staged-plane seam "HV4's class, stated at birth" and queues it (020) — but only in the item-staged / index-unrebuilt direction; neither the record nor 020 names P4 (a sibling's dirt absorbed by `rebuild` under CF3) or P6 (rebuilt, unstaged, hook green). BS1 stands as written. The record is silent on the 58 non-checkbox bullets (BS3), on what bounds the index once the harvest is gone (BS4), and on the legend leaving the read path (BS5). It confirms the design intent behind BS2's mechanism ("state is the item file's first line") without noticing the house writes wrapped items. The record does not change any severity.

### Divergences

- **Test counts, a third time inside the record itself.** The record body says `board.py` has "14 unit tests" and harvestscan "+3" (= 17); its own `SESSIONS.md` index line says "+20 tests"; the CHANGELOG says +13/+3; the commit says +17. Measured +23 with six inherited re-runs (BS6). Same figure, five spellings, none measured.
- **"The dirty-tree tell moves to the item file"** (record; CONCURRENCY). P4 shows the *sibling's* dirty item file is a tell the doctrine tells the claimer to disregard when it is not the claimer's item — and that disregarding it commits a wrong index. The tell moved; the rule about it did not.
- **The seam was already ruled on for a sibling scanner.** HV4 (ruled 2026-07-29, "accept": the wiring build handles the staged-vs-working-tree seam properly — the hook plane reads staged content) and PG1 (2026-08-05, MODERATE: a docstring claiming a staged read the tool does not perform) are the same class BS1 finds in `board.py` and its four doctrine restatements. The record calls the seam "stated at birth" — true of the tool docstring and `tools/README.md`, not of the ADR's Decision or CONCURRENCY, which state the stronger claim without the residual. Aggravating context for BS1; severity unchanged.
- **PG7 (net-line gate blind to terse-item massacres)** is not worsened by the split: item files are 3–40 lines and their index lines now count toward the gate too (`docs/ROADMAP.md` stays in `GATE_RECORDS`). Recorded because PG7 asked that a roadmap style shift re-open the question — this one did not shift the item shape.
- **F5 (sizescan, ruled 2026-07-19)** — "where a file is legitimately all-current, ground a budget or accept a standing red" — is the ruled path BS4 should be read against: a generated index that grows one line per item ever is neither "all-current" nor "harvestable" under the retired remedy; a class-grounded budget for a *generated* index is a third option F5's ruling already permits. Counsel under BS4 amended below to name it.
- **PG2 (file-level allow kill switch on line 1)** meets the board README's "an item file may open with an allow-marker": an item file that opens with a `pointerscan:allow:` marker is skipped whole by pointerscan while `board.py` indexes it as a live item. Pre-existing, unchanged by this delta; noted because the split makes line 1 of every item a first-class surface.

### Answers to the seven seeded questions

1. **Code-span glyphs lift as flags — yes, a projection defect, live.** `index_line` tests `f in rest` on the raw first line; item `130-…/010-…` opens with a backticked `⏳` in prose and renders `⏳🔎` in the index (`3d0df11` index line 133; still so at reconcile). `pointerscan` strips code spans for this reason; `board.py` does not. It re-creates the trap the 130 item describes — a non-pointer wearing the queue glyph in the first file a taker greps — one instance today. Recorded as **BS14 (minor)** below. My phase-1 ⏳ arithmetic under BS3 counted grep hits, not pointer lines; corrected in the amendment to BS3 below.
2. **Migration fidelity — held, including nested sub-bullets.** Line-multiset comparison (lens 3) found every non-preamble line present byte-for-byte after `../` re-basing; a re-parent or de-indent would change the line and show as missing, and none did. `160-…/080` and `090` keep their nested bullets verbatim (their lines are in the identical set). Allow-markers travel (the day-one datescan case is pinned by test and reproduced by P1). Only the preamble differs, by design (BS11).
3. **Stale index through the hook — yes; CI catches it.** Probed, not read: P6 (rebuilt but unstaged → hook green, index not committed) and P4 (sibling dirt absorbed → hook green, wrong `✅` committed). `board.py check` on each committed tree exits 1, which is what the CI plane runs against the pushed commit — so CI catches both, after the push. BS1.
4. **The GENERATED marker as a skip key — yes, an item file can escape pointerscan with it.** `pointerscan` tests `text.startswith(GENERATED_MARK)` — line 1 only, prefix match, any suffix. `board.py`'s `item_state` skips leading `<!--` lines, so an item file whose first line is the marker comment is indexed as a live item **and** skipped by pointerscan. It is a deliberate act with an audit trail (the line is in the diff), the same class as PG2's file-level switch, and no instance exists (grep: the marker appears only in the index and the two tools). Recorded as **BS12 (note)** with a one-line fix: skip only when the file *is* the index path, or have `check` reject the marker in an item file.
5. **Doctrine drift left behind — a residue, none of it a silent breach.** Surfaces still speaking monolith: `skills/queue-run/SKILL.md` step 4 ("mutate the item's `[~]` checkbox line on `main`" — no rebuild named) and line 71 ("roadmap harvest"); `docs/method/CONCURRENCY.md` line 581 ("the roadmap harvest"); `docs/build/templates/CLAUDE.md` step 2 and `templates/docs/ROADMAP.md` (correct for monolithic children — the fleet has not migrated); `tools/sizescan.py`'s ROADMAP remedy string (BS4). REVIEW.md rule 4's "ROADMAP `⏳`" wording still reads true. A session following queue-run's step 4 on the split board is *blocked* by the hook (P3), loudly and with the remedy printed — a stop, not a silent breach; the silent breaches are BS1's two, which no doctrine instructs except CF3's. All of this is the 040 sweep's scope; nothing here changes a severity.
6. **What stops accretion — nothing; and the cold-content gate is now silent for this board.** `sizescan`'s `COLD_CHECKBOX_FILES = {"ROADMAP.md"}` keys the `[x]` gate on the basename, so a `[x]` inside an item file is never seen, the index carries `✅` by design, and item files are not in `SIZE_REFERENCE` so they are never metered. The only signal left is the ROADMAP.md ~300-line advisory, whose remedy is retired. BS4 as written; F5's ruled third option (a class-grounded budget for the generated index) is the counsel amendment below.
7. **Children adopting half-way — the check fails closed, and the printed remedy would overwrite their hand-kept board.** A `docs/roadmap/` directory beside a hand-kept `ROADMAP.md` is reported *stale*, exit 1, unsoftenable — honest in the blocking direction (BS8 covers the name-collision case). But `rebuild` writes `docs/ROADMAP.md` unconditionally: it does not check for the GENERATED marker before overwriting, so a half-adopter who runs the remedy replaces their hand-kept board with a generated index (recoverable from git; still a surprise). Recorded as **BS13 (minor)**.

### Post-reconcile additions — clearly marked; phase-1 text above is unrevised

- **Amendment to BS3 (numbers only; severity unchanged, MODERATE).** Phase 1 wrote "8 ⏳ where the store holds 9". Correct at `3d0df11`: the index carried **6** `- ⏳` pointer lines (the 8 was a grep over glyph occurrences, which included one section heading and the code-span lift in Q1); the store held **7** pointers — 6 item files plus the README-resident one in section 020. The 🎯 figures (30 shown / 47 on the old top level) stand.
- **Amendment to BS4 counsel (severity unchanged, MODERATE).** Add F5's ruled option: a class-grounded `sizescan:budget` for a *generated* index (grounded in "one line per item ever", not in today's length) is a legitimate third answer beside "render open items only" and "unbounded by ruling", and sizescan's ROADMAP remedy string needs a split-board branch either way.
- **BS12 (note)** — The GENERATED marker is a line-1 prefix skip in `pointerscan` regardless of path; an item file opening with it is indexed live and un-linted. No live instance. Counsel: skip only the index path, or `check` rejects the marker in an item file (tested by a fixture item carrying the marker: `check` exit 1, pointerscan still lints it).
- **BS13 (minor)** — `rebuild` overwrites `docs/ROADMAP.md` without checking that the file it replaces carries the GENERATED marker (or is absent). A half-adopting child, or any repo where the check fires on a name collision (BS8), is told to run a remedy that replaces a hand-kept board. Counsel: refuse unless the existing file is absent or generated, with `--force` for a deliberate first migration (tested by a fixture with a hand-written `ROADMAP.md`: `rebuild` exit 1 with the reason; `rebuild --force` writes).
- **BS14 (minor)** — Eye-flags are lifted from the raw first line, code spans included: a backticked `⏳` in prose lifts as the queue glyph (`130-…/010-…` renders `⏳🔎`), re-creating the stale-pointer trap that item documents. `pointerscan` strips code spans; `board.py` should strip them before testing `FLAGS` (tested by that item rendering `🔎` only, and by a fixture with a code-span glyph).

**Overall after reconcile: PASS-WITH-FINDINGS — 1 MAJOR / 4 MODERATE / 5 minor / 4 note.** No phase-1 severity changed; BS12–BS14 added; BS3's ⏳ figures corrected; BS4's counsel widened by F5's ruled option. Every finding remains the principal's to rule (rule 3); the cycle stays open on BS1.

## Deferred material (folded in at verdict landing)

# Deferred — the board store migration cold pass

*Sibling of `2026-08-15-1030-board-store-migration-cold.md`. Open only after
the reviewer's own findings are durably written (REVIEW.md rule 1). Fold in
below the verdict and delete this file when the verdict lands.*

## References withheld from the brief

- **Intent record:** `docs/sessions/2026-08-15-0610-board-store-migration.md`
  (and its one-line entry in `docs/SESSIONS.md`).
- **The queue pointer:**
  `docs/roadmap/010-board-store-migration-per-item-files-mik/050-rule-4-cold-pass-queued.md`.
- **Related open items in the same section** (the author's own follow-ups —
  read as the author's account, not as settled scope): `020-board-check-staged-plane-seam.md`,
  `030-fleet-rollout-of-the-split-board.md`, `040-monolith-era-wording-sweep.md`.
- **Prior verdicts on neighbouring surfaces** — reconcile only, never anchor:
  `docs/reviews/2026-07-29-1306-b4-harvestscan-cold.md` (harvestscan),
  `docs/reviews/2026-08-05-1238-pointer-grammar-b4-wiring-cold.md`
  (pointerscan), `docs/reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`
  (sizescan's harvest gate, which the split retires in part).

## The brief-writer's seeded questions

Written by a non-author cold session from the delta alone. A floor, never a
fence — the reviewer's own findings come first.

1. **Index flags are derived from the raw first line, code spans included.**
   `board.py`'s `index_line` collects any glyph in `FLAGS` that appears in the
   item's first line. Item `130-…/010-…` opens with a `⏳` inside backticks
   and renders in the index as `⏳🔎` — a non-pointer item wearing the queue
   glyph in the file a taker greps first. `pointerscan` strips code spans for
   exactly this reason. Is this a defect in the projection, and does it
   recreate the stale-pointer trap the 130 item itself describes?
2. **Migration fidelity.** The claim is 4,063 lines → 27 sections / 118 items.
   Diff the pre-migration `docs/ROADMAP.md` (parent of `a9abc26`) against the
   concatenated store: is any line, allow-marker, or nested sub-bullet lost,
   re-parented, or de-indented? Nested sub-bullets under a pointer (the shape
   `160-…/080` and `090` carry) are the likeliest casualty.
3. **`--check` reads the worktree, not the staged plane.** The author records
   this as a stated residual and a follow-up item. Can a commit land with a
   stale index through the hook plane, and does the ci plane catch it? Probe
   it, do not read it.
4. **The GENERATED marker as a skip key.** Scanners skip any file carrying the
   marker line. Could an item file, or any other prose file, carry that line
   and thereby escape `pointerscan`? Is the marker matched on line 1 only?
5. **Doctrine drift left behind.** RECORD.md and CONCURRENCY.md moved with the
   mechanism; the author's own follow-up names a monolith-era wording sweep
   still owed. Which surfaces still tell a session to edit `ROADMAP.md`
   directly (REVIEW.md rule 4's pointer wording, skills, templates, children's
   floor blocks), and does any of them now instruct a breach of the `board`
   check?
6. **The harvest step retired.** With `[x]` flipped in place and no harvest,
   what now stops a section from accreting closed items and their narrative
   forever? Does `sizescan`'s cold-content gate still fire on a `[x]` inside
   an item file, or only on the (now never-`[x]`) index?
7. **Children.** The check reports not-in-scope where `docs/roadmap/` is
   absent. Is that honest for a child that adopts the split half-way — a
   `docs/roadmap/` directory present but a hand-kept `ROADMAP.md`?
