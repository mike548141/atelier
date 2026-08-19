# 2026-08-19 · 0257 UTC · Asking for a ruling — the device, and the verified basis beneath it

**Tier:** Opus 5 (1M). **Worktree:** `decision-ask-doctrine-0819`.
**Commission:** Mike, verbatim and in full, typos included — the wording is the
artefact, not my restatement of it:

> As a rule unless there are extenuiating circumstances repo's should use the
> AskUserQuestion feature to ask for questions, decisions, rulings, and similar
> feedback or clarifications from the principal (me). If there is too much
> detail to fit in AskUserQuestion then give the supporting information in the
> session so its visible while using AskUserQuestion.
>
> When asking for a decision you should verify that all information is the
> truth, the whole, truth, and nothing but the truth so I can make a properly
> informed decision. Do not infere or assume the information, if the cost is too
> high to verify then you must be clear with the principal about what you have
> assumed/infered.
>
> I like decisions to be supported with options including pro's, con's,
> impacts, and a recommendation.
>
> Add that to Atelier

## Three rules, and they do not all belong in one place

Read straight, the commission carries three separable rules: a **channel** rule
(use the structured device), an **evidence** rule (verified, or say what is
assumed), and a **shape** rule (options with their trade-offs, plus a
recommendation). Two of those are about what an ask must *contain*, and one is
about how it *travels*. The apex already owns the first kind — its
informed-principal duty lists what, why and likely impacts — so the shape and
evidence rules were written there as two more of the same list, not as a new
section competing with it. The channel rule went to `COMMUNICATION.md`, which
`AUTONOMY.md` already pointed at *for the how* and which had no such section to
land on. One fact, one home (`EVIDENCE.md` §9).

## What landed

**`00-APEX.md` § *The principal's authority is absolute…***

- Two bullets added to the briefing duty: **the options, each with its
  trade-offs** (what it buys, what it costs, what it affects; and where only one
  option is real, say so and say why the others are not), and **a
  recommendation** with its reasoning shown.
- The clause above the list read *"The agent may still recommend"*. It now reads
  that the agent **owes** one — permission upgraded to obligation, on his *"I
  like decisions to be supported with… a recommendation"*. Dated to him,
  2026-08-19, beside the 2026-07-14 grounding that clause already carried.
- A new paragraph, **every fact in the ask is verified or marked as not
  verified**, quoting his truth-the-whole-truth line, and stating the escape
  honestly: where verifying costs more than the decision is worth, name what is
  assumed — never present an inference in a verified fact's voice. Pointed at
  `EVIDENCE.md` §1 and §13 rather than restating either.
- A closing pointer to the new `COMMUNICATION.md` section for delivery.

**`COMMUNICATION.md` § *Asking for a ruling — the ask goes in the device, the
account beside it*** (new, above the worked example)

- The device is the **default channel** for decisions, rulings and
  clarifications — not a last resort, not reserved for the weighty ones.
- Why a device rather than a paragraph: an ask buried in prose competes with the
  evidence around it and invites a skim; a device returns a choice rather than a
  sentence to interpret. This is the doc's own visual axis applied to the part
  of a reply the principal must act on.
- **The device is small; the briefing duty is not.** When the apex account
  outgrows the widget, the account goes in the session reply *first*, on screen
  while he decides, and the device carries only the choice. The reverse — an
  account trimmed to fit — is an approval extracted by withholding, which the
  apex already forbids.
- Where no device exists (non-interactive run, scheduled batch), the ask is
  prose and carries identical content. The channel is the changeable part.
- **The tension with the anti-survey preference, named rather than left for a
  reader to trip over.** The calibration bars option surveys; this rule requires
  options. They are different things: surveying options for work the agent
  should simply have done spends attention on a decision nobody needed, whereas
  a decision that is genuinely his *is* an options question — and handing him
  one option is not restraint, it is deciding for him and asking him to
  countersign.

**`AUTONOMY.md` § *Always confirm*** — its existing `COMMUNICATION.md` pointer
now names the section, and moved out of the middle of an already 79-word
sentence into its own.

## Judgement calls worth the next session knowing

- **The tool is named as the instance, not the rule.** `AskUserQuestion` is
  Claude Code's spelling; the practice is *use the harness's structured decision
  device*. That is this doc's own two-things-kept-separate split, and ADR 0005's
  named-worked-example framing — an adopter on another harness substitutes their
  own device without touching the rule.
- **"Extenuating circumstances" was written as a mechanism, not a mood.** His
  wording allows exceptions; the doc names the one that is checkable — no device
  exists in this environment — rather than leaving a judgement hatch that any
  session could walk through.
- **Nothing was removed.** The apex's existing waiver clause (the principal may
  decide on less; the agent informs, never polices his diligence) is untouched
  and still governs: a recommendation being owed does not make his taking it
  conditional on reading it.

## Evidence

- `plainscan` measured as a **delta, not a level**: the three files carry 48
  findings at `HEAD` and 48 after the edit (`00-APEX.md` ×23 ·
  `COMMUNICATION.md` ×14 · `AUTONOMY.md` ×11, unchanged in each). Three
  intermediate drafts added findings and were rewritten until the delta was
  zero — the baseline was taken from `git show HEAD:` copies scanned in a
  scratch tree, not assumed.
- Full floor run at the landing commit, recorded in the commit message.

## Not claimed

**This rule is unenforced, and the honest reason is that nothing watches the
channel.** `plainscan` reads committed prose; it cannot see whether an ask went
out as a device or as a paragraph. The reply plane that once watched the agent's
own output is unwired (Mike, 2026-08-15) and its remedy was the half that
failed. A detector is *conceivable* — the transcript records tool calls, so
"asks that used the device" against "asks that did not" is countable after the
fact — but conceivable is not built, and I have not probed whether the
transcript distinguishes an ask from an ordinary reply. Queued as a candidate at
`220/060`, unfunded, with that uncertainty stated rather than smoothed over.

## The channel, mid-session

A private child filed a fifth finding over the cross-session channel while this
work was in flight — class only, no repo, hosts, client or filenames, and
explicitly *"not asking you to write doctrine"*. It claims a **threat-model gap
in `GUARDS.md`**: every guard the child has protects a *reader* from a bad
artefact, and none knows another *writer* exists. Queued at `320/050` as a
proposal, because it adds to the fourth requirement Mike ruled on 2026-08-17.

**One shape of the six was reproduced here, and only one.** The filer asked to
be checked rather than believed. Shape 2 — the floor reads the worktree, so a
peer's uncommitted edit fails your unrelated commit — reproduces at the parent
by reading `tools/floor.py`'s `_render`: **11 of 15 hook-plane checks render
absolute worktree paths, 4 take `--staged`**. That is a registry read, not a
two-session probe, and the item says so. The other five instances are recorded
as the child measured them, unreproduced.

Self-authored doctrine, so the rule-4 `⏳` is queued at `160/270` in this
landing commit, and neither taken nor spawned here. The `320/050` proposal is
board work, not doctrine, so it carries no pointer of its own.
