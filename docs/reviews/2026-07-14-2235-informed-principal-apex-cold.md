# Cold pass — the "informed principal" apex rule

**Work under review:** a new `00-APEX.md` section, *The principal's authority is
conditioned on being informed* (commit `dce5078`), plus its pointers at three
decision sites (`REVIEW.md` rule 3, `RECORD.md` ADR acceptance, `PROPAGATION.md`
floor bullet — the last re-stamped into `build/templates/CLAUDE.md`).

The **principle** is Mike's decision (2026-07-14) and is **not** under review:
that a principal decision or overrule requires the principal to be informed
first, in plain language, is settled. What is under review is the **wording** —
scope, absoluteness, placement, and whether it collides with anything already in
the doctrine.

**Independence posture (REVIEW.md):** the reviewer is a fresh agent that did not
author this text. This is **self-authored doctrine** (agent wording, Mike's
decision) → **rule 3 binds**: every finding is Mike's to decide. The reviewer
records a verdict and applies nothing; it may give per-finding counsel, labelled
as counsel.

## Lenses (run all three)

1. **Approach & assumptions** — is the apex the right home; is "the positive face
   of honesty" a sound framing or a rhetorical stretch; is conditioning
   *authority* on being-informed the right construction (vs a duty on the agent
   that leaves the authority intact)?
2. **Correctness & quality** — does the text say what it means; any overclaim;
   any edge it silently swallows; is the child-stamp re-stamp faithful?
3. **Completeness / harvest** — decision sites it should point at and doesn't
   (AUTONOMY grant-widening? COMMUNICATION?); existing doctrine it duplicates or
   contradicts.

## Method reminders

- Name your **own** load-bearing assumptions first (lens 1) and **commit them to
  this file below a `---` divider before** opening the deferred section or any
  prior verdict. The deferred author questions are a floor, never a fence.
- **Re-run every live-proven claim in scope**: the floor suite (247 tests incl.
  `test_templates` template-sync), `sizescan --check`, `linkscan`. A recorded
  green is a claim like any other.
- Verdict verbatim to this file below the divider; stable finding IDs.

<!-- ===================================================================== -->
<!-- DEFERRED — author's seeded questions. Open ONLY after your own attack -->
<!-- surface is written to this file. A floor for your attention, not a    -->
<!-- fence around it. -->
<!-- ===================================================================== -->

## Deferred — author's seeded questions (open after committing your own)

The author (this session) flagged three wording calls; Mike chose to keep the
current wording and let the reviewer test them:

1. **"An approval given on trust alone is not a decision the doctrine
   recognises."** Is this too absolute — could it be read to retroactively void
   routine confirmations, or to paralyse a principal who *chooses* to decide
   quickly on a low-stakes call? Or is the teeth exactly the point?
2. **Floor-block weight.** The rule added ~4 lines to the compressed
   child-stamped block every repo carries (`PROPAGATION.md` fenced block →
   `templates/CLAUDE.md`). Justified in the always-inlined floor, or should the
   child stamp point up and keep the full text apex-only?
3. **Seam with AUTONOMY's "just proceed."** The rule is scoped to the
   stop-and-confirm floor, not recoverable work the standing grant lets the
   agent do freely. Is that seam actually clean in the text, or does "before the
   agent asks the principal to rule" bleed into work that needs no ruling?

---

## Reviewer's attack surface (committed before reconciling the seeded questions)

**Honesty note on independence (apex).** Strict pre-commitment isolation was
*not* fully held here, and I name it rather than deny it: (a) my single Read of
this brief returned the whole file, so the deferred seeded-question block was in
view before this divider was written; (b) the commissioning task embedded the
same three questions in my instructions. So my context was seeded at input. The
mitigation is the one the house practice uses (the §2 pass's "read-at-selection
exposure named, not denied"): the attack surface below is formed from my own
reading of `00-APEX.md` and its five sibling docs, and it ranges deliberately
wider than the three seeded questions — that breadth, not a claim of blind
isolation, is what carries the independence.

**Load-bearing assumptions I intend to attack (lens 1):**

- **AS1 — Apex placement is right.** The rule belongs at level 0, above the
  precedence ladder, as an untradeable absolute (not a strong operating
  principle that could live in AUTONOMY/COMMUNICATION).
- **AS2 — The enumerated decision set is the real scope.** "hands certain
  decisions to the principal and to no one else — [list]" fixes the rule's
  reach; the list is closed and correct.
- **AS3 — "not a decision the doctrine recognises" has the right teeth.**
  Conditioning the *authority* (voiding the approval) is the right construction
  vs. a duty on the agent that leaves an uninformed decision standing.
- **AS4 — The remedy is determinate.** When the principal waives the briefing
  ("just do it"), the text tells the agent what to do, and it does not collide
  with Second Law obedience.
- **AS5 — The "positive face of honesty" framing is sound**, not a rhetorical
  stretch that smuggles a new *disclosure/comprehensibility* duty in under the
  non-falsehood banner.
- **AS6 — The floor-block/template restatement is narrowing-free** and maps the
  apex rule onto the *same* decision set the apex names.
- **AS7 — The trigger sentence covers its own list.** "before the agent asks
  the principal to rule" reaches every member of the enumerated set, including
  "any overrule of the agent's judgement" (which the principal, not the agent,
  initiates).
- **AS8 — Pointer coverage is complete.** The sites that needed a reciprocal
  pointer got one; none that the apex names was left un-stamped.
- **AS9 — The meta-sections still describe the apex correctly** after a third
  member was inserted between honesty and the Laws ("Why this is level 0" /
  "Who it binds" / the canonicality note).
- **AS10 — No live-proven claim in the commit is stale** (247 tests incl.
  `test_templates` sync, sizescan, linkscan, leakscan).

**Attack surface (where I will push hardest):** the apex list vs. the floor
list (AS2/AS6 — two different decision sets wearing one sentence); the
waive-the-briefing remedy vs. Second Law (AS4); the overrule-initiation seam
(AS7); the missing AUTONOMY back-pointer and AUTONOMY's pre-existing
"say what / why / irreversible" duty (AS8); and whether the two-member framing
of "Why this is level 0" now under-describes a three-member apex (AS9).

---

## Verdict — PASS-WITH-FINDINGS (0 MAJOR · 4 MEDIUM · 3 LOW)

Self-authored doctrine (agent wording, Mike's settled principle) → **REVIEW.md
rule 3 binds: every finding below is Mike's to decide.** This section records
counsel only; nothing is applied, and no source file
(`00-APEX.md`/`REVIEW.md`/`RECORD.md`/`PROPAGATION.md`/template) is edited by
the reviewer. Per the close rule (REVIEW.md): a pass with **no MAJOR** means the
cycle can close on Mike's decisions into the backlog — the application does not
spawn a second full ceremony.

**Independence caveat (named, not denied):** context was seeded at input (whole-
file Read exposed the deferred block; the commissioning task embedded the three
questions). Mitigation is breadth: the attack surface above was formed from the
doctrine itself and ranges past the three seeded questions to five structural
seams. The seeded questions are answered below as a *floor*, after — not as — my
own findings.

### Live-proven claims re-run (lens 2 on the record) — all reproduce
- **247 tests OK** (`python3 -m unittest discover -s tools -p 'test_*.py'`),
  incl. `test_templates` template-sync.
- **sizescan `--check` clean** — template `CLAUDE.md` at 95 lines, within budget.
- **linkscan clean · leakscan clean.**
- **Re-stamp verified character-identical:** the `PROPAGATION.md` fenced block
  (lines 97–102) and the `build/templates/CLAUDE.md` stamped block (lines 30–33)
  match verbatim; `test_templates` passing confirms it mechanically. ✅ No stale
  proof — a clean lens-2 reconciliation.

### Per-lens notes
- **Lens 1 (approach & assumptions).** Apex placement is **sound**: the rule is
  a genuine face of honesty *as this file defines honesty* (which already counts
  hedged omission and a suppressed caveat as violations), so a
  disclosure+comprehensibility duty sits inside the same absolute. Conditioning
  *authority* (voiding the approval) rather than merely imposing an agent duty is
  a deliberate, defensible construction — but its **teeth are aimed at the wrong
  actor** in the wording (F2). The load-bearing weakness is not the principle; it
  is that two *different* decision sets wear the one sentence (F1).
- **Lens 2 (correctness & quality).** Text is honest and non-overclaiming;
  proofs reproduce. Two internal-consistency defects: the operative trigger does
  not cover its own enumerated list (F3), and the meta-section still describes a
  two-member apex (F5).
- **Lens 3 (completeness / harvest).** Pointer coverage is **asymmetric**:
  `AUTONOMY.md` is named as a decision site but got no reciprocal pointer, and
  its pre-existing "surface it plainly … what / why / irreversible" duty
  (lines 104–107) is the same duty left un-reconciled (F4). `COMMUNICATION.md`
  already owns the "plain over jargon" + "decision apart from the reasoning"
  craft (lines 106–108) — the new rule's "recommendation is informing, not
  steering" overlaps it uncited (folded into F4 counsel).

### Findings

**F1 · MEDIUM · one sentence, two non-coextensive decision sets.**
The apex scopes the rule to a **closed governance list** — "hands certain
decisions to the principal and to no one else — [self-authored-doctrine finding,
ADR acceptance, parent/child conflict, grant-widening, any overrule]." The
`PROPAGATION.md`/template floor attaches the *identical* teeth ("an approval
given without that account is not a decision the doctrine recognises") to the
**operational always-confirm floor** — making-public, destructive, secrets,
spend, safety, lockout, unapproved-tool/trust-surface. Those two sets overlap
only at *grant-widening*. So the child stamp applies the apex rule to
confirmations the apex's own enumerated list never mentions — a child asserting
*more* than its parent, which is exactly what PROPAGATION's "narrowing-free
restatement / never silently contradict" guards against.
*Counsel (Mike's to decide):* make the apex list explicitly open and unify it —
e.g. "every decision the doctrine reserves to the principal, **whether a
governance ruling or an always-confirm floor stop**" — so the one sentence
provably covers both sets and the template stops out-scoping the apex.

**F2 · MEDIUM · lead finding · the teeth point at the principal's state, not the
agent's discharge; remedy unstated; Second-Law seam.** (Answers seeded q1.)
The duty is on the *agent* ("it owes him — unprompted"), discharged by
*providing* the what/why/impact. But "an approval given **on trust alone** is
not a decision the doctrine recognises" keys the void on the *principal's* state
of mind — whether he absorbed the account — which the agent cannot control. Two
cases the wording conflates: (a) agent failed to inform → decision rightly void;
(b) agent fully informed, unprompted and plain, and the principal said "yes,
don't need it, go" → still literally "on trust alone," so still void — even
though the agent discharged its duty. Case (b) puts the agent in a Second-Law
bind (obey the go-ahead vs. "the doctrine doesn't recognise this decision") with
no stated remedy, and risks the agent *policing the principal's diligence*.
*Counsel:* pin the trigger to the **agent's** act — the decision is void when the
agent *extracted* approval by **withholding** the account, not when the principal
*chose to act on less*. Preserve the principal's right to waive the briefing once
it has been offered; the agent's obligation is to *provide*, never to *refuse*.
One clause fixes it. (This is the seeded-clean-question trigger REVIEW.md warns
is the strongest — it is where I pushed hardest, and it earns the lead.)

**F3 · MEDIUM · the operative trigger doesn't cover its own list.**
"So *before the agent asks the principal to rule*, it owes him…" governs
**agent-initiated** asks. But the enumerated set includes "**any overrule of the
agent's judgement**" — which the *principal* initiates; the agent never "asks to
be overruled." So the one member most about the principal acting *against* the
agent falls outside the sentence that is supposed to trigger the duty.
*Counsel:* broaden the trigger to run both directions — "before the agent asks
the principal to rule, **or acts on the principal's overrule**" — so the informing
duty (surface what the overrule trades away) attaches to the overrule case too.

**F4 · MEDIUM · asymmetric pointer coverage; AUTONOMY's twin duty un-reconciled.**
Reciprocal pointers were stamped at REVIEW, RECORD, PROPAGATION — but **not at
`AUTONOMY.md`**, though grant-widening `(AUTONOMY.md)` is named in the apex list.
AUTONOMY already carries the same duty in prose (lines 104–107: "surface it
plainly (the apex): say what the action is, why, and what's irreversible about
it") and its floor section is where grant-widening actually lives. Result: the
one site that *pre-existingly states this duty* is the one left without the
cross-link, and the near-duplicate wording ("what/why/irreversible" vs.
"what/why/impact") sits un-harmonised. `COMMUNICATION.md` (106–108) similarly
owns the plain-language + separate-the-decision craft uncited.
*Counsel:* stamp AUTONOMY too (fold the pointer into its existing lines 104–107,
which then *become* the reciprocal reference rather than a rival statement), and
add a one-clause `COMMUNICATION.md` cross-link for the "how to inform" craft —
or state explicitly why AUTONOMY is exempt. Pick one; don't leave it asymmetric.

**F5 · LOW · meta-section describes a two-member apex.**
"Why this is level 0" still reads "**honesty and the Laws** are never traded off
… They bound the whole ladder," and "Who it binds" speaks of the apex
generically — neither names the new third top-level `##`. Since the rule is
pitched as a *face of honesty*, it rides under that absolute — but structurally
it is a peer heading, so the two-member framing now under-describes the file.
*Counsel:* add a half-clause to "Why this is level 0" naming the informed-
principal rule as part of the honesty face, **or** demote the new section to a
subsection under "Honesty is absolute" so the two-member framing stays true.

**F6 · LOW · "positive face of honesty" slightly oversells continuity.**
Honesty-as-non-falsehood forbids the *false* claim; the new rule additionally
compels a *true, comprehensible, unprompted disclosure*. That is an **extension**
(a duty of candour + comprehensibility), not merely honesty's positive image.
The framing survives because this file defines honesty broadly, but "positive
face" reads as pure restatement when it is partly addition.
*Counsel:* optional — "the positive face **and reach** of the honesty absolute"
or similar, only if Mike wants the extension named. Cosmetic.

**F7 · LOW · the memorable sentence now lives in four homes (lockstep cost).**
"not a decision the doctrine recognises" appears near-verbatim in `00-APEX.md`,
`REVIEW.md`, `PROPAGATION.md`, and the template (RECORD paraphrases). The
template copy is sanctioned inlining (the fail-safe floor); the REVIEW/RECORD
copies are pointer+gloss house style and load-bearing at their sites, so this is
**acceptable, not a violation** — but per RECORD's lockstep rule, a future
reword of the apex sentence must move all four together.
*Counsel:* none required; noted so the lockstep is on the record.

### Seeded questions (floor — answered after my own findings)
1. **Too absolute / voids routine confirmations?** Partly — but not where the
   author framed the risk. It does **not** retroactively void routine
   confirmations *in the apex* (scoped to the enumerated decision set). The real
   defect is upstream of "too absolute": the teeth key on the *principal's*
   absorption rather than the *agent's* discharge, creating the waive-case /
   Second-Law seam (**F2**), and the template widens the blast radius onto the
   whole operational floor (**F1**). Keep the teeth; fix what they bite.
2. **Floor-block weight?** **Justified.** Template is 95 lines, sizescan clean;
   +4 lines on an always-inlined floor that binds even if atelier is never read
   is proportionate — an informed-confirmation rule is exactly the safety-floor
   class that must survive without the fat pointer. The only issue is *scope*
   (F1), not *weight*. Keep it inlined; do not push it up to apex-only.
3. **AUTONOMY "just proceed" seam?** **Clean.** In both the apex and the template
   the rule is scoped to the stop-and-confirm set; "Everything recoverable …
   just proceed" immediately follows and is unaffected — it does **not** bleed
   into recoverable work. The seam that *isn't* clean runs the other way: the
   trigger under-covers the principal-initiated **overrule** (F3), and the
   AUTONOMY back-pointer is missing (F4).

**Disposition: PASS-WITH-FINDINGS.** The principle is sound and the wording is
honest and proof-backed; no MAJOR. The four MEDIUMs are all one- or two-clause
wording fixes at the seams (scope-unification, agent-vs-principal teeth,
overrule trigger, pointer symmetry). All are Mike's to decide (rule 3); once
decided, the fixes consolidate onto one ROADMAP follow-ups item and the cycle
closes without a further full ceremony.
