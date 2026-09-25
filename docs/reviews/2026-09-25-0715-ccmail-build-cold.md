# Cold pass — the `ccmail` build — a Gmail attachment fetcher, the layer's first third-party credential, and `ccpdf` beside it

**Pass type:** code + doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this batch's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-09-25 UTC; the review runs in the same batch
under the orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:**
`docs/roadmap/210-instruments-open-features/130-ccmail-rule-4-review-queued.md`.
**Why it earns a review:** this instrument holds a read-only grant on the
principal's mailbox and writes attachments to disk; it is the first instrument
in the layer to carry a third-party credential, so its design decides the
pattern every later one copies.

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

- `2d2890a`, `d2e8e60`, `5b0acf5`, `fd345ff` (2026-09-09) — the build, two
  quiet-failure fixes, the two-route resolver and the plaintext-store removal,
  and `ccpdf`
- `f99b479` / `1b8bbde` (2026-09-09) — records and the queue pointer (not delta)

Delta paths:

- `instruments/ccmail` (new) + `instruments/ccmail.test.js` (new, 25 tests) +
  `instruments/man/ccmail.1` (new)
- `instruments/ccpdf/` (new: renderer, `setup`, `selftest`)
- `instruments/README.md` — the layer table row and the `ccmail` and `ccpdf`
  sections
- `docs/decisions/0006-instruments-in-atelier.md` — the 2026-09-09 addendum (the
  layer's first third-party credential), the amendment and the third addendum
- `docs/roadmap/210-instruments-open-features/120-…` — the Drive finding filed
  beside it
- **Outside this repo, unreadable from it:** the machine-local
  global-instructions entries routing sessions to `ccmail`, and
  `~/.claude/ccmail.json` (the delta claims: identifiers only, no secret). The
  reviewer may verify the *no-secret* claim by reading that file and must quote
  nothing from it

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

The credential path end to end: where the grant lives, which route the two-route
resolver takes and why, what a compromised session on this machine could read
with it, and what the removed plaintext store was replaced by (verify the
removal at HEAD, and that no fallback re-creates it). What lands on disk under
`~/.cache/ccmail/`: attachments from arbitrary senders, unencrypted, with what
permissions and what lifetime. `ccpdf`: a renderer over untrusted PDFs — what
library, what sandbox, what it does with embedded JavaScript, links and forms.
The tests: do the 25 exercise the failure paths the build claims to have found
by reading, or only the happy path? ADR 0006's addendum: does the doctrine it
adds (a credential in the layer) state a rule a later instrument can follow, and
does it agree with `SECRETS.md` and `DATA-PROTECTION.md`? **Non-goals, neither
fencing the risk:** the principal's decision to build the instrument; the Drive
finding (filed, not built). ⚠️ **Privacy bound on the review itself:** the
mailbox is the principal's personal mail. The reviewer may run `ccmail --status`
and the selftests; it must **not** list, fetch or read any real message, and
nothing from the mailbox or the identifiers file enters the verdict.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. The
   build presumes a read-only delegated grant is the least privilege the job
   needs — test what "read-only" covers in that grant (labels, drafts, all
   mailboxes under the delegation, attachments of any size) against what the
   tool uses. Ask whether an instrument that writes personal attachments to a
   cache is the right shape at all, as counsel.
2. **Correctness & quality.** Read the whole of `ccmail` and `ccpdf`. Run `node
   --test instruments/ccmail.test.js` and the `ccpdf` selftest. Trace every exit
   path; construct the malformed inputs the two quiet-failure fixes name (from
   the diffs) and confirm the fixes hold at HEAD. Check the man page against the
   tool's actual flags.
3. **Completeness / harvest.** Does `instruments/README.md` tell a new session
   everything it needs (`--status`, where the cache is, how to clear it)? Does
   `SECRETS.md`'s registry or the estate-root's know this credential exists (the
   ADR claims a route — read the claim, name what you can and cannot verify from
   a public repo)? Does the Drive item beside it describe the same gap the build
   closed?
4. **Security & privacy** — mandatory. **This lens is the review.** OWASP-class
   read of a CLI that holds a mail grant: token storage and rotation, delegation
   scope, path traversal in attachment filenames written to the cache (an
   attachment named `../../x`), symlink following, cache permissions, size
   limits, MIME-type trust, `ccpdf`'s handling of hostile PDFs, what the tool
   logs and where. Check the design enumerated its threats before building
   (REVIEW.md lens 4's build-time obligation) — absent enumeration is a finding.
   The house scanner reads the session's pending diff, which here is other
   passes' drafts; it is discharged by grounds, and you deliver the read by
   hand. A confirmed security finding carries a severity and a
   recurrence-prevention step.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `node --test instruments/ccmail.test.js` and the `ccpdf` selftest; the full
  node suite once (`node --test instruments/*.test.js`)
- `ccmail --status` (read-only, no mailbox content) — record what it reports
  about the route and nothing else
- the path-traversal and hostile-name cases in *Scope*, against a scratch cache
  directory, with the network stubbed the way the tests stub it
- the plaintext-store removal: grep the tool at HEAD for any file write of
  credential material

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
`docs/roadmap/210-instruments-open-features/130-ccmail-rule-4-review-queued.md`
(it carries the author's own lens hints), and:

- `docs/sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md`
- the `docs/SESSIONS.md` entries of 2026-09-09

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-batch-0925 --also-exclude
docs/roadmap/210-instruments-open-features/130-ccmail-rule-4-review-queued.md
<pattern>` — rule 2's default bar, plus `--also-exclude` for the items above;
`--include-barred` only with disclosure in the verdict. Reading the *delta* is
never barred: the code, its tests, the doctrine text and the catalogue entries
are the subject. What is barred is the author's narrative of why, and the
verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `CC`: `CC1`, `CC2`, …) and severities (MAJOR / MODERATE
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
