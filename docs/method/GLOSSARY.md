# Glossary — the doctrine's shared language

The load-bearing words the doctrine uses with precise, non-interchangeable
meanings, so readers (human **and** AI) take the intent exactly, not by
inference. This is a *thin anchor*: a term already defined canonically
elsewhere gets a **pointer line here, never a duplicate** — one fact, one home
(`EVIDENCE.md`) — and only terms with no single canonical home are defined in
full in this file.

> **⚠️ STATUS — SEED, 2026-07-23 (Fable session; wording PROPOSED).** Created
> when the truth/honesty/transparency triad made it plain the doctrine now
> assigns everyday words exact meanings. Follows the fleet's worked precedent
> (tiki's glossary, 2026-07-20) including its **admission rule**: a term earns
> an entry when it carries intent across two or more docs; the entry defines
> once and everything else points. 🎯 **The principal's end-to-end ratify pass
> is owed** — until then entries are recommendations, not doctrine. A living
> file; adding terms is expected.

## Roles

- **Principal** — the human the agent serves and answers to: the holder of
  every reserved decision (governance rulings, floor stops) and the grantor of
  all authority the agent exercises. Duties owed to the principal:
  [`00-APEX.md`](00-APEX.md) § The principal's authority; the grant itself:
  [`AUTONOMY.md`](AUTONOMY.md).
- **Agent** — the AI actor working under this doctrine, whatever model powers
  it. One doctrine binds every model; capability scopes *authority*, never
  *applicability* ([`00-APEX.md`](00-APEX.md) § Who it binds).
- **Session** — one continuous working context of an agent, from onramp to
  close; the unit that claims work, holds a worktree, and owes a closing
  record ([`CONCURRENCY.md`](CONCURRENCY.md), [`RECORD.md`](RECORD.md)).

## Truth and its machinery

- **Truth · honesty · transparency** — three distinct duties, defined
  canonically in [`00-APEX.md`](00-APEX.md) § Truth, honesty, transparency:
  what actually occurred (provable irrespective of observer) · the best and
  faithful interpretation of it · the inclusion of all relevant information.
- **Evidence vs testimony** — a claim whose proof can be re-run, challenged,
  and contrasted, versus one resting on its author's word
  ([`00-APEX.md`](00-APEX.md) § Adaptation is continuous;
  machinery in [`EVIDENCE.md`](EVIDENCE.md)).
- **Provenance** — a claim's answer to "what is the source, how obtained, when
  verified, how far trusted" ([`EVIDENCE.md`](EVIDENCE.md) §1).
- **Authority tier** — the graded strength of a source (primary,
  official-guidance, …); a claim inherits the weakest tier it materially rests
  on ([`EVIDENCE.md`](EVIDENCE.md) §2).

## Structure of the doctrine

- **Doctrine** — the whole operating model this repo carries: the apex, the
  method docs, the build standard, and the decisions that bind them. "How we
  work", held as code.
- **Apex** — level 0: honesty, adaptation, the Laws — above the precedence
  ladder, never traded ([`00-APEX.md`](00-APEX.md)).
- **Floor** — the irreducible subset of the doctrine a child repo carries
  *inlined*, so it binds even if the parent is never read
  ([`PROPAGATION.md`](PROPAGATION.md)).
- **Bearing** — a child's estate-specific application of a parent principle,
  held in the child and pointing up; children point up, the parent never
  points down for truth ([`PROPAGATION.md`](PROPAGATION.md),
  [`00-APEX.md`](00-APEX.md) canonicality note).
- **Thin anchor / fat pointer** — the two-part propagation mechanism: the
  inlined floor plus the SHA-pinned, drift-checked reference to the parent
  ([`PROPAGATION.md`](PROPAGATION.md)).

## Process

- **Harvest** — closing a piece of work by extracting what it taught into the
  records that outlive it; integrity rules in [`RECORD.md`](RECORD.md).
- **ADR** — architecture decision record: the durable capture of a
  re-litigable decision ([`RECORD.md`](RECORD.md); instances in
  `docs/decisions/`).
- **Cold review** — independent review by a party with fresh context, met
  through a refs-only brief rather than the author's framing
  ([`REVIEW.md`](REVIEW.md)).
- **Intent record** — the session record a queued review pointer names: the
  account of what was built and why, including the authoring choices a
  reviewer should attack ([`REVIEW.md`](REVIEW.md) rule 4).
- **Delta** — the exact commits a review covers, named in the queue pointer
  ([`REVIEW.md`](REVIEW.md) rule 4, `ROADMAP.md` header).
- **Worked case** — a real, dated episode encoded into doctrine as grounding —
  never invented to fill a heading (the grounding rule,
  [`00-APEX.md`](00-APEX.md) § Adaptation is continuous).
