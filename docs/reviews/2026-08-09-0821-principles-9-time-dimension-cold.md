# Cold pass — the PRINCIPLES.md §9 time-dimension principle

**Pass type:** doctrine cold pass (REVIEW.md rule 4 — self-authored doctrine).
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04).

## Spawn provenance

- **Author of the work under review:** the sessions that landed the delta on
  2026-08-08 and its 2026-08-09 extension (see *What the work is*).
- **Who spawned this review:** the principal (Mike), in a session he opened on
  2026-08-09 and pointed at the review queue — rule 4's worked example. His
  words: *"Please do any review work that waiting."*
- **Author's non-involvement:** the taker session authored no part of this
  delta, was neither started nor instructed by the authoring sessions, and
  wrote this brief as the non-author taker. Rule 4's single criterion is met,
  and the tier was checked at selection.
- **Orchestration shape:** the review runs under an orchestrator holding a
  context partition — the intent-record references are withheld from this brief
  and handed to the reviewer only after its own findings are durably written
  (REVIEW.md rule 1, the one arrangement honestly called structural).

## What the work is

Doctrine landed 2026-08-08, extended 2026-08-09, reviewed at HEAD:

1. [`docs/method/PRINCIPLES.md`](../method/PRINCIPLES.md) — the new §9
   (*Data modelling — every fact carries its time dimension*), the §1–8 → §1–9
   scope line, and the *state vs stateless* situation test now pointing at §9;
   extended by the 2026-08-09 ruling — §9's derivation-metadata bullet and its
   *Scope* clause.
2. [`docs/method/README.md`](../method/README.md) — item 11's principle list.
3. [`docs/method/CONVENTIONS.md`](../method/CONVENTIONS.md) —
   § *What lives elsewhere*, the frame-vs-existence seam.
4. The `CHANGELOG.md` entries for both landings.

## Scope

Widest the work admits: the principle's intent, its wording as it will bind
future data-modelling decisions estate-wide, the seam it draws against
CONVENTIONS.md, and fit with the other eight principles. **Non-goals — one,
and it does not fence the risk:** the reviewer does not decide any finding.
Self-authored doctrine; findings are the principal's to rule on (rule 3).
Counsel may be recorded, labelled as such.

## The four lenses

1. **Approach & assumptions** — name the load-bearing assumptions yourself
   first. Is a time-dimension rule a *principle* (universal, situation-tested)
   or a convention? Is the frame-vs-existence seam drawn in the right place?
2. **Correctness & quality** — is §9 internally consistent, and consistent
   with how the repo's own records actually stamp time (UTC at rest)?
3. **Completeness / harvest** — what does a time-dimension principle owe that
   §9 does not say; what existing doctrine does it duplicate or contradict?
4. **Security & privacy** — mandatory. atelier is PUBLIC: does §9 instruct
   future repos to retain or stamp anything that widens a privacy surface
   (times joined to identities, derivation trails)? If genuinely surface-free,
   discharge in one explicit line with grounds. The house security scanner
   reads pending diffs; this is a landed-delta review, so state the reach case
   that applied.

## Re-run obligation

Any claim in the delta text stamped as measured, live-proven, or grounded is
re-run, not read, where the repo admits it — including the cross-references
between the three method docs (do they actually point where they claim).

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the intent-record refs are orchestrator-held under the rule-1 context partition, handed over only after the reviewer's findings are durably written -->

Rule 2 bars: `docs/ROADMAP-DONE.md`, `docs/sessions/`, every prior verdict in
`docs/reviews/`, and the intent-record item for this delta, rulings included
(its reference is held by the orchestrator and will be provided on receipt of
your committed findings). Reconcile after, never anchor before.

## Process

Append your verdict below a `---` divider in this file: provenance repeated,
per-lens answers, findings with stable IDs (prefix `TD`) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, and a follow-up checklist. Then report; the deferred
references arrive; append a reconcile section and finalise.

---

# Verdict — phase 1 (pre-reconcile)

**Provenance, repeated.** Cold rule-4 pass on self-authored doctrine, run on
Fable (the principal-named review tier, ruling 2026-08-04). Spawned by the
principal via an orchestrator holding the rule-1 context partition; the
reviewing session authored no part of this delta and was neither started nor
instructed by the authoring sessions. The reviewer named the load-bearing
assumptions before opening any delta file. Rule-2 bar honoured: no file in
`docs/sessions/`, `docs/ROADMAP-DONE.md`, `ROADMAP.md`, or any other review
was opened; the intent record was identified by *path only*
(`docs/sessions/2026-08-08-0744-principles-time-dimension.md`) via
`git show --name-only` and not read.

**Exposures disclosed, not denied.** (1) The two landing commit messages
(`c9c177a`, `98a6f37`) were read to identify the delta; they carry the
author's account of the work, including its placement reasoning. My
assumptions were named before that read, but the messages are author framing
and I read them — named here so the reconcile can weigh it. (2) The
tree-wide restatement sweep excluded `docs/SESSIONS.md` and `docs/sessions/`
per the records-exclusion discipline; no records content reached me.

**Security-scanner reach case.** Landed-delta review, clean tree: no pending
diff exists for `/security-review` to read, and its exclusions bar markdown
documentation — the delta's entire file class — so a clean pass would be
definitionally empty and is weighed as nothing. The lens was discharged by
direct analysis instead (lens 4 below), and it is *not* surface-free: see
TD1.

## Load-bearing assumptions (named first, then attacked)

1. A time-dimension rule is a *principle* (universal, situation-tested), not
   a convention. **Held** — it governs whether data is designed to carry a
   dimension at all: a design decision with a situation test, not a frame
   default. A dataset can satisfy every CONVENTIONS rule and still be
   undateable, which is the cleanest proof the two questions are different.
2. The frame-vs-existence seam is drawn in the right place. **Held** — and
   verified bidirectional: PRINCIPLES §9 points at CONVENTIONS for how a
   stamp is written; CONVENTIONS § *What lives elsewhere* points back for
   whether it exists. No drift between the two statements.
3. The repo's own records live the rule. **Held** — RECORD.md is verifiably
   append-only with absolute dating; both §9 provenance stamps are correct
   *in UTC* (landing commits 2026-08-08 07:46Z and 2026-08-09 02:40Z), so
   the NZ-evening date-ahead trap was not hit.
4. The 2026-08-09 extension widens no privacy surface. **Attacked and
   partially fell** — see TD1: the derivation bullet's "by whom" and the
   prefer-retain posture are a real privacy surface the principle prices
   only as ceremony.
5. Cross-references resolve as claimed. **Held** — every one re-run; see
   lens 2.

## Per-lens answers

**1 — Approach & assumptions.** Right problem, right layer. The core insight
— code gets a time dimension free from git so the "when?" habit never
transfers to data — is sound and well argued. Placement in PRINCIPLES as a
ninth section is correct: CONVENTIONS governs frames, DATA-PROTECTION owns
the destructive act, RECORD is the instinct applied to our own record, and
no data-modelling principle existed. Appending as §9 preserves the §N
citation stability that §7 promises. The retrofit ruling's asymmetry
argument (deferral is ongoing loss, not free waiting) is genuinely decisive
and honestly bounded — clock starts now, no fabricated backfill, gap
recorded. Ownership landing with the data-owning repo is consistent with
the propagation model, and declining a per-child ledger is the right DRY
call with the open question honestly left open.

**2 — Correctness & quality.** Every stamped claim re-run where the repo
admits it:

- `EVIDENCE.md` §3 is titled *Acquisition method sets error risk — record
  it* — the citation is verbatim-accurate, and the applied-at-the-data-layer
  reading is faithful to its content.
- `RECORD.md` is append-only with absolute dating (its own text, plus
  EVIDENCE §7) — the "same instinct already applied" claim holds.
- `DATA-PROTECTION.md` carries the destructive-op discipline and names
  privacy/retention obligations (NZ Privacy Act), so the hard-delete
  bullet's pointer resolves.
- The CONVENTIONS ADR link (2026-07-15-1327) exists; all in-text doc links
  resolve.
- The state-vs-stateless situation test points up to §9 and §9 points back
  down to it; the ladder intro reads §1–9; method README item 11 lists data
  modelling and describes §9 accurately.
- Both CHANGELOG entries were checked clause-by-clause against the doc text:
  faithful, no overclaim, and the unclosed status of the worked case is
  carried honestly in both.
- Tree-wide sweep (records excluded): no stale "§1–8" / "eight principles"
  restatement survives outside the CHANGELOG's own dated historical entries,
  and no skill, command, or template restates the principle list — the §6
  sweep-surface obligation had nothing left to sweep.
- The venue-guide grounding claim is *not re-runnable from this repo*: the
  dataset lives in a private child, deliberately unnamed here (correct under
  the public-record rule). Accepted on stated grounds, recorded as unverified
  by this pass — the one stamped claim this review could not re-run.

**3 — Completeness / harvest.** The five original clauses plus the two
extensions cover the load-bearing ground: two clocks, derivation, lifecycle,
deletion, unknown-vs-none, sizing, retrofit scope, ownership. What it owes
and does not say: the privacy face of the sizing test (TD1) and its relation
to its nearest in-file neighbour §6 (TD2). Duplication checked: no clause
restates EVIDENCE §7/§8 or RECORD; the derivation bullet cites rather than
copies EVIDENCE §3. Nothing contradicts the precedence ladder — the
hard-delete bullet correctly routes through rule 1.

**4 — Security & privacy.** Mandatory lens, run at design altitude, and not
surface-free: §9 instructs every future repo to retain *more* dated history
by default and to consider storing *who* established a fact. Times joined to
identities are exactly the class privacy regulation minimises. The principle
half-answers this — erasure routes through precedence rule 1 and
DATA-PROTECTION — but the sizing test prices over-carrying only as §2 KISS,
never as a §5 privacy cost. That gap is TD1, MODERATE. No secrets, no
personal data, and no private-repo identity enter the delta text itself; the
worked case is correctly generic.

## Findings

**TD1 — MODERATE — over-carrying is priced as ceremony, never as a privacy
surface.** §9's sizing bullet names carrying too much dimension as "§2 KISS
violated in the other direction", and the derivation bullet invites "by
whom, too, where that matters". For personal data both are §5 territory:
record-time trails and by-whom fields joined to identities are themselves
personal data, retention-limited by NZ Privacy Act IPP 9-class obligations,
and the principle's prefer-a-dated-end-state posture can point the opposite
way from a lawful retention limit. The erasure escape exists (hard-delete
bullet, precedence rule 1, DATA-PROTECTION) but the *sizing* decision — the
moment the dimension is designed — never names privacy as an input, in a
principle whose blast radius is every future dataset in the fleet. *Counsel,
labelled as such:* one clause suffices — in the sizing bullet, that for
personal data, dimension beyond the questions is a §5/privacy defect as
well as a KISS one, and retention limits can make the lawful answer *less*
dimension; the decision is the principal's.

**TD2 — minor — "which the other eight never reached" overstates against
§6, and §9 does not situate itself against its nearest neighbour.** §6
already says "Facts are dated and attributed" — at the system-evidence
layer, but a reader holding the two sibling slogans ("every fact carries
provenance" / "every fact carries its time dimension") is given no stated
relation, while §9 carefully situates itself against three *other* docs.
The file's overlaps-on-purpose preamble tolerates the overlap; the header's
"never reached" claim is the part that overstates. *Counsel:* one pointer
line in *Where the neighbouring rules sit* — §6 dates the system's own
facts and claims; §9 is the same instinct for the data the system holds —
and soften "never reached" accordingly.

**TD3 — note — record time bundles three divergent clocks.** "When we
learned it, wrote it, or last confirmed it" are themselves distinct facts
that diverge (learn Tuesday, write Thursday, reconfirm next month), and <!-- datescan:allow: illustrative hypothetical, not a date claim; wrapscan:allow: marker-inflated line -->
staleness computation specifically needs last-confirmed. The bullet's own
collapse argument applies one level down. The sizing test and the
derivation bullet's "when it was established" largely absorb this in
practice, which is why it is a note, not a defect demanding action.
*Counsel:* if touched for TD1/TD2, one parenthetical acknowledging record
time is itself a family, sized by the same question test.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 1 minor · 1 note.**

The principle is sound, correctly placed, honestly grounded, and every
re-runnable claim survived re-running. The findings are additive wording
gaps, not structural defects. Per rule 3 this reviewer decides nothing:
all findings are the principal's to rule on, and all counsel above is
labelled as counsel. Under the close rule, a pass with no MAJOR closes the
cycle once its findings are decided.

## Follow-up checklist

- [ ] Principal rules on TD1 (privacy face of the sizing test) — the one
      finding with fleet-wide propagation weight.
- [ ] Principal rules on TD2 (§6 neighbour line + "never reached" wording).
- [ ] Principal rules on TD3 (note; may reasonably be declined).
- [ ] Venue-guide grounding remains unverified by this pass — verifiable
      only from the owning repo; its retrofit item is that repo's to raise
      (§9 Scope clause), not atelier's.
- [ ] Reconcile section below, after the deferred intent-record references
      arrive.

## Reconcile (post-verdict; phase-1 text above unrevised)

Deferred reference received and read after the verdict was durably written:
the ROADMAP item *PRINCIPLES §9 — the time dimension, and what it now
obliges (Mike, 2026-08-08)*, rulings included. Nothing else in ROADMAP.md
was opened; `docs/sessions/`, `ROADMAP-DONE.md`, and all other verdicts
remain unopened.

**Agreements.** The intent record matches the delta as reviewed on every
point this pass examined: the rule statement, the clause list, both
2026-08-09 rulings (retrofits bind; a result carries its derivation), the
ownership stance (propagate by pointer, no per-child ledger, the
noticing-gap honestly left to evidence), and the no-ADR house pattern — the
record cites API-first and mobile-first as the precedent, and phase 1 had
independently verified both carry inline "decided 2026-07-14" stamps in
PRINCIPLES. The record's dates agree with the landing commits' UTC dates.
The still-open estate consequence matches §9's Scope clause and the
CHANGELOG with no drift in substance.

**Divergences.** One, small but worth naming because TD1 touches the same
clause: the intent record's clause list compresses the hard-delete bullet
to "no hard delete", which is stronger than the doctrine's actual text
("prefer a dated end-state"; erasure a deliberate, recorded act). The
doctrine's hedged form is the honest one. *Post-reconcile addition:* a
reader who meets §9 through this shorthand would read it as banning
deletion outright, which sharpens exactly the retention tension TD1 names —
counsel that if TD1 is accepted, the roadmap shorthand is worth one word of
softening in the same pass; if TD1 is declined, the shorthand is tolerable
index compression with the verbatim rulings held elsewhere.

**What the record reveals about the findings.** Nothing in the intent
record anticipates, seeds, or answers TD1, TD2, or TD3 — the privacy face
of the sizing test is absent from the record too, so TD1 stands as a
genuinely un-anchored finding, and no finding is weakened or answered by
the rulings. Conversely the record surfaces nothing this pass missed: its
one live concern (pointer-delivery may not suffice for a *retrofit*
obligation) is the same openness §9's Scope clause and the CHANGELOG carry,
already weighed in lens 1 and endorsed as honestly left open. One claim
stays unverifiable under the bar: the record says the three ruled items
were harvested verbatim to ROADMAP-DONE.md — that file is barred to this
pass, so verbatim-ness is the principal's or a later session's to spot-check.

**Status after reconcile.** No finding's severity or status changes.
**PASS-WITH-FINDINGS — 0 MAJOR · 1 MODERATE · 1 minor · 1 note** stands.
Verdict finalised.
