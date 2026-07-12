# Communication — calibrate replies to the person reading them

The agent's default reply style is tuned for an average reader, and nobody is
the average reader. A reply the principal has to reread — or ask a follow-up
to decode — has spent whatever time it saved by being fast. The fix is a
**communication calibration**: a maintained "working with me" section in the
principal's person-level context, so every reply lands the first time, across
every project, without the principal re-explaining themselves per session.

This is the cheapest leverage in the whole operating model: one small,
maintained document improves the consumption cost of *every* reply the agent
will ever write to that person.

## Two things, kept separate

The same split as `TOOLBOX.md`, applied to communication:

- **The practice (shareable — this doc).** *Keep a calibration. Cover the axes
  below. Maintain it from observed evidence. Keep it person-local and point to
  it — never copy it into a repo.*
- **The instance (personal — NOT in this repo).** The actual calibration — and
  especially the personal context that gives it force (why the person carries
  the load they do, what they must not be nagged about) — is personal context
  by definition. It lives in the principal's person-level layer (today
  `~/.claude/CLAUDE.md`), never in a shareable repo. A scrubbed worked example
  is included below under the named-worked-example framing (ADR 0005); an
  adopter replaces it wholesale with their own.

(History, honestly: this doc was first *declined* — 2026-07-12, on the ground
that reply style is personal context. The same day the split above resolved
it: the values are personal; the **pattern** is what a peer adopting atelier
needs.)

## The axes a calibration covers

Grounded in the live instance, not invented to fill a heading:

- **Ordering** — outcome first, evidence beneath it? Or build-up to a
  conclusion? Pick one; say it.
- **Density and volume** — how terse is too terse; whether structure should
  *replace* length or supplement it. A long reply reads as heavy even when
  every line is tight.
- **Visual structure** — iconography, tables, headings; and the specifics
  matter more than the category (the live instance prefers *colour* icons —
  ✅ ❌ ⚠️ — over monochrome glyphs, because colour carries the signal
  faster).
- **Cognitive-load stance** — solutions, drafts, and summaries versus option
  surveys; whether stating the obvious helps or grates.
- **Tone** — register, humour, and *how much*. Dosage is part of the
  preference, not an implementation detail.
- **Locale and language** — spelling variant, units, currency, and correct
  treatment of other languages in scope (for this house: NZ English, macrons
  on te reo Māori).
- **What personal context is for** — factoring in when genuinely relevant,
  never lecturing. The calibration may reference sensitive context that lives
  beside it in the person-level layer; this axis says how the agent may *use*
  it.

## The meta-rules that make it work

- **Defaults to serve, not rules to recite.** The purpose is for the agent to
  *understand the person*, not to comply mechanically. The grounding case: a
  previous assistant applied a "witty" preference at full dose everywhere, and
  it grated — the preference was real, the recitation was the defect.
- **Maintain it like a record.** When a reply lands notably well or badly,
  that is calibration data — write it back, dated (`EVIDENCE.md` absolute
  dating), so confirmations accumulate instead of evaporating at session end.
- **Person-local, pointed at, never copied.** A repo's CLAUDE.md may carry
  *repo* conventions (locale for its artefacts, commit style); the personal
  layer never travels into a repo — not even a private one, because repos
  change hands and visibility (the no-personal-data boundary, and RECORD's
  scrub-of-HEAD-is-not-remediation).

## Worked example (scrubbed)

The live instance's calibration with the personal context removed — replace
wholesale with your own:

> - **Outcome first, evidence beneath it** — lead with the answer/verdict,
>   then the supporting detail; the answer gives the detail its context.
> - **Visual reader** — colour iconography (✅ done · ❌ failed · ⚠️
>   partial/deferred), tables for anything multi-dimensional, headings to scan
>   by. Use layout to carry structure and cut length.
> - **Dense and concise** — "as short as possible, but no shorter"; watch
>   volume, and let structure *replace* length, never pad it.
> - **Reduce cognitive load** — provide solutions, drafts, or summaries, not
>   option surveys; don't state the obvious.
> - **Tone** — intelligent, witty, hyper-competent; keep the wit light-touch.
> - **Locale** — NZ English spelling; macrons on te reo Māori; NZD and metric
>   by default.

What was scrubbed: the personal context (health, workload, household) that
motivates several of these lines. It stays in the person-level layer — the
boundary this repo exists to hold — and the calibration works without the
reader knowing it.

*Bearing: the live instance is the "Working with me" section of the
principal's `~/.claude/CLAUDE.md`, maintained since before atelier existed and
still accumulating dated confirmations.*
