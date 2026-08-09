# 2026-08-08 · 0744 UTC · PRINCIPLES §9 — data carries its time dimension

**Model:** Opus · **Worktree:** `time-dimension-0808` · **Ask:** Mike, opening —
a rule he holds and wanted placed: *all data, application, system and user, must
have a time dimension*, with the explicit framing that this is about the data an
application **handles**, not the code, because git already gives code its
created/changed/removed history. His worked example: a restaurant in a venue
guide needs the date it opened as a business, the date it entered the guide, a
temporary closure, a reopening, and a permanent closure.

## Where it went, and why there

Mike named the placement as the open question — *"I don't know where in the
doctrine this is best positioned"* — so the placement decision is the substance
of this session, not a formality.

Four candidate homes were checked against what each doc actually governs:

| Candidate | Verdict |
|---|---|
| `CONVENTIONS.md` | **No.** It governs the *frame* a value is read against — a time needs a zone, a price a currency. Mike's rule is about whether the value exists at all. Different question; putting it here would blur the doc's one job. |
| `DATA-PROTECTION.md` | **Partly.** The hard-delete clause genuinely belongs to its subject matter, but the principle is far wider than deletion. It would have arrived as a fragment. |
| `RECORD.md` | **No** — but instructive. RECORD already *is* this rule, applied to our own record (append-only log, absolute dating everywhere). That is why the record reads cold years later. It governs records, not application data. |
| `PRINCIPLES.md` | **Yes.** The doc every design is measured against, and it had no data-modelling principle at all — §1–8 cover resilience, structure, interaction, state, security, legibility, reproducibility, leverage. Data modelling was a genuine hole, not a crowded shelf. |

Landed as **§9 — Data modelling: every fact carries its time dimension**, sized
as a section rather than a bullet because the rule has real content (two clocks,
lifecycle, deletion, open intervals, how much dimension to carry).

**No ADR.** The house pattern for adopting a new design principle is an inline
adoption stamp, not a decision record — API-first and one-responsive-web-app
both landed as "adopted as standing practice (decided 2026-07-14)" inside
PRINCIPLES itself. Following the precedent rather than minting a heavier
ceremony for this one.

## The rule as landed

Five clauses, each carrying its generalised case:

1. **Two clocks, kept apart** — *world time* (when it was true out there) vs
   *record time* (when we learned it, and how stale that is now). They diverge
   the moment you find out late. Collapsed into one column, two whole question
   classes die: *was this true on date X* and *what did we believe on date X*.
2. **Lifecycle, not a boolean** — `closed: true` loses *when*, cannot express a
   reopening, and rewrites history as it flips. The generalised form: wherever a
   flag answers *is it?*, ask whether the real question is *since when, and what
   before that?*
3. **A hard delete destroys the dimension outright** — including the fact the
   thing ever existed. A dated end-state is the default; a genuine erasure is a
   recorded act under precedence rule 1, not the routine way things stop being
   current.
4. **Open intervals are legitimate; "unknown" ≠ "none"** — one null standing for
   both is undetectable to the next reader, who reads it as *no* when the honest
   answer was *we never asked*. §0 honesty at the schema layer.
5. **Size the dimension by the questions** — full bitemporality is the heavy end
   and most data does not earn it. Carrying less than the domain's questions
   need is the defect §9 names; carrying more is KISS violated the other way.

## Grounding

Doctrine here must be extracted from decided practice, never invented to fill a
heading — so the case was checked before it was written, not asserted. A curated
venue guide in the fleet holds records with one nullable `verified` field and a
content-pipeline status, and **no world time at all**: it cannot say when a
venue opened, when it entered the guide, or tell a refit from a closure. Every
individual record is fine. The dimension was simply never modelled.

The case is written into §9 **unnamed** — `RECORD.md` § *The record is public*
regulates the join of a private sibling's name to a sensitive posture, and while
a schema gap is not that class, the repo name is not load-bearing for the lesson
either, so the generic form is both safer and better doctrine (roles, not
instances). It is also marked **live and unclosed** in the text: no rounding a
diagnosed gap into a fixed one.

## Seams named so nothing duplicates

- `CONVENTIONS.md` § *What lives elsewhere* gained the frame-vs-existence line:
  a dataset can satisfy every convention here and still be undateable.
- The *state vs stateless* situation test ("undated state is a future lie") now
  points up to §9 as its derived-snapshot instance.
- `method/README.md` item 11 re-lists the principles, since it enumerated seven
  of the eight and would have silently dropped the ninth.

## Handed to Mike, not decided here

Two consequences the landing deliberately does not settle, both queued 🎯 in
`ROADMAP.md` § *PRINCIPLES §9*:

- **Does §9 bind retrofits or only new designs?** Forward-only is free today and
  pays later in datasets that can never answer a temporal question;
  retrofit-obliged spends child-repo sessions now and, for the oldest data,
  can only start the clock — the dates are already gone. The asymmetry is why it
  is worth ruling rather than defaulting: every day without the dimension is a
  day of history that cannot be reconstructed.
- **The named retrofit case** belongs in the child repo's own roadmap and
  changes a shipped data shape, so raising it there is a decision, not a
  mechanical follow-up. Blocked on the ruling above.

## Close

Floor green on the hook plane (13 checks; ROADMAP's size advisory is the
standing pre-existing one). Self-authored doctrine ⇒ rule-4 `⏳` queued in
§ *Doctrine — review-owed*, not spawned here.

---

## Addendum · 2026-08-09 — Mike's ruling, and a clause the case had been sitting on

Both queued 🎯 ruled in one reply, plus a substantive addition.

**1. §9 binds retrofits and new designs.** Ruled against grandfathering, on the
asymmetry the item itself argued — Mike's words: *"this is true"* of the line
that deferring costs a day of unreconstructable history per day. The doctrine
bounds the obligation rather than taking it maximal: start the clock now, never
backfill dates that are gone (fabricating them would breach §0), record the
unrecoverable stretch instead of leaving it implicit. Landed as §9's *Scope*
clause.

**2. Ownership sits with the repo that owns the data.** atelier stops at the
principle and the `PROPAGATION.md` pointer. Deliberately **no per-child ledger**
here: it would be a second source of truth for work this repo does not perform.
The residual risk is recorded rather than pre-solved — a pin delivers doctrine
reliably, but a *retrofit* needs someone to notice it applies to data already
shipped, and if children miss it, that absence is the evidence for mechanising a
check. Tracked as the one remaining open line under the roadmap section.

**3. The clause the case had been sitting on.** Mike, on the venue example:
*"in all repos that have a need to store data like this should note the result
(e.g. verified) and the metadata should note when it was verified, how it came
to verified etc."* That is wider than time — it is **provenance of the
assertion**, and §9 as first landed only asked for the date. Added as the second
bullet: a field holding a conclusion carries *when it was established and by
what method*, because without it an owner-confirmed fact and a scraper's
two-year-old guess render identically. Anchored to `EVIDENCE.md` §3
(acquisition method sets error risk) — the same rule the record already applies
to claims, now stated at the data layer. The payoff named in the text: it makes
staleness **computable** rather than felt, since a refresh policy can only exist
where each value knows its own age and how expensively it was obtained.

Floor green; the `⏳` pointer's delta extended to cover this commit rather than a
second pointer raised — one doctrine cycle, one review.
