# 2026-07-21 · 2147 UTC · reviewer scope + security & privacy lens (Fable, main)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 145+1 -->
- [2026-07-21 · 2147 UTC · reviewer scope + security & privacy lens 4 (Fable, main)](2026-07-21-2147-review-scope-security-lens.md) — Mike asked two questions of the review doctrine: does it mandate the widest possible reviewer scope (intent, decisions, assumptions, design, docs, test code, real-world behaviour, code), and is security & privacy clearly a must on every review? Audit: scope ⚠️ structurally close but enumerated-never-mandated (test code and work-docs unnamed — the same enumeration that let "no source code" shrink two past verdicts); security & privacy ❌ absent — zero mentions of security/privacy/threat/OWASP anywhere in review doctrine or templates. Mike: "go", caveating real-world testing *where it's possible to do so*. Delta `f9db922`: scope-mandate paragraph above the lenses (whole commitment; non-goals the only legitimate narrowing; lenses organise, never bound) and **security & privacy as lens 4** (design-altitude privacy weakness through injection/XSS at code altitude; likely vectors checked against OWASP Top 10/ASVS, not recalled; surface-free work discharges in one explicit line with grounds — omission is the bug); child review-floor template carries the same sentence, fleet adopts at pin bump; method/README three→four lenses. Self-authored doctrine ⇒ **⏳ rule-4 pointer queued refs-only** (non-author taker; this session spawns nothing). **Addendum (same session, `a059e49`):** Mike granted `/security-review` — lens 4 now runs the harness's security scanner where one ships, the mechanical floor under the lens, never a discharge of it; ⏳ pointer widened to both deltas.


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

## Addendum — same session: /security-review named in lens 4 (`a059e49`)

Mike asked whether the harness's `/security-review` skill was wrapped into the
delta — it wasn't (lens 4 sanctioned OWASP catalogues but never the tool) —
and granted its use: *"If it is useful I'm happy for you to use it."* Second
delta `a059e49`: lens 4 now instructs the reviewer to run the harness's
security scanner where one exists (Claude Code's `/security-review` over the
in-scope diff is the house instance) and fold its findings in — the mechanical
floor layered under the lens per *What review is not*, never a discharge of
it, its clean pass a claim to weigh like any other. Child template carries the
same clause. The open `⏳` cycle now covers `f9db922` + `a059e49` as one
reviewable delta; the pointer updated refs-only.
