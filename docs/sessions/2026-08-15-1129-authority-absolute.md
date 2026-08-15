# 2026-08-15 · 1129 UTC · The principal's authority is absolute; his rulings are conditioned (Fable, wt: authority-absolute-0815)

**Mike's ruling, verbatim** (same session as the Laws removal, immediately
after it):

> "The principal's authority is conditioned on being informed" — This part
> of APEX is wrong. The principals authority is absolute, and claude can
> never over-rule the principal no matter the situation including if claude
> believes the principal is uninformed. It is the principals rulings that
> are conditioned on being informed. When you ask the princiapl to rule if
> something is good enough or if we should implement a particular option
> that ruling is challengable on the principal being informed. Even if
> informed that ruling is challengable by a review session as well. But
> the princiapls ability to make an authoratative decision must never be
> decayed. Update the doctrine to reflect all that.

## What changed

- **`00-APEX.md`** — the section is retitled *"The principal's authority
  is absolute; his rulings are conditioned on being informed"*. The
  sentence that put the condition on the authority ("That authority is
  real, but it is not exercisable uninformed: the principal cannot make —
  or override — a decision he has not been equipped to understand") is
  replaced by a paragraph stating: the authority is absolute and never
  decays; the agent can never overrule the principal in any situation,
  including one where it believes him uninformed; being informed
  conditions the *ruling*, which is challengeable on that basis and — even
  when informed — by an independent review session; a challenge is raised
  *to* the principal, who rules on it, and never licenses the agent to act
  as if the ruling had not been given. The "extracted approval" sentence
  now says such an approval stands as the principal's word but is open to
  challenge — raised by supplying the missing account and asking again,
  never by declining to obey. The accountability paragraph and the
  what/why/impact duty are unchanged.
- **Restatements aligned:** the section-title reference in `RECORD.md`
  (ADR acceptance), `AUTONOMY.md` (grant floor), `CONCURRENCY.md`
  (end-of-run report), `REVIEW.md` rule 3 (the "not a decision the doctrine
  recognises" line replaced with the challengeable-not-void framing); and
  the **child floor block** in `PROPAGATION.md` with its byte-identical
  `docs/build/templates/CLAUDE.md` stamp — the floor now says the
  authority is absolute, never overrule him even if you believe him
  uninformed, and an unbriefed approval is open to challenge on the
  briefing (stampscan: identical, 52 lines).

## Addendum — the dilemma line comes back as honesty doctrine

Mid-turn, Mike ruled on the flag the Laws-removal session had raised:

> And yes we do need to keep this point that claude must "Surface a genuine
> dilemma; never silently resolve it". This is a part of the honesty
> doctrine in the APEX, it is a part of being transparent is a necesity to
> being honest. As they say in the USA - Tell the truth, the whole truth,
> and nothing but the truth

Applied in the same commit stream: `00-APEX.md` § "Honesty is absolute"
gains an in-practice bullet (a fork quietly picked on the principal's
behalf is a withheld choice; withholding is dishonesty per the
transparency clause; the whole truth includes the dilemmas). Restored to
the child floor block + template stamp (stampscan identical, 53 lines) and
the `session-onramp` skill — under the *honesty* bullet in each, where it
now belongs, not the Laws bullet it used to ride.

## Judgement calls, said aloud

- **"Challengeable" is not "void".** The old wording had the doctrine
  refusing to recognise an unbriefed approval, which is a quiet overrule of
  the principal. The new wording keeps the ruling standing as his word and
  makes the agent's remedy re-briefing — the only move consistent with an
  authority that never decays. If Mike wants "challengeable" stronger or
  weaker than that, it is a one-paragraph edit.
- **Two floor bullets grew by two lines** — the floor block is the hottest
  read path in the fleet (SR2). The addition is a live safety statement
  (never overrule the principal), which SR2 says may not be trimmed away.
- **Children** still carry the old floor sentence until their next pin
  bump — the standing propagation lane; no child edited from here.

## Board and review state

- New `[x]` item in `160-doctrine-review-owed` (`200-…`) with the ruling
  verbatim; **rule-4 Fable cold pass queued** refs-only (`210-…`) —
  principal-ruled, agent-applied apex doctrine; queued, not spawned.
- The still-open *apex accountability* review cycle (AA1–AA5, 2026-07-26)
  covers the accountability paragraph this edit leaves untouched; the two
  cycles sit side by side rather than merging.
- Floor: scanners green locally through the hook; the pushed-floor run at
  head reported in-session at close.
