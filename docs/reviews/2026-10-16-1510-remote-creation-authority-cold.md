# Cold pass — REPO-STANDARD's remote-creation authority

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/530-rule-4-cold-pass-queued-remote-creation-authority.md`.
**Why it earns a review:** it changes what authorises an agent to create a remote repository — an
act on the boundary between "push to the owner's own remotes" (granted) and widening an audience
(the floor) — in the standard every new repo is built to.

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

- `96ffaa3` (2026-10-03) — build: a new remote needs the principal's ask, not 'push is
  recoverable' (200/100 C2)

Delta path: `docs/build/REPO-STANDARD.md`, step 5 of *Process — a new repo*. A later commit,
`1ffefc7`, edited other parts of the same file (another pass's subject); check it did not move
step 5.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Which text is the parent.** Step 5 now matches `skills/create-repo/SKILL.md` step 7. Establish
  from `docs/method/PROPAGATION.md` which of the two is canonical, how a parent/child disagreement
  is meant to be resolved (and what holds in the interim), and who decides it. Search the
  doctrine and `docs/decisions/` for any principal ruling on remote creation, either way.
- **AUTONOMY's classes.** `docs/method/AUTONOMY.md` grants push to the owner's own remotes and puts
  making a private thing public, and new trust surfaces, on the floor. Where does creating a remote
  sit? Does AUTONOMY say it, and does step 5 agree with what AUTONOMY says or leaves unsaid?
- **"The principal's ask itself."** Case table: the principal asks for "a new repo" with no
  mention of a remote; a queue run takes a board item that says "create repo X"; standardising an
  existing repo that has no remote; a local experiment later promoted; the instance profile's
  default visibility set to public; an owner account that is an organisation, not the operator.
  For each: does step 5 tell the session whether to proceed, confirm, or stop?
- **The steps after.** Step 6 sets delete-branch-on-merge "on the new remote", and the visibility
  fact is stamped into the child. What happens to both while a confirmation is pending or refused?
- **The cross-reference.** "`skills/create-repo` step 7 says the same": verify the claim, and
  whether anything keeps the two in step when either is renumbered.

**Non-goal:** whether creating a remote should need confirmation at all is the principal's call;
whether the text gives a session one clear answer, and agrees with its neighbours, is the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether the
   change took "the more careful reading" on authority the doctrine actually gives, and whether
   "the principal's ask" is something a session can determine from what it holds.
2. **Correctness & quality.** Diff `96ffaa3`. Run the case table and record it.
3. **Completeness / harvest.** Every other site that states who may create a remote or the "push
   is recoverable" reasoning: AUTONOMY, the create-repo skill's other steps, the session-onramp
   skill, `README.md`, the templates, the PROPAGATION floor region. Which still say the old thing?
4. **Security & privacy** — mandatory. A remote is an audience surface: wrong default visibility,
   the wrong owner account, a remote created before a scan has run on the first commit. Say whether
   step 5 and its neighbours keep each closed. No code surface: `/security-review` is discharged by
   grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `git log -S 'push is recoverable' --oneline` across the tree, to find every site that ever
  carried the old reasoning and whether each was swept
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/pathscan.py --root . .`
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

Do not create any remote, even a scratch one, to test the rule.

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
`docs/roadmap/160-doctrine-review-owed/530-rule-4-cold-pass-queued-remote-creation-authority.md`,
the sibling `docs/reviews/2026-10-16-1510-remote-creation-authority-cold.deferred.md`, the landing
commit's message body (the author's account; read subject, stat and diff only), and the
commissioning item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/530-rule-4-cold-pass-queued-remote-creation-authority.md
--also-exclude docs/reviews/2026-10-16-1510-remote-creation-authority-cold.deferred.md
--also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `RM`: `RM1`, `RM2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
