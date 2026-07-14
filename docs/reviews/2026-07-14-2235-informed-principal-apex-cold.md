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
