# Cold pass — the concurrency cue count

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/560-rule-4-cold-pass-queued-three-cues.md`.
**Why it earns a review:** § *The trigger* is how a session learns it may not be alone; the
delta changes the count of its firing cues and so every claim the paragraph makes about "the
cues" as a set. A small delta: keep the review proportionate, but test every predicate.

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

- `df0820e` (2026-10-03) — concurrency: three cues, not two (200/100 C5)

Delta path: `docs/method/CONCURRENCY.md`, § *The trigger*: the paragraph introducing the firing
cues and the line that heads their list. Read the whole section; the delta's meaning depends on
the sentences around the two edited words.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Every predicate over the set.** The paragraph and the list say the cues are cheap, need no
  locking machinery, are ways to *discover* concurrency, and that their silence licenses nothing;
  the third cue's own text calls the other two "discoveries you make by accident". Test each
  predicate against each of the three cues and record a cue-by-predicate table.
- **What a cue is.** The paragraph opens "The substrate rule still needs a firing cue". For each
  cue, does it end in the substrate action (move to a worktree), or only in knowledge? Is each a
  cue in the paragraph's own sense?
- **The section's opening.** Its first paragraph speaks of "a blind spot in the cues below" and
  names one cue's limit. Does it still read true over three?
- **History.** Find when the third cue and § *The channel* landed (`git log -S`), and whether
  that landing left other set-level claims or mirror sites un-updated besides the count.
- **Mirror sites.** Any other place that counts, lists or summarises the cues: the PROPAGATION
  floor region and its stamped template copy, this repo's `CLAUDE.md`, the `session-onramp` and
  `queue-run` skills, `docs/method/GLOSSARY.md`, § *The channel* itself.

**Non-goal:** the cues themselves (already doctrine); the paragraph's claims about them, and its
agreement with its mirrors, are the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   correcting a count was the whole of what the mismatch signalled.
2. **Correctness & quality.** Diff `df0820e`. Produce the predicate table above.
3. **Completeness / harvest.** The mirror sweep above; say which sites agree at HEAD.
4. **Security & privacy** — mandatory. The paragraph guards the shared working tree, an integrity
   surface. Check whether any reading lets a session treat a silent or unavailable channel as
   evidence it is alone. Otherwise discharge in one line with grounds. `/security-review` is
   discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `git log -S 'two cues' --oneline` and `git log -S 'Ask, when a channel exists' --oneline`
- `python3 tools/stampscan.py --warn --root . .` for the stamped floor region
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
`docs/roadmap/160-doctrine-review-owed/560-rule-4-cold-pass-queued-three-cues.md`, the sibling
`docs/reviews/2026-10-16-1510-three-cues-cold.deferred.md`, the landing commit's message body
(the author's account; read subject, stat and diff only), and the commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/560-rule-4-cold-pass-queued-three-cues.md --also-exclude
docs/reviews/2026-10-16-1510-three-cues-cold.deferred.md --also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `TC`: `TC1`, `TC2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
