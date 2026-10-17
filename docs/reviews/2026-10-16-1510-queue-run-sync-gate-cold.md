# Cold pass — the queue-run skill's sync step gains the status-first gate

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/520-rule-4-cold-pass-queued-queue-run-sync-gate.md`.
**Why it earns a review:** the skill is the delivery vehicle every queue run loads; its first act
on a shared checkout decides whether a peer's uncommitted work is preserved or shelved. A small
wording change here is executed verbatim by every orchestrator that loads it.

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

- `d6a3faf` (2026-10-03) — skills: queue-run reads git status before it pulls (200/100 C1)

Delta path: `skills/queue-run/SKILL.md`, step 2 (*Sync + onramp*). A later commit, `b218f1e`,
edited step 6 of the same file (another pass's subject); check it did not move step 2.

## Scope

Widest the work admits; the lenses organise it, they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Parent agreement, term by term.** Step 2 against `docs/method/CONCURRENCY.md` § *Integration
  hygiene* (the opening bookend's two gates) and § *The trigger*, the floor region in
  `docs/method/PROPAGATION.md`, its stamped copy in `docs/build/templates/CLAUDE.md`, and this
  repo's own `CLAUDE.md` read order step 1. Compare: what counts as "yours", what "stop" means,
  "no upstream" against "no remote", and the order of status, pull and onramp.
- **The skill's own contract.** Its header comment calls it a stamped copy that may compress its
  parent, never contradict it, and names restating standing rules as the drift it exists to
  avoid. Judge step 2 against that header, and check whether any guard watches this file.
- **An orchestrator's cases.** Walk the step for: a primary checkout dirty with a peer's work when
  the run must claim on `main` from the primary first (CONCURRENCY § *Claiming work*); a run
  resumed after a context cut with its own uncommitted work; worker output left in the primary;
  only untracked files; a detached HEAD; an upstream that is set but unreachable; a branch with a
  remote but no upstream. For each: what does the run do next, and is that written anywhere?
- **After "move to a worktree".** Which base does the new worktree take if the pull never ran?
- **Distribution.** The skill ships to other repos; say how a child receives this change.

**Non-goal:** the status-first rule itself in CONCURRENCY (already doctrine). Its restatement and
fit in the skill are the subject.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   skill step that restates its parent was the right fix for a skill step that contradicted it.
2. **Correctness & quality.** Diff `d6a3faf`. Run the case table above and record it.
3. **Completeness / harvest.** Every other place that tells a session to pull at start: the
   `session-onramp` skill, the session-open prompt under `docs/method/session-open/`, `README.md`,
   the plugin bundle. Which still carry the ungated bookend?
4. **Security & privacy** — mandatory. The hazard is integrity: a peer's work shelved onto a
   shared stash stack, popped by someone else, or absorbed into a commit. Say whether the new step
   closes each path. No code surface: `/security-review` is discharged by grounds.

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- the step itself, driven in a private scratch clone with a second linked worktree holding
  uncommitted edits: run the commands the step names in its order and record what happens
- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/pathscan.py --root . .`
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-1510-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Every probe that
  stashes, pulls or checks out runs in a private clone under your session scratchpad, named by
  your prefix — never against a live checkout.
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
`docs/roadmap/160-doctrine-review-owed/520-rule-4-cold-pass-queued-queue-run-sync-gate.md`, the
sibling `docs/reviews/2026-10-16-1510-queue-run-sync-gate-cold.deferred.md`, the landing commit's
message body (the author's account; read subject, stat and diff only), and the commissioning
item
`docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md`.

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/520-rule-4-cold-pass-queued-queue-run-sync-gate.md
--also-exclude docs/reviews/2026-10-16-1510-queue-run-sync-gate-cold.deferred.md --also-exclude
docs/roadmap/200-anti-slop-invariant-registry-promote-rec/100-r2-found-eleven-live-contradictions.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `SY`: `SY1`, `SY2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.

---

# Verdict — phase 1 (2026-10-17, 09:44–09:55 UTC)

## Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent — the tier the principal names for cold
  passes (ruling 2026-08-04), checked at spawn. Spawned 2026-10-17 by the Fable orchestrator of
  the 2026-10-17 rule-4 run, which claimed the pass in `8acfff1`, authored neither the delta nor
  this brief, and holds the deferred sibling outside my reach until these findings are
  committed (the context partition rule 1 calls structural). The orchestrator forms no finding
  and writes no severity. Neither the delta's author (the 2026-10-03 run) nor the brief-writer
  (an Opus subagent of the 2026-10-16 run) started or instructed this session.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD
  `f74fb29` (`8acfff1` and the brief's floor `2e2da81` both ancestors, checked with
  `merge-base --is-ancestor`). Read-only to me except this file; no git write was run in it.
  Every probe that pulled, stashed or checked out ran in a private scratch clone under my
  session scratchpad, folder `SY/`.
- **What I read:** this brief; `d6a3faf` and `b218f1e` as subject + `--stat` + diff on the
  delta path only (no message body); `skills/queue-run/SKILL.md`, `skills/session-onramp/
  SKILL.md`, `docs/method/REVIEW.md`, `docs/method/CONCURRENCY.md`, `docs/method/
  session-open/session-open-prompt.md` in full; the floor region of `docs/method/
  PROPAGATION.md` and its bundled-mode variant; `docs/build/templates/CLAUDE.md` lines 57–72;
  `CLAUDE.md` step 1; `README.md` §*Install as a Claude Code plugin*; `.claude-plugin/*.json`;
  `.githooks/pre-commit`, `.github/workflows/ci.yml`, `.atelier-floor.json`,
  `.stampscanignore`, `tools/blockscan_map.json` (one entry), `tools/test_templates.py`
  lines 395–578, `tools/worktree.py` (start path); board items `320/150`, `320/210`,
  `320/480` and two grep-hit lines of `360/README.md`. The `CHANGELOG.md` head and one
  2026-07 entry.
- **Not opened:** `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, any prior
  verdict, the queue pointer `160/520`, the sibling, the commissioning item `200/100`, any
  other `2026-10-16-15*` brief. No `--include-barred` sweep was run.
- ⚠️ **Exposure, disclosed:** (1) a file-level `grep -l` for the bookend listed the *names*
  of three prior verdicts and five session records (names only, not opened); (2) `ls` of
  `docs/roadmap/160-doctrine-review-owed/` showed the pointer filenames, `160/520` among them
  (not opened); (3) the coldsweep for `autostash` returned one line each from two *other*
  passes' pointers (`160/310`, `280/030`) — a finding ID with a severity word and a fragment
  about the autostash bookend. Neither names this delta; I formed no finding from them.
- **Tools run at a bare name:** none. No instrument was run.

## Lens 1 — approach & assumptions

Load-bearing assumptions, named first, then tested:

1. *A skill step may restate its parent so long as it does not contradict it.* The skill's own
   header says more: it "points at the doctrine rather than restating it" and names restating
   standing rules as "the drift the pattern was captured to kill". The delta replaced a
   two-line step that contradicted the parent with a seven-line step that restates it.
   The alternative fix — shrink step 2 to "run the opening bookend exactly as
   `CONCURRENCY.md` § *Integration hygiene* states it, then load the onramp" — removes the
   contradiction and the second source at once. The delta chose restatement without a guard
   (SY2).
2. *The status-first gate is sufficient for an orchestrator.* It is sufficient for a session
   that only needs to sync. An orchestrator's next act (step 4) is a commit on `main` from the
   primary checkout; a dirty primary makes the pull impossible, and nothing in step 2 or step 4
   says how the run then reaches a current `main` (SY1).
3. *"Yours" is decidable at step 2.* For a fresh run it is trivially empty; for a resumed run
   it is undecidable — the parenthetical "(or only your own work)" serves neither (SY4).
4. *The change reaches the orchestrators who execute it.* The skill travels only inside the
   plugin, whose version has not moved since 2026-07-21 (SY6).

Was restating the parent the right fix for a step that contradicted it? **Partly.** The
contradiction is gone and the restatement agrees with the parent term by term on the two
gates. But the file's own contract forbids the shape, no guard watches the copy, and the copy
already differs from its two sibling copies in one term (SY3).

## Lens 2 — correctness & quality

**The diff (`d6a3faf`).** Four files: the skill (+10/−3 on step 2), the queue pointer, the
commissioning item, the generated index. The skill hunk is the only delta path; the pointer
and item are records. `b218f1e` touched step 6 only (lines 75–78, "harvest" → "close"); step 2
sits at lines 49–55 unmoved — confirmed by diff.

**Term-by-term against the parent** (`CONCURRENCY.md` 180–192; floor bullet `PROPAGATION.md`
145–151 = template 57–63, verified identical by stampscan; `CLAUDE.md` 13–22):

| Term | Parent | Floor / template | Skill step 2 | Agreement |
| --- | --- | --- | --- | --- |
| Order | status, then pull | status, then pull | status, pull, onramp | same |
| "yours" | "anything dirty that is not yours" | "dirty work this session didn't make" | "dirty work that is not yours (or only your own work)" | same meaning; the skill adds an allowance (SY4) |
| "stop" | "a stop and a move to a worktree" | "stop and move" | "stop and move to a worktree" | same words, same gap (SY1) |
| no-remote gate | "no remote, no bookend … no upstream" | "where there is a remote" | "no upstream skips the pull" | three terms (SY3) |
| untracked | not stated | not stated | not stated | shared silence (SY5) |

**The case table** (each driven in the scratch clone, git 2.50.1; `R` = the primary is dirty
with a peer's work, incoming commit touches a different file unless stated):

| Case | What `git pull --rebase --autostash` did | What the step tells the run to do next | Written anywhere? |
| --- | --- | --- | --- |
| A. R, tracked edit | `Created autostash` → fast-forward → `Applied autostash`; stash list empty after; peer's edit back in place | the step forbids reaching this line; if run, the peer's work transited the shared stack | gate only |
| J. R, peer's file **staged** (the 2026-09-06 shape) | as A, but the peer's file came back **unstaged** (`M ` → ` M`) — the peer's index state was silently flattened even though nothing conflicted | same | **no** — neither surface says the clean case alters the peer's state |
| B. R, peer's edit conflicts with the incoming commit | `Applying autostash resulted in conflicts … safe in the stash`; `stash@{0}: autostash` left on the stack and **visible from the peer's worktree**; a `stash pop` there dropped conflict markers into the peer's tree | same | the parent names the shared stack; the skill says "never let it shelve" |
| C. untracked file only | not stashed, not touched; fast-forward beside it | ambiguous — is `??` "dirty work"? | **no** (SY5) |
| D. detached HEAD, dirty | refused: "not currently on a branch", exit 1, no stash | silent; outcome safe | no, harmless |
| E. no upstream at all, dirty | refused: "no tracking information", exit 1, no stash | "skips the pull" — matches git's own behaviour | parent + skill |
| F. upstream set, unreachable, dirty | fetch fails first, exit 1, no stash (the 2026-09-06 luck, reproduced) | silent; outcome safe | no, harmless |
| G. remote exists, branch has no upstream, dirty | refused as E, exit 1, no stash | skill: skip; floor: "where there is a remote" → run it → error | SY3 |
| H. "move to a worktree", pull never ran | `git worktree add -b x` based on local `main`, **3 behind** `origin/main`; `tools/worktree.py start` resolves its default start point to the branch *name* `main` and never fetches | nothing | **no** (SY1) |
| I. R, primary behind origin, run must claim | plain `pull --rebase` refuses ("You have unstaged changes"); `git fetch` + `merge --ff-only origin/main` fast-forwarded with the peer's dirty file untouched | step 4 says "from the primary checkout" and `§ Claiming work` says "push rejected → pull --rebase", which cannot run here | **no** (SY1) |

Case C2 (untracked file at a path the incoming commit creates) misfired in my harness — the
reset pulled the remote file in before the local one was written — so it is **not exercised**
and I claim nothing about it.

## Lens 3 — completeness / harvest

Every live place that tells a session to pull at start, swept with coldsweep (barred set
excluded, three patterns): the parent (gated), the floor bullet and its stamped template copy
(gated, identical), `CLAUDE.md` step 1 (gated; omits the no-remote gate, which is right for a
repo that has one), and the skill (gated by this delta). The `session-onramp` skill, the
session-open prompt and `README.md` carry no bookend at all — the prompt defers to
`CONCURRENCY.md` and to this skill, so the skill *is* the surface a run executes. The only
ungated bookends left are frozen records: `CHANGELOG.md` line 2318 (a 2026-07 entry) and
`360/README.md` line 8 (a board note describing the rule as it then stood). **No live surface
still carries the ungated form.** What the harvest found missing is not a surface but a
signal: nothing tells a plugin-only child the skill changed (SY6), and nothing tells a future
editor of the parent that the skill holds a copy (SY2).

## Lens 4 — security & privacy

**`/security-review` discharged by grounds:** it reads this session's pending diff, which is
the other reviewers' draft verdicts and the orchestrator's twenty sibling deletions — not the
delta, which landed 2026-10-03 — and its exclusions bar Markdown, so a clean pass over this
work would be definitionally empty. Checked by hand instead against the OWASP Top 10: the
only class that reaches a prose rule about a shared working tree is A08 *Software and Data
Integrity Failures*; there is no input, authentication, injection or secret surface.

The three integrity paths the brief names, against the probes:

- **A peer's work shelved onto the shared stash stack.** Cases A and J show it transits the
  stack even when nothing conflicts, and J shows the transit is not lossless (staged →
  unstaged). The step closes this path **only as prose**: a session that reads `git status`
  and stops does not reach the command. No mechanism; the floor's `board --staged` check
  guards the index at commit, not the bookend at open.
- **Popped by someone else.** Case B: the leftover `autostash` entry is listed from the peer
  worktree and a pop there writes conflict markers into the peer's tree. Closed by the same
  prose gate, and by nothing else.
- **Absorbed into a commit.** Step 2 is silent; the cover is step 4's pointer to `§ Claiming
  work` (claim alone at a dirty primary; read the whole staged diff). Adequate as a pointer.

No privacy surface: the delta names no person, path outside the repo, or secret. Nothing in
my probes touched a live checkout.

## Findings

**SY1 — MODERATE.** *Step 2's "stop and move to a worktree" leaves the run with no sync path,
and step 4 then cannot land.* At a dirty primary the pull is forbidden (correctly), so local
`main` stays where it was: the worktree the step tells the run to take is based on a stale
`main` (case H — 3 behind in the probe; the house tool `worktree.py start` resolves its default
start point to the branch name `main` and never fetches), the onramp is read from stale docs,
and the claim step 4 demands "on `main` from the primary checkout" lands on a stale `main`
whose push will be rejected, after which `§ Claiming work`'s remedy — `pull --rebase` — refuses
on the dirty tree (case I). Nothing on either surface says what the run does next. The parent
shares the gap word for word, so this is a fit defect the skill inherits, not one it created;
the brief's non-goal fences the rule, not its consequence for an orchestrator. *Counsel:*
`git fetch origin` is always safe at a dirty tree (touches no working file, creates no stash) —
say so; base the worktree on `origin/<main>`; for the claim, `git merge --ff-only
origin/<main>` in the primary when the peer's dirty paths and the incoming commits are
disjoint (case I did exactly this), else CF3's "sync, take the next open item, touch nothing".
Per `PROPAGATION.md`'s resolved-upward rule the words belong in the parent, with the skill
pointing at them.

**SY2 — MODERATE.** *The delta closes an instance of restatement drift by adding an unguarded
restatement.* The canonical rule gained its two gates on 2026-09-18 (`54201e0`, which
harmonised the floor bullet, the template and `CLAUDE.md` step 1 — and missed this skill, the
surface V3 names). The skill carried the contradicting form for fifteen days until `d6a3faf`.
That is the drift class the skill's header says it exists to kill, and the delta fixes the
instance without the class: `tools/test_templates.py` pins seven other phrases of this file
against `CONCURRENCY.md` and none of step 2; `tools/blockscan_map.json` maps `§ Integration
hygiene` to the floor bullet and the template only; stampscan verifies one stamped block in
the whole tree (the template) and the skill carries no `stamp:` region; `skills/` is outside
wrapscan, spellscan and pathscan scope. The next edit to the parent's bookend will leave this
copy stale again, and nothing will say so. *Counsel (either, not both):* (a) shrink step 2 to a
pointer — "run the opening bookend exactly as `CONCURRENCY.md` § *Integration hygiene* states
it; then load the onramp" — which is what the header promises; or (b) keep the words and pin
them the way the stop roster is pinned (a parity test on the two gate phrases, or a
`blockscan_map.json` entry adding the skill as a third target of `§ Integration hygiene`).

**SY3 — minor.** *Three copies, three terms for the no-remote gate.* Parent: "no remote, no
bookend — a repo with no upstream"; floor and template: "where there is a remote"; skill: "a
repo with no upstream skips the pull". Case G (a remote exists, the branch has no upstream)
separates them: git refuses the pull with exit 1 and no stash, so the skill's "upstream" is the
accurate term and the floor's "remote" sends a session into an error it was told would not
happen. Harmless in outcome, but V3/V5: the parent should pick one term and the copies carry
it. *Counsel:* "upstream" — it is the thing git actually tests.

**SY4 — minor.** *"(or only your own work)" allows a judgement the step cannot make.* At step 2
a fresh run has done nothing, so "yours" is empty by construction; the one run for which it is
not — one resumed after a context cut — cannot tell its own uncommitted work from a peer's, and
the step points it nowhere (`§ Surviving an interrupted session` is the home). Case J shows the
cost of a wrong guess is not nil even when nothing conflicts. *Counsel:* at step 2, "anything
dirty is a stop"; a resumed run runs the recovery sweep first.

**SY5 — minor.** *"Dirty work" does not say whether untracked files count.* `--autostash` never
stashes untracked files (case C), and a peer's commonest in-flight artefact is a new file — a
session record, a board item. The parent's recovery table treats "no untracked" as part of
clean; step 2 and the parent's bookend both say only "dirty". *Counsel:* "anything `git
status` shows, untracked included".

**SY6 — MODERATE.** *The change ships silently.* The skill reaches a child only inside the
plugin (`.claude-plugin/marketplace.json`, source `./`). `plugin.json` has carried `0.2.0`
since 2026-07-21 through four edits of this file; `PROPAGATION.md`'s bundled-mode variant
tells a plugin-only adopter to detect doctrine movement by grepping that version and then
"read the plugin's `CHANGELOG.md`", and `CHANGELOG.md` has no entry for `d6a3faf`. So the one
behaviour change every orchestrator executes first arrived with neither of the two signals the
doctrine says a child reads, and reaches a child only on an unprompted reinstall. The skill is
doctrine by function (rule 3), so by the doctrine's own grammar the version is owed a move.
*Counsel:* a `CHANGELOG.md` entry and a version bump for doctrine-bearing skill edits, stated
as a rule where the bundled-mode variant lives — or an honest note there that the version
tracks releases, not doctrine, and the drift check is weaker than it reads.

## Standing checklist V1–V7

- **V1** — discharged: the commit subject claims exactly what the diff does; the step's "never
  let `--autostash` shelve it" is a prohibition, not a claim of mechanism.
- **V2** — no "live-proven" claim in the delta; the step was re-driven anyway (ledger).
- **V3** — swept (lens 3): no live ungated bookend remains; term divergence is SY3, the missing
  delivery signal is SY6.
- **V4** — SY2: the skill is now a second statement of `§ Integration hygiene`, unstamped.
- **V5** — SY1: step 2's "move to a worktree" against step 4's "from the primary checkout".
- **V6** — lens 4 above; scanner discharged by grounds, OWASP checked by hand.
- **V7** — provenance stated in the brief and repeated above.

## Overall

**PASS-WITH-FINDINGS — 0 MAJOR · 3 MODERATE · 3 minor · 0 note.** The restatement is faithful
to its parent on both gates and removes a live contradiction every orchestrator executed; what
it does not do is tell a run how to proceed once the gate fires, guard the copy it added, or
reach the children who load it with any signal that it changed.

## Re-run ledger

All from the worktree root unless stated; heavy steps under `nice -n 10`, one at a time, in the
foreground. Exit codes read directly, not off a pipe (a first floor run read its codes through
a pipe and lost them; it was re-run to a file).

| Command | Result |
| --- | --- |
| `git show d6a3faf --stat --format='%h %s'`; `git show d6a3faf --format='%h %s' -- skills/queue-run/SKILL.md` | 4 files; skill hunk +10/−3 at step 2 |
| `git show b218f1e --format='%h %s' -- skills/queue-run/SKILL.md` | step 6 only; step 2 unmoved |
| `git merge-base --is-ancestor 8acfff1 HEAD`; same for `2e2da81` | both ancestors of `f74fb29` |
| `python3 tools/coldsweep.py --root . --also-exclude ×3 'autostash'` / `-i 'no (upstream\|remote)'` / `-i 'git status.{0,12}first'` | 25 / 28 / 7 hits; 396 files barred each run; no `--include-barred` |
| `nice -n 10 python3 tools/stampscan.py --warn --root . .` | clean — 1 stamped block verified (template = floor, identical); exit 0 |
| `nice -n 10 python3 tools/pathscan.py --root . .` | exit 0; 8 whole-tree advisories in `skills/create-repo/SKILL.md` and `tools/README.md`, none on the delta |
| `nice -n 10 python3 tools/floor.py --plane ci --root .` | **exit 0**; 11 enforced ✅, secretscan 23 advisory, leakscan degraded (no `--require-terms`), pathscan 2 advisory (`docs/decisions/2026-10-03-0641…` and the session-open prompt's `../atelier/…` path), neither on the delta |
| `nice -n 10 python3 tools/floor.py --plane hook --root .` | **exit 0**; all 11 enforced ✅ |
| `nice -n 10 python3 -m unittest discover -s tools -p 'test_templates.py'` | 44 tests OK — `QueueRunSkillTest` pins nothing about step 2 |
| `sh …/SY/probe.sh` (scratch clone: bare origin, primary, linked worktree) | cases A, B, H valid; case B's conflict poisoned C–G (my harness, not the step) |
| `sh …/SY/probe2.sh` (primary reset between cases) | C, D, E, F, G, I, J valid; C2 misfired (not exercised) |
| `python3 tools/floor.py --list --plane ci` / `--plane hook` | 16 registry checks per plane; no check targets `skills/` |
| `grep -rn 'stamp:begin' --include='*.md'` (records excluded) | one real stamp in the tree: `docs/build/templates/CLAUDE.md:18` |
| `git log --format='%h %ad %s' --date=short -- .claude-plugin/plugin.json` | last change 2026-07-21 (`2271a44`, v0.2.0) |
| `git log … --since=2026-09-10 --until=2026-09-25 -- <five sync surfaces> skills/` | `54201e0` 2026-09-18 touched the parent, floor, template and `CLAUDE.md`; no `skills/` commit until 2026-09-20 (`c38b7da`, unrelated) |
| `date -u` at open / at this write | 2026-10-17 09:44 UTC / 09:49 UTC |

The full Python suite and the Node suite were **not** run: the brief's re-run list did not
name them, the targeted guard (`test_templates.py`) was run, and the machine carried a load
average above 7 with two sibling reviewers live.

## Follow-up checklist (for the principal's decision — nothing applied)

- [ ] SY1 — decide where "what the run does after the stop" lives (parent, with the skill
      pointing); whether `fetch` + `origin/<main>` base + `--ff-only` becomes the written path.
- [ ] SY2 — choose pointer or pinned copy for step 2; if pinned, add the parity test or the
      blockscan map entry in the same commit as the wording.
- [ ] SY3 — one term for the gate ("upstream"), carried to the floor bullet and template.
- [ ] SY4 — drop the "(or only your own work)" allowance at step 2; point resumers at the sweep.
- [ ] SY5 — say whether `??` counts as dirty, in the parent.
- [ ] SY6 — rule on version bump + `CHANGELOG.md` entry for doctrine-bearing skill edits, or
      weaken the bundled-mode drift claim honestly.
- [ ] Exercise case C2 (untracked file at a path the incoming commit creates) before relying on
      any statement about it.
