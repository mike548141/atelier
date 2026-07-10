# Fable review — the method/ layer (propagation + harvest + PRINCIPLES keystone)

**Status:** brief (ask on top). Verdict appended below the divider after the
review runs. This is the review the 2026-07-10 build session deliberately
stopped for: the keystone `PRINCIPLES.md` + the whole new `method/` layer earned
their own review with fresh context before more content stacks on top (the
ROADMAP's "mechanism/review before more content" rule). Review **deep, not
fast** — generous Fable spend is authorised for this; it is structural,
load-bearing doctrine.

Nicely recursive: this applies the review lifecycle `REVIEW.md` just codified to
the doc that codified it. Run the three lenses on `REVIEW.md` too, not just past
it.

## What the work is (context for the reviewer)

Since the foundation review (`2026-07-10-atelier-foundation.md`, already
verdicted), the `method/` layer grew from its first slice to a near-complete
spine. In scope for this review — the net-new/changed docs at `atelier@957fa08`:

- **`PROPAGATION.md`** — the load-bearing architecture: "thin anchor, fat
  pointer" (a dependency + lockfile, for doctrine). Inlined safety floor + SHA
  pin + session-start drift check + the standard child doctrine block + the
  layer-override rule + the enforcement clause.
- **`EVIDENCE.md`** (harvest A1) — the machinery behind the apex's honesty:
  provenance, authority tiers, acquisition-method error risk, absolute dating,
  store-the-rule-not-the-value, one-fact-one-home, trigger-refresh,
  enforce-by-machine. Generalised from a private reference-library `STANDARDS.md`.
- **`REVIEW.md`** (harvest A2) — the enforcement half: more-capable-model review,
  three lenses, brief-on-top/verdict-below lifecycle.
- **`RECORD.md`** (harvest A3) — docs-as-code lockstep, append-only session log,
  ADRs, absolute dating.
- **`PRINCIPLES.md`** (the keystone) — extracted from stub to the canonical
  general spine: §1–7 + precedence ladder + situation tests, generalised off
  tiki's `docs/PRINCIPLES.md` with the cases **kept**.

Read the repo before reviewing: `README.md`, `docs/method/*`, `docs/ROADMAP.md`,
`docs/SESSIONS.md`, and — for the PRINCIPLES lens — the ros
`docs/PRINCIPLES.md` it was lifted from.

## Scope — three lenses, run all three

1. **Approach & assumptions** (most important — is this the right doctrine,
   shaped the right way?).
2. **Doctrine quality & honesty** (sound, internally consistent, no overclaim; a
   stub honestly a stub; no doc that claims more reach than it has).
3. **Completeness / harvest** (what these docs *should* cover and don't; what
   already exists in the child repos that they duplicated or ignored).

## Load-bearing assumptions to attack — by doc

If any of these is false, that doc is mis-built no matter how clean the prose.

### PROPAGATION.md

1. **The drift check actually fires.** The whole mechanism rests on a human/agent
   session running `git log PIN..HEAD` at session start and *acting* on output.
   The doc admits "observable, not enforced." Is that honest sufficiency, or a
   fig leaf that will rot silently the moment a session skips it? *Live datum for
   the reviewer:* in the session that wrote this brief, the check **did** fire and
   surfaced the moved commit — but n=1, and it was a diligent Opus session. Judge
   whether the mechanism survives an undiligent one.
2. **The inlined floor is a narrowing-free restatement of the apex + AUTONOMY
   floor.** This is directly checkable: diff the block's wording in
   `PROPAGATION.md` (and as stamped in `ros`/`faves` CLAUDE.md) against
   `00-APEX.md` and `AUTONOMY.md`. Any *silent* narrowing or contradiction is a
   defect — the doc claims "may compress but must not contradict." Does it hold?
3. **~15 lines can carry the safety floor.** Compression to fit is a stated goal.
   Is anything load-bearing dropped in the squeeze — a floor case that matters
   but didn't make the cut?
4. **Per-repo human pin-bump scales.** With N children, does staleness-made-
   visible actually get acted on per repo, or do most children rot behind a pin
   nobody moves? Is a fleet-level "which children are stale" view owed, and is
   its absence honestly acknowledged?

### EVIDENCE.md

5. **§12 enforce-by-machine has the reach it implies.** The validator story works
   "where the evidence lives in files." But most agent claims are ephemeral — in
   a chat reply, not a file. Does the doctrine have teeth for the *common*
   (in-conversation) case, or is §12 overclaiming, generalised too directly from
   the reference-library instance where everything *is* a file?
6. **The tier + acquisition taxonomy is usable in-loop, not just at authoring
   time.** Will an agent realistically tag every in-flight claim with tier and
   acquisition-risk, or is this aspirational ceremony that degrades to ignored?
   If aspirational, is it labelled as the *target discipline* honestly?
7. **Nothing load-bearing was lost lifting it off the private `STANDARDS.md`.**
   The reviewer can't see the source, but can sanity-check internal completeness:
   are the eleven+one rules mutually coherent, or are there seams where a
   client-advisory-specific rule was generalised into vagueness?

### REVIEW.md  ← attack this one directly

8. **"A *more capable* model reviews."** atelier's own economics are **Opus
   builds, Fable reviews** — and Fable is the *cheaper review tier*, not
   uniformly "more capable" than Opus. Is there a latent contradiction between
   REVIEW.md's "more capable where it counts" framing and what actually happens?
   The real value of the review may be **independence + different blind spots +
   fresh context**, not raw capability. Reviewer (you are Fable, reviewing this):
   say plainly whether "more capable" is the honest description of your own
   review of Opus's work, or whether the doc should be reframed to
   "independent, differently-blind, adversarial" with capability as one axis
   among several. This is the sharpest assumption in the batch.

### RECORD.md

9. **Lockstep docs-as-code is right *without exception*.** "A commit that leaves
   the man page stale is a broken commit" is stated absolutely. Is there a
   legitimate class of change where a doc follow-up genuinely *can* trail (e.g. a
   spike, an explicitly-marked WIP branch), making the absolutism a footgun that
   pushes people to skip the doc entirely rather than land it late? Or is the
   absolutism correct and the escape hatch a trap?

### PRINCIPLES.md (the keystone)

10. **The cases survived generalisation intact.** The claim is "generalised off
    tiki with the cases KEPT — a de-cased principle is theatre." Check each §1–7
    case: is it still concrete and teachable after the tiki specifics were lifted
    out, or did any collapse into an abstraction that no longer bites?
11. **The precedence ladder + situation tests still resolve real collisions.**
    Generalising can quietly drain a decision rule of its teeth. Do the ladder
    (protect > truth > availability > right-sized security > simplicity > cost)
    and the situation tests still adjudicate a concrete collision, or are they
    now too abstract to call a winner?
12. **KNOWN, do not re-flag as new:** the ros §1–7 prose still mirrors this
    canonical spine — a *transitional DRY breach*, flagged loudly at the top of
    ros `docs/PRINCIPLES.md` and ROADMAP-tracked for a focused ros trim session.
    The reviewer should **not** report this as a fresh finding; instead judge
    whether the *split of responsibility* is right (atelier = general spine; ros
    = bearings + case-law pointing up) so the pending trim has a sound target.

## Cross-cutting checks

- **DRY of the doctrine itself.** Absolute-dating and one-fact-one-home are now
  stated in EVIDENCE (§7, §9), RECORD, and PROPAGATION. Is the cross-referencing
  clean (one canonical home, the rest point to it), or has the doctrine layer
  begun violating its *own* one-fact-one-home rule by restating instead of
  linking? Name any restatement that should become a pointer.
- **Leak-check (these docs are shareable).** Scan for any personal/estate detail
  that shouldn't ship: EVIDENCE §8 uses "the fleet has 13 devices" and a
  `$40/mo` figure as illustrative stale-value anti-patterns — judge whether those
  are safely generic examples or real estate facts that leaked in and should be
  swapped for invented ones. Sweep all five docs the same way.
- **Honest stubbing of what's owed.** A6/A7, the full `MODEL-ECONOMICS.md`
  extraction, and the entire `build/` layer are pending. Confirm the docs +
  README + ROADMAP represent them as *absent/stubbed*, not falsely implied
  present (RECORD's own "stub honestly" rule, applied to this very batch).

## Real-world check (the honest test)

Doctrine is only real if it changes what a session does. For at least one doc,
find the evidence it already bit:

- **PROPAGATION** already fired once (this session's drift check). Did it behave
  as written — surface the moved commit, prompt a deliberate pin bump?
- **RECORD / REVIEW** — is this repo actually *run* by its own doctrine? Check
  that SESSIONS.md is append-only with detail-on-demand, that this very review
  follows the brief-on-top/verdict-below lifecycle, and that the foundation
  review's findings were dispositioned as REVIEW.md §4 requires — or flag the gap.

## Output format

Per `REVIEW.md` §3: append the verdict **below the divider in this file** —
per-lens answers, numbered findings with stable IDs (P1, E1, R1, V1, PR1…), each
tagged **[fixed]** or **[backlog]**, and a follow-up checklist. Then the ROADMAP
pointer ticks and a SESSIONS.md entry lands. A review that finds nothing on a
batch this structural is itself suspect — scope too narrow or read too fast.

---

<!-- Verdict appended here after the review runs. -->
