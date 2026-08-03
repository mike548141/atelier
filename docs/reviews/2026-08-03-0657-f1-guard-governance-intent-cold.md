# Brief — F1 guard-governance frame, design/intent cold pass (rule 4)

- **Work under review:** Track F / F1 (`docs/ROADMAP.md`) — the guard
  governance frame Mike named 2026-08-02: the three-way decomposition
  (identification confidence · probability of harm · impact of harm), the
  governance vocabulary (DRY policy-as-code · cannot-reduce ·
  acceptance/deferment · false-positive reporting · resolve/scope/soften ·
  side-stepping), and the claim that six open board items are instances of
  one unnamed frame. Records only; nothing built, nothing to diff.
- **Review shape:** design/intent pass per REVIEW.md § *Review the design,
  not only the build* — Mike's explicit ask: run the pass on the **origin
  problem and possible solutions**, ahead of any design; review as an input,
  not a gate. So counsel here may sketch the solution space; per the EI3
  precedent, nothing in it is a pre-ruling — concrete shapes go to Mike at
  build pickup.
- **Spawn provenance (rule 4):** taken from the `⏳` queue by a Fable session
  Mike spawned generically ("do any work that requires Fable, including
  reviews"). The F1 entry's author (the 2026-08-02 2340 Opus session)
  neither started nor instructed this session. The intent record
  (`sessions/2026-08-02-2340-guard-governance-frame.md`) stays unopened
  until the findings below are durably committed; it is read at reconcile.
- **Disclosed exposure:** the mandated onramp (SESSIONS.md tail) included
  that session's index entry — a condensed author account of the frame —
  before this taker could choose not to read it. Named for auditability.
  The E6d entry and the six mapped items were read in the ROADMAP as part
  of locating the queue, which for a records-only delta is unavoidable: the
  ROADMAP is both the queue and the artefact.
- **Load-bearing assumptions to attack**
  1. The three-way decomposition is sound and finer than E6d's two axes in
     a way that matters — not a distinction without a difference.
  2. The six-item mapping is accurate, and complete enough that a model
     built to the frame would cover the board's real cases.
  3. The vocabulary (six concepts) carves the space at its joints — nothing
     load-bearing is missing, none of the six is two things wearing one name.
  4. "Deliberately not pre-solved" is the right shape for the entry — the
     no-steering rule is honoured and the pass has enough to bite on.
- **Scope:** the frame, the mapping, the entry's own claims, and the
  solution space. Non-goals: reversing the standing E6d ruling (Mike kept it
  explicitly — the rebuild is forward work); re-reviewing E6a–E6d's build
  items (they keep their own cycle and the EI rulings).
- **Lenses:** all four; lens 1 carries the weight in a design/intent pass.

---

# Verdict — PASS-WITH-FINDINGS · 0 MAJOR / 2 MODERATE / 1 minor / 3 notes

**Provenance (restated per rule 4):** reviewed by a Fable session Mike
spawned generically; the reviewer authored neither the F1 entry nor anything
in Track E/F. Findings committed before the intent record was opened.

**Grounding re-run, not read:** every anchor the mapping leans on was
re-verified in the live tree — narrow-not-contradict is real
(`REPO-STANDARD.md:130`), resolved-upward is real (`PROPAGATION.md:254`),
C1's `why`+`review-by` machinery is live in `floor.py`, the `⏳` pointer
itself is refs-only as the preamble demands. The mapping's six anchors all
hold. D4's zero-adopters and the fleet claims are dated fleet state, not
re-runnable from this repo alone; taken as dated, not as current.

## Lens 1 — the decomposition survives attack, and it has teeth

**The three-way split is sound, and it is not a distinction without a
difference.** It is, in fact, the canonical structure of mature
vulnerability practice, which E6d's two axes had collapsed: classical risk
is likelihood × impact (axes 2 and 3), and scanner ecosystems bolt detection
confidence on as a separate first axis. Prior art worth importing at build
pickup (verify the specifics then — cited from general knowledge here):
CodeQL grades queries on *precision* (axis 1) separately from
*security-severity* (axis 3); Semgrep rules carry *confidence* and
*severity* as distinct fields; CVSS separates exploitability metrics from
impact metrics, and its **environmental score — the deployer adjusting
severity for their own context — is E6d(ii)'s repo-declared impact, already
named in someone else's standard.** GitHub secret scanning's validity checks
(is this credential *active*) are axis 2 mechanised. The frame is not
idiosyncratic; the estate would be rebuilding toward the state of practice,
which is the right direction to discover mid-rebuild rather than after.

**Where the split earns least:** axis 2 is measurable for credentials
(rotated? expired? test-scoped?) and nearly unmeasurable for the PII half of
the floor's stated intent — there is no "validity check" for an address at
rest. A model that demands three assessments per finding will be ignored;
the affordable form is **undeclared axes default to worst-case**, so the
split costs nothing until someone has grounds to declare otherwise.

## Findings

**FG1 (MODERATE, completeness) — the instance list under-counts, and the
missing instance is the one that would distort the rebuild.** C3 — the
sanctioned adoption path — is not in the mapping, and it is the frame's
sharpest case: first contact between a child and a shared guard it already
fails, resolved twice by documented bypass, recurring on every future
adoption. It is acceptance/deferment *and* sanctioned side-stepping at repo
granularity, and a model rebuilt around steady-state operation only (which
is what the six mapped instances are) will meet adoption as an afterthought
— the same shape as C1's transition spelling. The bootstrapped-with-
`--no-verify` children item is the same instance recorded from the other
end. **P3 sits on the boundary undeclared:** posture-conditioned-on-
visibility is a strictness function over repo properties — if the
governance model does not own "when does a guard tighten", P3 will build a
second original of it. Counsel: map C3 in (as the adoption/first-contact
case), and have the model state whether posture-by-visibility is inside or
outside its scope — either answer works; silence builds the drift.

**FG2 (MODERATE, the consequence the entry left for this pass to say) —
the split does change the response model, and it dissolves rather than
deepens the escalate-only tension.** Admitting axis 2 creates a principled
downward lane: a correctly-identified credential that is provably inert
(rotated, expired, revoked) is the textbook low-probability case. Under
escalate-only that finding blocks forever — and the estate *already* relieves
it, today, through allow-markers and ignore files with reasons. So the
downgrade lane E6d(i) forbids **already exists, spelled as exemption**. The
real invariant underneath Mike's ruling is not direction, it is
**provenance**: the *tool* may never lower a response on its own judgement
(that is where "this one doesn't matter" went wrong before), but a
**declared, reasoned, expiring, principal-visible act** already may — C1
built exactly that machinery. Counsel for the rebuild: replace the
direction-constraint with a provenance-constraint — automatic lowering
forbidden; declared lowering lawful, carrying `why` + `review-by`, because a
downward claim ("this is rotated") is a claim that rots and must re-prove
itself, where an upward move needs no expiry. This keeps everything E6d(i)
was protecting while making the taxonomy honest about what the estate
already does. Both of Mike's positions survive: the ruling was right against
tool-initiated lowering; his doubt was right that the model beneath it was
too coarse to say so.

**FG3 (minor, vocabulary) — granularity is a missing axis, and it is doing
silent work in the entry's own text.** "Declare acceptance or deferment —
today one spelling covers both" is true at *check* granularity only. At
*line* granularity the estate already separates them: an allow-marker with a
reason is pure acceptance (no expiry); an advisory is pure deferment (expiry
mandatory). The distinction Mike wants exists today — by granularity
accident, not design. The estate operates three levels (line: allow-marker ·
check: advisory/disabled · repo: not-wired/adopt-mode), and
resolve/scope/soften mean different things at each. Counsel: make
granularity an explicit axis of the taxonomy, and define acceptance vs
deferment by their real difference — **acceptance is indefinite with a
reason; deferment is temporary with an expiry** — which the one-spelling
ambiguity currently blurs.

**FG4 (note, prior art) — do not invent the vocabulary.** The concepts map
onto terms adopters already know (see lens 1): confidence/precision,
likelihood/exploitability, impact/severity, environmental adjustment,
validity. Building to familiar names is both a correctness check and an
adoption feature for a repo whose stated purpose is to be shareable.

**FG5 (note, no second original) — the false-positive route specialises
resolved-upward.** E1–E4's defect was the missing *operational* route
(where to file, what evidence, who triages), not a missing rule —
`PROPAGATION.md` already owns upward resolution. Per the RL2 discipline,
the model should define the route as a specialisation with a pointer, not
restate the rule.

**FG6 (note, feeds the funded pointer-grammar work) — this item's own `⏳`
pointer is a live boundary specimen.** It carries "Design/intent pass per
REVIEW.md § *Review the design…*" — an instruction to the reviewer, but a
procedural one (pass *type*), not evaluative and not a seeded question. A
detector scoped to "any instruction to the reviewer" flags it; the refs-only
ceiling as written ({delta, intent record, tier}) does not name pass-type as
a lawful field. Recorded so the grammar build decides the boundary on a real
case instead of the three breach instances only.

## Lenses 2–4

**Correctness/honesty of the entry itself:** clean. The standing-ruling
status is stated without spin; the frame/mapping attribution split is
honest; "whether the split changes the response model is the review's to
say" left the load-bearing question genuinely open (FG2 answers it); the
no-steering rule is honoured — no candidate model, no seeded questions. The
"six open items" count is bundle-dependent (E1–E4 as one; Track A closed but
its residue open) and with FG1's additions the true count is higher — noted
under the board's own figures-wrong-both-ways rule, folded into FG1 rather
than counted twice.

**Security & privacy:** records-only delta in a public repo. Manual pass:
the entry adds no new join of a private repo's name to its posture — every
side-stepping fact it cites (C4, Actions-disabled, advisory-never-expires)
was already public in this file, and no repo is named. `/security-review`
discharged with grounds: it reads pending diffs, and the only pending
change here is this brief (the SL2 trap); a records delta has no surface it
can reach.

## Reconcile (intent record opened after the findings were committed)

Nothing overturned; two things sharpened.

- The record names its own feared failure direction: the six-item mapping is
  the agent's synthesis, and "if the mapping is wrong it is wrong in a way
  that makes the frame look better-grounded than it is." **Measured, the
  error ran the other way** — every mapped anchor verified real, and the
  mapping *under*-counts (FG1: C3 and the bootstrap children are missing;
  P3 undeclared on the boundary). The frame is better-grounded than the
  entry claims, which is the good direction to be wrong in.
- The record's EI3 note — Mike's doubt and the E6 reviewer's reservation
  landing on the same soft spot independently — is exactly where FG2 lands
  a third time: three independent hands on the same joint is strong
  evidence the confidence/probability/impact seam is the load-bearing one.
- Carried forward, now for the **fourth** time by the record's own count:
  the `leakscan`-reaches-the-PII-half sweep (flagged 2026-07-29, endorsed
  by the E6 intent pass, unswept). Out of this pass's scope, but a
  companion the F1 rebuild will trip over if it is still undone at pickup.

**Disposition.** 0 MAJOR — no further cold pass is owed on the F1 entry
itself. FG1–FG6 are counsel for Mike's ruling (rule 3); they are input to
the F1 rebuild at pickup, per his review-as-input instruction. The rebuilt
model, when it lands, is self-authored doctrine and queues its own rule-4
pointer as always.
