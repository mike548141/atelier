# Review brief — B4 `harvestscan` cold pass (build + measurement + verdict)

- **Date:** 2026-07-29 1306 UTC
- **Subject:** commit `ff8080b` — `tools/harvestscan.py`,
  `tools/test_harvestscan.py`, and the B4 roadmap entry carrying the
  390-commit measurement and the **deliberately-not-wired** verdict. The
  reviewable commitment includes the verdict itself: the author reached
  "do not wire, not even advisory" about its own instrument, and shelving
  a guard is as reviewable as shipping one.
- **Spawn provenance (rule 4):** same Mike-spawned taker session as the E6
  and B2+B3 passes (Fable 5); author of nothing in the Track B chain; claim
  on `main` (`3cad1a9`) precedes this worktree.
- **Deferral exposure — named, not denied.** B4 shares its intent record
  (`sessions/2026-07-28-1233-track-b-enumerator.md`) with B2+B3, and this
  taker opened that record at the B2+B3 reconcile step — *before* this
  brief. What was therefore seen early: the author's "the detector works;
  the discriminator does not", its do-not-wire counsel, the
  `SURVIVAL_SIMILARITY`-left-alone rationale, the three-step measurement
  narrative, and the addendum about this pointer's own refs-only breach
  (a seeded first question, since scrubbed). Handling per REVIEW.md's
  application-review shape: the exposure is stated, the author's claims
  are treated as **seeded questions — a floor, never a fence** — and this
  reviewer's attack surface below is its own. The residual risk (framing
  inherited through the early read) cannot be unwound and is left on the
  record for Mike to weigh against the verdict.
- **Scanner reach:** `/security-review` discharged — landed delta, nothing
  in flight. Mechanical floor: the tool's tests, plus this pass's own
  replays.

## Scope — four lenses

1. **Approach:** is content-fingerprinting the right detector for
   lost-work deletions, and is per-commit firing rate the right
   *discriminator* measure to hang a wire/no-wire verdict on?
2. **Correctness:** does the tool do what the entry claims — including the
   two headline replays (26.9% over 390 commits; 2 items at `dd7fcb74`
   including the genuinely lost one)? Re-run, not read.
3. **Completeness:** what already guards this file (sizescan's
   cold-content/harvest-integrity gates; ROADMAP-DONE conventions) and
   whether B4's risk is left wholly unmitigated by shelving; the wireable
   variants the entry itself lists (delete-only commits, branch-base
   comparison) — costed or hand-waved?
4. **Security & privacy:** minimal surface (local git only) — verify no
   network, no write paths, and that replay output cannot leak private
   content into public records.

## Load-bearing assumptions to attack (the reviewer's own)

- **A1 — the replay methodology models the hook.** Each commit judged
  against its parent exactly as a staged hook would see it: merges,
  renames of `ROADMAP.md`, and multi-file commits handled coherently?
- **A2 — the 26.9% figure is reproducible** from the shipped tool at the
  shipped thresholds, and the `dd7fcb74` replay reports 2 items including
  the lost one. Re-run both.
- **A3 — "one in four commits warns ⇒ allow-markered into silence" is the
  right inference.** The premise imports the 2026-07-26 audit's rate-
  tolerance claim; test whether the *scoped* variants (delete-only
  commits — what fraction of the 390? — or bulk-deletion threshold) were
  measured before the verdict generalised to "do not wire, not even
  advisory", or only named as future shapes.
- **A4 — false negatives are known.** The verdict leans on false-positive
  rate; what is the *miss* rate on the one class that matters (real lost
  work)? A guard judged only on its noise is half-judged.
- **A5 — the tests bite:** 16 tests claimed; is there a red leg proving
  detection of a genuine lost-item deletion (the `dd7fcb74` class), and a
  leg pinning the bookkeeping-strip/containment behaviours?
- **A6 — `SURVIVAL_SIMILARITY` left alone.** The constant-fitting
  argument is sound in general; verify the constant's provenance is
  stated (grounded in the class, not the corpus — the repo's own
  ground-numeric-limits rule) rather than simply frozen.
- **A7 — shelved ≠ abandoned is real.** "Hand-run before deliberate bulk
  deletions" only works if something *tells* a session to hand-run it;
  is there any hook, doc line, or checklist wiring that intent, or is the
  shelf a memory-reborn pattern?

---

# Verdict — PASS-WITH-FINDINGS (1 MAJOR / 2 minor / 2 notes)

- **Date:** 2026-07-29 (UTC) · **Reviewer:** Fable 5, cold (deferral
  exposure as stated in the brief — the shared intent record was read at
  the B2+B3 reconcile, before this brief)
- **Provenance repeated (rule 4):** Mike-spawned taker, author of nothing
  in the chain; claim `3cad1a9` on `main` before the worktree.
- **Scanner line:** `/security-review` discharged (landed delta, nothing
  in flight). Mechanical floor: 16 unit tests + selftest green, plus this
  pass's own replay harness.
- **Overall:** the tool is well built and unusually honest about its own
  epistemics; every recorded figure reproduces exactly. The MAJOR is not
  in the code — it is in the **verdict**: "do not wire, not even
  advisory" was generalised from the unscoped measurement alone, and this
  pass's replay of the variant the entry names-but-never-measured points
  the other way.

## Re-run and verified

- **Selftest + 16 unit tests green**, including two must-fire legs (a
  genuinely lost item is reported) and the never-fails-a-build contract.
- **The headline measurement reproduces exactly.** This pass rebuilt the
  replay (the harness itself did not ship) from the tool's pure
  functions: over the 391 commits touching `docs/ROADMAP.md` up to the
  landing commit — **105 fired (26.9%), 158 items** — identical to the
  recorded 105 / 26.9% / 158. The recorded figures are honest and
  reproducible.
- **The `dd7fcb74` probe reproduces:** 2 items reported, including the
  genuinely lost completed item; the commit's shape was **+48/−184**.
- **`SURVIVAL_SIMILARITY` is honestly ungrounded** — labelled a tuning
  constant, left unmoved, with the fitting-a-constant refusal stated at
  the constant itself (A6 satisfied).
- **Security surface minimal as claimed:** local `git show` reads only,
  no network, no writes; findings print 160-char excerpts locally.

## Findings

- **HV1 (MAJOR — on the verdict, not the code) — "do not wire, not even
  advisory" rests on the unscoped measurement only, and the measured
  scoped variant points the other way.** The entry lists three wireable
  shapes and measures none; the tool's pure functions make that a
  minutes-long job (this pass did it). Measured over the same 391
  commits: scope the guard to **net-bulk-delete commits (≥50 net lines
  removed from the roadmap)** and the entire history contains **6
  in-scope commits, of which 3 warn — `dd7fcb74` (the motivating
  incident, caught) and two mass harvests (9 and 12 items condensed to
  the archive), which are precisely the diffs that merit eyes.** That is
  ~0.8% of all commits against the 26.9% that grounded the
  allow-marker-fatigue argument. A second, sharper correction to the
  entry: its **first-ranked** wireable shape — "commits that *only*
  delete" — would have **missed the incident**: `dd7fcb74` carried 48
  additions alongside its 184 deletions, so the workable scope is net
  line loss (or merge-base comparison), not strict delete-only. Counsel:
  re-put the wire/no-wire decision to Mike with these numbers — on this
  evidence a bulk-delete-scoped advisory is wireable (registry advisory,
  never blocking, per the tool's own threshold honesty); the decision is
  the principal's (rule 3 — enforcement doctrine by function).
- **HV2 (minor) — the pointer exclusion assumes a ceiling the record
  shows breached.** `is_pointer` skips `⏳` items because refs-only
  pointers hold no work-content — but this repo has recorded **three
  instances** of pointers carrying evaluative content. A content-bearing
  pointer that vanishes is invisible to this guard *by design*. The
  cheap mitigation is already FUNDED: the `reviewscan` ⏳-grammar check —
  once pointers are mechanically refs-only, the exclusion is sound.
  Name the dependency in the B4 entry so the two items are decided
  together.
- **HV3 (minor) — the survivor search is narrower than the docstring
  claims.** "A sufficiently similar body exists anywhere in the tracked
  records … or any other record" — the default search is exactly two
  files (`ROADMAP.md`, `ROADMAP-DONE.md`). An item harvested into a
  session record, a review file, or promoted into `method/` doctrine
  reads as vanished; the two mass-harvest warns above may be partly this.
  Either widen the default record stores (measure first — the harness
  exists now) or correct the docstring to name exactly what is searched.
- **HV4 (note) — plane wording.** Usage says "compare staged/working
  records against HEAD"; survivors are read from the **working tree**
  only. One word to fix now — and if the guard is ever wired, the hook
  plane reads *staged* content, a seam worth naming in the entry.
- **HV5 (note) — the shelf has no carrier.** "Run by hand before a
  deliberate bulk deletion" is wired to nothing — no doc line, checklist,
  or hook names the intent, which is the memory-reborn pattern the
  create-repo sweep named. One line in the ROADMAP header or `RECORD.md`
  beside the bulk-deletion moment would carry it. (If HV1 resolves as
  "wire scoped", this lapses.)

## Reconcile

The shared intent record was read before this brief (exposure disclosed
there). Re-read after findings were drafted: the author's account adds
nothing that answers HV1 — the scoped variants are named as future value
in both the entry and the record, unmeasured in both; the addendum's
history of this pointer's scrubbed steer ("test the verdict as well as
the code") converges with what this pass did on its own criteria, and
Mike's queueing note asked for exactly that. No contradiction found;
HV1's numbers are new evidence, not a re-reading.

## Decision — Mike's (rule 3)

HV1–HV5 await rulings; nothing applied. Cycle stays open (1 MAJOR):
rulings → application (own rule-4 pointer) → terminal pass.

## Rulings (Mike, 2026-07-29, plain-language walk-through with per-option
impacts; recorded verbatim by the reviewer, applied by no one yet)

- **HV1 — RULED: wire it, scoped, advisory.** The shelf verdict is
  overturned on the pass's measurement: `harvestscan` joins the registry
  scoped to net-bulk-delete roadmap commits (≥50 net lines removed),
  warn-only, never blocking (its threshold is honestly ungrounded, so a
  block would overclaim). Evidence basis: 6 in-scope commits in the
  391-commit history, 3 warns, all justified, the motivating incident
  caught; strict delete-only rejected because it misses the incident
  (+48/−184).
- **HV2 — RULED: accept.** The `is_pointer` exclusion's dependency on
  the FUNDED `reviewscan` ⏳-grammar check is named in the item; the two
  are decided/built together.
- **HV3 — RULED: accept.** The survivor search is widened to the record
  stores that actually receive harvests (`docs/sessions/`,
  `docs/reviews/`), with the effect measured by the replay harness
  before landing; the docstring names exactly what is searched.
- **HV4 — RULED: accept.** The usage wording is corrected, and the
  wiring build handles the staged-vs-working-tree seam properly (the
  hook plane reads staged content).
- **HV5 — LAPSED under HV1.** With the guard wired there is no shelf to
  carry a hand-run trigger for.

**Application owed:** one wiring build item (scope logic + tests +
registry entry + HV2–HV4 folds); it queues its rule-4 pointer in the
landing commit.
