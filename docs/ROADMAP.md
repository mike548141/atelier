# atelier ROADMAP

Lean; read every session. Completed detail moves to `ROADMAP-DONE.md` once this
grows. Sequencing rule from the 2026-07-10 review: **mechanism before more
content** — a repo that inherits docs but not the propagation + review cadence
has inherited the costume, not the doctrine.

Checkbox states: `[ ]` open · `[x]` done · `[~]` **claimed** by a live parallel
session — `(claimed <date>-<HHMM>, wt: <branch>)` — don't start a `[~]` item;
take the next open one (`method/CONCURRENCY.md` § Claiming work).

## Doctrine — review-owed

- [ ] **Applied-batch cold pass — CONCURRENCY "Claiming work" fixes (owed).**
      The first pass carried a MAJOR, so REVIEW.md's cycle rule owes a fresh
      un-briefed pass over the applied edits: confirm all seven landed faithfully
      and no new MAJOR arose. Cold, un-briefed; findings Mike's to decide.
- [x] **Cold review of CONCURRENCY "Claiming work"** — RAN 2026-07-13, un-briefed
      (reviewer chose its own attack surface): **PASS-WITH-FINDINGS**, verdict +
      decision in `reviews/2026-07-13-concurrency-claiming-work.md`. Core
      mechanism live-verified sound; **1 MAJOR · 4 MEDIUM · 2 LOW**. Mike ruled
      **all seven [fixed]**, applied same day. The MAJOR was real: the section
      gated claiming to worktree-mode, whose only reliable trigger is the
      principal's say-so — exactly the condition the grounding incident broke —
      so it wouldn't have fired in the case it was built for. Fix (option A,
      decouple): claiming now keys on **selection from the shared queue**, claim
      commit lands on `main` before branching. MEDIUMs: bundled lines serialise
      (fan-out needs per-leaf lines); adjacent one-line claims raise a trivial
      keep-both conflict (live-verified, "silent everywhere else" was false);
      put-away gained the `[~]`→`[ ]` reversion; tracker-based adopters pointed
      at the assignee primitive. LOW: timestamp demoted to a tiebreak.
      **Applied-batch cold pass owed** (above).
- [x] **Cold pass on the applied REACH batch — RAN 2026-07-13, same day:
      PASS-WITH-FINDINGS, no MAJOR — cycle CLOSED** per the stopping rule.
      Verdict verbatim in `reviews/2026-07-13-reach-batch-applied.md`.
      Fidelity 8/8 confirmed (two immaterial deviations, labelled, no drift
      label owed); the instance proof re-run 11/11. Eight findings H1–H8
      (four MEDIUM, four LOW) + two reconciliation residuals — none unseats
      an applied decision — consolidated onto the backlog item below, no
      further ceremony per the rule.
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
- [x] **REVIEW.md reviewer-independence rule — decided 2026-07-13, all
      fixed.** Two cold reviews ran: 2026-07-12 (scoped to the three independence
      edits, I1–I7, 3 MAJOR — `reviews/2026-07-12-review-independence.md`) and
      2026-07-13 (principal-commissioned, un-briefed, whole-doc, F1–F7 —
      `reviews/2026-07-13-review-doctrine-second-pass.md`). Mike ruled
      both batches **[fixed]**, choosing floor-not-fence on the seeded-questions
      fork and adding his own strengthening (questions influence by their very
      existence — the reviewer guards against their topic/tone steering its
      surface). Applied 2026-07-13 to REVIEW.md + PROPAGATION.md by a session
      that authored neither the doctrine nor either verdict; decisions
      stamped in both verdict files.
- [x] **Cold review of the applied independence batch — RAN 2026-07-13,
      decided same day: all nine [fixed], applied, cycle CLOSED.** Mike
      ruled the loop question directly: the cycle closes when a pass returns no
      MAJOR (this one did), and if MAJORs ever stop falling pass-to-pass, stop
      and ask him — both now encoded in REVIEW.md's application paragraph,
      alongside his endorsement of G1's structural fix (seeded questions defer
      below the brief's divider). This application spawns no further ceremony
      per the rule it encodes. **PASS-WITH-FINDINGS**, verdict verbatim in
      `reviews/2026-07-13-independence-batch-applied.md`. Fidelity confirmed:
      14/14 decisions faithfully applied (one deviation judged the right
      call — F2's pre-fork wording harmonised with the floor-not-fence
      decision). Nine findings G1–G9, five MEDIUM, none blocking: G1 the rule-1
      ordering instruction is behavioural where the house demands structural —
      exposure to seeded questions primes at read time, so defer them below the
      brief's divider (or name the ordering as mitigation-not-cure); G2 rule 3
      is wrongly conditioned on brief authorship (its true trigger is
      self-authored doctrine, however commissioned) and step 4 already says so;
      G3 the standing test's "passes clean" trigger keys on finding count — the
      metric F1 just evicted — and would not have fired on the REACH case
      itself; G4 the doctrine-review regress needs a stopping rule and the
      neutral-applier pattern deserves encoding; G5 application reviews can't
      honour rule 2 (the delta carries the decision stamps) — needs
      sequencing guidance. G6–G9 small wording/staleness. Applier's counsel,
      labelled (the applier authored the reviewed edits, so decides nothing):
      take all nine — G2/G6–G9 are mechanical; G1 suggests the deferred-
      questions brief shape (structural, matches rule 2); G3's re-key and G4's
      no-MAJOR stopping rule read sound; G5 pairs with G4's paragraph.
- [x] **REACH.md adversarial re-review — DECIDED 2026-07-13: all eight
      [fixed], applied same day** to `REACH.md` (A1–A8) + `AUTONOMY.md` (A1's
      matching secrets-floor carve-out, so the two docs state one rule) by a
      session that authored neither the doctrine nor the verdict; decisions
      stamped in the verdict file. **Cold pass on the applied batch owed**
      (REVIEW.md's cycle rule — tracked below). Original item follows:
      ~~DECISION OWED, Mike's, not the
      author's.** RAN 2026-07-12 (session 47's post-session self-review found
      the first review author-briefed — cold context, warm questions — so an
      un-briefed adversarial pass was commissioned; it chose its own attack
      questions and was barred from the prior review until its own verdict was
      drafted): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-12-reach-rereview.md`. Eight findings A1–A8, **none
      overlapping the first review's five**; two MAJOR, both on the credential
      boundary reading more permissively than decided practice (A1 "no further
      permission needed" vs AUTONOMY's always-confirm secrets floor; A2
      ride-a-session unscoped beyond fetch-only). The reviewer's judgement of
      the first review: tier right, basis unsound — every pre-seeded question
      pointed where the author was already looking. Findings await **Mike's**
      decision; the doc's author applies nothing here on its own.~~
- [x] **Cold review of `method/REACH.md`** — RAN 2026-07-12 (cold
      fresh-context agent): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-12-reach.md`. All four sharp questions cleared green — the
      ladder is a faithful abstraction with no invented rungs (generic 1–6 maps
      1:1 onto the Chrome-only instance, the partial-instance gap disclosed
      verbatim from this item); the two-halves join is *argued* on a real
      mechanism (same event at rungs 4–5), not asserted; the purpose-of-storage
      test covers the estate's cases without outlawing the one use the ladder
      exists for (riding the live session); no person-level leak (password
      manager named as a class, the ROADMAP's `Apple Passwords` instance
      correctly kept out). **5 findings R1–R5, all [fixed] same day** — none
      blocking, one theme (adopter-clarity + one genuine seam): R1 "the estate
      registry"/"keychain" definite references an outside adopter can't resolve →
      indefinite "a provisioning registry's entries"; R2 operator/principal
      identity the join leans on now *stated* where the halves meet; R3 the seam
      between the purpose test and the categorical browser rule closed (a
      browser's saved-credential store is never itself the provisioned path —
      ride, don't mint, whichever profile); R4 the rung-4/5 one-mechanism caveat
      pulled up beside the ladder; R5 the grant exception signalled at first
      statement ("without an explicit grant").
- [x] **Cold review of `method/COMMUNICATION.md`** — RAN 2026-07-12 (cold
      fresh-context agent, barred from the person-level layer by the brief so
      the leak question was judged as a genuine outside reader):
      **PASS-WITH-FINDINGS**, verdict in `reviews/2026-07-12-communication.md`.
      The sharpest question cleared: the scrubbed worked example does NOT leak
      the personal layer by implication — the join it creates is identity ×
      category-existence with zero specifics, and the categories named in the
      scrub note are the ones the repo's boundary statement already publishes.
      Axes grounded (unevenly evidenced, honestly so); decline-then-revisit
      read as append-only honesty, not relitigation. 4 findings C1–C4, all
      [fixed] same day — one theme: the doc held the boundary rigorously but
      was looser on itself (enforcement unstated → write-time-discipline-only
      now named; the not-even-private rule's divergence from the portability
      north star surfaced, kept strict with the reconciling why; the worked
      example dated as a snapshot per EVIDENCE §7/§9; the "works without the
      reader knowing it" overclaim sharpened to *functions* without it).
- [x] **Cold review of RECORD "keep private repos generic"** — RAN 2026-07-12
      (cold fresh-context agent): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-12-record-private-repos-generic.md`. The central clause
      held; the naming clause was mis-drawn — the harmful class is the **join**
      (a private repo's name × its sensitive posture), not the name, and the
      rule as written outlawed the repo's own records while the actual join
      survived the original scrub in four places. 7 findings R1–R7, all
      [fixed] same day: section redrafted (the join is the regulated class;
      name-only mentions sanctioned behind a load-bearing-name test, e.g.
      ros/faves/numen; enforcement stated honestly — write-time discipline +
      review sweeps, no mechanical floor exists; scrub-of-HEAD-is-not-
      remediation now opens the section), and the surviving joins scrubbed at
      HEAD (the fleet-adoption three-repo join; the infra-child coarse joins
      in SESSIONS/detail/ROADMAP — resolved the strict way, so doctrine and
      record agree). Residual, stated: pre-scrub prose stays reachable in
      public history; the write-time rule is the only control that exists.
- [x] **Cold review of the signing doctrine (SIGNING.md + ADR 0007)** — RAN
      2026-07-12 (cold fresh-context agent; every mechanical claim live-driven
      in a scratch repo, GitHub claims grounded in current docs):
      **PASS-WITH-FINDINGS**, verdict in `reviews/2026-07-12-signing-doctrine.md`.
      The core design proved out live — config block verbatim-correct, and the
      crown-jewel claim (bounded retirement keeps old signatures verifiable)
      is true: git passes the committer timestamp as verify-time. 10 findings
      G1–G10, all addressed same day; pre-activation, so every fix was a text
      edit — exactly what review-before-activation was for. The three
      blocking: verification made **two-plane** (GitHub's own merge commits —
      two already on `main` — are GPG-signed by the web-flow key and would
      have red-flagged the repo on first activation; the `gh api` verification
      check closes it spoof-safe), the badge-persistence claim was **inverted**
      vs current GitHub behaviour (removing a key does NOT un-verify history —
      corrected in SIGNING.md + ADR 0007 addendum), and quoted
      `valid-after="…"` timestamps mandated (the man page's unquoted form
      fails to parse on the estate's own ssh-keygen). Plus: trust list
      resolved at the child's pin, never floating `main` (a floated trust
      root defeats the blast-radius argument); custody, boundary-stub, and
      backdating honesty. Decision unchanged; activation still gates on Mike
      registering a key.
- [x] **Cold review of PRINCIPLES §8 ("Leverage")** — RAN 2026-07-11 (Fable,
      cold session): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-11-principles-8-leverage.md`. Placement verified against
      the pre-change text (appended-not-renumbered correct; §8 rightly off the
      precedence ladder); all ties hold; the gold-plate discipline genuinely
      bounds it. 3 findings, all [fixed] same day: intro's "§1–7" swept to
      "§1–8" (§6's own stale-claim class), §7's "Numbered last" opener made
      position-independent, and the optional observed-vs-predicted recurrence
      evidence bar taken. Gate cleared.
- [x] **Cold review of the plugin bundle (PR #3)** — RAN 2026-07-11 (Fable,
      cold session, isolated worktree): **PASS-WITH-FINDINGS, nothing blocks
      the merge** — verdict in `reviews/2026-07-11-plugin-bundle.md`. Proven
      live: install end-to-end (root-as-plugin delivers tools/+docs/ at the
      consumer end), `/atelier:scan` honest in a foreign repo, install-hook
      blocks/passes/fails-closed as documented, and merge-is-go-live proven
      directly (marketplace add from GitHub fails today — no manifest on
      main). 5 findings: 1–3 **[fixed] on the branch** (`030f185`, PR #3
      updated — update-invalidates-hooks warning, skills' plugin-root refs
      made location-relative, all three companions named); 4–5 notes, no
      action. User config verified clean after (install fully undone). **The
      merge (go-live) is Mike's call, now review-cleared.**
      **MERGED 2026-07-11 (Opus, session 38) — Mike authorised go-live.** PR #3
      merged to `main` (`a0ef731`) after resolving a CHANGELOG append-conflict
      with the intervening ccrepo work and re-running the floor green on the
      merged head (`6245986`: 34 Node + 205 Python + 4 scanners); CI green on
      the head SHA before merge. `main` now carries `.claude-plugin/plugin.json`
      + `marketplace.json`, so `/plugin marketplace add mike548141/atelier` →
      `/plugin install atelier@atelier` resolves — the doctrine now travels as
      behaviour. Branch deleted local+remote. **This is the first deliberate
      widening spent from the live-floor item below.**
- [x] **Cold review of CONCURRENCY "Every branch ends put away"** — RAN
      2026-07-11 (Fable, cold session): **PASS-WITH-FINDINGS**, verdict in
      `reviews/2026-07-11-concurrency-put-away.md`. Fork exhaustive for lines
      of work; no RECORD/REVIEW conflict (tag keeps history reachable;
      decision-in-session-log is RECORD's own discipline). 3 findings, all
      [fixed] same day: the bearing's "multiple sessions" count grounded
      explicitly (PR #1 close + session 34 — and sharpened: the branch was
      kept *deliberately* and still generated the re-derivation tax), a
      scoping clause added (integration/permanent branches are infrastructure,
      not open work), and the tag convention date-prefixed per RECORD. Gate
      cleared.
- [x] **create-repo: new repos born with delete-branch-on-merge** — DONE
      2026-07-11: the skill's create-remote step now follows `gh repo create`
      with `gh repo edit --delete-branch-on-merge` (stated as standard, not
      option), and REPO-STANDARD's new-repo process gained step 6 saying the
      same — the landed half of CONCURRENCY's put-away rule automatic at birth.

## Raised 2026-07-12 (logged, not yet scoped)

- [x] **Apply the REACH re-review findings A1–A8 on Mike's decision** — DONE
      2026-07-13: Mike ruled **all eight [fixed]** (the counsel had said A1–A5
      + judgement on the rest; he took the lot). Applied to `REACH.md` and
      `AUTONOMY.md` by a neutral hand (authored neither doctrine nor verdict);
      decisions stamped in `reviews/2026-07-12-reach-rereview.md`. The cold
      pass on the applied batch is the review-owed item at the top.
- [x] **Session-38 borderline join — SCRUBBED 2026-07-13, Mike's decision.**
      The name × debt join (a named child × "scan surfaced findings,
      owner-tracked, decided fix") was reworded out of all three public spots
      that carried it — the session-38 detail file, its SESSIONS.md index
      line, and the ROADMAP's standardisation bullet — keeping the
      transferable lesson (read the repo's own roadmap before externalising a
      scan report), each spot noting the scrub and that the old wording stays
      reachable in git history (a scrub of HEAD is not remediation).
- [x] **REVIEW.md — encode reviewer independence** — DONE 2026-07-12. The gap
      the REACH case proved: a *cold-context* review can still be
      *warm-questioned* — the REACH author wrote its brief's pre-seeded
      questions, all aimed where the author was already looking; the un-briefed
      re-run found eight findings, zero overlap, two MAJOR. Encoded as a new
      REVIEW.md section *Independence is more than fresh context* (three rules:
      reviewer chooses its own attack surface, barred from prior reviews until
      its verdict drafts, self-authored *doctrine* findings decided by the
      principal not the author) + two lifecycle carve-outs (step 1 author-brief
      exception, step 4 doctrine-decision carve-out). **Cold review owed**
      (tracked under *Doctrine — review-owed* at the top).

- Reply/reporting style — **reframed out of atelier scope 2026-07-12.** Mike
  clarified the purpose is *for the agent to understand him*, not rules the agent
  recites — so it's personal context (a specific person's communication
  preferences), which the no-personal-data boundary keeps in `~/.claude/`, not
  public atelier. Written into `~/.claude/CLAUDE.md`'s "Working with me" section
  (visual reader → iconography/tables; outcome-first-then-evidence; watch volume,
  let structure replace length). No atelier artifact — the clean call was *not*
  to build `method/REPORTING.md`.
  - **Revisited same day, by Mike — `method/COMMUNICATION.md` built
    (2026-07-12, session 43).** Not a reversal of the boundary: the *values*
    stay personal (`~/.claude/`), but Mike ruled the *pattern* shareable —
    peers adopting atelier work better with the agent if they keep their own
    calibration, and the doc is how they learn to. Same split as TOOLBOX
    (practice shareable / instance personal); Mike's calibration included
    scrubbed as the named worked example (ADR 0005 framing). The doc records
    this decline-then-revisit history honestly. **Review-owed** (below).
- [x] **Adopt browser-fetch as a teammate capability** — DONE 2026-07-12 (Opus,
      session 41). The first **capability** instrument: a Chrome-driving MCP
      server (fresh headless, or the operator's own Chrome over CDP for
      captcha/Cloudflare) for when `WebFetch`/curl are blocked. ADR 0006 got an
      addendum — `instruments/` widens to admit tools that **extend the
      teammate's reach**, not only observe; the zero-dep ethos flexes for a
      capability tool whose value needs deps (pinned `requirements`/`constraints`,
      a regenerable venv OUTSIDE the repo/iCloud, code versioned in-repo).
      `instruments/browser-fetch/` holds the **scrubbed** `server.py` (every
      "Mike" → operator, pre-SDK/machine history removed before this public repo),
      pinned deps, a reproducible `setup`, and a README. Proven end-to-end after
      setup (`browser_fetch` returned a rendered page; both tools register); MCP
      registration repointed to the atelier location. Not CI-unit-tested (a
      browser is disproportionate in CI); floor scanners cover `server.py`, live
      use verifies. **Confirmed + cleaned up 2026-07-12:** a fresh parallel
      session ran `browser_fetch` end-to-end against the re-registered server
      (example.com → 200; httpbin User-Agent showed `HeadlessChrome/149` — real
      Chrome), so the old `~/.claude/mcp-servers/browser-fetch` was deleted.
- [x] **Fetch escalation ladder — build the missing rungs + elevate to doctrine**
      — DONE 2026-07-12 (session 47): doctrine elevated (`method/REACH.md`,
      reviewed) and both build sub-items shipped (multi-engine rung 3,
      live-verified; explicit rung-4/5 port split). The full ladder is documented
      in `instruments/browser-fetch/README.md` (rungs 1 WebFetch/WebSearch ·
      2 curl · 3 `browser_fetch` standalone headless, now Chrome/Firefox/WebKit ·
      4 persistent dedicated profile `:9222` · 5 persistent everyday session
      `:9223` · 6 ask the operator). The **only residual is operator-gated**: a
      live rung-5 fetch needs the operator's everyday Chrome on `:9223`.
      Sub-items, for the record:
      - [x] **Other engines** — DONE 2026-07-12 (session 47). `browser_fetch`
            (rung 3) gains an `engine` param: `chromium` (default, real installed
            Chrome), `firefox` (Gecko), `webkit` (Safari's engine) — a second
            engine is a second way past anti-bot that keys on Chrome/headless
            specifically. Firefox + WebKit **live-verified** (each fetched
            example.com end-to-end through the server path). **Honest limit:**
            rungs 4/5 stay **Chrome-only by protocol** — CDP is Chrome's, and
            Playwright's `connect_over_cdp` speaks only CDP; Firefox/WebKit have
            no connect-to-running equivalent. Not a fillable stub — a real limit,
            documented in code + README.
      - [x] **Cleaner 4/5 split** — DONE 2026-07-12 (session 47). Made explicit
            two ways at once: `browser_fetch_persistent` gains a `rung` param
            (`4` dedicated / `5` everyday), each mapping to a **distinct port**
            (rung 4 → `:9222`, rung 5 → `:9223`) the operator binds to the
            matching profile — replacing the implicit "which profile is on
            `:9222`". Rung-specific not-reachable errors (rung 5's names the
            credential boundary and warns it's a deliberate escalation).
            Rung-4 live-proven on adoption (change is port-param, unit-covered);
            **rung-5 live fetch is owed-to-operator** by nature (needs the
            operator's everyday Chrome on `:9223` — can't be self-driven).
      - [x] **Elevate the credential boundary + ladder to `method/` doctrine**
            — DONE 2026-07-12 (session 47, Opus): `method/REACH.md` written,
            grounded in the browser-fetch README + this item. Both halves in one
            doc: the escalation ladder (engine-agnostic, cheapest-first) and the
            credential boundary as a purpose-of-storage test. Named for the
            instruments' third verb (*extend reach*, ADR 0006), indexed after
            ACCESS in the SECRETS/ACCESS family. **Review-owed** (cold
            fresh-context, session-40/44 pattern) — pre-seeded questions: does
            the ladder's generic shape stay honestly grounded without inventing
            rungs the instance doesn't have; is the two-halves-one-doc join
            argued or asserted; does the purpose-of-storage test cover the real
            estate cases without outlawing intended use. The rule as captured:
            - **Provisioned stores are the intended path** — credentials saved
              *so that* a repo/tool/agent can use them (keychain items the estate
              registry records, minted per-consumer API tokens, the SECRETS/
              ACCESS machinery). Agent use is what they exist for; in scope by
              design.
            - **Personal convenience stores are off-limits by default** — a
              browser profile's saved logins, the principal's password manager
              (here Apple Passwords; browsers hold little to nothing by his own
              practice): saved over years to ease the *principal's own* browsing,
              never provisioned for agent use, and far broader than any task
              needs. Riding an already-authenticated *session* is fine; the
              stored credentials that mint sessions are the line.
            - **The principal can grant across the line** — temporary or
              permanent, per credential, his explicit act; a grant moves that
              credential into the intended path (and belongs in the provisioned
              machinery, not ad-hoc).
            A shareable SECRETS/ACCESS-family boundary, currently stated only
            operationally in the browser-fetch README. The escalation principle
            (start cheapest, step down only when blocked) is likewise general.

## instruments/ layer (new 2026-07-11, ADR 0006)

- [x] **ccrepo — cost fidelity, full breakdown, and reach** (Mike, 2026-07-11) —
      three strands to make the DevFinOps view truer and more accessible; all
      three now addressed (the VS Code *build* stays a separate decision):
      - [x] **Actuals vs estimate — show both.** DONE 2026-07-11 (Opus, session
            38): config confirmed (USD Max-20x, all Claude families covered) and
            the code built. `~/.claude/ccrepo-billing.json` (machine-local, never
            in a repo; absent ⇒ estimate-only, byte-identical JSON contract
            preserved; malformed ⇒ ignored-with-warning, never fatal) drives an
            **Actual** column beside **Est (API)**: `covers[]` matches model
            families by prefix (after `claude-` stripped), `perTokenModels` carves
            one back out; covered tokens cost $0 marginal, the sunk plan fee is
            apportioned per repo by covered-token share (falls back to total-token
            share if nothing covered ran in range), uncovered models keep the
            API-rate figure. **Actual = plan share + uncovered spend**, so TOTAL
            Actual = fee + all uncovered — proven live: estate-wide Est
            US$2,305 vs Actual US$200 (the whole plan fee), and `--by-model`
            children sum to their repo. Both columns convert together under
            `--fx`; `--no-billing` forces estimate-only. Multi-month outlay +
            overage thresholds out of scope v1, stated as footnotes. 8 new pure
            tests (`loadBilling`/`coversPredicate`/`actualFor`/covered-split
            fold); suite 26→34 Node.
      - [x] **Full ccusage breakdown** — DONE 2026-07-11: ccrepo now shows
            Cache Create · Cache Read · **Cache Hit** (reads ÷ prompt-side
            tokens, the point-don't-paste signal made observable) alongside
            Input/Output/Total/Cost, in the table, `--by-model`/`--by-day`
            children, and `--json` (`cacheCreationTokens`/`cacheReadTokens`/
            `cacheHitRate`); definition footnoted in the output. Tests updated
            + new `cacheHitRate` unit (fixtures now mirror ccusage's real
            shape: totalTokens includes cache); driven live — repo-level hit
            rates 95–98%.
      - [x] **VS Code UI — SCOPED 2026-07-11** (the item asked for scoping
            before building; grounded via current docs, not memory). Findings:
            the official Claude Code extension exposes **no** third-party hook
            points (no API, no contributed-view extension points; open feature
            requests confirm); Claude Code's **statusline** can carry per-repo
            cost (rich stdin JSON incl. `workspace` + live session cost;
            ~1.1 s ccrepo run needs a TTL cache) but renders **only in
            terminal surfaces**, never the graphical panel. Recommended route:
            a tiny **sideloaded companion extension** (status bar item +
            tooltip breakdown reading `ccrepo --json`; local `.vsix`, no
            marketplace; declare workspace-trust, resolve PATH explicitly),
            ~4–6 h, with a ~1 h spike (40-line extension showing the workspace
            total) as the feasibility proof. Statusline script is a free
            adjunct for terminal sessions. Build is a separate decision.
- [x] **cctranscript — per-reply response IDs (`N.M`)** — DONE 2026-07-11.
      Both open decisions taken and stated in the code: a "reply" is a **text
      reply only** (the unit a human cites; thinking/tool turns stay
      unnumbered even under `--full` — clutter loses), and `--json` carries a
      `ref` field on every turn (`"1"` on prompts, `"1.2"` on replies, null on
      think/tool/result) so citations are machine-addressable. Header shows
      `◂ Claude 1.1 (Opus 4.8)`; a reply before any prompt (resumed session)
      numbers under exchange 0, honestly marking its prompt isn't in the log.
      `numberTurns()` pure + unit-tested; `--json` contract test asserts the
      ref scheme; driven live.
- [x] **ccrepo + cctranscript ship untested** — DONE 2026-07-11 (session 35).
      They shipped with no tests (session 34), unlike the `tools/` scanners which
      each carry a unittest + `--selftest`; cctranscript had since grown real
      rendering logic (wrapping, markdown, model tags, right-align, exchange
      rules). Now floored with `node:test` + `node:assert` — **zero-dep, mirrors
      `tools/`'s stdlib-only pattern and sets the Node layer's test convention**
      (the first Node test surface; decision recorded in the session log). Minimal
      testability refactor only: each CLI entrypoint guarded by
      `require.main === module`, pure functions `module.exports`ed — no behaviour
      change, except one stated fix (an explicit `.jsonl` path now recovers its
      repo label via `cwdFromLog`, as every other route already did). Coverage:
      `instruments/cctranscript.test.js` — a `--json` output-contract test over a
      checked-in synthetic fixture (`fixtures/session-sample.jsonl`) asserting role
      classification, model mapping, timestamp/text extraction, and `--think`/
      `--tools` gating (this is what catches a Claude Code log-format change), plus
      pure-function units; `instruments/ccrepo.test.js` — pure functions and the
      aggregation fold over fixture ccusage rows. Wired into `ci.yml`'s floor job.
      Grounded in EVIDENCE §14 (an honest instrument's "ok" is a claim the apex
      governs). **Residual:** ccrepo's coverage is pure-functions + aggregation
      only — the `ccusage` `execFileSync` call, JSON parse, FX conversion, and
      table render sit behind an untested seam (aggregation was factored out to
      `aggregate()` to test the fold; the shell-out itself has no test double yet).

## Doctrine calibration — reviewed

- [x] **Review the "match the ceremony to the risk" doctrine change** — RAN
      2026-07-11 (Fable, fresh session, the light read the item asked for):
      **PASS, no findings.** Grounding verified by probe, not read: `don't-stack`
      appears nowhere in pre-change `docs/method/` (`git grep` at `cb37310^` —
      the "un-codified habit enforced as a rule" claim is true), and the
      original hygiene item 1's own rationale was always pivot-cost, so the
      sharpening is restoration, not revision. Consistency held everywhere
      checked: the narrowed don't-stack matches all five recorded applications
      (each was a gate on unreviewed tooling/doctrine); the self-verifying
      carve-out cannot be over-read to exempt scanner-class changes because the
      **silent-failure-mode bullet catches them** — and the same session's
      child-CI-floor review is the live demonstration of both halves (d0870a4
      earned its review and needed it: the class was still open in the sibling
      scanners; the records-only edits around it earned none). Recursive check
      honoured: flagged, not self-certified, merged by the principal.
      Follow-up DONE 2026-07-11 (Opus, session 31, `53b41db`): the condensed
      `build/templates/docs/MODEL-ECONOMICS.md` hygiene line shipped the exact
      "One task per session; start fresh" misread this change diagnosed —
      inherited by every scaffold. Rewritten to carry the sharpening (a coherent
      *line*, not a checkbox; break for a genuine reason, not a green item) plus
      the new ceremony-to-risk bearing. Judged self-verifying, not a fresh
      review: it applies an *already-reviewed* decision to its condensed mirror
      (the second-copy-drift class test_templates.py guards; no live pin on this
      file's body). Suite 205 OK, unchanged.

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
      [rejected] decision, RECORD integration-boundary lockstep, PRINCIPLES
      missing cases, stale README/CHANGELOG). **The gate is cleared —
      extraction may resume.** Notably: the sharpest ask's premise was
      corrected, not confirmed — Fable is the *more* capable tier (the reframe
      to independence-as-core still landed, for peer adopters without a
      superior tier).
- [x] **Method-review follow-ups ([backlog] findings)** — CLOSED. faves adopted
      the P1 trust-surface floor wording at its session-21 pin bump
      (dde4170→bbdeece); the 2026-07-11 session-31 fleet bump then carried all
      three children (faves/numen/ros) current to `d45a431` — `tools/pins.py`
      reads **all 3 current ✓**.
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
      - [x] **ros: first consolidated estate access map** (B14) — DONE
            2026-07-12 (session 47; created by an agent scoped inside the private
            ros repo, then **landed on ros main** by the main line once ros's PR
            merged and it had no live session). `docs/ACCESS-MAP.md` in ros: a row
            per domain across ACCESS.md's four axes, seeded from ros's own
            scattered facts, honest per-domain onboarding status (nothing rounded
            up to "onboarded"). **Read before finalize caught a stale status** —
            a cell seeded while a ros work-stream was still in flight had gone
            stale by land time (the work had since merged, reviewed and
            live-proven), so it was corrected before push. Rebased onto the
            merged main (conflict-free, new file), signed, ff-merged + pushed
            (`82db55c`), worktree/branch put away. ACCESS.md's honest-status note
            flipped (map now exists). **Note:** ros's floor is red, but *not* on
            this map (it scans clean) — pre-existing scanner findings the owner
            judges false-positive-class, red since before the map landed;
            specifics in ros's own records. Separate from B14.
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
- [ ] **Code-signing standard across the fleet** (Mike, 2026-07-11) — "how do we
      sign all the code in the various repos". Two distinct layers, deliberately
      split by cost:
      - [x] **Doctrine drafted — DONE 2026-07-11 (Fable):** `method/SIGNING.md`
            + ADR 0007. SSH-native commit/tag signing fleet-wide (dedicated
            ed25519 signing key, machine-global config + create-repo-baked
            repo-local `commit.gpgsign=true`, one canonical append-only
            `allowed_signers` tracked in atelier, CI verification from each
            repo's adoption boundary; history never rewritten to sign it; what
            a signature honestly claims — machine custody, not personal
            authorship — stated per the apex). Rejected: GPG, sigstore/gitsign,
            no-signing (see the ADR). **Reviewed 2026-07-12** — PASS-WITH-
            FINDINGS, all G1–G10 addressed pre-activation (see the review-owed
            section above; `reviews/2026-07-12-signing-doctrine.md`).
      - [x] **Activation (ladder in SIGNING.md) — FULLY ACTIVE 2026-07-12 (Opus,
            session 41), warn-first.** All five ladder steps done. Step 1: Mike
            registered a dedicated ed25519 signing key (his act). Step 2: machine
            wired, atelier boundary `958b1ea` proven on both planes
            (`git verify-commit` good + `gh api …verified` true). Step 3:
            `create-repo` + REPO-STANDARD bake repo-local `commit.gpgsign`. Step
            5: `tools/signscan.py` (two-plane, known-signed-fixture selftest) +
            CI verification in atelier `ci.yml` and the child `floor.yml`
            template, trust list at the child's pin, **warn-first**. Step 4: **10
            house-floor children retrofit** (pin bump + floor signing steps +
            `SIGN_BOUNDARY`), 7 CI-green, 3 red on **pre-existing scanner debt**
            that fails before the signing steps run — not signing, the owner's
            debt (which children, and what debt, lives in their own private
            records — the name × debt join stays out of public atelier per
            RECORD; joined here until the 2026-07-12 session-47 scrub). **Bug the dogfood caught:**
            bare `valid-after` is read in the verifier's local tz, so atelier's
            own first CI run flagged every signed commit "not yet valid" in the
            UTC runner — fixed by UTC-anchoring with a `Z` suffix; SIGNING.md now
            mandates it, the selftest guards it. Caught before any child was
            touched — the reason to dogfood atelier first.
            **Two follow-ups (below).**
      - [x] **faves + ros: adopt the house floor (then signing-CI).** Both run
            bespoke `ci.yml`, never adopted `floor.yml`, so the fleet retrofit
            skipped their signing *verification* (they still sign every commit).
            A separate standardisation pass: give them the house floor, or inject
            signing steps into their bespoke CI. The pre-existing gap this work
            surfaced.
            - [x] **DONE 2026-07-12 (Fable, session 42) — full adoption, both
                  floors green on first run.** Current template alongside each
                  repo's bespoke `ci.yml`; pins bumped to a trust-resolving SHA
                  (both old pins predated `allowed_signers`, so verification
                  would have silently skipped); boundaries at each repo's last
                  unsigned commit; two-plane verification *verified* (not
                  skipped) — faves 9/9, ros 2/2 good. Unlike the three
                  debt-red children, both went green by encoding each repo's
                  charter through the scanners' designed hatches: repo-type
                  `--disable` tuning (content shapes for a listings site,
                  network shapes for a network-inventory repo — the flag's own
                  documented example), reasoned ignore globs for chartered
                  content (each entry stating it does NOT survive the
                  publish-time scrub pass), inline allow-markers for the
                  handful of shape false positives. licenscan enabled in both
                  (settled Apache-2.0 — the template's stated trigger); four
                  real broken links fixed in passing. leakscan CI cover stays
                  honestly structural-only; full-term cover remains on the
                  pre-commit hook.
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
- [x] **The next widening — plugin/skills bundle SPENT 2026-07-11** (Opus,
      session 38): the plugin bundle (PR #3) merged to `main` on Mike's explicit
      go-ahead — atelier is now an installable Claude Code plugin+marketplace,
      the doctrine travelling as behaviour (the higher-leverage option this item
      named). See the merged plugin-review item above for the go-live detail.
      **The live floor now advances to the *next* deliberate widening** — a
      public announcement, a v2 plugin (de-instanced `create-repo`, `worktree`/
      `fleet-pins` commands), or a published package. Still Mike's call, never the
      agent's initiative. For an announcement, reuse the ros `PUBLISHING.md`
      extract-scrub-fresh-export pattern; **scrub list must include client
      names**.
- [ ] **v2 plugin — CHOSEN 2026-07-13 (Mike's call): the next widening is
      spent here.** De-instance `create-repo` so it travels in the plugin, and
      ship `worktree` + `fleet-pins` as plugin commands — doctrine travelling
      as behaviour, wider than the current bundle. Needs a scoping pass first
      (what "de-instanced" means for a skill that stamps house identity), then
      the build; go-live via PR like the v1 bundle, reviewed before merge.
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
- [x] **Wire the public scanners into child CI** — DONE 2026-07-10 (Opus): the
      other half of the CI build, unblocked by the public flip (ADR 0005).
      `docs/build/templates/workflows/floor.yml` — a language-agnostic scanner
      floor any doctrine-inheriting child drops in beside its `ci.yml`. It checks
      `mike548141/atelier` out **as a sibling** and runs its public
      secretscan/leakscan/linkscan against the child's own tree (`repo/`) — no
      secret, no vendored copy, no drift. Design calls stated in the header, not
      buried: **floats `atelier@main`** (a scanner *floor* wants newest; also
      avoids a second stamped-SHA drift surface — the CLAUDE.md pin stays the sole
      doctrine-version truth; `ref:` commented for anyone wanting reproducible CI);
      **leakscan structural-only** (term list is machine-local — same honest scope
      as atelier's own `ci.yml`); **licenscan commented** (it hard-fails with no
      LICENSE, so it's a *publish* gate, wrong to default-on for a private child).
      Scan scoped to `repo/` because a whole-workspace scan would false-positive
      on atelier's own fake-secret fixtures (proven, load-bearing). Driven both
      ways before claimed: clean child passes 0/0/0, damaged child (real `AKIA…`
      key + broken link) blocks. Wired into create-repo (seed step 3, step 6 CI
      text), REPO-STANDARD file set, and pinned by 5 `test_templates.py` tests
      (one-source, repo-scoped, structural-only, licenscan-commented, least-priv;
      suite 190→195). The step-6 "not wired yet" text is retired.
  - [x] **Exercised on a real child (numen) — DONE 2026-07-11 (Opus).** Session
        27's owed real-child run: numen adopted `floor.yml`, closing its own
        stated no-CI-gate (unblocked by ADR 0005). Driving it caught two real link
        breaks in numen before push and exposed a **four-session linkscan false
        negative** — `SKIP_DIR_NAMES` held `build`, masking atelier's own
        `docs/build/` layer (14 files); fixed at `d0870a4` (drop `build`/`dist`;
        suite 195→196), which also caught the inherited template placeholder (now
        code-spanned). Proven on real GitHub Actions both ways: happy path green
        (`29092514962`), fail-closed red via a throwaway broken-link PR
        (`29092599385`, since cleaned up). Detail:
        `sessions/2026-07-11-28-child-ci-floor-exercised.md`.
  - [x] **Review the child-CI floor + the linkscan masking fix** — RAN
        2026-07-11 (Fable, cold session): **PASS-WITH-FINDINGS**, verdict below
        the divider in `docs/reviews/2026-07-11-child-ci-floor.md`. The brief's
        sharpest question answered decisively: the masking fix closed the
        *instance*, not the class — secretscan + leakscan still hardcode-skipped
        `build`/`dist` (a planted key in `docs/build/` scanned green, proven
        live), still phantom-succeeded on a nonexistent path (the linkscan L1
        class), and the child's ignore-file hatch was dead under exactly the
        floor.yml invocation (CWD-relative vs root-relative globs). Six findings
        N1–N6, all [fixed] + re-driven same session (suite 196→205): both
        scanners mirror the linkscan fixes; floor.yml gains every-push triggers
        (a never-PR'd branch was scanned by nothing), a selftests step, and
        in-file FP-hatch docs. Floating `atelier@main` attacked and **held**
        (N1–N3 reaching every child with zero bumps is the argument); the
        real-infra secret drive judged NOT owed (closed by composition).
        **Gate cleared — floor.yml may roll to further children.**
        - [x] Follow-ups — BOTH DONE 2026-07-11 (Opus), each proven on real
              infra. **atelier's own `ci.yml`** widened to every-push +
              `workflow_dispatch` (`2a4b2fd`); the gap-closure proven by pushing
              a throwaway `n4-trigger-proof` branch (never PR'd) and watching CI
              fire green on it — a run that would not have existed before — then
              torn down local+remote. **numen re-copied `floor.yml`** byte-for-
              byte from the post-review template (numen `f81f66f`), picking up the
              workflow-file fixes that don't float (N4 every-push, N5 selftests
              step, N6 hatch docs); numen's floor ran green with the new selftests
              step live in the job log. numen's tree re-scanned clean in the exact
              floor.yml shape first. numen's frozen pre-scaffold hook (no linkscan)
              stands as already flagged — its floor is the only linkscan gate.
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
- ~~`docker-heap` is unstandardised~~ — DONE 2026-07-11 (Opus, session 38):
  standardise-existing pass applied (doctrine block + pin `atelier@5db645e`,
  house README, `docs/` with ARCHITECTURE/ROADMAP/SESSIONS, CONTRIBUTING,
  `floor.yml` scoped for an infra repo, fail-closed hook, `.gitignore` fixed —
  it was self-ignoring + untracked). No stack config touched; what the scans
  reported is the owner's, in that repo's own private records *(reworded
  2026-07-13 on the principal's decision — the name × posture join; old wording
  in git history)*. Now `current` in `tools/pins.py`.
- ~~Where does estate-wide credential **governance** live?~~ — RESOLVED
  2026-07-13, the principal's designation: it lives in the **dedicated private
  estate-root repo**, which already exists and already holds the registry
  (metadata only — provider, scope, keychain item, expiry, roll story; never a
  value), the mint tooling, and the estate map, with its own ADR recording the
  root→child pattern. Which repo that is stays out of this public record —
  naming the registry's home is itself the pointer RECORD keeps out. The
  remaining half stands: the root→child *pattern* becomes a method/ candidate
  once a second provider confirms the shape.
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
