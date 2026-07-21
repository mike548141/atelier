# atelier ROADMAP

Lean by design: **what's open**, prioritised, read every session. Completed
detail lives in [`ROADMAP-DONE.md`](ROADMAP-DONE.md) — the current-truth/history
split (`method/RECORD.md`); `tools/sizescan.py` is the signal that keeps this
file honest. Sequencing rule from the 2026-07-10 review: **mechanism before more
content** — a repo that inherits docs but not the propagation + review cadence
has inherited the costume, not the doctrine.

Checkbox states: `[ ]` open · `[x]` done · `[~]` **claimed** by a live parallel
session — `(claimed <date>-<HHMM>, wt: <branch>)` — don't start a `[~]` item;
take the next open one (`method/CONCURRENCY.md` § Claiming work) ·
`⏳` **review queued** for a non-author to take — any spawner passing rule 4's
criterion may take it; the taker writes the brief (`method/REVIEW.md` rule 4).
**The pointer is refs only** — name the delta and the intent record, no
evaluative account; the account lives in the session record, so a taker meets
the work cold (REVIEW.md rule 4's ceiling, stated here at the point of use).

## Doctrine — review-owed

- ⏳ **Review-line artefact delta** — delta `fa7a90f` (ADR/decisions/ROADMAP
      templates + `tools/reviewscan.py` + wiring + `REVIEW.md` enforcement
      re-statement); intent record
      `docs/decisions/2026-07-21-0744-review-line-artefact.md`.
      **CLAIMED 2026-07-21 0913 UTC** by a rule-4 taker (Fable, Mike-spawned:
      "Please do any review work"; authored none of the delta). Brief →
      `docs/reviews/2026-07-21-0913-review-line-artefact-cold.md`
      (wt: review-line-artefact-cold-pass).
Completed review cycles (Claiming-work, REACH ×3, the independence batch,
COMMUNICATION, RECORD keep-generic, signing doctrine, PRINCIPLES §8, the plugin
bundle, CONCURRENCY put-away, CLI-docs standard, ADR 0006/ccarchive addendum,
CONVENTIONS + UTC-at-rest, lean-files/sizescan, the review-trigger/sizescan
combined cycle — 0407 → F1–F9 applied → 0544 → G1–G3 applied → 0629 terminal
no-MAJOR pass, closed 2026-07-19; the 2026-07-20 triple cycle — DOCUMENTATION
doctrine + CONCURRENCY posture flip + session-onramp operating-rhythm, three
rule-4 cold passes all PASS no-MAJOR, applied `87af9f9`) →
[`ROADMAP-DONE.md`](ROADMAP-DONE.md).

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

## instruments/ — open features

### ccarchive (Mike, 2026-07-17)

- [ ] **Restore from archive — full + delta** — replace mutated/missing local
      files from the archive (gunzip `<dest>/<rel>.gz` → `~/.claude/projects/<rel>`).
      A full `--restore` and a delta mode that restores only what the local-store
      audit flags (now built — `--audit`'s `mutated`/`renamed`/`pruned` buckets
      are the delta source). Must not clobber a live file *newer* than the
      archived copy (an in-flight session); confirm/refuse rather than overwrite
      silently. Note the `grown` bucket is *not* a restore target — the live file
      is ahead of the archive there, the opposite direction.
- [ ] **iCloud dataless-file awareness** — iCloud "Optimise Mac Storage" evicts
      the local bytes of unused files, leaving a dataless placeholder (contents
      still in the cloud). ccarchive must keep working: reading an evicted `.gz`
      faults it back on access (fine), but a whole-archive `--verify` would
      re-download *everything* — costly and it defeats the point of eviction.
      Detect dataless files (macOS `SF_DATALESS` st_flags / the ubiquity
      "downloaded" key) and (a) never mis-report an evicted-but-intact file as
      missing/corrupt, (b) don't gratuitously materialise them (skip by default;
      opt-in `--verify --materialise`), (c) ensure writing the manifest/new `.gz`
      never triggers a bulk re-download.
- [ ] **Sign the manifest (tamper-evidence)** — closes the `--verify` caveat: a
      tamperer who rewrites a `.gz` *and* the manifest currently passes. Sign
      `manifest.json` (detached signature / HMAC with a key kept **off the
      archive** — `~/.claude` or the macOS Keychain) so `--verify` detects a
      forged manifest, raising the anchor from "accidental corruption" to
      "tamper-evident". Key location/rotation is the real design question.

### ccrepo (Mike, 2026-07-17)

- [ ] **Tighten the ccusage reconciliation drift** — v2 lands at ~0.05% (a few
      dollars on ~$6.9k), reported every run. Tighten it further: chase the
      residual per-model (sonnet-5 is the largest at ~1.5%), decide whether
      `server_tool_use` per-call pricing (web search/fetch — deferred v1) is a
      real contributor worth pricing, and confirm the token-count edge cases where
      ccrepo's `(message.id, requestId)` last-wins dedup still differs from
      ccusage. Goal: shrink the drift and, where it can't go to zero, *name the
      cause* in the footnote rather than leave it a bare number.
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
  template should scope down. See MODEL-ECONOMICS "duplicate triggers".

Resolved questions (docker-heap standardisation, estate credential governance) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
