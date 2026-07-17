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

- ⏳ (claimed 2026-07-17-1000, wt: worktree-fable-review) **REPO-STANDARD: CLI tools ship both `--help` and a man page — cold review
      queued 2026-07-17.** New repo-craft convention in `build/REPO-STANDARD.md`
      (§ Repo-craft conventions): the two-register split — `--help` a one-screen
      digest that points at the manual, `man <tool>(1)` the plain-language full
      reference (FILES/EXAMPLES/NOTES) — plus how to wire it (`man/` dir, installer
      publishes to `MANPATH`). Children inherit it. Worked example landed in the
      same delta: `instruments/man/ccarchive.1` + a trimmed `ccarchive --help` +
      `instruments/install` man-wiring. **Self-authored doctrine ⇒ author must not
      warm-spawn the review** (rule 4); a non-author takes this ⏳. Intent record:
      `sessions/2026-07-17-0946-ccarchive-man-cli-docs-standard.md`. Brief seeds —
      is the digest/reference boundary drawn sharply enough to prevent drift; does
      the convention over-reach for repos with trivial one-flag tools (should it be
      sized to tool complexity like the rest of the standard).
- ⏳ (claimed 2026-07-17-1000, wt: worktree-fable-review) **ADR 0006 addendum (ccarchive — the *preserving* verb) — cold review
      queued 2026-07-17.** New instrument `ccarchive` and its ADR 0006 addendum:
      the `instruments/` layer gains a fourth verb (**preserve**) and its first
      *writing* instrument, admitted by the existing purpose rule with two guards
      (no personal data in code; write target a personal store outside any repo).
      Delta: the `instruments: add ccarchive` commit on branch `ccarchive` (the
      code + README are tested/driven and self-verifying; only the ADR addendum's
      doctrine gates). **Self-authored doctrine ⇒ its author must not warm-spawn
      the review** (rule 4); a non-author session takes this ⏳ and writes the
      brief. Intent record:
      `sessions/2026-07-17-0810-ccarchive-transcript-preservation.md`. Brief
      seeds — is "preserve" a real fourth verb or does it fold into observe; is
      the writing-instrument boundary (personal dest, runtime-derived) drawn
      tightly enough for a public repo; does the §8 reconciliation (ccarchive
      subsumes ccrepo's retention-ledger survival rationale) hold.
- ⏳ (claimed 2026-07-17-1000, wt: worktree-fable-review) **CONVENTIONS.md + UTC-at-rest ADR — cold review queued 2026-07-15.**
      New `method/CONVENTIONS.md` (the default-frame rule: declare once + label
      deviation/collision; foreign-data precedence) and ADR `2026-07-15-1327`
      (timestamps UTC at rest, identifiers UTC-forward, ELT-not-ETL). Delta:
      `67e8582` (doctrine) + `198cf32` (fidelity fixes — CLAUDE.md→CONVENTIONS
      pointer, clause-3 second ELT reason — from a full-feedback audit against
      Mike's prompts). **Self-authored doctrine ⇒ its author must not warm-spawn
      the review** (rule 4); a non-author session takes this ⏳ and writes the
      brief. Intent record: `sessions/2026-07-15-1327-conventions-default-frame.md`.
      Brief seeds — does the label rule's ~99%/exception split stay honest or
      invite over-labelling; is the foreign-data precedence grounded or padded;
      do the declared defaults leak anything person-local into a public repo;
      does "UTC-forward identifiers" cohere with RECORD's coordination-free rule.
Closed doctrine review cycles (REVIEW rule 4, MODEL-ECONOMICS triple delta,
"informed principal" apex rule, PRINCIPLES §2 four bullets — all CYCLE CLOSED
2026-07-14/15) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md) § Doctrine — completed
review cycles.

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
bundle, CONCURRENCY put-away) → [`ROADMAP-DONE.md`](ROADMAP-DONE.md).

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
            on *signing* (so the flip wouldn't newly-red them, but the fleet
            isn't clean enough to declare enforce-mode honestly): two fail
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

- [ ] **Local-store audit vs the archive manifest** — check the *live* store
      (`~/.claude/projects`) against the archive's `manifest.json` to spot
      **renamed, missing, or mutated** transcripts (the live file drifted from
      what was archived). Distinct from `--verify`, which checks the *archive*
      against its own manifest; this checks the *live store* against the archive.
      Read-only; reports drift.
- [ ] **Restore from archive — full + delta** — replace mutated/missing local
      files from the archive (gunzip `<dest>/<rel>.gz` → `~/.claude/projects/<rel>`).
      A full `--restore` and a delta mode that restores only what the local-store
      audit flags. Must not clobber a live file *newer* than the archived copy
      (an in-flight session); confirm/refuse rather than overwrite silently.
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

### man pages — convention rollout

- [ ] **cctranscript + ccrepo: man page + concise `--help`** — the split (full
      plain-language `man`, concise `--help` pointing to it) is established with
      `ccarchive` as the worked example (`instruments/man/`, published by
      `instruments/install`). Roll it out to the other CLIs. **ccrepo waits for
      the v2 rewrite to land** — don't churn its help mid-redesign.

## File-size hygiene (new 2026-07-14)

The generalised anti-bloat work. `sizescan` flags any current-truth file over
budget across the fleet; these are the outstanding harvests it surfaced.

- [x] **atelier: sizescan + RECORD doctrine + this ROADMAP harvest** — DONE
      2026-07-14 (1091→lean; completed detail → `ROADMAP-DONE.md`). Dogfood of
      the doctrine here first.
- [ ] **ros: harvest `docs/ROADMAP.md`** — `sizescan` flags it at **3197 lines**
      (~75% completed detail accreted onto finished items). Its own focused ros
      session: collapse done items to one-line pointers, move the case-law to
      ros's `ROADMAP-DONE.md` (which already exists at 1285 lines). Delicate —
      the narration is real case-law; relocate verbatim, never delete. Also
      `ros/CLAUDE.md` sits +34 over budget (mild).
- [ ] **faves: adopt the SESSIONS index/detail split** — `docs/SESSIONS.md` is
      **1157 lines**, a flat log that never adopted the index model (its own
      header already says "tail-read, don't load whole" — the split is the next
      step). Harvest `docs/ROADMAP.md` (766) too; `ARCHITECTURE.md` is +26 (mild).
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
      statically, so they adopt at their next pin bump / harvest. ros + faves
      (below) will red until harvested — that red is the intended trigger.

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
