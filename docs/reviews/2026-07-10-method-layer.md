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

## Verdict (2026-07-10, Fable 5) — PASS-WITH-FINDINGS

Reviewed at `atelier@957fa08` (verified: `docs/method/` unchanged through HEAD
`1c09fa4`, so the brief's scope holds at HEAD). Read whole: the five in-scope
docs, `00-APEX`, `AUTONOMY`, both READMEs, `MODEL-ECONOMICS` stub, `CHANGELOG`,
`ROADMAP`, `SESSIONS.md` (+ its git history), the foundation review, the ros
`docs/PRINCIPLES.md` source, and the stamped `ros`/`faves` doctrine blocks.
Mechanical pass: `tools/leakscan.py` full-cover (local term list present) —
**clean**.

**Overall: the architecture holds.** Nothing in the layer is structurally
mis-built; the load-bearing mechanism (thin anchor, fat pointer) is live-proven,
the harvest docs are grounded not invented, and the keystone's ladder still
adjudicates real collisions. Findings are 10 small corrections **[fixed]** this
session + 3 **[backlog]** slices. A batch this structural yielding no
architectural rework is itself evidence the foundation review + sequencing rule
did their job.

### Lens 1 — approach & assumptions (per brief question)

1. **Drift check fires — yes, n=4 and honestly framed.** Documented firings:
   the pin-bump session (dde4170→957fa08, inspected, session-log-only, bumped),
   the worktree session (noted 4 commits, deliberately deferred the bump to a
   ros session), and this session (6 commits surfaced; bump lands with this
   verdict). It also fired *usefully* — each time the output was read and a
   deliberate decision followed. Against the undiligent-session test: the doc
   is honest that it doesn't survive one ("observable, not enforced") and names
   review as the catch. That is sufficiency, not fig leaf — **provided the
   signal stays binary**. The rot risk is alarm fatigue, not skipping: non-
   doctrine commits (tools, session logs) re-surface every session until
   someone bumps, training sessions to skim. Fix: make explicit that an
   inspection finding no doctrine-bearing change should still bump (**P3
   [fixed]**).
2. **Inlined floor narrowing-free — one real drop.** Diffed the canonical
   block and both stamped children against `00-APEX` + `AUTONOMY`: the apex
   compression is faithful (drops rationale, no rules); the confirm-floor
   covers 7 of AUTONOMY's items, but **new trust surfaces** (deploy keys,
   webhooks, CI secrets, OAuth/app grants) is only derivable via AUTONOMY's
   "same class as unapproved tool" — a child-only reader can't get there from
   the block's wording. Silent narrowing, exactly the class the doc forbids
   (**P1 [fixed]**: four words in the floor line; children adopt at next pin
   bump, ros this session).
3. **~15 lines carries the floor — yes**, with P1 fixed. Nothing else
   load-bearing was dropped; the deploy-on-push and secret-in-commit cases
   compress safely into "private→public" and "secrets".
4. **Per-repo pin bump scales — honest at N=2, unexamined at N=10.** No
   fleet-level "which children are stale" view exists and its absence is not
   acknowledged. Cheap house-pattern fix exists (a `tools/` script reading
   each child's pin). **P2 [backlog]** — acknowledge in PROPAGATION + tool
   candidate.
5. **EVIDENCE §12 reach — scoped honestly, boundary unnamed.** §12's opening
   qualifier ("where the evidence lives in files") avoids the overclaim, but
   the doc never says what enforces the *common* case — the ephemeral
   in-conversation claim. Answer: nothing mechanical; only the apex + the
   review loop. That's tolerable but must be said (**E1 [fixed]**).
6. **Tier taxonomy usable in-loop — yes.** Well-drafted on this exact point:
   §1 demands the agent *be able to answer* provenance on challenge, not tag
   every claim inline. "Treat un-sourced recall as ai-inference until
   grounded" is an actionable in-loop rule, not ceremony. Holds.
7. **Coherence off the private source — one seam.** §4 ("never assert an
   uncorroborated fact") generalised *too strongly* from the advisory context
   where every fact arrives through a reporting chain: read literally it
   forbids asserting what a primary artefact directly shows (code you read, a
   value you measured) because it "appears in exactly one place". Direct
   observation of the primary is its own corroboration — §3's acquisition
   risk still applies. Scope §4 to reported/external facts (**E2 [fixed]**).
8. **"More capable" (the sharpest ask) — the brief's premise is factually
   wrong, and the reframe is still right.** Plainly, as asked: the brief
   asserts "Fable is the cheaper review tier, not uniformly more capable than
   Opus". Per Anthropic's published positioning (official-guidance tier, not
   my self-assessment): Fable 5 is a Mythos-class model that sits **above**
   Opus in capability; it is the *more expensive, usage-billed* tier used
   sparingly — "cheaper" conflated price-of-the-pass with capability. So in
   this estate today, REVIEW.md's "more capable where it counts" is the
   literal truth: the most capable model is deployed at review because that's
   where its marginal value per token is highest. **However** the reframe is
   still owed, for the doctrine's stated audience: a peer adopting atelier may
   have no superior tier at all, and review by an equal model with fresh
   context still delivers the irreducible core — **independence + different
   blind spots + fresh context** — with capability as a multiplier, not a
   precondition. As written, the doc quietly makes review sound contingent on
   owning a better model. Reframed (**R1 [fixed]**).
9. **Lockstep absolutism — confirmed footgun, with a precise fix.** The
   legitimate trailing case is the WIP/spike **branch**: intermediate commits
   with stale docs are normal and harmless there. The discipline's real
   boundary is **integration** — what lands on the shared branch lands
   doc-complete. Stated absolutely, the rule pushes exactly the two failure
   modes the brief guessed (skip the doc, or squash away honest history).
   Scope it to the integration boundary (**V1 [fixed]**); this also lines up
   with CONCURRENCY's worktree-per-line (a line lands as a unit).
10. **Cases survived generalisation — where they exist.** §1, §2, §6 cases are
    concrete and still bite (batch-refusal, federation seam, voided-proof
    comment). But §3, §4, and §7 carry **no case at all**, and §5's "honest
    pattern" paragraph is a rule, not a decided case — while the preamble
    claims "each carries a *generalised case*". The ros source has the
    missing cases (triggered-apply-not-cron; plan/apply idempotent diff;
    standing-credential debt; hand-surgery-as-tracked-debt). Preamble
    currently overclaims — an honesty nit in the keystone itself. Add the
    cases (**PR1 [fixed]**).
11. **Ladder + situation tests still adjudicate — yes.** Ran the live
    collisions against the generalised text: apply-bulkhead resolves under
    "whose failure is it" (remote peer → skip loudly; own partial plan →
    refuse); gate-sizing still calls the re-class; mitigation-under-
    uncertainty still holds the narrow scope. Substance unchanged from ros;
    teeth intact.
12. **Split of responsibility — sound; trim guidance for the ros session.**
    Atelier general spine + ros bearings/case-law pointing up is the right
    shape. For the pending trim: ros must **keep** its §0 tiki bearing, every
    *Tiki bearing/Already holds* line, the seven-tenet Zero-Trust estate
    mapping in §5 (far richer than atelier's general §5 — that's bearings,
    not duplication), and the whole precedent-annotated trade-offs section;
    it should **drop** only the general prose sentences that restate the
    spine verbatim. Not re-flagged as a finding, per the brief.

### Lens 2 — doctrine quality & honesty

Sound and internally consistent overall; overclaim found in three small
places, all stale-truth rather than false-claim: the repo README still lists
PRINCIPLES as "extraction in progress" after the extraction landed (**H1
[fixed]** — a lockstep miss in the repo that wrote the lockstep rule);
CHANGELOG's *Pending* section still lists the PRINCIPLES extraction that its
own *Changed* section records as done (**H2 [fixed]**); and the PRINCIPLES
preamble's every-principle-has-a-case claim (PR1, above). Stubs are honestly
stubs: MODEL-ECONOMICS says so twice, build/README is an explicit
pointer-not-yet-extracted, ROADMAP matches. `method/README.md` is accurate
about canonicality (only the top-level README lagged).

### Lens 3 — completeness / harvest

- **REVIEW.md lacks a dispute path.** Dispositions are only [fixed]/[backlog]
  — acceptance is structurally forced; a builder/owner who *disagrees* with a
  finding has no sanctioned move except silence, which is the one resolution
  the layer-override rule forbids elsewhere. Add **[rejected: grounds]**
  (**R2 [fixed]**).
- **The repo's own re-litigable decisions have no ADRs.** `docs/decisions/`
  holds only the template, yet SHA-as-version (vs tags), canonicality,
  private-first, and Apache-2.0 are all textbook re-litigation risks by
  RECORD's own test — currently recorded only as prose in
  SESSIONS/ROADMAP/PROPAGATION. **V2 [backlog]** — three or four short ADRs,
  a build-session task.
- **SESSIONS.md is outgrowing its own doctrine.** Recent entries run 30–60
  lines inline; RECORD prescribes index + detail-on-demand for exactly this.
  Adopt the ros split before it gets expensive (**V3 [backlog]**).
- Cross-cutting DRY of the doctrine: clean. Absolute dating and
  one-fact-one-home each have one canonical home (EVIDENCE §7/§9) and the
  restatements carry pointers. The one restatement worth trimming toward a
  pointer someday is RECORD's "Absolute dating" section — noted, not a
  finding.
- Leak-check (manual + leakscan): **clean**, one judgement nit — EVIDENCE §8
  uses "the fleet has 13 devices", a real estate figure, as its illustrative
  stale value; invented numbers cost nothing (**L1 [fixed]**). The `$40/mo`
  and legislative examples read as generic. No names, hosts, or addresses in
  any of the five docs.

### Real-world check

**PROPAGATION bit, as written** — four firings, each producing a deliberate,
recorded decision (bump / defer / bump-with-this-review). **The repo runs on
its own doctrine**: SESSIONS.md verified append-only against git history (zero
deletion lines since birth); this review followed REVIEW.md's lifecycle
end-to-end (brief on top → this verdict below the divider → dispositions →
ROADMAP tick + SESSIONS entry); the foundation review's findings were all
dispositioned [fixed]/[backlog] with the backlog traceable in ROADMAP. The two
places practice lags the text are V2 (no ADRs) and V3 (inline session bloat) —
both named above, neither structural.

### Findings — dispositions

| ID | Doc | Finding | Disposition |
|---|---|---|---|
| P1 | PROPAGATION | Inlined floor drops "new trust surfaces" — silent narrowing for child-only readers | **[fixed]** block + ros stamped copy |
| P3 | PROPAGATION | Drift-check noise: state that inspect-then-bump applies even when the delta doesn't bear on the repo | **[fixed]** |
| P2 | PROPAGATION | No fleet-level staleness view at N children; absence unacknowledged | **[backlog]** |
| E1 | EVIDENCE | §12 doesn't name the ephemeral-claim boundary (no validator for in-conversation claims) | **[fixed]** |
| E2 | EVIDENCE | §4 over-generalised: direct primary observation needs no second source | **[fixed]** |
| L1 | EVIDENCE | §8 "13 devices" is a real estate figure in a shareable doc | **[fixed]** |
| R1 | REVIEW | Reframe: independence + fresh context is the irreducible core; capability the multiplier (brief's capability premise also corrected) | **[fixed]** |
| R2 | REVIEW | Add **[rejected: grounds]** disposition — silence must not be the only way to disagree | **[fixed]** |
| V1 | RECORD | Scope lockstep to the integration boundary; WIP branches may trail until they land | **[fixed]** |
| V2 | RECORD (practice) | Write the missing ADRs (canonicality, SHA-as-version, private-first + licence) | **[backlog]** |
| V3 | RECORD (practice) | Split atelier SESSIONS.md to index + detail-on-demand | **[backlog]** |
| PR1 | PRINCIPLES | §3/§4/§5/§7 lost their cases in extraction while the preamble claims universal coverage — add generalised cases from ros | **[fixed]** |
| H1 | README | Stale "extraction in progress" for PRINCIPLES | **[fixed]** |
| H2 | CHANGELOG | *Pending* contradicts *Changed* on the PRINCIPLES extraction | **[fixed]** |

### Follow-up checklist

- [ ] **P2** — acknowledge the fleet-staleness gap in PROPAGATION when built;
      candidate `tools/` script that reads every child's pin and reports lag.
- [ ] **V2** — ADRs for canonicality, SHA-as-version, private-first+Apache-2.0
      (record the decisions already taken; a build session's task).
- [ ] **V3** — adopt the index/detail session-log split in atelier itself.
- [ ] **faves** — its stamped block adopts the P1 floor wording at its next
      pin bump (drift check will surface it; deliberately not edited from this
      session — atelier is the only granted working dir here besides ros).
- [ ] The **ros PRINCIPLES trim** may now proceed: this review trusts the
      atelier spine; trim guidance is in lens-1 answer 12.

*Review conduct note (EVIDENCE §2 discipline): the capability claim in R1 is
tiered official-guidance (Anthropic's published model positioning), not the
reviewer's self-assessment; every other finding is grounded in a direct read
of the artefacts named, at the SHAs stated.*
