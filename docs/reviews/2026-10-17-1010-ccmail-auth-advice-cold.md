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

---

## Phase 1 — verdict (cold pass, Fable)

**Written:** 2026-10-18 00:32 UTC (`date -u`), after every probe below. Nothing in this
section is revised after the sibling is released; it has not been released at this point.

### Provenance (rule 4, V7)

- **Reviewer.** This session runs as `claude-fable-5-1` (Fable 5.1), the tier the principal
  named (ruling 2026-08-04). Tier was checked at selection; it matches, so the pass ran.
- **Spawn.** Spawned by a Mike-opened Claude Code **cloud** session (`claude-fable-5-1`,
  orchestrating; it opened on `claude-opus-5` and Mike switched it to Fable before any claim
  or pass). That session authored none of the delta or the brief and was not started or
  instructed by their authors. The orchestrator forms no finding and writes no severity; it
  holds the `.deferred.md` sibling outside the checkout at a path I was not given, commits
  this phase-1 file before releasing the sibling to me, and received one operational note
  from Mike's watching session (model, queue scope, container facts, merge instruction — no
  evaluative content about any delta). The claim line in the queue pointer discloses the
  same shape; I have not opened the pointer.
- **Author of the work** (the brief's account, not re-driven here): a session in a private
  child repo. **Lander:** the 2026-10-17 review run's orchestrator, by the brief's account.
  What the landing's record shows when re-driven is in MA4 and MA10.
- **Where I worked.** One checkout, `/home/user/atelier`, branch
  `claude/review-work-briefs-adj6ad`, HEAD `c9d8a0d` — a cloud container with one full
  clone, no worktrees, no sibling repos, no estate root. The branch adds only this run's
  review commits over `0aff4d8`; the local `origin/main` is `fe020b1`, one board-only commit
  beyond that (`320/710`) touching no delta path, so the delta at HEAD is the delta on
  `main`. No git command that writes was run in the checkout; this file is the only edit.
  Every probe, stub, fixture, log and the private clone live under `/home/user/scratch/MA/`.
  I did not use `/tmp` (the instruments suite itself writes its fixtures to `os.tmpdir()`).
- **Container facts that bear — two corrected from my dispatch.** (1) The dispatch said no
  gcloud CLI. **A real Google Cloud SDK is installed** at `/usr/local/bin/gcloud` (a symlink
  into `/opt/google-cloud-sdk`, bundled Python present), and the environment carries a
  proxy-issued `CLOUDSDK_AUTH_ACCESS_TOKEN`. I never ran `gcloud` by name or by path; that
  variable was removed from the environment of every probe and of both test runs, and one
  replay (P1, under MA3) ran with a marker string in its place. (2) `/root/.claude/` exists —
  the harness's own directory, not Mike's personal context; it holds no `ccmail.json`. So
  by construction no real ccmail config, Keychain, login or mailbox was reachable. Also:
  Node's `https` ignores the proxy and has **direct egress** — a probe `GET` was answered,
  DNS resolves the two Google endpoints, and four table rows sent my stub's constant
  "token" to Google's IAM signing endpoint, which answered 401 (no side effect; the
  service-account name was a placeholder). `gh`'s token is invalid; every GitHub read below
  was an anonymous `api.github.com` GET. `mandoc` 1.14.6, Node 22.22, Python 3.13.
- **What I read, in order.** `docs/method/REVIEW.md` whole; this brief whole;
  `docs/method/00-APEX.md` once. Then the delta: `git diff 019157c^ 019157c` on the three
  paths; `git diff c7f5b73^ c7f5b73` on the man page; `--stat --format=%s` of both and of
  `fe020b1`; `instruments/ccmail`, `instruments/ccmail.test.js` and
  `instruments/man/ccmail.1` whole at HEAD; `instruments/README.md` (flag vocabulary,
  install and ccmail sections); `CHANGELOG.md` head and its instrument entries;
  `docs/decisions/0006-instruments-in-atelier.md` lines 180–212; `.github/workflows/ci.yml`;
  `.githooks/pre-commit`; `tools/coldsweep.py`'s header; `tools/wrapscan.py`'s suffix scope;
  the siblings' drift-guard tests (`instruments/ccclose.test.js` 515–560). **Not opened:**
  the sibling, the queue pointer, the intent record (`210/270`), `docs/SESSIONS.md`,
  `docs/sessions/`, `docs/ROADMAP-DONE.md`, any other `docs/reviews/` file, and any commit
  message body — the landing commit's, `c7f5b73`'s and the PR head's (GitHub's commit JSON
  was parsed for files and dates only, never its message field).
- **Exposure, disclosed.** Sweeps ran through `tools/coldsweep.py` with the brief's three
  `--also-exclude` paths and never `--include-barred`. Hit lines unavoidably showed: the
  ROADMAP index line for `210/270` (its title and `✅` state) and for `160/890` (title);
  lines of roadmap items `210/120`, `210/130` and `210/140` — `210/130` names the earlier
  ccmail verdict's filename (`2026-09-25-0715-…`), which I did not open; ADR 0006 and
  TOOLBOX lines. `git log` subjects on this branch and on `main`'s first-parent line between
  `019157c` and `c7f5b73` were seen (other passes' verdict titles; two session-close
  subjects, one naming "the man-page lint red and its fix"). GitHub's PR object exposed
  PR #108's title (identical to the commit subject), state and timestamps; I did not read
  its body or comments.
- **`/security-review`** was not spawned: the pending diff here is this brief, not the work.
  Discharged by grounds (lens 4). The OWASP catalogue was read **from memory**; the host has
  not resolved for earlier reviewers and I did not attempt it.

### Lens 1 — approach and assumptions

Load-bearing assumptions, named before any seeded question was read, each attacked:

1. **A configured delegation means the fallback is not needed** (the brief lists it; the
   code encodes it as `delegationConfigured(cfg)`). *False by the repo's own doctrine.*
   ADR 0006 records the principal's re-ruling: a fallback is still owed, and "preferring the
   route that stores nothing is not the same as pretending the other is unnecessary"; the
   tool's header, the man page's Route 2 text and `instruments/README.md` all say route 2
   exists *because* the login lapses. The delta says the fallback is "not needed" whenever
   delegation is *configured* — including the exact states (lapsed, CLI absent, signing
   refused) the doctrine says the fallback is for. Rows S3m, S4m, S2m, R2m, R3m. → **MA1**.
2. **The fix for a failing delegation is `gcloud auth login`, nothing else** (code comment
   above `keychainAbsentDetail`; `cmdAuth`). *True for the lapse class only.* `delegatedToken`
   returns five distinct failures; a fresh login repairs one. → **MA2**.
3. **Sessions relay status text verbatim, so wording is behaviour.** *Confirmed, and it
   raises the stakes:* the sweep found no doctrine, skill or template telling a session what
   to do when ccmail reports no route. The tool's strings are the only layer there is.
4. **A hand-up from a child may land in `instruments/` with review owed afterwards.** The
   pointer was queued in the landing commit, so rule 4's landing = queuing holds. What the
   landing bypassed is another matter → **MA4**.
5. **`CCMAIL_GCLOUD` is an override** (the e2e test treats it as one). *False:* it is the
   first of four candidates and is skipped silently when its target does not exist; the man
   page documents it as "when it is not in the usual places". → **MA3**.
6. **The e2e test is isolated by `PATH`.** *False:* `gcloudBin()` tries three absolute
   paths before `PATH`. Replayed here, the test's environment executed the real SDK
   wrapper. → **MA3**.
7. **The fallback is reachable only by explicit operator choice.** *True:* every
   `--auth --fallback` row without a terminal died at the terminal check with zero gcloud
   calls (A6–A8); no environment variable or config value selects it.

The non-goal ("the two-route design itself") is honest narrowing. MA1 sits inside the
brief's stated scope: "how this change presents and gates the fallback".

### Lens 2 — correctness and quality

Read whole: `delegationConfigured`, `keychainAbsentDetail`, `resolveToken`, `cmdAuth`,
`cmdStatus`, `gcloudBin`, `gcloudToken`, `delegatedToken`, and `main`'s parser. The core
change does what it claims: where delegation is **live**, `--status` no longer shows the
keychain as a failure and `--auth` exits 0 saying it is not needed (L1–L3 new, against L2
old, which still printed "fix: ccmail --auth" beside a live delegation). The over-reach is
the predicate (MA1) and the generalised advice (MA2). Both binaries were driven over the
same table below; the change in advice is shown, not asserted.

Tests: four added. The three unit tests pin the strings; the e2e test pins one row and
passes for a reason other than the one its comment states (MA3). Not covered: the
`--fallback` bypass, the `➖`/`optional` render, lapsed-versus-other wording (MA11).

### Lens 3 — completeness / harvest

Man page at HEAD (with `c7f5b73`): the Route 2 paragraph is updated; SYNOPSIS, OPTIONS and
EXAMPLES are not, and now contradict it (MA5). `instruments/README.md`: two mirror sites
unswept (MA6). `CHANGELOG.md` records instrument behaviour changes by date and has no
entry for this one — nor any ccmail entry at all, so the gap predates the delta (MA6). The
`--status --json` field `optional` is undocumented and shape-inconsistent (MA7). ccmail's
suite lacks the man-page and help-versus-man guards its four siblings carry (MA5).
Nothing duplicated by the delta; the predicate it factored out still lives inline in two
older places (MA13).

### Lens 4 — security and privacy

- **Design altitude.** The change decides when a client secret is requested and written to
  the Keychain. *No input skips a confirmation the old path had:* the terminal check, the
  two interactive prompts and `saveCreds` are unchanged; the new pre-check only adds an exit
  *before* them. *Nothing reaches the fallback without the operator choosing it:*
  `--fallback` must be typed (A6–A8). One new exposure of a different kind: an unattended
  `--auth` now runs the gcloud subprocess and two outbound POSTs before the terminal check
  (MA9) — read-only, the same calls `--status` makes.
- **Public-repo check** (described, never quoted): the diff, the comments, the help text and
  the man page name no child repo, mailbox, person or record. The one pronoun for the
  operator refers to the published author. The test fixtures use non-address placeholders.
  A grep for address-shaped and host-shaped strings over the three files and over the diff
  found none. The floor's leakscan ran on both planes: the hook plane refused for want of
  the user-local term list (`115/350`, expected); the CI plane's structural cover was clean.
- **Code altitude, OWASP Top 10 from memory.** A03 injection: `r.why` (gcloud's stderr) and
  Google's error text are interpolated unescaped into the advice — multi-line, as P1 shows;
  a readability defect, not an execution path. A05 misconfiguration: `CCMAIL_GCLOUD`'s
  semantics and the inherited `CLOUDSDK_*` environment (MA3). A07 authentication failures:
  gating unchanged, as above. A08 integrity: a test executing an unexpected real binary
  (MA3). A10 SSRF: the endpoints are constants. A01/A02/A04/A06/A09: no surface in this
  delta.
- **Confirmed security finding, with its two marks:** MA3 (severity MODERATE; the
  recurrence-prevention step is in the finding). It sits in tooling this repo ships for
  others; whether it routes through `SECURITY.md`'s private path is the principal's call —
  nothing is remotely exploitable; a test can touch a local credential CLI.

### Standing checklist

- **V1** — three claims stronger than their evidence: the test's comment (MA3), the "not
  needed" line (MA1), the brief's "landed PR #108" (MA10).
- **V2** — re-run ledger below. The landing commit's implicit "the floor is green" was
  false at its own commit (MA4).
- **V3** — the changed rule was not swept to SYNOPSIS/OPTIONS/EXAMPLES (MA5), to the README
  (MA6), or to the CHANGELOG (MA6).
- **V4** — the delegation predicate now has three homes (MA13).
- **V5** — the delta contradicts ADR 0006, the header, the man page and the README (MA1);
  the man page contradicts itself (MA5).
- **V6** — lens 4 above; `/security-review` discharged by grounds.
- **V7** — provenance above, repeating the brief's and the dispatch's accounts.

### The path table

Environment for every row: `HOME`, `CCMAIL_CONFIG` and `CCMAIL_GCLOUD` into scratch; stdin
`</dev/null`; the container's gcloud token removed; `PATH=/usr/bin:/bin` so no installed
gcloud is reachable by name. gcloud is a stub reached only through `CCMAIL_GCLOUD`: *live*
prints a constant token; *lapsed* exits 1 with a reauthentication message; *other* exits 1
with an unrelated error; each stub logs its calls. Rows suffixed **m** force
`process.platform` to `darwin` through a preload so the macOS-only keychain strings render
(`security` is absent, so the keychain reads as empty). Rows **N** inject a socket error
into `https.request`; rows **L** answer the three endpoints with canned 200s so the "live"
branch can be observed — that proves ccmail's branching, not Google. "New" is HEAD; "old"
is `019157c^`'s `instruments/ccmail`, extracted into scratch and run by path. Full logs:
`/home/user/scratch/MA/logs/table-{new,old}.log`, `extra-{new,old}.log`, `p1.err`.

`--auth`, no terminal:

- **A1** no delegation → new **1**, stderr: needs a terminal, run `ccmail --auth` yourself.
  Old identical. Relayed: "run it in your shell". Correct.
- **A2** delegation configured, gcloud live, signing refused (Google's real 401) → new **1**,
  stderr: not the fix here … *Delegation failed (Google's text) — try* `gcloud auth login`,
  then `--status`; or `--auth --fallback`. Old **1**: needs a terminal (no gcloud call, no
  network). Relayed: "run gcloud auth login" — **wrong fix** (MA2).
- **A3** delegation, login lapsed → new **1**: *the Google Cloud login has lapsed — run*
  `gcloud auth login`. Old: needs a terminal. Relayed: correct.
- **A4** delegation, gcloud fails otherwise → new **1**: *Delegation failed (gcloud failed:
  its stderr) — try* `gcloud auth login`. Old: needs a terminal. Relayed: **wrong** (MA2).
- **P1** the e2e test's exact environment (`PATH=/nonexistent`, `CCMAIL_GCLOUD` naming a
  missing file) on this host → new **1**: *Delegation failed (gcloud failed:
  /usr/local/bin/gcloud … readlink: not found … exec: python: not found) — try* `gcloud auth
  login`. The **real SDK wrapper ran** (MA3); the advice carries its error dump.
- **N1** delegation, network refused → new **1**, stderr: the bare socket error — no advice,
  no `--fallback` hint. Old **1**: needs a terminal (never reached the network).
- **L1** delegation live end to end → new **0**, stdout: already live for the subject via
  delegation — `--auth` is not needed. Old **1**: needs a terminal. The intended fix.
- **A6/A7/A8** `--auth --fallback`, any state → new **1**: needs a terminal, **zero gcloud
  calls** (the pre-check is skipped, as designed). Old **1**: unknown option.

`--fallback` elsewhere:

- **F1** `ccmail --fallback` alone → new **0**, prints the help text. Old 1: unknown option.
- **F2** `--status --fallback` → new: identical to `--status`; the flag is ignored silently.

`--status`, text and `--json` (exit 1 whenever no route is live, in both forms):

- **S1/S1j** no delegation, Linux → ❌ delegation not configured in the config path;
  ❌ keychain unavailable off macOS; JSON `optional: false`. Old: same text, no field.
- **S1m/S1mj** no delegation, macOS → ❌ keychain *nothing stored yet — fix: ccmail --auth*;
  `optional: false`. Old identical (minus the field). Relayed: "run ccmail --auth" — the one
  state where that is right.
- **S3m/S3mj** delegation **lapsed**, macOS → ❌ delegation *the Google Cloud login has
  lapsed — fix: gcloud auth login*; **➖** keychain *not set up — not needed, the delegation
  route is configured*; `optional: true`. Old: ❌ keychain *nothing stored yet — fix: ccmail
  --auth*. Relayed new: "gcloud auth login" (right) **and** "the fallback is not needed",
  while the tool is dark (MA1).
- **S4m** delegation fails otherwise, macOS → ❌ delegation *gcloud failed: its stderr* (no
  fix offered); ➖ keychain *not needed*. Old: ❌ keychain *fix: ccmail --auth*. Relayed new:
  **no actionable instruction at all** (MA1, MA2).
- **S2m** gcloud live, signing refused, macOS → ❌ delegation *could not sign as the
  workspace identity: Google's text*; ➖ keychain *not needed*. Same shape as S4m.
- **S2/S3/S4 (+j)** the same states on Linux → ➖ keychain *unavailable off macOS*; the `➖`
  glyph and `optional: true` appear off macOS too, where no fallback could exist.
- **N2/N3** network refused → new and old alike: **1**, stderr the bare socket error, **no
  route table and no JSON** — the exception escapes `cmdStatus` (pre-existing).
- **L2/L3** delegation live → **0**: ✅ live via the delegation route; ✅ delegation keyless;
  ➖ keychain *not set up — not needed…*; `optional: true`. Old **0** but ❌ keychain
  *nothing stored yet — fix: ccmail --auth* — the defect the change exists to fix, shown.

`resolveToken`'s both-fail message (via `--search`, reached before any API call):

- **R1m** no delegation, macOS → *stored grant — nothing stored yet — fix: ccmail --auth*
  (old wording: *nothing in the Keychain yet (fix: ccmail --auth)*).
- **R2m** lapsed → *delegation — the Google Cloud login has lapsed (fix: gcloud auth login)*
  / *stored grant — not set up — not needed, the delegation route is configured*.
- **R3m** other failure → *delegation — gcloud failed: its stderr* / *stored grant — not
  set up — not needed…* — no fix anywhere in the message.
- **R1–R3** Linux → *stored grant — unavailable off macOS* (unchanged). **N4** network
  refused → the bare socket error (unchanged).

Not drivable here, traced instead: a **present** Keychain grant (needs macOS `security`);
the "CLI not on this machine" branch — unreachable on any host with gcloud at one of the
three hardcoded paths, which is MA3's point; a **terminal-attached** `--auth` (barred by
the brief, rightly).

### Findings

**MA1 — MAJOR.** The new "not needed" predicate is *configured*, not *live*, and the
shipped text now contradicts the repo's recorded doctrine on the fallback's purpose.
`keychainAbsentDetail(delegationConfigured(cfg), …)` and `optional: delegated` fire in every
state where delegation is configured — lapsed (S3m), failing (S4m), refused (S2m) — and in
the both-fail message (R2m, R3m). In those states the tool says the fallback is "not
needed" at the moment the tool is dark, which ADR 0006 (lines 206–210, the principal's
re-ruling) says not to do: a fallback is still owed, and preferring the route that stores
nothing "is not the same as pretending the other is unnecessary". The header comment (lines
32–35 and 186–189), the man page (117–119) and `instruments/README.md` (619–621) carry the
same rationale. The grounding incident was a **live** delegation; the fix gates on
**configured**. Both call sites already know liveness (`resolveToken` holds `r.ok`;
`cmdStatus` holds the delegation route's `live`), so the narrower predicate costs nothing.
Lens 1, V1, V5. *Why MAJOR and not FAIL:* the change's core case is right and shown; the
predicate over-reaches into the states the doctrine reserves for the fallback.
*Counsel (labelled; the principal's to decide):* either (a) gate the "not needed" wording
and `optional` on the delegation route being **live**, with a neutral "not set up" (no
`--auth` advice) when delegation is configured but down; or (b) if the estate's stance is
now "where delegation is configured, a lapse is fixed by re-login and the fallback is for
estates without delegation", amend ADR 0006, the header, the man page and the README
together so one fact has one home. Either resolves the contradiction; (a) is the smaller
change and keeps the recorded ruling.

**MA2 — MODERATE.** `--auth`'s advice says `gcloud auth login` for every non-lapse
delegation failure. `cmdAuth` branches only on `r.expired`; its else-branch prints
"Delegation failed (…) — try gcloud auth login" for: the CLI not found or its wrapper
crashing (P1); a refused signing call (A2 — in the real world a missing token-creator grant
or a wrong service-account name); a delegation not registered for domain-wide delegation;
and a token-exchange failure. A fresh login repairs none of them. "Try" hedges; a session
relays the imperative. A network failure (N1) escapes as a bare exception with no advice
and no `--fallback` hint — new on the `--auth` path (the old `--auth` never reached the
network), pre-existing on `--status` and `resolveToken` (N2–N4). Meanwhile `--status`'s
delegation line offers a fix only for the lapse class, so the non-lapse rows (S4m, S2m,
R3m) carry **no** instruction where the old text carried a wrong one. Lens 2; assumption 3
makes this behaviour, not prose. *Counsel:* print `gcloud auth login` only when
`r.expired`; for the other classes name the remedy the code already knows (the CLI path
and `CCMAIL_GCLOUD` for a missing CLI; the Admin-console path for `unauthorized_client`;
"check the service-account name and your IAM grant" for a signing refusal); catch the
network error in `cmdAuth` and `cmdStatus` and report it as a route failure, not a crash.

**MA3 — MODERATE (security lens; recurrence step below).** The end-to-end test can execute
a real `gcloud`, and its isolation holds by accident. `gcloudBin()` consults `CCMAIL_GCLOUD`
only if that path **exists**, then `~/google-cloud-sdk/bin/gcloud`, `/opt/homebrew/bin/
gcloud` and `/usr/local/bin/gcloud`, and only then `PATH`. The test sets `CCMAIL_GCLOUD` to
a missing file and `PATH` to `/nonexistent`, and inherits the whole `process.env`. Replayed
here with the test's exact environment (P1), ccmail selected and **ran**
`/usr/local/bin/gcloud`; the SDK's shell wrapper then died because `readlink`, `dirname`
and `python` were not on the stripped `PATH`, so no token was printed and nothing left the
host — the wrapper's dependence on coreutils, not the test's design, and the wrapper's
error dump became the advice string the test then matched. On a macOS host with Homebrew's
gcloud the same real binary runs. A host whose gcloud at a candidate path survives an
empty `PATH` (a native build, or a wrapper handed `CLOUDSDK_PYTHON` and coreutils by
absolute path) would print whatever credential the inherited environment supplies — this
container's environment carries a `CLOUDSDK_AUTH_ACCESS_TOKEN` — and ccmail would POST it
to Google's IAM endpoint, which rows A2/S2 show is reachable directly from Node. The test
comment ("no gcloud on PATH: the route fails") is therefore false in mechanism (V1), and
the assertion `/gcloud auth login/` cannot tell "not on this machine" from "ran and
failed". CI at `c7f5b73` was green, consistent with the runner having no gcloud at those
three paths; the runner's layout was not verified here (relayed from memory).
*Severity:* MODERATE — real-CLI execution demonstrated; credential egress reachable by
construction, not demonstrated. *Recurrence prevention, for the class:* make an
**explicitly set** `CCMAIL_GCLOUD` authoritative (set and missing → "the configured gcloud
path does not exist", never a fall-through), so a test or an operator can pin the tool;
point the test's `CCMAIL_GCLOUD` at a stub that exits non-zero and strip `CLOUDSDK_*` from
the child environment; assert the branch that ran (the "not on this machine" text), not
the shared advice. Routing through `SECURITY.md`: the principal's call; the defect is local
to a host running the suite, not remotely exploitable.

**MA4 — MODERATE.** The delta landed with the CI floor red and stayed red for ten hours, and
the landing bypassed a red PR check. Re-driven from GitHub's anonymous API and `mandoc`:
PR #108's own two runs (push and pull_request, 2026-10-16T22:22Z) **failed at the "man
page lint" step**; `mandoc -T lint` on the man page at `019157c` exits 1 (STYLE: line 107 is
89 bytes, over the 80-byte limit) and exits 0 at HEAD. The PR was **closed unmerged**
(2026-10-17T12:12Z); its content reached `main` as a re-authored direct push, `019157c`
(authored 2026-10-17T09:21Z; the instrument trees are byte-identical to the PR head — a
`git diff` between them on `instruments/` is empty). Every `main` run from `8acfff1`
(2026-10-17T09:23Z, the push that carried the landing) to `8a8569a` (19:38Z) concluded
failure or cancelled — the two I opened failed at "man page lint" — until `c7f5b73` (19:43Z)
went green. `ci.yml` says this floor "gates publication, not just the merge", and the repo
is public. The pre-commit hook could not have caught it: the hook plane runs `floor.py`'s
scanners only, `wrapscan` covers `.md` files only (line 564), and the man-page lint exists
in CI alone — a plane mismatch for a file class the instruments layer ships. This is a
finding on the **landing**, which the brief discloses was the orchestrator's act, not on
the child's authorship. *Recurrence prevention:* a floor check that runs `mandoc -T lint
instruments/man/*.1` on the hook plane where `mandoc` is present (macOS ships it), honestly
declared where it is not; and a rule that PR content is not re-pushed to `main` while the
PR's own check is red. *Counsel:* `c7f5b73` is a sound fix; what is owed is the gate, and
a record of why the red stood.

**MA5 — MODERATE.** The man page at HEAD contradicts itself on the delta's own subject.
SYNOPSIS (line 5) lists `ccmail --auth` with no `[--fallback]`; OPTIONS `--auth` (184–186)
still reads "One-time interactive setup. Refuses to run without a terminal rather than
half-completing" — with delegation configured it is neither (L1 exits 0 without a terminal;
A2–A4 exit 1 after a network round trip); OPTIONS has no `--fallback` entry; EXAMPLES
(312–318) opens with `ccmail --auth` then `--status` as "Set up once on this machine" — the
exact instruction the change exists to stop sessions relaying, on the page `--help` calls
"the full reference". Only the Route 2 paragraph was updated. `ccmail.test.js` has none of
the man-page guards its four siblings carry ("a man page ships and is well-formed roff";
"every flag `--help` prints appears in the man page") — though, honestly, the siblings'
superset guard would pass here, because `--fallback` does appear in the Route 2 prose; the
gap it would not catch is section placement. `--allow-repo-dest` is likewise absent from
SYNOPSIS (pre-existing). V3, V5. *Counsel:* `[--fallback]` in SYNOPSIS; an OPTIONS entry;
rewrite the `--auth` entry to the new behaviour; open EXAMPLES with `--status` and point
delegation estates at `gcloud auth login`; add the sibling guards, extended to check
SYNOPSIS and OPTIONS.

**MA6 — minor.** Mirror sites not swept. `instruments/README.md` 133–137 ("where the
delegation route is unavailable, `ccmail --auth` mints…") and 619–621 (route 2's rationale)
say nothing of `--auth` refusing where delegation is configured, or of `--fallback`; the
rule changed in one home and not the other (V3). `CHANGELOG.md` records instrument
behaviour changes by date (cctranscript, ccclose, ccarchive entries) and has no entry for
this one; it has **no ccmail entry at all**, so the omission predates the delta and the
delta continued it. ADR 0006 line 186 ("`--auth` needs a terminal and a browser … no agent
session can perform it") remains true of the minting path and needs no edit.

**MA7 — minor.** `--status --json` gained `optional` undocumented and shape-inconsistent:
present (`true` or `false`) only on the keychain object when the keychain is empty, absent
when a grant is stored, absent on the delegation object. No consumer exists in the repo
(swept); the man page's `--json` entry says "available on every mode" and no schema for
the status object is documented anywhere. Off macOS the field is `true` whenever
delegation is configured, though no fallback can exist there (S3j, S4j). *Counsel:*
document the object once (man page, `--status`), make the field always present, and gate
it per MA1.

**MA8 — minor.** `--fallback` is parsed globally and ignored silently outside `--auth`:
`ccmail --fallback` alone prints the help text and exits 0 (F1); `--status --fallback`
behaves as `--status` (F2). `--allow-repo-dest` has the same shape, so this is precedent,
not novelty; but this flag gates a credential-minting path, and a flag that does nothing
in most positions teaches sessions it is harmless. *Counsel:* reject `--fallback` without
`--auth`, as `--limit` already rejects a bad value.

**MA9 — note.** Unattended `--auth` now spawns gcloud and makes two outbound POSTs (IAM
signJwt, token exchange) *before* the terminal check, and exits 0 with a success line when
delegation is live (L1); the old `--auth` never reached the network without a terminal
(old A2, L1). Read-only — the same calls `--status` makes — and arguably the right answer
to a session that was told to run `--auth`. Recorded because it reverses the man page's
"refuses to run without a terminal" and because a network-side failure now reaches a path
with no handler (MA2). The live line prints the delegated subject (a mailbox) to stdout —
the pattern `--status` already has; not a repo leak.

**MA10 — note (brief provenance).** The brief says `019157c` "is the commit that landed
PR #108". GitHub records PR #108 as **closed, not merged**; its head `7be5b3f` is not an
ancestor of `019157c` or of `main`; `019157c` is a separately authored commit (new author
date) carrying identical instrument content plus the pointer and the board rebuild. The
substance is right; the record should say "its content landed as a re-authored direct push
and the PR was closed unmerged", or a later reader checking GitHub will find the brief
wrong. The brief's "no later commit touches the three paths" was true when written and is
superseded at HEAD by `c7f5b73` (disclosed at claim).

**MA11 — note.** Coverage against the table: the unit tests pin the strings; the e2e test
pins one row and matches both branches of the advice. Untested, and observed here:
`--auth --fallback` skipping the pre-check (A6/A7: zero gcloud calls); the `➖`/`optional`
render (S3m, L2); lapsed-versus-other wording (A3 against A4). Each is one spawn with a
stub `CCMAIL_GCLOUD`, cheap once MA3's pin exists.

**MA12 — note.** `c7f5b73`'s wrap left a three-word source line ("API, set up")
mid-paragraph; roff renders it identically, so cosmetic. The `.TH` date stays 2026-09-09;
the five pages disagree among themselves on whether `.TH` tracks edits (ccarchive and
ccrepo match their last change; ccclose and cctranscript do not), so no convention is
breached.

**MA13 — note (V4).** The predicate "delegation is configured" now has three homes:
`delegationConfigured(cfg)` (line 102), and the same three-field test inline in
`resolveToken` (357) and `cmdStatus` (757). Harmless today; a fourth config field would
diverge them. *Counsel:* call the helper at both sites.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 4 MODERATE · 3 minor · 5 note** (MA1–MA13).
Not FAIL: the grounded case — a live delegation no longer sends the operator to `--auth` —
is correctly built, tested, and shown against the old binary. The MAJOR is the predicate's
over-reach into the states the recorded doctrine reserves for the fallback; under the
close rule a MAJOR keeps the cycle open.

### Re-run ledger

- `node --test instruments/ccmail.test.js`, by path, token removed, `CLOUDSDK_CONFIG`
  pointed into scratch → **30/30 pass**.
- `node --test instruments/*.test.js`, once, foreground, same containment (as CI) → 447
  tests: **431 pass, 16 skipped, 0 fail**, 23 s.
- `mandoc -T lint instruments/man/*.1` at HEAD (as CI) → **exit 0**.
- `mandoc -T lint` on the man page at `019157c` (private clone) → **exit 1**, STYLE, line
  107, 89 bytes.
- `node instruments/ccmail --help` by path → exit 0; help flags against the man page:
  `--fallback` in the page, **not** in SYNOPSIS or OPTIONS; `--allow-repo-dest` not in
  SYNOPSIS (pre-existing).
- Path table, HEAD binary: 29 stub rows + 7 fault-injected → logged, summarised above.
- Path table, `019157c^` binary (blob extracted into scratch), same rows → logged;
  differences stated per row.
- P1, the e2e test's exact environment with a marker token → the real SDK wrapper
  executed and died on the stripped `PATH`; no token printed; no network.
- `python3 tools/floor.py --plane ci --root .` at HEAD → **exit 0** (secretscan: 23
  advisory, none in the delta paths; leakscan: "cover not guaranteed", structural only).
- `python3 tools/floor.py --plane hook --root . --tools ./tools` at HEAD → **exit 1**:
  leakscan refuses without a local term list (`115/350`, expected); every other check
  green.
- Brief: "no later commit touches the three paths" → **false at HEAD**: `c7f5b73`.
- Brief: "landed PR #108; first-parent line, no merge commit" → first-parent: yes. PR
  closed unmerged; instrument trees identical to the PR head.
- Brief: who landed it → **not re-driven (relayed)**; the commit's author and committer
  identity is the published one.
- CI history around the landing (anonymous API) → PR runs failed at "man page lint";
  `main` red 2026-10-17 09:23Z–19:43Z; green at `c7f5b73`.
- Python tool suite (`tools/test_*.py`) → **not run**: no `tools/` change in the delta; CI's
  run at `c7f5b73` succeeded.
- macOS Keychain behaviour; the estate's real delegation; the CI runner's gcloud layout →
  **not re-driven here (relayed)**: no macOS, no estate, no authenticated platform read.

### Follow-up checklist (the principal's to decide; nothing applied)

- [ ] MA1 — choose (a) gate on live or (b) amend the four doctrine sites; then sweep.
- [ ] MA2 — per-class remedies in `cmdAuth`; catch the network error in both commands.
- [ ] MA3 — authoritative `CCMAIL_GCLOUD`; stub-pinned e2e test; strip `CLOUDSDK_*`.
- [ ] MA4 — man-page lint on the hook plane; no direct push of red-PR content.
- [ ] MA5 — SYNOPSIS, OPTIONS, EXAMPLES; the sibling guards for ccmail.
- [ ] MA6 — README mirror sites; a CHANGELOG entry (and ccmail's missing history).
- [ ] MA7 — document and stabilise the status JSON.
- [ ] MA8 — reject `--fallback` without `--auth`.
- [ ] MA10 — correct the landing account in the record that carries it.
- [ ] MA11, MA13 — tests for the observed rows; one home for the predicate.
