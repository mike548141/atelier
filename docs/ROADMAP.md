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

## Doctrine — review-owed

- 🎯 **The combined cold pass RAN 2026-07-19 (design-review section +
      commitment re-key + sizescan doctrine deltas): PASS-WITH-FINDINGS,
      3 MAJOR · 3 MEDIUM · 3 LOW — Mike's rulings owed on F1–F9.** Verdict +
      per-finding taker's counsel:
      `reviews/2026-07-19-0407-review-trigger-sizescan-combined-cold.md`.
      The doctrine content held; what failed is the verification record.
      Sharpest: F1 the stamped `<atelier-path>` pointer is never filled in a
      create-repo child and the prove-the-stamp grep misses it — 🚩 **keep the
      fleet re-stamp gated until fixed**; F2 the "old link broken in every
      stamped child" claim is false on re-run; F3 `skills/review-brief` still
      carries the old artefact-grammar trigger (the sweep never covered
      `skills/`). F8 rules the queued PRINCIPLES.md header question: genuine
      defect, re-key lines 1+3 with the application. 3 MAJOR ⇒ cycle open; on
      the rulings a non-author applies, and the applied batch queues its own
      ⏳ pass.
- [ ] **The 07-18 review-line remedy has no artefact.** `REVIEW.md` requires
      every durable design record to carry a `review:` line ("omission is the
      bug"), but no ADR template, `decisions/README.md`, or ROADMAP template
      carries the field — the templates manufacture the blank the rule calls a
      bug. Deliberately left out of `4c17f59` to keep that delta reviewable as
      one thing. Doctrine-by-function ⇒ earns its own review when taken.
      The 07-19 cold pass adds (F6): qualify REVIEW.md's "enforcement is
      structural" until this lands, and a cheap design-record lint belongs
      alongside it (the 0820 record's deferred question, answered yes).
- [ ] **REACH/AUTONOMY backlog — the cold pass's H1–H8 + residuals** (all
      backlog-grade; doctrine-substantive ones are the principal's when
      picked up). Sharpest three: H2 "existing cookies are fair game" reads
      as licensing cookie *export* (rung-5 reach with rung-3 isolation) —
      scope to in-place use through the ridden session; H3 the categorical
      browser-store exclusion now argues *against* the doc's own two criteria
      post-A1 (a provisioned bot-login profile passes both) — ground it or
      scope the test; H1 operator/principal conflation unstated (and the
      instance README drifts on it). Also: H4 the resource-owner's "no" never
      named as its own judgement; H5 "blocked" undefined for soft blocks; H6
      rung-1/2 equivalence overclaimed beyond the instance (challenges
      decided A4/A5 wording — principal's); H7 "never a standing grant" vs
      "temporary or permanent" seam; H8 instance-README alignment pass
      (stale pre-A4 absolute, boundary pointer should name REACH.md);
      residuals — AUTONOMY's "direct handling" doesn't literally catch
      machinery-mediated *repurposing*; two over-length lines to rewrap.
Completed review cycles (Claiming-work, REACH ×3, the independence batch,
COMMUNICATION, RECORD keep-generic, signing doctrine, PRINCIPLES §8, the plugin
bundle, CONCURRENCY put-away, CLI-docs standard, ADR 0006/ccarchive addendum,
CONVENTIONS + UTC-at-rest, lean-files/sizescan) →
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

- [x] **Local-store audit (`--audit`) — DONE 2026-07-17**; live store hashed
      against the manifest, only mutated+renamed count as drift. Detail →
      [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
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

### man pages — convention rollout

- [ ] **cctranscript + ccrepo: man page + concise `--help`** — the split (full
      plain-language `man`, concise `--help` pointing to it) is established with
      `ccarchive` as the worked example (`instruments/man/`, published by
      `instruments/install`). Roll it out to the other CLIs. **ccrepo v2 has now
      landed** (2026-07-17), so its help is stable — this is unblocked.

## File-size hygiene (new 2026-07-14)

The generalised anti-bloat work. `sizescan` flags any current-truth file over
budget across the fleet; these are the outstanding harvests it surfaced.

- [x] **Budgets are tripwires, not targets — Mike's ruling 2026-07-19, APPLIED.**
      `--check` now gates only the lossless-remedy files (`ROADMAP.md`,
      `SESSIONS.md` — a red demands a *move*, never rewording); judgement docs
      (`README`/`ARCHITECTURE`/`CLAUDE`) report but never fail the build. The
      one-sided signal (no thinness floor — that's stub-honestly judgement, not
      a number) stated as deliberate in the module doc. `sizescan.py` + report
      + `floor.yml` template comment; suite 267 green, both classes live-proven
      (atelier gated red exits 1; a judgement-doc red exits 0). Children adopt
      at pin bump. **Agent-authored doctrine ⇒ in the ⏳ review scope above.**
- [x] **hooks.atelierTools worktree bug was fleet-wide** — 9 more children
      carried the relative path (every worktree commit blocked by the
      fail-closed hook); all 10 set absolute 2026-07-19, and the **source
      fixed** — `create-repo` step 6 now absolutises the path it stamps.
Completed file-size work (the 2026-07-14 sizescan build/review + wiring; the
2026-07-18 fleet harvests — ros 7123→982 in two ruled stages, faves, shed;
the grounded-budgets correction) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).
- [ ] **Existing fleet children pick up the `floor.yml` size gate** — children
      copy `floor.yml` statically, so they adopt at their next pin bump /
      harvest. The fleet is sizescan-clean except ros's ROADMAP (structural —
      125 open items; its red is true and stays lit until ros declares a
      class-grounded budget or the item count falls). faves and ros run bespoke
      CI without `sizescan --check` — a separate floor-adoption step.

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
