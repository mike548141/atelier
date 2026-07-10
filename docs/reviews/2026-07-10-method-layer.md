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

## Verdict (2026-07-10) — Fable 5, usage-billed, fresh context

Read: all five in-scope docs + `00-APEX.md`, `AUTONOMY.md`, `MODEL-ECONOMICS.md`,
README, ROADMAP, SESSIONS tail, the foundation review, ros `docs/PRINCIPLES.md`,
and both stamped child blocks (ros + faves CLAUDE.md). Mechanical leak-scan run
over the five docs: **clean** (structural + local terms). Live datum worth
recording first: **this review session initially started on Opus by accident;
the MODEL-ECONOMICS "state your model + pool before spend" rule surfaced it in
the first line and Mike swapped to Fable before any review spend** — the
doctrine bit, live, before the review even began.

### Overall: PASS-WITH-FINDINGS

The layer is sound, honestly built, and demonstrably *lived* (drift check fired
n=2; review lifecycle followed recursively; leak boundary mechanically clean).
One framing defect was real and load-bearing — REVIEW.md's "more capable model"
(Q8/R1, fixed this session). The rest are compression drops, honest-gap
sentences owed, and small lockstep misses. Nothing invalidates the architecture.

### Per-question answers

**Q1 — drift check fires?** Honest sufficiency, with one overclaim now fixed.
Evidence: n=2 fires, both behaving exactly as written (surfaced the moved
commit → inspected → deliberate bump; documented in SESSIONS). It does *not*
survive an undiligent session, and the doc says so plainly ("observable, not
enforced"). The defect was downstream: the enforcement clause implied the review
loop catches the session that ignored the check, but reviews trigger on
structural/irreversible work — a routine session that skips it goes uncaught
until the next reviewed slice. That window is now named in the doc (P3
[fixed]). The mechanism *bounds* staleness; it never claimed to eliminate it —
and now it says which bound.

**Q2 — inlined floor narrowing-free?** Checked word-by-word against `00-APEX.md`
+ `AUTONOMY.md`, and both stamped children against the canonical block. The
children match the canonical text (ros appends its bearing line, faves appends
its publication-bound note — both legal narrowing/appending). But the canonical
block itself had **two silent drops** vs AUTONOMY's floor — see Q3. No
*contradiction* of the apex; the apex compression is faithful.

**Q3 — ~15 lines carries the floor?** **No — two load-bearing cases fell in the
squeeze.** (a) **New trust surfaces** (deploy keys, webhooks, CI secrets,
OAuth/app grants) — a full floor item in AUTONOMY, absent from the block; a
block-only agent could add a webhook unconfirmed. (b) **Deploy-on-push,
non-routine**: the block's "everything recoverable — commit/push/PR included —
just proceed" silently *loosens* AUTONOMY's confirm-first rule for a push that
publishes a new content class on a deploy-on-push repo (faves patched this
locally in its own block; the canonical text would have carried the loosening
to every future child). Both restored (P1, P2 [fixed]); the spec now reads ~20
lines with an explicit "compress prose, never floor coverage" rule. Children
re-stamp at next pin bump.

**Q4 — per-repo pin bump scales?** Proven at n=2, unproven beyond, and the doc
doesn't acknowledge the fleet-scale gap: staleness is observable only from
*inside* a session in that repo, so a dormant child rots invisibly. A
fleet-level drift view (for each child: pin vs atelier HEAD — a five-line
script or CI job) is owed and now ROADMAP-tracked (P4 [backlog]).

**Q5 — EVIDENCE §12 reach?** §12 scoped itself honestly ("where the evidence
lives in files") but stayed silent on what enforces the *common* case — the
in-conversation claim. Answer: nothing mechanical; only the apex plus the
review practice. That gap is now named in §12 (E2 [fixed]). Not an overclaim as
written, but an omission the apex style requires filling.

**Q6 — tier taxonomy usable in-loop?** Mostly honestly framed already: §1 says
the agent "must be able to answer" — capability on demand, not per-sentence
annotation ceremony. What was missing is the explicit two-register statement:
durable artifacts carry provenance *written down*; in-flight claims carry it
*on demand* + guesses labelled unprompted. Added to §1 (E3 [fixed]). With that,
this is target discipline honestly scoped, not aspirational ceremony.

**Q7 — seams from the lift?** One found. §4 ("never assert an uncorroborated
fact") is a reference-library rule that over-fires when generalised: a primary
artifact read directly (the code, the config, the measured output) appears in
exactly one place and needs no second source — it *is* the corroboration. The
letter of §4 forbade asserting it. Scoped (E1 [fixed]). Otherwise the eleven+one
rules are mutually coherent; §6's legislative flavour (bills, exposure drafts)
reads as worked examples, not vagueness. §11 generalised cleanly and is one of
the strongest sections.

**Q8 — "more capable model" (the sharpest ask).** **The framing does not hold,
and I am the counterexample.** I am Fable reviewing Opus's work — the *cheaper
review tier*, deliberately, per the house's own economics. MODEL-ECONOMICS
already states the true mechanism: "a capable plan-included model does the
*building*; a **separate, usage-billed** model does *review*" — separateness,
not superiority. So REVIEW.md contradicted its own economics doc. What actually
made this review bite: (1) **independence** — I carry none of the build
sessions' momentum or sunk-cost framing; (2) **different blind spots** — a
different model errs differently; (3) **the adversarial brief** — named
assumptions to attack; (4) **sufficient capability** — a real floor (a much
weaker reviewer would rubber-stamp this material), and for structural work "the
most capable reviewer economics allow" remains right. Capability is one axis
and a floor — not the definition. REVIEW.md reframed accordingly, with the
reframe recorded in-place as an honest correction; the same phrase aligned in
PROPAGATION's enforcement clause, README, and RECORD (R1 [fixed]). Note APEX's
"capability scopes authority" and AUTONOMY's "who acts" are about *building*
authority over live systems and were already correct — no change there.

**Q9 — lockstep absolutism?** Correct, with a scope clarification rather than
an escape hatch. The doc already contained the resolution in its own words
("...a lie the moment it **merges**") while stating the rule per-commit. Now
explicit: lockstep binds what lands on the shared branch; a spike/WIP commit
may trail its doc on its own branch; the merge is where it holds (V1 [fixed]).
This kills the footgun (nobody is pushed to skip docs to avoid "breaking" WIP
commits) without opening the "doc follows next week" hole on trunk — which
remains exactly the lie the rule exists to kill.

**Q10 — cases survived generalisation?** Substantially yes — the batch-op
anti-pattern, the federation seam, the voided-"proven"-comment cautionary case,
and the gate re-classing precedent all still bite as generalised. Two situation
tests, however, lost their precedent anchors entirely (mitigation-under-
uncertainty; special-case-vs-uniform) while the section header claims "every
ruling below generalises a real decided case". Both regained a one-line
generalised precedent (PR1 [fixed]); the header claim now holds. The Zero-Trust
compression (seven tenets → summary + name-the-gap) is the right split — the
tenet-by-tenet detail is estate-specific and correctly stays in ros.

**Q11 — ladder + tests still adjudicate?** Yes, and there is fresh live
evidence: the leak-scan-on-tiki decision (structural IP/MAC rules blocking
routine networking work → `--disable`, per the gate-sizing test: "a control
stricter than its threat trains bypass") is a real collision this repo resolved
*using* these tests, post-generalisation. The ladder retains teeth.

**Q12 — the split (not re-flagged, as instructed).** The split is right:
atelier = general spine with generalised cases; ros = bearings + named
precedents, pointing up. One guardrail for the pending trim session: after the
trim, ros's named case-law (D1, poe-cycle, change_policy) will be invisible to
peer adopters — so **before deleting ros §1–7 prose, confirm every atelier
case/test stands alone as a complete teachable statement** without the ros
detail behind it. Tracked in the follow-ups item (PR2).

### Cross-cutting

- **DRY of the doctrine:** clean. One-fact-one-home is canonical in EVIDENCE §9
  and pointed to (not restated) from RECORD, PRINCIPLES §2, and PROPAGATION.
  The single borderline restatement is RECORD's absolute-dating section, which
  repeats EVIDENCE §7's two rationales rather than just pointing — judged
  acceptable (two-line compression *with* citation, low drift risk); noted,
  no change.
- **Leak-check: clean.** Mechanical scan (structural + seeded local terms)
  passes on all five docs. EVIDENCE §8's "13 devices"/"$40/mo": judged **safely
  generic** — unattributed, no entity, no identifying combination; they read as
  invented illustrations whether or not they once were real. No swap needed.
- **Honest stubbing: holds, with one lockstep miss.** MODEL-ECONOMICS is loudly
  a stub; A6/A7 + build/ are ROADMAP-tracked open; docs/build/ exists (stub
  README). The miss: README still said PRINCIPLES' "canonical source is
  currently ros" — false since the extraction, and the extraction commit should
  have updated it (RECORD's own rule). README's method list also omitted four
  shipped docs (PROPAGATION, EVIDENCE, REVIEW, RECORD) + DATA-PROTECTION +
  TOOLBOX. Both fixed (X1 [fixed]).

### Real-world check

- **PROPAGATION bit, as written, twice:** dde4170-pin session surfaced 957f08 →
  inspected → deliberate bump (SESSIONS, 2026-07-10). Behaviour matched the doc
  exactly.
- **The repo is run by its own doctrine:** SESSIONS.md is append-only; the
  foundation review is brief-on-top/verdict-below with every finding
  dispositioned [fixed]/[backlog] per §4; this review recursively follows the
  same lifecycle. One practice gap: RECORD prescribes index + detail-on-demand,
  but atelier's own SESSIONS entries are ~40-line full-detail inline (V2
  [backlog] — split at the next natural point, or decide the threshold hasn't
  been reached and say so).
- **Bonus:** the state-your-model rule caught this session starting on the
  wrong model (top of verdict). Two mechanisms, both proven live.

### Findings

| ID | Doc | Finding | Disposition |
|---|---|---|---|
| P1 | PROPAGATION | Block floor dropped **new trust surfaces** (deploy keys/webhooks/CI secrets/OAuth) | **[fixed]** — restored to canonical block; children re-stamp at next bump |
| P2 | PROPAGATION | Block's "push — just proceed" silently loosened AUTONOMY's deploy-on-push non-routine confirm | **[fixed]** — new-content-class qualifier added |
| P3 | PROPAGATION | Enforcement clause implied review catches every ignoring session; review-trigger policy leaves routine-work windows | **[fixed]** — honest window named |
| P4 | PROPAGATION | No fleet-level staleness view; dormant children rot invisibly | **[backlog]** — ROADMAP follow-ups |
| E1 | EVIDENCE | §4 over-fires on primary direct reads (reference-library seam) | **[fixed]** — scoped |
| E2 | EVIDENCE | §12 silent on the in-conversation (common) case having no validator | **[fixed]** — gap named |
| E3 | EVIDENCE | Artifact-ceremony vs in-loop discipline registers not distinguished | **[fixed]** — two-register rule in §1 |
| R1 | REVIEW | "More capable model" framing contradicts MODEL-ECONOMICS + observed practice; independence is the mechanism | **[fixed]** — reframed here + PROPAGATION + README + RECORD, reframe recorded in-place |
| R2 | REVIEW | Reviewer write-authority + builder/reviewer disagreement path unstated | **[fixed]** — added to lifecycle §4 |
| V1 | RECORD | Lockstep absolutism per-commit vs its own "moment it merges"; WIP footgun | **[fixed]** — scoped to the shared branch |
| V2 | RECORD | atelier's own SESSIONS.md ignores the index/detail split it prescribes | **[backlog]** — split at next natural point |
| PR1 | PRINCIPLES | Two situation tests lost precedent anchors; header claims all rulings are cased | **[fixed]** — generalised precedents restored |
| PR2 | PRINCIPLES | Trim-session guardrail: atelier cases must stand alone before ros §1–7 prose is deleted | **[backlog]** — guardrail on the existing trim item |
| X1 | README | Stale PRINCIPLES canonicality line + four shipped method docs unlisted (lockstep miss) | **[fixed]** — README updated |

### Follow-up checklist

- [ ] **Fleet drift view** (P4): per child, pin vs atelier HEAD — script or CI;
      five lines, closes the dormant-child blind spot.
- [ ] **Re-stamp ros + faves doctrine blocks** at each repo's next pin bump —
      pick up the P1/P2 floor restorations (the mechanism will surface this
      itself once this branch merges).
- [ ] **SESSIONS.md index/detail split** (V2) at the next natural point.
- [ ] **ros PRINCIPLES trim guardrail** (PR2): verify each atelier case/test
      stands alone before deleting the ros §1–7 prose.
- [ ] CHANGELOG line per doctrine change: **done this session** (R1/P1/P2 etc.
      are doctrine changes; children's drift checks will surface them — that is
      the mechanism working, not a side effect).

*Reviewer's honesty note, per the apex: this session both found and fixed R1 —
finding-and-fixing in one session is sanctioned by the §4 rule this review
itself added (R2). The circularity is real and is why the rule distinguishes
small doctrine-consistent fixes (these) from structural rework (handed back).
If Mike judges any fix here structural, revert it to [backlog] — the findings
stand either way.*
