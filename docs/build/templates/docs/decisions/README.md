# Decision records

Short ADRs preserving the *deliberation* behind significant decisions —
the alternatives weighed, why they lost, and the evidence — which
`ARCHITECTURE.md` (current truth, compact) deliberately compresses away.

Write one when a decision (a) rejected a plausible alternative a future
session might re-propose, or (b) rests on evidence that took real work to
gather. Don't write one for reversible implementation choices — a code
comment covers those (the "comments say why" rule).

Format: one file, numbered `NNNN-slug.md`, about half a page. Sections:
**Status** (accepted / superseded-by-NNNN), **Date**, **Context**,
**Decision**, **Rejected** (each alternative + why it lost),
**Consequences**. Never edit an accepted ADR's substance — supersede it
with a new one.

## Index

<!-- One line per ADR, e.g.:
- [0001](0001-slug.md) — one-line summary of the decision
-->
