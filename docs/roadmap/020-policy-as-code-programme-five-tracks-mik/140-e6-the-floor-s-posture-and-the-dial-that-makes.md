- [ ] 🎯 **E6 — the floor's posture, and the dial that makes it reachable.
      RULED 2026-07-28 (Mike), three parts, all his call, none built.**

      **What was found.** The two boundary scanners hold *opposite* postures
      and nothing records that they differ. `leakscan` states its own at
      `leakscan.py`: over-flagging is fail-safe, because a false positive
      costs an allow-marker and a false negative costs a leak. `secretscan`
      states no posture at all and its docstring sells the reverse — context
      plus entropy as *precision* against raw entropy scanning. So the
      scanner guarding personal data is tuned to over-flag and the scanner
      guarding credentials is tuned to under-flag, which is backwards on
      risk: a leaked credential is actively exploitable in a way an address
      is not. No record shows that asymmetry being decided; it accumulated.

      **Why the narrowing happened — a design gap, not a judgement call.**
      `secretscan`'s `severity` field is decorative (`"high" | "medium" —
      advisory; any hit still blocks`), and the exit is a block on *any*
      finding. With one dial, the only way to avoid crying wolf on every git
      SHA and hex blob is to shrink detection — which is exactly what the
      `SLUG_RX` comment records itself doing ("deliberately letters-only …
      a real (pre-existing) gap and not one to widen"). **That decision was
      the principal's to make and was recorded as a code comment**, where it
      never reached him. Named as its own failure shape: a coverage
      narrowing settled at tool altitude.

      - **E6a — DONE 2026-08-03** (orchestrated run): the posture is doctrine
            — `SECRETS.md` § *The boundary's posture* states Mike's intent as
            the bar both scans answer to, over-flag as the fail-safe
            direction, the leakscan/secretscan asymmetry as
            found-and-decided, EI5's grounding (rotation presupposes
            detection), coverage narrowing as the principal's decision never
            a code comment, and the advisory dial as decided-not-built with
            EI1's consumer precondition. Rule-4 `⏳` queued at landing
            (§ *Doctrine — review-owed*).
      - **E6b — DONE 2026-08-06** (wt: e6b-secretscan-advisory-0806):
            every finding now carries a `response`; the blocking set is
            byte-identical (pinned by tests) and the new
            `low-variety-entropy` rule reports E6c's ruled whole shape on
            the context-free path — EI4's named narrowing site — at
            exit 0. All three ruled consumer legs landed: commit-time
            print, CI tree-wide re-print on every push (documented and
            pinned against a future scope narrowing), and the floor
            board's persistent 🟡 count with a 🔴 drift state so silence
            and zero can never look alike. First live run: 21 advisory
            findings tree-wide, every one a hash — a board reading 🟡 is
            the ruling working on day one. Interpretation made at the
            build and flagged to Mike: "the floor board" was read as
            `floor.py`'s per-repo board, not `floorfleet`'s estate board
            (which runs no scanners). **RULED 2026-08-09 (Mike): the
            per-repo build stands, AND an estate-wide combined view is
            funded — built in the private estate-root repo** (unnamed
            here by standing rule; the same convention as B1's scheduled
            job), as estate-state reporting rather than atelier
            machinery. Item queued below. Detail →
            [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *E6b built*.
      - [ ] **Estate-wide advisory-count view (Mike ruled 2026-08-09).**
            One screen totalling each repo's secretscan advisory count
            across the estate. Lives in the private estate-root repo —
            estate state, not shareable method — so the build is that
            repo's work; atelier's part, if any, is whatever output
            contract the view reads (the advisory-count line is already a
            pinned contract). Pattern precedent: B1's scheduled
            conformance job, which already enumerates the fleet from
            GitHub with a read-only token.
      - [ ] **E6d — impact is the second axis. RULED 2026-07-28 (Mike).** The
            tier must weigh *risk*, not confidence alone: a mid-confidence hit
            on a credential that opens the whole estate outranks a
            high-confidence hit on something insignificant. **The field the
            code calls `severity` is already confidence wearing severity's
            name** — `gcp-oauth-secret` is graded `medium` because its
            *pattern* is less specific, and `stripe-key` grades `sk_live_` and
            `sk_test_` identically while the token itself states its own blast
            radius. Three rulings:
            **(i) Escalate only.** Impact may raise a finding's response,
            never lower it. A high-confidence hit on something trivial still
            blocks exactly as today. Grounds: the downward direction is where
            a "this one doesn't matter" lane would live, and that assessment
            has been wrong here before; examples and fixtures are already
            served by placeholder detection and allow-markers, which force a
            written reason. Quieting comes from E6b's confidence tier, never
            from impact.
            **(ii) Repo-declared, via the seam that already exists.** Impact
            is *least* knowable exactly where it matters most: a shared
            scanner can class a vendor credential by construction, but cannot
            know what a home-grown `password=` opens. Only the repo knows, so
            the declaration rides the repo-local floor seam — which has **no
            adopters** (D4), and whose motivating case was a networking
            child's estate-token tripwire. That case is an impact declaration
            in all but name; adopting this proves the seam.
            **(iii) `confidence` × `impact` = `severity`, computed.** Rename
            the mislabelled field, add the second axis, and let the computed
            result drive block-vs-report — so the field stops misdescribing
            what it holds, which is how it came to be read as impact at all.
            **SCALE RULED 2026-08-04 (Mike, the EI3 proposal as brought):
            three repo-declared levels — `estate` / `repo` / `local`,
            undeclared defaults to `repo`** (the middle: silence neither
            inflates nor waives), class terms only in public trees. Computed
            response: high confidence blocks as today at any impact;
            low + `estate` escalates to block; low + `repo` or `local` is
            advisory. Nothing ever de-escalates below today's behaviour;
            the F1 rebuild may revisit the model (FG2). **Sequencing ruled
            with it: the build pairs with one child's first impact
            declaration** — the estate-token tripwire case — proving the D4
            seam and the axis together.
      - **E6c — DONE 2026-08-03** (orchestrated run, with the SF residue in
            one build): whole-shape carve-outs decided before every
            variety-reading gate in assigned-secret context — an unbroken
            32+ alphanumeric run (both hex leading forms, uppercase,
            base32) and a four-plus separator-joined word passphrase (both
            spellings) are no longer identifier/slug-suppressed; the ruled
            six-shape probe went 2/6 → 6/6, the blocking set only widened,
            and placeholder/indirection/path suppression keeps precedence
            (statements of what a value is *for*, not its variety). SF3's
            canary suite (16 shapes, count pinned, contract stated) now
            guards the gate. Detail → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
            § *secretscan residue + E6c*.

      **The split that makes the intent affordable** (recorded because it is
      the reasoning, not the instruction): credential-key context is nearly
      free to widen, because the key name has already done the filtering;
      the context-free path is where SHAs, file hashes, hex data and base64
      blobs live, and that is the path the advisory tier serves. The three
      hard cases Mike named land as — examples → placeholder detection plus
      the queued "describe, don't quote" rule (E5); file hashes and hex data
      → separated by context already, since neither sits under a
      credential-named key.

      🎯 **REVIEWED 2026-07-29 (rule-4 Fable cold pass, design/intent):
      PASS-WITH-FINDINGS — 1 MAJOR / 2 MODERATE / 1 minor / 2 notes.
      EI1–EI6 RULED 2026-07-29 (Mike, plain-language walk-through):**
      EI1 — a named advisory-findings consumer is a **build precondition
      of E6b** (shape not pre-ruled); EI2 — estate-detail impact
      declarations never in public trees, class terms only there; EI3 —
      matrix/scale/undeclared-default are **concrete proposals brought to
      Mike at build pickup**, not pre-rulings and not the builder's to
      settle; EI4 — the item is corrected to name `HIGH_ENTROPY_RX`'s
      mixed-class requirement as the real narrowing site; EI5 — E6a
      grounds on *rotation presupposes detection*; EI6 — per-plane
      advisory semantics, E6a-first ordering, and the leakscan asymmetry
      recorded as decided. Rulings verbatim + counsel:
      [E6 intent cold pass](../../reviews/2026-07-29-1243-e6-intent-cold.md).
      **Application owed to a neutral hand** (authored neither the E6
      text nor the verdict); it queues its own rule-4 pointer at landing.
      The companion sweep the intent record itself flags — whether
      `leakscan` reaches the PII half of the stated intent as
      `secretscan` reaches the credential half — is endorsed by the pass
      as real open work, not folded into it. **Ran 2026-08-03 → E7 below.**
