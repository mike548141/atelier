**2026-07-10 (Opus) — build/ layer opened + the secrets doctrine.** Mike: "keep
going on Atelier work until economics says start a new session." Extraction
section was closed last session; the next sequenced theme is the **build/ layer**.
Shipped three doctrine docs, each grounded-not-invented, each pointing up to
`method/` rather than copying it (the DRY discipline the review has enforced
before). All three review-owed (doctrine text → a REVIEW.md sampling pass, not a
validator run).

**1. `docs/build/REPO-STANDARD.md` (A10) — the repo-craft standard extracted from
the `create-repo` skill.** The build/ layer's first content: product-in-a-subfolder
(+ why), sizing-to-type table (static/web, package/CLI, infra, docs), the standard
file set, **honest-CI** (a green check that proves nothing is exactly the
phantom-success EVIDENCE §14 forbids an instrument), repo-craft conventions, and
the two processes (new / standardise-existing). It owns repo *shape only* and
points up for everything method/ already owns — EVIDENCE (grounded-not-invented),
RECORD (SESSIONS/ADRs/why-comments), REVIEW (reviews/ briefs), PROPAGATION (the
CLAUDE.md doctrine block), AUTONOMY (private-first). Instance specifics (exemplar
repo names, git identity, `gh` account, `$PP`, locale) deliberately stay in the
delivery vehicle (the skill), not the shareable doc — reinforced by atelier's
whole-repo leakscan hook. build/README rewritten from "pointer, not yet extracted"
→ layer index.

**2. `docs/method/SECRETS.md` — the cheaply-burned secrets doctrine.** Extracted
from ros §5 (credential triad) + §7 (secret-store-not-exempt). It's the
*make-rotation-cheap* half that the leak/secret scans' *detect* half depends on;
completes **detect → rotate → burn-cost-is-minutes** and closes AUTONOMY's
forward-reference to "the secrets doctrine" (line 61 literally said "per the
secrets doctrine" with no doc behind it). Core: reproducible / re-mintable as the
enabling property (internal rotate mechanically; external re-mint behind one
approval; no hand-kept irreplaceable token — you can't rotate what you can't
re-mint); the least → JIT → short-lived triad with standing creds as a **tracked
debt, not a resting state**; references-never-values in the right plane (config /
device / shareable-repo hold a reference, value lives only in the encrypted store,
scans enforce); rotation-on-cadence bounds the undetected-exposure window
independently of any breach. Instance mechanism (sops+age, `!secret`, the
credential map) stays in ros. Slotted into method/README as #5 after
DATA-PROTECTION; the rest renumbered (now 1–10).

**3. `docs/build/REPO-BOUNDARY.md` — the is-this-a-repo decision.** The decision
*before* REPO-STANDARD's shape decision: standalone repo vs component (folder) vs
monorepo folder, decided by **independent-lifecycle discriminators** (visibility,
release cadence, ownership/access, reuse, blast radius) not size — a repo is a
unit of independent lifecycle, loose-coupling from PRINCIPLES applied to the
boundary itself. Rich client engagement is the worked monorepo case. Standing
behaviour: **advise proactively**. When ambiguous, prefer the **reversible**
direction — split-later is cheap (filter-repo/subtree, history intact), merge is
painful. Removed from build/README's still-owed list.

**Sequencing judgement:** deliberately did *not* do "rewire create-repo to
inherit" (the Q1 fix) this session — it would stack the skill's delivery path onto
REPO-STANDARD text that hasn't been reviewed yet. Better to let the review catch
up first. Picked three independent extractions with low DRY risk instead.

Lockstep each (RECORD): CHANGELOG Added entry, ROADMAP line ticked with the
review-owed note, method/README or build/README index updated, leak+secret scans
clean on staged before each commit. Three commits, each pushed: `17ccbde`
(REPO-STANDARD), `85d3573` (SECRETS), `be0dbfd` (REPO-BOUNDARY).

**Model:** Opus, plan-included — doctrine extraction, not token-heavy; no flag.
**ros pin:** left at `3ba6275` — these are new method/ + build/ docs ros doesn't
inline (its CLAUDE.md floor is unchanged), so no floor-driven bump; a records-only
courtesy bump is available but I didn't originate a cross-repo pin change here.
**Remaining build/ queue:** rewire create-repo to inherit (after REPO-STANDARD is
reviewed) + move templates into atelier; supply-chain/release (A5+A11).
**Remaining safety-tooling doctrine:** safe-access-onboarding. **Growing review
batch:** EVIDENCE §13/§14 (prior session) + these three — a Fable REVIEW.md
sampling pass is now owed across the recent doctrine writes.
