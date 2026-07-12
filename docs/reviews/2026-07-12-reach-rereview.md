# Re-review: `docs/method/REACH.md` — independent adversarial pass

**Date:** 2026-07-12 · **Reviewer:** fresh-context agent, deliberately unbriefed
by the author · **Disposition owner:** Mike (the principal), not the doc's
author.

**Why this review exists.** REACH.md was authored, review-briefed, and
findings-dispositioned by the same agent in one session — a self-certification
loop. This pass is the independent break in that loop: no pre-seeded questions,
no author framing. Attack surface chosen by the reviewer.

## Attack questions (chosen independently)

1. **Floor coherence** — does the credential boundary contradict the
   `AUTONOMY.md` always-confirm floor it claims to sit inside?
2. **Boundary placement** — is "riding a session is fine" actually where the
   decided practice drew the line, or one line lower?
3. **Self-consistency** — does the ladder's own descent rule survive its own
   rungs?
4. **Rot resistance** — does the doc obey its own "what lives elsewhere" rule,
   and is what it says about the instance true *at HEAD*?
5. **Grounding** — which rules are extracted from decided practice
   (browser-fetch, SECRETS/ACCESS machinery) and which are invented to round
   out the prose?
6. **Sibling composition** — how does the reach ladder interact with
   `EVIDENCE.md` §13's acquisition ladder, `ADR 0006`'s third verb, and
   `SECRETS.md`'s scope boundary?
7. **Live proof** — per `REVIEW.md`, re-run the reproducible proof the doctrine
   leans on (the instance's unit suite).

Re-run result: `test_server.py` — 11/11 pass with the instance venv at HEAD.
The worked instance the doctrine cites is real and its reproducible proof
reproduces.

---

## Verdict: **PASS-WITH-FINDINGS**

The spine survives a genuinely hostile pass: the cheapest-first ladder is
extracted from a real, working instance (not invented); ride-not-mint is a
decided rule (browser-fetch README carried it before elevation); the
purpose-of-storage test genuinely generalises `SECRETS.md`'s scope boundary
rather than fabricating a new one; and no personal data or estate topology
leaks. I could not unseat the doc's core.

But two **major** findings sit exactly where a reach/credential doctrine can
least afford them — the credential section read standalone licenses more than
the floor allows (A1) and more than the decided practice decided (A2). Until
those two land, REACH.md should not be cited as the standalone authority on
what an agent may do with credentials and sessions; with them fixed, it stands.

## Findings

### A1 — MAJOR: "no further permission needed" contradicts the AUTONOMY secrets floor

REACH (provisioned-stores bullet): credentials provisioned for agent use are
*"in scope by design, no further permission needed beyond the grant that
provisioned them."*

`AUTONOMY.md` "Always confirm" floor: **"Secrets — reading, writing, moving, or
regenerating credentials/keys"** — and the floor holds *"standing grants
notwithstanding"*, with *"a grant in one context is not a grant for the next"*
stated explicitly. `SECRETS.md`/`ACCESS.md`'s decided model is narrower than
REACH's phrasing too: the *tooling resolves references* to values; the agent
handling credential values directly is precisely what the right-plane rule
avoids.

So either AUTONOMY's floor is overbroad (routine use of a provisioned token
plainly shouldn't re-prompt) or REACH has silently relaxed a floor — and the
house's own layer-override discipline (cited in `REVIEW.md` step 4) says a
doctrine conflict is named and resolved, never straddled. Today a reader of
REACH alone gets "draw on provisioned stores, no permission needed"; a reader
of AUTONOMY alone gets "reading credentials: always confirm". Both are current
doctrine.

**Fix:** reconcile explicitly, in whichever direction Mike decides. Likely
shape: REACH's bullet becomes "in scope *for the use they were provisioned
for, through the resolving machinery* — the provisioning grant is the confirm;
direct reads, exports, or repurposing of stored values stay on the AUTONOMY
floor", and AUTONOMY's secrets bullet gains the matching carve-out so the two
docs state one rule.

### A2 — MAJOR: "riding an open session is fine" is unscoped — the line is drawn one rung too low

The boundary guards only credential *minting*: *"existing cookies, a logged-in
tab are fair game"*, *"riding an open session is fine; touching the credentials
behind it is the line."* Nothing in REACH scopes what the agent may **do**
while riding. At rung 5 the ridden session is the principal's entire
authenticated life — email, purchases, admin panels. The decided practice being
generalised is *fetch-only* (browser-fetch returns rendered text; it acts on
nothing), but the doctrine text, read standalone, gives "fair game" cover to
state-changing acts through the session, gated only by a reader separately
remembering AUTONOMY's spend/people/publish floors. A security-boundary doc
whose one bright line is bright about the wrong thing: minting is not the only
way to abuse a session.

**Fix:** one sentence in the boundary section: riding licenses **retrieval**
(the reach this doc exists for); any state-changing action taken *through* a
ridden session is its own action under the AUTONOMY floor, and a rung-5 ride is
scoped to the exposure the operator deliberately made, not a standing grant.
This is what the instance already does — the doctrine should say so.

### A3 — MEDIUM: instance status inlined against the doc's own "never here" rule — and already false at HEAD

"What lives elsewhere" says the built ladder's status lives in the
browser-fetch README and ROADMAP, *"never here"* — while parenthetically
asserting that status here: *"today the real-engine rungs are one browser;
other engines and an explicit rung-4/5 split are open work"*. Commit `1463a36`
(same day, ~15 minutes after the reviewed text landed) falsified it: rung 3
now runs three engines (Firefox/WebKit live-verified), the rung-4/5 split is
explicit (`rung` parameter, per-rung ports), and the remaining honest gap is
different (rungs 4–5 Chrome-only, by CDP protocol). Doctrine now states false
facts about its own worked instance — the exact rot `EVIDENCE.md` §8/§9
(store the rule, one fact one home) exists to prevent, in the sentence that
claims to prevent it.

**Fix:** delete the status parenthetical; keep only the pointer. The doctrine
sentence should be rot-proof: "which engines fill which rungs, and the honest
gaps, live in the instance README and ROADMAP."

### A4 — MEDIUM: the descent rule is contradicted by the doc's own rung 2

The ladder rule is absolute: *"step down only when the current rung is actually
blocked"*, *"never open at a lower rung because it's more likely to work."*
But rung 2's own charter is **fit, not blockage**: "an API, a file, exact
headers, or when the processing in rung 1 gets in the way" — a POST to an API
cannot open at rung 1 at all, and the doc itself concedes rung 2 "clears no
new walls... a different *shape* of request, not a stronger one". As written,
every legitimate rung-2 opening violates the ladder's only rule, or the rule
means something it doesn't say.

**Fix:** split the rule to match what the doc already believes: rungs 1–2 are
chosen by **request shape** (they cost the same and clear the same walls);
block-gated, cost-paying descent starts at rung 3.

### A5 — MEDIUM: the "one axis" claim is false for half the ladder

*"The rungs climb one axis — isolation traded away for reach"* — but the
instance's own table marks rungs 1–2 isolation "n/a", and rung 3 is *fully
isolated*: a disposable browser is not less isolated than curl. Isolation is
only traded away across rungs 3→5. The tidy single-axis framing is a
load-bearing sentence (the second axis at rung 4 hangs off it) that the
ladder's top half doesn't satisfy.

**Fix:** claim the isolation axis for the engine rungs (3–5) where it's true,
and name the top half honestly (processing/capability, at equal wall-clearing
power).

### A6 — LOW: temporary grants can't be walked as written

The grant clause allows crossing *"per credential, temporary or permanent"* —
then requires every grant to move the credential *"into the provisioned
machinery (SECRETS.md's store, ACCESS.md's runbook)"*. For the **temporary**
grant the clause itself names ("use this once"), enrolling the value in the
encrypted store with a mint/rotate procedure is contradictory: a one-shot
credential shouldn't persist at all. The rule fails on one of the two cases it
explicitly covers.

**Fix:** standing grants enrol in the machinery; temporary grants expire with
the task, and what's *recorded* is the grant (dated, scoped — per EVIDENCE),
never the value.

### A7 — LOW: no composition with EVIDENCE §13's acquisition ladder

The method layer now holds two rung-ladders governing how an agent acquires an
external fact, with **opposite polarity**: EVIDENCE §13 — climb (spend more)
as *stakes* demand, "don't stop at the first rung"; REACH — stay high (spend
less), "never open at a lower rung", descend only on *block*. They are
reconcilable (REACH picks the pipe, EVIDENCE picks the evidential strength)
but neither doc says so, and a reader holding both gets contradictory-sounding
maxims for the same act.

**Fix:** one cross-reference sentence in REACH: the reach ladder chooses the
*access method* for a source; EVIDENCE §13 chooses how *strong* the evidence
must be — and stakes can compel a fetch that reach-economics alone would not.

### A8 — LOW: generality overclaimed from n=1; the ADR's third verb quietly narrowed

*"The rules here are general"* — yet the "general shape" is six rungs mapping
one-to-one onto the single instance's six tools; no second instance has ever
tested the generalisation, and the doc doesn't say so (the house rule is
stub-and-say-so, not round-up). Separately, REACH renders ADR 0006's third verb
as instruments that *"get the teammate through a wall"*; the ADR's decision is
broader — **capability** instruments that "extend what the teammate can *do*".
A future capability instrument with no wall involved would read REACH as
excluding it from the layer the ADR admits it to.

**Fix:** one honesty clause ("generalised from one worked instance;
engine-agnostic by construction, untested beyond it"), and align the third-verb
gloss with the ADR's wording ("extend reach" as one kind of capability).

## Follow-up checklist

- [ ] A1 — reconcile REACH provisioned-store clause with the AUTONOMY secrets floor (both docs)
- [ ] A2 — scope "riding is fine" to retrieval; state-changing acts take their own floor
- [ ] A3 — drop the stale instance-status parenthetical from "What lives elsewhere"
- [ ] A4 — restate descent rule: shape picks 1 vs 2; block gates 3+
- [ ] A5 — restrict the isolation axis to rungs 3–5
- [ ] A6 — temporary grants expire, they don't enrol
- [ ] A7 — cross-reference EVIDENCE §13
- [ ] A8 — honesty clause on generality; realign third-verb gloss with ADR 0006

---

## Comparison with the prior (author-briefed) review

*Written last, per the independence protocol: everything above was drafted
before reading `docs/reviews/2026-07-12-reach.md` or the session-47
ROADMAP/SESSIONS entries.*

**What it settled that I don't contest.** R1–R5 are real findings, correctly
dispositioned; their fixes are all present in the text I reviewed and they
hold (I independently probed the R3 seam — the "never itself the provisioned
path" sentence — and found it coherent before knowing it was a review fix).
The cold reviewer worked competently within its brief: the rung-by-rung
grounding check (Q1), the join argument (Q2), and the no-leak check (Q4)
were done properly and I reproduce their conclusions.

**What it settled that I contest.** Two of its green lights were checked in
only one direction:

- **Q3** asked whether the purpose test *outlaws the estate's intended use*
  — the failure mode *the author* was guarding against — and never asked the
  mirror question: whether "no further permission needed" is *more permissive
  than the AUTONOMY floor allows*. That mirror is my A1, a major.
- **Q5** scoped "family consistency" to SECRETS/ACCESS by name. Inside that
  scope its answer is right; but the family includes AUTONOMY (A1) and
  EVIDENCE (A7), and both contradictions sat outside the fence the brief
  drew.
- The verdict *praised* "riding the operator's live session is explicitly
  'fair game'" as coherence (Q3) without asking what the agent may do while
  riding — my A2, the other major.
- Q1's verdict praised the instance-status parenthetical as "the honesty bar
  met". It was verbatim-true at review time — but the same session's
  coordinating agent then landed `1463a36` (~15 minutes after the fold-in
  commit) and falsified it without touching REACH. The review endorsed the
  mechanism (instance status inlined in doctrine) whose rot my A3 records;
  the doc's own "never here" rule was the right instinct and the review
  blessed the exception to it.

**What I found that it missed.** All eight of my findings; none of R1–R5
overlap them. The pattern is not reviewer incompetence — it is the leash: all
five "sharp questions to attack" were written by the author, and every one
points where the author was already looking (is it grounded? is my join
convincing? does it forbid what I need allowed? did I leak?). Both majors lie
along axes the brief never pointed at: *too permissive against a sibling
floor*, and *conduct while inside the granted thing*. A cold reviewer with
warm questions inherits the author's blind spots at exactly one remove —
which is the self-certification residue this re-review exists to name.

**Does reading it change my verdict?** No. PASS-WITH-FINDINGS stands, with
A1/A2 as the majors that gate citing REACH as the standalone credential
authority. On whether the prior PASS was sound: the *tier* was right — the
doc's core genuinely survives — but the *basis* was not. "Five findings, all
Minor or Low, none blocking" was an artefact of the brief's aim, not of the
text: two major findings were available in the same words it read. For
REVIEW.md itself, the transferable lesson is procedural: when the work is
doctrine, the brief's sharp questions should not all be authored by the
doctrine's author — or at minimum the reviewer must be licensed (as this pass
was) to choose its own attack surface beyond them.
