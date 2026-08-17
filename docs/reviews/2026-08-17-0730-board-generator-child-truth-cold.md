# Cold pass — the board generator's child-facing strings

**Pass type:** code cold pass (REVIEW.md rule 4 — the delta changes a floor
tool that every child repo calls, and the strings it commits into a generated
file that children are told never to hand-edit; the fix, its own correction an
hour later, and the board items recording both were written by the same
session).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04). Checked
at selection: a session that cannot honour the bar stops rather than takes.
**Status:** BRIEF WRITTEN, REVIEW NOT RUN. The next cold session that passes
rule 4's criterion and the tier bar takes it — see *Spawn provenance*.

## Spawn provenance

- **Author of the work under review:** the session that landed the delta on
  2026-08-17 (wt: `board-generator-child-truth`, merged as `9f0dbf8`, plus the
  follow-up commit `a3a64aa` on `main`; Opus tier per the commit trailers).
- **Who wrote this brief:** an atelier session Mike opened 2026-08-17 at 0710
  UTC under his standing cold-session instruction — *"Please do any review work
  and any work that is fable dependent"*, and, mid-session, *"Write briefs too
  if they are required."* That session authored no part of this delta, was
  neither started nor instructed by the authoring session, and has edited no
  file this delta touches. It wrote this brief from the commits themselves
  (`git show` over the seven-commit series and the diff of `tools/board.py` and
  `tools/pointerscan.py`) and the queue pointer; it did **not** open the intent
  record (`docs/sessions/2026-08-17-0530-board-generator-child-truth.md`) or
  the board items `060`, `070`, `080` that the delta writes.
- ⚠️ **Three disclosures, all about the brief-writer, none about the delta.**
  1. **It read the `docs/SESSIONS.md` tail** at session onramp, before this
     brief was commissioned, and the last index entry there summarises this
     delta in the author's own words. That is rule-2 barred material and it was
     read. It is the reason the intent record itself was left unopened, and the
     reason the seeded questions in the sibling are held to what the code shows.
  2. **It read the commit messages in full.** They are the delta and are in
     scope as the author's claims — but they are also a long author's account,
     and a brief shaped by them inherits its framing. Generate your own reading
     of the diff before you weigh anything this brief says.
  3. **It is not on the Fable tier** — it is Opus. The tier bar in REVIEW rule 4
     is stated for the *reviewer*, and this is not the review; but satisfy
     yourself that a brief written off the named tier is acceptable and say so
     either way. If you judge otherwise, the correct outcome is to rewrite the
     brief, not to run the review on a brief you do not trust. The same session
     is orchestrating two *other* cold passes (the reply-gate unwiring and the
     apex authority correction) with Fable reviewers, and **stopped** on this
     one — it did not run this review.
- **Who takes the review:** the next cold session meeting rule 4's single
  criterion — a session the author neither started nor instructed — on the
  Fable tier, checked at selection. The taker repeats its own provenance in the
  verdict: how it was spawned, and its non-involvement with both the authoring
  session and this brief-writing session.
- **Orchestration shape:** the deferred material sits in the sibling
  `2026-08-17-0730-board-generator-child-truth-cold.deferred.md` (rule 1's
  split). Recommended: run under an orchestrator that holds the sibling's bytes
  and releases them only after the reviewer's findings are durably written. A
  taker working by hand opens the sibling as a deliberate second act after its
  findings are committed, and says so in the verdict. Fold in and delete when
  the verdict lands.
- **Adjacent pass, not this one.** The board-store migration pass
  (`2026-08-15-1030-board-store-migration-cold.md`) reviewed the migration that
  *created* this generator; its BS findings are a prior verdict, barred until
  reconcile. This pass reviews what the generator emits, and for whom.

## What the work is

Seven commits, of which three carry code. Reviewed at HEAD.

**`b2ba382` — the generator writes for the repo it lives in.** `board.py`
emitted `tools/board.py` into three strings a *child* reads: the index banner,
the index preamble, and the stale-index remedy `--check` prints. Children call
the floor's tools and never vendor them (ADR 0008), so all three named a file
that is not there. Changes: a new `rebuild_cmd(root)` decides the spelling per
root — repo-relative where the tool sits inside the tree it rebuilds, a
hook-resolution spelling where it does not, never an absolute path; the banner
`GENERATED_LINE` drops the path entirely (115 columns to 69); `GENERATED_MARK`
loses its `tools/` prefix, with a `GENERATED_MARKS` tuple keeping the legacy
spelling accepted as a prefix here and in `pointerscan.py`; the preamble is
hand-wrapped across three lines and carries the command; and section narrative
links render `*[Narrative](…)*` instead of repeating the path as link text.

**`363a846` — the wrapscan half was a trailing space.** The previous commit had
recorded in item `070` that the index cannot pass a repo-wide `wrapscan` and
that only a floor-policy ruling could fix it. The commit withdraws that: item
lines end in an unbreakable path token, which `wrapscan` already exempts, and
the exemption was lapsing only because a trailing ` 🎯` added a legal wrap point
after the path. `index_line()` now renders flags and the claim fragment
**before** the link; allow-comments stay trailing. Two selftest assertions pin
it. The commit also states that the earlier `127 → 78` figure counted lines the
gate never flagged, and that the two numbers in circulation (8 and 127) were the
gate's count and a raw column count, neither saying what it counted.

**`a3a64aa` — emit the hook's whole resolution order.** The child spelling
shipped an hour earlier as `"$ATELIER_TOOLS"/board.py`. `.githooks/pre-commit`
resolves `${ATELIER_TOOLS:-$(git config hooks.atelierTools)}`, and on the
machine that found it `ATELIER_TOOLS` is unset while the git config carries the
path — so in a child both the banner-adjacent preamble and the stale-index
remedy expanded to `python3 /board.py`. `rebuild_cmd()` now emits the whole
fallback chain, pinned by two selftest assertions.

**The board commits.** `e2551da` rewrites the fleet-rollout item — it records
that a child (`faves`) ran its split first, restates every figure as measured at
HEAD rather than adjusted, and states that the rollout shipped with this item's
own gate still shut. `ef484a3` files item `070`; `2428fdf` claims `060`;
`0213c08` files item `080` (the action word is the only bare positional in the
registry — filed, not fixed); `19eb0e2` files items `100` and `110` handed up by
a second child, one of them corrected on the way in. The board items are the
author's account of the same work and are in scope as such.

## Scope

Widest the work admits. This delta's subject is **text a tool writes into a
file another repo commits**, so the reviewable question is not only whether the
strings are correct here but whether they are correct *there*, and whether the
mechanism that decides between them can be wrong in a way no test in this repo
would show. In scope: whether `rebuild_cmd()`'s branch condition actually
distinguishes the two geometries it names, and what it emits for the geometries
it does not (a vendored copy, a symlinked tools directory, a submodule, a repo
whose board is not at `docs/roadmap/`); whether the two-spelling marker is
honoured everywhere the marker is read, not only where the diff touched;
whether the `wrapscan` exemption the flag reordering restores is a property the
code guarantees or one the current data happens to satisfy; whether the
selftest's tempdir root genuinely exercises a child's geometry or only resembles
it; whether the three numeric claims (28 → 0 pathscan here, 15 → 0 wrapscan in
the child, the withdrawn 127 → 78) are reproducible at HEAD; whether the
withdrawal of the `070` policy claim reached every surface that had already
repeated it; and whether a defect corrected within the hour by the same session
that shipped it indicates a check that should have caught it before the push.

**Non-goals, and neither fences the risk:** the *rollout* of the board to other
children is not under review — only what atelier ships for them to call; and no
finding is decided by the reviewer (rule 3), so counsel on the filed-not-fixed
items (`080`, `100`, `110`) is welcome but must be labelled as counsel.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself
   first. The stated principle is *every string this tool commits must be true
   in a repo that is not this one*. Is that principle enforced by anything, or
   asserted in a docstring and honoured by attention? Two defects of the same
   class shipped an hour apart — the first named a file only atelier has, the
   second a variable only some machines set. Is there a third instance of the
   class still in the tool, or in its neighbours in `tools/`? Consider whether
   the fix's own frame — *emit the whole resolution order* — is the right
   generalisation, or whether emitting an executable instruction at all is the
   assumption worth challenging.
2. **Correctness & quality.** Read the diff of `tools/board.py` and
   `tools/pointerscan.py` at HEAD, then read the whole of `rebuild_cmd()`,
   `build_index()`, `index_line()` and `run_check()` as they now stand — a diff
   hides what it did not touch. Check the `relative_to` branch against the roots
   each caller actually passes, and whether `run_check`'s root and
   `build_index`'s derived root are the same path in every invocation the floor
   makes. Check that every place a generated marker is compared honours both
   spellings, in this file and in every other tool that reads the index. Check
   the selftest assertions test the property their comment claims. Tests are
   reviewable on the same footing as the code.
3. **Completeness / harvest.** Every surface that stated the old strings or the
   withdrawn `070` claim: `tools/README.md`, `CHANGELOG.md`, the board items
   `060`/`070`/`080`, `docs/roadmap/README.md`, `docs/build/`, the child floor
   block and templates, and any doctrine that quotes the rebuild command. Does
   `CHANGELOG.md` cover all three code commits or only the first? A child
   carries an index generated under the old banner until its next rebuild — is
   that window stated anywhere a child session would see it? Are the
   filed-not-fixed items (`080`, `100`, `110`) queued with enough for a session
   that was not there to act on them?
4. **Security & privacy** — mandatory. atelier is PUBLIC, and this delta's
   whole subject is what gets *committed* into a file. The central claim is that
   an absolute path must never be written into a committed file because it is a
   machine-local fact. Test that claim rather than reading it: is there any root
   for which `rebuild_cmd()` emits an absolute path, a home directory, or a
   machine-specific name — and does the `no home directory in the index`
   assertion actually catch the cases that matter? Consider separately whether
   emitting `git config hooks.atelierTools` into a public file discloses
   anything about the estate's layout. The house security scanner reads the
   session's pending diff whatever path it is aimed at (board item `160-…/190`);
   this is a landed-delta review, so state the reach case that applied rather
   than assuming one. If the lens has no surface beyond the public-tree check,
   discharge it in one explicit line with grounds.

## Re-run obligation

Re-run, do not read:

- `python3 tools/board.py --selftest`, and the full Python and node suites, and
  the floor on **both** planes at HEAD. Lift the invocations from
  [`.githooks/pre-commit`](../../.githooks/pre-commit) and
  `.github/workflows/ci.yml` rather than guessing them.
- The pathscan claim: the commit says atelier's index went from 28
  generator-caused findings to 0, with one surviving finding that is a real
  stale path. Reproduce both halves — the 0 at HEAD, and the 28 before
  `b2ba382` — and check the survivor yourself rather than accepting it as read.
- The wrapscan claim: `wrapscan` clean on the index at HEAD, and the withdrawn
  arithmetic. The commit states 8 (now 15) was the gate's count and 127 a raw
  column count. Reproduce enough to say which claim the item now carries is
  true.
- **The child geometry.** The selftest's tempdir root is offered as a child's
  geometry. Verify it independently: build an index in a scratch clone whose
  tools live outside the tree, and read the emitted banner, preamble and stale
  remedy. Then run the emitted command literally, in a shell where
  `ATELIER_TOOLS` is unset, and say whether it works. Mutation probes belong in
  your own scratch clone, never in the worktree.
- A real child's `docs/ROADMAP.md` banner, if one is reachable from this
  machine, to say which spelling it currently carries. If it is not reachable,
  say so with grounds rather than inferring — a claim about another repo's state
  that was never read is the failure this delta itself is about.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`,
every prior verdict in `docs/reviews/` (the board-store migration pass
especially), the intent record for this delta, and the board items `060`, `070`
and `080` under `docs/roadmap/115-…/` and `docs/roadmap/160-…/`, which carry the
author's account of the same defects. The sibling `.deferred.md` holds those
references and the brief-writer's seeded questions; open it after your findings
are committed. Reconcile after, never anchor before. A taker whose own session
onramp has already read the `SESSIONS.md` tail discloses that in the verdict, as
this brief-writer has.

Reading the *code* the items describe is not barred — the tool, its tests, its
catalogue entry and the generated index are the delta. What is barred is the
author's narrative of why.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `BG`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then open the sibling; append a
reconcile section; fold the sibling in below it and delete the sibling;
finalise. Update the queue pointer
(`docs/roadmap/160-doctrine-review-owed/220-rule-4-cold-pass-queued-board-generator.md`)
and rebuild the index in the same commit.
