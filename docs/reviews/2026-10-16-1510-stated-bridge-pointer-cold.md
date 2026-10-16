# Cold pass — SECRETS' stated-bridge pointers repointed to PRINCIPLES

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/570-rule-4-cold-pass-queued-stated-bridge-pointer.md`.
**Why it earns a review:** SECRETS makes a standing credential, and a store with no read trail,
acceptable only as a named bridge; the citation is how a reader finds what a bridge obliges. A
citation that lands on the wrong rule, or misses a site, leaves that obligation unfindable. A
small delta: keep the review proportionate.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run that landed the commit below; its
  intent record is the session file dated 2026-10-03 0144 UTC that the pointer names (not opened
  by the brief-writer). The commit's trailer names an Opus model.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by the Mike-opened
  Opus queue-run session `abe96d8d` on 2026-10-16, on Mike's answer of that date that a fresh Opus
  session writes these briefs. Neither it nor its orchestrator authored the delta or was started
  or instructed by its author. **Off-tier for review, disclosed: it forms no finding and writes no
  severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the seven queue
  pointers it was assigned (160/500, 520–570; refs-only, each ending in the orchestrator's claim
  line); the seven landing commits' subjects, `--stat` lists, full message bodies (the author's
  account) and diffs on the delta paths; `docs/method/REVIEW.md` in full; the ask halves of two
  2026-10-04 briefs as templates; HEAD text of the neighbouring surfaces named in *Scope*; single
  grep-hit lines from unrelated board items and old `CHANGELOG.md` entries; filenames (not
  contents) of prior verdicts; and its own cross-session memory index. It did not open the intent
  record, the commissioning board item, `docs/SESSIONS.md`, `docs/sessions/`,
  `docs/ROADMAP-DONE.md` or any prior verdict. Its orchestrator read the `docs/SESSIONS.md` index
  tail (entries through 2026-10-16, including the authoring run's one-paragraph summary) and the
  2026-10-16 session record's close section, and passed no evaluative content beyond the pointer
  list. Everything evaluative the brief-writer formed is in the sibling.

## What the work is

Landing commit (diff it on the delta path; review at HEAD, `2e2da81` or later):

- `338ff6d` (2026-10-03) — secrets: the stated-bridge rule lives in PRINCIPLES, so point there
  (200/100 C6)

Delta path: `docs/method/SECRETS.md`, two citations — one closing the paragraph on standing
credentials as a tracked debt, one in the detection duty about a store with no read trail.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Fit at each site.** Read the cited rule in `docs/method/PRINCIPLES.md` (§7, *Codify before you
  converge; a hand-action is only a stated bridge*) and say, per SECRETS site, what kind of thing
  the site calls a bridge and whether the cited rule obliges what that site needs. Compare any
  other candidate home — for example §5's *Secure by default*, which refers to "the same 'stated
  bridge' grammar §7 gives".
- **The old home.** Confirm by search that `docs/method/DATA-PROTECTION.md` holds no such rule at
  HEAD, and say whether it ever did (`git log -S`).
- **Every site.** List every occurrence of "stated bridge" and every `DATA-PROTECTION.md`
  citation in SECRETS and its neighbours (`ACCESS.md`, `AUTONOMY.md`, `PRINCIPLES.md`,
  `GLOSSARY.md`). For each, say which rule it means and whether its citation (or lack of one)
  takes a reader there.
- **Citation form.** The new citations quote a phrase and name a file, with no section number or
  anchor. Is the quoted phrase verbatim, and would the citation survive the heading's rewording?

**Non-goal:** the stated-bridge doctrine itself; where SECRETS points for it, and whether that
place says what SECRETS relies on, is the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   "the stated-bridge rule" is one rule with one home, or a grammar used in several places.
2. **Correctness & quality.** Diff `338ff6d`. Record the per-site table from *Scope*.
3. **Completeness / harvest.** The sweep above; a mis-cited rule found once is a class to sweep.
4. **Security & privacy** — mandatory. SECRETS is security doctrine. Say whether a reader who
   follows each citation ends up knowing that a standing credential must stay listed, dated and
   tightened, not merely tolerated. No code surface: `/security-review` is discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `grep -n -i 'stated bridge\|stated-bridge\|DATA-PROTECTION' docs/method/*.md`, read in full
- `git log -S 'stated-bridge rule' --oneline` across the tree
- `python3 tools/linkscan.py --root . .` and `python3 tools/pathscan.py --root . .`
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-1510-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts go
  in a private clone under your session scratchpad, named by your prefix.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds, or
  keep the tree clean when you spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/570-rule-4-cold-pass-queued-stated-bridge-pointer.md`, the
sibling `docs/reviews/2026-10-16-1510-stated-bridge-pointer-cold.deferred.md`, the landing
commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/570-rule-4-cold-pass-queued-stated-bridge-pointer.md
--also-exclude docs/reviews/2026-10-16-1510-stated-bridge-pointer-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `BR`: `BR1`, `BR2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
