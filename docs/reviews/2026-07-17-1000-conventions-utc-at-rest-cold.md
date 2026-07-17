# Cold review — CONVENTIONS.md + the UTC-at-rest ADR

**Scope:** commits `67e8582` (doctrine) + `198cf32` (fidelity fixes) — the new
`docs/method/CONVENTIONS.md` (the default-frame rule: declare a default once at
the boundary and it carries silently; label only a deviation or a collision;
foreign-data preservation outranks normalisation) and ADR
`docs/decisions/2026-07-15-1327-timestamps-utc-at-rest.md` (timestamps UTC at
rest, local on presentation; record identifiers UTC-forward; ELT not ETL).
Review both files whole at HEAD plus the deltas, and their consistency with
the sibling docs that already carried frame rules (`method/RECORD.md`'s
coordination-free identifiers, `method/SIGNING.md`'s `Z`-anchoring,
`CLAUDE.md`'s conventions pointer). This is method-layer doctrine; children
inherit it by pointer, and the repo is public.

**Sequencing (REVIEW.md rules 1–2):** (1) read this brief **only above the
first `---` divider** (use a limited read); (2) review both docs at HEAD plus
the deltas, naming and attacking the load-bearing assumptions yourself, and
**write your attack surface durably into the verdict section of this file
first**; (3) only then open the deferred section below the divider, and the
intent record `docs/sessions/2026-07-15-1327-conventions-default-frame.md`
(the author's account — reconcile, never anchor). Name any residual exposure
rather than denying it.

**Spawn provenance (rule 4):** this brief is written by a **non-author** — a
fresh session the principal opened and pointed at the queue ("do any review
work"); the author session (Opus, intent record above) neither started nor
instructed the taking session or this reviewer. The reviewer is a cold spawn of
the taking session. One disclosure: the ROADMAP `⏳` pointer the taking session
read carried four seed questions (reproduced in the deferred section) — a
refs-only pointer is the spec; the exposure is named, not denied. The verdict
must repeat this provenance.

**This is self-authored doctrine (by function):** all findings are the
principal's to decide (rule 3) — record counsel per finding, labelled as the
reviewer's counsel; apply nothing.

**Re-run live proofs in scope:** the delta claims floor green (247 tool tests ·
sizescan · linkscan · scan triad) and that the ADR's own `1327` UTC identifier
against a local 2026-07-16 clock is the rule dogfooding itself. Re-run what
falls in scope; verify the dogfood claim rather than reading it.

**Run all three lenses** (approach & assumptions · correctness/honesty ·
completeness/harvest), deep not fast; findings get stable IDs (F1…) with
severity MAJOR/MEDIUM/LOW. Append your verdict to this file below the second
`---` divider.

---

## Deferred — seeded questions (open only after your attack surface is committed)

Carried from the author's ROADMAP pointer:

- Q1. Does the label rule's ~99%/exception split stay honest, or does it invite
  over-labelling?
- Q2. Is the foreign-data precedence grounded or padded?
- Q3. Do the declared defaults leak anything person-local into a public repo?
- Q4. Does "UTC-forward identifiers" cohere with RECORD's coordination-free
  rule?

---

## Verdict — cold review (Fable 5, 2026-07-17, ~1005 UTC)

**Spawn provenance (repeated per rule 4):** this brief was written by a
non-author — a fresh session the principal opened and pointed at the queue
("do any review work"); the author session (Opus, intent record) neither
started nor instructed the taking session or this reviewer. The reviewer is a
cold spawn of the taking session. The taking session's disclosed exposure: the
ROADMAP `⏳` pointer it read carried four seed questions, reproduced in the
deferred section.

**Reviewer's own exposure, disclosed:** while locating the verdict divider I
ran `tail -4` on this file and saw the final line of the deferred section —
seed Q4 ("Does UTC-forward identifiers cohere with RECORD's coordination-free
rule?"). One line, seen *after* my attack surface below was already formed in
working notes (the RECORD/CONCURRENCY coherence question was independently on
it — see A1), but before this durable write; named, not denied. Nothing else
below the first divider, and not the intent record, has been opened at the
time of this section's writing.

### Attack surface (formed before reading the deferred section or intent record)

- **A1 — Operationalisation vs lockstep.** The ADR changes what a record
  identifier *means* (`HHMM` now UTC). The sites an executor actually reads
  when minting one — `method/RECORD.md`, `method/CONCURRENCY.md`,
  `build/REPO-STANDARD.md`, the child templates — all still say "start time,
  24-hour" with no zone and no ADR pointer. Does that violate RECORD's own
  docs-as-code lockstep rule, and will children predictably mint local stamps?
- **A2 — Is the dogfood claim verifiable or self-reported?** Re-derive the
  arithmetic (13:27 UTC 2026-07-15 vs NZ wall clock) and test it behaviourally
  against post-boundary identifiers vs their commit times.
- **A3 — Label-strength consistency.** CONVENTIONS' table row says "local +
  labelled on presentation"; the ADR softens to "labelled when the zone could
  be doubted". Same rule at two strengths — which is canonical?
- **A4 — Grounding of the foreign-data/ELT clause.** The estate has no live
  ingestion surface; is clause 3 extracted from decided practice or invented
  to fill a heading (the repo's own hard constraint)?
- **A5 — The sorting claim.** "Sorts correctly across zones" holds only within
  a single regime; mixed local/UTC identifiers straddle the boundary — is the
  residual named at true strength?
- **A6 — Day-granularity prose dates.** A bare date in prose is now a UTC
  date; NZ mornings are the previous UTC day. Highest-frequency silent-break
  case — does any doc call it out?
- **A7 — Enforcement honesty.** No scanner can verify zone-correctness of a
  stamp; does the doctrine state its enforcement floor honestly (PROPAGATION's
  clause), or imply a mechanical hold it doesn't have?
- **A8 — Fidelity of the retold CI scar.** Does CONVENTIONS' "CI clock reading
  a local timestamp as UTC, rejecting every signed commit" match SIGNING's
  first-hand account?
- **A9 — Roles-not-instances.** Is "UTC at rest" itself a role or an instance?
  Could a peer adopter legitimately substitute a different canonical zone, and
  does the doc's substitution note cover time or only currency/locale?

*Live proofs re-run before this write (results in findings below): 247 tool
tests OK; sizescan, linkscan, leakscan, licenscan, secretscan all clean at
HEAD (325011b + 3 untracked briefs); post-boundary identifier behaviour
checked against commit times.*

### Reconciliation with the deferred section + intent record (opened after the attack surface above)

Seed Q4 = my A1; Q2 = my A4; Q1 folds into my A3. **Q3 (person-local leak) was
not on my surface** — answered under lens 2 below. The intent record confirms
rather than reshapes the findings: its four Mike-refinements ground clauses
1–3, its delivery notes explain the 6.6 h stamp-to-commit gap (session-limit
pause + reboot), and — decisive for F1 — its "Owed" section queues only this
cold review: no follow-up exists for the minting-site docs, so F1 is an
unacknowledged gap, not a stated deferral.

### Live proofs — re-run, not read

- **Suite:** `python3 -m unittest discover -s tools` → **Ran 247 tests, OK**
  (matches the claimed count exactly).
- **Scans at HEAD (`325011b` + the 3 untracked briefs):** sizescan ✅ ·
  linkscan ✅ · leakscan ✅ · licenscan ✅ · secretscan ✅ — all clean.
- **Dogfood claim, verified:** 2026-07-15T13:27Z = 2026-07-16T01:27 NZST — the
  local wall clock did read 07-16 while UTC read 07-15; arithmetic holds. The
  delivering commit `67e8582` (2026-07-16T08:06+12:00 = 2026-07-15T20:06Z)
  postdates the stamp, as it must. The stamp's exact minute is
  self-reported and independently unverifiable — but the *regime* verifies
  behaviourally: every post-boundary identifier read as UTC lands 1–41 min
  before its own commit (2026-07-16-1013 → committed 10:14Z; 2026-07-17-0810/
  0908/0946 → 08:51Z/09:09Z/09:47Z; the taking session's own briefs stamped
  1000 → claim commit 09:59Z), whereas read as local they'd trail by ~12 h.
  The rule is live practice, not just a claim.

### Lens 1 — approach & assumptions

The three-clause shape (declare-once · label-deviation-or-collision ·
precedence-on-conflict) is sound and well-grounded: each clause traces to a
dated principal refinement, and the ~99% figure is honestly flagged as a rule
of thumb with both failure directions (silent deviation, over-labelling)
named — Q1 answered: it stays honest. Two-artifact split (general rule +
worked instance) is the right altitude. The weak assumption is A1: the
doctrine assumes declaring the default at CONVENTIONS.md reaches executors,
but identifier-minting is directed by *other* docs that still describe the
old regime (F1). Enforcement is stated at true strength — no doc pretends a
scanner can hold zone-correctness (A7 clean).

### Lens 2 — correctness & honesty

Retold history is faithful: CONVENTIONS' CI-scar summary matches SIGNING's
first-hand account (A8 clean); "exactly the stance the identifier migration
took" matches ADR 2026-07-13 and its addendum. The dogfood claim verifies (see
above). **Q3: no person-local leak** — the declared defaults reveal only
locale (NZ), already public repo-wide (git identity, +12:00 offsets,
pre-existing NZ-English line); no health/family/financial/estate detail;
leakscan re-run clean. The 198cf32 fidelity fixes check out: CLAUDE.md now
genuinely points at CONVENTIONS.md, and clause 3 carries both ELT reasons.

### Lens 3 — completeness & harvest

The change is complete *within* the two files and their two indexes, but
incomplete across the doc graph it governs — the identifier-semantics change
never reached the sites that direct minting (F1), the prose-date corollary is
unstated (F3), and RECORD's absolute-dating section — a sibling frame rule —
is un-cross-referenced in either direction (folded into F3 counsel).

### Findings

**F1 — MAJOR — the identifier-minting sites still describe the old regime.**
The ADR redefines record-identifier semantics (`HHMM` from `date -u`), but
every doc an executor actually reads when naming a record still says "start
time, 24-hour" with no zone and no ADR pointer: `docs/method/RECORD.md:67`,
`docs/method/CONCURRENCY.md:108`, `docs/build/REPO-STANDARD.md:111`,
`docs/build/templates/CLAUDE.md:38`,
`docs/build/templates/docs/decisions/README.md:12`,
`docs/build/templates/docs/reviews/README.md:24`. By RECORD's own lockstep
rule ("the doc that governs a thing changes in the thing's commit… or the doc
is a lie the moment it merges") these went stale in `67e8582`. The child chain
is the sharp edge: children receive the compressed rule via the template
doctrine block and CONCURRENCY — neither carries UTC — so a child session
minting `date +%H%M` local is the predictable outcome; atelier's own
compliance (verified above) rests on author-session memory, not the record.
*Reviewer's counsel:* one small commit adding ", UTC (`date -u`) — ADR
2026-07-15" at each of the six sites; the two templates matter most, since a
child never reads atelier's ADRs.

**F2 — LOW — label-strength mismatch between the table and the ADR.**
CONVENTIONS' Time row says "local + labelled on presentation" (reads as
always-label); the ADR says labelled "when the zone could be doubted — not
tattooed on every value". A reader citing only the table will over-label —
the failure mode the doc itself warns against. The resolution the ADR gestures
at (at the presentation layer the reader's own zone is the shared default, so
silent is safe) is never stated. *Reviewer's counsel:* align the row to
"local on presentation, labelled where doubtable", or state the per-layer
default explicitly in the ADR.

**F3 — LOW — the prose-date corollary is unstated.** "Every timestamp atelier
authors… is UTC" implies a bare prose date is now a *UTC* date, but neither
doc says so, and RECORD's absolute-dating section (the rule governing prose
dates, EVIDENCE §7) is un-cross-referenced. NZ mornings are the previous UTC
day, so a morning session naturally writes a local date that mismatches its
own UTC identifier — the highest-frequency silent break the rule will meet.
*Reviewer's counsel:* one sentence in the ADR's consequences ("the absolute
date in prose is the UTC date") plus a pointer in RECORD §absolute-dating.

**F4 — LOW — foreign-data clause grounded but instance-less, unmarked.**
Q2 answered: clause 3 / the ADR's ELT bullet is *grounded* — the intent record
traces it to Mike's explicit precedence ruling — so it is not padding. But it
is the one clause with no live instance in the estate (no ingestion surface
exists), stated in operational present tense ("Foreign-data ingestion must
carry a zone-metadata field") with no marker, unlike SIGNING's deferred-layer
pattern (stated trigger). *Reviewer's counsel:* a half-line "no live
ingestion surface yet; the first one is this clause's proving ground" keeps
the stub-honestly ethos intact.

**F5 — LOW — the cross-zone sorting claim is stated one notch too strong at
the boundary.** "It sorts correctly across zones" holds within the UTC
regime; the ADR names mixed local/UTC coexistence "as designed" but not its
concrete consequence — near the boundary a UTC key can sort *before* a local
key minted earlier in real time (this ADR's own 07-15 filename against any
local 07-15 afternoon stamp is the worked example). Implied, never stated.
*Reviewer's counsel:* one clause in the consequences naming boundary-era sort
inversion as accepted.

### Verdict

**PASS-WITH-FINDINGS** — 1 MAJOR · 0 MEDIUM · 4 LOW. The doctrine is sound,
honestly grounded in dated principal rulings, and verifiably live (floor
green at 247/247; the UTC regime confirmed behaviourally across every
post-boundary identifier). The MAJOR is not in what the two files say but in
where the saying stopped: the rule changed what a record identifier means and
never reached the six docs that direct the minting — atelier's own lockstep
rule, applied to itself. All findings are the principal's to decide; nothing
has been applied.

*Reviewed by a cold spawn (Fable 5), 2026-07-17 ~1015 UTC. Files touched:
this brief only (appended). No commits, no pushes.*

---

## Addendum — principal-raised finding (2026-07-17, post-verdict)

Raised by Mike while reading this verdict; elaborated and recorded by the
taking session (not the reviewer), labelled as such. The decision is his, with
the F1–F5 batch.

**F6 — LOW — the "ISO 8601" table row declares a standard the estate
deliberately profiles, without saying so.** Strict ISO 8601 separates date and
time with `T` (`2026-07-16T15:06` extended, `20260716T1506` basic; a space is
RFC 3339's readability concession, not ISO), and a value with no zone
designator means *local* time. The estate's actual shapes, checked at HEAD:
machine-authored timestamps are strict ISO (`toISOString()` → `T`+`Z`, e.g.
ccarchive's manifest); record identifiers are a filename-safe key profile
(`YYYY-MM-DD-HHMM`, hyphen standing in for `T`, no colon — `:` is illegal or
hostile in filenames, zone carried by the UTC-at-rest default); prose stamps
are space-separated and labelled (`0958 UTC`); SIGNING's
`valid-after="20260711Z"` is ssh-keygen's own foreign syntax, kept as-is. The
CONVENTIONS row ("ISO 8601 — `YYYY-MM-DD`, 24-hour, `Z` for UTC") declares
none of this, so by the doc's own rule the identifier and prose shapes read as
*unlabelled deviations* from the declared default — the anti-pattern the doc
names, in its own table (same family as F2's label-strength mismatch).
*Taker's counsel:* rewrite the row as a declared profile, one line per shape —
strict ISO 8601 with `T` and `Z` for machine-authored timestamps; the
`YYYY-MM-DD-HHMM` key profile for record identifiers (hyphen for `T`, zone
from the UTC-at-rest default); date + `HHMM UTC` in prose; foreign formats
(ssh-keygen) kept as-is under clause 3. That is declare-once with named
deviations — the rule the doc itself teaches.

---

## Decision — 2026-07-17, ruled by Mike (principal)

Mike ruled **F1–F6 all [fixed] as counselled** (F1–F5 "make all the changes as
you counselled" after a plain-language walk-through; F6 is his own finding,
raised and ruled in the same exchange). Applied the same day by the taking
session (authored neither the doctrine nor this verdict). What was applied:

- **F1 (MAJOR)** — the six identifier-minting sites now state UTC (`date -u`)
  with the ADR pointer: `RECORD.md`, `CONCURRENCY.md`, `REPO-STANDARD.md`, and
  the three child templates (`templates/CLAUDE.md` via the canonical block in
  `PROPAGATION.md` — both edited together, drift test green; decisions and
  reviews README templates). Children pick it up at their next pin bump.
- **F2** — the Time row now reads "local on presentation, labelled where
  doubtable", aligned with the ADR's strength.
- **F3** — ADR addendum: a bare prose date is a UTC date; RECORD's
  absolute-dating section states it and points at the ADR.
- **F4** — clause 3 carries the honest marker: no live ingestion surface yet;
  the first is the clause's proving ground.
- **F5** — ADR addendum names boundary-era sort inversion as accepted.
- **F6 (principal-raised)** — the "ISO 8601" row rewritten as the declared
  house profile: strict ISO with `T`+`Z` for machine-authored timestamps; the
  `YYYY-MM-DD-HHMM` filename-safe key shape for record identifiers (hyphen for
  `T`, zone from the UTC-at-rest default); `YYYY-MM-DD` + `HHMM UTC` in prose.

The ADR itself changed only by dated addendum (the lifecycle's append-only
verb); the decision is unchanged. Verified after applying: 247 tool tests
(template drift test green) · sizescan · linkscan — all green.

**1 MAJOR at the pass ⇒ the cycle stays open:** the applied batch's cold pass
is queued `⏳` in the ROADMAP for a non-author to take (the applier queues,
never spawns — rule 4 applied to the application).
