# atelier ROADMAP

Lean by design: **what's open**, prioritised, read every session. Completed
detail lives in [`ROADMAP-DONE.md`](ROADMAP-DONE.md) — the current-truth/history
split (`method/RECORD.md`); `tools/sizescan.py` is the signal that keeps this
file honest. Sequencing rule from the 2026-07-10 review: **mechanism before more
content** — a repo that inherits docs but not the propagation + review cadence
has inherited the costume, not the doctrine.

Checkbox states — a **work-owed tri-state**, never a disposition (Mike,
2026-07-22): `[ ]` work still owed · `[x]` **no more work owed** — delivered,
superseded, or declined, with the disposition said in the item's own text (a
dated note), never a fourth bracket · `[~]` **claimed** by a live parallel
session — `(claimed <date>-<HHMM>, wt: <branch>)`, optionally extended in place
with a resume breadcrumb (`· at: <step>` — CONCURRENCY § Surviving an
interrupted session) — don't start a `[~]` item;
take the next open one (`method/CONCURRENCY.md` § Claiming work) ·
`⏳` **review queued** for a non-author to take — any spawner passing rule 4's
criterion may take it; the taker writes the brief (`method/REVIEW.md` rule 4).
**The pointer is refs only** — name the delta and the intent record, no
evaluative account; the account lives in the session record, so a taker meets
the work cold (REVIEW.md rule 4's ceiling, stated here at the point of use).
And the delta list stays *complete*: a later commit that touches a queued
delta's doctrine surfaces — even for hygiene — widens the pointer's delta
list in the same commit (AW6 ruling, 2026-07-23).

## Doctrine — review-owed

Completed review cycles (Claiming-work, REACH ×3, the independence batch,
COMMUNICATION, RECORD keep-generic, signing doctrine, PRINCIPLES §8, the plugin
bundle, CONCURRENCY put-away, CLI-docs standard, ADR 0006/ccarchive addendum,
CONVENTIONS + UTC-at-rest, lean-files/sizescan, the review-trigger/sizescan
combined cycle — 0407 → F1–F9 applied → 0544 → G1–G3 applied → 0629 terminal
no-MAJOR pass, closed 2026-07-19; the 2026-07-20 triple cycle — DOCUMENTATION
doctrine + CONCURRENCY posture flip + session-onramp operating-rhythm, three
rule-4 cold passes all PASS no-MAJOR, applied `87af9f9`; the review-line
artefact cycle — rule-4 cold pass PASS 0M/1M/5L, Mike's accept-all applied
terminal, closed 2026-07-21; the REVIEW.md scope/lens-4 cycle — 2158 cold
pass 2M/3M/2L → SL1–SL7 accept-all applied `d553045` → 0244 terminal
no-MAJOR application pass, closed 2026-07-22; the harvest-integrity cycle —
0819 pass 1M/3M/2n → HI-F1–F6 accept-all applied `30d350c` → 0943 terminal
no-MAJOR application pass, closed 2026-07-22; the secrets/access cycle —
1021 rule-4 cold pass taken by the 1018 queue run, PASS-WITH-FINDINGS
0M/4m/4L/1n terminal; SA1–SA9 ruled accept-all and applied `f8350ee`
2026-07-23, cycle closed; the economics cycle — 0222 rule-4 cold pass
0M/4m/3L/1n, EB1–EB8 ruled accept-all, terminal application `86f8530`
2026-07-23; the queue-run cycle — 1149 pass → QR1–QR9 applied `b65209c` →
0222 rule-4 application pass 0M/1m/3L/2n, QA1–QA6 applied `5891184`
terminal 2026-07-23; the v2-plugin cycle — 1215 pass → VP1–VP8 applied
`ff8a07f` → 0222 rule-4 application pass 0M/2m/1L/1n, VA1–VA4 applied
`bbaec81` terminal 2026-07-23) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- [ ] 🎯 **AWA1–AWA4 rulings (Mike) — apex-widening cycle terminal** — the
  AW-rulings application's rule-4 cold pass ran 2026-07-23-0330 (taker-spawned
  per the claim; **PASS-WITH-FINDINGS 0M/2m/1L/1n**, verdict:
  [`reviews/2026-07-23-0330-aw-application-cold.md`](reviews/2026-07-23-0330-aw-application-cold.md)).
  All nine AW decision stamps reproduce at HEAD; no MAJOR ⇒ the cycle closes
  on Mike's ruling (REVIEW.md close rule) and that ruling's application is
  the terminal one — no further pointer. Counsel: take all four, each small —
  AWA1 add the child-template floor block to the AW2 sweep list · AWA2 close
  AW6's landing→queuing window (queue the ⏳ in the landing commit) · AWA3
  split the 00-APEX double attribution · AWA4 folds into AWA2.
- [ ] 🎯 **Glossary ratify pass (Mike)** — end-to-end read of
  `method/GLOSSARY.md`: tighten wording, rule on the full-definition entries
  (principal / agent / session / doctrine — new canonical homes), confirm the
  admission rule. Until then the SEED banner holds entries as PROPOSED.
- [ ] **Capture → doctrine candidate: the close all-clear should carry the
  pushed floor run's result** (grounded 2026-07-23: a session's 00:47 close
  pushed a 🎯-closed item and ended with the floor red — reviewscan since
  00:06 + its own un-harvested `[x]`; the next session inherited the debt and
  restored green, `165c40f`). RECORD.md's close rule demands evidence under
  the all-clear but never names the CI result; "scanners green locally" is
  not "floor green at head". Small wording-sized RECORD.md edit; rides the
  normal review cycle when taken.
- [ ] **Propagate the widened apex floor to children — and sweep every in-repo
  apex restatement** (surfaces named per AW2's ruling, 2026-07-23, so the
  sweep is mechanical): root `README.md:57` + `:93`;
  `docs/method/PRINCIPLES.md:10` + `:316`; `docs/method/PROPAGATION.md:40` +
  its inlined floor template block; `skills/session-onramp/SKILL.md`
  description + §1; `docs/method/README.md:11` (EVIDENCE named behind honesty
  only, now the truth bar) — all still two-element at HEAD. Per AW8's ruling:
  the child floor's adaptation line must carry the honesty-precondition
  clause verbatim-or-equivalent. Gated on the apex review cycle above closing
  (the application pass ran 2026-07-23-0330, no MAJOR — the cycle closes on
  Mike's AWA ruling; if AWA1 is taken, this sweep list gains the
  child-template floor block); then the in-repo sweep + fleet sweep,
  per-child commits.

## build/ layer — open strands

- [ ] **Code-signing standard across the fleet** (Mike, 2026-07-11) — "how do we
      sign all the code in the various repos". Two distinct layers, deliberately
      split by cost:
      - [ ] **Flip CI from warn to block.** signscan runs `--warn` fleet-wide;
            flipping to blocking (drop `--warn`, make the gh-plane warning an
            error) is Mike's call once the pre-existing scanner debt is cleared
            and every active machine signs. Vigilant mode stays off until then.
            **Gate assessed 2026-07-12 (session 47), corrected same day by the
            post-session self-review — not met, and the blockers are the
            owners', not the main line's.** None of the three red children fails
            on *signing* (~~so the flip wouldn't newly-red them~~ — **corrected
            2026-07-19, see below**; but the fleet isn't clean enough to declare
            enforce-mode honestly): two fail
            secretscan on owner-tracked secret debt (the principal's rotations,
            session 39's owed list); the third is red on **both** its bespoke CI
            (lint + a test error, agent-actionable, separate cleanup) **and**
            its floor (leakscan findings). Which child is which lives in their
            own private records, not here (RECORD's name × debt join).
            **Retraction:** this session first published a claim that session 41
            had "mis-filed" the third child's redness as scanner debt — that
            claim was built on a `--limit 1` run query that happened to catch
            the bespoke CI workflow; the floor workflow is red too, session 41's
            filing was accurate, and the accusation is withdrawn. On the two
            secret-debt children signscan never runs (secretscan fails first).
            The **"every active machine signs"** half is also unverified. Flip
            held — Mike's call + Mike's action (the rotations). **Hold
            re-confirmed by Mike 2026-07-23** (offered a scheduled rotation
            sitting; chose hold-as-is).
            **Correction 2026-07-19 — "wouldn't newly-red them" was wrong; the
            greens proved nothing** (under `--warn` no floor can *fail* on
            signing, and on scanner-red children the signing steps never run).
            **Before flipping, run `tools/signfleet.py`** — built this session
            for exactly this question. First run: **10 pass, 2 fail, both
            currently green**. Seven unsigned commits from two causes, neither a
            second machine: a boundary set too early, and five replayed by a
            **rebase-merge** (`gh pr merge --rebase`; merges here are agent-run)
            which re-commits server-side, stripping signatures — a recurring
            hazard, since squash/merge-commit are web-flow-signed and it is not.
            Evidence chain in the session record. **Applied (principal's call):
            both boundaries corrected (signfleet 12/12) and
            `allow_rebase_merge` disabled on all 13 repos — shut server-side
            rather than left to each session to remember; merge-commit + squash
            remain, local rebase unaffected, reversible.** Remaining blocker:
            the scanner debt. "Every active machine signs" stays unverified, but
            the drift behind that doubt is explained and is **not** a machine.
      - [ ] **Release-artifact signing + SBOM (deferred, was A5).** Signing *built
            artifacts* + a deterministic SBOM needs external tooling (syft/cosign),
            which hits the tool-install floor and breaks the zero-dep house-tool
            pattern — a deliberate design call, not a build. Revisit when a real
            *release* (a published package/binary) needs provenance; GitHub's
            native artifact attestations are the lightest route if so. Now also
            recorded as SIGNING.md's layer 2 with the same stated trigger.
  - [ ] **C5 backlog strand**: `tools/scaffold.py` (mechanise the
        seed/rename/stamp core; skill becomes its wrapper) — only if a stamp
        defect recurs despite step 5's new mechanical prove-the-stamp.

Completed build/inheritance work (REPO-STANDARD, licenscan, signing doctrine +
activation, faves/ros floor adoption, create-repo rewire + real-scaffold,
REPO-BOUNDARY, worktree tooling) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Orchestrated queue runs — from hand-carried prompt to doctrine (Mike, 2026-07-22)

Built 2026-07-22 as ratified (CONCURRENCY § Orchestrated queue runs +
ECONOMICS § tier split + plugin-bundled `queue-run` skill) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md). What remains open is its review:

- [ ] **Third-seat executor trial (Mike, 2026-07-23, per `dadde1d`)** — on the
  next queue run, dispatch one or two *routine, well-floored* items to the
  mid tier (Sonnet) instead of the workhorse; orchestrator reviews as normal.
  Keep the step-down only on the floor's evidence (scanners/tests/review all
  green, no hand-up); record the outcome either way — tier claims are
  extracted from practice, not assumed. Fan-out sub-agents on the cheapest
  genuinely-capable tier is already standing practice (no trial needed).

## Security doctrine vs public good practice — gap analysis (Mike, 2026-07-22)

Mike's directive during the SECRETS.md access-management session: *"take into
account any publicly available good practice for security that we should build
into the doctrine"* — OWASP named, the NCSC developers collection linked, and a
secure-SDLC checklist pasted (threat modelling/STRIDE, secure defaults, least
privilege, secure coding, secrets management, supply-chain checks, automated
scanning, peer review, continuous learning). The *credentials* slice landed
same-session (SECRETS.md "Grounding in public practice", `caa85fe` — NIST SP
800-63B rev 4 + OWASP secrets cheat sheet, corroboration named, the one
divergence owned). The rest is a doctrine-wide sweep, deliberately not crammed
into that delta:

Mapping done 2026-07-22 (record:
[`sessions/2026-07-22-1025-security-canon-gap-map.md`](sessions/2026-07-22-1025-security-canon-gap-map.md)
— A/B/E confirmed narrow, C reframed to mutable-tag CI actions, D dismissed
instance-layer) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- [ ] 🎯 **SCA1–SCA3 rulings (Mike) — security-canon cycle terminal** — the
  SC-rulings application's rule-4 cold pass ran 2026-07-23-0330 (same
  taker-spawn; **PASS-WITH-FINDINGS 0M/1m/1L/1n**, verdict:
  [`reviews/2026-07-23-0330-sc-application-cold.md`](reviews/2026-07-23-0330-sc-application-cold.md)).
  All six SC decision stamps reproduce (PVR re-verified live,
  `enabled:true`); no MAJOR ⇒ the cycle closes on Mike's ruling and that
  ruling's application is terminal. Counsel: take all three, wording-sized —
  SCA1 state the atelier@main code-execution grant and its bound beside the
  named asymmetry · SCA2 hedge "scanner fixes reach children automatically"
  to the floor template's default configuration · SCA3 add `→ enabled: true`
  to REPO-STANDARD's PVR verify command.
- **Already held — name, don't rebuild** (verified by the mapping,
  2026-07-22): automated scanning in the pipeline (the floor scanners), peer
  review before ship (REVIEW.md), least privilege (SECRETS triad), secrets
  never in source (right plane), repo protection (ADR 0007 signing + the
  floor — active since 2026-07-12 per SIGNING.md), incident learning (the
  harvest loop; the anti-slop *promotion rule* is a capture below, not yet
  doctrine — the original list overclaimed it, corrected 2026-07-22), clean
  maintainable code (PRINCIPLES).

*review: WARRANTED when the mapping moves to doctrine edits; the capture
itself is records-only.*

## Anti-slop invariant registry — promote recurring review findings to always-on checks (Mike, 2026-07-21)

Source: <https://thenewstack.io/engineering-ai-slop-registry/> (Aviator). A
mechanism for AI+human engineering that fits atelier's "mechanism before more
content" ethos. The idea: an **invariant catalog** — codified, always-checked
rules capturing the conventions/constraints that live in senior engineers'
heads (convention blindness, deprecated APIs, module boundaries, security
baselines) and that a model has no per-codebase training for. They call it the
"anti-AI-slop registry".

**What's genuinely NEW for atelier** (much is already ours — see below): the
systematic REGISTRY and its promotion rule.
Mining done 2026-07-22 (330 findings / 47 reviews → 5 scanner + 7 verifier
candidates; record:
[`sessions/2026-07-22-1036-invariant-candidates.md`](sessions/2026-07-22-1036-invariant-candidates.md))
→ [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- **S1–S5 / V1–V7 ALL APPROVED 2026-07-23** (Mike, plain-language
  walk-through of the mining record's candidates; the PROPOSED-then-ratify
  pattern; S5 approved explicitly on ROI over its borderline finding
  count). Approved seams/homes are the record's proposals unamended: all
  twelve shared-floor. The promotion rule itself (>2 occurrences ⇒
  candidate) is thereby exercised end-to-end and stands as practice.
- [ ] **Build the approved scanners S1–S5** — line-wrap (S1), prose-path
      resolution via linkscan extension (S2), absolute-UTC dating (S3),
      stamp-drift vs canonical parent (S4), NZ-English wordlist (S5). Each
      lands with tests + selftest + floor wiring per the scanner house
      pattern; first-of-kind ones earn their review before gating
      (don't-stack).
- [ ] **Codify V1–V7 as the always-loaded reviewer checklist** — the
      registry mechanism's doctrine half; lands in REVIEW.md/the review
      skill with each item's cited grounding. Self-authored doctrine ⇒
      rule-4 ⏳ at landing.
- [ ] **Two-layer acceptance criteria, one verification pass.** (Build item —
      waits on the 🎯 rulings above; the mining record's "how the registry
      would be checked" section holds the proposal.) Per-change
      criteria (task-specific) + the invariant catalog (loaded automatically)
      assemble into ONE checklist a verifier runs. The author need not remember
      the org rule — the catalog enforces it unasked. Invariants are
      declarative rules with conditions (path globs, exemptions), e.g. "writes
      to `users` must go through the repository; exempt migrations; glob
      `src/**/*.go`".
- [ ] **Enforcement seam — how does an invariant get checked?** (Per-candidate
      seams proposed in the mining record — scanner vs checklist vs verifier,
      one line of why each; decisions ride the 🎯 rulings above.) Three
      candidates to place on our existing spectrum: a CI scanner (like
      leakscan/secretscan — the machine-checkable ones), a review-time
      checklist item, or an agent-verifier criterion. Decide which invariants
      are code-checkable (→ scanner) vs judgement (→ verifier/human).
- [ ] **Where does the registry live?** (Proposed per candidate in the mining
      record — all five scanner candidates shared-floor, one checklist
      repo-specific; decision rides the 🎯 rulings above.) atelier-shared floor invariants (fleet-
      wide, like the current scanners) vs repo-specific catalogs (a child's own
      conventions). Likely both, same layering as doctrine: shared floor +
      local append. Ties REPO-STANDARD.

**What atelier ALREADY has (this EXTENDS, doesn't invent):**
- The **floor scanners** (leakscan/secretscan/signscan/sizescan) ARE always-on
  invariants — machine-checked, fleet-wide, never re-argued. This idea
  generalises them to project-specific, review-derived rules.
- **Writer ≠ verifier independence** — REVIEW.md rule 4 (different context,
  different blind spots, structured findings on the durable record) is exactly
  the article's "the writing agent and verifying agent are different… a
  structured report per criterion, not a gut-check from the same model".
  Corroboration of standing doctrine, not a new claim.
- **Move human judgment UPSTREAM / review before build** — "humans review
  specs, plans, constraints, acceptance criteria, not 500-line diffs" is our
  review-is-an-input-not-a-gate line (ros CLAUDE.md + REVIEW.md). Corroborated
  by their intent-driven experiment (spec reviewed first → agent builds 6k LOC
  → second agent verifies 65 criteria in 6 min: 60 pass / 4 fail / 1 partial).

Framing worth keeping: *"You're not building software anymore. You're building
the machine that builds software, and quality control is part of that machine."*
*review: WARRANTED when this moves from capture to doctrine/mechanism (it
touches REVIEW.md + EVIDENCE.md + the scanner floor); brief owed at pickup.*

## instruments/ — open features

### ccarchive (Mike, 2026-07-17)

Restore (full + delta), dataless awareness, and manifest signing all built
2026-07-22; the two open questions answered by measurement (tool-result
sidecar capture hole; keep-separate counselled) → detail in
[`ROADMAP-DONE.md`](ROADMAP-DONE.md), record
[`sessions/2026-07-22-1050-cc-instruments-questions.md`](sessions/2026-07-22-1050-cc-instruments-questions.md).
What remains is Mike's:

- **Metadata classes RULED 2026-07-23** (plain-language walk-through, the
  cc-instruments record's context relayed): tool-result sidecars **capture**;
  per-project `memory/*.md` **capture**; top-level `history.jsonl`
  **capture — Mike overturned the lean-exclude counsel** (wants the
  typed-prompt stream as a first-class artefact; grounds: his call, small
  cost). Signing defaults + keep-separate counsel **accepted as-is** —
  binary exits, new-machine red-until-key, two instruments; that 🎯 closes
  with no work owed.
- **ccarchive capture widened — BUILT 2026-07-23** (`3c6394d`, merged
  `2df595e`): all four ruled classes first-class end-to-end, exclusions
  now documented in a man-page CAPTURE section, 150 tests green. One
  operator note: the shrink guard covers memory files uniformly, so a
  legitimately condensed memory file needs `--force` — safe-over-silent.
  Detail → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

### ccrepo (Mike, 2026-07-17)

Reconciliation drift closed 2026-07-22 (richest-record dedup; exact ccusage
match on frozen data); spend-config fill closed 2026-07-23 (populated from
real receipts, machine-local) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- **Archive sourcing (the ccrepo half of the seam)**: cctranscript reads
  ccarchive's mirror since 2026-07-23 (`--archive` — ROADMAP-DONE); ccrepo
  still reads only the live dir, so its month/quarter rollups stop at Claude
  Code's prune horizon. Same shape when picked up: transparent gunzip behind
  one read choke-point, eviction-aware walking (never bulk-fault an iCloud
  dataless archive back to disk — see cctranscript's port of ccarchive's
  SF_DATALESS check).

Completed instruments work (ccrepo actuals/breakdown, ccarchive integrity/audit,
the **man-page convention rollout — ccarchive worked example + cctranscript +
ccrepo, all installed CLIs now carry a `man/<tool>.1` + trimmed `--help`, closed
2026-07-21**) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## File-size hygiene (new 2026-07-14)

The generalised anti-bloat work. `sizescan` flags relocatable **cold content** on
the hot path across the fleet (and reports size as advisory); these are the
outstanding strands.

Completed file-size work (the 2026-07-14 sizescan build/review + wiring; the
2026-07-18 fleet harvests — ros 7123→982 in two ruled stages, faves, shed; the
grounded-budgets correction; the 2026-07-19 tripwire-split application, superseded
by the cold-content rebalance; the **2026-07-20 size-signal rebalance to a
cold-content gate + its rule-4 review (PASS 0M/2M/3L) + Mike's accept-all ruling
applied 2026-07-21**; the fleet-wide `hooks.atelierTools` fix) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).
- [ ] **Existing fleet children pick up the reworked `floor.yml` gate** — children
      copy `floor.yml` statically, so they adopt the cold-content gate at their
      next pin bump / harvest. **At the same bump, apply the 2026-07-23 trigger
      ruling (Mike): private children that take no fork PRs drop the
      `pull_request` trigger** — halves metered-minute burn; the merge-preview
      scan is consciously traded away where the owner is the only contributor;
      public children keep both (free). They also inherit the SHA-pinned
      actions + the SECURITY.md template from the security-canon close. **The rebalance dissolves the all-open-roadmap
      red**: a wholly-open ROADMAP (ros's ~125 open items) no longer reds on
      length — with no cold content to relocate it is advisory now, not a standing
      red — so the class-grounded-budget workaround is no longer needed for that
      case. A child that still reds does so on un-harvested `[x]` items, its own
      harvest lane. faves and ros run bespoke CI without `sizescan --check` — a
      separate floor-adoption step.

## North star — context follows the person, work follows anywhere

- [ ] **Two-tier person-context portability.** **Design pass DELIVERED
      2026-07-22** →
      [`sessions/2026-07-22-1233-person-context-portability-design.md`](sessions/2026-07-22-1233-person-context-portability-design.md)
      — constraints C1–C8 from cited doctrine, an 8-threat pass, candidate
      architectures per leg, argued recommendations (tier-1 filesystem:
      age/sops capsule, decrypt-on-need; tier-2: estate-root private repo +
      wrong-tier gate; tier-1 phone: out of scope app-native, phone-as-
      terminal when needed; tier-2 phone: app memory as a declared, dated
      second system; seam: filesystem canonical, phone derived). Records-
      only; review WARRANTED when it moves to build/doctrine.
  - **D1–D5 RULED 2026-07-23** (plain-language walk-throughs; stamps and
    grounds in the design record §Decision stamps): D1 the capsule rides
    the private estate repo (plaintext-binding reading confirmed); D2+D4
    **full app-plane parity, superseding the design's counsel** — both
    tiers reach phone/web/desktop-app memory as a generated, date-stamped
    profile (grounds recorded: no phone-unique risk; tier-1 already
    transits the provider in filesystem-leg conversations; standing
    memory deletable); D3 ADP enabled and may be load-bearing; D5 the key
    backup lives in the person-level credential home.
  - [ ] **Build the capsule** — encrypt tier-1 into an age capsule with
        per-machine keys, estate-repo carrier (D1), decrypt-on-need
        unlock, key backed up per D5. Gated on writing the
        **tier-classification rule** (what makes a fact tier 1 — a
        doctrine act) and the wrong-tier pre-commit gate (design §5).
  - [ ] **App-plane profile generator** — render the date-stamped
        both-tier profile from the canonical store for the app's
        memory/Projects (D2/D4 parity ruling); define the reconcile
        cadence; the one-directional seam holds (filesystem canonical).
      Original item, for context: both excluded from atelier, both
      must reach every device Mike works from, handled by sensitivity:
      - *Crown-jewels* (health/family/finance/estate map): E2E-encrypted only
        (iCloud ADP or sops/age); **never a plain remote, not even private
        GitHub**; encrypted at rest even locally; device floor (FileVault/
        passcode).
      - *Instance/identity/toolbox* (accounts, venv paths, domains, client-entity
        facts): private but lighter; may tolerate a private store/repo.
      Honest gap: the **iPhone leg has no filesystem mechanism** — the Claude app
      doesn't read `~/.claude`; phone-side is app memory/Projects, a different
      system. This needs a focused design pass, not "a sync problem".
- [ ] **Resume any project from any device, anywhere** — depends on propagation
      + person-context above.

## Session archive — decided 2026-07-23

Superseded by ccarchive (Mike's ruling, plain-language walk-through): the
nightly iCloud archive under ADP-class E2E answers the original item's
encryption concern; one archive, tamper-checked, capture widened same day
(sidecars + memory + prompt history). Consciously not taken: the NAS
second leg and a rolling-retention clock — history is kept indefinitely
unless Mike asks for a retention rule. Detail →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Sharing — public since 2026-07-10 (ADR 0005)

The private-first sequence (peer-adoption → restructure → *then* public) was
consciously collapsed: the peer-of-two never became a peer-of-three, so **public
is the friction mechanism**, not a reward withheld until after it. atelier is
public as a **named worked example** (README "If you're adopting this"). What was
"before public release" is now **post-public hardening**:

- [ ] **One real peer adoption** (CEL, then a client-org) — still the highest-value
      hardening; now happens *with* strangers able to read it too. Treat their
      confusion as the harvest.
- [ ] **Practice/instance restructure** of AUTONOMY + STORAGE — the person-local
      specifics (grant ledger, Apple/iCloud) → marked worked-examples. No longer
      a publication gate; do it as the named-worked-example framing gets tested by
      a real adopter.
- [ ] **Exercise the interactive fill + bundled-mode scaffold end-to-end**
      — owed post-ship; both flagged unexercised (model-prose, proven at
      use) in the CHANGELOG's own honesty note. Per VA2 (2026-07-23) the
      exercise now includes the **plugin-update case**: install 0.2.0,
      scaffold bundled-mode, update the plugin, observe whether the stamped
      `<plugin-path>` tracks, dangles, or goes stale — then reconcile
      `commands/install-hook.md`'s dangling-path wording and make the
      variant's drift bullet state what a missing path means. No text change
      before the observation (the honest fix is the exercise, not a guessed
      sentence).

Completed sharing work (public release, the plugin bundle widening, atelier's own
CI, child-CI scanner floor, linkscan build + wiring) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Open questions

- **Checkbox grammar RULED 2026-07-23 (Mike): keep the tri-state** — the
  bracket answers the one machine-checked question (is work owed?);
  dispositions live in dated notes. Promote to five states only if we find
  ourselves repeatedly grepping dispositions apart (the promotion rule).

- Does ros keep canonical copies of any doctrine, or hold only bearings + point
  up for everything (as §0 now does)? Default: point up; resolve per doc at
  extraction.
- **Floor template's duplicate trigger — RULED 2026-07-23 (Mike): trim
  `pull_request` on no-fork private children**, applied per child at its
  next pin bump (standing guidance now in the fleet-adoption item above);
  public children keep both triggers (free). The template itself stays
  two-trigger — it serves public repos too, and the N4 publish-safety
  rationale holds there. Full two-sided analysis preserved →
  [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- [ ] **Map and understand the difference between honesty (that claude does
      well), the truth, and transparency** — MIKE'S raw note, to be fleshed out
      BY MIKE before anyone interprets it: it is fundamental to atelier (apex-
      level, touches 00-APEX.md) and he wants to define it himself. Do NOT
      elaborate, reframe, or seed a design around this line until Mike has
      expanded it. Prompt him with exactly this line. (Mike, 2026-07-22.)
- [ ] **Grab the AI chat (Teams, 15/7/26) with a colleague** — MIKE'S raw
      to-do, to be fleshed out and positioned BY MIKE before anyone interprets
      it. The export is held locally/privately; the full verbatim pointer
      (name + path) is kept in Mike's private note, deliberately NOT published
      here (atelier is public). Do NOT interpret until Mike expands it.
      (Mike, 2026-07-22.)
The `MODEL-ECONOMICS.md` → `ECONOMICS.md` rename was executed 2026-07-22
(nothing dangles; children re-point at their next pin bump) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

Resolved questions (docker-heap standardisation, estate credential governance) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
