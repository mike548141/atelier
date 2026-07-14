# Cold review — MODEL-ECONOMICS triple delta (sub-agents · tier selection · context reset)

**Scope:** the working-tree delta to `docs/method/MODEL-ECONOMICS.md` (one
commit, 2026-07-15): (1) the one-paragraph "Subagents for fan-out" expanded to
a section *Sub-agents — isolation, not savings*; (2) a tier-selection paragraph
appended to *One doctrine, tiered authority*; (3) session-hygiene item 4
rewritten as *reset by record, not by compaction*. Review the edited doc at
HEAD, whole, plus the delta.

**Independence note:** this brief is author-written (the same session authored
the delta), so the independence rules bind in full (`REVIEW.md`): name your own
attack surface and commit it to your draft **before** opening the deferred
section below the divider; treat this brief's framing — including its account
of what the work is — as attackable; read no prior verdicts until your own
findings are committed. This is doctrine, self-authored: **all findings are the
principal's to decide** (rule 3) — the author may append labelled counsel only.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict below a second `---` divider in
this file.

---

## Deferred — author's seeded questions (open only after your attack surface is committed)

- S1. The sub-agent section claims delegation "often spends *more* total
  tokens than inline" — is that honest across both pools, or does it overclaim
  for the plan-included case where parallel sub-agents mostly cost wall-clock
  allowance, not marginal dollars?
- S2. "The report is all that survives" — does the doc anywhere conflict with
  this (e.g. the inline-review pattern assumes the verdict file, not the
  transcript, carries the detail)? Is the fresh-context-verification bullet
  consistent with `REVIEW.md`'s independence rules, or does it invite
  author-framed spawn prompts without naming that bind?
- S3. Tier selection: does "cheapest model that genuinely does the work"
  collide with the existing pool split (plan-included builds vs usage-billed
  reviews), which selects by *pool*, not by *capability*? Are the two rules
  composable as written, and is the precedence between them stated or left to
  collide?
- S4. Hygiene item 4: is "the record is this method's compaction" a real
  equivalence or rhetoric — a session record is written for the *next* session,
  a compaction serves the *current* one mid-task; does the text honestly cover
  the mid-task case?
- S5. Naming drift: the doc now uses "sub-agent(s)" where the old text said
  "subagents" — check consistency doc-wide and against sibling docs.

---

## Verdict — cold pass 2026-07-15

### Attack surface (reviewer's own, committed before the deferred section was opened)

**Lens 1 — approach & assumptions**

- A1. Is "isolation, not savings" the right correction, and is the stated flip
  axis (early-in-short vs deep-in-long session) the true lever? Candidate
  counter-model: the payback is (tokens kept out of context) × (turns *remaining*
  ahead) plus deferred quality decay — remaining work, not depth accrued.
- A2. Does "a sub-agent is mechanically a cold reviewer (independence, different
  blind spots, fresh context)" survive REVIEW.md's own rule that fresh context is
  necessary but *not sufficient* — the spawn prompt is an author-warm brief
  (REACH: framing leaks through the ask)? Does the pointer to REVIEW.md carry
  enough of that caveat, or does this doc alone mint false cold reviews?
- A3. The tier-selection paragraph assumes one price meter ("the cheapest model
  that genuinely does the work"). Does it survive the doc's own opening two-pool
  frame, where a plan-included capable model can cost fewer marginal dollars than
  a usage-billed cheap one?
- A4. Reset-by-record assumes the session record is an adequate substitute for
  compaction. A record captures decisions and state for resumption, not in-flight
  conversational detail — test whether the /compact-as-fallback carve-out
  actually covers the gap.
- A5. Grounding (atelier's stub-don't-fabricate rule): are the new empirical
  claims — sub-agent re-pays fixed overhead, "often spends *more* total tokens",
  "cost is linear the whole way", cache-warmth behaviour — extracted from
  verifiable harness fact / decided practice, or asserted to fill the heading?
  PRINCIPLES §6: a claim carries its provenance and its test.
- A6. The brief's account of the work ("three deltas") is itself attackable —
  verify the diff is exactly that and nothing else rides the commit.

**Lens 2 — correctness & honesty**

- C1. Re-run the mechanics claims against current harness/API fact, not memory:
  (a) sub-agent fixed overhead (own system prompt + tool schemas) — true;
  (b) "the cache stays warm" — tension with hygiene item 3: a long-running
  sub-agent idles the main session past the cache TTL, so delegation can *cool*
  the main cache; the real benefit is a lean, stable prefix, not warmth;
  (c) "the cost is linear the whole way" — check against stepped long-context
  pricing tiers and harness cliffs (auto-compact trigger, hard context limit);
  (d) cache writes dearer than reads — consistency with item 3.
- C2. Rework-pricing rule: "a cheap attempt that fails and is redone on the
  capable model costs more than starting capable" — expected-cost framing (a
  likely-enough success still makes the cheap attempt rational), and
  pool-dependence (a failed cheap attempt on plan quota burns no dollars).
- C3. Internal consistency at HEAD: new item 4 vs item 1's break-reasons and the
  closing "bulk off the hot path" paragraph; sub-agent section vs "know which
  pool"; tier paragraph vs REVIEW.md's capable-model-reviews rule and the
  "match the ceremony to the risk" section.
- C4. Relative time in doctrine: "(In today's harness …)" vs RECORD.md's
  absolute-dating rule — will that aside rot silently?

**Lens 3 — completeness / harvest**

- H1. The commit lands both a sub-agent section and a tier-selection rule and
  never composes them: fan-out delegated to a *cheaper tier* changes the "often
  costs more total" headline (more tokens ≠ more cost when the tier is cheaper).
- H2. Sub-agent spend and the pool self-check: delegated tokens bill to the same
  meter — does "know which pool" cover spawned agents, and should it?
- H3. Wall-clock parallelism is a real economic benefit of parallel slices the
  section names but doesn't credit — deliberate scope-out or a miss?
- H4. What the rewrites dropped: the old one-liner's usage-billed emphasis
  (retained), item 4's "a standing practice, not a failure" reassurance
  (dropped) — anything load-bearing lost?
- H5. Do the sibling docs need reciprocal updates (REVIEW.md's inline-review
  bullet, RECORD.md's pointer to session hygiene) — and were they left
  consistent?

### Reconciliation with the deferred seeded questions

Opened only after the attack surface above was committed. S1 and S3 sharpen my
A3/C2/H2 (pool-blindness — folded into F3); S2 matches my A2 (→ F1); S4
matches my A4 and reconciles clean — "the record is this method's compaction"
is an analogy, not an equivalence claim, and the text honestly delegates the
mid-task case to the in-place-compaction fallback, so no finding; S5 (naming
drift) was not on my surface and produced F6. The seeded set missed the flip-axis
error (F2), the cache-warmth tension (F5), and the tier×sub-agent composition
(F4).

### Live claims re-run (lens 2 applied to the text's factual assertions)

Checked against the current API reference, not memory: cache reads ~0.1× /
writes 1.25× (5-minute default TTL) — item 3's write>read and few-minutes-TTL
claims hold. Current-generation models carry the 1M window at standard pricing
with **no long-context premium**, so "the cost is linear the whole way" holds
on today's meters (I attacked it expecting a stepped premium; the attack
failed — recorded because a clean re-run is evidence too). Output at ~5× input
supports the opening pools paragraph. Sub-agent fixed overhead (own system
prompt + tool schemas, report-only return) is true of the current harness, which
also supports a per-sub-agent model override (bears on F4). Commit scope matches
the brief's account (MODEL-ECONOMICS delta + ROADMAP pointer + this brief;
nothing else rides it).

### Findings

Self-authored doctrine — all findings are the principal's to decide (REVIEW
rule 3); recommendations only, nothing applied.

**F1 — MEDIUM — sub-agent ≡ cold reviewer overclaims independence.**
*What:* "a sub-agent is mechanically a cold reviewer (independence, different
blind spots, fresh context — `REVIEW.md`)" (§Sub-agents). *Why:* REVIEW.md's own
core rule is that fresh context is necessary but **not sufficient** — the spawn
prompt is an author-warm brief, and "different blind spots" is precisely the
property the REACH case showed an author-framed spawn does *not* deliver.
REVIEW.md's parallel inline-review bullet says "the independence rules bind it
in full"; this doc's version carries no such signal, and its own *Triggering
reviews* section (which the bullet equates itself with) doesn't either.
*Likely impact:* a reader of MODEL-ECONOMICS alone mints a "cold review" from a
warm spawn prompt — the exact failure the independence rules exist to prevent.
*Recommend:* one clause — the spawn prompt is a brief and the independence
rules (deferred seeded questions, own attack surface first) bind; point at
REVIEW.md's inline-review bullet.

**F2 — MEDIUM — the economics-flip axis is mis-specified.**
*What:* "the economics flip with session length — early in a short session,
delegation is pure overhead; deep in a long session … it is the cheapest read
available." *Why:* the token arithmetic turns on the work **remaining ahead** —
every subsequent turn re-carries whatever entered the main context — not on
depth already accrued. Depth matters only via quality decay, which the text
already credits separately. The two quoted corners are the cases where both
variables happen to agree; presented as an axis of "session length" they
mis-steer the off-diagonal cases. *Likely impact:* a reader early in a long
session (delegation's *highest*-payback point — the savings compound over the
most remaining turns) is steered away from delegating; a reader near the end of
a long session is steered toward it as its payback window closes.
*Recommend:* restate the lever as remaining work: delegation pays in proportion
to how much session lies *ahead* to re-carry the reading, plus the decay it
defers — not how deep you already are.

**F3 — MEDIUM — tier selection and the sub-agent cost claim are pool-blind.**
*What:* "the cheapest model that genuinely does the work" reads as a single
price ladder, and "often spends *more* total tokens" reads as "costs more".
*Why:* the doc's own opening frame has two meters. Under it, "cheapest" can
invert — a plan-included capable model costs no marginal dollars while a
usage-billed smaller model costs real money — and more total tokens on the plan
pool is allowance draw-down, not dollars (seeded S1/S3 aim here too; the
pool-split rule selects by *pool*, tier selection selects by *capability*, and
the precedence between them is unstated). *Likely impact:* an adopter
optimising "cheapest model" against the API price list makes the exact mistake
the pools section exists to prevent; the sub-agent section's headline cost
claim overstates for plan-included sessions. *Recommend:* one sentence
anchoring tier selection inside the pool split ("cheapest within the pool the
risk frame already selected"), and qualify the sub-agent total-cost claim per
pool.

**F4 — LOW — sub-agents × tier selection never composed.**
*What:* the same commit lands both new rules but never connects them: a
sub-agent can run a *cheaper tier* than the main session (the current harness
supports a per-sub-agent model override). *Why:* cheap-tier fan-out is the
natural composition — mechanical reading is exactly the "pattern-following work
runs on a cheaper model" case, and it materially softens "often costs more
total". *Likely impact:* adopters pay capable-model rates for mechanical
fan-out the doctrine already licenses running cheap. *Recommend:* a clause in
the when-to-reach list: fan-out sub-agents are also where the tier-selection
rule bites — delegate mechanical reading to the cheapest tier that genuinely
does it.

**F5 — LOW — "the cache stays warm" can be exactly backwards.**
*What:* the isolation bullet credits delegation with "the cache stays warm".
*Why:* item 3 of this same doc: the prompt cache expires after a few minutes
(verified: 5-minute default TTL; writes ~1.25×, reads ~0.1×). A sub-agent that
runs longer than the TTL leaves the main session idle past expiry — the next
main turn re-*writes* the cache at the premium rate. The durable benefit is a
lean, *stable* prefix, not warmth. *Likely impact:* minor mis-claim inside an
otherwise-correct bullet; a long-running delegation is charged as churn while
the doc promises the opposite. *Recommend:* say "the prefix stays lean and
stable" and note the TTL interaction for long-running sub-agents.

**F6 — LOW — stale sibling template + naming drift (seeded S5).**
*What:* `docs/build/templates/docs/MODEL-ECONOMICS.md` still carries the
pre-delta one-liner ("**Subagents** (Explore, etc.) — fan-out reading/searching
so the main context stays lean") and the old unhyphenated spelling; within
`docs/method/` the new "sub-agent(s)" is now used consistently. *Why:* the
template is what child repos scaffold from; it doesn't contradict the new
doctrine (the lean-context clause was the correct half of the old text) but it
teaches none of the delta's corrections (isolation-not-savings, lossiness,
when-not), and the naming now drifts from the parent. *Likely impact:* new
children inherit the superseded framing until someone notices. *Recommend:*
sweep the template's sub-agent bullet to a one-line pointer at the parent
section (thin anchor, fat pointer — PROPAGATION), matching the new spelling.

### Verdict

**PASS-WITH-FINDINGS** — 0 MAJOR · 3 MEDIUM (F1–F3) · 3 LOW (F4–F6).

The delta is honest and well-grounded overall: its central corrections
(isolation-not-savings, verifiability-gated tier choice, record-first reset)
survive attack, and every factual pricing/caching claim I re-ran against the
current reference held — including one I expected to fail ("cost is linear the
whole way"). The MEDIUMs are a mis-specified lever (F2), a pool-blindness the
doc's own opening frame exposes (F3), and an independence signal the sibling
doctrine carries but this text drops (F1). Cold pass complete
2026-07-15; decisions are Mike's.

---

## Author's counsel (labelled per REVIEW rule 3 — the decision is the principal's)

The author accepts all six findings as correct; none is contested. Per
finding: **F1 accept** — add the one-clause independence bind (the spawn prompt
is a brief; deferred seeded questions, own attack surface first) with a pointer
at REVIEW.md's inline-review bullet. **F2 accept** — the reviewer's arithmetic
is right: restate the flip axis as work *remaining ahead* plus the decay it
defers, not depth accrued. **F3 accept** — anchor tier selection inside the
pool split ("cheapest within the pool the risk frame already selected") and
qualify the sub-agent total-cost claim per pool. **F4 accept** — one clause
composing cheap-tier fan-out with the tier rule. **F5 accept** — "the prefix
stays lean and stable", noting the TTL interaction for long-running
sub-agents. **F6 accept** — sweep the child template's sub-agent bullet to a
thin pointer at the parent section, matching spelling. All six are
severity-proportionate one-clause/one-sweep edits; with 0 MAJOR the close rule
applies — once ruled, the application spawns no further full ceremony.

---

## Decision (Mike, 2026-07-15) — cycle CLOSED

- **F1 [fixed]** — Mike ruled for independence, accepting the counsel up to
  and including a ban: "reviews must remain independent, if that means no warm
  spawns for reviews then that is fine. If that is what your counselling then
  I agree." Applied as counselled — **the bind, not the ban**: the sub-agent
  section now states that fresh context alone is not independence and that the
  independence rules bind in full on author-spawned reviews, pointing at
  REVIEW.md. A ban on warm spawns would change REVIEW.md's sanctioned
  inline-review pattern and remains open to the principal if the bind proves
  insufficient — the distinction was flagged to Mike at application.
- **F2 [fixed]** — flip axis restated as work *remaining ahead* plus the decay
  delegation defers; depth-accrued framing removed.
- **F3 [fixed]** — sub-agent total-cost claim qualified per pool (allowance vs
  dollars); tier selection anchored inside the pool split ("pick the pool
  first, then the tier within it").
- **F4 [fixed]** — cheap-tier fan-out composed into the when-to-reach list.
- **F5 [fixed]** — "cache stays warm" replaced by the lean, stable prefix,
  with the TTL caveat for long-running sub-agents.
- **F6 [fixed]** — child template's bullet swept to a thin pointer at the
  parent section, spelling aligned.
- **Also applied, principal-supplied at the same ruling:** price the *job*,
  not the token — a dearer model that completes the work in fewer turns,
  retries and re-reviews is often the cheaper way to get it done — woven into
  the tier paragraph beside the rework rule it generalises.

0 MAJOR at the cold pass ⇒ this ruled application ends the cycle without a
further ceremony (REVIEW.md, the close rule).

**F1 disposition REOPENED (Mike, 2026-07-15, later the same day).** The
"agree if that's what you're counselling" ruling did not reflect Mike's
intention — he has asked for a proper plain-language walk-through of what the
author was recommending before ruling. The applied text (the bind) stays in
place while that conversation runs, since it restates REVIEW.md's existing
position rather than adding new policy; F1's *ruling*, not its text, is what
is open. F2–F6 and the price-the-job nuance are unaffected.
