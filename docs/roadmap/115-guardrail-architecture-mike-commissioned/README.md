# Guardrails for atelier and its children (Mike commissioned 2026-08-15)

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

**Scope correction, 2026-08-15.** The first pass answered the *example* and
called it the commission. Mike corrected it twice in one message. First, the
datescan question was an illustration, not the scope. Second, the question it
illustrates is **narrow-scoped guards versus a wider purpose-based guard**, and
the first pass had turned that into a question about *breadth* — many small
checks versus one big one. Both errors are recorded here rather than fixed
quietly, because the
first pass's items are still on this board and a later reader needs to know
which frame each was written in. Items `010`–`090` are the first pass. Items
`100` and up are the second.

## What was run

Ten agents across two passes, 2026-08-15. Pass one: a guard inventory, a
verbatim intent recovery, external prior art, a divergence case-file, and a
doctrine census. Pass two, after the correction: the full guardrail surface
beyond scanners, child-repo outcomes measured live, the purpose-versus-feature
question proper, and the cost side.

## The answer, in three parts

### 1. On the axis Mike actually asked about

**Neither organising principle is safe, and the defect is that neither is
declared.** Feature-based guards do not erode over time — they are *born aimed
off*. `datescan`'s loudest check carries 95% of its output against a breach
class that none of its three grounding incidents contained. But purpose-based
guards are not immune either: `stampscan` is the most purpose-shaped guard in
the tree, and it enforces the **inverse** of the doctrine it cites, and has
since it shipped. A purpose-based guard formalised wrongly is worse than a
feature-based one, because it looks principled and nobody re-derives it.

Every registry entry already carries a `why` field. It is printed and **never
compared to anything**. The asymmetry underneath that is the finding: *the
estate demands a reason for weakening a guard, and no reason for building one.*

The one recorded case of a guard being tested against its purpose found what
eight rule-level findings had all missed. That section labelled itself
"(reviewer, mandatory)" while being mandated nowhere, and it appears in one of
109 review files.

So the answer is not to merge guards and not to abandon feature-based checks.
It is to make the purpose a **first-class, testable field**, so a guard that
drifts from it is a finding rather than a discovery. Item `120`.

### 2. On the commission as asked

**Scanners are one class of guardrail out of eleven, and the only mature one.**
Twenty-one mechanisms act *after* an act — at commit, at CI, at review. Five act
before it, and only one of those is mechanical rather than prose. The class that
could sit between a decision and the act is the harness plane, and it is empty
in atelier and reaches no child.

That is the structural reason the aim recorded in the policy-as-code section —
doctrine that is directive as well as enforced — has no carrier. It is not a
wording problem. There is nowhere for a before-mechanism to live. Item `100`.

The consequence shows in what is guarded: `00-APEX.md` has **no blocking gate on
any rule**, and `AUTONOMY.md`'s always-confirm floor has none either, including
the line forbidding an agent from widening its own authority. Item `110`.

### 3. On the child repos

**Measured 2026-08-15, not recalled.** Enforcement propagation works: 18 of 18
floors wired, by call rather than copy, exactly as its decision record intended.
Everything else propagates badly or not at all. Sixteen of seventeen pins are
stale, nine of them about five weeks back. Eight children run a safety floor
missing three of its seven concerns, unchanged a week after the audit that found
it. Roughly 1% of the method corpus reaches a child's context at session start.
Items `150`–`170`.

And the enumerator built to stop all this decaying has itself decayed: **the
daily estate conformance job has failed 19 times out of 19 and never once been
green.** Item `140`.

## The shape of what should be built

Four things, in order, and only the last is a new scanner.

1. **A before-plane** — the harness class, so a guardrail can act at the moment
   of decision rather than at the commit. Everything the principal's directive
   aim needs, and the only place the apex and autonomy floors could ever be
   mechanised.
2. **Purpose as a declared, tested field** on every guard, with a replay proving
   the check fires on its own grounding incidents.
3. **Coverage reporting** — a guard says whether its rule fired at all, so
   "clean" and "scanned nothing" stop looking identical.
4. **Then** the data-provenance check, over structured data only.

## What is queued elsewhere and not restated

The enforcement-ladder floor question and expiry-at-every-granularity have
carriers in other sections and are pointed at, not repeated. The evidence-window
rule proposed in item `010` survives the correction, but pass two showed it is
**necessary and not sufficient** — it explains why a proxy is forced and says
nothing about testing the proxy once forced. That is noted in the item itself.
