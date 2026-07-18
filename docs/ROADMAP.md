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

- ⏳ **`method/REVIEW.md` — new section "Review the design, not only the build
      — the earliest review is the cheapest"** (+ the structural review-line
      convention). Delta: `method/REVIEW.md`, section inserted before *When to
      review — inline or batched*. Intent record:
      `decisions/2026-07-18-0820-review-the-design-not-only-the-build.md`.
      Principal's ruling 2026-07-18. Self-authored doctrine (author: Opus,
      `ros` session 2026-07-18) ⇒ rule 4: **the taker writes the brief**; the
      author has queued this pointer and written none. Sibling application
      already committed in `ros` at `55d0d51` (`CLAUDE.md` + ROADMAP review
      policy) — in scope for the same pass if the taker wants it.
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
- [x] **Lean-files doctrine + `sizescan` — reviewed 2026-07-14, all findings
      resolved, cycle closed.** Cold un-briefed pass **PASS-WITH-FINDINGS**
      (1 MAJOR · 2 MEDIUM · 1 LOW); verdict in
      `reviews/2026-07-14-2048-lean-files-sizescan-cold.md`. F1 (fail-open
      ancestor-dir) + F2 (body marker self-exempt) + F4 (dup paths) fixed +
      pinned + F1 live-reproven; **F3 decided by Mike — SESSIONS index rotation**
      (RECORD.md sharpened: append-only *content*, relocatable home →
      `SESSIONS-ARCHIVE.md`). `sizescan` now wired `--check` into the gate (see
      *File-size hygiene* below).

Completed review cycles (Claiming-work, REACH ×3, the independence batch,
COMMUNICATION, RECORD keep-generic, signing doctrine, PRINCIPLES §8, the plugin
bundle, CONCURRENCY put-away, CLI-docs standard, ADR 0006/ccarchive addendum,
CONVENTIONS + UTC-at-rest) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

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
            **Correction 2026-07-19 — "wouldn't newly-red them" was wrong, and
            the greens proved nothing** (under `--warn` no floor has ever
            *failed* on signing; on scanner-red children the signing steps never
            run at all). A blocking-mode probe over all 12 children at their own
            pins/boundaries: **10 pass, 2 fail — both currently green**, neither
            among the scanner-red three. Seven commits dated 2026-07-12
            (activation day) are unsigned, from two causes, **neither a second
            machine**: (a) an adoption boundary set one commit too early; (b)
            five replayed by a **GitHub web-UI "Rebase and merge"** — re-committed
            server-side, signatures stripped, committer set to the merging
            account (pre-merge originals survive as dangling objects, correctly
            signed). (b) is a **recurring hazard**: squash/merge-commit are
            web-flow-signed (signscan defers those to the gh plane), rebase-merge
            is not. Flip now also needs the two boundaries fixed + a rebase-merge
            decision. Child identities stay in their private records, per above.
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

- [x] **Local-store audit vs the archive manifest — DONE 2026-07-17.**
      `ccarchive --audit` hashes every live `.jsonl` and buckets it against the
      manifest: **synced** · **grown** (archived bytes a strict prefix — a plain
      append, kept out of the drift signal so an active session isn't a false
      alarm) · **mutated** (rewritten/truncated) · **renamed** (content matched
      an archived path now gone from live) · **new** · **pruned**. Only mutated +
      renamed are drift (listed, non-zero exit); the rest are counted. Read-only
      over both trees (no write path ⇒ no git-worktree guard). Pure core
      (`auditCategorize` + `classifyDivergence`) unit-tested; +11 tests (35→46
      ccarchive, 86 instrument), man AUDIT section (mandoc clean), README +
      `--help`. Driven live: 435 archived · 432 synced · 3 grown · 19 new · 0
      drift → exit 0.
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

- [x] **atelier: sizescan + RECORD doctrine + this ROADMAP harvest** — DONE
      2026-07-14 (1091→lean; completed detail → `ROADMAP-DONE.md`). Dogfood of
      the doctrine here first.
- [ ] **ros: harvest `docs/ROADMAP.md`** — `sizescan` flags it now at **4933
      lines** (grown from the 3197 recorded when this item was filed; ~75%
      completed detail accreted onto finished items). Its own focused ros
      session: collapse done items to one-line pointers, move the case-law to
      ros's `ROADMAP-DONE.md` (which already exists at 1285 lines). Delicate —
      the narration is real case-law; relocate verbatim, never delete. Also
      `ros/CLAUDE.md` sits +34 over budget (mild). **⚠️ Check ros-session
      liveness first**: a wholesale reorg of this file collides hard with a live
      ros session (they claim roadmap items = edit the same file). Attempted
      2026-07-17-2235 and released on discovering an active ros session
      (`radius-home` worktree) mid-claim — take it only when ros is quiet.
- [x] **faves: SESSIONS/ROADMAP/ARCHITECTURE harvest — DONE 2026-07-18,
      `sizescan` clean.** `SESSIONS.md` 1157→234 (rotation → new
      `SESSIONS-ARCHIVE.md`), `ROADMAP.md` 766→299 (resolved → new
      `ROADMAP-DONE.md`, verbatim), `ARCHITECTURE.md` 276→250. `dba7658..ab6a12d`.
- [x] **`sizescan` reviewed + wired into the gate** — DONE 2026-07-14. Cold pass
      cleared (PASS-WITH-FINDINGS); F1 (fail-open ancestor-dir MAJOR) fixed +
      live-reproven, F2 (prose-mention self-exempt) fixed (markers header-only),
      F4 dedup fixed; **F3 decided by Mike — index rotation** (`SESSIONS.md`
      tail + `SESSIONS-ARCHIVE.md` growth store; RECORD.md sharpened). Now runs
      `--check` in atelier's `ci.yml` and the child `floor.yml` template (a repo
      that adopts the floor while over-budget reds → the signal to harvest;
      `sizescan:budget=N`/`allow` hatches). Suite 240→247; pinned in
      `test_sizescan.py` + `test_templates.py`.
- [ ] **Existing fleet children pick up the `floor.yml` size gate** — the
      template now carries `sizescan --check`, but children copy `floor.yml`
      statically, so they adopt at their next pin bump / harvest. ros (above)
      will red until harvested — that red is the intended trigger. faves is now
      harvested (2026-07-18), so adopting the gate there is safe (faves' CI
      doesn't yet run `sizescan --check` — a separate floor-adoption step).

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
