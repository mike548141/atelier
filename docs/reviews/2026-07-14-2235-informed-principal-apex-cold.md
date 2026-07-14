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
