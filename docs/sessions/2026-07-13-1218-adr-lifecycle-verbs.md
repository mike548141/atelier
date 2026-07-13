# 2026-07-13 · 12:18 — the ADR lifecycle encoded (Fable)

Same conversation, next gap: the morning's work had twice leaned on "the 0007
precedent — never edit an accepted ADR's substance, append to it", and Mike
ruled the precedent should be a rule: a design decision is immutable once
made, but it can be revoked (end-dated so it no longer applies), given
addenda, or superseded.

## The gap

Half-encoded. `RECORD.md` and the decisions READMEs carried immutability and
the supersession verb; the **addendum** verb ran on precedent alone (ADR 0007,
2026-07-12; the record-identifiers ADR twice today) and **revocation** —
ending a decision without replacing it — didn't exist in the vocabulary at
all.

## Codified (`d9924f0`)

- **`method/RECORD.md`** (the home) — an ADR is immutable once decided;
  everything after acceptance happens by *appending*, in one of three verbs:
  **Addendum** (a dated section when the same decision matures — grounded in
  the two live uses), **Revoked** (`revoked <date>` on the status line + a
  dated addendum saying why and from when; the file stays in the record — a
  revoked decision still explains the era it governed), **Superseded**
  (`superseded by <file>`, the new ADR points back). Never an edit.
- **decisions READMEs (repo + template, together)** — status vocabulary
  extended to `accepted / revoked <date> / superseded by <file>`; the
  never-edit line expanded into the three-verb mechanics, pointing up to
  RECORD for the full lifecycle.

## Addendum (same conversation, ~12:22) — the draft state

Mike anchored the lifecycle to the IEEE/IETF standards shape (draft → active →
superseded or withdrawn), which exposed the state the three verbs skipped:
**draft**. Encoded: draft is the one *mutable* state — deliberation written
down, binding on nothing yet; acceptance is the principal's decision, never
the author's, and is what freezes the substance. This gives the recurring
"await Mike's decision" pattern a first-class home: the agent can author the
deliberation as a draft ADR and the ruling flips it to accepted. Status
vocabulary is now draft / accepted / revoked `<date>` / superseded by
`<file>`; RECORD.md names the standards-body anchor; both READMEs and both
template copies updated together.

## Owed

- Children pick it up at their next pin bump alongside the identifier scheme.
- Same cold-review sweep covers it with the rest of the day's doctrine.
