# Review brief — SECRETS.md access-management expansion + ACCESS.md step-2 line (cold pass)

- **Date/time:** 2026-07-22 1021 UTC
- **Reviewer:** cold-spawned session, branch `atelier-secrets-review`
- **Subject:** delta `caa85fe` — SECRETS.md new sections (replaceability-absolute
  paragraph; one-credential-one-entity-one-system non-reuse rules; asymmetric
  keys graded; minting bar; exposure watch/roll/never-scrub; grounding in public
  practice; what-lives-elsewhere widening) and ACCESS.md step 2's
  minted-fresh-for-this-domain line.
- **Intent record:** `docs/sessions/2026-07-22-1005-secrets-access-doctrine.md`
  — **deferred material**, not opened before the findings below were committed
  (REVIEW.md rules 1–2). No prior review of this delta exists to defer.

## Spawn provenance (REVIEW.md rule 4)

This review was taken from the shared queue (the ROADMAP `⏳` pointer) by an
orchestrator session that Mike opened and pointed at the queue with a generic
"progress any unclaimed work" instruction — the worked example rule 4 names.
Neither Mike's instruction nor the orchestrator supplied any framing, findings,
or account of the work; the delta's author spawned nothing and instructed no
one. This reviewer authored none of the work under review. The queue pointer
carried refs only (delta hash, file/section list, intent-record path), per
rule 4's refs-only ceiling.

## Status of the work

Self-authored doctrine (doctrine by function — REVIEW.md rule 3): the wording
was produced by the agent's judgement, recording Mike's in-conversation rulings
of 2026-07-22. **Findings are Mike's to decide.** Nothing is applied to
`docs/method/` by this review; each finding carries the plain-language
what/why/likely-impact the informed-principal rule requires (00-APEX).

## Scope

Widest the work admits: the intent behind the rulings, the assumptions
under the new rules, the wording as doctrine future agents will obey, its
consistency with sibling doctrine (DATA-PROTECTION, ACCESS, EVIDENCE,
AUTONOMY, REVIEW), the external-grounding claims (NIST SP 800-63B rev 4,
OWASP Secrets Management Cheat Sheet — verified against the live sources,
not from memory), and the mechanical floor re-run at HEAD. No non-goals are
declared; nothing is fenced off.

## Assumptions to attack (named cold, before any deferred material)

1. **"Nothing the target stores or sees can be replayed"** — the asymmetric-key
   grading's load-bearing claim. True of data at rest; is it true of live
   sessions (agent forwarding, in-session abuse)?
2. **"The economics always favour rolling"** — assumes every credential's burn
   costs minutes. Does the doctrine's own honest boundary (master key,
   person-level class) survive contact with the new absolute?
3. **The watch leg's three surfaces** — can the exemplar store class the
   doctrine itself names (sops+age, file-based) actually provide an access
   trail? An unachievable standing duty is silent non-compliance waiting to
   happen.
4. **"No length that isn't simply the platform's maximum"** — is max-length the
   same thing as max-entropy? What about huge caps and silently-truncating
   verifiers?
5. **The citation claims** — does 800-63B rev 4 actually say what the grounding
   section claims (composition rules, blocklists, no scheduled expiry,
   change-on-evidence, final 2025-07-31)? Does the OWASP sheet actually carry
   the audit-trail detail absorbed as the watch leg's third surface? Is the
   "one owned divergence" really a divergence, given NIST's human-password
   scope?
6. **Absolutes vs edges** — "never scrub", "replaceability is absolute",
   "never present the same credential": which edge cases (unpublished history,
   break-glass/outage access, central-auth alternatives) do the absolutes
   quietly run over?
7. **Duplication** — does the new Exposure section restate the pre-existing
   cadence section's loop in a second home (EVIDENCE §9)?

## Lenses

The four REVIEW.md lenses, security/privacy at every altitude — noting this
work *is* security doctrine, so lens 4 is the substance, not an add-on.
`/security-review` reach: this is a landed-delta review of markdown doctrine —
the scanner's exclusions bar the file class, so a run would be definitionally
empty; discharged on those grounds, weighed as nothing (REVIEW.md lens-4
cautions, SL2 grounding).

---

# Verdict

**PASS-WITH-FINDINGS** — 0 MAJOR · 4 MINOR · 4 LOW · 1 nit. The delta is
sound doctrine: correctly grounded, honestly scoped, consistent with its
siblings, and its external citations say what it claims they say (verified
against the live sources). The findings are edge-hardening — places where an
absolute quietly runs over a real operational class, or a corroboration
slightly over-reaches — none overturns a rule's direction. Provenance
restated: this review was spawned by an orchestrator Mike pointed at the
queue; the author spawned nothing, instructed no one, and supplied no framing;
this reviewer authored none of the work.

## Re-runs and verifications (the trail a verdict earns trust by)

- **Scanner floor at HEAD** (this worktree, `9e7e031`): leakscan ✅ clean ·
  secretscan ✅ clean · linkscan ✅ (both changed files) · reviewscan ✅ ·
  sizescan ✅ for both changed files (its one advisory is `ROADMAP.md`
  length, not this delta). Exit codes checked explicitly.
- **Review-line rule**: the doctrine change carries its queued pointer (the
  ROADMAP `⏳` item) — the omission-is-the-bug rule is satisfied.
- **NIST SP 800-63B rev 4** (fetched live): rev 4 confirmed **final
  2025-07-31** (CSRC publication record). Confirmed verbatim-class claims:
  composition requirements "SHALL NOT be imposed"; verifiers "SHALL compare
  the prospective secret against a blocklist" of compromised passwords;
  "SHALL NOT require subscribers to change passwords periodically" but
  "SHALL force a change if there is evidence that the authenticator has been
  compromised". Scope confirmed as human-memorised secrets. **One residual,
  named:** the specific rationale wording the doctrine paraphrases ("forced
  rotation degrades what humans choose next") lives in Appendix A, which the
  fetch could not retrieve; it is the well-attested rationale carried forward
  from rev 3's Appendix A and is consistent with everything the normative
  text says — verified in substance, not to the letter.
- **OWASP Secrets Management Cheat Sheet** (fetched live): centralised
  store ✅, automated rotation ✅, fine-grained least privilege ✅, and the
  audit section confirmed **tamper-resistant** logging including who
  requested/used a secret, when, and attempts to reuse expired secrets —
  exactly the detail SECRETS.md absorbs as the watch leg's third surface. It
  also corroborates never-scrub's cost claim: it warns history rewriting
  "will break any other links to a given commit", with rotation the primary
  remediation.
- **Cross-references**: ACCESS.md step 2 → SECRETS.md section heading matches
  exactly; SECRETS non-reuse → ACCESS step 2 plane-split rule resolves;
  stated-bridge references → DATA-PROTECTION.md exists as claimed; EVIDENCE §8
  (store the rule) says what the pre-existing frame claims.
- **Commit-message claim** "captured on the ROADMAP … (next commit)": verified
  — `958490a` added the gap-analysis item, now claimed `[~]` by a sibling
  worktree.
- **`/security-review`**: discharged, not run — landed-delta review of
  markdown doctrine; the scanner's exclusions bar the file class, so a clean
  pass would be definitionally empty (weighed as nothing), and running a
  pending-changes scanner over a review draft is the SL2-proven hazard.

## Lens 1 — approach & assumptions

The frame is right. Non-reuse argued from blast radius and revocation
independence (not compliance ritual), asymmetric keys *graded* on the actual
verifier-holds-what asymmetry rather than exempted by class, minting argued
from Kerckhoffs, exposure as watch→roll→rehearse with the cadence doing double
duty as the rehearsal — each rule carries its mechanism, which is what makes
doctrine survivable when the platform changes. The "one owned divergence" is
in fact over-owned: NIST's no-scheduled-expiry rule is scoped to
human-memorised passwords, so the machine-secret cadence is outside its scope
rather than contrary to it — and OWASP's automated-rotation recommendation
affirmatively corroborates the cadence. Honest conservatism, not an error
(noted, no finding). The findings below are where assumptions meet edges.

## Findings

Severity: MAJOR (direction wrong or materially overclaims) · MINOR (real gap,
one-clause fix) · LOW (sharpening) · nit. All are Mike's to decide (rule 3);
none has been applied.

### SA1 — MINOR — asymmetric-key grading omits the live-session channel

**What:** the grading rests on "the target holds only the public half, and
nothing it stores or sees can be replayed against another system". True of
data at rest — but a compromised target can abuse a *live* authentication
channel: with SSH agent forwarding (or an equivalent delegated-credential
mechanism) active, the compromised host can authenticate onward to any system
the fleet-wide key opens, without ever holding the key. **Why it matters:**
the sentence is the load-bearing justification for accepting one key across
many systems; as written it overstates the isolation, and a reader could
conclude a compromised target gains nothing toward the rest of the fleet.
**Likely impact if unfixed:** agents/adopters enable agent forwarding to
convenience a hop-through workflow, believing the doctrine says the fleet-wide
key makes that safe — precisely the case where one compromised box reaches
everything. **Suggested shape of fix (Mike's call):** one caveat line in the
residual-duties sentence — no delegated use of the key through untrusted
systems (no agent forwarding to hosts you don't control), and
presence-confirmation (touch-to-sign) where hardware backing offers it.

### SA2 — MINOR — the watch leg's third surface is unachievable on the doctrine's own exemplar store

**What:** the watch leg names "the secret store's own access trail (who
resolved which secret, when)" as a standing surface, and warns "a store that
can't account for its reads can't tell you a secret was taken". But the store
class this file itself names as the exemplar ("e.g. sops+age", What lives
elsewhere) is file-based: decryption is offline, and no read trail exists or
can be retrofitted. **Why it matters:** the doctrine's own discipline (the
stated-bridge rule it cites twice in this very delta) says an unmeetable duty
must be a named debt, never silent; as written, every sops/age-class adopter —
likely most of this doctrine's audience — inherits a standing duty they
cannot perform, with no bridge language. The delta's own words name the
failure mode: a duty "that exists only as prose is a hope". **Likely impact
if unfixed:** the third surface is silently skipped fleet-wide, and the
watch-leg claim quietly over-promises. **Suggested shape of fix:** qualify —
"where the store can provide one; a file-based store that cannot is a named
limitation (stated bridge), weighed when choosing store technology".

### SA3 — MINOR — the minting rule conflates maximum entropy with maximum length

**What:** "machine-minted at the maximum entropy the technology accepts" is
the right bar, but the operative clause "no length that isn't simply the
platform's maximum" hard-codes max-*length* as the rule. **Why it matters:**
entropy saturates — beyond ~128 bits of randomness, added length buys no
security — while pathological lengths carry real costs: platforms with huge or
unbounded caps (thousands of characters), and verifiers that silently
truncate (bcrypt-class verifiers ignore everything past 72 bytes, so the
"extra" length is imaginary — the effective secret is shorter than the
recorded one, and the record now misstates what authenticates). The
doctrine's own Kerckhoffs framing argues for entropy-sufficiency, not a
length fetish. **Likely impact if unfixed:** agents minting absurd values
where caps are huge; worse, a truncating verifier makes the stored value and
the effective credential diverge — a small, silent integrity lie in the
store. **Suggested shape of fix:** state the bar as entropy — machine-mint at
the platform's maximum *up to entropy sufficiency* (a named threshold, e.g.
128 bits), with the platform's cap governing below that point; where a
verifier truncates, the *effective* length is the cap and is recorded as
such.

### SA4 — MINOR — no break-glass / store-unreachable class

**What:** the doctrine covers store-resolved machine secrets and explicitly
excludes person-level credentials, but a third class sits between them and is
unaddressed: credentials a human must transcribe during an outage when the
store may be unreachable — the OOB console password, the switch serial-line
login mid-network-incident, the hypervisor root when the store's own host is
down. **Why it matters:** for that class, a max-entropy max-length string is
genuinely hostile to the recovery path (transcription from a phone screen at
2 am), and the temptation the doctrine doesn't name is exactly the one it
exists to kill: a human "memorable" scheme. Standard practice for the class is
still machine-minted, still schemeless, but transcription-optimised (a
generated word-sequence passphrase). The minting rule as written forbids that
trade-off — a use-imposed constraint is not a "technology-imposed cap".
**Likely impact if unfixed:** either the recovery path degrades, or operators
quietly deviate — un-named deviation being the defect the stated-bridge
discipline exists to prevent. Note the store's own reachability during
incidents is the same edge, one level up — the honest boundary covers the
master key's *loss*, not the store being unreachable while its host is down.
**Suggested shape of fix:** name the break-glass class — machine-minted,
transcription-format, stated as a bridge with its constraint recorded, per
platform, instance-local — or explicitly rule it out of scope alongside
person-level credentials so the silence is a decision, not a gap.

### SA5 — LOW — the NIST screening corroboration slightly over-reaches

**What:** the grounding bullet claims "screen-against-breached-lists
corroborates the watch leg". NIST's blocklist requirement is a
*creation-time verifier* duty (check the prospective password when it is
set), not standing exposure monitoring; the watch leg is an ongoing duty.
**Why it matters:** the grounding section's whole value is precision —
corroboration named, divergence owned — so a citation doing slightly more
work than the source supports is the one defect the section can't afford.
Ongoing screening is real practice (platform-offered breached-credential
monitoring), just not what 800-63B mandates. **Suggested shape of fix:**
attribute creation-time screening to NIST and ongoing screening to platform
practice, or soften "corroborates" to "is the same mechanism at mint time".

### SA6 — LOW — "never scrub" heading is broader than its own body

**What:** the body is careful — "*published* history", rollable credentials,
"dead text" — but the heading and closing line are absolute. Two edges the
absolute runs over: (a) *unpublished* local history, where amending away a
just-committed secret before push costs nothing (no clones diverge, no
signatures break) and is routine; (b) residue that is not a rollable
credential — a leaked private key whose past captured traffic lacks forward
secrecy, or personal data, where "roll it and the corpse is dead" doesn't
hold (the personal-data case is DATA-PROTECTION's, but nothing here points
there). **Likely impact:** low — but doctrine absolutes get quoted out of
their body's qualifiers. **Suggested shape of fix:** one scoping line:
never scrub *published* history *of rolled credentials*; pre-push history is
fair game, and non-credential residue is `DATA-PROTECTION.md`'s problem.

### SA7 — LOW — the exposure section and the cadence section now share a fact across two homes

**What:** pre-existing "Rotation cadence" closes with the full loop
("detect → rotate immediately on any suspicion → rotate on cadence");
the new Exposure section restates the first two legs at higher resolution
("watch" / "roll on confidence, not proof"). Same rule, two homes, two
phrasings ("suspicion" vs "credible risk") — EVIDENCE §9's one-fact-one-home
tension, inside the very file. Not a contradiction; a drift risk. **Suggested
shape of fix:** make the cadence section's loop line point into the Exposure
section (or vice versa) so one of them owns the wording.

### SA8 — LOW — the non-reuse section doesn't name central auth as the stronger resolution

**What:** the per-switch example resolves fleet reuse by minting per-device
local secrets. Where the platform supports central/federated auth
(RADIUS/TACACS-class), the stronger move is eliminating device-local secrets
entirely — which the delta's own secure-defaults bullet ("stronger
authenticator class — take it by default") implies but the non-reuse section
never points to. **Likely impact:** an adopter reads the non-reuse section in
isolation and builds per-device password plumbing on a platform that offered
central auth. **Suggested shape of fix:** one pointer line from the
across-systems bullet to the secure-defaults ladder.

### SA9 — nit — "artifact" (US) in a NZ-English repo

The new asymmetric-keys section writes "irreplaceable artifact".
CONVENTIONS.md mandates NZ English ("artefact"); REVIEW.md itself uses both
spellings and pre-existing SECRETS.md text already carried "artifact", so the
delta followed local precedent — the inconsistency is repo-wide and
pre-existing, merely extended by one instance. Sweep-class fix, not urgent.

## Lens 2 — correctness & quality (beyond the findings)

- Every ruling in the commit message is present in the text — nothing claimed
  as landed is missing, nothing landed is unclaimed. The commit message's
  deliberate exclusion (wider secure-SDLC practice) is real and tracked
  (ROADMAP gap-analysis item, verified above).
- Attribution discipline is clean: each new rule is stamped "Mike's rulings,
  2026-07-22" — the doctrine distinguishes decided practice from invention,
  per the ground-everything constraint.
- The privilege-split paragraph's boundary test ("don't multiply credentials
  that would only ever be used together") is the right guard against the
  rule's own failure mode (credential sprawl). Good.

## Lens 3 — completeness / harvest (beyond the findings)

- ACCESS.md step 2's insertion composes correctly with its existing
  two-scoped-credentials text — the minted-fresh line and the plane-split
  are distinct duties and now both live at the onboarding moment, which is
  where the commit message says reuse tempts. Sound placement.
- The What-lives-elsewhere widening (imposed caps instance-local) closes the
  loop the minting section opens. No orphaned rule.

## Lens 4 — security & privacy

The delta *is* lens-4 subject matter, and the review above is substantively
this lens. Delta-specific checks: no literal example secrets or house values
in the new prose (leakscan/secretscan clean at HEAD, exit codes checked);
the examples are generic (a switch rack, a 30-character cap); nothing reveals
estate topology beyond the already-public store-class mention that predates
the delta. Publishing house *shape* rules in a public repo is priced by the
delta's own Kerckhoffs argument: the minting format is publishable at zero
cost — the doctrine's publication is self-consistent with its content.
`/security-review` discharge stated in the re-runs section.

## Author-position section

None found on the record within this review's non-deferred material — the
queue pointer was refs-only, as rule 4 requires. (Reconcile note below covers
the intent record.)

---

## Reconcile (deferred material opened only after the findings above were committed)

Opened after commit `[see brief-commit hash in log]`: the intent record
`docs/sessions/2026-07-22-1005-secrets-access-doctrine.md`. No prior review
of this delta exists.

*(Reconcile findings appended below after reading.)*
