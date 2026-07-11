# Changelog

All notable changes to atelier. Format: [Keep a Changelog](https://keepachangelog.com/);
newest first. Everything stays under _Unreleased_ until there's a reason to tag.

## [Unreleased]

### Added (2026-07-11 — PRINCIPLES §8: leverage / "productive laziness")
- **`docs/method/PRINCIPLES.md` gains §8 "Leverage — invest now to stop paying
  later"** — Mike named the principle; strategic laziness is leverage: spend more
  now (a work-avoiding *design*, or a reliable *reusable tool*) to save repeated
  work later and get consistent, robust outputs. Two forms — **design out the
  work** (thin-anchor-fat-pointer, one-source) and **build the reliable tool once**
  (the scan triad; the codified verb that replaced recurring hand-surgery, a §7
  case now generalised; tied to EVIDENCE §14 — the tool is a source, so build it
  tested-and-honest). Plus **the discipline** (payback needs real recurrence, not
  gold-plating; never a shortcut through §0–§2) and a **"One-off or recurring?"**
  situation test. Appended, not renumbered (§5 is cross-referenced; external cites
  of `PRINCIPLES §N` must not shift). Grounded, not invented — the repo already
  instantiates it. **Review-owed** by the ceremony-calibration rule (doctrine text;
  flagged, not self-certified).

### Changed (2026-07-11 — the child-CI-floor review: the masking fix now covers the class)
- **secretscan + leakscan hardened by the child-CI-floor review** (Fable, cold
  session: `docs/reviews/2026-07-11-child-ci-floor.md`, PASS-WITH-FINDINGS,
  N1–N6 all fixed + re-driven; suite 196→205). The review's headline: the
  `d0870a4` linkscan masking fix had closed the *instance*, not the class —
  proven live at review HEAD, a planted `AKIA…` key in `docs/build/` scanned
  **green** whole-tree because both boundary scanners still hardcode-skipped
  `build`/`dist` (N1, now mirrored out); both also **phantom-succeeded on a
  nonexistent path** ("✓ clean", exit 0 — the linkscan L1 silent-success class;
  now exit 2, N2); and the ignore-file hatch was **dead whenever CWD ≠ root** —
  exactly floor.yml's invocation — because globs were matched against
  CWD-relative paths (N3, both sides now resolved, mirroring linkscan's
  reviewed `_rel`). `floor.yml` gains **every-push triggers** (a never-PR'd
  feature branch was scanned by nothing, while the header claimed "every push";
  N4), a **scanner-selftests step** before the scans (N5), and **in-file
  false-positive hatch docs** (N6) — all pinned by new `test_templates.py`
  tests. Floating `atelier@main` was attacked and held: the scanner fixes reach
  every child's next run with zero per-child bumps, which for a security floor
  is the safety property. Follow-up: numen re-copies floor.yml (workflow-file
  fixes don't float).

### Added (2026-07-10 — child CI scanner floor: the public scanners now gate child repos)
- **`docs/build/templates/workflows/floor.yml`** — the CI backstop to the
  pre-commit scan hook, for any repo that inherits house doctrine. The hook only
  guards the clone it's installed in (git transports neither hooks nor config);
  this workflow re-runs the publish/leak scans on every push + PR. It checks
  `mike548141/atelier` out **beside** the repo and runs its public
  secretscan/leakscan/linkscan against the repo's own tree — **one source, no
  vendored copy, no drift**, now possible because atelier is public (ADR 0005)
  and the scanners are zero-dep stdlib. Design calls are in the header:
  **`atelier@main`** floats (a security floor wants the newest scanner; and it
  avoids a second stamped-SHA drift surface — CLAUDE.md's pin stays the only
  doctrine-version truth); **leakscan structural-only** (its term list is
  machine-local — the same honest scope as atelier's own `ci.yml`);
  **licenscan commented** (no-LICENSE hard-fails it, so it's a *publish* gate,
  not an always-on floor for a private child). The scan is scoped to the repo's
  tree, not the whole workspace — atelier's own fake-secret fixtures would
  false-positive otherwise. Proven both ways (clean child 0/0/0; damaged child
  with a real key + broken link blocks) and pinned by 5 `test_templates.py`
  tests (suite 190→195). create-repo seeds it and REPO-STANDARD lists it; the
  skill's "CI scanning not wired yet" note is retired.

### Changed (2026-07-10 — the linkscan review: gate cleared, five assumptions repaired)
- **`tools/linkscan.py` hardened by its own review** (Fable, cold session:
  `docs/reviews/2026-07-10-linkscan.md`, PASS-WITH-FINDINGS, findings L1–L10).
  The brief's five load-bearing assumptions all took damage, proven live before
  fixing: a **typo'd path arg scanned nothing and exited 0** (now a usage error,
  exit 2 — the EVIDENCE §14 silent-success class in a gate-destined tool);
  **case-mismatched links** green on a case-insensitive disk but 404 on GitHub
  (now checked against on-disk casing, unicode-normalisation-safe); links
  **escaping the repo root** (new `outside-root` finding — GitHub serves nothing
  above the repository root); **anchor matching now exact** like GitHub's
  fragment matching, with the fix printed when only the casing is wrong — which
  required teaching the slugger that GitHub *keeps* literal underscores;
  **parenthesised filenames** (`a(1).md`) parse instead of false-positiving;
  **fence tracking** length- and info-string-aware (a ``` inside a ```` block
  stays code) via one shared tracker for links and headings; **setext headings**
  now mint anchors (they were false-positiving valid links, filed under the
  wrong failure class in the residual). Root-relative `/…` semantics verified
  against GitHub's docs (matches). Residual list updated: setext off;
  HTML-minted anchors and indented-code false positives on, the latter
  deliberately unfixed (the fix would cost real false negatives). Suite
  **171→187**, selftest +2 cases, whole tree rescanned clean under the stricter
  checks. **Gate cleared** — wiring into `ci.yml`/`pre-commit.sample` is
  unblocked but left to the next build session (a reviewer doesn't wire its own
  same-day fixes into the gate).

### Added (2026-07-10 — linkscan: the internal-link integrity check)
- **`tools/linkscan.py`** — the mechanical check that atelier's "thin anchor, fat
  pointer" graph (`method/PROPAGATION.md`) actually resolves. A relative link that
  404s — a renamed file, a moved doc, a typo'd `#anchor` — is a silent hole in the
  doctrine graph; this catches it before a reader (or adopter) does. Scope is
  deliberately narrow: **internal `[text](path)` links only** (external schemes and
  `//host` skipped — the network is a flakier tool's job). Two finding kinds:
  `missing-file` (path unresolved, relative to the linking file / repo root for
  `/…`) and `missing-anchor` (a `#fragment` into a Markdown target whose GitHub
  slug matches no heading; `#L42` line refs and non-Markdown anchors skipped).
  Fenced/inline code stripped so example links don't false-positive.
- Same house pattern as the scan triad: zero-dep stdlib, `--selftest`,
  `linkscan:allow` + `.linkscanignore` hatches, fail-safe exit codes (`0` clean /
  `1` break / `2` couldn't-complete — never a silent green). **`tools/test_linkscan.py`**
  adds 26 tests (suite 145→171). Proven live — selftest OK, whole tree clean (55
  Markdown files, 36 internal links), anchor pass/fail + a planted break verified
  against real files. Honest residual added to `tools/README.md`: reference-style
  links, HTML links, setext headings, a `](…)` split across two lines, and slugger
  divergence from full CommonMark are the known blind spots.
- **Review-gated before it becomes a gate** (`docs/reviews/2026-07-10-linkscan.md`,
  brief) — the false-negative surface is the sharpest lens. **Not yet wired into
  `ci.yml`/`pre-commit.sample`**; that wiring waits for the verdict
  (don't-stack-a-gate-on-unreviewed-tooling, third application after the method
  layer and the create-repo mechanism).

### Added (2026-07-10 — atelier's own CI: the floor, dogfooded)
- **`.github/workflows/ci.yml` (job `floor`)** — going public (ADR 0005)
  dissolved the blocker, so the floor every review had been asserting by hand now
  runs on every push and PR: the tool test suite (145 tests), the three scanner
  `--selftest`s, and the scan triad (`secretscan`/`leakscan`/`licenscan
  --expect Apache-2.0`) over the whole tree. Zero-dep stdlib → a runner needs
  only Python.
- **Honest CI scope, in the header not the fine print**: secretscan/licenscan run
  at full cover; **leakscan runs structural-only and deliberately WITHOUT
  `--require-terms`**, because its literal person/estate term list is
  machine-local by design (`~/.claude`, never in any repo) — CI can't hold it and
  must not. Full leakscan cover stays where the term list lives: the pre-commit
  hook on a real machine.
- Least-privilege (`contents: read`), concurrency-cancel for cost hygiene.
  **Live-proven twice on GitHub** — first run green (11s), then `checkout@v5` +
  `setup-python@v6` to clear the Node-20 deprecation annotation, re-run green (7s,
  11/11 steps, no annotation). Watched, not assumed (REVIEW's re-run-live-proven
  rule). The file doubles as the reference a child copies to run atelier's public
  `tools/` in its own CI (that half + a markdown link-check remain open).

### Fixed (2026-07-10 — the create-repo delivery-mechanism review: C1–C10, all fixed + re-driven)
- **The Fable sweep of the rewire ran cold and PASSED-WITH-FINDINGS** (verdict in
  `docs/reviews/2026-07-10-create-repo-rewire.md`); the gate is cleared — keeper
  repos may be scaffolded. Two findings proven live before fixing: **C1** a fresh
  clone of a scaffolded repo lost the hook + `hooks.atelierTools` silently
  (git transports neither) and committed a planted `AKIA…` key green — the
  fail-open class one hop later; now stated at the three places a new clone
  looks (template CLAUDE.md "Hooks don't travel" bullet, CONTRIBUTING
  once-per-clone install lines, the hook header). **C2** the stamped drift
  check broke run-verbatim — the block stamped the atelier path unquoted and
  the house path contains spaces; the canonical block (PROPAGATION) + template
  now quote it, and the skill stamps sibling-relative `../atelier` with a
  mechanical prove-the-stamp (grep unfilled placeholders; run the drift command
  verbatim, expect empty).
- **Template-block drift is now mechanically impossible to miss** (C3):
  `tools/test_templates.py` diffs the template's stamped doctrine block against
  PROPAGATION's canonical text character-for-character on every suite run, and
  pins the four-placeholder set (C4 — PROPAGATION's prose said "three" while
  its own block carried four). Suite 142→145 OK.
- **Honesty sweeps** (C6–C10): the hook's/README's "pair with CI" lines now
  state that child-repo CI scanning is *not wired yet* (the hook is a child's
  only scan gate — deferred scanner-distribution call); `templates/LICENSE`
  added (Apache-2.0 verbatim; was copied from faves — a second source with no
  target line for "set the holder"); the `ATELIER_TOOLS` trust surface stated
  in the hook header; skill step 7's `gh repo create` re-anchored to Mike's
  ask (not "push is recoverable"); the atelier-present precondition now checks
  the templates are *readable*, not just that the path exists (iCloud
  eviction).

### Fixed (2026-07-10 — create-repo scaffold exercised end-to-end; scan-hook fail-open defect closed)
- **The scaffolded scan hook silently protected nothing.** Exercising `create-repo`
  on a real local scaffold (the owed real-scaffold run) surfaced a defect the
  session-18 scratch dry-run couldn't: `tools/pre-commit.sample` hardcoded the
  scanners at `$repo_root/tools/` and **failed open** (`[ -f ] → skip`) when they
  were absent. A child repo has no scanners of its own — they live only in atelier
  — so its copied hook waved *every* commit through, secrets included (proven: a
  commit carrying a real `AKIA…` key went straight into history). The "costume,
  not doctrine" failure one layer down, and a textbook §14 silent-success defect.
- **Fix — resolve up + fail closed.** The sample now resolves atelier's tools dir
  (`ATELIER_TOOLS` env → `git config hooks.atelierTools` → in-repo fallback, so
  atelier itself still works) and **blocks the commit with an explanation** when a
  scanner it is configured to run is missing — a gate that can't scan must never
  pass silently. `create-repo` step 6 now bakes the path
  (`git config hooks.atelierTools "$PP/atelier/tools"`) and prove-it-once
  instructions. Re-exercised: fail-closed with no config, blocks a real secret
  with config, passes a clean commit, atelier's own path unaffected. Suite 137 OK.
- **The fix's contract pinned by tests** (same day, follow-on): the hook was the
  one scan artifact with *no* automated tests — exactly where the defect lived,
  and the live re-proof was one-time (the B1 lesson: a recorded proof can be
  stale by the time it's durable). `tools/test_precommit.py` added — 5 tests
  driving real `git commit`s in throwaway repos: fail-closed when unresolvable,
  config-resolution blocks a planted secret / passes clean, env-wins-over-config,
  in-repo fallback. **Known-failure proven**: the pre-fix sample re-run under the
  same scenario commits the secret with exit 0 — the tests catch the defect
  class, not just bless the fix. Suite 137→142 OK; tools/README wiring section
  now documents `hooks.atelierTools`/`ATELIER_TOOLS` + fail-closed.
- **Owed, surfaced not fixed:** CI templates carry *no* scanner step, so a
  scaffolded repo's only scan gate is the machine-local hook — the "pair it with CI"
  line in both the sample and step 6 is currently unbacked. Wiring scanners into CI
  needs the scanner-distribution decision (vendor / fetch atelier / publish) — the
  deferred supply-chain question; recorded in ROADMAP, not half-built here.

### Changed (2026-07-10 — create-repo rewired to inherit; templates moved into build/)
- **The core Q1 fix landed.** `create-repo` no longer re-encodes the standard from
  memory — it now **inherits from atelier** (the source) and **stamps the standard
  doctrine block + SHA pin** into every new repo's `CLAUDE.md`. The gap this
  closes: the skill had *no CLAUDE.md template at all*, so new repos were born
  with no inlined safety floor, no pointer up, no drift check — the whole
  `PROPAGATION.md` mechanism bypassed at birth. No delivery path now leaves a repo
  wisdom-empty.
- **Templates moved** from the skill's private copy into `docs/build/templates/`
  (18 files) — one source shared by the skill and the published methodology, per
  REPO-STANDARD's decided direction. Added the missing **`CLAUDE.md` template**
  carrying the stamped doctrine block (canonical text stays in PROPAGATION.md).
  Scrubbed of instance residue as they crossed into the shareable repo: `NOTICE`
  holder hardcoded to a company → `<copyright holder>`; `ci-static.yml` project
  name "Nova" → generic; `reviews/README.md` static-web-specific examples →
  type-neutral. Caught one **live drift** that grounds the whole one-source move:
  the `MODEL-ECONOMICS` template still named **ros** as canonical months after it
  was extracted to atelier — fixed to point up to atelier. Verified: residue grep
  clean, `leakscan` clean on the subtree.
- REPO-STANDARD + `build/README.md` updated from "owed" to done: templates now in
  `build/templates/`; the skill *inherits + stamps* rather than re-encodes; the
  seed→rename→fill→stamp→scan→push procedure documented. The skill is machine-local
  (delivery vehicle); it carries only instance specifics (exemplars, git identity,
  `gh` account, `$PP`, default holder, locale) and hard-depends on atelier being
  present — failing honestly if it is not. The stamp's mechanical core was
  dry-run-proven in a scratch scaffold (seed+renames, sizing, all four
  placeholders filled, the drift-check ran verbatim and read "current"); a
  real-repo run (`gh` create + hook install) and a Fable sweep remain owed.

### Changed (2026-07-10 — the post-method-review batch review, PASS-WITH-FINDINGS)
- The gated Fable sweep of `957fa08..f72031c` ran (verdict below the divider in
  `docs/reviews/2026-07-10-post-method-review-batch.md`): floor green (3
  selftests, 137 tests, live runs), 16 findings B1–B16 — every one carrying an
  in-repo fix applied and verified same session, plus two backlog strands (the
  ros access map from B14; a REVIEW.md lifecycle line). The two sharpest were honesty defects of the class the batch
  itself codified: **B1** — the licenscan "live-proven clean" claim was false at
  the commit that recorded it (the scan flagged its own unexempted test
  fixtures; fixed with `.licenscanignore`, re-proven exit 0); **B14** — ACCESS
  pointed at an estate access map ros doesn't hold (wording corrected to honest
  status; ros owes the map). Tool fixes: **B2** `-only`/`+` SPDX suffixes now
  normalise (a `GPL-2.0-only` header mis-tiered block→warn); **B4** `--staged`
  now uses `--diff-filter=ACMR` in both scanners — a renamed-and-edited file's
  added lines were invisible to the hook hot path (proven live both ways);
  **B5** leakscan `--require-terms` fails closed (exit 2) when the local list is
  absent, for hooks/CI expecting full cover; **B7** `tools/README.md` gains
  "What these scans cannot see" — the stated residual false-negative surface.
  Doctrine fixes: REPO-STANDARD's subfolder rule scoped to deployable-artifact
  repos (B8) + no-gate-must-be-stated (B9); RECORD gains the comments-say-*why*
  rule REPO-STANDARD already pointed at (B10); SECRETS gains the honest boundary
  (master-key loss is redundancy-guarded; person-level vault out of scope, B12);
  ACCESS owns its step-5 strengthening + states the one-broad-credential
  fallback (B13); EVIDENCE §13 gains the §11/§13 stakes-win tiebreak (B15);
  REPO-BOUNDARY gains split-*promptly* (B16). Suite 133→137. **The review gate
  is cleared; the create-repo rewire may stack.**

### Added (2026-07-10 — licence-consistency pre-publish gate)
- `tools/licenscan.py` (+ `tools/test_licenscan.py`, 35 tests) — the third
  pre-publish scan, completing the triad: leakscan (no personal data) · secretscan
  (no credentials) · **licenscan (no licence surprise)**. Three checks: LICENSE
  present and SPDX-recognised; every licence declaration (pyproject/package.json/
  Cargo/gemspec/setup.cfg/README badge) agrees with it; no incompatible
  `SPDX-License-Identifier` header (copyleft-into-permissive is a block — can't be
  relicensed on publish). Conservative + advisory (flags for a human, not legal
  advice), `--expect <SPDX>` assertion for CI, zero-dep stdlib, allow-marker +
  `.licenscanignore` escape hatches, `--selftest`. A pre-publish gate, not an
  every-commit hook (private repos carry licence mess harmlessly; it bites at the
  public boundary AUTONOMY already gates). ~~Live-proven clean on atelier itself
  (`--expect Apache-2.0`).~~ *(Correction, 2026-07-10 review B1: false at the
  commit that recorded it — the scan flagged its own unexempted test fixtures.
  Fixed and re-proven clean the same day; see the review entry above.)*
  tools/README documents it; suite 98→133. Reviewed 2026-07-10 (B1–B3).

### Added (2026-07-10 — access onboarding doctrine)
- `docs/method/ACCESS.md` — safe-access-onboarding: the ordered runbook for the
  moment access to a new domain (network/cloud/NAS/workspace/API) is granted.
  Invents no rule; **sequences** the existing ones — grant-recorded-not-originated
  (`AUTONOMY`), narrowest-credential + plane-split, credential-into-store-first
  (`SECRETS`), read-only first ring + reconcile-or-stop (`DATA-PROTECTION`),
  destructive gate encoded *before* destructive power, widen-in-rings each ring
  earned, Zero-Trust the new domain. The active onboarding counterpart to the
  DATA-PROTECTION/SECRETS/AUTONOMY posture; encodes the estate-access expansion as
  doctrine instead of memory. The concrete estate access map stays person-local in
  ros (sensitive topology, protected under DATA-PROTECTION). Slotted into
  method/README as #6 (after SECRETS); the rest renumbered. Reviewed 2026-07-10
  (batch review — B13 strengthening owned + fallback, B14 access-map claim
  corrected; see the review entry above).

### Added (2026-07-10 — the secrets doctrine)
- `docs/method/SECRETS.md` — the *make-rotation-cheap* half that the leak/secret
  scans' *detect* half depends on; extracted from ros §5 (credential triad) + §7
  (secret-store-not-exempt). Reproducible / re-mintable as the enabling property
  (internal secrets rotate mechanically, external re-mint from code behind one
  approval — no hand-kept irreplaceable token); the least → JIT → short-lived
  triad with standing credentials as a tracked debt, not a resting state;
  references-never-values in the right plane (config/device/shareable-repo hold a
  reference, the value lives only in the encrypted store, scans enforce it);
  rotation-on-cadence bounds the undetected-exposure window. Completes the
  *detect → rotate → burn-cost-is-minutes* arc and closes `AUTONOMY.md`'s
  forward-reference to "the secrets doctrine". Instance mechanism (sops+age,
  `!secret` syntax, the credential map) stays in ros. Slotted into method/README
  as #5 (after DATA-PROTECTION); the rest renumbered.

### Added (2026-07-10 — build/ layer: repo-boundary guidance)
- `docs/build/REPO-BOUNDARY.md` — the decision before the standard: whether a
  piece of work is its own repo, a component (folder in an existing repo), or a
  monorepo folder. Decided by independent-lifecycle discriminators (visibility,
  release cadence, ownership/access, reuse, blast radius) rather than size; a repo
  is a unit of independent lifecycle (loose-coupling from PRINCIPLES applied to the
  boundary). The rich client engagement is the worked monorepo case. Standing
  behaviour: advise proactively. When ambiguous, prefer the reversible direction —
  split later is cheap, merge is painful. Indexed in build/README; removed from
  its still-owed list.

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
