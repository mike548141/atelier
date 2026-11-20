# 2026-08-08 · 0744 UTC · PRINCIPLES §9 — data carries its time dimension

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 249+1 -->
- [2026-08-08 · 0744 UTC · PRINCIPLES §9 — data carries its time dimension (Opus, wt: time-dimension-0808)](2026-08-08-0744-principles-time-dimension.md) — Mike minted a rule and named its *placement* as the open question: all data — application, system, user — must have a time dimension, explicitly about the data an application handles rather than the code, since git already dates code's creation, change and removal. Four homes checked against what each doc actually governs: `CONVENTIONS.md` governs the *frame* a value is read against, not whether it exists; `DATA-PROTECTION.md` owns only the deletion clause; `RECORD.md` already *is* this rule applied to our own record, which is why the record reads cold years later. It landed in `PRINCIPLES.md` as **§9 — Data modelling**, where the hole was genuine: §1–8 never reached the data a system holds about the world, and the gap is structural rather than an oversight, because code gets its time dimension free from git so the habit of asking "when?" never transfers. Five clauses: two clocks kept apart (world vs record time), lifecycle transitions instead of booleans, a hard delete destroying the dimension outright, open intervals as legitimate with "unknown" ≠ "none", and the dimension sized by the questions the domain will ask. No ADR — the house pattern for a new principle is an inline adoption stamp (API-first, mobile-first, both 2026-07-14). Grounded before it was written: a curated venue guide in the fleet carries one nullable `verified` field and no world time at all, so it cannot tell a refit from a closure — written in unnamed (the name is not load-bearing for the lesson) and marked **live and unclosed**. Seams named in both directions so no rule duplicates another. Two consequences handed to Mike, not decided: whether §9 obliges retrofits or binds new designs only, and the child-repo retrofit that follows it. Floor green; self-authored doctrine ⇒ rule-4 `⏳` queued, not spawned.
<!-- archivecut:log-entry docs/SESSIONS.md 250+1 -->
- [2026-08-09 · 0810 UTC · §9 ruled — it binds retrofits, and a stored result carries its derivation (Opus, addendum to the 2026-08-08 entry)](2026-08-08-0744-principles-time-dimension.md) — Mike ruled both queued 🎯 in one reply and added a third clause. **Retrofits bind**, no grandfathering, decided on the asymmetry the item argued — deferring is not cost-free waiting but ongoing loss — with the obligation bounded honestly in the doctrine rather than taken maximal: start the clock now, never backfill dates that are gone (fabricating them would breach §0), record the unrecoverable stretch. **Ownership sits with the repo that owns the data**; atelier stops at the principle and the `PROPAGATION.md` pointer, and deliberately keeps *no* per-child ledger, which would be a second source of truth for work this repo does not perform — the residual is recorded instead of pre-solved, since a pin delivers doctrine reliably but a retrofit needs someone to notice it applies to data already shipped, and children missing it is the evidence that would justify a check. **Third clause, wider than time:** generalising from the `verified` field in §9's own case, a field holding a *conclusion* now carries when it was established and by what method — without it an owner-confirmed fact and a scraper's two-year-old guess render identically. Anchored to `EVIDENCE.md` §3, the same rule the record already applies to claims, now stated at the data layer; the payoff is that staleness becomes computable rather than felt. One doctrine cycle, so the existing `⏳` pointer's delta was extended rather than a second pointer raised.
<!-- archivecut:log-entry docs/SESSIONS.md 251+1 -->
- [2026-08-09 · 0300 UTC · a cancelled floor run is not an all-clear (Opus, second addendum to the 2026-08-08 entry)](2026-08-08-0744-principles-time-dimension.md) — Mike asked for the session's own floor run to be finished rather than leaning on the superseding commit's green, and the ask surfaced a hole in the rule that governs closes. `RECORD.md` already required the pushed floor run's result over the local scan, but never anticipated a third state: `ci.yml` runs the floor under `cancel-in-progress: true`, so a parallel session's push to the same ref cancels the in-flight run for the earlier commit — it ends `cancelled`, neither pass nor fail, and no run ever reports on the commit that was actually pushed. Observed live here: the ruling commit's run was killed ~90 seconds in by a second session's push, and the first close cited that later commit's green — true, and this tree is its ancestor, but it is evidence for a different commit and the distinction went unmade. Re-run attempt 2 against the session's own SHA returned success. Landed as a sub-bullet at the point of use rather than a new section, since the surrounding rule was right and merely under-specified: read the *conclusion*, never "the run finished"; on `cancelled`, re-run against your own SHA. Deliberately not built — the cancellation is correct behaviour that protects the Actions-minutes pool, so the remedy is reading discipline, and a close-time probe is left for evidence of recurrence: one instance grounds a clause, not a build. Rule-4 `⏳` queued.


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

## Addendum 2 · 2026-08-09 — the close itself surfaced a hole in the close rule

Asked to finish the floor run rather than lean on the superseding commit's
green, which turned a papered-over detail into a recorded finding.

**What happened.** The ruling commit `98a6f37` was pushed; its floor run started;
~90 seconds later a **parallel session** pushed `00f6f59` and the run ended
`cancelled`. `ci.yml` sets `concurrency: cancel-in-progress: true`, so this is
routine, not a fault. The first close cited the superseding commit's green run —
true, and it does cover this tree since `98a6f37` is its ancestor, but it is
evidence for a *different* commit and the distinction was not made. Re-running
attempt 2 against `98a6f37` returned `success`; that is the honest all-clear.

**Why it is worth doctrine.** `RECORD.md`'s existing rule says the evidence is
the floor **at head**, not the local scan — it never anticipated a *third*
state. `cancelled` is neither pass nor fail, and the failure mode is silent: a
session reads "the run finished", sees no red, and closes. The clause landed as
a sub-bullet at the point of use rather than a new section — the surrounding rule
is already the right rule, it was just under-specified.

**What was deliberately not built.** The cancellation is correct behaviour;
`cancel-in-progress` is what stops a busy ref burning Actions minutes on
superseded trees. So the remedy is reading discipline, not config. A close-time
probe that refuses to report green on a `cancelled` conclusion is plausible and
is left unbuilt: one instance grounds a clause, not a build, and if it recurs
that recurrence is the evidence.

**Concurrency note for whoever reads this cold:** a second session was live on
this repo throughout the 2026-08-09 work, pushing to `main` in the same working
copy. Nothing collided — this session's writes were committed and pushed before
each pause — but the "assume you are not alone" prior was correct, and the
cancelled run is a *second*, previously unrecorded way a parallel session's push
touches your work.
