# 2026-07-22 · 1233 UTC · Two-tier person-context portability — design pass (records-only)

**Design capture, records-only.** Deliverable for the ROADMAP north-star item
*"Two-tier person-context portability"* (claimed 2026-07-22-1233 — the focused
design pass only). Everything below is **proposal**; every decision is Mike's;
nothing here is doctrine until ratified. Per the item's own framing, this is a
focused design pass, not "a sync problem".
**review: WARRANTED when this moves to build/doctrine; the capture itself is
records-only** (the gap-map precedent, 2026-07-22-1025).

**Boundary note.** This document is written entirely in tier/device/mechanism
classes, as the ROADMAP item is. No tier-1 *content* appears here — describing
the safe, is the point (`CLAUDE.md` hard constraints; TOOLBOX.md "the instance").

---

## 1. Problem statement and constraints

Two tiers of person-context live **outside** atelier and must reach every
device the principal works from:

| | Tier 1 — crown jewels | Tier 2 — instance/identity/toolbox |
|---|---|---|
| **Class of content** | health / family / finance / estate-map facts (the ROADMAP item's own class list) | accounts, venv paths, domains, client-entity facts, tool manifest auth column |
| **Encryption class** | E2E only (iCloud-ADP class or sops/age class) | private, lighter |
| **Remote rule** | **never a plain remote — not even private GitHub** | may tolerate a private store/repo |
| **Local at rest** | encrypted at rest *even locally*, above the device floor | device floor suffices |
| **Device floor** | FileVault/passcode class, every device | same |

Constraints derived from cited doctrine:

- **C1 — plaintext never rides an untrusted plane.** SECRETS.md "Right plane,
  never the wrong one": the value lives in exactly one (encrypted) place;
  everywhere else holds a reference. SECRETS.md explicitly blesses the
  age/sops-class store file "rid[ing] an ordinary backup or private remote
  without becoming the exposure" — i.e. the never-plain-remote rule binds the
  **plaintext**, and ciphertext is a different object. ⚠️ The ROADMAP wording
  *could* be read stricter (nothing tier-1, even encrypted, on a plain remote);
  §4 marks that reading 🎯 for ratification.
- **C2 — minimise the irreplaceable/exposable set.** DATA-PROTECTION.md
  "Reproducibility is data insurance" and "Other people's data is not yours to
  risk": tier-1 material includes third parties' personal information (family-
  class facts), carrying privacy obligations — hold the minimum, never widen
  exposure, never move it somewhere less protected. Any design that copies
  tier-1 into a *less* protected plane to gain convenience is a defect by
  construction.
- **C3 — no sync engine under a tooling-hot working copy.** STORAGE.md "The one
  gotcha": sync engines evict contents and serve stale reads under tools that
  touch many files fast — learned the hard way and retired in 2026-07-14's move
  to a plain local path. The person-context directory on a filesystem device is
  read by the harness at every session start and written continuously
  (transcripts, memory files); it is exactly the hot path the gotcha names.
- **C4 — the device is disposable; the context must survive it.** STORAGE.md
  "The rule": if the machine vanished, the context must be rebuildable from
  what remains. A tier-1 store that exists on one device only is a standing
  defect; equally, SECRETS.md's honest boundary applies — the master key's
  *loss* is unrecoverable by re-minting, so an out-of-band key backup is a
  **named obligation**, not a nicety.
- **C5 — gates by machine, not by memory.** DATA-PROTECTION.md "Encode it,
  don't just remember it" and SECRETS.md's scan posture: the tier boundary must
  be enforced by a check on the write path, not by an agent recalling the rule.
- **C6 — the phone leg is a different system, honestly.** The Claude iOS-class
  app reads no filesystem; phone-side context is app memory/Projects — content
  the app consumes is held on the **provider's** plane (conversations,
  Projects, memory), not the principal's. No mechanism choice on the phone can
  dodge that; the design must state it rather than paper over it (00-APEX.md:
  never a claim stronger than its evidence).
- **C7 — new sync mechanisms are new trust surfaces.** ACCESS.md: onboarding a
  domain (a sync service, a peer-sync daemon) is a floor event — owner grants,
  narrowest credential, read-only first ring. Any candidate that adds a daemon
  or service pays this cost explicitly.
- **C8 — the estate-root pattern already exists for tier 2.** PROPAGATION.md
  "estate resources — point up, don't re-derive": a **private estate-root
  repo** is the doctrinal home for provider plans, credentials references,
  inventory; public children reference it by local-path convention, never by
  name. Tier 2 should extend a shape that exists rather than invent a rival.

A present-state fact worth naming (mechanism-class, no content): today's
arrangement loads person-context **wholesale** at session start on filesystem
devices, with no tier split in the loading path. The design should allow the
always-loaded layer to be tier-2 while tier-1 loads on need — that serves both
C2 and threat T6 below.

---

## 2. Threat pass (right-sized, per REVIEW.md lens 4)

REVIEW.md lens 4 requires enumerating a design's threats **before** building —
"name the handful of threats that actually bear on the work's class", not full
STRIDE. Who/what could attack each surface:

| # | Surface | Threat actor / event | What it gets if unanswered |
|---|---|---|---|
| **T1** | Sync channel (transit) | Network observer; provider mid-path | Tier-1 plaintext in flight |
| **T2** | Remote store at rest | Provider insider; account compromise; legal/compelled access; breach of the provider | The whole tier at rest |
| **T3** | Local store at rest / device loss | Thief with the device; opportunistic access to an unlocked machine | Whatever rests in plaintext locally |
| **T4** | Wrong-tier write | Honest error — human or agent writes a tier-1 fact into the tier-2 store | Tier-1 material inherits tier-2's weaker posture, silently |
| **T5** | Public-repo leak path | Tier material of either tier reaches atelier or a public child | Publication — unrecoverable (a push is publication) |
| **T6** | Session plane | Tier-1 plaintext loaded into a session travels onward — transcripts, records, a commit, a pasted reply | Exposure via a plane nobody thought of as "the store" |
| **T7** | Key / recovery loss | Lost age identity, lost recovery contact/key for the E2E account | **Availability** failure: the store outlives the ability to read it (SECRETS.md honest boundary — loss ≠ exposure) |
| **T8** | Phone provider plane | Anything the app consumes is held provider-side | Tier-1 in a remote store the principal doesn't control — the never-plain-remote rule collides with the platform's shape |

How the candidate classes answer (✅ answered by design · ⚠️ partially / by
discipline · ❌ unanswered):

| Threat | E2E folder sync (plaintext local) | age/sops capsule (ciphertext anywhere) | Plain private repo | App memory / Projects | Paste-in capsule | Phone-as-terminal |
|---|---|---|---|---|---|---|
| T1 transit | ✅ E2E | ✅ ciphertext | ⚠️ TLS only | ⚠️ TLS to provider | ⚠️ TLS to provider | ✅ tunnelled to own device |
| T2 remote at rest | ✅ provider holds no keys | ✅ remote holds ciphertext | ❌ repo access = plaintext | ❌ provider-held plaintext | ❌ once pasted, provider-held | ✅ nothing new remote |
| T3 local at rest | ❌ plaintext above device floor | ✅ decrypt-on-demand, nothing resident | ❌ plaintext clone | n/a (no local store) | n/a | ✅ nothing lands on the phone |
| T4 wrong-tier write | ⚠️ discipline only | ✅ gate on the tier-2 write path (§3) | needs the gate | ⚠️ discipline only | ⚠️ generator controls content | ✅ no phone-side store to mis-write |
| T5 public leak | ⚠️ existing leakscan floor | ✅ ciphertext is inert even if leaked | ⚠️ existing floor | ⚠️ out of repo reach | ⚠️ same | ✅ same as filesystem leg |
| T6 session plane | ❌ wholesale-loaded | ⚠️ load-on-need shrinks it | ⚠️ | ❌ memory *is* the session plane | ⚠️ per-conversation, bounded | ⚠️ transcript still exists device-side |
| T7 key loss | ⚠️ account recovery machinery | ⚠️ **key backup is a named obligation** | ✅ no key | ✅ no key | ⚠️ inherits capsule key | ⚠️ inherits device access |
| T8 phone plane | n/a | n/a | n/a | ❌ the threat, embodied | ❌ accepted per-paste | ✅ dodged entirely |

🔎 Two findings fall straight out of the table:

1. **T4 is procedural, not cryptographic.** No mechanism prevents a tier-1
   fact being *written into* the tier-2 store; only a gate on the tier-2 write
   path does (C5). That gate needs a written classification rule — "what makes
   a fact tier 1" — before it can scan for anything. That rule is a doctrine
   artefact this pass does not write (§5).
2. **T8 is a trust ruling, not a design choice.** Every phone-native option
   puts consumed content on the provider's plane. The real question is whether
   the principal accepts the provider as a holder of *any* tier-1 material.
   Mechanism selection is downstream of that ruling (§4, 🎯).

---

## 3. Candidate architectures per leg

### 3a. Filesystem leg (desktop/laptop class — devices with `~/.claude`-class paths)

| | **F1 · E2E folder sync** (ADP-class) | **F2 · age/sops encrypted capsule** | **F3 · plain private repo** (estate-root) | **F4 · peer sync** (Syncthing-class) |
|---|---|---|---|---|
| Carrier | provider sync engine over an E2E-enabled account | ciphertext file(s); *any* channel — private repo, E2E folder, even ordinary backup (SECRETS.md) | git over a private remote | device-to-device daemon, no third-party remote |
| At rest, remote | ✅ E2E (keys device-held) — *if* the E2E tier is actually enabled on the account | ✅ ciphertext | ❌ plaintext to anyone with repo access | ✅ no remote exists |
| At rest, local | ❌ plaintext (device floor only) | ✅ plaintext exists transiently, on demand | ❌ plaintext clone | ❌ plaintext replica per device |
| In transit | ✅ | ✅ | ⚠️ TLS | ✅ (own devices) |
| Session consumption | files simply present at the path; zero ceremony | decrypt-on-need: a small unlock step (hook or explicit command) renders plaintext to a transient path or straight into session context | ordinary file reads of the clone | files present at the path |
| Offline / failure | last-synced copy; conflict files under concurrent edits; **C3 gotcha**: eviction/stale reads under a tooling-hot tree | ciphertext is local once synced; decryption is offline; conflict = git-style merge of ciphertext ⚠️ (opaque — resolve by re-encrypt from canonical) | full git semantics: history, merge, provenance | replica present; sync needs devices to meet; no history |
| Ceremony / cost | lowest — and priced accordingly in the threat table | key provisioning once per device; an unlock step per use; **key-backup obligation (T7)** | clone + pull; the shape every session already knows | new daemon per device = new trust surface (C7); ongoing care |
| Tier fit | tier 2 plausible; tier 1 fails "encrypted at rest even locally" | **tier 1 shaped**: meets every tier-1 clause | **tier 2 only** — the ROADMAP says so in terms | either tier technically; pays C7 for what F2 gets cheaper |

Notes with the honesty on:

- **F1's E2E claim is conditional** on an account-level setting whose status is
  a fact only the principal knows, and whose coverage has product-defined
  exclusions. A design that inherits its confidentiality from a toggleable
  account setting holds T2 by configuration, not by construction. And C3 applies
  in full if the synced folder is the *live* context directory.
- **F2 splits canonical from carrier.** The capsule (one or few age-encrypted
  files) is canonical; the channel that moves ciphertext is a commodity. Keys:
  one age identity **per device** (SECRETS.md asymmetric grading — one key
  across systems is acceptable, but per-device identities keep device
  revocation clean: evict a device by re-encrypting to the surviving
  recipients). Losing all identities loses the store — hence the out-of-band
  key backup as a named obligation, kept survivable by copies (SECRETS.md
  honest boundary).
- **F2's consumption model serves T6**: the always-loaded person-context layer
  becomes tier-2 (safe to sit in plaintext under the device floor), and tier-1
  is decrypted *into a session only when the work needs it* — data
  minimisation on the session plane, not just the storage plane.
- **F3 is the estate-root repo atelier's doctrine already points at** (C8). It
  gains the tier-2 wrong-tier gate cheaply: git has a pre-commit hook point,
  and the house already runs leakscan-class hooks — extend the class, don't
  invent a scanner.
- **F4** buys nothing F2 doesn't, at the price of a daemon on every device.
  Named, considered, set aside.

### 3b. Phone leg (app-class device — no filesystem access; C6/T8 govern)

| | **P1 · app memory/Projects as a second system** | **P2 · paste-in bootstrap capsule** | **P3 · tier-1 out of scope on phone** | **P4 · E2E file + attach on use** | **P5 · phone-as-terminal** | **P6 · personal context endpoint** (connector/MCP-class) |
|---|---|---|---|---|---|---|
| Carrier | provider's memory/Projects store | text rendered from the canonical store, pasted per conversation | none (tier 2 only reaches the phone) | file in E2E cloud storage, attached into a conversation when needed | none — the phone drives a session on a filesystem device (remote-session/SSH-class); that leg's mechanism carries the context | a server the app queries |
| At rest | ❌ provider-held plaintext, standing | ❌ provider-held once pasted, per conversation | ✅ nothing tier-1 at rest phone-side | ✅ E2E until used; ❌ provider-held once attached | ✅ nothing lands on the phone | ❌ endpoint holds it; provider transits it |
| Consumption | automatic — the app's own context features | manual paste at conversation start | n/a | manual attach | full filesystem-leg semantics, small screen | automatic once wired |
| Offline / failure | works offline-ish per app behaviour; **drift** is the failure mode — no diffable state, no version | stale capsule = wrong context, silently, unless the capsule self-identifies | no failure mode — the gap is declared | needs the file synced + reachable | needs the home device up and reachable — real availability dependency | endpoint down = no context |
| Ceremony | low per use; **reconciliation discipline** is the recurring cost | per-conversation paste; regeneration cadence | zero | per-use attach | per-use connect | 🛑 build + operate an internet-reachable service fronting crown jewels — a new attack surface out of all proportion to the need |
| Tier fit | tier 2; tier 1 only under an explicit provider-trust ruling | either tier *if* provider trust is ruled acceptable for the pasted subset | tier 1 (by exclusion) | marginal improvement on P2 for at-rest posture | **the only option that gets tier-1 semantics onto the phone without provider-held tier-1 at rest** | rejected for tier 1 on its face; over-built for tier 2 |

- **P1 must be run as a *deliberately separate second system*, not a mirror.**
  There is no supported way to write app memory programmatically; reconciliation
  is a human-executed discipline: the canonical (filesystem) store renders a
  compact tier-2 profile; the principal seeds Projects/memory from it; a
  **version/date stamp inside the profile text** lets any phone session state
  which profile it holds, making drift observable (the PROPAGATION.md pin
  shape, applied to app memory — observable, not enforced).
- **P2 vs P1** is freshness-control vs convenience: the paste capsule is exact
  and versioned at each use but costs ceremony every conversation; app memory
  is ambient but drifts. They compose: memory holds the stable tier-2 core, a
  paste capsule tops up when a conversation needs specifics.
- **P5 is the honest escape hatch for tier-1-on-the-move**: the phone is a
  screen, not a store. Its costs are real — a reachable always-on device, and
  device-onboarding per ACCESS.md for the access path — but it is the only
  candidate in the row that answers T8 rather than accepting it.

### 3c. The seam between the legs

One rule proposed: **the filesystem leg is canonical; everything phone-side is
derived and dated.**

- A generator (future build, not this pass) renders phone-side artefacts from
  the canonical store: the tier-2 bootstrap profile (for P1 seeding), the paste
  capsule (P2), each carrying its version stamp.
- Flow is one-directional by default. Anything learned *on* the phone that
  deserves to persist is carried back by the principal into the canonical
  store — a reconciliation checklist, on a cadence, not a sync engine. This is
  deliberate: a bidirectional seam would make the provider-held plane a write
  source for the crown-jewel store, inverting C2.
- Drift is made observable, never assumed away: the stamp answers "which
  version of me does the phone hold?", and the reconcile cadence bounds how
  stale the answer can be — the same shape as SECRETS.md's rotation cadence
  bounding the undetected window.

---

## 4. Recommendations (argued; every one is a proposal)

| Tier × leg | Recommend | Runner-up, and why not |
|---|---|---|
| **Tier 1 · filesystem** | **F2 — age/sops encrypted capsule**, canonical, per-device identities, decrypt-on-need, out-of-band key backup | F1 E2E folder sync — fails "encrypted at rest even locally", inherits C3's sync-under-tooling gotcha on a hot path, and rests its whole T2 answer on an account setting rather than construction |
| **Tier 1 · ciphertext channel** | ride the estate-root private repo (ciphertext only, per SECRETS.md "safe to ride a private remote") — history and provenance for free | E2E folder as the channel — works, but adds nothing over ciphertext-in-git and gives up history |
| **Tier 2 · filesystem** | **F3 — estate-root private repo** (extends PROPAGATION.md's existing pointer shape), with a **wrong-tier pre-commit gate** (leakscan-class, driven by a written tier-classification rule) | F1 folder sync — no hook point for the T4 gate, no history, C3 exposure |
| **Tier 1 · phone** | **P3 by default — out of scope for the app-native path**, with **P5 phone-as-terminal** as the sanctioned route when tier-1 context is genuinely needed on the move | P2/P4 curated capsule — viable *only* under an explicit provider-trust ruling, and even then for a curated minimal subset, never the full tier; it accepts T8 rather than answering it |
| **Tier 2 · phone** | **P1 — app memory/Projects as a declared second system**, seeded from a generated, version-stamped profile; reconciliation on a stated cadence | P2 paste-every-time — exact but heavy; keep it as the top-up for specifics, not the base |
| **Seam** | filesystem canonical → phone derived+dated; one-directional by default; human-executed reconcile checklist | any bidirectional sync ambition — inverts C2 and has no mechanism to stand on anyway |

### 🎯 Decisions only the principal can make

> **🎯 D1 — The strict-reading question.** Does "never a plain remote, not even
> private GitHub" bind the *plaintext* (this design's reading, per SECRETS.md's
> ciphertext-may-ride-a-private-remote clause) — or bind tier-1 material in
> *any* form, ciphertext included? If the stricter reading: the tier-1 channel
> drops to E2E folder or peer sync for ciphertext transport; the capsule design
> itself survives unchanged.
>
> **🎯 D2 — The provider-trust ruling (governs the whole phone leg for
> tier 1).** Is the provider acceptable as a holder of any tier-1 material at
> all — even a curated subset, even transiently in a conversation? *No* forces
> P3+P5 (the recommendation). *A bounded yes* opens P2/P4 for a defined subset.
>
> **🎯 D3 — Is the ADP-class E2E tier actually enabled** on the relevant
> account, and is the principal willing to make an account setting load-bearing
> for anything? (Only bears on the runner-ups F1/P4; the recommendations don't
> depend on it.)
>
> **🎯 D4 — Appetite for phone-side context at all.** How much does mobile work
> actually need beyond tier-2 identity/instance facts? The reconcile cadence
> and the P5 investment both size to this answer.
>
> **🎯 D5 — Key-backup home.** The age master-key backup is a named obligation
> (T7); where it lives — personal vault class, paper, second device — is
> person-level and outside any repo (SECRETS.md scope clause). Needs a decision,
> not a mechanism.

---

## 5. What this deliberately does not decide

- **Build steps.** The capsule tooling (encrypt/decrypt-on-need, unlock hook),
  the profile/capsule generator, the wrong-tier pre-commit gate, key
  provisioning per device — all future work, gated on §4's decisions.
- **The tier-classification rule.** The T4 gate cannot exist before a written
  rule says what makes a fact tier 1. Writing that rule is a doctrine act, not
  a records act.
- **Doctrine edits.** STORAGE.md (a fourth storage class: the person-context
  capsule), TOOLBOX.md (the instance manifest's portable home), PROPAGATION.md
  (whether the estate-root pointer language absorbs the tier split) all have
  seams here; none is edited by this pass.
- **Re-tiering the always-loaded layer** — splitting today's wholesale
  session-start load into an always-loaded tier-2 layer plus on-demand tier-1
  — is proposed (§3a, T6) but is a migration with its own pass.
- **Cadences and channels** — reconcile cadence, ciphertext channel choice,
  P5's access-path onboarding (a full ACCESS.md sequence in its own right).
- **Anything downstream of D1–D5.** Where a decision above changes the answer,
  the dependent choice is parked, not presumed.

The "resume any project from any device" north-star item remains open and
depends on this design landing — this pass feeds it; it does not claim it.

---

## Decision stamps (Mike, 2026-07-23 — D1–D5 ruled)

Ruled in plain-language walk-throughs; where a ruling supersedes this
design's counsel, the grounds are recorded — the decision is the
principal's (REVIEW.md rule 3).

- **D1 — plaintext-binding reading confirmed; carrier = the private
  estate repo.** The encrypted capsule may ride private GitHub (history
  and provenance for free); the readable content never leaves owned
  devices. Confirmed after an explicit locked-box walk-through.
- **D2 + D4 — FULL PARITY for the app plane, superseding the design's
  P3/P1 counsel.** Mike's challenge, upheld on examination: there is no
  phone-unique risk — the app plane is identical on phone/web/desktop
  app, and tier-1 material already transits the provider's servers in
  every filesystem-leg conversation, so barring *standing* app memory
  protected a line already crossed in daily practice. Ruling: both tiers
  go to the app plane via memory/Projects as a **generated, date-stamped
  profile**, refreshed on a cadence, deletable at will. The residuals
  stand as named: staleness (the date stamp + reconcile cadence is the
  control) and second-copy drift (one-directional seam unchanged —
  filesystem canonical, app-plane derived).
- **D3 — ADP is enabled and may be load-bearing** — F1/P4-class E2E
  channels are available where convenient; the capsule remains primary.
- **D5 — key backup lives in Apple Passwords** (secure note in the
  person-level credential home, per the standing personal-credentials
  rule; outside every repo and every machine the key protects).

Unblocked build strand → ROADMAP (capsule build; tier-classification
rule + wrong-tier gate; app-plane profile generator + cadence).
