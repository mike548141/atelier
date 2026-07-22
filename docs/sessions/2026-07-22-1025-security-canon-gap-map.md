# 2026-07-22 · 1025 UTC · Security canon vs method/ — gap map (records-only)

Landing evidence for ROADMAP *"Security doctrine vs public good practice — gap
analysis"*, item *"Map the public canon against `method/` + the scanner floor"*
(claimed 2026-07-22-1018, wt: atelier-sec-gap-map). The credentials slice
already landed (SECRETS.md "Grounding in public practice", `caa85fe`); this is
the doctrine-wide sweep.

**Scope discipline.** This record *maps* — it proposes doctrine seams but edits
no `docs/method/`. Every "already held" claim below was verified by reading the
cited doc, not by trusting the ROADMAP list. Corroboration is named as
corroboration; a gap I could not confirm stays labelled candidate. Proposals are
labelled proposals for a future session; the doctrine-edit work earns its own
review (ROADMAP: *review WARRANTED when the mapping moves to doctrine edits*).

---

## 1. Canon source → where held in atelier (verified) or gap

Legend: ✅ held (doc named, read) · ⚠️ partial / framed differently · ❌ gap
(→ §2 candidate) · 🔒 instance-layer by design (correctly not in this shareable
repo).

### NCSC "Secure development & deployment" — 8 principles

| # | Principle | atelier | Where (verified) |
|---|---|---|---|
| 1 | Secure development is everyone's concern | ✅ | REVIEW.md lens 4 "a must on every review, not a specialist add-on"; PRINCIPLES §5 "design inputs from the first line" |
| 2 | Keep security knowledge sharp | ⚠️ | Implicit — REVIEW lens 4 mandates consulting open catalogues (OWASP Top 10/ASVS) "checked, not recalled". No standalone training practice (out of scope for a solo/agent operating model) |
| 3 | Produce clean & maintainable code | ✅ | PRINCIPLES §2 (KISS/DRY, loose coupling, Unix), §6 (legibility). "Complexity is the enemy of security" = §2 KISS verbatim in spirit |
| 4 | Secure your development environment | 🔒 | Instance-layer — TOOLBOX.md keeps the tool/credential manifest machine-local; ACCESS.md onboards domains. Dev-env hardening itself is estate context, not shareable doctrine |
| 5 | Protect your code repository | ✅ | ADR 0007 SSH commit/tag signing (**active** 2026-07-12, SIGNING.md); the scanner floor (secretscan/leakscan on push); AUTONOMY push floor |
| 6 | Secure the build & deployment pipeline | ⚠️ | Signing + floor scanners in CI (ci.yml) hold most of it; **residual: third-party GitHub Actions pinned by mutable tag, not SHA** → §2 gap C |
| 7 | Continually test your security | ✅ | Floor scanners gate every commit; REVIEW.md folds `/security-review` in as the mechanical floor under lens 4 |
| 8 | Plan for security flaws | ⚠️ | Credential-exposure case fully held (SECRETS.md watch→roll→never-scrub); general vuln capture-and-track rides generic REVIEW→ROADMAP, unframed → §2 gap E |

### NIST SSDF (SP 800-218) — 4 practice groups

| Group | atelier | Where (verified) |
|---|---|---|
| **PO** Prepare the Organization | ✅ | 00-APEX + all of method/ *is* the prepared process; PRINCIPLES §5 sets security as a design input |
| **PS** Protect the Software | ✅ | ADR 0007 signing (integrity/provenance); secretscan (no creds in history); RECORD append-only + never-rewrite-history |
| **PW** Produce Well-Secured Software | ⚠️ | PW.1 design-to-mitigate = PRINCIPLES §5 + REVIEW design-review, but **no named threat-modelling step** → §2 gap A; PW.5/PW.6 secure coding = PRINCIPLES §1 fail-fast validation + REVIEW lens 4 (→ §2 gap D, mostly dismissed) |
| **RV** Respond to Vulnerabilities | ⚠️ | Credential path held (SECRETS exposure runbook); general residual-vuln identify/track/prevent-recurrence unframed → §2 gap E |

### OWASP SAMM — 15 practices across 5 functions

| Practice | atelier | Where (verified) |
|---|---|---|
| Governance: Strategy/Policy/Education | ✅/⚠️ | Policy = all of method/; Education not a formal practice (see NCSC 2) |
| Design: **Threat Assessment** | ❌ | → §2 gap A |
| Design: Security Requirements | ✅ | PRINCIPLES §5, precedence rule 4 "hold the security posture — right-sized" |
| Design: Secure Architecture | ✅ | PRINCIPLES §2 (swappable seams, security-critical held to §5), §5 Zero Trust |
| Implementation: Secure Build | ⚠️ | Zero-dep ethos (tools/README, ADR 0007) shrinks the surface; dependency screening → §2 gap C |
| Implementation: Secure Deployment | ✅ | Signing + floor gate the push/publish boundary; licenscan pre-publish |
| Implementation: **Defect Management** | ⚠️ | REVIEW findings → [fixed]/[backlog]/[rejected] → ROADMAP; security-defect triage unframed → §2 gap E |
| Verification: Architecture Assessment | ✅ | REVIEW.md "review the design, not only the build"; lens 1 approach & assumptions |
| Verification: Requirements/Security Testing | ✅ | Floor scanners + `/security-review` (REVIEW lens 4); tool selftests/unittests |
| Operations: **Incident Management** | ⚠️ | Credential-exposure runbook held (SECRETS); general incident/disclosure posture → §2 gap E |
| Operations: Environment/Operational Mgmt | 🔒 | Instance-layer (the estate itself; ros/docker-heap), not this repo |

### OWASP ASVS — chapters (v4.0.3 stable; v5.0 2025 reorg, ch.1 now Encoding & Sanitization, verified live)

| ASVS domain | atelier | Where (verified) |
|---|---|---|
| V1 Architecture, Design & **Threat Modeling** | ❌ | → §2 gap A |
| V2/V3 Authentication, Session | ✅ | SECRETS.md triad + non-reuse + minting; ACCESS.md onboarding; NIST 800-63B grounding |
| V4 Access Control | ✅ | SECRETS privilege-split (sudo shape); ACCESS.md rings; PRINCIPLES §5 Zero Trust least-privilege |
| V5 Validation, Sanitization & Encoding | ⚠️ | PRINCIPLES §1 fail-fast/strict-schema/canonicalising validators; REVIEW lens 4 (injection/XSS). Concrete encoding rules 🔒 → §2 gap D |
| V6 Stored Cryptography | ✅ | SECRETS.md machine-mint at max entropy, Kerckhoffs on shape; age/sops encrypted-at-rest |
| V7 Error Handling & Logging | ✅ | PRINCIPLES §6 observable-by-design (silent success = defect); SECRETS watch leg (store audit trail) |
| V8 Data Protection | ✅ | DATA-PROTECTION.md (whole doc); precedence rule 1 |
| V9 Communication | 🔒 | Instance-layer (Cloudflare/traefik/TLS in docker-heap), not shareable doctrine |
| V10 Malicious Code / dependencies | ❌ | → §2 gap C |
| V11 Business Logic | ✅ | REVIEW lens 1 (right problem, right way); PRINCIPLES §4 idempotent/convergent |
| V12/V13 Files, API | ✅ | PRINCIPLES §2 API-first, machine-readable twin, exit-code contracts |
| V14 Configuration | ⚠️ | Secure-defaults for access/failure held (fail-safe→deny, SECRETS deny-by-default); generalised config secure-defaults → §2 gap B |

### CIS Controls v8.1 — 18 controls (safeguards, not dev-doctrine; mapped where relevant)

| CIS | atelier | Note |
|---|---|---|
| 2 Software Asset Inventory · 7 Continuous Vuln Mgmt · 15 Service Provider | ❌ | Dependency/component screening → §2 gap C |
| 3 Data Protection | ✅ | DATA-PROTECTION.md |
| 4 Secure Configuration | ⚠️ | → §2 gap B |
| 5/6 Account & Access Mgmt | ✅ | SECRETS.md + ACCESS.md |
| 8 Audit Log Mgmt | ✅ | SECRETS watch leg (store access trail); PRINCIPLES §6 provenance |
| 16 Application Software Security | ⚠️ | Covered by REVIEW + floor + PRINCIPLES; SDLC-security = this whole sweep |
| 17 Incident Response | ⚠️ | → §2 gap E |
| 1, 9–14, 18 (asset/network/malware/pentest) | 🔒 | Estate-operations controls, instance-layer — not a doctrine repo's scope |

### OWASP Proactive Controls 2024 (C1–C10) & Cheat Sheet Series

C1 access control ✅ · C2 crypto ✅ (SECRETS) · **C3 validate input** ⚠️→gap D ·
C4 security-from-start ✅ (PRINCIPLES §5) · **C5 secure-by-default** ⚠️→gap B ·
**C6 keep components secure** ❌→gap C · C7 secure identities ✅ (SECRETS) ·
C8 browser security 🔒 (no browser surface yet) · C9 logging/monitoring ✅
(PRINCIPLES §6, SECRETS watch) · C10 SSRF 🔒 (no server surface yet). The Cheat
Sheet Series (Input Validation, Injection Prevention, Secrets Management) is the
same corroboration set — Secrets Management already cited in SECRETS.md.

---

## 2. Candidate gaps — CONFIRMED / DISMISSED

The ROADMAP listed five candidate gaps "to be confirmed by the mapping, not
assumed." Verdicts:

### A. Threat modelling at design time (STRIDE-class) — **CONFIRMED (narrow)**

**Grounds.** Canon is unanimous this is its own design activity: ASVS V1, SAMM
Threat Assessment, SSDF PW.1, Proactive C4. atelier has the *seam* the ROADMAP
guessed — REVIEW.md lens 1 (attack the load-bearing assumptions), lens 4 at
design altitude ("what the work exposes, over-collects, or leaks by weakness of
design"), and "review the design, not only the build" — plus PRINCIPLES §5
(security by design) and §1 "design the unhappy path too". But every one of
these is **reviewer-side and adversarial-after-the-fact**: the *builder* is
nowhere told to enumerate the threats to a design as a first-class design step.
Threat modelling is present as a review lens, absent as a build activity. The
gap is real but small — the seam is identified, not missing.

### B. Secure-defaults beyond credentials (deny-by-default) — **CONFIRMED (narrow)**

**Grounds.** Held in fragments: PRINCIPLES §1 fail-safe "default destructive
actions to deny"; SECRETS.md "deny-by-default on access, take the stronger
authenticator class by default" (credential-scoped); §5 Zero Trust "network
location alone grants no trust". What is *not* stated is the general posture —
a new surface (config, service, feature, port, exposure) defaults **closed /
minimal**, and opening it needs the stated reason. Proactive C5 and ASVS V14
name this as a standalone control. The pieces exist; the generalisation from
"access + failure states" to "all defaults" does not.

### C. Supply-chain / dependency vuln screening — **CONFIRMED (reframed by zero-dep)**

**Grounds.** licenscan covers *licence* compatibility only; nothing screens
dependencies for known vulnerabilities (no SCA, no Dependabot/renovate config
present, no SBOM at rest — SBOM deferred in ADR 0007). The zero-dep house ethos
(tools/README "Zero third-party dependencies", the swappable-seam pattern
PRINCIPLES §2, §8 "design out the work") is the **primary supply-chain control**
and genuinely shrinks the runtime surface to near-zero — but it does not zero
the *residual*, which the mapping made concrete:

1. **CI consumes third-party GitHub Actions pinned by mutable major-version
   tag** — `actions/checkout@v5`, `actions/setup-python@v6`,
   `actions/setup-node@v4` (ci.yml). A moved tag ships new code into the trusted
   build. Canon (SSDF PS/PW, CIS 7, NCSC 6) wants SHA-pinning of actions.
2. **Toolchain provenance** — the floor still trusts system `python3`, `git`,
   `gh`, the OS, and the runner image. Unstated as a dependency at all.
3. **Already-tracked residuals**: scanner distribution to children
   (vendor/fetch/publish — tools/README names it "the deferred supply-chain
   call") and SBOM (ADR 0007 deferred to first published artifact).

So: confirmed gap, but the correct doctrine move is *name the zero-dep posture
as the control* and enumerate the small residual, not import a heavyweight SCA
pipeline. This was the mapping's most substantive finding.

### D. Secure-coding floor (input validation / injection) — **DISMISSED as a doctrine gap (framing note only)**

**Grounds.** The principle-altitude floor **is** held: PRINCIPLES §1 "fail-fast
on bad input — reject corrupt/invalid data at the edge, strict schema,
canonicalising validators, so a typo fails locally and never silently
downstream", and REVIEW.md lens 4 names "injection, cross-site scripting,
auth/authz gaps, unsafe input paths" as must-check vectors. The *concrete*
secure-coding rules canon wants (parameterised queries, per-context output
encoding — ASVS V5, Proactive C3, the Injection cheat sheet) are legitimately
**instance/code-layer**: atelier is a doctrine repo whose own code is small
stdlib-Python tools with near-zero injection surface, and the ROADMAP itself
predicted "likely instance-layer". No doctrine gap. **One honest note:**
PRINCIPLES §1 frames validation as *resilience*, never as *injection defence* —
the two are the same act. A one-line bearing would close the framing seam; not a
structural miss.

### E. "Plan for security flaws" — vulnerability capture-and-track — **CONFIRMED (partial)**

**Grounds.** The credential-exposure slice is fully held and is a genuine
strength: SECRETS.md watch→roll-on-confidence→never-scrub, with the cadence roll
doubling as a rehearsed incident runbook. What is *not* held: (1) a
**security-framed** vuln lifecycle — a flaw found in atelier's own shipped tools
rides the generic REVIEW→[backlog]→ROADMAP flow with no severity triage,
recurrence-prevention step (SSDF RV's third leg), or security tag; (2) a
**coordinated-disclosure posture** — atelier is PUBLIC and ships scanners other
repos adopt, yet there is no SECURITY.md / advisory path for a reporter. NCSC 8,
SSDF RV, CIS 17, SAMM Incident+Defect Management all name this. Confirmed.

**Note on the ROADMAP's own "already held" list.** It cites "incident learning
(harvest + the anti-slop promotion rule)". Verified: the **harvest** discipline
*is* doctrine (RECORD.md session-close tidy-up; the residue-harvest practice).
The **anti-slop promotion rule** is **not yet doctrine** — it is a ROADMAP
*capture* ("Anti-slop invariant registry", 2026-07-21, sourced to Aviator),
explicitly positioned as extending what atelier has. Naming it as "already held"
slightly overclaims; the general learning-into-record loop is held, the
formalised promotion rule is captured-not-built. Flagged for honesty, not as a
sweep gap.

---

## 3. Confirmed gaps → proposed doctrine seams (PROPOSALS for a future session)

Sizes are rough estimates for scoping, not commitments. All would be
self-authored doctrine → rule-4 cold review on the edit.

| Gap | Proposed seam (file · section) | Rough shape / size |
|---|---|---|
| **A** Threat modelling | REVIEW.md — extend "review the design" so lens-1/lens-4 design-altitude review *names* a lightweight threat pass; **or** a short PRINCIPLES §5 bullet "enumerate a design's threats before building it, right-sized (not full STRIDE ceremony)". Prefer REVIEW — the seam already lives there. | ~1 paragraph + a §5 pointer. No new doc. |
| **B** Secure defaults | PRINCIPLES §5 — generalise the existing fail-safe/deny-by-default bullets into one "secure defaults" statement: a new surface defaults closed/minimal; opening needs the stated reason (same "stated bridge" grammar already used). | ~1 bullet, generalising text already present. |
| **C** Supply chain | tools/README + a PRINCIPLES §2/§8 bearing: **name zero-dep as the supply-chain control**, then the residual — SHA-pin CI actions (a concrete ci.yml change, gateable), state toolchain trust, cross-link the already-deferred scanner-distribution + SBOM triggers. | ~1 doctrine paragraph + a real ci.yml pin change (own small task). |
| **D** Secure coding (framing only) | PRINCIPLES §1 or §5 — one bearing line: input validation is also injection defence; concrete encoding rules stay instance-layer. | 1 line. Optional. |
| **E** Vuln capture-and-track | Two moves: (1) a short REVIEW.md / RECORD.md note that a *security* finding carries severity + a recurrence-prevention step (SSDF RV) on the existing backlog flow; (2) a repo-root **SECURITY.md** disclosure policy — warranted because the repo is public and ships adopted tooling. | (1) ~1 paragraph; (2) a new short SECURITY.md (a floor artifact, template-able for children). |

**Sequencing suggestion (proposal).** C's action-pinning and E's SECURITY.md are
the two with live public-repo exposure and are the most concrete — good first
slice. A, B, D are doctrine-text refinements that can batch into one edit +
one cold review.

---

## 4. Sources consulted (with access dates)

All fetched live 2026-07-22 (UTC), not recalled:

- **NCSC developers collection** — <https://www.ncsc.gov.uk/collection/developers-collection> — 8 principles, retrieved in full.
- **NIST SSDF SP 800-218** — <https://csrc.nist.gov/Projects/ssdf> — 4 practice groups (PO/PS/PW/RV), retrieved.
- **OWASP SAMM** — <https://owaspsamm.org/model/> — 5 functions / 15 practices, retrieved.
- **OWASP ASVS** — <https://owasp.org/www-project-application-security-verification-standard/> (v5.0 confirms ch.1 Encoding & Sanitization, injection §1.2); chapter domains v4.0.3 (stable canon). GitHub/Wikipedia chapter-list fetches returned partial/404 — v4.0.3 domain names used as established canon, flagged as such.
- **CIS Controls v8.1** — <https://www.cisecurity.org/controls/cis-controls-list> — 18 controls, retrieved.
- **OWASP Proactive Controls 2024** — <http://top10proactive.owasp.org/> — C1–C10, retrieved.
- **Cheat Sheet Series** (Input Validation, Injection Prevention, Secrets Management) — referenced as corroboration; Secrets Management already cited in SECRETS.md.
- **NIST SP 800-63B rev 4** — already consulted and cited in the SECRETS.md credentials slice (`caa85fe`); not re-fetched here.

## Review

Records-only mapping, no doctrine edited → `review: not warranted` for this
record itself. The doctrine edits it proposes (§3) are self-authored doctrine and
earn a rule-4 cold spawn *when taken* — the ROADMAP item already carries
`review: WARRANTED when the mapping moves to doctrine edits`.
