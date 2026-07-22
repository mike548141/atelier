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
no-MAJOR application pass, closed 2026-07-22) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

- [x] **SECRETS.md access-management expansion + ACCESS.md step-2 line** —
  rule-4 cold pass on `caa85fe` run 2026-07-22 by the wave-1 queue run
  (provenance in the brief; the run authored none of the delta):
  **PASS-WITH-FINDINGS 0 MAJOR · 4 MINOR · 4 LOW · 1 nit**, citations
  verified live, live-proven claims re-run clean, reconcile overturned
  nothing — terminal per the close rule, cycle closed. Verdict:
  [`reviews/2026-07-22-1021-secrets-access-cold-pass.md`](reviews/2026-07-22-1021-secrets-access-cold-pass.md).
- [ ] 🎯 **SA1–SA8 rulings (secrets/access cold pass)** — self-authored
  doctrine, so the findings are Mike's to decide (rule 3); nothing applied.
  Sharpest four: SA1 the asymmetric-key grading misses the agent-forwarding
  channel (a compromised target can reach the fleet a shared key opens);
  SA2 the watch leg's third surface is unachievable on the doctrine's own
  exemplar store (sops+age has no read trail); SA3 minting conflates max
  entropy with max length (silently-truncating verifiers); SA4 no
  break-glass / store-unreachable class. Per-finding what/why/impact in the
  verdict.

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
            held — Mike's call + Mike's action (the rotations).
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

- [x] **Name the pattern in `method/`** — built 2026-07-22 by a fresh
      session per Mike's ratification ("build as counselled"), wave-2 queue
      run, `343def8`: CONCURRENCY.md § Orchestrated queue runs (96 lines —
      run mechanics, role check at open, default selection order, per-item
      close as the cap-safety property, four named stop conditions + the
      🎯-surfacing report, rule-4 synergy) + ECONOMICS.md § The
      orchestrated-run tier split (22 lines). Section-vs-new-file settled by
      the builder on actual size, as ratified. Every ratified element landed,
      incl. the deliberately-out items named at the point a reader would
      look. Grounded on both bearings (man-page rollout + the live
      2026-07-22-1018 run).
- [x] **Mechanise it as a skill** — built same delta, `8111e9f`:
      `skills/queue-run/SKILL.md`, plugin-bundled by auto-discovery exactly
      as review-brief travels (no manifest change needed — verified);
      stamped-copy header points up, narrowing-free.
- ⏳ **Orchestrated-queue-run doctrine + skill — rule-4 cold review owed.**
  Delta: `343def8` (CONCURRENCY § Orchestrated queue runs + ECONOMICS § the
  orchestrated-run tier split) + `8111e9f` (`skills/queue-run` +
  README/session-onramp wiring). Intent record:
  [`sessions/2026-07-22-1018-orchestrated-queue-run.md`](sessions/2026-07-22-1018-orchestrated-queue-run.md).
  Doctrine by function → full rule-4 cycle; the 2026-07-22-1018 run authored
  the delta, so that run (and its workers) cannot take this.

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

- [x] **Map the public canon against `method/` + the scanner floor** — done
      2026-07-22 (wave-1 queue run): mapping record
      [`sessions/2026-07-22-1025-security-canon-gap-map.md`](sessions/2026-07-22-1025-security-canon-gap-map.md),
      every "already held" claim verified by reading the cited doc. Verdicts
      on the capture's candidates: **A** threat modelling CONFIRMED (narrow —
      reviewer-side held, the *builder* is never told to enumerate threats);
      **B** secure defaults CONFIRMED (narrow — fragments, not generalised);
      **C** supply chain CONFIRMED reframed (zero-dep *is* the control; the
      live residual is third-party CI actions pinned by mutable tag, not
      SHA); **D** secure-coding floor DISMISSED (instance-layer by design;
      one framing line owed); **E** vuln lifecycle CONFIRMED (partial —
      credential path fully held; missing severity/recurrence framing and a
      public-repo SECURITY.md disclosure posture). The mapping also
      corrected this section's "already held" list (below).
- [ ] **Doctrine edits for confirmed gaps A/B/C/E** — seams and rough sizes
      proposed in the mapping record §3 (proposals, not decisions).
      Suggested first slice: SHA-pin the CI actions + a SECURITY.md — both
      live public-repo exposure. Self-authored doctrine: each edit lands
      with its rule-4 `⏳`.
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
- [x] **Promotion rule — recurrence makes an invariant** — the mining half
      done 2026-07-22 (wave-2 queue run, `84fb112`): 330 findings across all
      47 review files clustered into 5 scanner candidates (S1 wrap-hygiene —
      the class that shipped three cycles running; S2 named-path-resolves;
      S3 UTC dating; S4 template stamp-drift; S5 NZ spelling, carried on ROI)
      + 7 verifier/checklist candidates (V1 overclaim-vs-evidence is the
      largest cluster at ~30 — validating the doctrine, not exposing a gap),
      below-threshold classes named, already-enforced classes credited, and
      one ⚠️: fail-open/detector-edge (~23) kept recurring *after* the
      selftest floor — "harden tools/ tests", not "solved". Record:
      [`sessions/2026-07-22-1036-invariant-candidates.md`](sessions/2026-07-22-1036-invariant-candidates.md).
- [ ] 🎯 **Rule on the invariant candidates S1–S5 / V1–V7** — per-candidate
      approval is Mike's (the PROPOSED-then-ratify pattern); each carries its
      cited occurrences + proposed seam/home in the record. Approved scanner
      candidates become build items; approved verifier candidates feed the
      REVIEW.md/skill checklist when the registry mechanism lands. Original
      capture text (the promotion rule): any review finding
      left **more than twice** should become an invariant. Mine historical
      review records, cluster them, generate invariant CANDIDATES for **human
      approval** (matches our PROPOSED-then-ratify pattern — the glossary does
      this). "Each invariant you codify is a check that will never cost a
      reviewer time again." atelier already has the review corpus to mine
      (session records + `reviews/` briefs + verdicts).
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

- [x] **Restore from archive — full + delta** — built 2026-07-22 (wave-1
      queue run, `9ca1425`): `--restore` (full) + `--restore --delta`
      (audit's mutated/pruned/renamed buckets), `--dry-run`/`--force`/`--json`
      reused. Content-first safety: `grown` never a target (byte-prefix
      check, so even a full restore can't drop a live tail); diverged+newer
      live refuses unless `--force` (loud); zip-slip containment; additive
      only (renamed restores the OLD path, never deletes the live rename —
      documented choice). Suite 46→63 ccarchive / 109 instruments green,
      re-proven post-merge; live fixture run exercised every exit path.
      Man page + README updated per the CLI-docs standard.
- [x] **iCloud dataless-file awareness** — built 2026-07-22 (wave-3 queue
      run, `12794d6`): `SF_DATALESS` read via BSD `stat -f %f` (Node exposes
      no `st_flags` — investigated incl. bigint stats), classifier **verified
      against a real evicted file** in the live archive, `stat` proven
      non-faulting. `--verify`/`--audit` skip evicted files into a distinct
      `evicted`/undetermined bucket (never a failure, never mis-read as
      missing/corrupt; success line says "every *checked* transcript");
      opt-in `--materialise` reads them deliberately; `--restore` still
      faults content back by design (documented); manifest/backfill writes
      proven non-faulting. Honest residual: the end-to-end skip on a *live*
      eviction is seam-simulated, not exercised — nothing was evicted to
      test. Suite 109→116 (118 instruments-wide post-merge). The `--json`
      audit contract gains the `evicted` array — consistent-awareness call
      endorsed at merge.
- [x] **Sign the manifest (tamper-evidence)** — built 2026-07-22 (wave-4
      queue run, `2a85839`): detached HMAC-SHA256 sidecar
      (`manifest.json.sig`), key off-archive at `~/.claude` (file over
      Keychain — cron/launchd reads it promptless; the key guards
      tamper-evidence, not confidentiality), `--rekey` rotation re-signs the
      current manifest (SECRETS replaceability — a roll loses nothing),
      five verify states each honest and non-zero (tampered / key-mismatch /
      unsigned-legacy-migrates / no-key-unverifiable; verify never mints).
      The closed caveat proven live: forged `.gz` + recomputed manifest hash
      → signature MISMATCH, exit 1. Non-protections stated in the man page
      (key theft forges; no anti-rollback; evidence, not prevention). Suite
      70→84 ccarchive / 132 instruments-wide, re-proven post-merge.
      🎯 Two contestable defaults, Mike's to overturn if wanted: binary 0/1
      exit codes (unverifiable vs proven-tamper distinguished in text/JSON
      only), and no-key verify exiting red on a legitimate new machine until
      the key arrives out-of-band (deliberate never-silently-pass).
- [x] **Is there any metadata that ccarchive misses?** — answered 2026-07-22
      (wave-3 queue run, `5ce9f00`): yes. The real hole is
      `tool-results/` sidecars — offloaded tool-output payloads the
      transcript only points at, so the archive can hold dangling references
      while advertising a complete record (≈7% of transcript volume;
      recommendation: CAPTURE, plus man-page honesty about what is excluded
      regardless). Full classification (capture / exclude-and-document /
      needs-Mike) in
      [`sessions/2026-07-22-1050-cc-instruments-questions.md`](sessions/2026-07-22-1050-cc-instruments-questions.md).
- [ ] 🎯 **Rule on the metadata classes** — needs-Mike calls: per-project
      `memory/*.md` (durable cross-session state, most personal) and
      top-level `history.jsonl` (typed-prompt stream, lean-exclude
      counselled); plus approve/decline the CAPTURE of tool-result sidecars
      (a build item once ruled).
- [x] **Should cctranscript and ccarchive be one?** — analysed 2026-07-22
      (wave-3 queue run, same record): **keep separate** counselled. Measured
      shared code is ~10 lines; merging would couple ccarchive's
      schema-immunity (the property guarding the sole durable copy) to
      cctranscript's schema-fragile parser, and blur ADR 0006's observe vs
      preserve verbs. Counter-case captured (natural pipeline pair → argues
      for a `--source <archive>` flag on the reader, not a merge); middle
      path (shared lib) only if shared code crosses ~40–50 lines. 🎯 Mike's
      call whether to accept the recommendation; no work owed until then.

### ccrepo (Mike, 2026-07-17)

- [x] **Tighten the ccusage reconciliation drift** — done 2026-07-22 (wave-2
      queue run, `75bba4c`). Root cause found and fixed: the
      `(message.id, requestId)` dedup kept the **last** log line, and the logs
      re-emit messages with a trailing partial/zeroed usage line — last-wins
      silently dropped tokens. Now keeps the **richest** record (max-total),
      which matches ccusage **exactly** on a frozen matched-session set;
      sonnet-5 (the ~1.5% outlier) → 0.00%, total drift → ~0.00% with only
      in-flight current-session variance left, reported plainly.
      `server_tool_use` measured live: present on many messages but every
      counter zero — per-call pricing not built, the v1 "named contributor"
      hypothesis retracted in the design doc as measured-false. Per-model
      reconcile also scoped to matched sessions (one-sided window-edge
      sessions no longer smear into phantom per-model deltas). Suite 92→94
      green (111 instruments-wide, re-proven post-merge).
- [ ] **Actual spend (plan or usage) vs the API-usage estimate** — the money-side
      analog of the ccusage cross-check. ccrepo's cost is an API-list-price
      *estimate*; the billing model (`ccrepo-billing.json`) already apportions a
      flat plan fee into an Actual column, but Mike wants to compare **what he
      genuinely pays** — a subscription tier (e.g. Max 5x/20x) or metered usage —
      against what ccrepo computes from API usage, and see the delta. Needs a
      machine-local source of real spend (plan tier + period, or an exported
      usage/invoice figure) and a reconciliation footnote like the ccusage one but
      for dollars actually billed. Personal data ⇒ the spend source stays in
      `~/.claude`, never a repo (same boundary as `ccrepo-billing.json`).

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
      next pin bump / harvest. **The rebalance dissolves the all-open-roadmap
      red**: a wholly-open ROADMAP (ros's ~125 open items) no longer reds on
      length — with no cold content to relocate it is advisory now, not a standing
      red — so the class-grounded-budget workaround is no longer needed for that
      case. A child that still reds does so on un-harvested `[x]` items, its own
      harvest lane. faves and ros run bespoke CI without `sizescan --check` — a
      separate floor-adoption step.

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

- [ ] **One real peer adoption** (CEL, then a client-org) — still the highest-value
      hardening; now happens *with* strangers able to read it too. Treat their
      confusion as the harvest.
- [ ] **Practice/instance restructure** of AUTONOMY + STORAGE — the person-local
      specifics (grant ledger, Apple/iCloud) → marked worked-examples. No longer
      a publication gate; do it as the named-worked-example framing gets tested by
      a real adopter.
- [ ] **v2 plugin — CHOSEN 2026-07-13 (Mike's call): the next widening is
      spent here.** De-instance `create-repo` so it travels in the plugin, and
      ship `worktree` + `fleet-pins` as plugin commands — doctrine travelling
      as behaviour, wider than the current bundle. Needs a scoping pass first
      (what "de-instanced" means for a skill that stamps house identity), then
      the build; go-live via PR like the v1 bundle, reviewed before merge.

Completed sharing work (public release, the plugin bundle widening, atelier's own
CI, child-CI scanner floor, linkscan build + wiring) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

## Open questions

- [ ] 🎯 **Extend the checkbox grammar to five states?** (Mike, 2026-07-22,
  mid-build) — proposal: add `[-]` declined and `[^]` superseded beside the
  tri-state. **Builder's counsel: keep the tri-state** — the bracket answers
  the one machine-checked question (is work owed?); declined/superseded both
  answer "no" and need a dated note for the *why* regardless, so extra
  states are a second copy of one fact (the point-of-use drift class).
  Promote to distinct states only if we find ourselves repeatedly grepping
  dispositions apart (the anti-slop promotion rule). Mike's call; Mike
  himself flagged the complication risk.

- Does ros keep canonical copies of any doctrine, or hold only bearings + point
  up for everything (as §0 now does)? Default: point up; resolve per doc at
  extraction.
- **Floor template's duplicate trigger (raised 2026-07-13, for a future
  session).** `build/templates/workflows/floor.yml` fires on `push:` (all
  branches) **plus** `pull_request`, so any branch with an open PR scans
  **twice** — free on public atelier, but *metered minutes* in every private
  child that copies it. Genuinely two-sided, which is why it wasn't auto-fixed:
  the `push` run scans the branch tip (what a public push *publishes*), the
  `pull_request` run scans the *merge preview* a tip-push can't see and covers
  fork PRs (no `push` event in the base repo) — so they aren't pure duplicates.
  The N4 review deliberately chose every-push for the public publish-safety
  rationale; trimming the overlap (e.g. dropping `pull_request` where a repo
  takes no fork PRs, or scoping `push`) touches that decision, so it's the
  estate's call per repo, not the agent's. Decide whether the merge-preview +
  fork-PR coverage earns the second metered run on private children, or the
  template should scope down. See ECONOMICS "duplicate triggers".

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
- [x] **`MODEL-ECONOMICS.md` renamed to `ECONOMICS.md`** — Mike's 2026-07-22
      decision executed 2026-07-22 (wave-1 queue run, `b639513`): `git mv` on
      the canonical file and the child-template copy, 24 pointer refs across
      16 live files; history append-only (113 old-name refs in records stand).
      Deliberation record:
      [`sessions/2026-07-22-0435-economics-rename-decision.md`](sessions/2026-07-22-0435-economics-rename-decision.md).
      Light review discharged mechanically per the item's own note: linkscan
      clean before/after, 323 tool tests green incl. the template block-sync
      test, orchestrator diff-verified at merge. Nothing dangles cross-repo —
      children resolve refs against their pins; each child updates its
      atelier-pointing refs (stamped block's session-rhythm pointer, floor.yml
      comments) **at its next pin bump**, and a child's own private
      `MODEL-ECONOMICS.md` counterpart keeps its name by that child's call
      (ros recorded exactly this, 2026-07-22).

Resolved questions (docker-heap standardisation, estate credential governance) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
