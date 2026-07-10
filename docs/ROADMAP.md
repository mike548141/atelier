# atelier ROADMAP

Lean; read every session. Completed detail moves to `ROADMAP-DONE.md` once this
grows. Sequencing rule from the 2026-07-10 review: **mechanism before more
content** — a repo that inherits docs but not the propagation + review cadence
has inherited the costume, not the doctrine.

## Done (2026-07-10)

- [x] Scaffold + method/ first slice: `00-APEX`, `AUTONOMY`, `STORAGE`,
      `CONCURRENCY`, `TOOLBOX`.
- [x] Foundation review (2 Fable + 1 harvest) — `docs/reviews/2026-07-10-…`.
- [x] Autonomy floor closed (self-widening, lockout-class, GitHub-surface,
      deploy carve-out, recoverability-ends-at-push, pull-quote) + global
      commit/push/PR grant.
- [x] **Canonicality decided** (atelier canonical; children point up) and the
      active APEX↔ros §0 DRY breach fixed — ros §0 shrunk to inlined floor +
      pointer (first instance of the anchor pattern).
- [x] All-models-one-doctrine stated (APEX "who it binds"); review-trigger
      policy + tiered-authority in MODEL-ECONOMICS.

## Next — the propagation mechanism (do BEFORE further extraction)

The load-bearing architecture, review-endorsed shape: **"thin anchor, fat
pointer"** (dependency + lockfile for doctrine). Written up in
`docs/method/PROPAGATION.md` (2026-07-10).

- [x] **Version atelier** — decided: the **commit SHA is the version** (no tag
      ceremony); CHANGELOG is the human-readable index; tags reserved for
      milestones. One CHANGELOG line per doctrine change.
- [x] **Define the standard child CLAUDE.md doctrine block** — inlined safety
      floor (apex + always-confirm) + pointer + SHA pin + one-line drift check
      (`git -C <atelier-path> log --oneline PIN..HEAD`) riding the session-start
      read + a stated **repo-visibility fact** (verifiable via `gh repo view`).
      Canonical text lives in `PROPAGATION.md`.
- [x] **Retrofit `faves` and `ros`** with the block (stamped at the mechanism's
      commit SHA).
- [x] **Layer-override rule** into `method/`: a child may narrow or append,
      never silently contradict; a contradiction is a defect to surface.
      (`PROPAGATION.md` § layer-override rule.)
- [x] **Enforcement clause** (the category error, in writing): documents are the
      standard; the review-with-a-more-capable-model practice is the enforcement.
      (`PROPAGATION.md` § enforcement clause.)

## Review gate — before more content stacks on the method/ layer

The "mechanism/review before more content" rule: the keystone + the whole `method/`
layer earn a review with fresh context before extraction continues.

- [x] **Fable review of the `method/` layer** — RAN 2026-07-10:
      **PASS-WITH-FINDINGS**, verdict below the divider in
      `docs/reviews/2026-07-10-method-layer.md`. Architecture holds; 10
      findings [fixed] same session (trust-surface floor gap, drift-check
      alarm-fatigue guard, EVIDENCE §4 scope + §12 boundary, REVIEW reframe +
      [rejected] disposition, RECORD integration-boundary lockstep, PRINCIPLES
      missing cases, stale README/CHANGELOG). **The gate is cleared —
      extraction may resume.** Notably: the sharpest ask's premise was
      corrected, not confirmed — Fable is the *more* capable tier (the reframe
      to independence-as-core still landed, for peer adopters without a
      superior tier).
- [ ] **Method-review follow-ups ([backlog] findings)** — remaining: faves
      adopts the P1 floor wording at its next pin bump (surfaced now by
      `tools/pins.py` — faves reads 9 behind).
      - [x] P2 fleet pin view — DONE 2026-07-10 (Opus): `tools/pins.py`, the
            read-only roll-up of every child's pin vs atelier HEAD
            (`current`/`behind N`/`ahead`/`diverged`/`unknown`/`no-pin`, `--log`/
            `--json`/`--check`/`--selftest`); 12 stdlib tests; live-proven
            (faves 9 behind, ros current). PROPAGATION honest caveat updated to
            acknowledge it as observability-not-enforcement.
      - [x] V2 ADRs — DONE 2026-07-10 (Fable): `docs/decisions/0001–0004`
            (canonicality, SHA-as-version, private-first, Apache-2.0).
      - [x] V3 SESSIONS split — DONE 2026-07-10 (Fable): index +
            `docs/sessions/` detail files, entries preserved verbatim.

## Then — extraction (keep the case-law, don't strip it)

Generalise the *bearings/cases*, don't delete them (a de-cased principle is
theatre). Leave tiki-specific bearings + review case-law in ros.

- [x] **`PRINCIPLES.md`** spine + precedence ladder + situation tests, with
      generalised cases. Extracted 2026-07-10; canonical here.
- [x] **Trim ros `docs/PRINCIPLES.md`** — DONE 2026-07-10 (Fable, ros
      `73fd50b`) per the verdict's trim guidance (lens-1 answer 12): kept the
      §0 bearing, every Tiki-bearing/Already-holds line, the seven-tenet ZT
      estate mapping, and the whole precedent-annotated trade-offs section;
      dropped only the general prose the spine states. The transitional DRY
      breach is closed.
- [x] **`MODEL-ECONOMICS.md`** general shape — DONE 2026-07-10 (Opus): promoted
      stub → canonical. Match-the-model-to-job + which-pool self-check + tiered
      authority + inline/batched review triggering (already in the stub) plus the
      general session-hygiene mechanics + cache economics extracted from ros
      (per-model cache, TTL churn, point-don't-paste, one-task, heavy-skills).
      Person-local numbers (prices, model roster, 35k overhead) stay in ros; a
      foot-pointer names the split. README + method/README swept off "stub".
- [x] **`EVIDENCE.md`** (harvest A1 — highest-value net-new) — authority tiers,
      acquisition-method error risk, absolute-dating, store-the-rule-not-the-value,
      one-fact-one-home, trigger-based refresh, enforce-by-machine; mechanically
      hardens the apex. Generalised from a private reference-library `STANDARDS.md`.
- [x] **Peer-review lifecycle** doc (harvest A2 → `REVIEW.md`) +
      **session/doc-as-code discipline** doc (harvest A3 → `RECORD.md`) — both
      written 2026-07-10; close the enforcement-clause forward-references.
- [x] **Model-capability authority** section in AUTONOMY (harvest A4 — the
      *who-acts* axis; "policy in memory protects nothing — encode it").
      Ratified by Mike 2026-07-10; written into `method/AUTONOMY.md`.
- [x] **Source-acquisition ladder (A6) + honest-instrument (A7)** — DONE
      2026-07-10 (Opus): `EVIDENCE.md` §13 (climb the acquisition ladder to the
      *cost of being wrong*, state the gap when blocked) + §14 (an instrument the
      agent builds is a source; its "ok"/"applied" is a claim the apex governs —
      verified-not-attempted, silent-success-is-a-defect, "unknown"-is-required,
      known-failure-test enforces). Grounded in §3/§11 and PRINCIPLES §6; ros
      diagnose/apply phantom-success named as the estate instance. Closes the
      extraction section. Reviewed 2026-07-10 (batch review — holds; B15 §13/§11
      stakes-win tiebreak added).

## Review gate — the post-method-review batch (before more content stacks)

The same "mechanism/review before more content" rule that gated the `method/`
layer now gates everything built since it. Session 15 flagged this as the
standout debt; sessions 14–15 deliberately did not stack on it.

- [x] **Fable sweep of the `957fa08..f72031c` batch** — RAN 2026-07-10 (Fable,
      fresh session): **PASS-WITH-FINDINGS**, verdict below the divider in
      `docs/reviews/2026-07-10-post-method-review-batch.md`. Floor green (3
      selftests + 133→137 tests + live runs), doctrine grounded, ros cross-read
      done. 16 findings B1–B16, **every one carrying an in-repo fix, applied +
      verified same session**; two backlog strands remain below. The two
      sharpest: B1 a "live-proven clean" claim false at the commit that
      recorded it — licenscan flagged its own unexempted fixtures; B14 ACCESS
      pointing at an estate access map ros doesn't hold. Scan fixes re-run
      clean; B4 (renamed-file staged hole) proven live both scanners. **The
      gate is cleared — the create-repo rewire and further stacking may
      resume.**
- [ ] **Batch-review follow-ups ([backlog] findings)** — the consolidated item:
      - [ ] **ros: first consolidated estate access map** (B14) — domains
            onboarded / credential per domain / plane split / rings walked;
            sensitive content, a ros session's job (seed from the nas02/tiki
            facts SPECS already scatters). ACCESS.md now states the honest
            status until it exists.
      - [x] **REVIEW.md addition** — DONE 2026-07-10 (Opus): new "Re-run every
            'live-proven' claim in scope" subsection — a recorded proof is a
            claim that can be stale by the commit that records it, so a review
            re-runs the work's asserted proofs, not just reads them. Grounded
            twice (B1 the scan's stale "live-proven clean"; C2 the stamped drift
            check that broke run-verbatim). Review-owed like any doctrine edit.

## build/ layer + inheritance delivery

- [x] **Extract the `create-repo` standard into `docs/build/`** — DONE
      2026-07-10 (Opus): `docs/build/REPO-STANDARD.md` (product-in-subfolder + why,
      sizing-to-type, the standard file set, honest-CI, standardise-existing
      process, repo-craft conventions), pointing up to `method/` for the
      cross-cutting doctrine (EVIDENCE/RECORD/REVIEW/PROPAGATION/AUTONOMY) instead
      of copying it. build/README rewritten from pointer → layer index. Reviewed
      2026-07-10 (batch review — B8 subfolder rule scoped to deployable-artifact
      repos, B9 no-gate-must-be-stated, B10 RECORD gained the pointed-at
      comments rule, B11 templates/staleness swept). Instance specifics stay in
      the skill. Templates-move + rewire-to-inherit remain (below).
- [x] **Licence-consistency pre-publish gate** (A11) — DONE 2026-07-10 (Opus):
      `tools/licenscan.py`, the third pre-publish scan (leakscan · secretscan ·
      licenscan). Three checks — LICENSE present + SPDX-recognised, every
      declaration (pyproject/package.json/Cargo/gemspec/setup.cfg/README badge)
      agrees, no incompatible `SPDX-License-Identifier` header (copyleft-into-
      permissive blocks). Conservative + advisory, `--expect <SPDX>` for CI,
      zero-dep, allow-marker + `.licenscanignore` hatches, `--selftest`. 35 tests
      (suite 98→133). *Correction (2026-07-10 review, B1): the original
      "live-proven clean on atelier" claim here was **false at the commit that
      recorded it** — the scan flagged its own unexempted test fixtures at HEAD;
      any mid-build clean run didn't survive to the commit. Fixed (`.licenscanignore`,
      same reasoned exemption as the sibling scans) and re-proven:
      `--expect Apache-2.0` exit 0 at the review session's close.* Reviewed
      2026-07-10 (the batch review, B1–B3 fixed: `-only`/`+` SPDX suffixes,
      prose-header residual stated).
- [ ] **Supply-chain/release standard** (A5) — committed deterministic SBOM +
      keyless signing. DEFERRED: SBOM/signing needs external tooling (syft/cosign),
      which hits the tool-install floor + breaks the zero-dep house-tool pattern —
      a deliberate design call, not a build. Revisit when a real release needs it.
- [x] **Rewire `create-repo` to inherit from atelier** — DONE 2026-07-10 (Opus):
      the core Q1 fix. The skill now inherits from atelier (points up to
      REPO-STANDARD/REPO-BOUNDARY/PROPAGATION, seeds from `build/templates/`)
      instead of re-encoding the standard, and **stamps the doctrine block + SHA
      pin** into every new repo's CLAUDE.md — the skill had *no CLAUDE.md template
      at all*, so PROPAGATION was bypassed at birth. Templates moved skill→
      `build/templates/` (18 files, one source), the missing CLAUDE.md template
      added, three instance-residue scrubs + one live ros-is-canonical drift fix;
      leakscan clean. Skill stays machine-local (delivery vehicle), hard-depends
      on atelier, fails honestly if absent. Stamp core dry-run-proven in scratch
      (renames + all four placeholders + drift-check runs "current"); real-repo
      run (`gh` create + hook install) + Fable sweep owed. Review-owed.
  - [x] **Real-scaffold exercise — DONE 2026-07-10 (Opus):** scaffolded a real
        local git repo from the templates (seed → 3 renames → stamp → hook →
        commit) and drove the hook end-to-end. Surfaced + fixed a live
        **scan-hook fail-open defect** the scratch dry-run couldn't:
        `tools/pre-commit.sample` pointed at `$repo_root/tools/` and skipped
        silently when the scanners were absent — a child has none (they live in
        atelier), so its hook committed a real `AKIA…` secret. Fixed to resolve
        atelier's tools (`ATELIER_TOOLS` → `git config hooks.atelierTools` →
        in-repo fallback) and **fail closed**; step 6 bakes the path + a
        prove-it-once check. Re-proven: fail-closed / blocks-secret / passes-clean
        / atelier-unaffected, then pinned by `tools/test_precommit.py` (5 tests,
        known-failure proven against the pre-fix sample; suite 137→142 OK).
        **Still owed:** the single `gh repo
        create --push` step (not run — outward, unneeded for a throwaway); the
        Fable sweep (now briefed — gate below); and **CI scan wiring** — CI
        templates run no scanner, so the hook is a scaffolded repo's only scan
        gate (needs the scanner-distribution call: vendor / fetch atelier /
        publish — folds into the deferred supply-chain item).

## Review gate — the create-repo delivery mechanism (before it scaffolds a real repo)

The same rule, third application: the mechanism that stamps doctrine into every
future repo must itself be reviewed before it's *used in anger*. Brief written
2026-07-10: `docs/reviews/2026-07-10-create-repo-rewire.md` — range
`f72031c..92c0112` **plus the machine-local skill** (outside the repo; no other
review will catch it). Nine load-bearing assumptions to attack; the sharpest:
clone-loses-hook-and-config (does protection evaporate on machine two?),
template-block drift vs PROPAGATION's canonical text, and prose-stamp-procedure
as model-memory reborn. **Run cold, fresh session.**

- [x] **Fable sweep of `f72031c..92c0112` + the skill** — RAN 2026-07-10
      (Fable, cold session): **PASS-WITH-FINDINGS**, verdict below the divider
      in `docs/reviews/2026-07-10-create-repo-rewire.md`. Floor green (142→145
      tests, 3 selftests, leakscan/licenscan clean); mechanism driven live
      twice. 10 findings C1–C10, **all [fixed] + re-driven same session**. The
      two sharpest, both proven live: C1 a fresh clone loses hook + config
      silently — machine two committed a planted `AKIA…` key green (fixed at
      the three places a new clone looks: CLAUDE.md bullet, CONTRIBUTING
      once-per-clone install, hook header); C2 the stamped drift check breaks
      run-verbatim — unquoted spacey path, and the skill's `$PP/atelier`
      contradicted the `../atelier` house practice (skill now stamps
      sibling-relative + block quotes the path + a mechanical prove-the-stamp
      in step 5). `tools/test_templates.py` pins template-block ≡ PROPAGATION
      canonical (C3). **Both owed items now closed 2026-07-10 (Opus):** the
      outward `gh repo create --push` step driven live for the first time —
      scaffolded **`numen`** (`mike548141/numen`, PRIVATE, verified
      `isPrivate: true`), the first keeper repo, born from this mechanism at
      `atelier@bbdeece`; hook proven live to block a planted `AKIA…` key +
      pass the real commit clean, drift check clean run-verbatim, no
      `settings.local.json` leaked. And ros (f72031c→bbdeece) + faves
      (dde4170→bbdeece, +the P1 trust-surface floor clause it lagged) pin bumps
      carried the reworded block down — fleet now all-current (`tools/pins.py`).
  - [ ] **C5 backlog strand**: `tools/scaffold.py` (mechanise the
        seed/rename/stamp core; skill becomes its wrapper) — only if a stamp
        defect recurs despite step 5's new mechanical prove-the-stamp.
- [x] Until the verdict: create-repo may be used for throwaway/scratch
      exercising, but **don't scaffold a real keeper repo on the unreviewed
      mechanism** (the don't-stack-on-unreviewed rule, applied to delivery
      instead of doctrine). *Cleared 2026-07-10 by the sweep above — keeper
      repos may be scaffolded.*
- [x] **Repo-boundary guidance** — DONE 2026-07-10 (Opus): `docs/build/
      REPO-BOUNDARY.md`, the is-this-a-repo decision by independent-lifecycle
      discriminators (visibility/cadence/ownership/reuse/blast-radius) → standalone
      / component / monorepo-folder (rich client engagement as the monorepo case);
      advise proactively; when ambiguous prefer the reversible direction (split
      later is cheap, merge is painful). Reviewed 2026-07-10 (batch review —
      discriminators decide the three live cases; B16 split-promptly clause).
- [x] **Parallel-work tooling** (Mike 2026-07-10: make fork-and-merge a *tool*,
      not just doctrine) — built as `tools/worktree.py`
      (`start`/`list`/`land`/`remove`), the one-command delivery of CONCURRENCY's
      worktree-per-line: fork outside iCloud, hygiene view, push+PR back, guarded
      cleanup. Guards encode the doctrine — iCloud-base refusal, branch-off-main,
      stale/dirty flags, no-lose-work on remove. 12 stdlib tests + live-proven on
      atelier itself (start → list → remove round-trip, main tree left untouched).
      Built the same session Mike was handed the worktree recipe to run the
      method/ Fable review as a parallel line.

## Safety tooling (gates the person-context + archive threads)

- [x] **Mechanical leak-scan** — built 2026-07-10 as `tools/leakscan.py`
      (+ README, `pre-commit.sample`, `leakscan-terms.example.txt`, unittest).
      Shareable structural patterns (always run) + machine-local literal-term
      list (`~/.claude/leakscan-terms.txt`, never in a repo); graceful
      degradation to structural-only with a loud warning; `--staged` hot path,
      `--json`, fail-safe exit codes; `.leakscanignore` + `leakscan:allow`
      escape hatches; `--disable <rules>` + `--staged <subtree>` for networking
      repos / private-repo-with-shareable-subtree. Proven: caught real address/
      coordinate/name leaks in its own first-draft fixtures; **local term list
      SEEDED** in `~/.claude/`; **hooks INSTALLED** (atelier whole-repo; ros
      `tiki/`-scoped with network-shape rules off) and block/pass proven live.
      Full-cover scan validated the earlier tiki scrub — 1 residue (the intended
      OSS author name in `pyproject.toml`, allow-marked) out of 738 raw hits.
      **Owed:** CI wiring (a hook only guards the machine it's on); portability
      of the term list to Mike's other devices (north-star); extend patterns as
      gaps appear. Reviewed 2026-07-10 (batch review — B4 renamed-file staged
      hole fixed + proven live, B5 `--require-terms` fail-closed flag for
      hooks/CI, B7 residual false-negative surface now stated in tools/README).
- [x] **Secret-scan on push** — built 2026-07-10 as `tools/secretscan.py` (a
      zero-dep, self-written "equiv", not a gitleaks install — matches the house
      tool pattern + dodges the tool-install floor). Named vendor formats + a
      secret-named-assignment/entropy workhorse; skips the safe indirections
      (`!secret`/`${VAR}`/`<ph>`), code refs, public keys and URL paths.
      **Validated 0 FP over real tiki source/inventory/docs** (25→0 across three
      FP-class fixes) while still catching the fixture-secret shapes; report
      redacts to length+entropy. 47 tests; combined pre-commit sample runs it
      with leakscan; `.secretscanignore` + allow-marker escape hatches.
      Reviewed 2026-07-10 (batch review — pattern set + heuristic hold, skip-list
      verified against SECRETS.md's named forms; B4 renamed-file staged hole
      fixed + proven live, B6/B7 residuals stated). **Owed:** CI wiring (dead until atelier has a remote);
      hook portability to Mike's other repos. Closes the *detect* half of
      *detect → rotate → burn-cost-is-minutes*.
- [x] **`DATA-PROTECTION.md`** written (2026-07-10) — read-before-write; verified
      way-back before any destructive op; data plane is the slow lane even under
      broad grants; reproducibility as insurance; protect others' data.
- [x] **Safe-access-onboarding doctrine** — DONE 2026-07-10 (Opus):
      `method/ACCESS.md`, the ordered onboarding runbook (grant-recorded-not-
      originated → narrowest credential + plane-split → credential-into-store-first
      → read-only first ring + reconcile-or-stop → destructive gate encoded before
      destructive power → widen-in-rings → Zero-Trust the domain). Invents no rule;
      sequences AUTONOMY/DATA-PROTECTION/SECRETS/PRINCIPLES for the moment access is
      new. The concrete estate access map is instance-local (sensitive topology,
      protected under DATA-PROTECTION; ros owes its first consolidated map —
      B14 backlog). method/README #6. Reviewed 2026-07-10 (batch review — B13
      step-5 strengthening owned + one-credential fallback stated, B14 access-map
      claim corrected to honest status).
- [x] **`SECRETS.md`** doctrine — DONE 2026-07-10 (Opus): `method/SECRETS.md`,
      extracted from ros §5 (credential triad) + §7 (secret-store-not-exempt).
      Reproducible / re-mintable enabling property (internal rotate mechanically,
      external re-mint behind one approval); the least/JIT/short-lived triad with
      standing creds as tracked-debt-not-resting-state; references-never-values in
      the right plane; rotation-on-cadence bounds the undetected window. Closes
      AUTONOMY's forward-reference to "the secrets doctrine" and completes the
      *detect → rotate → burn-cost-is-minutes* arc with the two scans. Instance
      mechanism (sops+age, `!secret`, the credential map) stays in ros — ros
      cross-read confirmed it holds that content. Reviewed 2026-07-10 (batch
      review — B12 honest boundary added: master-key loss is redundancy-guarded,
      person-level vault out of scope by design).

## North star — context follows the person, work follows anywhere

- [ ] **Two-tier person-context portability.** Both excluded from atelier, both
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

## Session archive (decide)

- [ ] Archive sessions as **encrypted cold storage** — NAS, local-only (never
      iCloud-broad, never a repo), ~12-month rolling retention, **no search
      index initially** (searchability = exfil surface); NZ Privacy Act retention
      applies (third-party PII in transcripts). Start with Claude Code
      `~/.claude/projects/**/*.jsonl`; "every session incl. chat/cowork" needs
      export machinery that doesn't exist yet — say so.

## Sharing — public since 2026-07-10 (ADR 0005)

The private-first sequence (peer-adoption → restructure → *then* public) was
consciously collapsed: the peer-of-two never became a peer-of-three, so **public
is the friction mechanism**, not a reward withheld until after it. atelier is
public as a **named worked example** (README "If you're adopting this"). What was
"before public release" is now **post-public hardening**:

- [x] **Public release (readable repo)** — DONE 2026-07-10 (ADR 0005), as a named
      worked example: no genericise-the-voice pass, no instance-restructure
      precondition; the audit showed the hard boundary already held. The flip
      was `gh repo edit --visibility public`, act-then-record.
- [ ] **One real peer adoption** (CEL, then a client-org) — still the highest-value
      hardening; now happens *with* strangers able to read it too. Treat their
      confusion as the harvest.
- [ ] **Practice/instance restructure** of AUTONOMY + STORAGE — the person-local
      specifics (grant ledger, Apple/iCloud) → marked worked-examples. No longer
      a publication gate; do it as the named-worked-example framing gets tested by
      a real adopter.
- [ ] **The next widening** — a public announcement, or packaging as a **Claude
      Code plugin/skills bundle** (plugin = behaviour travels — higher leverage).
      This is now the live floor item (Mike's call, not the agent's). Reuse the
      ros `PUBLISHING.md` extract-scrub-fresh-export pattern; **scrub list must
      include client names**.
- [x] **atelier's own CI** — DONE 2026-07-10 (Opus): `.github/workflows/ci.yml`
      (job `floor`) dogfoods the floor every review asserted by hand — the tool
      test suite, three scanner `--selftest`s, and the scan triad over the whole
      tree. Zero-dep stdlib means a public runner needs only Python. Honest
      scope baked into the header: secretscan/licenscan at full cover; **leakscan
      structural-only, deliberately no `--require-terms`** (its term list is
      machine-local by design — CI can't hold it and must not). Least-privilege
      (`contents: read`), concurrency-cancel. **Live-proven twice on GitHub** (7s,
      11/11 steps, no deprecation annotation after the `checkout@v5`/
      `setup-python@v6` bump) — not assumed; watched green.
- [ ] **Wire the public scanners into child CI** — the other half, still open: a
      child's CI checks out `mike548141/atelier` and runs its public `tools/` (no
      secret, no vendored copy, no drift). atelier's own `ci.yml` is the reference
      to adapt (swap the in-repo tool steps for an atelier checkout).
- [x] **Markdown internal-link check** — BUILT 2026-07-10 (Opus), **REVIEWED
      2026-07-10 (Fable, cold session): PASS-WITH-FINDINGS, gate cleared** —
      verdict below the divider in `docs/reviews/2026-07-10-linkscan.md`.
      `tools/linkscan.py`, the mechanical check that atelier's "thin anchor, fat
      pointer" graph actually resolves. The review proved damage to **all five**
      of the brief's load-bearing assumptions and fixed it same session (suite
      171→187): L1 a typo'd path arg scanned nothing and exited 0 (the §14
      silent-success class — now exit 2); L2 case-mismatched links green on APFS
      but 404 on GitHub (now walked against on-disk casing, NFC/NFD-safe); L3
      links escaping the repo root (new `outside-root` kind — GitHub serves
      nothing above root); L4+L5 anchor matching now exact like GitHub's, after
      fixing the slugger's underscore-stripping divergence; L6 parenthesised
      filenames parse; L7 fence tracking length/info-string-aware (nested ````
      examples stay code); L9 setext headings now mint anchors. L8 root-relative
      `/…` semantics verified against GitHub docs; L10 indented-code FP stated
      as residual by design.
  - [x] **Wire linkscan into `ci.yml` + `pre-commit.sample`** — DONE 2026-07-10
        (Opus), the session after the verdict (don't-stack honoured). CI: a
        `--selftest` line + a whole-tree `linkscan --root . .` step, mirroring
        the triad. Hook: linkscan added as a **whole-tree integrity** check —
        *not* `--staged` like the two boundary scanners, because a link breaks
        when a *different* file is renamed/deleted (the stale file is usually
        not the one in your diff). `run_scan` generalised to drop the hardcoded
        `--staged` so each scanner declares its own mode; header documents the
        distinct contract; block-message + README updated. Contract pinned by
        three new `test_precommit.py` tests incl. the whole-tree crux (a rename
        breaking an *unstaged* link blocks — a staged-only scan would miss it);
        suite 187→190. Installed atelier hook refreshed so this very commit
        dogfoods it. **Residual, stated:** a scaffolded child inherits the
        stricter whole-tree contract (its whole doc tree must stay link-clean to
        commit, vs the diff-scoped boundary scanners) — cheap for a clean tree,
        `linkscan:allow`/`.linkscanignore`/`--no-verify` are the hatches.

## Open questions

- Does ros keep canonical copies of any doctrine, or hold only bearings + point
  up for everything (as §0 now does)? Default: point up; resolve per doc at
  extraction.
- `docker-heap` is unstandardised (stub README, no CLAUDE.md) — run the
  standardise-existing pass when convenient.
