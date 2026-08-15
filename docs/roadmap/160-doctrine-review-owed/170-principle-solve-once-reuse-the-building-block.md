- [ ] **Principle: solve once, reuse the building block (Mike, 2026-07-25)** —
  solve a problem once, then compose from the blocks you already have; never
  re-solve a solved problem. Holds at two scopes:
  - **In-repo:** one implementation of a capability, many consumers — e.g. tiki
    writes the wire-protocol handling *once*, and every use case calls that
    module rather than re-deriving it. (Standard composability; atelier already
    holds its anti-duplication twin, *one fact, one home* — EVIDENCE §9 / V4.)
  - **Cross-repo:** the "building block" is also **intelligence and case-law**,
    not just code. A problem solved in one repo's domain becomes a reusable block
    for the others via three flows — **up** (child → atelier, e.g. first-
    principles elevating; the up-flow captured above), **down** (atelier →
    children, PROPAGATION), and **lateral** (child → child directly).
  **The unifying claim:** code primitives and knowledge primitives obey the
  **same solve-once law** — factor the reusable thing, then consume it, whether
  it is a function or a doctrine. This reframes what atelier *is*: the fleet's
  **shared library for knowledge** — what tiki's wire-protocol module is *within*
  tiki, atelier is for doctrine/case-law *across* the fleet. Already-held on the
  in-repo side (composability + one-fact-one-home); the new part is the
  cross-scope generalisation + the atelier-as-knowledge-library framing. Clusters
  with the two captures above; likely lands in `PRINCIPLES.md` (with a
  `PROPAGATION.md` cross-link for the flow topology). Review WARRANTED if/when it
  moves to doctrine.
