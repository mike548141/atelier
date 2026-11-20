# Done before the split

The board's finished work from before it moved to one file per item,
cut from `docs/ROADMAP-DONE.md`
(last changed in `a9abc266`) into one `[x]` item file per entry by
`tools/archivecut.py`. Below the marker line this page is that file
verbatim: its preamble, its headings and every line that was not an
entry, in order, with each entry replaced by a link to the item file
that holds it, and links re-pointed for the new depth.
`python3 tools/archivecut.py --verify` rebuilds the original from these
files and compares it with the last committed copy.

<!-- archivecut:verbatim-below -->
# atelier ROADMAP — completed detail (archive)

The append-only companion to [`ROADMAP.md`](../../ROADMAP.md): the case-law of finished
work, moved here so the live roadmap stays lean (the current-truth/history split,
`method/RECORD.md`). **Entries are preserved verbatim** from ROADMAP.md; this
file is a destination that is *meant* to grow (`sizescan` never meters its size;
since 2026-07-22 it checks archive stores for **harvest integrity** — a live
`[ ]`/`[~]`/`⏳` list item here gates the floor: finished history only, `[x]`
with a disposition note where work was superseded or declined).
First harvested 2026-07-14 (ROADMAP.md had reached 1091 lines).

**FROZEN 2026-08-15** (board-store ADR, Mike's ruling): the board moved to one
file per item under [`roadmap/`](../README.md), and a done item now simply
stays in its own file as `[x]` — its `git log` is the provenance a harvest used
to approximate. Nothing new is harvested here; this file remains the verbatim
archive of everything completed before the split, grepped on demand.

## Doctrine — completed review cycles
- ✅ [0010-awa1-awa4-rulings-aw-application-cold-pass-ver](0010-awa1-awa4-rulings-aw-application-cold-pass-ver.md)
- ✅ [0020-sca1-sca3-rulings-sc-application-cold-pass-ver](0020-sca1-sca3-rulings-sc-application-cold-pass-ver.md)
- ✅ [0030-eb1-eb8-rulings-economics-cold-pass-verdict](0030-eb1-eb8-rulings-economics-cold-pass-verdict.md)
- ✅ [0040-qa1-qa6-rulings-qr-application-cold-pass-verdi](0040-qa1-qa6-rulings-qr-application-cold-pass-verdi.md)
- ✅ [0050-va1-va4-rulings-v2-plugin-application-cold-pas](0050-va1-va4-rulings-v2-plugin-application-cold-pas.md)
- ✅ [0060-sa1-sa8-rulings-secrets-access-cold-pass-verdi](0060-sa1-sa8-rulings-secrets-access-cold-pass-verdi.md)
- ✅ [0070-hi-application-pass-residue-ha1-ha5-mike-s-rul](0070-hi-application-pass-residue-ha1-ha5-mike-s-rul.md)
- ✅ [0080-hi-application-cold-pass-terminal-cycle-closed](0080-hi-application-cold-pass-terminal-cycle-closed.md)
- ✅ [0090-harvest-integrity-gate-cold-pass-run-ruled-app](0090-harvest-integrity-gate-cold-pass-run-ruled-app.md)
- ✅ [0100-harvest-integrity-invariant-no-live-checkbox-i](0100-harvest-integrity-invariant-no-live-checkbox-i.md)
- ✅ [0110-interruption-resilience-cycle-ir1-ir4-await-mi](0110-interruption-resilience-cycle-ir1-ir4-await-mi.md)
- ✅ [0120-scope-lens-4-cycle-residue-ac1-ac2-mike-s-ruli](0120-scope-lens-4-cycle-residue-ac1-ac2-mike-s-ruli.md)
- ✅ [0130-draft-the-three-interruption-resilience-gaps-a](0130-draft-the-three-interruption-resilience-gaps-a.md)
- ✅ [0140-review-line-artefact-cycle-rs1-rs6-closed-2026](0140-review-line-artefact-cycle-rs1-rs6-closed-2026.md)
- ✅ [0150-reach-autonomy-backlog-h1-h8-residuals-closed](0150-reach-autonomy-backlog-h1-h8-residuals-closed.md)
- ✅ [0160-fleet-re-stamp-of-the-reviews-template](0160-fleet-re-stamp-of-the-reviews-template.md)
- ✅ [0170-documentation-doctrine-what-great-documentatio](0170-documentation-doctrine-what-great-documentatio.md)


- ✅ [0180-concurrency-posture-flip-assume-you-are-not-al](0180-concurrency-posture-flip-assume-you-are-not-al.md)

- ✅ [0190-session-onramp-operating-rhythm-surface-the-wo](0190-session-onramp-operating-rhythm-surface-the-wo.md)
- ✅ [0200-cli-docs-standard-applied-batch-cold-pass-revi](0200-cli-docs-standard-applied-batch-cold-pass-revi.md)
- ✅ [0210-adr-0006-addendum-ccarchive-the-preserve-verb](0210-adr-0006-addendum-ccarchive-the-preserve-verb.md)
- ✅ [0220-conventions-utc-at-rest-adr-applied-batch-cold](0220-conventions-utc-at-rest-adr-applied-batch-cold.md)
Closed doctrine review cycles (REVIEW rule 4, MODEL-ECONOMICS triple delta,
"informed principal" apex rule, PRINCIPLES §2 four bullets — all CYCLE CLOSED
2026-07-14/15) → [`README.md`](README.md) § Doctrine — completed
review cycles.
- ✅ [0230-review-rule-4-cycle-closed-2026-07-15](0230-review-rule-4-cycle-closed-2026-07-15.md)
- ✅ [0240-model-economics-triple-delta-cycle-closed-2026](0240-model-economics-triple-delta-cycle-closed-2026.md)
- ✅ [0250-informed-principal-apex-rule-reviewed-applied](0250-informed-principal-apex-rule-reviewed-applied.md)
- ✅ [0260-principles-2-four-bullets-cycle-closed-2026-07](0260-principles-2-four-bullets-cycle-closed-2026-07.md)
- ✅ [0270-applied-batch-cold-pass-concurrency-claiming-w](0270-applied-batch-cold-pass-concurrency-claiming-w.md)
- ✅ [0280-cold-review-of-concurrency-claiming-work](0280-cold-review-of-concurrency-claiming-work.md)
- ✅ [0290-cold-pass-on-the-applied-reach-batch-ran-2026](0290-cold-pass-on-the-applied-reach-batch-ran-2026.md)
- ✅ [0300-review-md-reviewer-independence-rule-decided-2](0300-review-md-reviewer-independence-rule-decided-2.md)
- ✅ [0310-cold-review-of-the-applied-independence-batch](0310-cold-review-of-the-applied-independence-batch.md)
- ✅ [0320-reach-md-adversarial-re-review-decided-2026-07](0320-reach-md-adversarial-re-review-decided-2026-07.md)
- ✅ [0330-cold-review-of-method-reach-md](0330-cold-review-of-method-reach-md.md)
- ✅ [0340-cold-review-of-method-communication-md](0340-cold-review-of-method-communication-md.md)
- ✅ [0350-cold-review-of-record-keep-private-repos-gener](0350-cold-review-of-record-keep-private-repos-gener.md)
- ✅ [0360-cold-review-of-the-signing-doctrine-signing-md](0360-cold-review-of-the-signing-doctrine-signing-md.md)
- ✅ [0370-cold-review-of-principles-8-leverage](0370-cold-review-of-principles-8-leverage.md)
- ✅ [0380-cold-review-of-the-plugin-bundle-pr-3](0380-cold-review-of-the-plugin-bundle-pr-3.md)
- ✅ [0390-cold-review-of-concurrency-every-branch-ends-p](0390-cold-review-of-concurrency-every-branch-ends-p.md)
- ✅ [0400-create-repo-new-repos-born-with-delete-branch](0400-create-repo-new-repos-born-with-delete-branch.md)

## Raised 2026-07-12 (logged, then resolved)

- ✅ [0410-apply-the-reach-re-review-findings-a1-a8-on-mi](0410-apply-the-reach-re-review-findings-a1-a8-on-mi.md)
- ✅ [0420-session-38-borderline-join-scrubbed-2026-07-13](0420-session-38-borderline-join-scrubbed-2026-07-13.md)
- ✅ [0430-review-md-encode-reviewer-independence](0430-review-md-encode-reviewer-independence.md)

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
- ✅ [0440-adopt-browser-fetch-as-a-teammate-capability](0440-adopt-browser-fetch-as-a-teammate-capability.md)
- ✅ [0450-fetch-escalation-ladder-build-the-missing-rung](0450-fetch-escalation-ladder-build-the-missing-rung.md)

## instruments/ layer (new 2026-07-11, ADR 0006)

- ✅ [0460-both-observers-read-the-ccarchive-archive-from](0460-both-observers-read-the-ccarchive-archive-from.md)

- ✅ [0470-fill-the-machine-local-spend-config-done-2026](0470-fill-the-machine-local-spend-config-done-2026.md)

- ✅ [0480-man-page-convention-rollout-cctranscript-ccrep](0480-man-page-convention-rollout-cctranscript-ccrep.md)

- ✅ [0490-ccrepo-cost-fidelity-full-breakdown-and-reach](0490-ccrepo-cost-fidelity-full-breakdown-and-reach.md)
- ✅ [0500-cctranscript-per-reply-response-ids-n-m](0500-cctranscript-per-reply-response-ids-n-m.md)
- ✅ [0510-ccrepo-cctranscript-ship-untested](0510-ccrepo-cctranscript-ship-untested.md)

## Doctrine calibration — reviewed

- ✅ [0520-review-the-match-the-ceremony-to-the-risk-doct](0520-review-the-match-the-ceremony-to-the-risk-doct.md)

## Done (2026-07-10)

- ✅ [0530-scaffold-method-first-slice-00-apex-autonomy-s](0530-scaffold-method-first-slice-00-apex-autonomy-s.md)
- ✅ [0540-foundation-review-2-fable-1-harvest-docs-revie](0540-foundation-review-2-fable-1-harvest-docs-revie.md)
- ✅ [0550-autonomy-floor-closed-self-widening-lockout-cl](0550-autonomy-floor-closed-self-widening-lockout-cl.md)
- ✅ [0560-canonicality-decided](0560-canonicality-decided.md)
- ✅ [0570-all-models-one-doctrine-stated-apex-who-it-bin](0570-all-models-one-doctrine-stated-apex-who-it-bin.md)

## Next — the propagation mechanism (do BEFORE further extraction)

The load-bearing architecture, review-endorsed shape: **"thin anchor, fat
pointer"** (dependency + lockfile for doctrine). Written up in
`docs/method/PROPAGATION.md` (2026-07-10).

- ✅ [0580-version-atelier](0580-version-atelier.md)
- ✅ [0590-define-the-standard-child-claude-md-doctrine-b](0590-define-the-standard-child-claude-md-doctrine-b.md)
- ✅ [0600-retrofit-faves-and-ros](0600-retrofit-faves-and-ros.md)
- ✅ [0610-layer-override-rule](0610-layer-override-rule.md)
- ✅ [0620-enforcement-clause](0620-enforcement-clause.md)

## Review gate — before more content stacks on the method/ layer

The "mechanism/review before more content" rule: the keystone + the whole `method/`
layer earn a review with fresh context before extraction continues.

- ✅ [0630-fable-review-of-the-method-layer](0630-fable-review-of-the-method-layer.md)
- ✅ [0640-method-review-follow-ups-91-backlog-93-finding](0640-method-review-follow-ups-91-backlog-93-finding.md)

## Then — extraction (keep the case-law, don't strip it)

Generalise the *bearings/cases*, don't delete them (a de-cased principle is
theatre). Leave tiki-specific bearings + review case-law in ros.

- ✅ [0650-principles-md](0650-principles-md.md)
- ✅ [0660-trim-ros-docs-principles-md](0660-trim-ros-docs-principles-md.md)
- ✅ [0670-model-economics-md](0670-model-economics-md.md)
- ✅ [0680-evidence-md](0680-evidence-md.md)
- ✅ [0690-peer-review-lifecycle](0690-peer-review-lifecycle.md)
- ✅ [0700-model-capability-authority](0700-model-capability-authority.md)
- ✅ [0710-source-acquisition-ladder-a6-honest-instrument](0710-source-acquisition-ladder-a6-honest-instrument.md)

## Review gate — the post-method-review batch (before more content stacks)

The same "mechanism/review before more content" rule that gated the `method/`
layer now gates everything built since it. Session 15 flagged this as the
standout debt; sessions 14–15 deliberately did not stack on it.

- ✅ [0720-fable-sweep-of-the-957fa08-f72031c-batch](0720-fable-sweep-of-the-957fa08-f72031c-batch.md)
- ✅ [0730-batch-review-follow-ups-91-backlog-93-findings](0730-batch-review-follow-ups-91-backlog-93-findings.md)

## build/ layer + inheritance delivery — completed
- ✅ [0740-extract-the-create-repo-standard-into-docs-bui](0740-extract-the-create-repo-standard-into-docs-bui.md)
- ✅ [0750-licence-consistency-pre-publish-gate](0750-licence-consistency-pre-publish-gate.md)

The completed children of the code-signing item (its open strands stay in ROADMAP.md):

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

- ✅ [0760-rewire-create-repo-to-inherit-from-atelier](0760-rewire-create-repo-to-inherit-from-atelier.md)

## Review gate — the create-repo delivery mechanism
The same rule, third application: the mechanism that stamps doctrine into every
future repo must itself be reviewed before it's *used in anger*. Brief written
2026-07-10: `docs/reviews/2026-07-10-create-repo-rewire.md` — range
`f72031c..92c0112` **plus the machine-local skill** (outside the repo; no other
review will catch it). Nine load-bearing assumptions to attack; the sharpest:
clone-loses-hook-and-config (does protection evaporate on machine two?),
template-block drift vs PROPAGATION's canonical text, and prose-stamp-procedure
as model-memory reborn. **Run cold, fresh session.**

- ✅ [0770-fable-sweep-of-f72031c-92c0112-the-skill](0770-fable-sweep-of-f72031c-92c0112-the-skill.md)

- ✅ [0780-don-t-scaffold-a-real-keeper-repo-on-the-unrev](0780-don-t-scaffold-a-real-keeper-repo-on-the-unrev.md)
- ✅ [0790-repo-boundary-guidance](0790-repo-boundary-guidance.md)
- ✅ [0800-parallel-work-tooling](0800-parallel-work-tooling.md)

## Safety tooling (gates the person-context + archive threads)

- ✅ [0810-mechanical-leak-scan](0810-mechanical-leak-scan.md)
- ✅ [0820-secret-scan-on-push](0820-secret-scan-on-push.md)
- ✅ [0830-data-protection-md](0830-data-protection-md.md)
- ✅ [0840-safe-access-onboarding-doctrine](0840-safe-access-onboarding-doctrine.md)
- ✅ [0850-secrets-md](0850-secrets-md.md)

## Sharing — completed
- ✅ [0860-p1-the-command-allowlist-is-untracked-estate-w](0860-p1-the-command-allowlist-is-untracked-estate-w.md)

- ✅ [0870-p2-publishscan-built-and-registry-wired-blocki](0870-p2-publishscan-built-and-registry-wired-blocki.md)

- ✅ [0880-public-release-readable-repo](0880-public-release-readable-repo.md)

- ✅ [0890-the-next-widening-plugin-skills-bundle-spent-2](0890-the-next-widening-plugin-skills-bundle-spent-2.md)

- ✅ [0900-atelier-s-own-ci](0900-atelier-s-own-ci.md)
- ✅ [0910-wire-the-public-scanners-into-child-ci](0910-wire-the-public-scanners-into-child-ci.md)
- ✅ [0920-markdown-internal-link-check](0920-markdown-internal-link-check.md)

## Open questions — resolved
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

## File-size hygiene — completed detail

- ✅ [0930-sizescan-reviewed-wired-into-the-gate](0930-sizescan-reviewed-wired-into-the-gate.md)

- ✅ [0940-atelier-sizescan-record-doctrine-this-roadmap](0940-atelier-sizescan-record-doctrine-this-roadmap.md)

- ✅ [0950-faves-sessions-roadmap-architecture-harvest-do](0950-faves-sessions-roadmap-architecture-harvest-do.md)

- ✅ [0960-shed-sessions-md-rotated-done-2026-07-18](0960-shed-sessions-md-rotated-done-2026-07-18.md)

- ✅ [0970-ros-completed-detail-harvest-done-2026-07-18](0970-ros-completed-detail-harvest-done-2026-07-18.md)

- ✅ [0980-ros-both-structural-calls-ruled-by-mike-applie](0980-ros-both-structural-calls-ruled-by-mike-applie.md)

- ✅ [0990-budget-hatches-must-be-grounded-corrected-2026](0990-budget-hatches-must-be-grounded-corrected-2026.md)

- ✅ [1000-lean-files-doctrine-sizescan-reviewed-2026-07](1000-lean-files-doctrine-sizescan-reviewed-2026-07.md)

- ✅ [1010-budgets-are-tripwires-not-targets-mike-s-rulin](1010-budgets-are-tripwires-not-targets-mike-s-rulin.md)

- ✅ [1020-size-signal-rebalance-to-a-cold-content-gate-c](1020-size-signal-rebalance-to-a-cold-content-gate-c.md)

- ✅ [1030-hooks-ateliertools-worktree-bug-was-fleet-wide](1030-hooks-ateliertools-worktree-bug-was-fleet-wide.md)

## instruments/ccarchive — completed detail (moved 2026-07-19)

- ✅ [1040-local-store-audit-vs-the-archive-manifest-done](1040-local-store-audit-vs-the-archive-manifest-done.md)

## Orchestrated queue run — completed detail (moved 2026-07-22)

The 2026-07-22-1018 run's ten landed items, harvested at the run's own close
(intent record: `sessions/2026-07-22-1018-orchestrated-queue-run.md`).

- ✅ [1050-secrets-md-access-management-expansion-access](1050-secrets-md-access-management-expansion-access.md)
- ✅ [1060-map-the-public-canon-against-method-the-scanne](1060-map-the-public-canon-against-method-the-scanne.md)
- ✅ [1070-model-economics-md-renamed-to-economics-md](1070-model-economics-md-renamed-to-economics-md.md)
- ✅ [1080-queue-run-name-the-pattern-in-method](1080-queue-run-name-the-pattern-in-method.md)
- ✅ [1090-queue-run-mechanise-it-as-a-skill](1090-queue-run-mechanise-it-as-a-skill.md)
- ✅ [1100-anti-slop-promotion-rule-the-mining-half](1100-anti-slop-promotion-rule-the-mining-half.md)
- ✅ [1110-ccrepo-tighten-the-ccusage-reconciliation-drif](1110-ccrepo-tighten-the-ccusage-reconciliation-drif.md)
- ✅ [1120-ccarchive-restore-from-archive-full-delta](1120-ccarchive-restore-from-archive-full-delta.md)
- ✅ [1130-ccarchive-icloud-dataless-file-awareness](1130-ccarchive-icloud-dataless-file-awareness.md)
- ✅ [1140-ccarchive-sign-the-manifest-tamper-evidence](1140-ccarchive-sign-the-manifest-tamper-evidence.md)
- ✅ [1150-ccarchive-is-there-any-metadata-it-misses](1150-ccarchive-is-there-any-metadata-it-misses.md)
- ✅ [1160-should-cctranscript-and-ccarchive-be-one](1160-should-cctranscript-and-ccarchive-be-one.md)

## Orchestrated queue run #2 — completed detail (moved 2026-07-22)

Run record: `sessions/2026-07-22-1210-orchestrated-queue-run.md`. Open residue
(🎯 VP1–VP8, 🎯 spend config, 🎯 D1–D5, the security-canon `⏳`) stays live in
ROADMAP.md; the finished detail is preserved here.

- ✅ [1170-v2-plugin-de-instance-review-delivered-2026-07](1170-v2-plugin-de-instance-review-delivered-2026-07.md)
- ✅ [1180-doctrine-edits-for-confirmed-gaps-a-b-c-e-buil](1180-doctrine-edits-for-confirmed-gaps-a-b-c-e-buil.md)
- ✅ [1190-actual-spend-plan-or-usage-vs-the-api-usage-es](1190-actual-spend-plan-or-usage-vs-the-api-usage-es.md)

## v2 plugin shipped + the VP/D rulings (moved 2026-07-23)

- ✅ [1200-v2-plugin-chosen-2026-07-13-shipped-2026-07-23](1200-v2-plugin-chosen-2026-07-13-shipped-2026-07-23.md)
- ✅ [1210-portability-d1-d5-ruled-2026-07-23](1210-portability-d1-d5-ruled-2026-07-23.md)

## The 2026-07-23 decision sitting — standing backlog cleared (moved 2026-07-23)

Mike worked the whole standing 🎯 backlog in plain-language walk-throughs
(run record: the 1210 queue-run's addenda). Rulings and their closed items:

- ✅ [1220-ccarchive-metadata-classes-signing-defaults](1220-ccarchive-metadata-classes-signing-defaults.md)
- ✅ [1230-invariant-candidates-s1-s5-v1-v7-all-approved](1230-invariant-candidates-s1-s5-v1-v7-all-approved.md)
- ✅ [1240-checkbox-grammar-keep-the-tri-state](1240-checkbox-grammar-keep-the-tri-state.md)
- ✅ [1250-session-archive-superseded-by-ccarchive-under](1250-session-archive-superseded-by-ccarchive-under.md)
- ✅ [1260-floor-template-duplicate-trigger-trim-pull-req](1260-floor-template-duplicate-trigger-trim-pull-req.md)
- ✅ [1270-signing-warn-block-flip-hold-re-confirmed](1270-signing-warn-block-flip-hold-re-confirmed.md)

Still Mike's, deliberately untouched: the honesty/truth/transparency note
(being expanded via the apex-triad work), the Teams-chat note (prompted
verbatim, awaiting his expansion), the glossary ratify pass (his read).

## Orchestrated queue runs 0441 + 0618 — completed detail (moved 2026-07-23)

Two Opus-orchestrated queue runs' deliveries. The 0441 run left its four `[x]`
items un-harvested on the live ROADMAP; the 0618 run harvested both runs'
completed items at its close to restore the `sizescan --check` floor to green
— the worked case for the ROADMAP "close all-clear should carry the pushed
floor run's result" capture (the floor had been red on un-harvested `[x]`
across several sessions).

### Doctrine

- ✅ [1280-in-repo-apex-restatements-swept-to-three-eleme](1280-in-repo-apex-restatements-swept-to-three-eleme.md)

### Anti-slop invariant scanners S1/S3/S5 + the S3 review

All three wired ADVISORY-ONLY (`--warn`, exit 0) in `ci.yml`; none in the
blocking pre-commit hook nor child `floor.yml` — each earns an independent
review before gating (don't-stack). Their `⏳` first-of-kind reviews (S1, S5)
and the datescan follow-ons (apply DSR1–DSR8; the advisory→blocking flip) stay
open on the live ROADMAP.

- ✅ [1290-s3-datescan-built-2026-07-23](1290-s3-datescan-built-2026-07-23.md)
- ✅ [1300-s1-wrapscan-built-2026-07-23](1300-s1-wrapscan-built-2026-07-23.md)
- ✅ [1310-s5-spellscan-built-2026-07-23](1310-s5-spellscan-built-2026-07-23.md)
- ✅ [1320-datescan-s3-review-done-2026-07-23](1320-datescan-s3-review-done-2026-07-23.md)

### instruments — cc-tools flag vocabulary (Mike, 2026-07-23)

- ✅ [1330-audit-align-the-flag-vocabulary-across-the-cc](1330-audit-align-the-flag-vocabulary-across-the-cc.md)
- ✅ [1340-flag-vocabulary-rule-ratified-2026-07-23-mike](1340-flag-vocabulary-rule-ratified-2026-07-23-mike.md)

### instruments — ccrepo rollup precompute ledger (Mike, 2026-07-17)

- ✅ [1350-ccrepo-rollup-precompute-ledger-delivered-2026](1350-ccrepo-rollup-precompute-ledger-delivered-2026.md)
- ✅ [1360-rollup-default-confirmed-2026-07-23-mike-trans](1360-rollup-default-confirmed-2026-07-23-mike-trans.md)
- ✅ [1370-ccrepo-context-size-column-delivered-2026-07-2](1370-ccrepo-context-size-column-delivered-2026-07-2.md)
- ✅ [1380-ccrepo-opus-5-price-gap-found-closed-2026-07-2](1380-ccrepo-opus-5-price-gap-found-closed-2026-07-2.md)

- ✅ [1390-ci-floor-restored-to-green-delivered-2026-07-2](1390-ci-floor-restored-to-green-delivered-2026-07-2.md)

## Queue run 0707 — datescan DSR-apply + S1/S5 first-of-kind reviews (moved 2026-07-23)

Verbatim from ROADMAP.md; the live follow-ons (apply-findings + Mike's-call
flips/rulings) stay open in ROADMAP.md. Session record:
[`sessions/2026-07-23-0707-orchestrated-queue-run.md`](../../sessions/2026-07-23-0707-orchestrated-queue-run.md).

- ✅ [1400-apply-datescan-review-findings-dsr1-dsr8-re-ba](1400-apply-datescan-review-findings-dsr1-dsr8-re-ba.md)
- ✅ [1410-wrapscan-s1-first-of-kind-review-done-2026-07](1410-wrapscan-s1-first-of-kind-review-done-2026-07.md)
- ✅ [1420-spellscan-s5-first-of-kind-review-done-2026-07](1420-spellscan-s5-first-of-kind-review-done-2026-07.md)

## Queue run 0959 — S2/S4 scanner builds + wrapscan/spellscan applies (moved 2026-07-23)

Opus-orchestrated queue run (Mike: "maximise plan use"), Sonnet executors in
worktrees, per-item close. Four items closed (a fifth, the RECORD.md
close-all-clear doctrine, stays live as a ⏳ review in ROADMAP.md).

### Anti-slop invariant scanners — S2 + S4 built (all five S1–S5 now built)

- ✅ [1430-build-the-approved-scanners-s1-s5](1430-build-the-approved-scanners-s1-s5.md)

### wrapscan (S1) review applied — WS1–WS6 + option-A scope

- ✅ [1440-apply-wrapscan-review-findings-ws1-ws6-impleme](1440-apply-wrapscan-review-findings-ws1-ws6-impleme.md)

### spellscan (S5) review applied — SS1–SS4 + catalogue rename

- ✅ [1450-apply-spellscan-review-findings-ss1-ss4-tame-t](1450-apply-spellscan-review-findings-ss1-ss4-tame-t.md)

### wrapscan + spellscan flipped advisory→blocking (Mike's rulings, same run)

Both scanners built/reviewed/applied earlier this run were flipped to BLOCKING on
Mike's plain-language rulings during the close-out:

- **wrapscan → blocking.** Precondition met (option-A doctrine-surface scope,
  0 findings). atelier `ci.yml` dropped `--warn`; child `floor.yml` template
  gained a blocking wrapscan step + selftest (children re-baseline their record
  stores via `.wrapscanignore` on adoption — atelier's doctrine-surface scope is
  atelier-specific, so children scope `repo/docs` broadly and ignore their logs).
- **spellscan → blocking** + the **frozen-record `artifact` question RULED: keep
  history verbatim.** The ~36 general-sense `artifact` breaches live in frozen
  record stores; Mike ruled they are NOT retro-spelled. So spellscan is scoped to
  the live doctrine surface with a `.spellscanignore` netting the record stores
  (`docs/sessions/`, `docs/reviews/`, `docs/SESSIONS.md`, `docs/ROADMAP-DONE.md`,
  `*-DONE.md`/`*-ARCHIVE.md`). Re-baseline turned up 2 genuine doctrine-surface
  findings, both resolved honestly: ADR 0007's "Artifact signing/SBOM" is the
  software-supply-chain term-of-art (allow-marked, not mis-corrected to
  "Artefact"), and one general-sense `artifact`→`artefact` fixed in a decision
  record. atelier `ci.yml` dropped `--warn`; child `floor.yml` gained a blocking
  spellscan step + selftest with the same re-baseline note.

Both flips follow datescan's 0707 pattern (atelier blocks now; children adopt +
re-baseline at their next pin bump). Suite 601 green; atelier floor green at head.

## Enforcement propagation — the estate rollout (ADR 0008, done 2026-07-25)

Closed the propagation gap end to end: 13 of 13 children moved off vendored
floor copies onto a called floor. `floorfleet --remote --check` exits 0.

- ✅ [1460-wire-the-13-children](1460-wire-the-13-children.md)
- ✅ [1470-repo-specific-scoping-preserved](1470-repo-specific-scoping-preserved.md)

## Licence gate enabled estate-wide (Mike ruled 2026-07-25)

Publish-readiness, not tidiness — Mike's correction of an earlier deferral.

- ✅ [1480-10-repos-declare-apache-2-0-and-pass-the-gate](1480-10-repos-declare-apache-2-0-and-pass-the-gate.md)
- ✅ [1490-3-proprietary-repos-disabled-with-the-reason-r](1490-3-proprietary-repos-disabled-with-the-reason-r.md)

## Scanner sharp edge — `--staged` + an absolute path covered nothing (done 2026-07-25)

- ✅ [1500-secretscan-leakscan-now-refuse-an-absolute-pos](1500-secretscan-leakscan-now-refuse-an-absolute-pos.md)

## Queue run 0702 — ccrepo v3 asks 1+3, cctranscript agent count (moved 2026-07-26)

Orchestrated queue run under Mike's standing brief. Records owned by the
orchestrator; workers committed in isolated worktrees and touched no record file.

### instruments — cctranscript reports agents *finished* beside agents *started*

- ✅ [1510-exact-agent-count-built-2026-07-26](1510-exact-agent-count-built-2026-07-26.md)

### instruments — ccrepo v3 asks 1 and 3 (`7cf8163`, merged `70bc1ad`)

- ✅ [1520-1-time-bound-the-price-table-a-price-is-effect](1520-1-time-bound-the-price-table-a-price-is-effect.md)
- ✅ [1530-3-g-session](1530-3-g-session.md)

## ccarchive encryption at rest — design pass (moved 2026-07-26)

Delivered `d913698`, merged `7701a62`; the design document itself lives at
[`instruments/ccarchive.encryption.design.md`](../../../instruments/ccarchive.encryption.design.md).
**The build is NOT done** — one decision stays open with Mike and is tracked live
in [`ROADMAP.md`](../../ROADMAP.md); this is the design pass's completed detail only.

- ✅ [1540-ccarchive-encryption-at-rest-secure-by-default](1540-ccarchive-encryption-at-rest-secure-by-default.md)

### floorfleet reads the tracked shim — the hook question, half-answered estate-wide (2026-07-26)

- ✅ [1550-floorfleet-remote-now-checks-the-tracked-shim](1550-floorfleet-remote-now-checks-the-tracked-shim.md)

### ccrepo v3 ask 2 — filter by context size (moved 2026-07-26)

- ✅ [1560-context-min-max-open-ended-either-end-k-m-suff](1560-context-min-max-open-ended-either-end-k-m-suff.md)

### ccrepo v3 asks 4 + 5 — multi-key sort, `--top`, sectioned help (moved 2026-07-26)

- ✅ [1570-4-multi-key-sort-within-a-level-plus-top](1570-4-multi-key-sort-within-a-level-plus-top.md)
- ✅ [1580-5-sectioned-help](1580-5-sectioned-help.md)

### linkscan names the fix when the path is computable (moved 2026-07-26)

- ✅ [1590-linkscan-prints-the-replacement-path](1590-linkscan-prints-the-replacement-path.md)

## Policy-as-code programme — A5a: the parent was not running its own floor (done 2026-07-27)

- ✅ [1600-core-hookspath-was-unset-in-the-atelier-clone](1600-core-hookspath-was-unset-in-the-atelier-clone.md)

## Policy-as-code programme — Track A: the fail-opens closed (done 2026-07-27)

Landed in worktree `track-a-fail-opens`, four commits, session record
[`2026-07-27-2301-track-a-fail-opens`](../../sessions/2026-07-27-2301-track-a-fail-opens.md).
Findings were counsel from the 2026-07-26 rule-4 Fable passes; the rulings were
Mike's (REVIEW rule 3). Tests 694 → 720, green in **both** environments (with a
machine term list, and with none). Every fix was driven live against the probe
that proved the defect, not asserted from the diff.

**The rulings, and the two measurements that decided them.** Both 🎯 items were
walked through in plain language first, and in both cases the roadmap's own
statement of the cost was wrong in the direction that made the strong fix
affordable.

- **A1/EP1** — the roadmap warned of "an immediate blast radius". Measured: of
  19 repos, **2** declare `scope`/`flags` and **all four declared paths
  resolve**; of 14 with a floor config, **0** lack their records tree. The
  structural reason it is safe: every no-advisory-form scanner defaults to the
  repo **root**, which always resolves, so the skip branch reaches a boundary
  check only through an *explicit* declaration — and the three docs-scoped
  scanners that need the skip are all advisory-capable. The cases do not
  overlap. **Zero children red.** Ruled **(a)+(c)**; (b), the stated-reason
  requirement, deferred to ride with C1's schema change rather than be decided
  twice.
- **A2/EP3** — the roadmap said requiring terms "fails closed on … every CI
  runner by design". Not for a hook-plane change: both workflows invoke
  `--plane ci` and the hook template is never invoked by CI; no test ran a real
  hook-plane `leakscan`. Ruled **(c)** — Mike asked why (a) was recommended
  over (c), was told that (a) makes the degraded-render path unreachable on the
  hook plane, and ruled (c) anyway for **measurement over inference**.

- ✅ [1610-a1-a-scope-path-resolving-to-nothing-silently](1610-a1-a-scope-path-resolving-to-nothing-silently.md)
- ✅ [1620-a2-the-hook-plane-s-leakscan-cover-was-asserte](1620-a2-the-hook-plane-s-leakscan-cover-was-asserte.md)
- ✅ [1630-a3-floor-py-asserted-cover-it-lacked](1630-a3-floor-py-asserted-cover-it-lacked.md)
- ✅ [1640-a4-ls1-ls5-the-repo-local-seam-s-edges](1640-a4-ls1-ls5-the-repo-local-seam-s-edges.md)
- ✅ [1650-a5b-floorfleet-has-a-parent-row](1650-a5b-floorfleet-has-a-parent-row.md)

**Two things the work surfaced that were not in the brief**, both fixed here:

- **A contract test asserted the opposite of the ruling.** The registry test
  banned `--require-terms` on **both** planes, reading the two planes as one —
  right for CI, wrong for the hook, where it forbade the flag on the plane the
  design says carries the full cover. Narrowed to CI with its complement added,
  not deleted.
- **Three pre-commit tests were passing *because* the hook was degraded**, and
  were env-gated in the misleading direction: green on a laptop holding
  `~/.claude/leakscan-terms.txt`, red on every CI runner. They now pin a term
  list inside the fixture. Every suite run was done twice, and the LS1 test
  sets `GITHUB_ACTIONS` explicitly rather than inheriting it, because
  annotation mode is env-gated and a test that merely runs the floor would pass
  by never entering the branch it means to exercise.

**Estate consequence, deliberate.** A new machine or fresh clone now blocks on
its first commit until `~/.claude/leakscan-terms.txt` exists. Documented as a
once-per-machine step in the child CONTRIBUTING template, which said only "two
lines" before, and worded so the block reads as intended rather than as broken
tooling.

### The application's own cold pass — TA1–TA9 (done 2026-07-28)

- ✅ [1660-reviewed-2026-07-28](1660-reviewed-2026-07-28.md)

**The MAJOR, and the third measurement that decided a ruling.** TA1: the A1
scope guard tested path *existence*, not membership, so a declared scope that
resolved somewhere else — `/etc`, `..`, or an in-tree symlink pointing out —
passed the guard, rendered on the hook plane to a prefix matching nothing in
the staged diff, and exited 0. A boundary check vacated under a green tick.
The same commit series had closed exactly this lexical-vs-resolved gap for
`local.run` (LS3) and left fleet `scope` with neither half, so the asymmetry
sat inside one diff — and the guard's own comment claimed the class was shut.

Measured before costing, and the pattern held a third time: 14 configs across
the estate, 2 declaring `scope`, 4 declared paths, **every one relative and
in-tree**. Zero migrations, so the thorough fix (validate at parse, both
spellings, plus resolved containment for the symlink member) cost no more than
the narrow one. The cheap-vs-thorough trade this programme keeps expecting has
now failed to materialise four times.

**Applied beyond the letter of the ruling, named as such.** `local.*.scope`
feeds the same `subtrees`/`_render` path as fleet `scope` and carried the
identical hazard. The ruling named only fleet `scope`, but guarding one
spelling of "where does this check look" while leaving its siblings open *is*
the finding, so the rule was applied to both.

**Fixed at the claim rather than the mechanism, also named.** TA4: the 🟡
partial-cover note was read off argv and asserted a cover *level*, which the
scanner's own output could contradict on a machine holding a term list. The
floor cannot observe real cover without capturing child output, and streaming
scanner prose live is worth more than closing a gap that errs toward claiming
*less*. The note now states the invocation, which is true in both
environments; the 🟡 stays because a real runner holds no list.

**The rest.** TA2 rode free (rejected at parse, so an absolute scope never
reaches the scanner that used to crash on it). TA3 gives partial scope drift on
a *softenable* check a 🟡 and a "N of M scope paths missing" note — it must not
block, but shrunken cover reported as full is what this whole track is about.
TA5: `PARENT_RUN_RE` matched inside comments, so a parent that commented out
its floor step read `wired` on the board built to catch exactly that; comments
are now stripped by a quote-aware lexer, with both over-corrections pinned.
TA6 moved a module-import side effect into `setUpModule`. TA7: the board could
not discover children when run from a worktree — the mode this repo's doctrine
prescribes for write-heavy work — because the default search root was the
worktree's parent; it now resolves the main checkout, the same way the parent
row's label already did. TA8 restored EP2's MAJOR grade in the intent record.
TA9 gave AWA2 a grammar for multi-commit landings: the landing commit is the
one that *completes* the series.

## Policy-as-code programme — Track C: C1, the advisory grows an end date (done 2026-07-28)

- ✅ [1670-c1-advisory-takes-a-reason-and-an-expiry](1670-c1-advisory-takes-a-reason-and-an-expiry.md)

**What changed.** `advisory` was a bare list of scanner names carrying neither a
reason nor a review date, so nothing distinguished "three days into adopting
this check" from "softened in March and forgotten". `disabled` — the harder and
more visible opt-out — had demanded a stated reason all along; the softer one
demanded nothing, which is backwards. It is now `{name: {why, review-by}}` with
both required and the date validated as a real ISO 8601 date at parse, which is
what lets the ageing comparison downstream be a plain string compare.

**Expiry is reporting pressure, never a block.** A passed `review-by` renders 🔴
on the floor and on the fleet board — with the number of days it has been
standing, because "expired" reads identically on day one and day two hundred —
and exits 0. A commit failing because of a date somebody set months earlier is
how a forcing function turns into a `--no-verify` habit.

**The transition was the real design decision.** Children fetch `atelier@main`
at CI run time, so a hard error on the old spelling would have broken all ten
children's CI the afternoon it landed. The bare list still parses, marks itself
`legacy`, and renders 🟡 on every run and every board row. That debt is tracked
at C1b, not left implicit: a transition spelling still parsing in a month would
be C1's own decay one level up, which would be a fine joke and a real defect.

**A1(b).** Narrowing a check that may never be softened now states why — `scope`
gains a `{paths, why}` form, with the `why` required only for the five
boundary/integrity scanners, since narrowing a prose check is an ordinary
layout fact. No `review-by`: a narrowed scope is a permanent structural fact
about a repo, not dated debt waiting to be cleared. Estate reach: one
declaration.

**The measurement, and a pattern worth naming.** The roadmap said 11 advisory
declarations across 8 children; the sweep found **17 across 10**. That is the
fourth blast-radius figure this programme has stated wrongly — and the first
that *understated* the work, where the previous three all made a strong fix look
more expensive than it was. The lesson is not "the roadmap is optimistic", it is
that its numbers are not an input a ruling can rest on, in either direction, and
that re-measuring costs minutes.

## Boundary findings — the tracked data export (done 2026-07-28)

- ✅ [1680-high-entropy-hits-in-a-tracked-data-export](1680-high-entropy-hits-in-a-tracked-data-export.md)

### The Track A cycle's terminal pass — TAA1–TAA4 (done 2026-07-28)

- ✅ [1690-reviewed-2026-07-28](1690-reviewed-2026-07-28.md)

Every live claim in the TA application re-ran true: both TA1 red legs
(`/etc` scope and the escaping symlink — rc 0 at `3fb6437`, rc 1 at HEAD),
TA5's wired→absent flip on a commented-out workflow line, TA6's import
hygiene, TA7's board run from a real worktree (parent + 13 children), the
`321bbd3` blast radius exact to the row (14 configs / 2 scoping / 4 unique
paths / 0 failing), 733 green at `d80f9d8`, and 759 + 207 green at HEAD in
BOTH environments (machine term list present and absent). Push telemetry
confirmed the TA9 grammar was met by its own series: the pointer left in
the same push as the completing commits.

The one substantive finding (TAA1) is an honesty lapse in a comment, not in
behaviour: the scope guard's class-members comment entered the series as an
overclaim ("the rest of that class"), was corrected to an underclaim
mid-series, and landed still claiming "(open)" two members that `321bbd3`
had shut — with the out-of-delta C1 commit later appending a correcting
tail while leaving the "(open)" labels. Same comment, three states, none
true at its landing.

### C1 phase 1's cold pass — C1F1–C1F3 (done 2026-07-28)

- ✅ [1700-reviewed-2026-07-28](1700-reviewed-2026-07-28.md)

Every claim re-ran true before the intent record was opened: eight parse
edges refused by message with rc 1 and zero tracebacks; the three render
states live (expired 🔴 with rc 0 — red, never blocking, as ruled); all
four A1(b) edges as ruled; the estate measurement exact (17 advisory
declarations across 10 children, and exactly 17 🟡 unmigrated rows on the
live board); 747 green at `549930b`; the pointer pushed with its landing
commit. The one substantive finding (C1F1) is a render displacement: the
new advisory `why` occupies the note slot the TA3 drift warning uses, so a
softened check with a half-resolving scope shows its reason but not its
shrink outside `--json`.

### The estate-root widening's cold pass — ER1–ER4 (done 2026-07-28)

- ✅ [1710-reviewed-2026-07-28](1710-reviewed-2026-07-28.md)

The paragraph's evidence re-ran clean: the 63-across-19 sweep reproduces
exactly at word boundaries (a naive substring sweep returns 471 — matching
inside ordinary words — which vindicates the *shape* of C5's cry-wolf
concern while confirming the measured zero-ordinary-word claim), the
forward-only rule has held since landing with zero new mentions, and the
text withholds the name it says it withholds. The minor (ER1) is the
widening's own lesson one transition further: the rule is silent at the
private→public flip, the moment a scrub still buys everything back.

### The secretscan fragment-match fix's cold pass — SF1–SF4 (done 2026-07-28)

- ✅ [1720-reviewed-2026-07-28](1720-reviewed-2026-07-28.md)

All four red legs reproduced on synthetic fixtures against the pre-fix
scanner; the three introduced-FP fixes hold with no new false positives
from the boundary change; the estate re-scan matches the claim (the one
moved figure is the ruled untrack of the data export); every committed
test value verified synthetic. The minor (SF1) is live-proven: the
kebab-slug exemption un-flags hyphenated diceware-style passphrases the
old scanner caught — the snake-case twin was already exempt, so the fix
completed a pre-existing hole's spelling rather than opening a class, but
the cost went unnamed. The pass also corrected two figures at reconcile:
the lowercase-hex gap is half its stated size (letter-leading only), and
the "entropy net catches ≥32 chars" aside holds only for mixed-class
values.

## Policy-as-code programme — Track B: the board learned to say "and passing" (done 2026-07-28)

### B2 + B3 — conformance and compliance, held apart (done 2026-07-28)

- ✅ [1730-floorfleet-proves-a-repo-calls-the-floor-never](1730-floorfleet-proves-a-repo-calls-the-floor-never.md)
- ✅ [1740-a-blind-spot-worth-closing-cheaply](1740-a-blind-spot-worth-closing-cheaply.md)

**The first live run is the whole argument for the item.** `--remote --status`
against the estate: all 13 children reported `wired ✅` — and **5 of 14 repos
had been RED on their default branch since the 2026-07-25 rollout**, three days
unnoticed, every one of them showing as fully conformant on the old board. The
roadmap entry predicted this exactly ("the board can read 'all 13 ✓' while
several repos are failing every run"); it was not a hypothetical.

**The proposed shape for B3 was costlier than it needed to be, and that is
worth keeping.** The entry suggested one `actions/permissions` call per child.
That endpoint requires GitHub's **Administration** permission — the
repo-*settings* permission — so adopting it as a requirement would have widened
the scheduled check's token across the entire private estate to learn one
boolean. Instead the switch is read authoritatively **when the token happens to
carry that permission** and inferred from run history when it does not: a floor
that has never run once is the same practical absence whatever caused it. The
board then **declares which authority answered**, because a board that cannot
say how well it knows something is the same failure as one that reports green
on nothing. Permission requirements were read from GitHub's published
fine-grained-PAT reference rather than assumed.

**Design notes worth carrying.** `classify_run` is pure and the selftest drives
every branch offline, mirroring the split `classify` already used — the I/O
sits in `read_run`. `--check` without `--status` keeps its exact previous
meaning (conformance alone), so nothing standing on the old exit code moved;
`--status` widens it to require green. `behind` was added beyond the item's
ask: a SUCCESS conclusion against a commit that is no longer the branch head
says PASSING about code that was never scanned, which is the same
confidently-wrong family one step subtler. The parent row gained a `workflow`
field because atelier runs the floor from its own `ci.yml` rather than the
caller filename its children use, so its run history was otherwise
unaddressable. 12 new tests; suite 759 → 771, all green.

### B1 — the conformance check runs on a schedule (done 2026-07-28)

- ✅ [1750-b-scheduled-workflow-in-a-private-repo](1750-b-scheduled-workflow-in-a-private-repo.md)

**The four options as they stood, preserved verbatim** — the decision is only
legible beside what it was chosen over:

- ✅ [1760-a-pat-in-atelier-s-ci](1760-a-pat-in-atelier-s-ci.md)
- ✅ [1770-b-scheduled-workflow-in-a-private-repo](1770-b-scheduled-workflow-in-a-private-repo.md)
- ✅ [1780-c-scheduled-local-run-cron-launchd](1780-c-scheduled-local-run-cron-launchd.md)
- ✅ [1790-d-add-it-to-the-session-close-ritual](1790-d-add-it-to-the-session-close-ritual.md)

**The item's costing was wrong, and the reason generalises.** B1 read "the work
is small: the schedule, `--check` wiring, and a failure message", on the premise
that `floorfleet --remote` was remote end-to-end. It was not. `--remote` read
each repo's CONTENT from GitHub and still DISCOVERED children by walking the
directories beside the atelier checkout — so on a GitHub runner it would have
found no children and exited 2. Fail-safe, but not a check. Stated at the right
altitude: **the estate this board could see was the estate that happened to be
cloned on one laptop.** That is the same class as every other finding in this
programme, one level further out than any of them.

`--from-github <owner>` was therefore the real work. It also closes the blind
spot the tool documented about itself — a repo that exists and was never cloned
here was not reported as a red, it was not reported at all — and it lists repos
in the account carrying no atelier pin as *unenrolled*, so a repo that never
adopted the floor is a visible choice rather than silence. Swept on landing: 6
unenrolled, of which 3 are public (exactly the three already named in the
roadmap, so that figure was right) and 3 private and untouched since 2016.

**Two bugs found in the building, both the same family as the programme's
organising finding — a check that runs and covers nothing:**

- `users/{owner}/repos` returns PUBLIC repos only: 4 of 20 here. A tool whose
  whole claim is enumeration would have enumerated a quarter of the estate and
  reported clean. Both listings are now unioned and paginated.
- `_gh_json` accepted a `--jq` projection, and `--jq .sha` prints a BARE string
  which is not valid JSON. The parse failed, the caller read `None` as "head
  unknown", and the `behind` check was **inert on its first live run without
  ever erroring**. The helper now takes no `--jq`. The unit test had agreed with
  the defect, because its fixture returned the bare sha the buggy call appeared
  to produce — a fixture that models the wrong contract proves the wrong thing,
  and that is noted at the fixture rather than silently corrected.

**The token, and what was deliberately not asked for.** `FLOORFLEET_TOKEN`:
fine-grained, read-only, expiring, **Metadata + Contents + Actions** read.
`Administration: read` was declined — it would let the board read the repo-level
Actions switch directly, but it is the repo-*settings* permission and would have
widened the token across the whole private estate to learn one boolean, when run
history answers the same question. Minting stays Mike's (always-confirm floor
action); the agent wires around a secret and never creates one.

**It asserts the full claim and will be red before it is green.** Five children
were red on their default branches for three days when this landed. Narrowing
the gate to conformance alone would make the board green by not asking the
second question, which is precisely the failure the job exists to catch.

### B1 — the token, and the proof it works (done 2026-07-28)

- ✅ [1800-floorfleet-token-minted-and-the-scheduled-job](1800-floorfleet-token-minted-and-the-scheduled-job.md)

**Why "all repositories" rather than the 13 named children — this is the part
worth keeping.** A token scoped to a named list cannot see repo 14. A new child
would not appear in the account listing at all, so the board would report it as
*nothing* rather than as a red — which is precisely the under-enumeration
failure the whole instrument exists to prevent, reintroduced through its
credential. Read-only `contents` + `actions` on the owner's own account is a
modest surface; a list-scoped token would have quietly defeated the tool.

**The proof.** A `workflow_dispatch` run on 2026-07-28 exercised the whole path
on a GitHub runner with **no local clones of anything**: 13 children plus the
parent enumerated from GitHub, every repo's latest floor run read, the six
unenrolled repos listed, and **exit 1 on the five red floors** — failing for the
right reason rather than on a configuration fault, which is the only distinction
that makes a red board worth having.

🔎 **The degraded-authority path was proven in production, not merely
unit-tested.** The board printed *"Actions-off was INFERRED (not read) for 14
repo(s)"*. The token deliberately carries no `Administration: read`, so the
repo-level Actions switch is unreadable, and the check fell back to run history
**and declared that it had done so**. Declining the wider permission was argued
on the grounds that the same question is answerable more cheaply; that argument
is now a demonstrated fact rather than a design claim.

One expected non-finding on the board, called out in the workflow's own comments
before it was ever run: `❌ personal-data term list: absent`. That list is
machine-local by design — it lives outside every repo — so a runner never has
one. It gates the HOOK plane on a developer's machine and does not gate this
job, and the board says so rather than leaving a reader to infer it.

### The two application passes — PA1–PA4, PSA1–PSA2 (done 2026-08-03)

The 2026-08-02 rulings application earned two rule-4 cold passes; both ran
2026-08-03 by a Mike-spawned Fable taker and both cycles closed terminal
(no MAJOR). Mike ruled all six residue findings the same day, each as
counselled, and the application landed within the hour.

- **PA1 [fixed]** — the PB3 rebase notice corrupted `--json` output under a
  subdir `--root` (reproduced: `json.load` raised on the prose-then-document
  stdout). The notice now prints to stderr and the JSON carries
  `rebased_to` — always present, `null` when `--root` was already the top,
  so the field set stays comparable run to run. The breaking probe is now a
  test.
- **PA2 [no change, decided]** — depth matching reds `config/.env.example`
  anywhere, and that shape is conventionally a deliberately-tracked
  template. Ruled leave-the-pattern: a name-shape carve-out is a permanent
  blind spot in a security scanner (SF1's lesson — real values get pasted
  into templates), and the reasoned ignore line is the designed,
  reviewable answer. If FP reports accumulate, Track E weighs them with
  data.
- **PA3 [fixed]** — a `#` glued to a glob silently truncated the exemption
  to a *different path* than written. Ruled fix-at-next-parser-touch, and
  the PA1 commit *was* the next touch, so it was discharged there: a
  no-space `#` is a loud config error (exit 2), tested.
- **PA4 [folded]** — publishscan's config-authored strings (globs echoed in
  errors, finding paths in output) print raw to terminals — C1F3's class.
  Named into C1F3's fix scope so one strip-at-parse change closes the class
  everywhere; no separate work item.
- **PSA1 [fixed]** — TOOLBOX's residual clause said "template", singular;
  two templates publish, and the local one discloses the `acceptEdits`
  default mode. The clause now names both and the mode bit. Ruled
  fix-at-next-TOOLBOX-touch; the records commit was that touch.
- **PSA2 [accepted]** — PS1's corrected standardise instruction reaches
  children at their next pin bump, with each child's own `publishscan` as
  the interim guard. That is the designed propagation model; the finding's
  value was making the dependency explicit, and it is now written in the
  verdict and here.

Verdicts:
[publishscan application](../../reviews/2026-08-03-0649-publishscan-application-cold.md) ·
[publish-surface application](../../reviews/2026-08-03-0653-publish-surface-application-cold.md).

## Doctrine — the harvest rides the `[x]` commit, enacted (done 2026-08-03)

Found 2026-07-26, enacted 2026-08-03 by the orchestrated run's inline claim —
which closed in the commit that landed the work, per the clause it was landing.
The preamble's checkbox-states paragraph gained two sentences: an `[x]` and its
harvest to this file are one commit, never two; and an inline claim (`wt: none`)
closes in the commit that lands its work. Rule-4 `⏳` queued in the same commit
(ROADMAP § Doctrine — review-owed). Entry preserved verbatim below.

- ✅ [1810-state-at-the-point-of-use-that-marking-91-x-93](1810-state-at-the-point-of-use-that-marking-91-x-93.md)

## Estate-root widening pass residue — ER1–ER4 applied (done 2026-08-03)

Ruled 2026-07-28 (Mike, plain-language walk-through with per-option impacts);
cycle already CLOSED
([verdict](../../reviews/2026-07-28-1216-estate-root-widening-cold.md), 0 MAJOR /
1 minor / 3 notes, every count re-swept independently). Applied 2026-08-03 by
the orchestrated run as the terminal application of a closed cycle — no pointer
queued.

- ✅ [1820-er1](1820-er1.md)
- ✅ [1830-er2](1830-er2.md)
- ✅ [1840-er3](1840-er3.md)
- ✅ [1850-er4](1850-er4.md)

## Third-seat executor trial — runs 1–4, promotion landed (done 2026-08-03)

The trial Mike opened 2026-07-23 (`dadde1d`): dispatch routine, well-floored
items to the mid tier, keep the step-down only on the floor's evidence, record
the outcome either way. Four runs, nine dispatched items, one failure; the
promotion the data supported landed 2026-08-03 in `ECONOMICS.md` § *The
orchestrated-run tier split* (mid tier as standing executor for well-floored
known-pattern builds + prescriptively-reviewed fixes; discriminator floor
density, not nominal class; rule-4 `⏳` queued at landing). Run outcomes
preserved verbatim below. (Moved from ROADMAP.md 2026-08-03.)

  - **Run 1 outcome — 2026-07-23 (Opus-orchestrated queue run):** two items
    dispatched to Sonnet — the **cc-tools vocab audit** (`85b17dd`: clean
    single-file delivery, zero-drift finding correct on my review, 160/160 node
    tests, recommendation correctly *held as a recommendation* not baked) and
    the **S3 datescan build** (`6077972`: `tools/datescan.py` + 41 tests, suite
    372 green, advisory wiring correct, honest baseline reported, exemption
    limits documented honestly). **Both PASSED the orchestrator review with no
    hand-up and no rework** — first positive data point that Sonnet genuinely
    does the routine-docs and first-of-kind-scanner classes under the floor.
    **One run ≠ a standing tier claim** (extracted-from-practice wants
    corroboration): leave the trial open for a second run's data before
    promoting Sonnet to the standing executor seat for these classes. Note for
    contrast: the doctrine-text apex sweep + the correctness-sensitive ccrepo
    ledger were kept on **Opus** this run (doctrine-text + silent-failure class
    → capable tier, per ECONOMICS QR5) — the split behaved exactly as the tier
    rule predicts.
  - **Run 2 outcome — 2026-07-23 (0618 Opus-orchestrated queue run):** two more
    Sonnet items — the **S1 wrapscan** and **S5 spellscan** first-of-kind scanner
    builds (`72e8ecb`/`760260473`, advisory-only, 40+60 tests, suite 472). **Both
    PASSED** the orchestrator review no-rework, each surfacing an honest judgement
    call left to its ⏳ review. (Recorded in the 0618 session entry as "run 2" but
    not folded into this trial record until the 0707 run — reconciled here.)
  - **Run 3 outcome — 2026-07-23 (0707 Opus-orchestrated queue run):** one item
    to Sonnet — **applying the datescan DSR1–DSR8 review findings + re-baseline**
    (`b7b292c`). This is a *step up* from run 1's classes: not a fresh build or a
    docs audit but **modifying scanner detection logic** (a silent-failure class,
    the kind ECONOMICS QR5 nominally routes to the capable tier). It was
    dispatched to Sonnet because it was **exceptionally well-floored** — 41
    existing tests + selftest + a cold review naming exactly what to change — and
    the orchestrator (Opus) re-verified the suite and read the risk-bearing DSR3
    logic + header before merge. **PASSED with no rework**: all eight findings
    applied, baseline 60→0, and Sonnet independently **caught three further real
    bugs** the review hadn't named, declared the DSR3 silent-miss trade honestly
    in-header, and correctly *declined to guess* an un-derivable date (left an
    honest `allow`). **Reading:** the discriminator that worked was the *floor
    density*, not the nominal class — a well-floored silent-failure task with a
    prescriptive review is safely Sonnet-with-Opus-verify; a *thinly*-floored one
    still isn't. **Three runs now agree** (five Sonnet items, zero rework): the
    docs-audit, fresh-scanner-build, and prescriptively-reviewed-fix classes all
    clear the floor. This is now enough corroboration to **write Sonnet into
    ECONOMICS as the standing executor** for those classes — a small doctrine edit
    (self-authored ⇒ rule-4 ⏳ at landing) that a future session should take; the
    one guardrail the data supports is *floor density, not nominal class*, so the
    doctrine line must say "well-floored + prescriptively-reviewed", not "any
    routine work". The two first-of-kind *reviews* this run stayed on **Opus**
    (gate-flip judgement → capable tier) — split held as predicted.
  - **Run 4 outcome — 2026-07-23 (0959 Opus-orchestrated queue run) — NOT a
    clean sweep, and the exception is the useful data.** Four Sonnet items: the
    two review-applies (wrapscan, spellscan — prescriptively-reviewed-fix) and
    the **pathscan (S2)** build (fresh build of a *known* pattern — reused
    linkscan-shaped path resolution) all **PASSED no-rework**. The fourth,
    **stampscan (S4)**, did **not**: a genuinely-new mechanism (marker parsing)
    whose failure mode — parsing its own documentation as real markers and
    exit-2-blocking the floor — its fixtures couldn't anticipate. The defect
    surfaced **at head** and needed an orchestrator correction (unwire). This
    *confirms* the tier split's safety logic (catchable failure caught by
    floor + Opus review, precisely where the split says to pay for capability)
    and **sharpens the promotion line**: the discriminator is **floor density,
    not nominal class** — a fresh build of a *known* pattern is Sonnet-safe, a
    fresh build of a *novel mechanism* keeps Opus-verify-at-merge earning its
    keep (its floor is necessarily thin — fixtures can't cover an unknown
    failure mode). So the standing-executor doctrine line (still owed, future
    session) should read "well-floored builds of *known* patterns +
    prescriptively-reviewed fixes", and must **not** generalise to "any
    first-of-kind build". Four runs of data now; the promotion edit stays a
    future session's rule-4 doctrine act.

## secretscan residue + E6c — low variety is not innocence (done 2026-08-03)

SF1+SF2+SF3 ruled 2026-07-28 (Mike, walk-through with a live six-shape probe;
cycle already CLOSED, verdict
[secretscan fragment cold](../../reviews/2026-07-28-1220-secretscan-fragment-cold.md)),
then superseded in shape by E6c's general rule — in credential-key context,
low character variety is not evidence of innocence — and built to E6c by the
2026-08-03 orchestrated run in one secretscan change. Whole-shape carve-outs
now decide before every variety-reading gate on the assigned path (32+
unbroken alphanumeric runs, both hex leading forms, uppercase, base32; and
four-plus separator-joined word passphrases, both spellings); the ruled probe
went 2/6 → 6/6; placeholder/indirection/path suppression keeps precedence;
the blocking set only widened. SF3's canary suite: 16 shapes across the five
ruled families plus vendor formats, count pinned, contract stated at the top
of the test file. The triage record's ≥32-entropy aside carries its dated
correction at source, and the SF verdict's own quoted specimen carries a
reasoned allow-marker (the new rule flagging it is the finding fixed). Suite
830 → 846 green; selftest extended with both ruled shapes. Entry preserved
verbatim below. (Moved from ROADMAP.md 2026-08-03.)

- ✅ [1860-secretscan-pass-residue-sf1-sf4-ruled-2026-07](1860-secretscan-pass-residue-sf1-sf4-ruled-2026-07.md)

## B2+B3 FS rulings applied — the board carries its authority (done 2026-08-03)

FS1–FS5 ruled 2026-07-29 (Mike, all accepted, FS1 both legs), applied
2026-08-03 by the orchestrated run: discovery authority printed beside the
answer (footer + `--json`, loud warning on an empty private-capable listing),
the three-outcome remote read (`unknown` rows red `--check`; only HTTP 404
means "not enrolled"), the token spec's all-repos grant stated on every
surface atelier carries, the wired-denominator headline, archived/unreadable
counts printed even at zero, and the `green("")` docstring + selftest legs.
One out-of-scope crash fix landed with it: a repo carrying no
`.atelier-floor.json` felled `render` (advisory initialised as a bare list
where every reader expects the C1 dict) — the board felled by the very
absence it exists to report; fixed with a test. Suite +22 (66 → 88 in
floorfleet's own file); live `--from-github` end-to-end run clean. The
application's rule-4 pointer is queued (the FS1 MAJOR keeps the cycle open).
Ruling entry preserved verbatim below. (Moved from ROADMAP.md 2026-08-03.)

- ✅ [1870-b2-b3-reviewed-2026-07-29-rule-4-fable-cold-pa](1870-b2-b3-reviewed-2026-07-29-rule-4-fable-cold-pa.md)

## TAA + C1F residues applied — the floor line tells the whole truth (done 2026-08-03)

Both ruled 2026-07-28 (Mike, plain-language walk-throughs), both cycles
already CLOSED
([TA application verdict](../../reviews/2026-07-28-1136-ta-application-cold.md) ·
[C1 advisory verdict](../../reviews/2026-07-28-1204-c1-advisory-cold.md)); applied
2026-08-03 by the orchestrated run as terminal applications — no pointers
queued. TAA1: the scope-guard comment re-labelled, all class members shut,
pinned by a source-text test. TAA2 + C1F1 unified as one note-joining design
(the `elif` is gone; `why`, drift and cover notes join on the line). C1F2:
`days_over` on the floor line, twinned with floorfleet's wording and pinned
equal by test. C1F3 + PA4: C0 controls stripped at both ruled parse seams
(floor's whole-document config ingest; publishscan's ignore-file and output
surfaces) — drop-don't-escape, with the interpolation-point encoding kept as
the layered inner guard and the LS1 security test rewritten to say so.
Residue found honestly at application: `floorfleet` parses child configs
through its own seam and remains an open surface of the class — recorded as
a live Track C item. Suite +23. Both ruling entries preserved verbatim below.
(Moved from ROADMAP.md 2026-08-03.)

- ✅ [1880-ta-application-pass-residue-taa1-taa3-ruled-20](1880-ta-application-pass-residue-taa1-taa3-ruled-20.md)
- ✅ [1890-c1-pass-residue-c1f1-c1f3-ruled-2026-07-28-mik](1890-c1-pass-residue-c1f1-c1f3-ruled-2026-07-28-mik.md)

## The ⏳ pointer grammar mechanised + B4 wired (done 2026-08-03)

The FUNDED build (Mike, 2026-07-28) and the B4 HV rulings (Mike, 2026-07-29),
landed as one build per HV2 by the 2026-08-03 orchestrated run — a session
that authored none of the breaches. `tools/pointerscan.py`: the grammar
detector (seeded questions + three reviewer-direction families, each traceable
to a real instance) and the cycle-state detector (an item asserting a review
is owed while carrying that review's verdict; state read from the item's own
text, not an item↔verdict key — the only mechanical keys were measured at a
near-total false-positive rate by the 2026-07-26 audit, the failure
`harvestscan` fingerprints content to avoid, and order is the discriminator:
a verdict link alone is lawful, review-has-run evidence *preceding* an owed
claim is not). Scope settled on evidence: marker glyph in bullet or state
prefix, OR a review-obligation phrase inside an emphasis run, `[x]` never a
pointer — emphasis-scoping measured against plain-prose scoping, which swept
in two innocent discussion items including the FUNDED entry itself. **Pass
type ruled a lawful fourth field** beside {delta, intent record, tier}: tier
is the same class of fact, both route the review, the ceiling forbids an
evaluative account, not routing; the FG6 boundary specimen passes clean.

**The corpus corrections, recorded so nothing inherits the old figures:**
instance 2 was LOCATED (the pathscan S2 first-of-kind pointer, live
2026-07-24 → 2026-07-27, carrying three seeded questions — matching the
finding's "two of three pointed away from the load-bearing problem"); the
"five stale residues" of `98cef9e` were **seven** (the sweep had looked only
in § Doctrine — review-owed; two were still live at HEAD and were fixed in
the landing merge: the ADR 0008 entry and the floor-local seam entry, both
now stating "reviewed — the ruling is what is owed"); the "three instances"
of grammar breach were **19 distinct defects** across 424 roadmap revisions
(14 commits, 3.3%, every spot-check a true positive). A third live finding
was P6's marker misuse (`⏳` where a decision was owed) — re-marked `🎯`.

**B4 wiring per the HV rulings:** `harvestscan` registry-wired, scoped to
net-bulk-delete commits (≥50 net lines off `ROADMAP.md` alone — gating on the
watched pair nets a harvest to zero, 1 in-scope commit instead of 6),
warn-only; shipped-config replay reproduces the cold pass exactly (6 in
scope, 3 warn, 15 items, the dd7fcb74 incident caught). HV2: the pointer
exclusion is pointerscan's test now (the old copy saw two of four pointer
shapes). HV3 as ruled was measurably inert (session records hold almost no
checkbox items) — the survivor search gained prose paragraphs in the harvest
destinations only, and the widening's effect was measured before landing
(107 → 85 firing commits across the ungated history). HV4: plane wording
fixed (--staged reads the INDEX). The replay harness ships as `--replay`.
Suite +42 across the build; both selftests green; all acceptance pairs
correct. Handed up, recorded as open work: a warn-only registry scanner
renders `✅ enforced` on the floor board (EP3's class — decide together).
The three source entries preserved verbatim below.
(Moved from ROADMAP.md 2026-08-03.)

- ✅ [1900-the-pointer-steered-its-own-reviewer-third-ins](1900-the-pointer-steered-its-own-reviewer-third-ins.md)

- ✅ [1910-funded-mike-2026-07-28-mechanise-the-pointer-g](1910-funded-mike-2026-07-28-mechanise-the-pointer-g.md)

- ✅ [1920-b4-reviewed-2026-07-29-rule-4-fable-cold-pass](1920-b4-reviewed-2026-07-29-rule-4-fable-cold-pass.md)


## The 2026-08-05 queue take — five cold passes, every cycle closed (done 2026-08-05)

The whole rule-4 queue of the 2026-08-03 orchestrated run taken by a
Mike-spawned Fable session (author sessions uninvolved), claimed on `main`
before the worktree per CONCURRENCY § Claiming work. All five passes returned
**0 MAJOR** and every open cycle closed terminal: pointer-grammar build + B4
wiring (both cycles), the FS application (B2+B3), the mid-tier
standing-executor doctrine, the E6 application (the intent cycle), and the
landing-equals-bookkeeping clauses. Findings held for Mike's ruling in the
ROADMAP § *Doctrine — review-owed* item of the same date; verdicts:
[pointer-grammar + B4](../../reviews/2026-08-05-1238-pointer-grammar-b4-wiring-cold.md) ·
[FS application](../../reviews/2026-08-05-1244-fs-application-cold.md) ·
[mid-tier executor](../../reviews/2026-08-05-1248-mid-tier-standing-executor-cold.md) ·
[E6 application](../../reviews/2026-08-05-1253-e6-application-cold.md) ·
[landing-equals-bookkeeping](../../reviews/2026-08-05-1258-landing-equals-bookkeeping-cold.md).
The five refs-only pointers this take discharges are preserved in the
verdicts' brief sections verbatim (each brief opens with its queue ref), so
the pointer text is not duplicated here.

**Addendum (same session): a sixth pass.** The `queue-batch-0806` landing
queued its own rule-4 pointer while this take was in flight; the same taker
claimed and ran it — the sitting's five doctrine edits, PASS 0 MAJOR,
cycle closed
([verdict](../../reviews/2026-08-05-1301-sitting-five-edits-cold.md)). Its pointer
is likewise preserved in the verdict's brief section. **A seventh followed**: the
F1/`GUARDS.md` + twelve-scanner allowances landing queued its pointer while
the sixth was closing; same taker, PASS-WITH-FINDINGS 0 MAJOR, F1's review
cycle closed
([verdict](../../reviews/2026-08-05-1320-f1-guards-allowances-cold.md)).
## The 2026-08-04 sitting's five small doctrine edits (done 2026-08-05)

All five ruled 2026-08-04 at the decision sitting; delivered 2026-08-05 in one
landing (wt: queue-batch-0806). What landed: the tier bar + stop clause at
`REVIEW.md` rule 4's spawn criterion and this repo's `⏳` legend; the
withdrawn-pass general case closing `REVIEW.md`'s lifecycle section; the
show-first bulk-deletion rule in `RECORD.md` with the `AUTONOMY.md`
cross-link; describe-don't-quote as a `RECORD.md` standing rule; the
session-onramp apex block re-taught to the Zeroth form, with the
restatement-sweep surface list written into `PRINCIPLES.md` §6 (plugin
surfaces included — the checklist-widening sweep found session-onramp the
only Laws restatement under `skills/` + `commands/`). Rule-4 `⏳` queued at
landing as one batch pointer (§ *Doctrine — review-owed*). Items verbatim:

- ✅ [1930-e5-write-down-describe-don-t-quote-as-a-standi](1930-e5-write-down-describe-don-t-quote-as-a-standi.md)
- ✅ [1940-zl1-major-the-surface-that-binds-the-apex-at-s](1940-zl1-major-the-surface-that-binds-the-apex-at-s.md)
- ✅ [1950-write-down-which-tier-reviews-the-rule-exists](1950-write-down-which-tier-reviews-the-rule-exists.md)
- ✅ [1960-promote-the-withdrawn-pass-convention-into-rev](1960-promote-the-withdrawn-pass-convention-into-rev.md)
- ✅ [1970-doctrine-candidate-bulk-deletion-from-a-record](1970-doctrine-candidate-bulk-deletion-from-a-record.md)

## C5 executed — the estate-root name has its forcing function (done 2026-08-05)

Executed 2026-08-05 (wt: queue-batch-0806): the composed ruling applied
to the machine-local term list — the bare literal term plus a
repo-reference-shapes pattern (owner/name, the local path form, a
name@sha form, the possessive) — and verified with a staged probe in a
scratch repo: the bare name and the owner/name shape both flag on
added lines; an ordinary-English word embedding the name passes
(word-boundary honoured). Forward-only by construction. The token-spec
item below closed the same day in the estate-root repo itself.
Item verbatim as closed:

- ✅ [1980-c5-a-forcing-function-for-the-estate-root-name](1980-c5-a-forcing-function-for-the-estate-root-name.md)

- ✅ [1990-the-scheduled-consumer-s-workflow-still-owes-i](1990-the-scheduled-consumer-s-workflow-still-owes-i.md)

## The licence gate learns proprietary — E1 + E2 (done 2026-08-05)

Both licence-gate items delivered 2026-08-05 (wt: queue-batch-0806),
built to the fix shapes and required tests the items themselves state.
E1: an unrecognised LICENSE body is read as a declared custom licence
(an explicit `LicenseRef-` id where the body names one, otherwise a
sentinel); the per-file SPDX-header checks keep running, and a vendored
strong-copyleft header under a custom licence blocks as the poison pill
it is. The allow marker now retires only the unrecognised-body warn,
never the header checks, and `--expect` compares the declared id too.
The item's reproduction fixture now reports the copyleft file (run
end-to-end at delivery). E2: sixteen unambiguous OSI trove classifiers
resolve to SPDX ids before the unknown-declaration check; ambiguous
family names deliberately stay on the warn. Module tests 37 → 52, full
suite green, live tree clean. Honest limits recorded in the module
docstring: under a custom licence only the copyleft judgement is made
(metadata declarations have no id to compare against; a permissive
foreign header goes unremarked), and a proprietary repo still exits 1
until its LICENSE carries an allow marker or an explicit `LicenseRef-`
id — deliberate friction, both remedies stated in the finding message.
The three children `disabled` on exactly this gap are now unblocked;
retiring those declarations is each child's own act at its next floor
touch, per the advisory/disabled ageing item. Items verbatim:

- ✅ [2000-licenscan-gap-support-proprietary-licenseref-l](2000-licenscan-gap-support-proprietary-licenseref-l.md)
- ✅ [2010-licenscan-gap-map-known-pypi-trove-classifiers](2010-licenscan-gap-map-known-pypi-trove-classifiers.md)

**CORRECTION, same day (2026-08-05, the executing session):** the execution
above was **REVERTED hours after it landed**, on measurement, and C5 returns
to the live roadmap as a decision owed. What execution surfaced that the
ruling's premises did not model: **(a)** forward-only held on the *hook*
plane only — a local **full-tree** leakscan run (the ci-plane floor
reviewers re-run as an obligation, and orchestrators run at verification)
went red with **86 term findings across the frozen records**, because this
repo's records legitimately reference the estate root and the term list
cannot tell a new line from a frozen one; three Fable cold passes were in
flight with that command in their briefs. **(b)** The zero-ordinary-English
measurement was falsified at HEAD — a tool docstring uses the word as plain
English (the 63-occurrence corpus predated it and was records-only), so the
cry-wolf premise the ruling retired is alive after all. **(c)** The
estate-root repo's own records carry ~364 self-references, and under E7's
D1 ruling (allow-markers never exempt the term list) a future self-naming
line there hard-blocks with no in-repo hatch. The term list is restored to
its pre-execution state, verified green on the full tree. The re-ruling —
with these facts on the table — is queued in Track C.

## D2 delivered — stampscan's three preconditions built, wired advisory (done 2026-08-05)

Ruled 2026-08-04 (fund the fixes over the counselled shelve); delivered
2026-08-05 (wt: queue-batch-0806) to the reviewer's bar, step 1. ST1:
the parser strips fenced blocks and inline-code spans before marker
recognition; stripped lines still enter payloads verbatim, so
comparison is untouched. ST7 taken as part of ST1's remediation: the
template's end marker moved to its own line, `template_block()` strips
marker lines, and the end-marker regex anchors to line start. ST2:
narrowing to nothing is drift however declared; a genuine partial
narrow still passes. ST4: `source=` confined to `--root`, escape is a
config error. ST5: the convention has doctrine words now —
`PROPAGATION.md` states what a stamp is, what `narrow=<reason>`
declares, and who may declare it; `tools/README.md` gains its section;
`.stampscanignore` ships the house net (measured at landing: the
parser fix alone clears the live tree, so the ignore file is the
standing net for the named residual, not a load-bearing patch). ST6
honesty fixes taken. Wired advisory in atelier's `ci.yml` only; the
live tree that exited 2 with five config errors now exits 0 both
scopes, and the one live stamped pair still reads identical at 52
lines. Module tests 46 → 65 (+1 in test_templates); full suite green.
ST3 stays open as the registry-wiring bar — the D2-residue item on the
live roadmap. Built by an Opus worker to the ruled counsel; verified
by the orchestrator. Item verbatim:

- ✅ [2020-d2-stampscan-fix-at-the-parser-or-shelve-it](2020-d2-stampscan-fix-at-the-parser-or-shelve-it.md)

## The 2026-08-06 queue take — three cold passes, every cycle closed (done 2026-08-06)

The remaining rule-4 queue — the three pointers the 2026-08-05 queue batch
landed — taken by a Mike-spawned Fable session (author sessions uninvolved),
claimed on `main` before the worktree per CONCURRENCY § Claiming work. All
three passes returned **0 MAJOR** and every open cycle closed terminal: the
licenscan E1+E2 build (first pass on that delta), the stampscan D2
application (closing the ST/S4 cycle its three MAJORs had held open), and
the pathscan D1 rescope application (closing the PS/S2 cycle likewise).
Findings held for Mike's ruling in the ROADMAP § *Doctrine — review-owed*
item of the same date; verdicts:
[licenscan E1+E2](../../reviews/2026-08-06-0903-licenscan-e1e2-cold.md) ·
[stampscan D2 application](../../reviews/2026-08-06-0938-stampscan-d2-application-cold.md) ·
[pathscan D1 application](../../reviews/2026-08-06-1002-pathscan-d1-application-cold.md).
Every live-proven claim in the three deltas re-ran clean, including the
measured "parser fix alone clears the tree" claim (re-run with the ignore
file bypassed) and the pathscan gateable-surface scan (clean, 10
suppressions, each reasoned). The three refs-only pointers this take
discharges are preserved in the verdicts' brief sections verbatim (each
brief opens with its delta and intent-record refs), so the pointer text is
not duplicated here — the precedent the 2026-08-05 take set, and the shape
the harvest-integrity gate exists to force.

**The ruling round and its application (same day, 2026-08-06).** Mike ruled
all fourteen residue findings in a plain-language AskUserQuestion
walk-through: eleven fixed, three accepted as recorded (LC5 multi-LICENSE
pick order · SD5 fence-closer asymmetry · PD3 the deliberate
pathscan/linkscan double-report). Applied the same session
(wt: ruled-fixes-0806), each fix probed both directions; decisions stamped
in the three verdicts. Highlights: licenscan's unknown-license suppression
now requires a reasoned marker and tallies the retirement (LC1/LC2 — its
last reasonless hatch); stampscan's region extraction reads the
code-stripped view so a fenced example can never shadow the real region
(SD1), prints a suppression tally whose first live run surfaced 98
silently-skipped files (SD3), and voids a whitespace-only `narrow=` (SD4);
`PROPAGATION.md`'s stamp paragraph rewritten to the current truth (SD2);
the five merge-stranded tests moved above the `__main__` blocks (LC3/PD1 —
true totals 56/75/76). **This also closed D2 residue (b)** — stampscan
joins the GUARDS allowance model; the tally was the only work owed, the
entry's loader half having already landed in the ten-loader sweep
(verified at HEAD, the board corrected). Item verbatim:

- **D2 residue (b) — stampscan joins the GUARDS allowance model.** The
  D2 build and the F1/allowances sweep landed the same day in
  parallel sessions, so stampscan — the eleventh scanner — missed
  the sweep that put the other ten onto the model: its ignore-file
  loader does not yet require a stated reason per glob, and it
  prints no suppression tally. Small alignment build; rides the
  next stampscan touch.

## The decisions index catches up — five ADRs listed (done 2026-08-06)

The `docs/decisions/README.md` index was missing the five records dated
2026-07-18 → 2026-07-23 (found 2026-08-05 while adding the P6 draft's entry;
the index is the only map of that directory). Fixed 2026-08-06 (wt:
decisions-index-0806): each missing ADR read in full and distilled to a
one-line entry in the established style; the two same-day 2026-07-21 records
disambiguated with their full `YYYY-MM-DD-HHMM` identifiers (no prior
precedent existed); the stale drift footnote removed in the same commit
because the fix falsified it. `linkscan` exit 0; full floor green at the
merge. The item's open question — should this index be generated rather than
hand-maintained, since drift is exactly the failure mode a hand-maintained
index has — was put to Mike at this session's close rather than left queued.

## E7 built — leakscan's funded PII fixes land (done 2026-08-06)

The 2026-08-03 sweep found leakscan materially behind the credential half;
Mike ruled every finding 2026-08-04 and the funded build landed 2026-08-06
(wt: e7-leakscan-build-0806, one commit, its rule-4 pointer queued at this
landing). **The ruling, verbatim from the item:** D1 fixed as (a) — applied
2026-08-05 — allow-markers exempt structural rules only, the term list
always runs; D2 fixed as (a) — the IPv6-shape rule requires `::` or
four-plus groups (settling E4 and the clock-times boundary entry, one fix,
three entries); D3–D6 all fixed (safe-set widening, address suffix guard,
MAC dedupe, exact all-zeroes match); G1, G2, G4, G6, G7 funded (the
key-context layer with placeholder suppression and its own canary suite;
path scanning; Luhn-checked cards + IBAN + the NZ hyphenated bank shape
with bare-digit forms staying key-context-only; term-list derived forms
documented with opt-in derivation; the bracketed phone form); G5 deferred —
revisit on first real miss; G3 ruled BLOCKING — an unscannable or
metadata-bearing binary blocks and a legitimate image carries a one-time
reasoned marker, keeping E6a's no-advisory-form decision intact.

**What the build delivered.** A third layer (`pii-key-context`) reads
labels rather than values — personal data has no entropy signature, so the
key name is the only available analogue of secretscan's context-free net —
guarded by a 27-shape canary suite with 13 pinned placeholder shapes as its
counterweight. All three layers now run over each file's repo-relative
PATH as well as its content (line 0, rendered "in the path name"; a
binary's name is read even though its body is not). Cards are Luhn-checked
with an issuer-digit guard, IBANs mod-97-validated, and a generic
`SHADOWED_BY` mechanism stops a MAC being re-reported as IPv6 — shadow
spans computed before allow-markers so an exempted MAC leaves no blind
spot, and a disabled shadower casts no shadow. `forms:` terms match
slug/snake/dotted/camel/run-together spellings, opt-in only. The IPv4 safe
set gained all 33 computed netmasks, the broadcast/unspecified addresses,
the loopback net and eight public resolvers — RFC 1918, CGNAT and
link-local still flag.

**Verification.** Suite 1060 → 1121 (leakscan 53 → 114), exit 0; tree
structural run exit 0; selftest exit 0; hook-plane floor exit 0; the
local full-cover plane's 3 pre-existing findings (the published-identity
lines, D1's recorded consequence) measured byte-identical before and
after. The sweep's probe block now flags end to end on `pii-key-context`.

**Honest limits, stated by the build.** Two G1 keys were tried and
withdrawn against measured false positives (`diagnosis` opens every
root-cause paragraph in the estate — 3 live FPs; bare `ird` matched prose
— now compound-only), reasons written into the code. Path scanning is
literal per the ruling: a hyphen-slugged address in a filename is not
caught (names-in-slugs are `forms:`' job; addresses-in-slugs are nobody's),
and a path has no inline marker hatch — `.leakscanignore` is the only
escape. The initials form of a name is outside G6 as ruled. The
RFC 3849 IPv6 documentation prefix flags — not ruled safe, left fail-safe
(and quoting it in this very entry turned the harvest commit red until the
line was reworded to describe it: the describe-don't-quote rule earning its
keep on the rule's own paperwork). Amex's 4-6-5 grouped spelling is
unmatched (the bare 15-digit form is caught); a Luhn-valid run with an
issuer digit outside 2–6 passes.
Derivation is line-based — a name split across lines matches nothing.
Four allow-markers in the tree are now dead weight (three loopback
markers D3 obsoleted, one clock-time marker D2 obsoleted) — left in place
deliberately: three sit in frozen records and instruments outside the
build's file scope; noted in the CHANGELOG for a separate deliberate edit.

## E6b built — secretscan's second response, and E3's carve-out (done 2026-08-06)

E6b (ruled 2026-07-28; consumer named by Mike 2026-08-04 as the build's
precondition) landed 2026-08-06 (wt: e6b-secretscan-advisory-0806, four
commits, rule-4 pointer queued at this landing). Every finding now carries
a `response` — `block` for the named vendor formats, `assigned-secret` and
the mixed-class entropy net, byte for byte as before and pinned by tests;
`advisory` for the new `low-variety-entropy` rule, which reports E6c's
already-ruled whole shape (an unbroken 32+ alphanumeric run) on the
context-free path EI4 named as the real narrowing site, and exits 0. No
new threshold was introduced anywhere — the length is E6c's, the
mixed-class split is the existing net's, only the response is new.

**The three consumer legs, all live-verified.** Hook: advisory findings
print at the commit that introduces them (observed in the build's own
pre-commit runs). CI: `--plane ci` scans at full-tree cover, so every push
re-prints all of them — no new step needed; the property is documented in
`ci.yml` and pinned by a test precisely because a future
`scope.secretscan` narrowing would end it without touching the workflow.
Board: `floor.py` reads the count off that run's output via a printed
contract line (the scanner prints its known zero; a missing line renders
as a 🔴 "count contract has drifted", never a silent 0 — silence and zero
must not look alike), pinned from both sides by a contract test that runs
the real scanner. **Interpretation flagged rather than buried:** the
ruling's "floor board" was read as `floor.py`'s per-repo board;
`floorfleet` (which reads wiring and run status, and runs no scanners) was
deliberately not given a count — put to Mike at this close.

**First live measurement: 21 advisory findings tree-wide, every one a
hash** — 12 SHA-pinned Actions digests, 2 test checksums, 7 fixtures.
Left unsuppressed deliberately: a board reading 🟡 21 is the ruling
working on day one, not a defect.

**E3, riding as ruled:** the public-key fingerprint shape is suppressed
whole-shape (both ruled spellings), canaried both directions — a
fingerprint-prefixed body of the wrong length is a credential wearing a
fingerprint's hat and still blocks — and counted in the tally, never
silent. The legacy colon-hex form produces nothing to suppress today
(colons are outside the entropy net's character class); it is recognised
and canaried anyway so a future widening cannot start flagging it without
someone deciding to.

**Stated limits and residue.** `PUBLIC_KEY_RX` still subtracts silently —
queued as its own small item. Docker image digests land in the advisory
tier (not ruled, so not suppressed). A non-alphanumeric token carrying
separators still passes both tiers, and the four-word passphrase shape
stays silent context-free — deliberate, the cry-wolf tax the tier exists
to avoid. `floor.py` now buffers this one scanner's sub-second output to
read the count. One test contract was narrowed on purpose and says so in
code: the old "no finding of any kind on a bare SHA" assertion encoded
block-as-the-only-response, exactly what E6b was ruled to change. Suite
1060 → 1103 on the branch; E6d untouched and not foreclosed (`response`
sits beside the mislabelled `severity` field, leaving E6d(iii) a clean
site).

## The EP application — the ADR 0008 ruled fixes land (done 2026-08-06)

EP1–EP10 were ruled 2026-08-04 (Mike, plain-language walk-through, all as
counselled; the sitting found the MAJORs' substance already closed by
Track A). The application landed 2026-08-06 (wt: ep-application-0806, five
commits, rule-4 pointer queued at the landing; the cycle's MAJORs keep it
open past this, so the application earns its own cold pass).

**What landed.** EP1(b): a `flags` declaration on a never-softened scanner
now requires a stated reason, mirroring the `scope` twin — which was found
**already landed 2026-07-28** (C1 phase 1's A1(b), commit `549930b`), so
the ruling entry's "verified absent at HEAD" was half wrong: the
cycle-state residue class, again, corrected from the tree. Probed nine
ways in a throwaway repo: reasonless blocks with the working form named,
reasoned passes, softenable scanners stay reason-free, and a mode-changing
flag smuggled through the reasoned form still blocks. EP4: a deliberate
pin is documented as two edits (`uses:@<sha>` and `atelier-ref`), and the
board's `pinned` detail now says the scanners still float unless both are
set. EP5: the registry-selftest loop reads `--root repo`, and the proving
story for `local` checks is DECIDED as skip-with-comment — the child's own
CI owns proving its check — applied consistently to atelier's own latent
inverse in `ci.yml`. EP6: ADR 0008 gains Decision 6, the repo-local seam,
dated and pointing at the seam doctrine in `tools/floor.py`. EP7: the
Consequences name the control that makes floating `@main` safe — atelier
`main`'s own protection — and state the compromise consequence at full
strength (arbitrary code in every child's CI). EP8: trigger shape joins
floorfleet's stated concession. EP9: the hook guards a missing `python3`
with a remedy that is not the bypass, both hook copies byte-identical,
driven by a real commit on a PATH without the interpreter. EP10: the
prove-it-landed block prints `core.hooksPath` first, closing the "clean
registry while every commit goes unscanned" gap.

**Blast radius, measured not estimated:** two declarations on unsoftenable
checks exist across the estate — one legacy-exempt, one already reasoned —
so zero repos go red at their next push. atelier's own config (softenable
scopes only) stays green.

**Deferral surfaced, not buried:** the new `flags` reason mirrors
`scope`'s C1 legacy exemption — a bare-list spelling cannot carry a
reason, so it parses. The ruled forcing function therefore arrives with C1
phase 2 (when the legacy spelling dies), not now. Consistency was chosen
over a split where one key of an old-spelling pair reds and the other
passes; put to Mike at this session's close in case he wants it to bite
sooner. Two conventions noted: ConfigError exits 1 (the file's one-class-
one-code convention; the twin `scope` rule ships the same), and `scope`'s
older error message does not name the working form while the new `flags`
one does — an asymmetry left for the application's own cold pass.

**Verification at the branch:** suite 1164 → 1178 exit 0; floor selftest
12/12; hook plane exit 0; ci plane exit 1 on the pre-existing
published-identity term findings, proven byte-identical to the fork via a
clean `git archive` re-run; floorfleet `--check` exit 0 with 15/15 wired
and the cover-reduction lines rendering; instruments untouched (207 node
tests pass, empty diff).

**History preserved with the item:** an Opus pass ran on this delta
2026-07-26 0647 UTC and was NOT ACCEPTED — cold review passes are Fable's
(Mike, 2026-07-26); the accepted Fable verdict is the review linked from
the item, and the withdrawn pass stays quarantined under
`docs/reviews/withdrawn/`, its findings dead.

## The floor-render batch — three states, PS5, and the C1F3 strip (done 2026-08-06)

Three floor-plumbing items, all ruled or queued, landed as one delta (wt:
floor-render-batch-0806, two commits, rule-4 pointer queued at the
landing).

**The third render state (ruled 2026-08-04).** A warn-only registry entry
— `harvestscan`, `pointerscan`, now `pathscan` — rendered the same
`✅ enforced` a blocking scanner earns while printing findings, the
"identical output for materially different cover" shape EP3 named. The
board now shows three states on every plane and in `--json`/`--list`:
`✅ enforced`, `advisory`, and `👁️ warn-only` ("reports findings, can
never block this build"). Warn-only is derived from the registry argv
itself (or a `warn_only` field for checks with no blocking form), never a
hand-maintained list, and the two statements of the fact are pinned to
each other both directions by selftest + suite — a future warn-first line
renders correctly with no second edit, and cannot be wired warn-first
while the board claims enforcement. Exit codes unchanged: `Result.failed`
includes warn-only, so an unreadable tree or config error still blocks —
the render fix does not quietly turn an environment error into a pass.
E6b's 🟡 advisory-count note (a blocking check that also reported) shares
no wording with 👁️ (a check that gates nothing, ever); a child declaring
a warn-only check `advisory` renders `advisory`, deliberately — the state
names what ran.

**PS5 — pathscan promoted (the D1 ruling's deferred half).** The bespoke
`ci.yml` step was the vendored-policy shape one level up: a check the
parent ran and no child had ever heard of. One registry line replaced it —
equivalence proved, not asserted (same 1 finding, same 10 suppressions;
0.18s on atelier's scope) — with atelier's scope moved to
`.atelier-floor.json` beside its wrapscan/spellscan twins, and a `docs`
default for children. Warn-only stays; the blocking flip is a separate
later ruling, now a one-argument change that reaches the whole estate.
The check's one live finding was fixed at the landing rather than left to
the flip: the 2026-07-19 index line this session's own decisions-index
worker wrote had dropped a path's `build/templates/` prefix, naming a
file that does not exist — the promoted check caught the session's own
work within hours of both landing.

**C1F3 — the floorfleet strip.** floorfleet read child
`.atelier-floor.json` files through its own parsers and printed
child-authored `why`/reason/description strings raw. Proved against the
fork as control: five ESC (including clear-screen and cursor-up), a BEL
and a NUL from one child's declarations reached the terminal; with the
strip, zero, and ordinary text — em dashes, macrons — byte-identical.
`floor._strip_controls` was made public and shared rather than twinned (a
second copy is the per-surface list the function exists instead of), and
a latent crash was fixed en route: an array-shaped child config took the
whole board down with an AttributeError instead of marking one row
unreadable. Two existing tests that looped asserting literal "enforced"
now read the expected state off the registry, so they keep asking their
real question. Residue queued, not buried: `classify`/`_live_yaml` and
the caller-`ref` detail line are further child-authored text surfaces the
ruled seam did not cover — same class, narrower surface, own small item.

**Verification at the branch:** suite 1178 → 1200 exit 0; floor selftest
13 scanners 0 failures; hook plane exit 0 with the three states
rendering; ci plane exit 1 byte-identical to the fork's pre-existing
term findings, pathscan absent from the blocked list; floorfleet
`--check` exit 0; floorfleet selftest exit 0.

## §9 ruled — retrofits bind, and a result carries its derivation (done 2026-08-09)

*Harvested from `ROADMAP.md` § PRINCIPLES §9 — the time dimension. The
estate consequence of the retrofit ruling stays live there; only the ruled
items moved.*

**Both open consequences RULED 2026-08-09 (Mike), and a third clause added.**

- ✅ [2030-scope-9-binds-retrofits-and-new-designs](2030-scope-9-binds-retrofits-and-new-designs.md)
- ✅ [2040-ownership-the-repo-that-owns-the-data-owns-the](2040-ownership-the-repo-that-owns-the-data-owns-the.md)
- ✅ [2050-a-stored-result-carries-its-derivation-not-onl](2050-a-stored-result-carries-its-derivation-not-onl.md)

## Estate duplication + exception audit (2026-08-09)

- ✅ [2060-two-ignore-globs-are-deferments-filed-as-accep](2060-two-ignore-globs-are-deferments-filed-as-accep.md)

## spellscan's reason class silently voided live allow-markers — fixed at the class (2026-08-09)

Harvested 2026-08-09: the item below was still `[ ]` on the hot path hours after
`8276a54` closed it, asserting "the class itself is unfixed and every child
inherits it" while the tree said otherwise. Third instance of the cycle-state
residue class since 2026-08-05, and the one where the stale claim was
*load-bearing* —
a reader would have concluded the estate still carried a silent false-negative
in every scanner. Verified before flipping, not taken on the commit message's
word: **14 regex sites across 12 scanners** now carry the widened class
(`[\w\"\'“‘]`), enumerated at HEAD — `datescan` and `pathscan` ×2 each (bare
mention-guard + named-group form), `stampscan` bare, and one apiece in
`leakscan`, `licenscan`, `linkscan`, `pointerscan`, `reviewscan`, `secretscan`,
`sizescan`, `spellscan`, `wrapscan`. The three scanners with no allow grammar
(`harvestscan`, `publishscan`, `signscan`) are correctly untouched. Suite 1210,
floor exit 0 at `6887118`.

Both of the item's own open threads are closed by the shape of the fix, which is
why nothing survives to re-queue:

- The 🤔 **open question** — widen to `\S` or narrower — was *answered by the
  fix*, narrowly: straight and typographic opening quotes are admitted and
  nothing else, so a documentation mention (`<!-- datescan:allow: -->`) still
  reads as a mention rather than a live exemption. That is the thing `\w` was
  protecting, and it is kept.
- The ⚠️ **sibling-scanner precondition** — "check the siblings before fixing
  one" — was discharged by fixing at the class rather than the instance. The
  item's own count of "ten loaders" was low: twelve carry the grammar.

- ✅ [2070-a-reason-that-opens-with-punctuation-does-not](2070-a-reason-that-opens-with-punctuation-does-not.md)

*What survives on the hot path, and deliberately: § Estate duplication +
exception audit's* **Make a voided allowance visible** *item. The fix above
closed the known cause; a marker that parses as nothing is still
indistinguishable from no marker, so the next parser gap will also be silent.
That is instance one of the class, queued not built (`PROPAGATION.md` rung 2).*

## The floor-local-seam cycle's verdict pointer, retired (2026-08-09)

Harvested 2026-08-09 alongside the entry above — the same cycle-state residue
class, and the fourth instance the board has produced. The bullet had **already
diagnosed itself** in place ("This item's 'await Mike's ruling' was stale from
that date: the second cycle-state residue this sitting found hiding in coarse
wording. Kept only as the verdict pointer; no work owed") and *still* sat on the
hot path as `[ ] 🎯` — so a reader scanning for Mike's outstanding rulings
counted a ruling that was made, applied and verified two weeks earlier. Naming
the residue is not clearing it; the `[x]` is.

Re-verified at HEAD `6887118` before flipping, all five LS fixes traced to live
code rather than to the claim: encoding at the interpolation point
(`read_text(encoding="utf-8")`), the OSError wrap, symlink-resolving containment
(`_inside` resolves both sides then compares with `commonpath`, with symlink
tests in *both* directions — escaping blocked, staying-inside still runs),
unknown-key refusal (`LOCAL_KEYS` + the parse-time rejection), and the
disabled-local `➕` marking in `floorfleet`. Both cited commits exist and say
what the item says they say.

- ✅ [2080-state-ruled-and-applied-ls1-ls5-landed-2026-07](2080-state-ruled-and-applied-ls1-ls5-landed-2026-07.md)

## secretscan's last invisible subtraction (done 2026-08-09)

Track E residue, and the last uncounted subtraction in the scanner.
`PUBLIC_KEY_RX` skips a line's entropy pass entirely — the deliberate carve-out
that stops an SSH public key reading as a credential — and it predated the GUARDS
counted-suppression model, so the lines it wrote off appeared in no tally.

**Whether the finding was even still true was the crux, and it was settled by
probe.** The clean line already ended `1 public-key fingerprint(s)`, which reads
like the same thing and is not: that counter is E3's whole-shape fingerprint
carve-out, incremented *inside* the entropy loop, while `PUBLIC_KEY_RX` skipped
the loop from outside it. Same 68-char body on two lines, one naming
`ssh-ed25519` and one not — the first went clean with every tally field at 0, the
second returned a blocking high-entropy finding. A blocking finding vanished and
no number moved: precisely the state GUARDS rule (b) exists to forbid.

**What it was hiding on the live tree: two real suppressions** — `allowed_signers`
and a line in `tools/signscan.py`, both genuine SSH allowed-signers public keys at
entropy 5.1. So "small alignment" understated it; the green tick had
under-reported its own subtractions since the carve-out landed.

The fix keeps the suppression byte-identical and changes only what is said about
it: the carve-out moved *inside* the span loop (same regex, same per-line scope,
same precedence ahead of the E3 check) so it can count each span before
continuing. `N by public-key line` is **appended** rather than inserted, and
prints at zero, because two runs of this board get read side by side. Tests
122 → 134, both directions plus the widest-suppression cases (a named assigned
credential on a public-key line still blocks; `private_key =` is not a public-key
line). Full suite 1210 → 1222, floor `conclusion=success` on the pushed run.

- ✅ [2090-public-key-rx-subtracts-silently](2090-public-key-rx-subtracts-silently.md)

## The parent states its own reasons (done 2026-08-09)

`GUARDS.md` rule (c) binds atelier identically to any child, and atelier's own
`scope` block had been narrowing three checks with no reason travelling with the
declaration. Migrated to the reasoned spelling — which also clears the
atelier-side precondition **C1b phase 2** names, since the legacy bare-list form
cannot carry a `why` at all.

The reasons were **lifted, never invented**, which is the whole difficulty of
this class of fix: WS1's 2026-07-23 option-A ruling and its measured ~6:1
noise-to-signal for an unscoped `docs/**`; Mike's 2026-07-23 frozen-history
ruling (records are kept verbatim, history is not retro-spelled); and PS4's
records-named-out ground from `b012884` (a record describes the tree as it stood
when written, and with no time axis it can never come clean without markers that
would falsify it). Each declaration also states **what cover is given up**, which
is the half a scope declaration usually omits.

- ✅ [2100-atelier-s-own-scope-block-carries-no-why-and-t](2100-atelier-s-own-scope-block-carries-no-why-and-t.md)

*The `ros` half of the same finding stayed OPEN and was deliberately not
delivered from here — work lands in the repo it changes (Mike's ruling,
2026-08-09). It is owed a queue entry in `ros` and nothing more from an atelier
session.*

## The subagent metadata sidecar is captured (done 2026-08-09)

Mike ruled this a new capture class on 2026-07-28. The sidecar beside each
subagent log holds facts recorded nowhere else — `toolUseId`, the join key back
to the spawning `tool_use` block in the parent session log; `spawnDepth` and
`parentAgentId`, which resolve the nesting ambiguity cctranscript's own
finished-agents comment names; and `model`, the tier an agent actually ran on,
which is the fact the queue-run tier discipline is asserted against.

**The open sub-choice, taken narrow:** scoped to `subagents/`, not name-matched
`*.meta.json` at any depth. The allowlist's point is that it admits *known*
classes and leaves the unrecognised out visibly; matching at any depth would
sweep in a future unrelated artefact sight-unseen. The cost is stated rather than
buried — if Claude Code moves subagent logs, this class silently goes empty, and
the drift alarm only fires when the *whole* walk yields nothing. Same exposure
`tool-results/` already carries: no new blindness, none removed.

**Two of the five build notes needed no code**, and saying so is the honest
result: restore mapping and manifest/integrity are structural consequences of
keying everything on `<rel>.gz`. Both were *proved* — a pruned sidecar restores
byte-identical, a tampered `.gz` is caught as `mismatch`.

**The shrink guard is inert on this class**, which is a better answer than "it's
fine": it fires only on a rewrite, and 0 of 545 sidecars was rewritten more than
a second after creation. No size or class exception was carved in — that would
weaken a working guard for an event never observed. Pinned by a two-halves test:
a tiny *first* capture is never refused, a shrinking *rewrite* is.

**The backfill is free, verified rather than assumed** — code path plus a
synthetic run where the sidecar appears with its mtime backdated a *year* and is
still taken, which is the load-bearing part because it proves age is irrelevant.
545 sidecars / 87,883 bytes on the first run after the class landed.

**Every recorded figure was stale, all larger** — 425 → 545 sidecars, 66 KB →
85.8 KB, 418 → 521 archived logs, and 538 → 545 inside a single session because
agents were spawning while it was counted. Nothing was wrong in *kind*: the key
census, the zero-archived state and the single permanent loss all held exactly.
One wording correction: the sidecar *replaces* the `.jsonl` extension rather than
appending to it, which would have misled anyone building the pairing by
concatenation. Tests 95 → 99, `mandoc -T lint` exit 0, no new flags.

- ✅ [2110-capture-the-subagent-meta-json-sidecar-mike-ru](2110-capture-the-subagent-meta-json-sidecar-mike-ru.md)
- ✅ [2120-backfill-the-sidecars-for-already-archived-tra](2120-backfill-the-sidecars-for-already-archived-tra.md)

*The one thing this work FOUND rather than finished stayed on the hot path: the
real archive exits 1 on every scheduled run, on two legitimately-condensed
whole-document files. It predates this build, so it was queued, not folded in.*

## worktree.py asks the right questions (done 2026-08-09)

`CONCURRENCY.md` as a command failed at the one cwd an operator is most likely to
be in when they land work — inside the worktree. `list` labelled that worktree's
branch `main` and showed no ahead/behind, `land <feature>` said
`no worktree found`, and `start` produced `<repo>-<old-feature>-<new-feature>`.

**The recorded diagnosis was wrong, and that is the more useful half.** The item
said the *branch* came from the cwd. It did not — the branch was already
per-worktree and already correct, which the entry itself half-admitted by noting
`git branch --show-current` agreed throughout. What came from the cwd was **repo
identity**: `toplevel(Path.cwd())` answers "which checkout am I in", and three
call sites spent that answer as "which repo is this". So `collect()` set `is_main`
true for the *current* tree, and `_feature_worktree()`/`cmd_start()` built the
directory suffix from the current tree's name. The same correction applies to
"drops its ahead/behind counts": the counts were computed correctly the whole
time and merely *suppressed*, because `render_list` gates the `↑/↓` flag on
`not is_main`. Fixing identity restored them without touching that code — and a
symptom the entry never mentioned, `start` from inside a worktree, was the same
root cause.

Identity now comes from the first entry of `git worktree list --porcelain` (git
always lists the primary tree first), so it no longer depends on where the
command ran. `_feature_worktree` returns the porcelain **entry** rather than a
bare path, so callers read the branch off the worktree they matched, and
`parse_worktrees` finally parses the `HEAD <sha>` line its docstring had claimed
for a key it never set.

**`remove` asked a ref a direct push never moves.** `git branch --merged <local
main>` refused a branch that `merge-base --is-ancestor HEAD origin/main` confirms
is contained — teaching `--force` as the routine escape from a safety check. The
referent is now `origin/<main>` then local `<main>`, each verified real, with only
exit 0 counting as merged, and an empty ref list meaning **not merged**. No
network by default (a direct push already updates the local remote-tracking ref,
confirmed on the bench); `--fetch` is opt-in.

**One fail-open the switch would have introduced, caught in the same pass:** a
detached worktree's branch reads as the literal string `"HEAD"`, and `merge-base`
would have resolved that in the *main* tree — reporting every detached worktree as
merged and removable. It now checks the detached HEAD sha.

Tests 12 → 27 on the module, suite 1222 → 1237, selftest OK, hook-plane floor exit
0, and `list` verified byte-identical from both cwds. The tests do the thing the
bug needed rather than mocking it: a real linked worktree in a temp repo, and a
bare temp remote proving a branch landed only on `origin/main` is removable while
a genuinely unmerged one is still refused.

*A baseline discrepancy resolved rather than left as a puzzle: the worker measured
1222 where this session's opening baseline said 1210. Both were right — the 1210
predates the secretscan commit in the same batch, which added exactly 12 tests.
The worker's own hypothesis (an uncollected `test_worktree.py`, which also has 12)
was a coincidence of numbers.*

- ✅ [2130-tools-worktree-py-resolves-the-branch-from-the](2130-tools-worktree-py-resolves-the-branch-from-the.md)
- ✅ [2140-remove-compares-against-local-main-which-a-dir](2140-remove-compares-against-local-main-which-a-dir.md)

*Five pre-existing defects the fix surfaced stayed on the hot path, queued not
taken — one of them (`list`'s ↑/↓ referent) would change what "behind" means on a
widely-read board.*

## cctranscript learns to search (done 2026-08-09)

Mike's ask, 2026-07-26: *"Something that lets you search all the transcripts using
regex or for a simple term. If you give cctranscript a command like `--repo` that
limits the scope to search within."* Designed 2026-07-27 with no decision left
open for him; built 2026-08-09.

The shape came from measurement, not intuition: a whole-file regex **gate** first,
so a file that misses is never parsed; UTF-8 throughout; `/i` case-folding (free at
1.8 s) rather than lowercasing the text (4.3 s); and no index, which the design
deferred as unnecessary. latin1 decoding is the fastest option of all at 0.9 s and
was rejected outright — it silently corrupts macrons, and this estate writes te reo
Māori with them. `readTurns` gained an opts object defaulting to existing
behaviour so search reuses the one extraction path instead of growing a second.
Tests 38 → 62; `mandoc -T lint` exit 0 against a baseline that was also 0, so a
real bar; drift guard green; `--help` inside its 24-line pin.

**DONE condition 13 is PARTIALLY met, and the design was wrong about the reason.**
§4 claimed "the refs are free". At file grain they are not: an `N.M` ref counts
every preceding turn, so *parse only the lines that survive the gate* and *exact
gate-invariant refs* are mutually exclusive — a contradiction the design never
noticed. Correctness was chosen, so a file that passes the gate is parsed whole.
A selective search runs at **1.22–1.32×** a bare read, which meets the condition;
a term present in every session reaches **3.7×** (9.6 s), which does not. Rather
than let a wall-clock assertion go flaky, the guard became structural —
`meta.sessionsParsed` is reported on every run and a test pins
`parsed:1 / swept:13`, which is the property the 1.5× condition existed to
protect. Recorded as partial rather than talked up.

**§10's raw-line prefilter had an unmentioned false-negative class.** The gate
reads raw JSON, where quotes, backslashes, newlines and occasionally non-ASCII
arrive escaped — the live store holds 6 escaped `ā` sequences against 6,698 raw
ones — so a plain gate could hide a hit the decoded text would show. Literal
terms are now gated on an alternation of every form the term can take (measured
free) and matched against the *decoded* turn text, so escaped spellings produce
neither false negatives nor false positives. For `--regex` the limitation is real
and lives in NOTES rather than being papered over.

**The doctrinal loose end the design named is closed.** `instruments/README.md`'s
`--materialise` note was the worked example of the ratified
flags-follow-operation rule, and it argued the flag's *absence* from cctranscript
was principled because cctranscript "never reads every file". `--search` **is**
the bulk read, so the operation appeared and the word followed. The note keeps its
original reasoning in the past tense — the rule's history stays legible — and now
states the rule in both directions: withholding the flag once the operation exists
is the same failure mirrored. Verified against the sibling surfaces rather than
assumed; no ccarchive or ccrepo behaviour had to change.

Three further design claims were corrected on contact and are recorded at the top
of the design doc rather than edited out of it: §7's illustrated tool row shows the
render's one-line summary, where the build excerpts the whole tool input (searching
one chosen field is the quiet wrongness §5 warns against); `--top` is asked for in
one §7 sentence and appears in neither the surface list nor the DONE conditions;
and two figures were stale — 440 sessions / 500 MB became 556 / 707 MB, and 24,856
thinking blocks became 31,800 with the load-bearing part holding exactly (9 carry
text, none after 2026-07-04).

- ✅ [2150-search-across-transcripts-design-done-2026-07](2150-search-across-transcripts-design-done-2026-07.md)

*The archive-plane cost stayed on the hot path, queued not taken: pool
construction dominates every `--from-archive` run and is pre-existing —
`--search` only made it visible.*

## The communication floor

Harvested 2026-08-09 from ROADMAP.md § *All doctrine directive first, enforced
second*, where the open half of this work continues.

- ✅ [2160-the-chat-plane-house-numbers-ruled-2026-08-09](2160-the-chat-plane-house-numbers-ruled-2026-08-09.md)
- ✅ [2170-the-stop-hook-is-installed-2026-08-09](2170-the-stop-hook-is-installed-2026-08-09.md)

## E8 — pathscan truncated root-anchored paths (done 2026-08-10)

The first defect this board received from a child repo under Track F's
queue-never-deliver rule, and it closed exactly as the rule intends: `faves`
reported it and left its 14 lines flagging; the fix landed here, in the repo
that owns the code.

**The reported diagnosis was wrong, and the correction is the more useful
half.** The report named dot-directories — "a path whose first segment starts
with a dot loses its leading `.well-` and its slash" — and its own repro
supported that reading, because `/.well-known/security.txt` was the only shape
it had. The real trigger is a **hyphen**, anywhere before the token's last `/`:
`/docs/some-dir/x.md` truncates to `dir/x.md` and `/a/b-c/d.md` to `c/d.md`, no
dot involved. `.well-known` was simply the commonest hyphenated
root-anchored path in a published tree.

**One character, and the invariant that explains it.** `_PATH_TOKEN`'s
lookbehind excluded `\w`, `.`, `/`, `*` and `?` but not `-`, while the token
class accepted `-`. A run of token characters can only be blocked at its start
by a preceding `/`, since every other lookbehind character is itself in the
token class and would have been consumed as part of the same run — so the
hyphen was the one place a match could resync mid-token inside a `/`-anchored
run. The header had claimed since it was written that leading-`/` mentions are
skipped; that claim was true only for paths with no hyphen in them, which is
why the class hid for so long behind a bullet that read as correct. The
invariant now stated at the regex: **the lookbehind must exclude every
character the token class accepts, plus `/`.** That is the same hole, and the
same fix, as the `*`/`?` exclusion already sitting two lines above it.

**Confirmed on this repo's own corpus, in both directions.** The gated
doctrine surface was and stayed clean. Across the whole tree 8 findings
dropped, 208 → 200, and every one was the defect: six spellings of
`repo/SKILL.md` truncated from `~/.claude/skills/create-repo/SKILL.md`; one
`plugin/plugin.json` from `<plugin-path>/.claude-plugin/plugin.json`, which is
the "tail of a just-blanked placeholder" the header names as skipped and which
was not; and `known/security.txt` from the E8 entry itself — the board's own
bug report was being mangled by the bug it reported. No legitimate finding was
lost. Module tests 76 → 86, suite 1284 → 1294, both directions pinned:
hyphenated relative paths are still candidates, a broken hyphenated path still
flags, and a token whose run begins with a hyphen still matches.

**What was deliberately not done.** Root-anchored paths are still skipped
whole, so a genuinely broken one still goes unflagged — the docstring's named
false negative, unchanged, and now pinned by a test that says so rather than
left to be rediscovered. The defect was the truncation, never the skip.
Resolving root-anchored mentions against the scan root is a separate design
decision, and it would not have helped the reporting repo in any case: its
`/.well-known/…` references are published **site URLs**, not repo paths, and
belong with the scheme-URL exemption rather than in the resolver.

- ✅ [2180-e8-pathscan-mangles-a-root-anchored-dot-direct](2180-e8-pathscan-mangles-a-root-anchored-dot-direct.md)

*Nothing is owed back to `faves` from here — children point up, the parent
never points down for truth (`method/PROPAGATION.md`), and the scanner ships to
children at floating `atelier@main`, so the fix reaches that repo on its next
floor run with no action taken in it. Clearing the 14 now-passing lines and
closing its queue entry is a `faves` session's work, not this one's.*
