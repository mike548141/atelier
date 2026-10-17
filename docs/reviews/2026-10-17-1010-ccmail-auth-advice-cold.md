# Cold pass — ccmail stops sending the operator to `--auth`

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/890-rule-4-cold-pass-queued-ccmail-auth-advice.md`.
**Why it earns a review:** it changes what a credential tool tells the operator to do,
and when it will mint a stored grant. Sessions relay that advice verbatim, so a wrong
line becomes a wrong instruction to a person; and the change arrived as a hand-up from
a private child into this public repo's instruments.

## Spawn provenance

- **Author of the work under review:** a session in a private child repo that filed the
  hand-up and wrote the change (the pointer's account; its own record stays private).
  The commit's trailer names an Opus model. Its intent record is the board item the
  pointer names, not opened here.
- **Who landed it:** the pointer says the 2026-10-17 review run landed it on `main` and
  authored none of it. That review run works in worktree `atelier-review-1017`, as this
  brief-writer's orchestrator does: by the pointer's account the orchestrator landed
  this delta. Disclosed so the taker can weigh it; landing is not authorship.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17
  by the Mike-opened Fable review session working in worktree `atelier-review-1017`, on
  Mike's 2026-10-16 answer that a fresh Opus session writes these briefs. It authored
  none of the delta. It is **off-tier for review, disclosed: it forms no finding and
  writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that passes
  rule 4's criterion and was not started or instructed by the filing session or the
  lander. If it runs as reviewer-plus-orchestrator, rule 4's off-tier conditions apply
  and are disclosed in the claim, the pointer and the verdict. The reviewer repeats its
  own provenance in its verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This brief-writer
  read: its instruction file, which named the landing commit's subject; the four queue
  pointers it was assigned (160/860–890) in full, and 160/500 in full as the shape of
  an append line (including that item's result line); the staging directory's file
  listing, and the first 50 lines of one peer brief of this batch (160/850) and its
  append, for shape; the landing commit's subject, `--stat`, full diff on the three
  delta paths **and message body** (the filing session's account); `instruments/ccmail`
  around its delegation route; grep-hit lines for `--auth` and "fallback" in the tool
  and `instruments/README.md`; three templates in full; `docs/reviews/` filenames and
  filename-level greps (no prior verdict opened); and its harness-loaded memory index.
  Writing the other three briefs of its set, it also read those deltas' diffs, message
  bodies and parts of their code, and grep-hit lines of a sweep that included single
  lines of board items 115/290 and 115/320. It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or `docs/method/REVIEW.md`. What its orchestrator read is the
  orchestrator's to disclose; it passed on an instruction file, three templates, a list
  of taken prefixes and the landing commit's subject, and no evaluative content.
  Everything evaluative is in the sibling.

## What the work is

Landing commit (diff it on the delta paths; review the paths at HEAD, `2f9cfe4` or
later):

- `019157c` (authored 2026-10-17 09:21 UTC, committed 09:22 UTC) — instruments: a
  hand-up from a private child — ccmail stops sending the operator to --auth. It is the
  commit that landed PR #108; it sits on `main`'s first-parent line with no merge
  commit.

Delta paths (the pointer's own list):

- `instruments/ccmail` — `delegationConfigured`, `keychainAbsentDetail`, the keychain
  branch of `resolveToken`, `cmdAuth`'s new delegation check and `--fallback`, the
  keychain route in `cmdStatus` (its `optional` field and the ➖ render), the help text,
  the argument parser and the exports
- `instruments/ccmail.test.js` — the four added tests
- `instruments/man/ccmail.1` — the Route 2 paragraph

The commit also added the intent record and this pass's pointer, and rebuilt the board
index; those are not the delta. No later commit touches the three paths (checked with
`git log 019157c..HEAD`); confirm that at your HEAD.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests and
live behaviour. The lenses organise it; they do not bound it. Non-goals are the only
narrowing and are themselves reviewable.

Probe, at least:

- **Every path through the two commands.** Tabulate `--auth` (delegation configured or
  not; live, lapsed, or failing for another reason; `--fallback` or not; with and
  without a terminal) and `--status` (text and `--json`; keychain empty, present or
  unavailable; delegation configured or not, live or not), and `resolveToken`'s message
  when both routes fail. For each: exit code, stream, and the instruction a session
  reading it would relay.
- **Is the advice right?** Where the new text names `gcloud auth login` as the fix,
  check it against every failure `delegatedToken` and `gcloudToken` can return (no CLI
  found, a lapsed login, a refused signing call, a wrong subject, a network failure).
  Which of them does a fresh login not fix?
- **The new flag.** `--fallback` is parsed globally. What does it do, or silently not
  do, beside the other modes? Is it in the man page's synopsis and the flag vocabulary
  section of `instruments/README.md`?
- **Order of operations.** `--auth` now tries the delegation route before the terminal
  check. What runs, and what reaches the network, when an unattended session calls
  `--auth`?
- **The JSON contract.** The keychain route gains `optional`. Who reads `--status --json`,
  and is the field documented?
- **The tests' isolation.** The end-to-end test points `HOME`, the config and the
  gcloud override at a temporary directory and empties `PATH`. Trace `gcloudBin`'s
  candidate list at HEAD and say whether the test can reach a real CLI, a real login or
  the network on a machine that has one installed.

**Non-goals:** the two-route design itself (delegation preferred, Keychain fallback),
which an earlier pass reviewed. How this change presents and gates the fallback is in
scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Among
   them: that a configured delegation means the fallback is never needed; that sessions
   relay status text verbatim, so wording is behaviour; that a hand-up from a child may
   land code in atelier's instruments with its review owed afterwards.
2. **Correctness & quality.** Read the delta functions and `cmdAuth`, `cmdStatus` and
   `resolveToken` whole; diff `019157c` on the three paths. Build the path table from
   *Scope*. Check whether the tests' cases cover each row or only the advice strings.
3. **Completeness / harvest.** `instruments/README.md`'s ccmail and install sections, the
   tool's header docstring, the help text against the man page (the drift guards the
   instruments suite runs), `CHANGELOG.md`, and any doctrine or skill that tells a
   session what to do when ccmail reports no route.
4. **Security & privacy** — mandatory. The change decides when the tool asks for a
   client secret and writes one to the Keychain. Can any input now skip a confirmation
   the old path had, or reach the fallback without the operator choosing it? This repo
   is PUBLIC and the change came from a private child: check the commit message, code
   comments, help text and man page for anything that names or points at the child, its
   mailbox, its people or its records. Describe, never quote. `/security-review` is
   discharged by grounds (a landed delta; the pending diff is not the work) — say so,
   and do the code-altitude read by hand against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift invocations from `.github/workflows/ci.yml` (the instruments
job) rather than guessing.

- `node --test instruments/ccmail.test.js`, then the whole instruments suite once as CI
  runs it (`node --test instruments/*.test.js`), foreground
- `mandoc -T lint instruments/man/ccmail.1`; `node instruments/ccmail --help` by path
- the path table, driven by path with `HOME`, `CCMAIL_CONFIG` and `CCMAIL_GCLOUD`
  pointing into your scratchpad and a stub `gcloud` script that simulates a live, a
  lapsed and an otherwise failing login; stdin not a terminal
- `019157c^` against `019157c` in a scratch clone over the same table, so the change in
  advice is shown, not asserted
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`, and
  the hook plane as `.githooks/pre-commit` invokes it)

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only git is
  fine. Probes, stubs and older checkouts go in a private clone under your session
  scratchpad, named by your prefix.
- **Never touch the real credential surface.** Never run ccmail against the machine's
  real config, Keychain, gcloud login or mailbox; never run `--auth` attached to a
  terminal; never run anything with a side effect. Never run an installed tool by bare
  name from `PATH`; instruments are symlinked onto it from another checkout.
- One heavy process at a time on a shared machine: the instruments suite at most once
  whole, in the foreground.
- `/security-review` reads the session's pending diff: discharge it by grounds for this
  landed delta, or keep the tree clean whenever you spawn it — never with this brief or
  its sibling dirty.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ English.
  Never quote a secret, placeholder token, email address, account, service-account name
  or personal detail — this repo is PUBLIC; describe and locate instead.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-17-1010-ccmail-auth-advice-cold.deferred.md`, the
landing commit's message body (the filing session's account; read subject, stat and
diff only), and the intent record:

- `docs/roadmap/210-instruments-open-features/270-ccmail-sent-the-operator-to-a-setup-he-did-not-need.md`

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/890-rule-4-cold-pass-queued-ccmail-auth-advice.md
--also-exclude docs/reviews/2026-10-17-1010-ccmail-auth-advice-cold.deferred.md
--also-exclude
docs/roadmap/210-instruments-open-features/270-ccmail-sent-the-operator-to-a-setup-he-did-not-need.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is
never barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then append
your verdict below a `---` divider in THIS file: provenance repeated (how you were
spawned, your tier, what you read), per-lens answers, the standing checklist V1–V7 each
answered or discharged with grounds, the path table, findings with stable IDs (prefix
`MA`: `MA1`, `MA2`, …) and severities (MAJOR / MODERATE / minor / note), an overall
PASS / PASS-WITH-FINDINGS / FAIL line with counts, a re-run ledger, and a follow-up
checklist. Then STOP and commit phase 1 unrevised before opening the sibling. Edit no
other file.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict: per-finding
notes against the seeded questions and the intent record, any finding formed at
reconcile marked as such, and the overall line restated. Never revise phase-1 text.
Then fold the sibling in below the reconcile and delete it.

Findings are the principal's to decide (rule 3): record all, apply nothing; counsel per
finding is welcome, labelled and kept beneath it.
