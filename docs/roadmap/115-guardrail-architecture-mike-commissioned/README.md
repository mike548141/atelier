# Guardrail architecture — narrow guards vs one broad guard (Mike commissioned 2026-08-15)

**The ask, in Mike's words** (kept verbatim; the restatement below is a reading
of it, not a replacement — where they differ, the quote governs):

> I want you to coordinate subagents (whatever model is the best fit) to
> research what guardrails we can and should build in atelier to ensure the best
> outcomes from atelier itself and the child repos. For example one concern I
> have is we are making lots of narrowly scoped guards like datescan, and that
> might be the right approach, but should we instead that a providence scan?
>
> If you look at past session transcripts you will find things like I have said
> all data must have a time dimension (e.g. the price on a dish in faves is
> valid from X to Y dates). But we also talk about timestamping facts to
> understand their provenance metadata i.e. how was the fact collected/received,
> by who, when, what is our confidence level in the fact etc...
>
> If datescan starts to be interpreted as just it must have a date and the date
> must be formatted a certain way then it may force unintended outcomes, miss
> the intended outcome, or even cause damage

**How it was answered.** Six agents, run 2026-08-15. A rule-by-rule inventory of
every guard. A verbatim recovery of Mike's stated intent on time and provenance,
across every repo's transcripts. External prior art. A case-file of every
recorded instance in this estate of a guard enforcing its letter and missing its
point. And a doctrine-enforcement census. Roughly sixty dated divergence
incidents were recovered from the repo's own records.

## What the research concluded

**The premise is confirmed on the exact guard Mike named.** The `datescan` cold
pass of 2026-07-23 recorded it. Its verdict: the scanner is *"well-built; aimed
slightly off the mistake that actually cost the five-file sweep"*. The loudest
check produces 57 of 60 findings on a breach class that not one grounding
incident contained.

**But the concern lands on a different tool than the example suggests.**
`datescan` enforces `EVIDENCE.md` §7 — state time absolutely, never relative to
*now* — over written prose. It never checks that a date *exists*, and it never
looks at application data. So it cannot drift toward "a date must exist and be
formatted thus"; it was never doing that job. `PRINCIPLES.md` §9 — data carries
the time dimension its domain implies — has **no guard at all**. The gap is
total rather than partial, and §9 itself already separates the two questions:
existence is §9's, frame is `CONVENTIONS.md`'s.

**The predicate that explains the divergence is not narrowness.** Every serious
incident recovered has one shape: *the fact that licenses the exception lives
outside the guard's evidence window*. `pathscan` has no time axis, so records
naming historical paths can never come clean. `plainscan`'s window is one
document while the reader's knowledge spans years. A term list cannot express
"this name is public in *this* repo". `stampscan` cannot tell a doc describing
its syntax from one using it. Syntax checks and presence checks drift at the
same rate; the window explains the variance, the syntax/presence axis does not.
A second pattern is as clean: guards over machine-shaped input barely drift at
all, while guards over prose drift constantly.

**So broadening would make it worse, not better.** A broader guard serves a
wider intent through the same narrow window. One suppression then silences the
whole concern — the defect `GUARDS.md` names when it ranks Line below Check
below Repo. The external precedent points the same way. ESLint, Ruff, Semgrep
and the Open Policy Agent each consolidated *engines* while keeping rules
granular and separately suppressible. None consolidated intents.

**And Mike has already ruled the shape of the answer**, on 2026-07-19: *"We
should fix the source of the problem upstream rather than adding more and more
mitigations downstream to mitigate the problem."*
That record also gives the test. A fix is downstream when it must be applied in
several places and the next one will cost as many again. The reason-required
loader exists in ten to eleven per-scanner copies, and correcting it took
fourteen regex sites across twelve files. That is the downstream signature by
Mike's own definition.

## What is queued here, and what is not

Two of the four decisions surfaced by the research are **not** filed here
because they already have homes: the enforcement-ladder floor question sits in
the policy-as-code section, and expiry-at-every-granularity sits in the
estate-audit section. Neither is restated — pointing up, never a second
original. The items below are the ones with no existing carrier.

Everything here is queued, not built. Two are decisions that are Mike's; the
rest are defects and builds that wait on those decisions or on their own
evidence bar.
