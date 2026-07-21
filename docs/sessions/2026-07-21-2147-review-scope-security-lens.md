# 2026-07-21 · 2147 UTC · reviewer scope + security & privacy lens (Fable, main)

**Delta:** `f9db922` — `docs/method/REVIEW.md`, `docs/method/README.md`,
`docs/build/templates/docs/reviews/README.md`.

## The ask

Mike asked two questions of the review doctrine:

1. Does atelier tell reviewers to use the **widest possible scope** — not just
   design but the decisions and assumptions that went into it, the intent or
   idea that drives it, documentation, test code, real-world testing, and the
   code itself?
2. Is it clear that **security and privacy is a must for every review** — from
   privacy issues born of design weakness to SQL-injection/XSS classes in
   code, with likely threat vectors checked against open sources like OWASP?

## What the audit found

- **Scope: mostly there in structure, not stated as a mandate.** The three
  lenses plus the commitment-not-artefact trigger covered intent, assumptions,
  design and code — but the scope was *enumerated*, never declared unbounded.
  Test code was never named as reviewable; documentation-of-the-work only fell
  implicitly under lenses 2–3; and enumeration invites exactly the "no source
  code, so not my problem" shrinkage the doc itself records twice (2026-07-15,
  2026-07-18).
- **Security & privacy: absent.** Zero occurrences of security, privacy,
  threat, OWASP, or injection in `REVIEW.md`, the review brief conventions, or
  the child template. The only defences were the secret/leak scanners (a
  mechanical floor for one narrow class) and an optional harness skill nothing
  tells anyone to run — the invisibility failure mode `REVIEW.md` itself
  names.

## The ruling

Mike: **"go"**, with one caveat — real-world testing binds *"where it's
possible to do so"*. Both deltas accepted as counselled:

1. A scope-mandate paragraph above the lenses: scope is the whole commitment
   (intent, decisions, assumptions, design, docs, code, tests, real-world
   behaviour — exercised live where possible, re-run from claims where not);
   the brief's non-goals are the only legitimate narrowing; the lenses
   organise the scope, they do not bound it.
2. **Security & privacy as lens 4** (numbering preserved so existing
   lens-1/2/3 references stay valid): a must on every review, running at
   design altitude (exposure, over-collection, privacy-by-design-weakness)
   and code altitude (injection, XSS, authn/authz, secret handling); *likely*
   vectors checked against open catalogues (OWASP Top 10 / ASVS), not
   recalled; a genuinely surface-free work discharges the lens in one
   explicit line with grounds — omission is the bug.

Child floor (`templates/docs/reviews/README.md`) carries the same sentence,
narrowing-free; the fleet adopts at next pin bump.

## Review status

Self-authored doctrine (rule 4): this session authored the delta and therefore
neither spawns nor briefs its review. `⏳` pointer queued in the ROADMAP,
refs only. One framing note for the taker to weigh, recorded here where the
deferral discipline governs when it is read: the delta was drafted in the same
session that ran the gap audit above, so the audit's framing (what was
"missing") and the fix share an author — the cold pass should re-derive
whether the gaps were real and whether lens 4's shape (per-lens vs per-brief,
the discharge line, the OWASP expectation) is the right mechanism, not take
this record's account of them.
