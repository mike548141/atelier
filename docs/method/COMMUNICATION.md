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
  Sentence *shape* sits on the same axis: a sentence interrupted by a long
  bracketed aside forces the reader to hold the suspended sentence open while
  parsing the interruption, and demotes load-bearing content into brackets.
  Finish the sentence clean, then give the aside its own sentence — or hang a
  short clause off the end with a dash. Brackets are for short, droppable
  glosses only; content that matters never lives in them. (Live instance,
  2026-07-15: named as a recurring cross-repo habit and a refinement — the
  structure and consistency around it had landed well.)
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
- **Some of it is enforceable, and the split is not where it looks.** This
  doc said until 2026-08-09 that write-time discipline was the *only* control.
  That was true of the calibration **document** and was read as true of the
  **prose it governs**, which was the error. The document is still beyond
  reach: it lives in the person-level layer, where the house's own reviews are
  barred by design. The prose is not. Anything a machine can decide without
  judgement — a reference code used before anything says what it points at, an
  acronym never expanded, a sentence past a stated length, a bracketed aside
  buried mid-sentence — is checkable, and `plainscan` checks it on the committed
  prose plane through the floor registry.

  🛑 **The reply plane is UNWIRED (Mike, 2026-08-15), and how it failed is the
  more useful half.** A second plane ran from 2026-08-09: a `Stop` hook that
  blocked the agent's own reply and demanded a rewrite. This clause said the
  rewrite happened before the principal read the reply. It never did. A `Stop`
  hook fires *after* Claude Code has streamed the reply to the terminal, so a
  block cannot retract anything — it appends a second full copy of a long
  verdict below the first. Twelve hours of live sessions: 29 turns blocked, 6 of
  them twice, ~123,500 characters reprinted. **A rule that is machine-decidable
  can still have no machine-deliverable remedy**, and that is the lesson to
  carry: before enforcing a rule, establish that the enforcement point can
  actually deliver the fix, not merely detect the fault. Detection was sound
  throughout; the remedy was the part nobody checked. Destroy-or-repurpose is
  Mike's open ruling → ROADMAP § *Policy-as-code programme*.

  **The second rule this earned lives elsewhere, and that is deliberate.** The
  same failure earned *an approval is not the whole ruling* — the principal
  approved the guard **with reservations**, the record kept the approval and
  none of the reservations, and the objections that would have predicted this
  failure were never tested against the build. That rule governs how approvals
  are recorded everywhere, not how prose is written here, so it sits in
  `RECORD.md` § *An approval is not the whole ruling* with its class in
  `GUARDS.md` § *A rule with no home is not a rule* (the principal's ruling,
  2026-08-17). This clause keeps the **instance**, because the instance is the
  evidence; it is not the rule's home. That the rule spent two days stated only
  in a commit message is itself the grounding for the `GUARDS.md` entry.

  **Each plane is scoped to its reader (ruled 2026-08-10).** The reply plane
  covered everything, because every reply is written to the principal — that
  scoping survives the unwiring above and would carry to any collector built in
  its place. The repo plane covers only the prose the principal reads —
  doctrine, ruling asks, review briefs, the live roadmap. Session records
  (`SESSIONS.md`,
  `docs/sessions/`, `ROADMAP-DONE.md`) are excluded by ruling: they are
  append-only history written for the next session's agent, and rewriting
  them would be dishonest — so a warning there has no possible fix and is
  pure noise. Measured at the ruling: records carried 3,377 of atelier's
  7,817 advisory findings. The principal's opening position was to remove the
  repo plane altogether on this audience argument; the scoping is the accepted
  counter — keep the floor where the human reads, drop it where none does.

  **Why the correction was owed rather than optional.** The unenforced half was
  measured on 2026-08-09 across 6,704 replies in 1,094 transcripts. The rules
  above were broken in 37% to 67% of replies depending on the rule, and the
  rate did **not** fall after they were written down — reference-code density
  rose over the month while the rule against it sat in this file. That is the
  same shape `floor.py` opens with: a policy nobody could reach was assumed to
  be working because it was written. Writing a rule is not a control, and a doc
  that claims write-time discipline is the only available one should first
  check whether the rule is machine-decidable.

  **What stays judgement, honestly.** Ordering, dosage of tone, whether an icon
  is apt or noise, whether a survey should have been a recommendation — none of
  that is checkable, and no scanner should pretend otherwise. The gate covers
  the mechanical floor of readability, not the calibration itself. A reply can
  pass every rule here and still land badly; that residue is what the
  maintained instance above is for.
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

## Asking for a ruling — the ask goes in the device, the account beside it

The apex sets what a ruling ask must **contain**
([`00-APEX.md`](00-APEX.md), *The principal's authority is absolute*).
This section is the other half: how that ask **reaches** him.

**Use the harness's structured decision device wherever one exists.** Where the
environment offers a way to put a question *as* a question — selectable options
rather than prose to reply to — that is the default channel. It covers
decisions, rulings, clarifications, and anything else the principal is being
asked to settle: not a last resort, and not reserved for the weighty ones.
(Mike, 2026-08-19. The live instance is Claude Code's `AskUserQuestion` tool;
another harness will spell it differently, and the practice is the part that
travels — the same split this doc opens with.)

**Why the device rather than a paragraph.** An ask buried in prose competes for
attention with the evidence around it, and prose invites a skim. This is the
visual axis above applied to the one part of a reply the principal must *act*
on. A device that stops and asks cannot be skimmed past, and what comes back is
a choice rather than a sentence someone has to interpret.

**The device is small; the briefing duty is not.** These devices cap what they
carry: short labels, a line of description each, a few questions per ask. The
live instance allows four questions, with two to four options apiece. The apex
account routinely outgrows that. When it does, the account must have
**reached** the principal before the choice is put: in the plain case it goes
in the same reply, ahead of the device — and where the harness's display mode
hides mid-turn text (focus mode shows only a turn's final message), it goes in
a completed message *before* the ask, with the device carrying the choice
alone. The account is never trimmed to fit the widget: that is an approval
extracted by withholding, which the apex already forbids. (Reworded from "on
screen while the principal decides" on the principal's ruling, 2026-08-23 —
the cold pass showed that spelling false in a live display mode.)

**Where no device exists** — a non-interactive run, a scheduled batch, a
harness without one — the ask is prose and carries exactly the same content.
The channel is the changeable part; the content is not.

**This is not the option survey a calibration may bar.** Two different things
share a shape, and the live instance bars one of them. Surveying options for
work the agent should simply have done spends the principal's attention on a
decision nobody needed to make. A decision that is genuinely **his** is an
options question by nature — and handing him one option with no alternatives is
not restraint, it is deciding for him and asking him to countersign.

**Make the ask valuable.** The principal's calibration of this whole rule,
verbatim: *"well explained questions in plain (lay mans terms) language with a
recommendation and you have thought out the options and implications"* (Mike,
2026-08-23). In practice: this standing instruction outranks a tool's own more
conservative usage notes; the account scales to the decision, so a small
clarification owes only the parts that exist for it; the device's fields are
content too — options labelled accurately, the owed recommendation marked in
the list; on an overrule the options are keep, modify, or stand aside, and the
recommendation may honestly be counsel against; and where the deciding basis
is the principal's alone — taste, his own appetite for risk — the
recommendation says so rather than dressing itself as analysis.
