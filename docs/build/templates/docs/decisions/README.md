# Decision records

Short ADRs preserving the *deliberation* behind significant decisions —
the alternatives weighed, why they lost, and the evidence — which
`ARCHITECTURE.md` (current truth, compact) deliberately compresses away.

Write one when a decision (a) rejected a plausible alternative a future
session might re-propose, or (b) rests on evidence that took real work to
gather. Don't write one for reversible implementation choices — a code
comment covers those (the "comments say why" rule).

Format: one file, `<YYYY-MM-DD>-<HHMM>-<slug>.md` (start time, 24-hour —
coordination-free, per atelier's `method/CONCURRENCY.md` record-identifier
rule; files named under retired schemes keep their names), about half a page.
Sections: **Status** (accepted / revoked `<date>` / superseded by `<file>`),
**Date**, **Context**, **Decision**, **Rejected** (each alternative + why it
lost), **Consequences**. An accepted ADR's substance is immutable — everything
after acceptance is appended, never edited: a dated **Addendum** section when
the decision matures, `revoked <date>` + addendum when it stops applying with
no replacement, `superseded by <file>` when a new ADR replaces it (the full
lifecycle is atelier's `method/RECORD.md`).

## Index

<!-- One line per ADR — replace with live entries. The example below is a
single-line code span so its placeholder link isn't scanned as a real one:
`[2026-01-15](2026-01-15-0930-slug.md) — one-line summary of the decision` -->
