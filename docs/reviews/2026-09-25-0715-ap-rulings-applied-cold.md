# Cold pass — the AP rulings applied — the ADR 0008 amendment and its code surfaces

**Pass type:** code + doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md`.
**Why it earns a review:** an ADR control clause re-worded to describe a
boundary that is deliberately *not* enforced, plus the code and workflow
surfaces that clause describes — a wrong word here is inherited by every child
that calls the floor at `@main`.

## Spawn provenance

- **Author of the work under review:** the session(s) that landed the commits
  named under *What the work is*. This brief-writer was not that session, was
  neither started nor instructed by it, and has edited none of the delta's
  paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-09-20 and
  re-pointed on 2026-09-24 with the prompt "Please deliver all fable dependent
  work, and work that would be best delivered using fable", on the Fable tier
  (`claude-fable-5-1`), orchestrating this batch of twenty rule-4 passes. It
  wrote this brief from the queue pointer, the landing commits' subjects and
  file lists, and the delta paths' names; it did not open the intent record or
  any prior verdict on these surfaces.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree, commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the `docs/SESSIONS.md` index entries of 2026-09-11 to 2026-09-19
  (the last three summarise the 2026-09-18 and 2026-09-19 runs in the authors'
  words); the first 30 lines and the last ~3,000 characters of
  `docs/sessions/2026-09-20-1053-queue-run-the-loose-ends.md`, read during an
  interrupted-session sweep on 2026-09-20; every queued `⏳` pointer on the board
  in full, including each pointer's own "lens that matters" paragraph — that
  paragraph is the author's framing and has been moved to this pass's sibling;
  the pass file `docs/reviews/2026-08-17-1000-coldsweep-cold.md` in full (brief
  and verdict) and lines 1–80 of
  `docs/reviews/2026-08-21-0820-pointing-up-cold.md`, both as formatting
  templates; the landing commits' subjects and `--stat` file lists (never the
  diffs); and, as doctrine read at onramp, `docs/method/CONCURRENCY.md` §§ *On a
  split board*, *Claiming at a dirty primary checkout* and *Surviving an
  interrupted session*, `docs/method/REVIEW.md` and `docs/method/00-APEX.md` at
  HEAD. Per-pass additions are marked ⚠️ under *Deferred reading*.

## What the work is

Landing commits (diff these; review the paths at HEAD):

- `501ec37` (2026-08-23) — the landing commit; it also carries the FR rulings'
  application to `tools/pathscan.py`, which is **outside** this pass's delta

Delta paths:

- `docs/decisions/0008-enforcement-is-called-not-copied.md` — the 2026-08-23
  amendment at the foot (AP1 truth re-word; AP2 list correction)
- `tools/floor.py` — the softenable-set docstring (note: the file was
  substantially edited on 2026-09-18 and 2026-09-20 by later, separately-queued
  work; review the docstring's claim as it stands at HEAD and name which later
  commit moved it, if any)
- `.github/workflows/floor.yml` — the two `env:`-routed signature steps (AP3)
- `tools/leakscan.py` + `tools/test_leakscan.py` — the explicit-terms-path error
  (AP4); the file was later rewritten to stream (2026-09-20), so check the AP4
  behaviour survived
- the queued board items `docs/roadmap/115-*/180-*.md` and
  `docs/roadmap/020-*/340-*.md` as the delta's own account of what it left open

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Whether the amendment says the truth about `main`'s boundary as it stands at
HEAD — re-read the live state (`gh api
repos/mike548141/atelier/branches/main/protection`, `gh api
repos/mike548141/atelier/rulesets`) rather than trusting the amendment's
description of it — and whether the `env:`-routed signature steps close the
injection shape they were written against or only move it. Whether the
softenable set the docstring describes is the set the registry actually enforces
(read `SOFTENABLE`/equivalent against every `Scanner` entry). Whether the AP4
error path in `leakscan.py` fires on the shape it names and on the neighbouring
shapes it does not. **Non-goal, and it does not fence the risk:** the
principal's rulings (AP1–AP8) are not under review — only their application in
text and code.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   The amendment claims a control clause can be *honest about not being
   enforced* and still be the thing that makes a floating `@main` call safe —
   test whether an appended amendment that contradicts the clause above it
   leaves a reader with one truth or two. Consider whether "not enabled,
   deliberately" is a state the ADR can carry without a review line of its own.
2. **Correctness & quality.** Diff `501ec37` for the in-scope paths only. Trace
   the two workflow steps: does routing an untrusted value through `env:`
   actually stop shell interpolation for every consumer of that step, including
   any `run:` that re-expands it? Run the leakscan tests; construct the AP4
   error case by hand with a path that does not exist, a path that is a
   directory, and an empty file, and say what each prints and exits.
3. **Completeness / harvest.** Every other surface that describes `main`'s
   boundary or the softenable set: `tools/README.md`, `CONTRIBUTING.md` (the
   repo's and the template's), `docs/build/REPO-STANDARD.md`, `SECURITY.md`, the
   `floorfleet` boundary row added 2026-09-18. Do they agree with the amendment,
   or does one still state the pre-amendment claim?
4. **Security & privacy** — mandatory. atelier is PUBLIC. The amendment names
   what is *not* protected on `main` — is that disclosure itself an exposure (it
   tells an attacker the branch accepts unsigned, unreviewed pushes from any
   collaborator) or is it the honest floor the doctrine requires? Say which, as
   counsel. Check the workflow steps for the OWASP injection class they were
   written against and for the `pull_request_target` / fork-secrets class beside
   it. The house security scanner reads the session's pending diff, and in this
   shared worktree that is other passes' drafts — it is **discharged by
   grounds** here (landed-delta review); say so in one line and deliver the
   code-altitude read by hand.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_leakscan tools.test_floor
  tools.test_precommit` at HEAD; the full Python suite once (`python3 -m
  unittest discover -s tools`) and note the count
- `python3 tools/floor.py --validate` (or the invocation `.githooks/pre-commit`
  actually uses — lift it, don't guess) on the hook plane
- the live boundary read named in *Scope*, with the output recorded (redact
  nothing — it is public API data about a public repo)
- the `env:`-routing claim: reproduce a value containing `$(…)` and backticks
  flowing through the step in a scratch workflow dry-run or by reading the shell
  the step generates

## House rules for this run

- You work in the shared review worktree
  `/Users/mike/worktrees/atelier-review-batch-0925` (branch
  `review-batch-0925`), read-only except for THIS brief file. Other reviewers
  are working there at the same time on their own briefs; never open another
  `docs/reviews/2026-09-25-0715-*` file — it is another pass's framing.
- Run **no git command that writes** in the worktree (no add, commit, stash,
  checkout, worktree, reset, clean). Read-only git (`log`, `show`, `diff`,
  `blame`, `branch -r`) is fine. Mutation probes, checkouts of older commits,
  scratch children and scratch linked worktrees go in your own clone: `git clone
  <worktree> <scratchpad>/<PREFIX>/probe` under the session scratchpad, named by
  your prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full Python suite
  (`python3 -m unittest discover -s tools`, in the foreground, ~minutes) at most
  once, never scan any tree outside the worktree or your scratch clone, and
  never point a scanner at the machine's other repos.
- `/security-review` is **discharged by grounds** for this batch: it reads the
  session's pending diff, which in the shared worktree is other passes' unstaged
  drafts, and this is a landed-delta review. State that line in your lens-4
  answer and deliver the code-altitude read by hand, checked against the OWASP
  catalogue where the work has a code surface.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" tree-wide,
  and would block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ
  English. Never quote a secret, a placeholder token, an email address or any
  personal detail — this repo is PUBLIC; describe, don't quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md`
(it carries the author's own lens hints), and:

- the verdict `docs/reviews/2026-08-09-0824-ep-application-cold.md` (the AP
  verdict and its § *Rulings — 2026-08-23*, which is this delta's intent record)
- `docs/reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md` (the EP
  verdict beneath it)
- `docs/ROADMAP-DONE.md` § *The EP application*

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `AR`: `AR1`, `AR2`, …) and severities (MAJOR / MODERATE
/ minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger with the commands and their results, and a follow-up checklist.
Then STOP and report to the orchestrator that phase 1 is written. Do not open
the sibling (it is not in the tree); do not edit the queue pointer, the board,
or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
records, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings on doctrine are the principal's to decide (rule 3): record all, apply
nothing; your counsel per finding is welcome, labelled as counsel and kept
beneath the finding.

---

# Verdict — phase 1, written 2026-09-25 (07:10–07:40 UTC)

## Provenance, repeated

- **Spawn.** A fresh Fable subagent (`claude-fable-5-1`, self-reported model id),
  spawned by the batch orchestrator with this brief as its only framing. I am not
  the author's session and was not instructed by it. Shape: reviewer-plus-
  orchestrator as the brief discloses; the orchestrator formed no finding.
- **Where.** The shared worktree `/Users/mike/worktrees/atelier-review-batch-0925`
  at `c4b9cd0`, read-only; probes ran in my own clone of it (same HEAD) under
  the session scratchpad. No git command that writes was run in the worktree.
- **What I read.** `docs/method/REVIEW.md` and `00-APEX.md` at HEAD; the
  `501ec37` diff for the in-scope paths, plus its `--stat` and — disclosed, since
  it is the author's narrative of *why* — its **commit message body**, which
  `git show` prints with the diff; every delta path at HEAD; the board items
  `115/180`, `020/340` and, surfaced by the cold sweep and not in the bar,
  the `140/*` group (`README.md`, `010`, `020`) — the last is the principal's
  ruling as the board records it and bears directly on lens 1, so I name it
  as author-adjacent exposure; `tools/floorfleet.py` (boundary row),
  `tools/signscan.py` (`commit_range`), `tools/leakscan.py` (terms loading),
  `tools/test_floor.py::SoftenableListsPinnedToRegistry`, the template caller
  `docs/build/templates/workflows/floor.yml`, the template `CONTRIBUTING.md`,
  `SECURITY.md`, `SIGNING.md` lines 55–75, `CHANGELOG.md` lines 60–80 and
  `.githooks/pre-commit`. Sweeps ran through `tools/coldsweep.py` with the
  brief's `--also-exclude`; `--include-barred` was never used.
- **Not opened.** `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`,
  every other `docs/reviews/` file (including every `2026-09-25-0715-*` sibling),
  the queue pointer `160/090`, and the `.deferred.md` sibling.
- **Tier.** Fable on both seats; the off-tier clause is not invoked.

## Lens 1 — approach and assumptions

Load-bearing assumptions, named first and then tested:

1. *An appended amendment can make a frozen ADR true.* Only if the amendment is
   itself true when written and the contradicted clause points forward to it.
   Neither holds here: the amendment was **false at its own recording commit**
   (AR1), and the 2026-08-06 clause above it carries no pointer down, so a
   reader at HEAD meets **three** accounts of the boundary — the 2026-08-06
   clause (three controls in force), the 2026-08-23 amendment (none in force,
   "no ruleset"), and the live API (an active ruleset, admin-bypassable). The
   code inherits the middle one: `floorfleet.py` cites the amendment's
   "warn-first on both planes" sentence as its ground for treating
   `required_signatures` as informational (AR2). One truth or two? Three.
2. *"Not enabled, deliberately" can be carried without a review line of its
   own.* The amendment carries none; the ADR's header line still reads
   "queued — pointer owed" (AR4). The queued pointer at `160/090` is the
   amendment's review line by the landing-equals-queuing rule, but nothing in
   the ADR says so; a reader of the record alone cannot find it.
3. *The live state was re-read at the amendment.* The text says "re-affirmed at
   this amendment". The ruleset the amendment denies was created
   2026-08-09T09:58Z and recorded on the board 2026-08-15 — eight days before the
   amendment. Either the re-read did not happen or it read the wrong endpoint.
   This is the apex's named defect — a claim stronger than its evidence, in a
   verified voice — on the one clause every child inherits at `@main`.
4. *AP4's principle is "explicit-but-missing is an error".* The ruling's
   principle as the docstring states it is wider: "never a quieter scan". The
   code applies it to one of four neighbouring shapes (AR3).

The non-goal (rulings not under review) does not fence the risk: every finding
below is on the *application* — text and code — not on what was ruled. Phase 2
will show whether AP1's wording was dictated; that changes attribution, not the
truth of the record.

## Lens 2 — correctness and quality

- **AP1.** Falsified by re-run — see AR1 and the ledger.
- **AP2.** The docstring at HEAD names the no-advisory set as secretscan,
  leakscan, conflictscan, linkscan, reviewscan, board, licenscan; the registry
  (`advisory is None`) gives exactly those seven. `020/340`'s pin test holds it
  (`test_floor.py:1705`). The `conflictscan` addition moved the paragraph on
  2026-09-18 (`6d2782f`); the claim survives. The ADR amendment's own list now
  lacks `conflictscan` (AR5).
- **AP3.** Traced and reproduced. Both `run:` blocks consume `$SIGN_BOUNDARY`
  double-quoted, once each; nothing re-expands it. A hostile value carrying
  `$(…)`, backticks, `;`, a glob and a leading dash reached `signscan` as one
  intact argv element and created no marker file in three shapes; the pre-AP3
  inline shape, emulated, fired the injection (marker files created). Residue in
  AR6.
- **AP4.** Fires on the named shape (missing `--terms` and missing env var: exit 2,
  message names the source and refuses the fallback). On the neighbours it does
  not: an **empty file** passes as "clean (structural + local)" with zero terms,
  even under `--require-terms`; a **directory** or an **unreadable file** is a
  raw traceback at exit 1; a **set-but-empty** env var or `--terms ""` falls
  through to the default list silently (AR3). `test_precommit`'s updated
  assertion matches the live message.

## Lens 3 — completeness and harvest

Surfaces that describe the boundary or the softenable set, checked at HEAD:

| Surface | State against the amendment |
|---|---|
| ADR 0008 lines 140–158 (2026-08-06 clause) | still states the pre-amendment claim; no forward pointer |
| ADR 0008 amendment (2026-08-23) | states a boundary that was already false when written (AR1) |
| ADR 0008 header `review:` line | "queued — pointer owed" after two passes (AR4) |
| `140/README`, `140/010`, `140/020` | record the ruleset (id, rules, bypass) and say the clause is still not true |
| `115/180` (delta) | "a ruleset … is the likely shape" written 14 days after the ruleset existed; closed BUILT 2026-09-18 |
| `floorfleet.py` boundary row | reads rule types only; cites the stale sentence; overclaims on green (AR2) |
| `floor.py` docstring | agrees with the registry (pinned) |
| `docs/build/templates/CONTRIBUTING.md` | agrees with the registry (pinned) |
| root `CONTRIBUTING.md` | does not exist in this repo — the brief's "the repo's and the template's" names one file that is not there |
| `docs/build/REPO-STANDARD.md`, `SECURITY.md`, `tools/README.md` | make no claim about `main`'s boundary or the softenable set; nothing to disagree |
| `SIGNING.md` line 65 | "branch protection is the compensating control" — the pre-amendment claim, unqualified |
| `CHANGELOG.md` 2026-08-06 and 2026-08-23 entries | dated history; the 2026-09-18 entry records the boundary row |

The amendment's "Until it lands, this clause is the truth" has lapsed: `115/180`
landed 2026-09-18 and no further amendment followed; `140/020` (open) is the
board's own account that the clause is still not true.

## Lens 4 — security and privacy

`/security-review` is **discharged by grounds**: it reads the session's pending
diff, which in this shared worktree is other passes' drafts, and this is a
landed-delta review. The code-altitude read was done by hand against the OWASP
Top 10 (A03 injection; A08 software and data integrity; A05 misconfiguration)
and the GitHub Actions hardening guidance for script injection.

- **Is the disclosure an exposure?** No — it is the honest floor, and it is
  *under*-disclosure. The boundary state is publicly readable **without a
  token**: `rules/branches/main`, `rulesets` and `rulesets/20603641` (including
  the bypass actors) all answered HTTP 200 unauthenticated; only the classic
  `branches/main/protection` endpoint is gated (401). An attacker reads more
  from the API than from the ADR. Counsel: keep disclosing, and disclose the
  true state (AR1).
- **Injection (A03).** Closed for `sign-boundary` by the `env:` route, proven
  above. Remaining inline expansion: `${{ github.repository }}` at line 192 — a
  platform-controlled value with a restricted alphabet, not caller input;
  acceptable, worth a one-line comment (AR6).
- **`pull_request_target` / fork secrets.** The reusable workflow has only a
  `workflow_call` trigger; the template caller triggers on `push`,
  `pull_request` and `workflow_dispatch` — no `pull_request_target`;
  `permissions: contents: read` on both; the gh-plane uses the read-only
  `github.token`. Clean, with the trail.
- **Integrity (A08).** The floating `@main` rests on the boundary. In force
  today: an active ruleset (`deletion`, `non_fast_forward`,
  `required_signatures`) with `bypass_mode: always` for the repository-admin
  role, and the account holding that role is the **only** collaborator (1) and
  has 2FA on (verified as a boolean, nothing more). So the ruleset guards
  against accident and third-party push; it does not bind the only actor who
  can push. That is what the principal ruled (`140/README`); it is not what the
  ADR says (AR1), and the machine check does not watch the bypass (AR2).
- **Privacy.** No personal detail in the delta; the amendment's "single-owner
  account" is the honest minimum. This verdict quotes no email, token or key.

## Findings

### AR1 — MAJOR (security) — the "true strength" amendment was false when written, and at HEAD

The 2026-08-23 amendment states: "A live read (2026-08-09, re-affirmed at this
amendment) shows … `main` carries no branch protection and no ruleset,
signature verification is warn-first on both planes … Branch protection is
deliberately **not** enabled." Re-run 2026-09-25: ruleset `20603641`
("main — the estate's guard supply chain (ADR 0008 control)") is `active` on
`~DEFAULT_BRANCH` with `deletion`, `non_fast_forward` and `required_signatures`;
its `created_at` is 2026-08-09T21:58:10+12:00 (09:58Z), `updated_at` the same
second, one history entry. The amendment landed 2026-08-23T05:54Z — fourteen
days later — and the board had recorded the ruleset, its id and the ruling
("ruleset with owner bypass, plus a machine-check") on 2026-08-15 (`a9abc26`).
Three of the amendment's factual claims fail: "no ruleset"; "branch protection
deliberately not enabled" (a ruleset is GitHub's current branch protection, and
one was enabled by ruling); "warn-first on both planes" (the server plane
requires signatures, bypassable by admin). The item it queues, `115/180`,
repeats the error ("a force-push/deletion-blocking ruleset … is the likely
shape"). The clause "Until it lands, this clause is the truth of the boundary"
lapsed on 2026-09-18 with no re-amendment. `140/020` (open, 2026-08-15) already
says the clause "is now closer to true and still not true" — so the drift is
known and queued, which lowers the urgency, not the severity: an ADR that every
child inherits at `@main` states, in a security-control clause, a state that
the public API contradicts, and its "re-affirmed" is an unverified claim in a
verified voice.

*Recurrence-prevention step (REVIEW.md's shape for a security finding):* any
amendment that describes live platform state carries the API read verbatim
(endpoint, timestamp, body) beside the prose, so the claim and its evidence
cannot part; and the machine row reads the bypass (AR2) so a widening is seen.

*Counsel, principal's call:* a second dated amendment beneath the first — never
an edit of it — stating the live state as read (ruleset id, three rules,
admin bypass `always`, single collaborator, 2FA), what that does and does not
protect against (accident and third-party push: yes; owner-token compromise:
no), and pointing at `140/020` as the vehicle; plus a one-line forward pointer
under the 2026-08-06 clause ("superseded — see amendments of 2026-08-23 and
<date>") so a reader meets one truth. Correct `115/180`'s close note the same
way. Reconcile with the AP verdict's rulings text in phase 2 before wording.

### AR2 — MODERATE — the boundary row overclaims on green and does not read the bypass

`floorfleet.classify_boundary` reads `rules/branches/main`, a flat list of rule
types, and prints on green: "main's ruleset blocks force-push and deletion".
For the only actor who can push it does not: `rulesets/20603641` reports
`bypass_actors: [{RepositoryRole 5, bypass_mode: always}]` and
`current_user_can_bypass: always`, and the collaborator count is one. The row
is measuring the control that was ruled ("with owner bypass"), so red/green is
right; the *sentence* is stronger than the evidence, and a later widening of
the bypass (another role, another actor) would leave the row green. The row's
docstring and header also cite the amendment's "warn-first on both planes" as
the reason `required_signatures` is informational — the stale sentence has
become code's authority. Live run: `('green', …)`; selftest ok.

*Counsel:* read `rulesets/{id}` for each id the flat list names, print the
bypass actors on the row, and word green as the ruling did — "blocks
third-party and accidental force-push/deletion; admin bypass: always". Ground
the informational choice in the ruling (`140/README`), not the amendment.

### AR3 — MODERATE — AP4 closes one of four neighbouring "quieter scan" shapes

Hand-constructed on the scratch clone, `--root .` on one doctrine file:

| Shape | Exit | What it printed |
|---|---|---|
| `--terms <missing>` / env `<missing>` | 2 | the AP4 refusal, naming the source |
| `--terms <directory>` / env `<directory>` | 1 | raw `IsADirectoryError` traceback, no remedy |
| `--terms <unreadable file>` | 1 | raw `PermissionError` traceback, no remedy |
| `--terms <empty file>`, with and without `--require-terms` | 0 | "✓ leakscan clean (structural + local)" |
| env `""` (set, empty) or `--terms ""`, with `--require-terms` | 0 | fell through to the default list silently |

The empty file is the dangerous one: a zero-byte list (a failed sync, a
truncated write) satisfies `--require-terms`, loads nothing, and the pass line
claims local cover — the exact "quieter scan reported as a pass" the ruling
names. The traceback shapes fail closed by accident and carry no remedy, which
is the "reaches for `--no-verify`" hazard `test_precommit` itself names. The
AP4 test pins only the first row.

*Counsel:* treat an empty explicit value as explicit and refuse it; catch
`OSError` at `load_local_terms` and exit 2 with the AP4 message shape; under
`--require-terms`, zero loaded terms is exit 2 (or at minimum the pass line
says "0 local terms"); pin all four shapes in `test_leakscan`.

### AR4 — minor — the ADR's own `review:` line never advanced

`docs/decisions/0008-…md:5` still reads "review: queued — `docs/reviews/`
pointer owed" after the EP pass (2026-07-26), the AP pass (2026-08-09), the
2026-08-06 addition and the 2026-08-23 amendment. `reviewscan` checks presence,
not currency. A reader meets an ADR that says its review is owed and two
amendments that apply rulings from reviews that ran. *Counsel:* the review line
is a status field, not frozen narrative; point it at the two verdict files.

### AR5 — minor — the pin test cites a sentence that does not exist; the "accepted" drift has begun

`test_floor.py:1716–1720` excludes ADR 0008 from the registry pin on the ground
"atelier's own CLAUDE.md: 'ADRs are frozen records'". `CLAUDE.md` contains no
such sentence (grep: no hit; `docs/decisions/README.md:38` speaks only of
records frozen before 2026-07-21). The exclusion may still be right — an
amendment is a dated statement — but a validator's stated ground should exist.
And the amendment's "at HEAD the … no-advisory set is secretscan, leakscan,
linkscan, reviewscan, board and licenscan" already lacks `conflictscan`
(2026-09-18); "at HEAD" in a frozen record reads as *this* HEAD. *Counsel:*
cite `RECORD.md`'s actual rule or drop the citation; in future amendments
write "as of <date>" rather than "at HEAD".

### AR6 — note — AP3 residue

(a) `${{ github.repository }}` is still expanded inline at `floor.yml:192`;
platform-controlled and alphabet-restricted, so not the injection class, but
the step comment should say why it is exempt from the AP3 rule. (b)
`signscan.commit_range` builds `f"{boundary}..HEAD"`; a boundary beginning
with `-` becomes a single option-shaped token — it must end in `..HEAD`, so no
real `rev-list` option matches, and the probe produced a clean usage error —
but `git rev-list --end-of-options` closes the class outright. (c) A malformed
boundary is exit 2 on the machine-key step even with `--warn`: environment
errors are not warned. That is the right behaviour and undocumented; the
"WARN-FIRST" comment should say the warn covers verification results only.

### AR7 — note — brief framing that did not survive contact

(a) The brief's re-run line `python3 -m unittest tools.test_leakscan …` cannot
import `test_leakscan` (it does a bare `import leakscan`); the working shape is
`discover -s tools -p test_leakscan.py`. (b) The orchestrator's environment
note said python3 is 3.9; the interpreter on PATH is 3.14.6 and no `python3.9`
exists on PATH, so nothing here was exercised under the hook's stated 3.9.
(c) The brief names "CONTRIBUTING.md (the repo's and the template's)"; only the
template exists.

## Overall

**FAIL — 1 MAJOR · 2 MODERATE · 2 minor · 2 note.** The AP1 application — the
delta's headline, "the boundary control stated at its true strength" — does
not reproduce: it was false at its own recording commit and is false at HEAD.
The AP2, AP3 and AP4 applications hold, with the MODERATE residue in AR2 and
AR3. Nothing here contests a ruling; everything is application.

## Re-run ledger

| # | Command / read | Result |
|---|---|---|
| 1 | `gh api repos/mike548141/atelier/branches/main/protection` | 404 "Branch not protected" (classic protection) |
| 2 | `gh api repos/mike548141/atelier/rulesets` | one ruleset, id 20603641, `active`, created 2026-08-09T21:58:10+12:00 |
| 3 | `gh api …/rulesets/20603641` | rules `deletion`, `non_fast_forward`, `required_signatures`; `bypass_actors` RepositoryRole 5 `always`; `current_user_can_bypass: always`; history: one version |
| 4 | `gh api …/rules/branches/main` | the same three rule types |
| 5 | `gh api …/branches/main --jq .protected` | `true` (rulesets count as protection) |
| 6 | `gh api …/collaborators --jq length` · `gh api user --jq .two_factor_authentication` | `1` · `true` |
| 7 | unauthenticated `curl` of items 2–4 | HTTP 200 each; `branches/main/protection` HTTP 401 |
| 8 | `python3 -m unittest tools.test_leakscan tools.test_floor tools.test_precommit` (scratch clone, 3.14.6) | Ran 153 in 155 s; 1 error — `test_leakscan` import (AR7a); floor + precommit passed |
| 9 | `python3 -m unittest discover -s tools -p test_leakscan.py` | Ran 134 in 22 s — OK |
| 10 | `python3 -m unittest discover -s tools` (once, 07:20:04–07:29:24Z) | **result not captured** — my `tail` caught buffered selftest stdout and my exit-code capture used bash syntax in zsh; not re-run under the one-run rule. Rows 8–9 cover the in-scope modules |
| 11 | `python3 tools/floor.py --plane hook --root <clone> --tools <clone>/tools` (lifted from `.githooks/pre-commit:82`; `--validate` does not exist) | exit 0; 12 enforced ✅, 3 warn-only 👁️; pathscan and pointerscan each report 1 advisory finding, sizescan 2 size-advisory |
| 12 | `python3 tools/floorfleet.py --selftest` · `floorfleet.read_boundary(Path('.'))` | ok · `('green', "main's ruleset blocks force-push and deletion (required-signatures: present …)")` |
| 13 | `env_probe.sh` (scratchpad `AR/`): hostile `SIGN_BOUNDARY` through both step shapes, stub and real signscan; inline shape for contrast | no marker files in the `env:` shapes; signscan exit 2 "git rev-list failed" (usage); the inline shape created both marker files |
| 14 | `ap4_probe.sh` (scratchpad `AR/`): nine terms-path shapes | table under AR3 |
| 15 | registry `advisory` per `Scanner` vs docstring list | seven `None` entries; docstring names the same seven |
| 16 | `coldsweep.py` (default bar + `--also-exclude` the pointer), patterns: branch protection, ruleset, advisory form, softened, warn-first | surfaces in the lens-3 table; no `--include-barred` |

## Follow-up checklist

- [ ] AR1 — principal rules on a second amendment + forward pointer; correct `115/180`'s close note; reconcile wording with the AP rulings text (phase 2)
- [ ] AR2 — `floorfleet` reads `rulesets/{id}` bypass actors; re-word the green line; re-ground the informational choice
- [ ] AR3 — `leakscan`: empty explicit value refused; `OSError` → exit 2 with remedy; zero terms under `--require-terms` → exit 2; four shapes pinned
- [ ] AR4 — ADR 0008 `review:` line pointed at the two verdicts
- [ ] AR5 — fix the pin test's citation; "as of <date>" phrasing in future amendments
- [ ] AR6 — comment on `github.repository`; `--end-of-options` in `signscan`; warn-scope comment
- [ ] AR7 — brief template's re-run line uses the `discover` shape; environment note corrected
- [ ] Phase 2 — reconcile against the sibling and the AP/EP intent records

### Reconcile — after receiving the sibling (2026-09-26, 14:17 UTC)

Phase 1 was committed unrevised at `d1ac3e0` before the sibling's text reached me.
Opened only then: `docs/reviews/2026-08-09-0824-ep-application-cold.md` in full from
its findings down (AP1–AP8, its reconcile, and § *Rulings — 2026-08-23*);
`docs/reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md` § EP7 and its
reconciliation; `docs/ROADMAP-DONE.md` § *The EP application*; and the queue
pointer `160/090`. Nothing else was opened; `docs/SESSIONS.md` and `docs/sessions/`
stayed closed. Nothing above is revised. One exposure to own: the `140/*` board
items I read in phase 1 carry the principal's 2026-08-09 ruling in the board's
words, so my phase-1 reading of the boundary was not formed blind to that ruling;
it was formed blind to the AP verdict and to the 2026-08-23 rulings text, which
is the bar rule 2 sets.

#### Per finding, against the intent records

- **AR1 — not anticipated; the falsity originates upstream of the application.**
  The AP verdict's AP1 (read 2026-08-09, roughly 08:24 UTC) said "no branch
  protection and no ruleset on `main`" — **true when read**: the ruleset's
  `created_at` is 2026-08-09T09:58Z, after the verdict. The board (`140/README`,
  2026-08-15) records the principal ruling that same day for "ruleset with owner
  bypass, plus a machine-check", chosen *over* re-wording, and applied the same
  day — the live ruleset matches that description exactly (id, three rules,
  admin bypass). Then § *Rulings — 2026-08-23* records AP1 ruled again, solo,
  as "re-word to the truth … branch protection is not enabled (it would break
  the direct-to-main workflow … the trade-off was put to him plainly)". So the
  2026-08-23 ruling's stated premise was already false by fourteen days and
  already contradicted by the board by eight. The application then wrote that
  premise into the ADR faithfully. **AR1 stands at MAJOR unchanged**; its
  attribution moves from the applier to the briefing of the 2026-08-23 round
  (AR8, below). The rulings text's "AP1 [fixed — truth amendment appended]"
  does not survive the close rule ("a finding is only closed when its fix is
  itself verified"): the amendment was not verified against the live state,
  and `140/020` (2026-08-15) already said "AP1 therefore stays OPEN".
- **AR2 — half anticipated.** AP1's counsel asked for exactly the row that
  landed ("a parent-row check reading branch-protection/ruleset state, red
  when absent"); the row does that. The bypass was not in AP1's counsel, but
  `140/020` names it as the control's limit ("never against compromise of his
  own token") — known on the board, not carried into the row's wording or its
  read. AR2 stands, MODERATE.
- **AR3 — the ruling's letter was applied; its class was not.** AP4 was
  narrowly "a set-but-missing `ATELIER_LEAKSCAN_TERMS` silently falls back";
  the ruling was "an explicitly-set terms path that does not resolve is an
  error". The code matches that letter. The empty-file case is EP3's class —
  the EP cycle's MAJOR on the hook plane's "full cover" being asserted, whose
  fix pinned "no list blocks rather than half scanning"; an empty list is half
  scanning with the list present. Lineage EP3 → AP4 → AR3; AR3 stands,
  MODERATE, and the lineage strengthens the counsel to pin all four shapes.
- **AR4 — not anticipated by either verdict.** Neither pass noticed the ADR's
  header line; both wrote rulings beneath a record that still says its review
  is owed. Stands, minor.
- **AR5 — a quiet narrowing of the ruling.** AP2 was ruled "queue the test
  that pins the **three** lists"; the delivered test pins two and excludes the
  ADR on a citation that does not exist. `020/340`'s close note discloses the
  exclusion honestly, which is why this stays minor rather than rising; the
  ground given for it should be a real one.
- **AR6 — AP3 applied as ruled; residues new.** The AP verdict's AP7 (the awk
  parse of `--list`) is the nearest sibling and is a different surface.
  Stands, note.
- **AR7 — the same class as the AP verdict's AP8**: brief framing that did not
  survive contact (there the suite-count claim; here the re-run invocation and
  the environment note). Two passes in a row; the brief template's re-run
  block is the place to fix it. Stands, note.

#### The seeded questions

1. *Does the amendment close EP7's counsel, or only AP1's instance?* Neither,
   at HEAD. EP7's counsel was to convert an accepted risk into a **named,
   checkable** control. The 2026-08-06 clause named one; AP1 found it not in
   force; the amendment re-named the controls in force — wrongly (AR1) — and
   funded the check. The check now exists (`floorfleet`, 2026-09-18), so
   "checkable" is met for `deletion` and `non_fast_forward`; "named" truthfully
   is not, and the bypass is neither named in the ADR nor read by the check
   (AR2). EP7 closes when a true statement of the control and a check that
   reads what the statement names exist together; today each half is
   somewhere else.
2. *Does the `floorfleet` row check the control the amendment describes, and
   does the amendment know the row exists?* It checks a **different** one. The
   amendment says `main` has no ruleset and branch protection is deliberately
   not enabled, so the control the amendment describes is the absence of one;
   the row checks the 2026-08-09 ruling's control (a ruleset blocking
   force-push and deletion) and reads the amendment only to justify treating
   `required_signatures` as informational. The amendment does not know the row
   exists (it predates it and was never re-amended); the row knows the
   amendment and inherits its stale sentence. `140/010` "Noticed" the mismatch
   at the build and routed it to `140/020`; the pointer under review lists
   `115/180` as queued, and it is closed BUILT under `140/010`.

#### Finding formed at reconcile

### AR8 — MAJOR (governance) — the 2026-08-23 AP1 ruling was taken on a stale briefing

Formed at reconcile, from the records only. Two rulings on AP1 stand in the
record fourteen days apart: 2026-08-09, "ruleset with owner bypass, plus a
machine-check" — chosen over re-wording — applied the same day (`140/README`,
corroborated by the live ruleset's creation time and shape); and 2026-08-23,
"re-word to the truth … branch protection is not enabled", whose recorded
premise the first ruling had already falsified. The apex conditions a ruling
on the principal being informed, and makes an under-briefed ruling
challengeable **on the briefing, by re-briefing and asking again** — never
void. The transcript of the 2026-08-23 round is outside my scope, so I cannot
say what was said aloud; what the record shows is a second ruling written down
without the first, and an ADR amendment that carries the second's premise.
Severity MAJOR because the mechanism is the apex's own informed-ruling
condition, on the estate's widest-blast-radius clause.

*Counsel, principal's call:* re-brief AP1 once, with the live read beside it
— the ruleset as it is, the bypass and what it does and does not cover, the
row as built — and ask which ruling stands; then the second amendment AR1
counsels records the answer. Recurrence-prevention: a ruling round's ask on a
finding that has a prior ruling on the board names that ruling in the ask.

#### Overall, restated

**FAIL — 2 MAJOR · 2 MODERATE · 2 minor · 2 note** (AR8 added at reconcile;
no phase-1 severity moved). The AP1 application does not reproduce and the
ruling it applied was under-briefed; AP2–AP4 hold with the residue recorded.

- [ ] AR8 — principal re-briefed on AP1 with the live read; the standing ruling
      named; the ask template names prior rulings

## Deferred material — folded in at reconcile

# Deferred material — ap-rulings-applied (open only after your findings are durably written)

Sibling of `docs/reviews/2026-09-25-0715-ap-rulings-applied-cold.md` under
REVIEW.md rule 1's split; held by the orchestrator outside the worktree. Folded
into the brief below the verdict when the verdict lands.

## Intent records

- `docs/reviews/2026-08-09-0824-ep-application-cold.md` § *Rulings — 2026-08-23*
  — the principal's dispositions AP1–AP8 in the wording he selected. **Not
  opened by the brief-writer.**
- `docs/reviews/2026-08-09-0824-ep-application-cold.md` (the AP verdict above
  the rulings) and
  `docs/reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md` (EP) —
  the two prior verdicts on these surfaces. **Not opened by the brief-writer.**
- `docs/roadmap/160-doctrine-review-owed/090-…` — the board item, which carries
  the author's summary of AP1 and AP2. **Read by the brief-writer** (it is the
  queue pointer); its summary is the author's, and the reviewer forms its own
  reading first.

## Prior verdicts and barred items on the same surfaces

- the verdict `docs/reviews/2026-08-09-0824-ep-application-cold.md` (the AP
  verdict and its § *Rulings — 2026-08-23*, which is this delta's intent record)
- `docs/reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md` (the EP
  verdict beneath it)
- `docs/ROADMAP-DONE.md` § *The EP application*

## The queue pointer's own lens hints — the author's seeded questions, verbatim

The pointer carries no lens paragraph — refs only.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

1. AP1 was classified at reconcile as a descendant of EP7. Does the amendment
   close EP7's counsel, or only AP1's instance of it?
2. The pointer lists `115/180` ("machine-check the main-branch boundary") as
   queued. At HEAD, `floorfleet` gained a `main`-ruleset row on 2026-09-18. Does
   that row *check the control the amendment describes*, or a different one —
   and does the amendment know the row exists?
