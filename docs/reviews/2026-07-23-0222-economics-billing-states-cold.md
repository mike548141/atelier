# Cold review (rule 4) — economics rework: billing states of the marginal token

**Subject (refs only):** delta commit `dadde1d` at HEAD. Touched surfaces:
`docs/method/ECONOMICS.md`, `docs/build/templates/docs/ECONOMICS.md`,
renamed-section cross-references in `docs/method/REVIEW.md` and
`docs/method/CONCURRENCY.md`, plus the intent record
`docs/decisions/2026-07-23-0001-billing-state-of-the-marginal-token.md`
(deferred — not opened until the reviewer's findings were durably written; see
the reconcile section below the verdict).

**Spawn provenance:** this review was spawned by a non-author taker session that
the principal (Mike) opened and pointed at the review queue on 2026-07-23; the
work's author neither started nor instructed this review or this reviewer; the
taker authored none of the delta and gave the reviewer refs only, no evaluative
account.

**What the work is, as this reviewer establishes it from the delta and HEAD:**
the provider moved the capable model into the operator's subscription
(plan-included up to a capped share, usage-billed past it, faster draw-down),
which broke `ECONOMICS.md`'s two-pool billing binary. The delta reworks the
opening frame into three billing states of the *marginal token*
(plan-included / plan-included-capped / usage-billed) plus a draw-down-rate
refinement; renames the self-check to the marginal-cost self-check with two
guards (dear-meter builds; silent cap-crossing) and a stop-or-pay cap rule
hooked to `AUTONOMY.md`'s spend floor; adds two hard edges to the tier ladder
(capacity never picks the tier; hand-ups are noisy and end at the principal);
adds a third seat to the orchestrated-run split (fan-out below the workhorse;
a per-run stepped-down-executor trial); re-grounds the child ECONOMICS
template; and updates two renamed-section cross-references. Self-authored
doctrine — a Fable session's wording encoding the principal's quoted rulings —
so REVIEW.md rules 3–4 govern: findings below are the principal's to decide;
this reviewer applies nothing.

**Attack surface, named by this reviewer as its first act:**

1. **Faithful encoding** — the wording claims to encode three principal
   rulings. Does the doctrine text over-reach, under-reach, or smuggle
   author judgement beyond what was ruled? (Checked twice: against the delta's
   own claims first; against the quoted rulings at the reconcile step.)
2. **Frame coherence at HEAD** — the delta replaces "pools" with "billing
   states". Does the rest of `ECONOMICS.md`, and every doc that describes it,
   still read true — or does the old frame survive in unswept remnants
   (the same-commit stale-claim sweep, 00-APEX adaptation / PRINCIPLES §6)?
3. **Enforceability of the new self-check** — the rule now mandates stating a
   capped model's distance from its cap. Is that observable from where the rule
   binds, and what does an honest session do when it isn't?
4. **The template as propagation surface** — the child template hard-coded the
   old billing mapping and went stale when the plan moved. Does the fix remove
   that failure mode or re-instantiate it?
5. **Cross-reference integrity** — every renamed-section pointer the delta
   touched, and every pointer it *should* have touched, resolves and reads true
   (`AUTONOMY.md` spend floor, `CONCURRENCY.md` role check and
   deliberately-not-in list, `REVIEW.md` triggering section, both READMEs,
   REPO-STANDARD, ROADMAP/CHANGELOG claims).
6. **Privacy at design altitude** — the repo is public and billing/plan details
   are person-local by this doctrine's own boundary: does the delta leak plan
   names, prices, cap shares, entitlements, or other estate specifics?

**The four lenses:** approach & assumptions (is billing-state-of-the-marginal-
token the right frame, and are its load-bearing assumptions true); correctness &
quality (does the text do what the commit claims, honestly); completeness /
harvest (what the sweep missed, what siblings contradict); security & privacy
(the leak surface above, plus the mechanical floor re-run).

**Re-run obligations taken on:** the four scanners as the pre-commit hook
invokes them (whole-tree modes — nothing is staged on a landed delta), and both
test suites (`node --test instruments/*.test.js`,
`python3 -m unittest discover -s tools`).

**Deviations owned:** while sweeping HEAD for stale two-pool terminology, one
grep's matched lines included four to five lines of the deferred intent record
before findings were committed. The exposed fragments (the two-pool-binary
diagnosis, the provider-move description, the three-state list, and a mention
that the old template hard-coded the billing mapping) overlap the delta's own
commit message, so the contamination is small — but the deferral discipline was
dented, and this note names it rather than denying it. Findings EB1–EB8 were
established from the delta and HEAD before the record was opened in full.

Brief written 2026-07-23 0229 UTC, before the deep pass's findings were
finalised and before the deferred record was opened.

---

# Verdict — PASS-WITH-FINDINGS (0M/4m/3L/1n)

**Spawn provenance (repeated):** this review was spawned by a non-author taker
session that the principal (Mike) opened and pointed at the review queue on
2026-07-23; the work's author neither started nor instructed this review or
this reviewer; the taker authored none of the delta and gave the reviewer refs
only, no evaluative account.

**What was re-run, with results (2026-07-23, this worktree at `main`/HEAD):**

- `python3 tools/secretscan.py --root . .` — ✅ clean, exit 0.
- `python3 tools/leakscan.py --root . .` — ✅ clean (structural + local), exit 0.
- `python3 tools/linkscan.py --root . .` — ✅ every internal link resolves,
  exit 0 (this proves the delta's renamed-section pointers *resolve*; findings
  EB1/EB7 are about pointers that resolve but read false or misdirect — a class
  linkscan cannot see).
- `python3 tools/reviewscan.py --root . .` — ✅ clean; 3 post-2026-07-21
  decision records carry a review line (the delta's own intent record among
  them), exit 0.
- `node --test instruments/*.test.js` — ✅ fail 0, exit 0.
- `python3 -m unittest discover -s tools` — ✅ OK, exit 0.
- `/security-review` — discharged, not run: the delta is landed markdown
  doctrine; the scanner scans pending diffs and excludes markdown
  documentation, so there is nothing it can genuinely be aimed at here and a
  clean pass would be definitionally empty (REVIEW.md lens 4, the SL2
  caution).

**Lens 4 discharge (privacy, design altitude):** no MAJOR leak. The delta adds
no plan name, no prices, no cap percentage, no allowance figures, and no
personal data; the principal's quoted ruling contains no estate specifics; the
one dated fact ("it has — 2026-07") describes a provider-public product change.
Model names and billing-state *shapes* in the child template (see EB4) are
provider-public product facts, the same class as the pre-existing
"usage-billed: real money" line they replace — noted there as a design
observation, not a leak.

## Findings

### EB1 — minor — the stale-claim sweep missed both READMEs

**Claim:** the delta retired the "know which pool" self-check and the
"plan model builds, usage-billed model reviews" split, and its commit message
claims the renamed-section cross-references were updated — but both doctrine
indexes still teach the retired frame. `README.md:68–70` and
`docs/method/README.md:51–54` describe ECONOMICS as "match the model to the job
(plan model builds, usage-billed model reviews), the which-pool self-check". The
section name no longer exists, and the parenthetical states as doctrine exactly
what the delta demoted ("risk assigns the seats" — the capable model is not
usage-billed-by-default any more).
**Evidence:** `README.md:68–70`; `docs/method/README.md:51–54`; contrast
`docs/method/ECONOMICS.md:25–33` and `:82`.
**Counsel:** one-line fixes in both indexes ("billing states of the marginal
token… the marginal-cost self-check"). The class-level lesson is that the
same-commit sweep (00-APEX adaptation bullet; PRINCIPLES §6) needs a
terminology grep, not memory — the delta's author swept the pointers it
remembered (REVIEW, CONCURRENCY) and missed the ones it didn't. Decision is
Mike's.

### EB2 — minor — the two-pool frame survives inside the reworked file itself

**Claim:** two remnants of the retired frame sit in `ECONOMICS.md` at HEAD and
no longer read true. (a) `:116` — "A **third spend pool** sits beside the two
model pools above" — the doc above now defines three billing states, not two
model pools; "third" and "the two model pools" dangle. (b) `:213–217` —
"'Cheapest' is judged inside the pool split that opens this doc, because the
two meters differ… Pick the pool first, then the tier within it" — the doc no
longer opens with a pool split, there are now three meters-worth of states, and
"pick the pool first" is not executable in the new frame (the session doesn't
pick a billing state; it reads one off the plan).
**Evidence:** `docs/method/ECONOMICS.md:116–118, 213–217` vs `:10–18`.
**Counsel:** rewrite (a) as CI-compute-beside-the-model-spend without the
count, and (b) against the three states ("judged against the marginal token's
billing state and draw-down rate…"). Same sweep class as EB1, but inside the
delta's own primary file — worth fixing in the same application pass.

### EB3 — minor — "distance from its cap" assumes an observable the doctrine elsewhere says is invisible

**Claim:** the standing rule now requires a session to "state in one line the
running model, its billing state, and — for a capped model — the distance from
its cap" (`ECONOMICS.md:90–92`). The same section's second guard is grounded in
that meter being *invisible*: "past the cap the next token is real money **with
no visible switch**… nothing breaks, it just silently bills" (`:99–101`). No
surface for reading cap distance is named, and no fallback is stated for when
none exists — so the mandated line may be unfillable exactly where the guard
matters, and an honest session doesn't know whether "distance unknown" trips
the guard or discharges it. A rule that can't be followed from where it binds
degrades into guessing or silent omission (the rule-grammar lesson).
**Evidence:** `docs/method/ECONOMICS.md:90–101`; contrast the CI analogue,
where the meter (the forge's minutes page) exists even though failure is open.
**Counsel:** one clause closes it, e.g. "where no surface reports cap distance,
*unknown* trips the guard — flag and confirm before heavy spend, or consult the
plan's usage surface first." Fail toward confirmation, never toward silence.
Decision is Mike's.

### EB4 — minor — the child template re-instantiates the hard-coding the delta diagnoses

**Claim:** the failure the delta corrects was partly that the template
hard-coded a billing mapping ("Fable (usage-billed: real money)") which went
stale when the plan moved. The fix hard-codes the *new* mapping — "Fable
(plan-included, premium draw, capped share)", "Sonnet / Haiku (plan-included,
cheapest draw)" — into the same propagation surface, directly against the
parent's own new rule ("read the state off the current plan, never off habit",
`ECONOMICS.md:10–12`) and its foot-note ("those are plan details and change
with pricing; this doctrine does not", `:390–394`). Next provider move, every
scaffolded child carries confidently wrong billing facts again — the template
teaches the habit the parent forbids.
**Evidence:** `docs/build/templates/docs/ECONOMICS.md:7–18`; the delta's own
before/after at `dadde1d` (template hunk); `docs/method/ECONOMICS.md:10–12,
390–394`; `docs/build/REPO-STANDARD.md:121–123` ("the repo file carries only
what's repo-local, or points up entirely" — billing state is plan-local, not
repo-local).
**Counsel:** keep the *roles* (workhorse builds; capable tier orchestrates,
reviews, solves hard problems; cheapest tier fans out) and state the
read-the-state rule with a pointer to the person-local plan facts, rather than
naming current billing states inline. If the worked-example value of naming the
current mapping is judged worth the staleness risk, say so in the template
("as at 2026-07 — read the current plan") so the staleness is at least dated.
Privacy note, for completeness: the model names and state shapes are
provider-public product facts — this is a coherence finding, not a leak.
Decision is Mike's.

### EB5 — LOW — the template's Fable bullet yokes "orchestrator" to review-shaped scoping advice

**Claim:** the bullet now opens "the orchestrator, reviewer and hard-problem
solver" and then advises "so keep it **scoped**: hand it a diff/file list; ask
for *findings*, not rewrites" — advice that fits the reviewer role only. An
orchestrated queue run is a long-running seat that cannot be handed a scoped
diff; a child-repo reader following the bullet literally would conclude
orchestration should be scoped-and-short, which contradicts the parent's
orchestrated-run split.
**Evidence:** `docs/build/templates/docs/ECONOMICS.md:9–15`; contrast
`docs/method/ECONOMICS.md:248–263`.
**Counsel:** split the sentence — scoping advice attaches to reviews/hard
problems; orchestration points at the parent's tier split.

### EB6 — LOW — two seats defined by the same formula

**Claim:** the workhorse tier is defined as "the cheapest model that genuinely
does the work" (`ECONOMICS.md:252–254`, QR8), and the new third-seat paragraph
places fan-out "**below** the workhorse" on "the cheapest tier that genuinely
does them" (`:276–279`). The same test names two different seats; the text
relies on the reader supplying that "the work" differs per seat (item builds vs
mechanical reads). As written, "below the cheapest that genuinely does the
work" reads as a contradiction on first pass.
**Evidence:** `docs/method/ECONOMICS.md:252–254, 276–279`.
**Counsel:** qualify the seat definitions by work class once — e.g. workhorse =
"cheapest that genuinely does *the items' builds*" — so "below" has something
to be below.

### EB7 — LOW — a renamed pointer that resolves but misdirects

**Claim:** `CONCURRENCY.md:541–544` says estate plan facts are what
"`ECONOMICS.md` deliberately does not hold (§ Know the marginal cost of the
running model)". The renamed section exists (linkscan-true), but the
deliberately-not-held claim actually lives in ECONOMICS' head-note and
person-local foot-note, not in that section — the self-check section says
nothing about withholding plan facts. Pre-existing misdirection preserved by
the rename, not introduced by it.
**Evidence:** `docs/method/CONCURRENCY.md:541–545`;
`docs/method/ECONOMICS.md:3–6, 82–112, 388–394`.
**Counsel:** point at the doc's person-local boundary (head/foot) rather than
the self-check section.

### EB8 — nit — AUTONOMY's spend example is now the edge case, not the modal one

**Claim:** `AUTONOMY.md:96–97` illustrates the spend floor with "e.g. a billed
model review — see ECONOMICS". Under the new frame the modal review is
plan-included until a cap is crossed; the example still parses (a past-cap
review *is* billed) but no longer names the representative case the delta
itself establishes — cap-crossing.
**Evidence:** `docs/method/AUTONOMY.md:96–97`; `docs/method/ECONOMICS.md:103–108`.
**Counsel:** "e.g. crossing a capped model's cap into usage billing" as the
example, next time AUTONOMY is edited; not worth its own commit.

## What held under attack (stated so the pass is auditable, not a stamp)

- **The frame itself** (lens 1): billing-state-of-the-marginal-token is the
  right correction — the state genuinely is a property of the next token under
  the current plan, not of the model, and the delta's own trigger (the same
  model changing state in 2026-07) is the existence proof. The
  risk-assigns/billing-prices split cleanly repairs the framing debt of billing
  facts carrying the tier rationale.
- **The cap rule's floor hook**: "spend beyond the plan" in `AUTONOMY.md:96` is
  exactly what cap-crossing is; the cross-reference resolves and reads true.
- **Coherence with siblings**: `REVIEW.md:19` ("most capable available model
  reviews…") and `:397`, `CONCURRENCY.md:457–463` (role check as the
  marginal-cost self-check at run-open) all read true against the reworked
  section; the fails-open analogy to CI overage matches the CI section's own
  behaviour split; the hand-up ladder ending at the principal is consistent
  with 00-APEX "Who it binds" (escalates — logs and hands up) and sharpens it
  without contradiction.
- **Claims audit**: the ROADMAP item for the executor trial exists
  (`docs/ROADMAP.md:158`), the CHANGELOG entry matches the delta's content,
  and the intent record carries a review line (reviewscan-verified) naming
  this cold pass's queue pointer.

## Reconciliation with the deferred intent record (opened only after the findings above were durably written)

*(Written after EB1–EB8 were committed to this file; the partial early exposure
via one grep is owned in the brief's deviations note.)*

The record structures itself as **three quoted principal rulings** (rulings 1–2
verbatim quotes; ruling 3 a recorded adoption) plus **five numbered decisions**
— the decisions are themselves the session's wording around the rulings, so
the fidelity check below runs quote → decision → doctrine text.

- **Ruling 1 (quoted: cheaper models welcome "in all situations, not just when
  the tank is empty", but "we never decay the quality or integrity of the work
  because the tank is low, we either stop/delay the work or I choose to pay
  usage fees"):** faithfully encoded — the "capacity never picks the tier"
  edge (`ECONOMICS.md:232–238`) carries both halves (cheaper-is-welcome-
  everywhere *and* never-as-a-cap-response), and the stop-or-pay cap rule
  (`:103–112`) quotes the ruling's operative sentence verbatim; I verified the
  quote in the doctrine matches the record's character-for-character.
- **Ruling 2 (quoted: fail "noisily, not silently so another model can take up
  the work. Or all models failing/incapable coming to me"):** faithfully
  encoded at `:239–246` and the template's closing bullet — the
  workhorse → capable → principal ladder is exactly the quote's two clauses in
  order. The closing sentence ("a report the apex's honesty burden requires,
  not a failure it punishes") is author wording beyond the quote, but it
  encodes 00-APEX honesty rather than new policy — acceptable.
- **Ruling 3 (adopted: third seat — fan-out on the cheapest genuinely-capable
  tier; per-run stepped-down-executor trial):** encoded at `:276–286` with the
  extraction-from-practice guard (trial per run, keep on the floor's
  evidence); the ROADMAP trial item (`docs/ROADMAP.md:158`) closes the loop.
- **The decisions layer:** the three-states frame, draw-down rate, and
  risk-assigns/billing-prices are the record's Decisions 1–2 — correctly
  presented there as the session's corrective shape, not as quoted rulings —
  and the doctrine text matches them. One correction to this reviewer's
  pre-reconcile assumption: "read off the current plan, never off habit" is in
  the record's Decision 1, not invented at the doctrine layer — which makes
  EB4 sharper, since the record's own Consequences then endorse re-hardcoding
  the current mapping into the template ("so children inherit the corrected
  floor") while its Context diagnoses the old hard-coding as part of the debt.
  EB4's counsel therefore targets a *recorded* consequence, not a drafting
  slip; the decision remains Mike's, now flagged as a tension on the record
  itself.
- **EB3 cross-check:** neither the rulings nor the decisions mention stating
  distance-from-cap — that mandate is doctrine-layer author wording, which
  strengthens the case for naming its fallback (fidelity is not at issue;
  enforceability is).
- **The record's hygiene:** carries a `review:` line pointing at this queue
  item (reviewscan-verified), dates the rulings, and explicitly holds the
  estate numbers out ("the plan's name, the cap share, prices… this record
  deliberately carries none of them") — verified true of its text, consistent
  with the lens-4 discharge above. "Weekly allowance" (Context) is a
  provider-public plan shape, same class as the template's state names.

No finding is withdrawn or added by the reconciliation; counts stand at
0M/4m/3L/1n. Per REVIEW.md rules 3–4: every finding above is counsel; the
decisions are the principal's.

*Reviewer: cold rule-4 pass, Fable, 2026-07-23 (verdict finalised ~0234 UTC).*
