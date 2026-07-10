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
      extraction section. Review-owed (doctrine text — a REVIEW.md sampling pass).

## build/ layer + inheritance delivery

- [x] **Extract the `create-repo` standard into `docs/build/`** — DONE
      2026-07-10 (Opus): `docs/build/REPO-STANDARD.md` (product-in-subfolder + why,
      sizing-to-type, the standard file set, honest-CI, standardise-existing
      process, repo-craft conventions), pointing up to `method/` for the
      cross-cutting doctrine (EVIDENCE/RECORD/REVIEW/PROPAGATION/AUTONOMY) instead
      of copying it. build/README rewritten from pointer → layer index. Review-owed
      (doctrine text — a REVIEW.md sampling pass). Instance specifics stay in the
      skill. Templates-move + rewire-to-inherit remain (below).
- [ ] **Supply-chain/release standard** (A5) — committed deterministic SBOM +
      keyless signing; **licence-consistency pre-publish gate** (A11).
- [ ] **Rewire `create-repo` to inherit from atelier** — stamp the doctrine
      block + pin; the skill is the *delivery vehicle*, atelier is the *source*.
      No delivery path bypasses create-repo. (The core Q1 fix.)
- [ ] **Repo-boundary guidance** — Claude *directs* standalone-repo vs component
      vs monorepo-folder (e.g. a rich client engagement). Standing behaviour:
      advise proactively.
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
      gaps appear. Review-owed (mechanical control, so a validator/CI run is most
      of the enforcement — but the pattern set + the shareable/local split
      deserve an approach review).
- [x] **Secret-scan on push** — built 2026-07-10 as `tools/secretscan.py` (a
      zero-dep, self-written "equiv", not a gitleaks install — matches the house
      tool pattern + dodges the tool-install floor). Named vendor formats + a
      secret-named-assignment/entropy workhorse; skips the safe indirections
      (`!secret`/`${VAR}`/`<ph>`), code refs, public keys and URL paths.
      **Validated 0 FP over real tiki source/inventory/docs** (25→0 across three
      FP-class fixes) while still catching the fixture-secret shapes; report
      redacts to length+entropy. 47 tests; combined pre-commit sample runs it
      with leakscan; `.secretscanignore` + allow-marker escape hatches.
      Review-owed (mechanical control — a validator run is most of the
      enforcement, but the pattern set + the assigned/entropy heuristic deserve
      an approach review). **Owed:** CI wiring (dead until atelier has a remote);
      hook portability to Mike's other repos. Closes the *detect* half of
      *detect → rotate → burn-cost-is-minutes*.
- [x] **`DATA-PROTECTION.md`** written (2026-07-10) — read-before-write; verified
      way-back before any destructive op; data plane is the slow lane even under
      broad grants; reproducibility as insurance; protect others' data.
- [ ] **Safe-access-onboarding doctrine** — the checklist for onboarding a new
      access domain (network, cloud tenancy, NAS, workspace): least-privilege /
      scoped-per-capability, **read-first**, widen-in-rings, credential in the
      secret store not inline, and — for any domain holding data — a
      **snapshot/restore-before-destructive gate** encoded, not remembered.
      (Shareable doctrine; the concrete estate access map is instance-local, not
      in this repo.)
- [ ] **`SECRETS.md`** doctrine (extract ros §5) — reproducible / re-mintable
      secrets so rotation is low-work/low-risk (internal: rotate at will;
      external: re-mint behind one approval); least/JIT/short-lived as the goal;
      a rotation cadence that bounds any undetected-exposure window. Pairs with
      the two scans above: *detect → rotate immediately → the burn cost is
      minutes.* (Mike, 2026-07-10: a burned secret must be easily replaceable.)

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

## Sharing (private-first)

- [ ] **One real peer adoption** (CEL, then a client-org) hardens the doctrine
      before any public work — shareability is untested (audience-of-two so far);
      treat their confusion as the harvest.
- [ ] Full **practice/instance restructure** of AUTONOMY + STORAGE before public
      release (grant ledger, Apple/iCloud specifics → marked worked-examples or
      person-local).
- [ ] Public release + packaging: readable repo vs **Claude Code plugin/skills
      bundle** (plugin = behaviour travels — higher leverage). Reuse the ros
      `PUBLISHING.md` extract-scrub-fresh-export pattern. **Scrub list must
      include client names** (e.g. any client-org named in docs).

## Open questions

- Does ros keep canonical copies of any doctrine, or hold only bearings + point
  up for everything (as §0 now does)? Default: point up; resolve per doc at
  extraction.
- `docker-heap` is unstandardised (stub README, no CLAUDE.md) — run the
  standardise-existing pass when convenient.
