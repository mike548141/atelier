# The review-line artefact — templated field + a lint scoped to decision records

**Status**: draft • **Date**: 2026-07-21
**Review**: queued — the ⏳ pointer in `docs/ROADMAP.md` (rule-4 cold pass on
this delta; the taker writes the brief)

## Context

`REVIEW.md`'s remedy for the invisible-decline failure mode requires every
durable design record to carry a `review:` line — but no template carried the
field, so the templates manufactured the blank the rule calls a bug
(2026-07-19 cold-pass F6 qualified the doctrine's "enforcement is structural"
claim accordingly). The `2026-07-18-0820` record deferred "a cheap
design-record lint" to this delta's reviewer, who answered **yes** (F6's
decision: "can ride that item").

## Decision

Three parts, landing together:

1. **The templates carry the field.** The ADR template and decisions README
   spec a **Review** line (queued pointer, or `not warranted — <grounds>`);
   the ROADMAP template states the convention for direction-setting entries.
2. **`tools/reviewscan.py`** reds a decision record that omits the line —
   wired into the pre-commit hook, atelier's CI, and the child `floor.yml`.
   Scope is deliberately narrow: files under `docs/decisions/` named on the
   coordination-free scheme, **presence only** (the judgement's honesty stays
   the reviewer's and the principal's work, not a validator's).
3. **The boundary is the artefact's landing date (2026-07-21).** Records
   frozen before it are append-only (`RECORD.md`) and blameless — the lint
   binds from the day the templates began prompting. Same shape as
   `floor.yml`'s signing adoption boundary: the mechanism's own landing date,
   never a number picked to pass.

## Rejected

- **Linting roadmap headings too:** fires on prose and gets trained away —
  the 0820 record's grounds, honoured; there the convention stays a written
  rule and `REVIEW.md` says so per surface.
- **Retrofitting the field into frozen records:** accepted records are
  append-only; a retro-edit rewrites the deliberation record to satisfy a
  rule that post-dates it.
- **Templates without the lint:** the exact "read ≠ complied" class F6 named —
  a fourth written copy wearing a template's costume.

## Consequences

- A new decision record without a stated review judgement fails the commit
  hook and CI — the omission is now an act a machine catches, not a blank a
  reader skims past.
- Children inherit field + lint at their next pin bump (template copies) and
  immediately via `floor.yml`'s float-to-main scanner checkout.
- Honest residual: roadmap-section compliance still rests on convention;
  if that proves insufficient in practice, a scoped per-repo lint is the next
  rung (0820's own escalation path).
