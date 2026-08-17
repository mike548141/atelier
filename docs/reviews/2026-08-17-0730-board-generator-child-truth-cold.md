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

---

## Verdict — BG cold pass, phase 1 (2026-08-17, written 10:20 UTC)

**Overall: PASS-WITH-FINDINGS — 0 MAJOR / 4 MODERATE / 4 minor / 4 note.**
The three code commits do what they say for the geometry they name (tool
inside the tree, or tool outside it with the hook configured), and every claim
I could re-run reproduced in kind. What does not hold is the generalisation
around them: the index text now depends on *where the generator ran from*
(BG1), the child command names two of the hook's three branches (BG2), the
"passes wrapscan in any repo" property is data-dependent rather than
renderer-guaranteed (BG3), and the corrections did not reach the surfaces that
still carry the withdrawn and superseded claims (BG4). None is a wrong
direction; all four are the same class the delta itself named — a string that
is true from one place and asserted true from every place.

### Provenance, repeated — and four disclosures

- **Reviewer:** this verdict was formed by a Fable-tier reviewer subagent
  spawned by an orchestrator session that Mike opened on 2026-08-17 at 0955
  UTC on the Fable tier under his standing cold-session instruction. The
  reviewer read the delta cold: the diffs of `tools/board.py` and
  `tools/pointerscan.py` first, the whole tool at HEAD second, the commit
  messages third, the brief's *What the work is* only after forming its own
  reading. Every finding and every severity below is the reviewer's; the
  orchestrator formed none and wrote none.
- **Non-involvement:** neither the orchestrator nor the reviewer wrote any part
  of the delta (`e2551da`…`19eb0e2`, `a3a64aa`), and neither wrote this brief.
  The brief was written by a separate session (Opus tier, per its own
  disclosure); the reviewer was neither started nor instructed by the
  authoring session or by the brief-writing session.
- **Disclosure (a) — the partition.** The orchestrator read the
  `docs/SESSIONS.md` tail at its onramp, including the index line summarising
  this delta, and read the queue pointer items. The reviewer read none of
  those. The `.deferred.md` sibling was held out of the worktree by the
  orchestrator and has not been opened; this section is written before its
  release.
- **Disclosure (b) — one accidental exposure.** One `coldsweep` for the string
  `atelierTools` was run without the `--also-exclude` flags for this pass's
  barred board items, and printed three lines (14, 41, 46) of item `010/080`,
  which I read. They restate the hook's resolution order and the a3a64aa
  correction. The third-branch reading (BG2) and the geometry probes that
  ground it were run *before* that sweep; the exposure changed no finding.
  Every later sweep ran through a wrapper that always excludes `010/060`,
  `010/070` and `010/080`. A second sweep, for the estate-root repo's name,
  ran without the item exclusions and printed **filenames and counts only**
  (no content lines).
- **Disclosure (c) — the brief's barred paths were wrong.** The brief bars
  items `060`/`070`/`080` "under `docs/roadmap/115-…/` and `160-…/`". The
  delta writes `060`/`070`/`080` under
  `docs/roadmap/010-board-store-migration-per-item-files-mik/`. I barred the
  `010` items (the ones this delta writes) and did not open the `115`/`160`
  ones either. The other `010` items the delta writes (`030`, `090`, `100`,
  `110`) are not barred and were read after the probes.
- **Disclosure (d) — off-tier brief.** The brief was written on Opus. It is
  acceptable: it is a scope-and-pointer document, its account of the work is
  the commit messages' account and says so, and my reading of the diff was
  formed before I weighed it. Its one factual slip (the item paths, above)
  did not steer the pass. Prefix `BG` — collision was checked against
  filenames in `docs/reviews/` only (the contents are barred); residual noted.
- **Tools:** all sweeps via `tools/coldsweep.py`; no `--include-barred`.
  `/security-review` was not run (it reads the session's pending diff, which
  in this shared worktree is other passes' briefs). No git state was changed;
  every mutation probe ran in scratch clones under the session scratchpad.

### Lens 1 — load-bearing assumptions, in my own words

1. *A child's index is always generated by tools that sit outside the child's
   tree.* Mostly true (ADR 0008; the child CI keeps `repo/` and `atelier/` as
   siblings). But `rebuild_cmd()` decides by `Path(__file__).resolve()`
   against `root.resolve()`, so **the decision follows the tool's real
   location, not the repo's identity** — and that is a geometry, not a fact
   about the repo. Two consequences the delta did not test: (BG1) atelier's
   own index rendered by another clone's tools is the child spelling; (BG2) a
   child whose `tools/` is a symlink resolves *outside* and gets the child
   spelling even though the in-tree spelling was true there.
2. *The hook's resolution order is the one true spelling and it has two
   branches.* False. `.githooks/pre-commit` (line 53–54) resolves
   `${ATELIER_TOOLS:-$(git config --get hooks.atelierTools)}` **then**
   `${tools_dir:-$repo_root/tools}`. The delta's own rule — "emit the whole
   order or none of it" — was applied to two of three branches (BG2).
3. *The index is a deterministic function of the item files.* It was; it is
   now a function of the item files **and** the generator's location. The
   selftest's determinism check runs the same geometry twice (BG1).
4. *Flags-before-link makes every item line wrapscan-exempt.* Only where the
   last whitespace before column 85 falls inside the title and the line ends
   in the path. A trailing sibling allow marker (a feature this generator
   advertises and tests) breaks it whenever glyph + title + link exceeds 85 —
   which at the first child's slug lengths is always (BG3).
5. *pathscan and wrapscan are the prose gates that matter for the index.*
   `plainscan` fires 13 times on atelier's index at HEAD; `spellscan` and
   `datescan` read it too (clean today). The generalisation the delta rejected
   — a marker-aware exemption, as `pointerscan` already has — is the one the
   evidence points at (BG6).
6. *"Never an absolute path" is enforced.* True **by construction**: the
   in-tree branch emits a root-relative path, the other a fixed string. The
   assertion offered as its pin (`no home directory in the index`) cannot fail
   in the geometry it tests and fails spuriously with `HOME=/` (BG7).
7. *The reader runs the emitted command from the repo root.* Unstated; from a
   subdirectory both spellings print "not in scope" and exit 0 (BG8).
8. *The principle "every string must be true in a repo that is not this one"
   is enforced by something.* It is asserted in a docstring and honoured by
   attention. Nothing ties the emitted `${…}` expression to the hook's actual
   expression, and no test runs the emitted command. A test that resolves
   both under the same env/config matrix would have caught b2ba382's defect,
   a3a64aa's, and BG2 (counsel, below).

**Is emitting an executable instruction the right frame?** Half. The delta
gives one string to two surfaces with different constraints: the *committed*
preamble (must be portable forever) and the *printed* remedy (ephemeral, may
be exact). Making one string satisfy both is why it satisfies neither fully.
Counsel: the printed remedy may name the tool's own resolved location — it is
never committed — and the committed preamble may point at the mechanism
("the `board` floor check; your hook knows where the tools live") rather
than a shell one-liner. Labelled counsel; the choice is Mike's.

### Lens 2 — correctness & quality

- `rebuild_cmd()`'s branch condition distinguishes *tool-inside-root* from
  *tool-outside-root* after symlink resolution — not *atelier* from *child*.
  Callers: `build_index(board)` derives `board.parent.parent`; `run_check`
  passes its `root`; both are the same path in every floor invocation
  (hook: absolute `$repo_root`; CI: `.`; child CI: `repo`). Verified: `--root`
  via a symlinked path, from a subdirectory with a relative root, and via
  `.` all agree (G3, G4).
- The two-spelling marker: `board.py` and `pointerscan.py` are the only
  readers of the marker in the tree (`harvestscan` watches the index by
  *name*, not marker); both accept both spellings as a prefix. Honoured.
- The wrapscan exemption is not a property the code guarantees (BG3, probes
  3–4). The comment "a line carrying [an allow-comment] exempts itself anyway"
  is false for sibling-scanner markers when the pre-marker text exceeds 85.
- The selftest's tempdir root is a child's geometry only in the sense that
  the tool is outside it; it exercises neither the in-tree branch nor a
  mixed geometry, and neither the selftest nor `test_board.py` runs
  `wrapscan`/`pathscan` on the output — the "flag precedes the link" and "no
  item line ends in a flag" checks are proxies for the property, not the
  property.
- The a3a64aa defect **should** have been caught before push, by any test
  that executed the emitted string. Two commits pinned the emitted string
  itself (first the half spelling, then the fuller one) — pinning the output
  of a decision is not testing the decision.
- The three numeric claims: reproduced (ledger). One characterisation is
  wrong: the pathscan survivor `F1/GUARDS.md` is a finding-ID-and-filename
  fragment in an item title (`docs/roadmap/160-…/060-…`), a path that never
  existed in history — a false positive, not "a real stale path" (BG9).

### Lens 3 — completeness / harvest

- `tools/README.md` (board entry) still states **both** superseded claims: the
  `$ATELIER_TOOLS` spelling, and the withdrawn 070 residual verbatim ("the
  index cannot pass a repo-wide `wrapscan` … board item `010/070`, unruled").
  363a846 and a3a64aa did not touch it (BG4).
- `CHANGELOG.md` covers b2ba382 and 363a846 only; the a3a64aa correction is
  absent, and the entry's `$ATELIER_TOOLS` wording is now false (BG4). The
  entry's "28 false findings per commit here" overstates: atelier's own floor
  scopes `pathscan` away from the index (`.atelier-floor.json`), so nothing
  fired per commit here — 28 was a hand run (BG10).
- `tools/board.py`'s module docstring (line 59) still says the
  `$ATELIER_TOOLS` spelling; only `rebuild_cmd()`'s docstring was updated.
- Item `030` (fleet-rollout guidance to the next children) still says the
  index "needs `.wrapscanignore` + `.pathscanignore` entries" and that
  `tools/board.py` in a child is "a shim, not a copy" — both retired by this
  very delta (BG5). Its "first child done, two open" is also already behind
  the fleet: nine reachable children carry a generated index at HEAD.
- `docs/method/CONCURRENCY.md` line 249 tells a reader to run
  `tools/board.py rebuild` — doctrine children inherit, same class as the
  fixed strings; `docs/roadmap/README.md` names `tools/board.py` as the
  generator, which is fine (it names the source, not an instruction).
- The rebuild window: one reachable private child carries the **legacy**
  banner at HEAD. Nothing a child session reads states the window; the
  mechanism that closes it is the enforced check going stale on its next
  commit, with the remedy printed. Adequate, but only if the printed remedy
  works there (BG2 says: only where the hook is configured).
- Filed-not-fixed items `090`, `100`, `110` carry enough for a cold session
  to act (mechanism, reproduction, fix candidates, source). Counsel below.

### Lens 4 — security & privacy

- **Absolute path / home directory:** no root makes `rebuild_cmd()` emit one
  — the in-tree branch is root-relative by construction, the other a fixed
  string. Probed: symlinked root, symlinked tools, vendored nested tools,
  another clone's tools, subdirectory invocation. The pin offered for it is
  weak (BG7), but the property holds.
- **`git config hooks.atelierTools` in a public file:** discloses only that
  the estate's hook reads a config key of that name — already public in
  `.githooks/pre-commit`, `tools/pre-commit.sample`, `commands/install-hook.md`
  and the child templates. No new disclosure.
- **Copy-paste surface:** the emitted command executes `git config` output as
  a path — the same trust class as the hook itself (its TRUST NOTE); no user
  input reaches the emitted string. The in-tree spelling is unquoted
  (`python3 {here} rebuild`), so a vendored path containing a space would
  break the paste — cosmetic.
- **Public tree:** the CHANGELOG entry and item `030` name two private
  children by repo name. Pre-existing practice (30 live-tree hits for the
  estate-root repo's name alone), not new to this delta — flagged (BG11).
- **House scanner reach:** landed-delta review; the only pending diff in this
  worktree is other passes' briefs, and the delta's `.md` half is outside the
  scanner's file classes — its clean pass would be definitionally empty.
  Discharged by hand: no threat vector of the tool's class (input paths,
  shell-out, secrets) is touched by this delta beyond the copy-paste note.

### Findings

- **BG1 · MODERATE** — *The index text, and so the enforced check's verdict,
  depends on where the generator ran from.* Another clone's `board.py`
  checking atelier's tree reports the committed index **stale** (probe G2);
  a `rebuild` from that geometry writes the child spelling into atelier's own
  index, after which atelier's in-tree tools call it stale again (G2b) —
  flip-flop across geometries. Determinism became geometry-conditional; no
  test covers the in-tree branch or a mixed geometry; a machine that exports
  `ATELIER_TOOLS` (which the hook's own comment invites "so a test/CI run can
  redirect") meets it in every atelier worktree, on a check with no advisory
  form. *Counsel:* decide the spelling from the repo (is `tools/board.py` a
  tracked file of `root`?) rather than from the tool's location; or emit one
  spelling everywhere.
- **BG2 · MODERATE** — *The child spelling names two of the hook's three
  branches.* The hook falls through to `$repo_root/tools`; the emitted string
  does not. A child whose `tools/` is a symlink to atelier's resolves outside
  the root and gets the child spelling, which expands to `python3 /board.py`
  with neither env nor config set — while `python3 tools/board.py rebuild`
  worked there (G5). A fresh clone of the public child, before its hook is
  configured, gets the same bare Python error with no remedy (G7); the hook
  in that state prints a three-line remedy. The docstring's "true everywhere"
  is an overclaim; a3a64aa's own principle applied to itself.
  *Counsel:* `"${ATELIER_TOOLS:-$(git config hooks.atelierTools || echo
  tools)}"` carries the whole order; better, add a test that resolves the
  hook's expression and the emitted one under the same env/config matrix and
  asserts they agree — the check that would have caught b2ba382, a3a64aa and
  this.
- **BG3 · MODERATE** — *"Passes wrapscan in any repo" is a property of the
  current data, not the renderer.* A source state line of 81 columns carrying
  a `datescan:allow` marker (a feature the generator advertises and the
  selftest pins) renders to a 187-column index line that `wrapscan` flags
  (probe 4): the sibling-marker exemption applies only when the pre-marker
  text fits, and glyph + title + link exceeds 85 for every item at the first
  child's slug lengths (longest link 125 columns). `wrapscan` is enforced by
  default in a child, so the block lands on the file readers are told never
  to hand-edit, with "wrap it" as the remedy. Long claim fragments plus long
  titles on one state line can do the same (probe 3). The withdrawal of the
  070 policy question therefore rests on a property the code does not hold;
  the question is not closed. *Counsel:* either the prose gates skip files
  opening with the GENERATED marker (as `pointerscan` does), or the renderer
  keeps allow-comments before the link too and the property is tested by
  running `wrapscan` over generated output in the selftest.
- **BG4 · MODERATE** — *The corrections did not reach the surfaces that
  restate the corrected claims.* `tools/README.md` still carries the
  `$ATELIER_TOOLS` spelling **and** the withdrawn 070 residual verbatim;
  `CHANGELOG.md` covers two of three code commits and states the superseded
  spelling; `board.py`'s module docstring says the same. A reader of the
  catalogue is told the opposite of what the code does and what the record
  says was withdrawn.
- **BG5 · minor** — Item `030`'s guidance to the next children (ignore files
  needed; shim needed) is stale as of this delta, and its fleet picture is
  behind: nine reachable children carry a generated index; one private child
  sits in the legacy-banner window now.
- **BG6 · minor** — `plainscan` fires 13× on atelier's generated index at
  HEAD (warn-only) — the "check nobody reads" class the delta fixed for
  `pathscan`, left in place for the next gate. The delta's reasoning
  generalises to a marker-aware exemption; declaring the ruling "not needed"
  was premature.
- **BG7 · minor** — The `no home directory in the index` assertion cannot
  fail in the geometry it tests (no path is emitted there) and fails
  spuriously with `HOME=/` (probe G9: `board selftest FAIL`), which would red
  the CI selftest step in a minimal container. It pins nothing about the
  in-tree branch, which is the only branch that emits a path.
- **BG8 · minor** — Run from a subdirectory, both emitted spellings print
  "not in scope" and exit 0 — a silent no-op in the direction of "fine".
  *Counsel:* default `--root` to the git toplevel, or carry
  `--root "$(git rev-parse --show-toplevel)"` in the emitted string.
- **BG9 · note** — The surviving `pathscan` finding is a false positive
  (`F1/GUARDS.md`, a title fragment), not "a real stale path" as b2ba382 and
  363a846 state; the count is right, the characterisation is wrong.
- **BG10 · note** — "28 false findings per commit here" — atelier scopes
  `pathscan` away from the index; the 28 was a hand run, not a per-commit
  cost here (it was per-commit in the child, which had no scope block).
- **BG11 · note** — The CHANGELOG entry and item `030` add to the public
  repo's naming of private children by repo name; pre-existing practice, not
  introduced here — for Mike's awareness.
- **BG12 · note** — The brief's barred-item paths (`115-…`, `160-…`) do not
  match the items the delta writes (`010-…`); a taker following the brief
  literally would bar the wrong files and read the right ones.

### Re-run ledger — what I ran, what I got, what each number counts

| Claim / probe | Result (what the number counts) |
|---|---|
| `board.py --selftest` | OK, rc 0 |
| Python suite (`unittest discover -s tools`) | 1344 tests, OK (delta said 1,321 at its own HEAD; tree has grown) |
| Node suite (`instruments/*.test.js`) | 235 pass, 0 fail |
| Hook plane (`floor.py --plane hook`) at HEAD | rc 0; `board ✅ enforced` |
| CI plane (`floor.py --plane ci`) at HEAD | rc 0; secretscan 22 advisory (expected) |
| Every registry `--selftest` + floor/floorfleet/signscan + stampscan + mandoc | all rc 0 |
| pathscan on atelier index at HEAD | 1 finding (`F1/GUARDS.md`, false positive) — findings, unscoped hand run |
| pathscan on atelier index at `b2ba382^` (scratch clone) | 29 findings: 28 narrative-link-text + the same survivor |
| pathscan on the public child's committed index (HEAD tools, absolute path) | 0 |
| pathscan, pre-fix generator over the public child's items (scratch) | 49 findings, 48 narrative-caused |
| wrapscan on atelier index at HEAD | 0 gate findings; 176 lines over 85 **code points** (177 by bytes — awk counts bytes) of 328 |
| wrapscan on atelier index at `b2ba382^` | 62 gate findings; 188 lines over 85 (bytes) of 294 |
| wrapscan, pre-fix generator over the public child's items (scratch) | 16 gate findings, 14 of them flag-ending lines; 142 raw (bytes) of 306 |
| wrapscan, HEAD generator over the same | 0 gate findings; 91 raw (code points) of 308; output byte-identical to the child's committed index |
| Public child's banner + preamble at HEAD | new banner; full-order child command; 85 columns exactly |
| Reachable children (first line only) | 9 generated indexes: 8 new spelling, 1 legacy; 3 no split board |
| Emitted command run literally, child, `ATELIER_TOOLS` unset, config set (sh and zsh) | rc 0 |
| Same, env set instead of config | rc 0 |
| Same, neither set (fresh clone) | `can't open file '/board.py'`, rc 2 |
| Symlinked `tools/` child, neither set | child spelling emitted; rc 2; in-tree spelling rc 0 |
| Vendored nested tools | `python3 vendor/atelier/tools/board.py rebuild`, rc 0 |
| Another clone's tools checking atelier | **stale**, rc 1; rebuild writes child spelling; in-tree tools then say stale |
| Symlinked root path; subdirectory + relative root | current, rc 0 (both) |
| Subdirectory, no `--root` | "not in scope", rc 0 |
| `HOME=/` selftest | FAIL (`no home directory in the index`); `HOME` unset: OK |
| Sibling allow marker on an 81-col state line, atelier-length slugs | index line 187 cols, wrapscan 1 finding; source files clean |
| Banner length | 69 code points (71 bytes) — the "115 → 69" claim holds in code points |
| Item-110 defect | reproduced by accident: `pathscan --root <child> docs/ROADMAP.md` from an atelier CWD scanned atelier's file under the child's rules |

### Follow-up checklist

- [ ] BG1 — decide the spelling from the repo, not the tool's location; add a
      mixed-geometry test (another tools dir against this root).
- [ ] BG2 — emit the hook's third branch or drop the executable string from
      the committed preamble; add the hook-vs-emitted resolution test.
- [ ] BG3 — run `wrapscan` over generated output in the selftest; decide the
      generated-file exemption question honestly (Mike's ruling).
- [ ] BG4 — sweep `tools/README.md`, `CHANGELOG.md`, `board.py` module
      docstring for the `$ATELIER_TOOLS` spelling and the withdrawn residual.
- [ ] BG5 — refresh item `030`'s child guidance and fleet picture.
- [ ] BG6 — treat `plainscan` on the index the same way as `pathscan` was.
- [ ] BG7 — replace the home-directory assertion with one on the in-tree
      branch's output.
- [ ] BG8 — root default / `--root` in the emitted string.
- [ ] BG9–BG10 — correct the record's characterisations (survivor; per-commit).
- [ ] BG11 — Mike's call on private-child names in the public tree.
- [ ] BG12 — fix the brief's barred paths when folding the sibling in.

### Counsel on the filed-not-fixed items (labelled counsel, not findings)

- `090` (action word is the only bare positional): agree with the item's
  reading; the flag form matches the house precedent, and it removes the
  special case from the registry. Wants its own claim, as the item says.
- `100` (a child's `[~]` means partially delivered): a ruling, not a defect;
  the item frames the three options fairly. Counsel only that the rollout
  guidance (item `030`) carry the question *before* the cut, as `100` asks.
- `110` (relative path args resolve against cwd): 🔥 is right — it bit this
  review within the hour, producing a confident wrong reading of a child's
  index. Fix at the shared layer; a test that a relative arg plus a foreign
  `--root` cannot read the cwd.

### Reconcile (2026-08-17, after release)

**Provenance of this step.** Released by the orchestrator by message after
it committed the phase-1 verdict (`3ec982a` on the worktree branch); the
sibling's text was carried verbatim in that message. Opened after release, in
this order and for reconcile only: board items `010/060`, `010/070`,
`010/080`; the intent record
`docs/sessions/2026-08-17-0530-board-generator-child-truth.md`; the one
`docs/SESSIONS.md` index line for it (line 266, located by grepping the
record's slug — only that line was printed, and it was cut at 2,000
characters); and the two prior verdicts the sibling names — the board-store
migration pass (its provenance headings, its findings BS1–BS14 and its
reconcile headings) and the floor-render pass (its findings list and the
FR1/FR2 text). Nothing else in `docs/sessions/`, `docs/reviews/` or
`ROADMAP-DONE.md` was opened. Phase-1 text above is unrevised.

**Per finding — anticipated, or new?**

- **BG1** — Not anticipated. Item `080` and the intent record both state the
  premise as a fact about *repos* ("in a child the tool lives in atelier's
  checkout"); the code decides on *geometry*. Neither names a mixed
  geometry. Severity unchanged.
- **BG2** — Not anticipated as a finding, but the record itself contains the
  evidence: item `080` describes the first child's shim as resolving
  `ATELIER_TOOLS` → `git config hooks.atelierTools` → a *third* fallback —
  the shim knew three branches; the string that replaced it knows two.
  Severity unchanged.
- **BG3** — Contradicted by the record, which is why it matters: item `070`
  and the intent record both state "such a line exempts itself anyway" and
  "passes both scanners unscoped, in any repo, with no ignore file", and
  make that the stated ground for *not* asking the generated-file exemption
  ruling. Probe 4 falsifies the first and so the second. Severity unchanged
  (no live instance; the workaround — a `wrapscan:allow` on the source line
  — travels and self-exempts).
- **BG4** — Not anticipated. Item `080` was corrected in place for the
  spelling (its ⚠️ paragraph); `070`, the intent record and the SESSIONS
  line still carry `$ATELIER_TOOLS` — acceptable in a *record* (history is
  kept), not in `tools/README.md` and `CHANGELOG.md`, which are live
  surfaces. The withdrawn 070 residual survives verbatim in
  `tools/README.md`. Severity unchanged.
- **BG5** — Not anticipated; the record's `030` rewrite pre-dates the code
  commits and was not swept after them. Unchanged.
- **BG6** — Not anticipated; the record's "not asked" ruling considered two
  gates. Unchanged.
- **BG7** — Partly anticipated: the record presents the assertion as the
  proof that no home directory reaches the index; the reconcile confirms it
  was read as a proof, not as the tautology it is. Unchanged.
- **BG8** — Not anticipated. Unchanged.
- **BG9** — Contradicted by the record: `070` and the intent record both call
  `F1/GUARDS.md` "a real stale path inherited verbatim from an item's own
  title". A path of that name never existed in the tree's history; it is a
  finding-ID-and-filename fragment. Note stands.
- **BG10** — Not anticipated; `070` itself states that atelier's scope block
  means "neither has ever fired here", which is the fact BG10 relies on.
  Unchanged.
- **BG11** — Anticipated by **BS10** (note, lens 4): "the fleet-rollout item
  names three private repos … in a public record". This delta adds to the
  same class; BS10 is still awaiting ruling. Note stands, now with a prior.
- **BG12** — Not applicable to the record. Unchanged.

**Severity changes:** none. `BG1: MODERATE → MODERATE`,
`BG2: MODERATE → MODERATE`, `BG3: MODERATE → MODERATE`,
`BG4: MODERATE → MODERATE` (grounds per finding above).

**Selftest corpus and claims versus the intent record.** The record's
verification block claims `--selftest` OK, `test_board` + `test_pointerscan`
46/46, the full suite, `pathscan` 28 → 1 with the survivor "confirmed real",
`wrapscan` clean, and the first child's figures measured in a scratch tree
from `origin/main` and `672ad17^`. Re-run: selftest OK; suite 1,344 OK
(the tree has grown); pathscan 29 → 1 (28 narrative-caused — the record's
"28" is the generator-caused count, and it holds); wrapscan 0; the child's
figures reproduce (6,274 lines at `672ad17^`; 48 sections; 54 item files;
271-line index at `d57e359`/`54ba716`, 268 at `672ad17` itself). The record's
"the selftest's root is a tempdir, which is exactly a child's geometry" is
the claim lens 2 qualifies: it is *a* child geometry (tool outside root),
and the only one the corpus exercises. The survivor characterisation is
wrong (BG9). Everything else matches.

**BS1's relationship to BG1/BG2.** BS1 (MAJOR, open) is that `run_check`
compares worktree to worktree, so the hook can pass a stale or wrongly
rebuilt index. BG1 and BG2 sit on the same `check` path one step later:
BG1 makes the *want* side of that comparison depend on where the tool ran
(so a correct index can be reported stale, and a `rebuild` under BS1's P4
conditions from a foreign geometry would absorb sibling dirt *and* write the
foreign spelling); BG2 is what the remedy string says when the comparison
fails. Item `060` (the argv abort) already recorded that the check "had
never actually run via the floor" when BS's "floor green both planes" was
measured — BS1's guarantee, then BS7/090's argv, then BG1's geometry, are
three successive reasons the hook-plane `board` guarantee is weaker than its
four restatements say. All three belong in the same ruling round.

**The eight seeded questions.**

1. *Marker reads in `board.py`.* `GENERATED_MARK` is used once, in the
   selftest against freshly generated text; `GENERATED_MARKS` is **defined
   and never read** in `board.py` — `run_check` compares whole text and
   never inspects an existing index's marker (BS13's point from the other
   side). So the docstring's "here and in pointerscan" is vacuous for
   "here": there is no comparison to honour either spelling. Genuinely
   new; recorded as BG13 below.
2. *Allow-comments after the link.* Covered by BG3, and falsified: only a
   `wrapscan:allow` marker exempts by itself; a sibling marker exempts only
   when the pre-marker text fits in 85 columns, which at real slug lengths
   it never does. A long item line with a short sibling marker is flagged.
3. *Geometries.* Covered by BG1/BG2 and probes G2–G7: symlinked root and
   `/tmp` vs `/private/tmp` both resolve correctly (true → true); vendored
   nested tools emit a true relative path; a symlinked `tools/` is the case
   where a *true* condition (tool resolves outside) yields a *false* string.
4. *Roots.* Covered (lens 2): the same path in every floor invocation,
   relative or absolute; `board` does not share item `110`'s shape because
   it takes no path targets — everything derives from `--root`.
5. *A check that would have caught it.* Covered (lens 1 point 8, BG2
   counsel): nothing asserts the emitted command *runs*; the two assertions
   pin the string's shape. The reconcile confirms the record presents the
   shape assertion as the proof.
6. *The withdrawal.* Covered by BG4: `tools/README.md` still carries the
   retracted claim. New nuance: the correction never reached the principal's
   queue because the ruling was withdrawn before it was asked — and BG3 says
   the question is still live, so the round now hears it from the reviewer
   rather than the author.
7. *Neighbours in `tools/`.* Genuinely new as a sweep; done at reconcile.
   Checked and cleared: every prose scanner's printed remedy names an ignore
   file or allow marker (repo-generic); `floor.py`'s fail-closed text names
   the config key generically; `floorfleet.py`'s parent remedy prints
   `python3 tools/floor.py` only for the parent, where it is true. Two
   neighbours carry the class: `sizescan.py`'s ROADMAP remedy names the
   retired harvest (already BS4), and `tools/hooks/plain-reply.py` hardcodes
   an estate-layout fallback path (`~/.pets/atelier/tools`) as an import
   candidate — a private-estate fact in a public tool, outside this delta
   (BG14 below).
8. *Item `030`'s figures.* Partly covered (BG5). The public child's figures
   reproduce (above); the two private children's cannot be re-measured by
   this pass (their trees are barred to it) and are taken as stated. The
   item does say what it counted — lines — which is the improvement `363a846`
   asked for; what it no longer says correctly is the guidance (BG5).

**Post-reconcile additions — clearly marked; phase-1 text above is unrevised.**

- **BG13 · note** — `GENERATED_MARKS` in `board.py` is dead: defined for the
  two-spelling promise and never read there. Harmless today; the promise the
  docstring makes for "here" is not backed by any comparison. Counsel: either
  use it (BS13's refuse-unless-generated check would) or drop it and let the
  docstring say `pointerscan` alone reads the marker.
- **BG14 · note (outside this delta)** — `tools/hooks/plain-reply.py` names
  `~/.pets/atelier/tools` as a fallback import path — the estate's private
  layout in a shipped tool, the class this delta was fixing. Not this delta's
  surface; for whichever cycle owns the reply-gate tooling.

**Overall after reconcile: PASS-WITH-FINDINGS — 0 MAJOR / 4 MODERATE /
4 minor / 6 note.** No phase-1 severity changed; BG13–BG14 added as notes.
Every finding is the principal's to rule (REVIEW.md rule 3).

## Deferred material — folded in at reconcile

# Deferred material — the board generator's child-facing strings (open only after your findings are durably written)

Sibling of `2026-08-17-0730-board-generator-child-truth-cold.md` under
REVIEW.md rule 1's split. Fold into the brief below the verdict and delete this
file when the verdict lands.

## Intent records

- `docs/sessions/2026-08-17-0530-board-generator-child-truth.md` — the
  authoring session's account. **Not opened by the brief-writer.**
- The board items the delta writes: `060` (the generated banner names a path
  only atelier has), `070` (the index fails two scanners it generates into),
  `080` (the action word is the only bare positional), and the two handed up by
  a second child, `100` and `110`. **None opened by the brief-writer** — their
  content is known here only from the commit messages that filed them.
- The `docs/SESSIONS.md` index entry for the same session. ⚠️ **This one WAS
  read by the brief-writer**, at onramp and before this brief was commissioned
  — see the disclosure in the brief. It is the reason the intent record above
  was left closed.

## Prior verdicts on the same surfaces

- `docs/reviews/2026-08-15-1030-board-store-migration-cold.md` — the pass on
  the migration that created this generator. BS1 (MAJOR) concerns the hook
  plane's stale-index guarantee, which is the same `--check` path this delta
  edits the remedy string of; BS1–BS14 await the principal's ruling round.
  Reconcile against it.
- `docs/reviews/2026-08-09-0823-floor-render-batch-cold.md` — the pass on the
  floor's render states, if your findings reach how `board`'s check reports
  through the floor rather than what it prints.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these. Treat a question you did not think of
as a prompt to re-read the surface, not as an agenda — and note that the
brief-writer read the author's commit messages in full, so these questions
inherit some of the author's framing.

1. `board.py` now defines both `GENERATED_MARK` and a `GENERATED_MARKS` tuple,
   and its docstring says the marker is matched as a prefix against both
   spellings *"here and in pointerscan"*. `pointerscan.py` visibly does so.
   Trace every read of the marker in `board.py` itself and say which constant
   each one uses. If a comparison in this file honours only one spelling, what
   does that do to an index generated under the other — and is that the
   behaviour the docstring promises?
2. The `wrapscan` exemption is restored by making every item line end in its
   path. Allow-comments still render *after* the link, so a line carrying one
   does not end in a path. The commit says such a line "exempts itself anyway".
   Is that true of every allow-comment shape the board's grammar admits, or of
   the ones currently in the tree? What happens to a long item line whose
   allow-comment is short?
3. `rebuild_cmd()` branches on `Path(__file__).resolve().relative_to(root)`
   raising `ValueError`. Enumerate the geometries this can meet: a symlinked
   `tools/` directory, a symlinked repo root, a child that vendors the tool
   after all, a checkout reached through `/private/var` versus `/var` on this
   platform. In which of them does the branch pick the spelling the reader
   needs — and in which does a *true* condition produce a *false* string?
4. `build_index()` derives its root as `board.parent.parent`; `run_check()`
   passes its own `root`. Are these the same path in every invocation the floor
   makes, including when the tool is called with `--root` and a relative path?
   The estate has a live finding (board item `110`) that `--root` is honoured
   for rules and not for targets in at least four tools. Does `board` share it?
5. Two defects of one class shipped an hour apart, both found by a child rather
   than by this repo's own floor. Is there a check that would have caught
   either before the push — and if the answer is "the selftest, had it asserted
   the emitted command *runs*", does anything now assert that? Distinguish an
   assertion that the string has the right shape from evidence that the command
   works.
6. Item `070` recorded a conclusion — that only a floor-policy ruling could fix
   the wrapscan half — that the next commit withdrew. Follow the withdrawal:
   does any surface still carry the retracted claim, and did the correction
   reach the principal's decision queue as clearly as the original would have?
   A wrong finding that nearly cost a ruling is worth a note either way.
7. The delta's own frame is that a generator must not assume the repo it lives
   in. Apply that frame outward: do the other tools in `tools/` that write text
   into committed files (or into a child's terminal at the moment a check
   fails) make the same assumption anywhere? Name what you checked, including
   what you checked and cleared.
8. The rollout item `e2551da` states that the rollout shipped with this item's
   own gate still shut, and that every previous figure in it was low. Is the
   *current* set of figures reproducible at HEAD, and does the item now say
   what it counted — the failure mode the wrapscan arithmetic in `363a846`
   diagnosed one commit later?

**Cycle state:** CLOSED at 0 MAJOR (REVIEW.md: the cycle closes when a pass
returns no MAJOR finding); BG1–BG14 go to the principal's ruling round; this
pass applied nothing.
