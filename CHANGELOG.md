# Changelog

All notable changes to atelier. Format: [Keep a Changelog](https://keepachangelog.com/);
newest first. Everything stays under _Unreleased_ until there's a reason to tag.

## [Unreleased]

### Added (2026-07-10 — build/ layer: the repo standard extracted (A10))
- `docs/build/REPO-STANDARD.md` — the repo-craft standard extracted from the
  `create-repo` skill into readable, forkable doctrine: product-in-a-subfolder
  (+ why), sizing the standard to the repo type, the standard file set,
  **honest-CI** (a green check that proves nothing is the phantom-success
  `method/` forbids an instrument), repo-craft conventions, and the two processes
  (new repo / standardise an existing one). It owns repo *shape* only and points
  up to `method/` for the cross-cutting doctrine (EVIDENCE for grounded-not-
  invented, RECORD for SESSIONS/ADRs/why-comments, REVIEW for the reviews/ briefs,
  PROPAGATION for the CLAUDE.md doctrine block, AUTONOMY for private-first) rather
  than copying it. Instance-local specifics (exemplar repos, git identity, `gh`
  account, workspace path, locale) stay in the delivery vehicle (the skill).
- `docs/build/README.md` rewritten from "pointer, not yet extracted" to the layer
  index; still-owed list now names templates-move, rewire-skill-to-inherit,
  supply-chain/release, and repo-boundary guidance.

### Changed (2026-07-10 — harvest extraction: A6 + A7, the last of the extraction section)
- `docs/method/EVIDENCE.md` gains **§13 source-acquisition escalation ladder**
  (harvest A6) and **§14 honest-instrument doctrine** (harvest A7). §13 is the
  active counterpart to §3: when a claim matters more than its current rung
  supports, climb the recall→snippet→fetch→tool-call→corroborate→reproduce
  ladder — the rung set by *the cost of being wrong, not the cost of climbing* —
  and state the gap when blocked rather than promoting a weak rung. §14 turns
  §1–§4 on the tools the agent *builds*: an instrument's own "ok"/"applied" is a
  claim the apex governs — success means verified not attempted, silent success
  is a defect (PRINCIPLES §6), "unknown" is a required output, and a known-failure
  test is the machine enforcement. Closes the extraction section's last line; the
  ros diagnose/apply phantom-success case-law is now named as §14's estate
  instance in the closing bearing.

### Changed (2026-07-10 — salvaged from the parallel review line)
- `docs/method/EVIDENCE.md` §1 gains the **two-register** provenance rule — a
  durable artifact carries provenance *written down*, an in-flight claim carries
  it *on demand* (answer-on-challenge + label-guesses-unprompted); ceremony
  scales with durability, discipline never drops. This was finding E3 in the
  worktree-branch draft of the method-layer review (`atelier-method-review`),
  which main's verdict had judged "§1 holds" and so never applied. Recovered
  during the worktree reconciliation before that branch was retired.

### Changed (2026-07-10 — harvest extraction)
- `docs/method/MODEL-ECONOMICS.md` promoted stub → **canonical**. Keeps the
  stub's match-the-model / which-pool self-check / tiered-authority /
  inline-batched review triggering, and adds the general session-hygiene
  mechanics + cache economics extracted from ros (per-model prompt cache, TTL
  churn, output>input, one-task-per-session, heavy-skills-are-episodic,
  point-don't-paste, keep-the-hot-path-lean). The estate-specific numbers
  (prices, model roster, measured session-overhead) stay person-local in ros; a
  foot-pointer names the split. README + `method/README` swept off "stub".

### Added (2026-07-10 — method-review backlog finding P2)
- `tools/pins.py` — the fleet view of "which children are stale" against atelier
  HEAD, closing the method-review's remaining backlog finding. The per-child
  drift check (PROPAGATION §4) is pull-based; this is the roll-up — stood in
  atelier it reads every child's pin and reports `current`/`behind N`/`ahead`/
  `diverged`/`unknown`/`no-pin`, with `--log` to show the drift a stale child
  would inspect. Deliberately **read-only**: bumping a pin stays the per-repo
  human-in-the-loop act (PROPAGATION §5), so the tool widens observability, not
  enforcement — the honest caveat in PROPAGATION is updated to say exactly that.
  Zero-dep, `--json`/`--check`/`--selftest`, fail-safe exit codes; 12 stdlib
  tests over real throwaway repos (behind/ahead/diverged/unknown/no-pin +
  discovery). Live-proven on the real fleet: faves 9 behind, ros current.

### Changed (2026-07-10 — method-review backlog finding P2)
- `docs/method/PROPAGATION.md` honest caveat acknowledges the fleet pin view
  (`tools/pins.py`) as the per-child → fleet observability widening, restating
  that it changes nothing about enforcement.

### Added (2026-07-10 — records, not doctrine: no method/ change)
- `docs/decisions/` ADRs 0001–0004 for the decided re-litigable questions
  (method-review finding V2): atelier-is-canonical, SHA-is-the-version,
  private-first, Apache-2.0. Deliberations recorded from the session/review
  record; 0004 is honest that the licence landed at scaffold via the house
  convention and records the reasoning that holds it.

### Changed (2026-07-10 — records, not doctrine: no method/ change)
- `docs/SESSIONS.md` split to index + `docs/sessions/<date>-NN-slug.md` detail
  files (method-review finding V3), entries preserved verbatim — the
  index/detail split RECORD.md prescribes, applied to atelier itself.
- ros `docs/PRINCIPLES.md` trimmed to bearings + case-law (the transitional
  DRY breach closed) — the change lives in ros (`73fd50b`); noted here because
  atelier's ROADMAP extraction item tracked it.

### Changed (2026-07-10 — method/-layer Fable review, PASS-WITH-FINDINGS)
- The gated review of the whole `method/` layer ran; verdict in
  `docs/reviews/2026-07-10-method-layer.md`. Ten findings fixed in the same
  commit: the child doctrine block's inlined floor now names **new trust
  surfaces** (deploy keys/webhooks/OAuth grants — was a silent narrowing of the
  AUTONOMY floor; children adopt at their next pin bump); the drift check says
  to bump even on a non-doctrine delta (alarm-fatigue guard); EVIDENCE §4
  scoped to *reported* facts (direct primary observation is its own
  corroboration), §12 names the ephemeral-claim boundary (no validator reaches
  an in-conversation claim), §8's real fleet figure swapped for an invented
  one; REVIEW reframed — independence + fresh context is the irreducible core
  of review, capability the multiplier not the precondition (cross-references
  swept in PROPAGATION + both READMEs), and the disposition set gained
  **[rejected: grounds]** so disagreement is recorded, never silent; RECORD's
  lockstep rule scoped to the integration boundary (a WIP branch may trail
  until it lands); PRINCIPLES §3/§4/§5/§7 got their generalised cases back
  (the preamble's every-principle-carries-a-case claim is now true); stale
  README/CHANGELOG statements about the PRINCIPLES extraction corrected.
  Backlog: fleet-level pin-staleness view; ADRs for atelier's own decided
  questions; SESSIONS.md index/detail split.

### Added
- `tools/secretscan.py` — the detection half of the secrets story: a zero-dep
  pre-commit/CI scan that blocks a plaintext CREDENTIAL from entering git
  history, in *every* repo (a burned secret is burned whatever the repo's
  visibility). Named vendor formats (AWS/GitHub/Slack/Google/Stripe/Anthropic/
  OpenAI/… tokens, private-key/PGP headers, JWTs) flag on shape; a secret-named
  assignment with a high-entropy value catches home-grown secrets. Skips the
  safe indirections (`!secret`, `${VAR}`, `<placeholder>`), code refs, public
  keys and URL paths — validated at **0 false positives** over real tiki source/
  inventory/docs while still catching the fixture-secret shapes. Report redacts
  to length+entropy, never the value. `--staged`/`--json`/`--disable`/
  `--selftest`, `.secretscanignore` + `secretscan:allow`; 47 stdlib tests. The
  shared pre-commit sample now runs both scanners. Pairs with the SECRETS
  doctrine: detect → rotate → the burn cost is minutes.
- `tools/worktree.py` — one command for `CONCURRENCY.md`'s "one worktree per
  line of work": `start`/`list`/`land`/`remove`. Bakes the doctrine's guards into
  the tool — refuses an iCloud base (sync corrupts a live `.git` index), branches
  off the integration branch so a line never inherits a half-done branch, flags
  stale/dirty worktrees (merge hazards + leaked file handles), and refuses to
  delete uncommitted/unmerged work without `--force`. Zero-dep, `--json`,
  `--selftest`, fail-safe exit codes; 12 stdlib tests over real throwaway repos.
  Makes the parallel-work doctrine a tool, not just prose (Mike, 2026-07-10).
- `tools/leakscan.py` — the mechanical leak-scan (first executable control):
  shareable structural patterns + a machine-local literal-term list, run as a
  pre-commit hook and in CI to keep personal/estate data out of a shareable
  repo. Zero-dep, `--json`, self-tested; caught real address/coordinate leaks in
  its own fixtures on first run. `--disable <rules>` + `--staged <subtree>` scope
  it to a networking repo's shareable subtree (proven on ros `tiki/`).
- Initial scaffold: the `method/` layer stands up first.
- `docs/method/00-APEX.md` — honesty is absolute, then the AI-adapted Three
  Laws (extracted from ros `docs/PRINCIPLES.md` §0, generalised estate-wide).
- `docs/method/AUTONOMY.md` — per-repo autonomy framework; reconciles the
  ros (commit-only) vs faves (commit + push, deploy-on-push) grants.
- `docs/method/STORAGE.md` — GitHub master / iCloud backup / Time Machine→NAS
  whole-machine / laptop disposable; keep churn (venvs, caches, worktrees) out
  of iCloud.
- `docs/method/CONCURRENCY.md` — one worktree per line of work; serialise
  real-world side-effects.
- `docs/method/TOOLBOX.md` — keep a tool manifest; approved-but-missing may be
  installed; the personal inventory stays machine-local, not in this repo.
- `docs/method/PROPAGATION.md` — the propagation mechanism: thin-anchor /
  fat-pointer (inlined safety floor + SHA pin + session-start drift check), the
  standard child doctrine block, the layer-override rule, and the enforcement
  clause (read ≠ complied). Versioning decided: the commit SHA is the version;
  CHANGELOG is the human-readable index; tags reserved for milestones.
- `docs/method/EVIDENCE.md` — the machinery behind the apex's honesty (harvest
  A1): authority tiers, acquisition-method error risk, absolute dating,
  store-the-rule-not-the-value, one-fact-one-home, trigger-based refresh,
  invest-where-the-model-is-weak, enforce-by-machine. Generalised from a private
  reference-library `STANDARDS.md`.
- `docs/method/REVIEW.md` — the enforcement half (harvest A2): independent
  review by a more capable model; three lenses; brief-on-top/verdict-below
  lifecycle; inline-vs-batched triggering.
- `docs/method/RECORD.md` — session + doc-as-code discipline (harvest A3):
  lockstep doc change, append-only session log with detail-on-demand, ADRs for
  re-litigable decisions, absolute dating; the record is what makes a session
  resumable cold.

### Changed
- `docs/method/PRINCIPLES.md` — extracted from stub to the canonical general
  spine (§1–7 + precedence ladder + situation tests, generalised off tiki with
  the cases kept). ros `docs/PRINCIPLES.md` is now the *bearings + case-law*
  child that points up; trimming its transitional general-prose duplication is a
  tracked ROADMAP follow-up.
- README, CLAUDE onramp, LICENSE (Apache-2.0), house `.gitignore` +
  `.claude/settings.json`.

### Pending (see ROADMAP)
- The `build/` layer: the `create-repo` standard + templates.
- `create-repo` rewired to inherit from atelier instead of copying empty
  templates.
