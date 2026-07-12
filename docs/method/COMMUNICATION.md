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
- **Visual structure** — iconography, tables, headings, and call-out devices
  (blockquotes, dedicated sections); the specifics matter more than the
  category (the live instance prefers *colour* icons — ✅ ❌ ⚠️ — over
  monochrome glyphs, because colour carries the signal faster; confirmed
  2026-07-12). Two refinements from the same instance (2026-07-12): don't
  ration the icon vocabulary to a fixed set — reach for the one that *fits*
  the moment (🎉 a real win, 🎯 a decision that's the reader's to make, 🚩 a
  caution) — under the guardrail that an *apt* icon is signal and an
  *overused* one is noise. And surface the parts the reader must **act on** —
  a decision, an action, a caution — in a device that draws the eye and sits
  *apart* from the reasoning, so the ask never hides inside the evidence.
- **Accessibility of the language** — a term the reader hasn't signalled they
  share, or a wall of unbroken prose, costs a reread exactly as a missing
  colour-glyph does. Define or drop the jargon; prefer plain words; let
  structure break the wall. (Live instance, 2026-07-12: replies had run
  text-heavy and term-laden — same reader, same cost as the visual axis.)
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
  Enforcement, stated honestly (`PROPAGATION.md`'s clause): write-time
  discipline is the *only* control — the instance sits outside the reach of
  every mechanical floor and every review sweep, because the house's own
  reviews are barred from the person-level layer by design.
- **Person-local, pointed at, never copied.** A repo's CLAUDE.md may carry
  *repo* conventions (locale for its artefacts, commit style); the personal
  layer never travels into a repo — not even a private one, because repos
  change hands and visibility (the no-personal-data boundary, and RECORD's
  scrub-of-HEAD-is-not-remediation). This is deliberately stricter than the
  portability north star's lighter tier, which tolerates a private store for
  instance-level facts: a calibration travels *with* its motivators, so it
  gets crown-jewel handling whole. The scrubbed snapshot below is the one
  sanctioned exception — ADR 0005's named-worked-example framing, replaced
  wholesale by an adopter.

## Worked example (scrubbed)

The live instance's calibration with the personal context removed — a
snapshot taken 2026-07-12 (the instance moves; this illustrates the shape,
it does not track the original). Replace wholesale with your own:

> - **Outcome first, evidence beneath it** — lead with the answer/verdict,
>   then the supporting detail; the answer gives the detail its context.
> - **Visual reader** — colour iconography (✅ done · ❌ failed · ⚠️
>   partial/deferred, and the wider palette when it fits — 🎉 🎯 🚩), tables
>   for anything multi-dimensional, headings to scan by; surface actions and
>   decisions in an eye-catching call-out, apart from the reasoning. Use
>   layout to carry structure and cut length.
> - **Plain over jargon** — define or drop terms the reader hasn't signalled
>   they share; don't run text-heavy.
> - **Dense and concise** — "as short as possible, but no shorter"; watch
>   volume, and let structure *replace* length, never pad it.
> - **Reduce cognitive load** — provide solutions, drafts, or summaries, not
>   option surveys; don't state the obvious.
> - **Tone** — intelligent, witty, hyper-competent; keep the wit light-touch.
> - **Locale** — NZ English spelling; macrons on te reo Māori; NZD and metric
>   by default.

What was scrubbed: the personal context (health, workload, household) that
motivates several of these lines. It stays in the person-level layer — the
boundary this repo exists to hold. The calibration *functions* without it —
every line above is executable as printed; the understanding that turns
rules into judgement stays person-local, which is why the instance, not
this snapshot, is what the agent actually serves.

*Bearing: the live instance is the "Working with me" section of the
principal's `~/.claude/CLAUDE.md`, maintained since before atelier existed and
still accumulating dated confirmations.*
