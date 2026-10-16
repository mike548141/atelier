# Cold pass — "harvest" scoped to monolithic boards across the close lists

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/540-rule-4-cold-pass-queued-harvest-only-on-a-monolithic-board.md`.
**Why it earns a review:** it edits what every session does at close — in the record doctrine,
the queue-run pattern, the queue-run skill and the principal's own session-open prompt — and
narrows a word that more than one rule uses.

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

Landing commit (diff it on the delta paths; review at HEAD, `2e2da81` or later):

- `b218f1e` (2026-10-03) — record: harvest is a monolithic-board step, everywhere it is named
  (200/100 C3)

Delta paths (the pointer's own list):

- `docs/method/RECORD.md` — the harvest trigger, at the end of the harvest-integrity paragraph
- `docs/method/CONCURRENCY.md` — the closing-litany bullet in § *Orchestrated queue runs*
- `docs/method/session-open/session-open-prompt.md` — *Ending the session*
- `skills/queue-run/SKILL.md` — step 6, *Per-item close*

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **What "harvest" means.** Collect every sense the live doctrine gives the word: RECORD's
  (collapsing closed items to pointers, moving detail to the archive store), `GLOSSARY.md`'s
  (extracting what a piece of work taught into durable records), the apex's "Harvest, then
  encode", REVIEW's lens 3 *Completeness / harvest*. Say which sense each delta site meant before
  the edit and after it, and whether narrowing one sense dropped another from a close list.
- **RECORD agrees with itself.** The split-board rule (a completed item flips `[x]` in its own
  file and "there is no harvest step") against the edited trigger; and whether "the session-close
  tidy-up (above)" still resolves to the passage it means.
- **The new term.** "Roadmap close" appears in two delta sites. Is it defined anywhere a session
  would look, and does each site's parenthetical parse for a split board, a monolithic board, and a
  repo mid-migration?
- **The tools agree.** `tools/harvestscan.py`, `tools/sizescan.py`'s archive gate and
  `tools/board.py`, as documented in `tools/README.md`: do they treat split and monolithic boards
  the way the edited text says?
- **Children.** The template `docs/build/templates/docs/ROADMAP.md` stamps a monolithic board.
  Does a child reading its stamped close rule now know what to do at close?

**Non-goal:** the split-board design itself (already doctrine). The close lists' consistency with
it is the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether
   scoping the word was the right fix, against defining it once and pointing at the definition.
2. **Correctness & quality.** Diff `b218f1e` on the four paths. Record, per delta site, the text
   before and after and which board shapes it now covers.
3. **Completeness / harvest.** Every other close list that names the roadmap step: the template
   `CLAUDE.md` *Session rhythm* bullet, this repo's `CLAUDE.md`, the `session-onramp` skill, the
   PROPAGATION floor region, other files under `docs/method/session-open/`. Which were left as
   they were, and does each still agree?
4. **Security & privacy** — mandatory. Harvest moves or deletes record content; RECORD makes bulk
   deletion from a record store a show-first action. Say whether the scoping changes when that
   deletion happens or whether it is shown first. No code surface: `/security-review` is
   discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/harvestscan.py --root . .`, `python3 tools/sizescan.py --check --root . .` and
  `python3 tools/board.py --check --root .`, exit codes read explicitly
- `python3 tools/pathscan.py --root . .` and `python3 tools/linkscan.py --root . .` over the
  delta sites' cross-references
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
`docs/roadmap/160-doctrine-review-owed/540-rule-4-cold-pass-queued-harvest-only-on-a-monolithic-board.md`,
the sibling `docs/reviews/2026-10-16-1510-harvest-monolithic-board-cold.deferred.md`, the landing
commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/540-rule-4-cold-pass-queued-harvest-only-on-a-monolithic-board.md
--also-exclude docs/reviews/2026-10-16-1510-harvest-monolithic-board-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `HM`: `HM1`, `HM2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
