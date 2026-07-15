# Conventions — the default frame, and what fills it

Many values can't be read without a frame they don't carry: a time needs a zone,
a price needs a currency, a measurement needs a unit, a date needs a format, text
needs an encoding. Ship the value without the frame and every reader supplies
their own — usually their local one — and a silent mismatch follows. That's the
CI clock reading a local timestamp as UTC and rejecting every signed commit; it's
a price sticker with no currency; it's the mother of a whole family of bugs. This
doc names the anti-pattern once and declares the estate's defaults, so the next
unlabelled-value case has a rule to point at instead of a fresh argument.

## The rule

1. **Declare a default frame, once, at the boundary.** Every value carrying a
   frame is read against a default. Declare that default at the layer or edge
   where the values live — a schema field, a column header, one line of a doc —
   and it carries *silently* from there. No per-value label. This is the
   readability half: a default stated once costs one line; a default tattooed on
   every value is noise that costs a reread each time.

2. **Label a deviation, or a collision.** State the frame *on the value* when it
   departs from the declared default, or when several frames coexist with no
   single default to assume. The lone watch on your wrist needs no zone; a wall
   of clocks each shows a different one, so each is labelled. As a rule of thumb
   this is ~99% "declare once, stay silent" — but it is risk- and context-based,
   not absolute: where a mislabel is costly enough, labelling every value is the
   deliberate exception. The failure mode cuts both ways — a silent deviation is
   a latent bug; over-labelling is noise. Pick for the reader.

3. **Precedence when principles collide.** "Preserve data we don't own" outranks
   "normalise to the default." Data from an external party is kept as received —
   integrity and verifiability first, and no transform cost spent rewriting data
   we didn't author — and its frame is recorded as *metadata
   alongside*, never rewritten into the payload. The kept data then re-enters
   rule 2 as a labelled deviation, and that metadata is its label. ELT, not ETL.

*Worked examples — the same rule, three shapes:* a **shop sticker** carries no
currency because every party shares the local default (rule 1, silent); crossing
a **border** you must find out the local currency, because you've stepped outside
the shared default (the default was never global); a **wall of clocks** labels
each, because frames collide with no default to assume (rule 2).

The dangerous case is none of these — it's a value *silently deviating from a
default that was assumed but never actually shared*. A stated, shared default is
a perfectly safe assumption; the rule's whole job is to keep every default in the
stated-and-shared column and never let a deviation go silent.

## The declared defaults

Unless a value says otherwise, these are the frames in force across the estate's
repos and the work going forward:

| Frame | Default | Notes |
|---|---|---|
| **Time** | UTC at rest; local + labelled on presentation | Record identifiers UTC-forward. Full deliberation + the foreign-data precedence: [ADR 2026-07-15](../decisions/2026-07-15-1327-timestamps-utc-at-rest.md). |
| **Currency** | NZD | A bare `$` is NZD. Another currency is labelled (rule 2). |
| **Date & time format** | ISO 8601 | `YYYY-MM-DD`, 24-hour, `Z` for UTC. Self-describing — kills DD/MM vs MM/DD ambiguity. |
| **Text encoding** | UTF-8 | Macrons on te reo Māori depend on it; a tool that mangles `Māori` is a silent frame break. |
| **Language / dialect** | New Zealand English, with te reo Māori | NZ spelling (organise, licence); macrons (tohutō) correct. |

*(These are this estate's worked defaults. A peer adopter substitutes their own —
their currency, their locale — the doctrine is **declare a default and label
deviations**, not these specific values. Same roles-not-instances split as
STORAGE.)*

## What lives elsewhere, and maintenance

- **Time's full case** — UTC-at-rest, identifiers-forward, the foreign-data
  precedence — is the ADR linked above; this table is its one-line home.
- **SIGNING's `Z`-anchoring** is the same at-rest rule applied to signing
  timestamps — the instance that drew blood before the rule was general.
- **NZ English + macrons** also appear in the session onramp (`CLAUDE.md`); this
  doc is canonical, the onramp is a pointer.
- Maintain like a record: when a default changes, date the change here — a
  default is only safe while it's the *current* stated one.
