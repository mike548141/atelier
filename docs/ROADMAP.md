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

- [x] **Fable review of the `method/` layer** — run 2026-07-10 (Fable 5,
      usage-billed); verdict below the divider in
      `docs/reviews/2026-07-10-method-layer.md`. **PASS-WITH-FINDINGS**: 14
      findings, 11 [fixed] in-session (headline R1: "more capable model"
      reframed to **independent capable review** — independence, not
      superiority, is the mechanism; plus two floor cases restored to the
      child doctrine block), 3 [backlog] → follow-ups item below.
- [ ] **Method-review follow-ups (2026-07-10):** (a) fleet-level drift view —
      per child, pin vs atelier HEAD (P4); (b) re-stamp ros + faves doctrine
      blocks at each repo's next pin bump to pick up the P1/P2 floor
      restorations; (c) SESSIONS.md index/detail split at the next natural
      point (V2); (d) trim guardrail folded into the ros PRINCIPLES trim item
      below (PR2).

## Then — extraction (keep the case-law, don't strip it)

Generalise the *bearings/cases*, don't delete them (a de-cased principle is
theatre). Leave tiki-specific bearings + review case-law in ros.

- [x] **`PRINCIPLES.md`** spine + precedence ladder + situation tests, with
      generalised cases. Extracted 2026-07-10; canonical here.
- [ ] **Trim ros `docs/PRINCIPLES.md`** to pointer + tiki bearings + review
      case-law only — its general §1–7 prose now duplicates atelier's canonical
      spine (a transitional DRY breach, flagged loudly at the top of that file,
      not silent). Deserves its own careful session in ros so the case-law isn't
      damaged in the trim. **Guardrail (method-review PR2):** before deleting
      ros prose, confirm every atelier case/situation test stands alone as a
      complete teachable statement — post-trim, ros's named precedents are
      invisible to peer adopters.
- [ ] **`MODEL-ECONOMICS.md`** general shape (numbers stay person-local). (Stub
      has review-trigger + tiered authority already.)
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
- [ ] Honest-instrument (A7) + source-acquisition ladder (A6) into method/.

## build/ layer + inheritance delivery

- [ ] Extract the `create-repo` standard into `docs/build/` (product-in-subfolder,
      standardise-existing process, honest-CI, lockstep-change, ADR rule, TODO/
      comment conventions — harvest A10).
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
- [ ] **Secret-scan on push** (gitleaks or equiv) — the *detection* half of the
      secrets mitigation: an exposed secret is only a cheap rotate-now event if
      you *know* it was exposed.
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
