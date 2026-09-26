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

---

## Verdict — phase 1 (written 2026-09-26T14:31Z)

### Provenance, repeated

- **Spawned by** the batch orchestrator (`claude-fable-5-1`), not by the author of the
  work. I am a fresh subagent with this brief as my only framing; I was neither started
  nor instructed by the session(s) that landed `2d2890a`…`fd345ff`. The orchestrator
  holds the deferred sibling outside the worktree and forms no finding.
- **Tier:** `claude-fable-5-1`, checked at spawn.
- **Where I worked:** the shared worktree at `f81a98f` when I began; the branch advanced
  to `999e354` while I worked (other passes' verdicts). Verified by `git log` that no
  delta path changed between the two. My scratch clone (for the floor) is at `c19ae9a`.
- **What I read (in scope):** this brief; `docs/method/REVIEW.md`, `00-APEX.md`,
  `SECRETS.md`, `DATA-PROTECTION.md`; every delta path in full (`instruments/ccmail`,
  `ccmail.test.js`, `man/ccmail.1`, `ccpdf/{pdfrender.swift,setup,selftest}`,
  `instruments/README.md` §§ install and `ccmail`/`ccpdf`, ADR 0006 whole,
  roadmap 210/120); the full diffs of `5b0acf5` and `d2e8e60`; `--stat` of all four
  landing commits; greps of `.githooks/pre-commit`, `tools/floor.py --help`,
  `.github/workflows/ci.yml`; three Google documentation pages (scopes, native-app
  OAuth, domain-wide delegation) fetched 2026-09-26.
- **Outside the repo, disclosed:** the machine-local identifiers file (shape only, via a
  script that printed key names, types and lengths — no values); the live cache
  directory (modes, counts, total size — no names, no contents); the cloud CLI's user
  credential store (existence, mode and byte size of two files — nothing opened); the
  machine-local global instructions were *injected* into my context at spawn as system
  context, not opened by me — they route sessions to `ccmail` and match the README.
- **Rule-2 exposure, disclosed:** a memory index injected at spawn carried two one-line
  entries touching this work (that a keyless delegation identity pre-existed, and to
  check a private registry before minting credentials). I did not open those files. No
  barred path was opened; every sweep ran through `tools/coldsweep.py` with
  `--also-exclude` for the queue pointer and the sibling briefs (347 files excluded).
- **Privacy bound, honoured:** no message was listed, fetched or read. `ccmail --status`
  ran once with addresses masked in my shell; only its route lines are recorded below.
  One planned probe (a locked-Keychain read) was **not run** because it would touch the
  real Keychain item's service name; recorded under CC11 as reasoned, not probed.

### Lens 1 — approach and assumptions (named by me, then attacked)

- **A1 — `gmail.readonly` is least privilege for the job.** Holds at Google's
  granularity: the scopes page (fetched 2026-09-26) offers no narrower scope that returns
  attachment bytes; `gmail.metadata` excludes bodies and so attachments. But the grant is
  wider than the four calls the tool makes (`messages.list`, `messages.get`,
  `attachments.get`, `getProfile`): it also reads labels, drafts and mailbox *settings*
  (filters, forwarding, delegates). The docs say "read-only" and never say "wider than
  used". Recorded, not a finding — there is no tighter grant to take.
- **A2 — "The delegation route stores nothing."** True of `ccmail`; **false of the
  route.** It authenticates from the cloud CLI's user credential, which on this machine is
  a long-lived refresh token in a plaintext SQLite file under the home directory (mode
  600, 20 KB — existence and mode checked, nothing read). That is the artefact class the
  same ruling banned. → **CC1**.
- **A3 — "Keyless" answers the domain-wide objection.** It answers half. The ADR's own
  first text names the other half — "it can be pointed at any mailbox in the domain" —
  and the amendment does not weigh it. Google's delegation page (fetched 2026-09-26)
  describes access "on behalf of multiple individual users in your organization" and
  names no per-user restriction. → **CC1**.
- **A4 — A disk cache outside every repo is the right shape.** Counsel: the *shape* is
  right — paths not bytes is the correct answer to the context-window cost — but the
  cache is a store of other people's data and is not protected like one. → **CC2**.
- **A5 — The fallback route keeps the tool from going dark.** Unmet in practice at
  review time: both routes are down and the fallback has never been minted. → **CC10**.
- **A6 — A stand-in `pdftoppm` on PDFKit is safe to point at mail attachments.** The
  parser is Apple's and is patched with the OS; the draw path has no script engine. But
  the renderer has no size cap and no sandbox. → **CC4**.
- **Brief framing attacked:** "25 tests" — the suite is 26. "The 2026-09-09 addendum" —
  ADR 0006 carries *two* 2026-09-09 addenda plus an amendment; the second's heading says
  "third" where the count makes it the fourth (CC7).

### Lens 2 — correctness and quality

- Whole of `ccmail` (1,011 lines) and `ccpdf` read; every exit path traced: `die` → 1;
  `--status --json` without a live route → 1; unhandled rejections → `die`. The suite
  passes 26/26; the full instruments suite 277/277; `mandoc -T lint` clean.
- **The two quiet-failure fixes (`5b0acf5`) hold at HEAD by reading:** `unzipList`
  carries `maxBuffer: 32 MB` (line 513); the consent server carries the five-minute
  timeout (lines 684–688). Neither is re-driven — one needs a multi-megabyte container,
  the other five minutes of wall clock and a real consent — and the author said so in
  the commit. The `metadataHeaders` fix (`d2e8e60`) is re-driven by its own test.
- **Man page versus flags:** two claims are false at HEAD and one is loose → **CC7**.
- **Write path defects found by probe:** silent overwrite on duplicate or colliding
  names; a mid-batch crash on a long extension → **CC6**.
- Honest about scope: the sidecar's first line declares extraction; `--search` is
  labelled the fallback; off-macOS storage refuses rather than degrades. Good.

### Lens 3 — completeness and harvest

- `instruments/README.md` tells a new session `--status` (line 132) and where the cache
  is (line 575). It does **not** say how to clear the cache, nor does the man page —
  folded into **CC2**.
- The ADR's claim that the delegation facts "were already written down in the estate's
  own registry" **cannot be verified from this public repo** and names no path — which is
  correct for a public record. I did not open any private registry. What can be verified:
  the identifiers file holds a comment (41 words of prose), a service-account address and
  a mailbox address, and nothing token-shaped. **No secret**, as the delta claims.
- The Drive item (210/120) describes the same gap class — bytes reachable in principle,
  unusable in practice — and grades its own evidence honestly ("read, not measured").
- `SECRETS.md`'s standing-credential list: not addressed → **CC9**.
- `ccpdf`'s selftest is not in CI (ubuntu runner, no `swiftc`); the ADR's "verified by
  live use" stance matches the `browser-fetch` precedent. The installed binary is the
  same byte-size as a fresh build from HEAD and passes the selftest.

### Lens 4 — security and privacy (this lens is the review)

**`/security-review` is discharged by grounds:** it reads the session's pending diff,
which in this shared worktree is other passes' unstaged drafts, and this is a
landed-delta review. The read below is by hand against the OWASP Top 10 (2021):

- **A01 access control** — path traversal: held (19 hostile names, 0 escapes). Symlink
  following and a symlinked `--dest` bypassing the repo guard: **CC5**. Domain-wide
  reach: **CC1**.
- **A02 cryptographic/credential storage** — route 2 in Keychain, no plaintext write of
  credential material anywhere in the tool (grep: the only `writeFileSync` calls are the
  attachment and the sidecar, lines 860/869; `CCMAIL_CREDENTIALS` survives only as the
  ADR's superseded control text). Route 1's real secret is plaintext outside the tool:
  **CC1**. Cache at rest world-readable: **CC2**.
- **A03 injection** — query parameters escaped (test re-run); all child processes are
  `spawnSync` with argument arrays, no shell string; the message id is spliced unescaped
  into the URL path and the destination path: **CC5**.
- **A04 insecure design** — no threat enumeration in the delta: **CC3**. No render size
  cap: **CC4**. No attachment size cap — bounded in practice by Gmail's inbound limit
  and a 256 MB `maxBuffer` on extraction; recorded, not a finding.
- **A05 misconfiguration** — cache modes: **CC2**.
- **A06 vulnerable components** — `--text` hands attacker-controlled containers to
  Apple's Info-ZIP 6.00 (2009); `ccpdf` hands attacker-controlled PDFs to PDFKit
  unsandboxed. Both are OS-patched; noted under **CC4/CC11**.
- **A07 authentication** — loopback consent without `state` or PKCE: **CC8**.
- **A09 logging** — nothing is logged to disk by the tool. Subjects, senders, dates and
  the account address are printed to stdout, i.e. into the session transcript, which
  `ccarchive` then preserves. That is the design's stated data flow, recorded here so it
  is not invisible.
- **A10 SSRF** — every host is a constant; no input reaches a hostname. Held.

### Findings

**CC1 — MAJOR (doctrine; rule 3 — the principal's to decide).** The delegation-first
ruling of 2026-09-09 rests on a picture that is incomplete in two ways the delta does not
state. (a) Keylessness removed the key-file objection but not the blast radius the ADR's
own first text named: with a fresh cloud login, whoever can run a shell as this user can
mint `gmail.readonly` tokens for **any mailbox the identity delegates over**, not one.
(b) "Stores nothing" is a property of `ccmail`, not of the route: it authenticates from
the cloud CLI's user refresh token, a plaintext file under the home directory — the class
the same ruling banned. Route 2, by contrast, reaches one mailbox but its refresh token
and client secret are liftable by any process running as the user with one `security`
command (no dialog, by design — line 147) and remain valid off-machine until revoked.
Neither route's "what a compromised session on this machine can read with it" appears
in the ADR, README or man page — and that line is what the brief asked for. The apex
conditions rulings on being informed; this one is challengeable on the briefing.
*Recurrence prevention:* the ADR's controls list for future credential-holding
instruments gains a required line — *what a compromised session on this machine can
read with it, per route* — so the omission is caught at the next instrument's ADR.
*Counsel (labelled):* re-brief the principal with (a) and (b) in plain language. Options:
(i) keep delegation-first and record the exposure as a stated bridge, with the
delegation identity on the standing-credential list; (ii) flip to personal-grant-first —
one mailbox, revocable from the account page, at the cost of one Keychain secret;
(iii) in either order, make `ccmail` refuse a `subject` that differs from the cloud
login's own identity — defence in depth for this tool only, honest that the raw token
is untouched. My recommendation: (i)+(iii) if the domain holds one human mailbox;
(ii)+(iii) if it holds more. I do not know which, and did not look.

**CC2 — MODERATE (security/privacy; design).** Attachments from arbitrary senders land
under `~/.cache/ccmail/` as world-readable files in world-readable directories (umask
022 → directories 755, files 644 — checked on the live cache: 1 message directory,
6 files, 1.8 MB, oldest 2026-09-09), with no lifetime, no retention rule, no `--clear`,
and no README or man-page line on clearing them. `DATA-PROTECTION.md`: "never move it
somewhere less protected". Mail behind an authenticated mailbox becomes plaintext on
disk indefinitely. *Recurrence prevention:* `mkdirSync(..., { mode: 0o700 })` and
`writeFileSync(..., { mode: 0o600 })`, a test asserting the modes (the `ccarchive`
signing-key test is the in-repo precedent), a documented clear (`rm -rf` line or
`--clear`), and a stated retention posture in the man page's FILES section.

**CC3 — MODERATE (security; build-time obligation).** No threat enumeration exists in
the delta. The code answers three threats in comments (repo destination, plaintext
store, content into the context window) and `safeName` answers traversal; nothing names
who or what attacks the surface, so hostile Office containers, hostile PDFs, cache
exposure, compromised-session reach and consent CSRF were never listed and mostly not
answered (CC1, CC2, CC4, CC8). REVIEW.md lens 4: absent enumeration is the finding. The
barred intent record may hold one; to reconcile in phase 2. *Recurrence prevention:* a
threat list in the ADR addendum for any instrument that holds a credential or opens
attacker-supplied bytes.

**CC4 — MODERATE (security; `ccpdf`).** The renderer has no bound on bitmap size and no
sandbox. Probed against a fresh build from HEAD: a one-page PDF whose only hostile
property is a 100,000-point MediaBox, at the reader's fixed 100 dpi, ran **104 s at
4.4 GB resident** before failing at finalise; a 14,400-point page rendered a 10,000 px
square (0.8 GB resident); `-r 100000` on a tiny page was OOM-killed. The MediaBox is
sender-controlled and mail is the input. JavaScript `OpenAction` and `Launch` actions
rendered with exit 0 and no observed side effect — PDFKit's draw path has no script
engine — so that half of the brief's question is clean. *Recurrence prevention:* refuse
above a pixel budget with a named error (poppler's own behaviour is the reference), and
consider a `sandbox-exec` profile for a process whose whole input is untrusted.

**CC5 — minor (security).** Three write-path gaps, all probed: (a) a symlink in the
destination is followed — a pre-placed link named like the attachment redirects the
write to any file the user can write (probe D overwrote a victim file); (b)
`insideGitWorkTree` resolves but does not `realpath`, so a `--dest` reached through a
symlink into a repo bypasses the guard (probe E); (c) the message id is spliced
unvalidated into both the URL path and the destination path (`../../escape` resolves
outside the cache base — probe F; the repo guard still runs on the result). The man
page's own example, `--dest /tmp/valuations`, points at the shared sticky `/tmp` where
(a) is the classic vector. *Recurrence prevention:* open with the `wx` flag, `realpath`
before the guard, validate the id against `^[0-9a-f]+$`.

**CC6 — minor (correctness).** Same-name attachments silently overwrite (probe B: two
`image.png` → one file, second content); sanitised names collide (2 of 19 hostile names
mapped to the same file); a name whose *extension* exceeds 180 characters throws
`ENAMETOOLONG` mid-batch — earlier files are written, later ones are not, and the error
names no attachment (probe C). *Fix shape:* suffix on collision, cap the extension too,
and continue past a failed write with a `warn` line as the no-data path already does.

**CC7 — minor (docs versus behaviour).** (a) Man page: "a bare `--get` means all" —
at HEAD `ccmail <id> --get` dies "--get needs a value", and `--get --text` consumes
`--text` as the selector and then fails as "nothing matches" (probed; no network).
(b) `--status`: "One live API call" — it makes up to five and mints the delegated token
twice (lines 725 and 756). (c) A partially-missing selector (`1,99`) silently drops the
miss; the man page promises only that a total miss errors. (d) README line 571 points
`ccmail` at "ADR 0006's third addendum"; the ADR labels the *ccpdf* addendum "third"
(by count it is the fourth). (e) The brief's "25 tests" is 26.

**CC8 — minor (security; auth).** The loopback consent sends neither `state` nor a PKCE
`code_challenge`; Google's native-app guidance (fetched 2026-09-26) marks both
"Recommended" for exactly this flow. Any local process that reaches the port first ends
the consent (login-CSRF or denial). Human-run, once per machine, so minor. *Recurrence
prevention:* add both — about fifteen lines — and assert them in a test of the URL.

**CC9 — minor (doctrine/completeness).** `SECRETS.md`'s triad makes a standing
credential "a tracked debt to shorten" with a stated reason on a list. Route 2's refresh
token and route 1's cloud-login credential plus delegation identity are standing; the
ADR names re-mint and revoke paths but no list entry. And the ADR's four-controls list
(lines 163–179), which it says a future instrument "inherits as the precedent", still
presents the 0600-file fallback as "the documented fallback" while the amendment below
removes it. *Counsel:* one pointer line in the list ("withdrawn by the amendment below");
one line in the private registry naming the two standing credentials and their reason.

**CC10 — MODERATE (live behaviour).** At review time (2026-09-26T14:15Z) `ccmail
--status` reported **no way in**: the delegation route "the Google Cloud login has
lapsed", the Keychain route "nothing stored yet". The ADR's reason for keeping route 2 —
the tool "cannot be dark for a day" — is unmet because the human `--auth` step was never
performed on this machine, and every session the global instructions route to `ccmail`
fails at the door. Not a code defect; an operational one, and the doctrine's stated
guarantee is unmet seventeen days after landing.

> 🎯 **For Mike:** run `ccmail --auth` once (a terminal and a browser), and/or refresh the
> cloud login — then `ccmail --status`. Until then no session can open an attachment.

**CC11 — note (tests and thin layers).** Untested at HEAD: the network layer, resolver
fall-through, the whole `cmdGet` write path, and both `5b0acf5` fixes (author-stated).
The `insideGitWorkTree` test's first assertion is tautological on macOS (`realpath`
differs, so it compares the call to itself); the second line does the work. `walkParts`
keeps a filename-bearing part that has neither id nor data (probe H) — `cmdGet` would
then fetch `/attachments/null`, die at 404 and abandon the batch after partial writes.
An attached `.eml` is never fetchable whole, only its inner parts. `request()` has no
timeout. `xmlText` decodes decimal but not hex entities (probe I). A right-to-left
override character passes `safeName` untouched, so a listed name can display reversed.
A Keychain read that fails for any reason other than absence (exit 44) is reported as
"nothing stored yet" (lines 134–137) — reasoned from code, deliberately not probed.

**CC12 — note (harvest, clean).** The Drive item describes the same class as the gap
closed and grades itself honestly. The installed `pdftoppm` matches HEAD's build and
passes the selftest. The identifiers file holds no secret. `setup` refuses to shadow a
real poppler and installs only after the selftest passes (read; the install path was
not re-run because a binary already exists there).

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR (CC1), 4 MODERATE (CC2, CC3, CC4, CC10), 5 minor
(CC5–CC9), 2 notes (CC11, CC12).** The tool's three central claims hold under probe —
no traversal, no plaintext credential write, no repo destination — and the code is
careful where it looked. What it did not look at is the ruling it rests on (CC1), the
cache it fills (CC2) and the renderer it feeds (CC4); those are design findings, and
CC1 is the principal's to re-decide, informed. The cycle stays open on CC1.

### Re-run ledger

| Claim / probe | Command (abridged) | Result |
|---|---|---|
| Unit suite | `node --test instruments/ccmail.test.js` | 26/26 pass |
| Full instruments suite | `node --test instruments/*.test.js` | 277/277 pass |
| Man page lints | `mandoc -T lint instruments/man/ccmail.1` | clean, exit 0 |
| CI-plane floor | `floor.py --plane ci`, clone `c19ae9a` | exit 0; 2 warn-only, off-delta |
| Python suite | `unittest discover -s tools` | **not run** — no Python in delta; see note |
| `ccmail --status` | live, addresses masked | both routes down (CC10); exit 1 |
| Identifiers file | key names/types/lengths only | 3 keys; nothing token-shaped |
| Plaintext store removed | coldsweep, env name + `0600` | ADR old text; `ccarchive` key only |
| Hostile names | probe A/A2, 19 names, scratch cache | 0 escapes; 2 collisions |
| Duplicate names | probe B | second silently overwrites first |
| Long / multibyte names | probe C | long extension throws `ENAMETOOLONG`; 170 CJK chars ok |
| Symlink in dest | probe D | followed; victim overwritten |
| Symlinked `--dest` into repo | probe E | guard returns null (bypassed) |
| Message id as path | probe F | `../../escape` resolves outside base |
| Arg parsing | bare `--get`; `--get --text`; `--bogus`; `--limit 0` | dies; swallowed; dies; dies |
| `ccpdf` build + selftest | `swiftc` from HEAD; selftest fresh + installed | both pass; same size |
| Hostile PDF: JS + Launch | `-jpeg -r 100` on a fresh build | exit 0, no side effect |
| Hostile PDF: truncated | as above | exit 1, "could not open" |
| Hostile PDF: 100,000 pt box | as above | 104 s, 4.4 GB RSS, then exit 1 |
| Hostile PDF: 14,400 pt box | `-r 50` | 0.8 GB RSS, 10,000 px file written |
| Caller dpi `-r 100000` | tiny page | OOM-killed (exit 137) |
| Scope coverage | Google scopes page, 2026-09-26 | no narrower attachment scope |
| PKCE/state guidance | Google native-app page, 2026-09-26 | both "Recommended" |
| Delegation reach | Google delegation page, 2026-09-26 | "multiple individual users"; no limit |
| Keychain absent exit | `security find-generic-password -s ccmail -w` | exit 44 |

Probe scripts: `scratchpad/CC/names.js`, `scratchpad/CC/pdfprobe.sh`. The two heavy
PDF probes ran longer and larger than intended on a shared machine (104 s, 4.4 GB; one
OOM kill); recorded so no one repeats them to confirm CC4 — the numbers are the proof.

### Follow-up checklist

- [ ] CC1 — re-brief the principal (what/why/impacts/options/recommendation) on the two
      unstated facts; record the ruling in ADR 0006; add the per-route exposure line to
      the controls list.
- [ ] CC2 — cache modes 700/600 with a test; documented clear; retention line in FILES.
- [ ] CC3 — threat list in the ADR addendum; reconcile against the intent record.
- [ ] CC4 — pixel budget with a named error in `pdfrender.swift`; sandbox considered.
- [ ] CC5 — `wx` open flag, `realpath` before the guard, id validation.
- [ ] CC6 — collision suffix, extension cap, continue-past-failure with `warn`.
- [ ] CC7 — man page: bare `--get`, `--status` call count, partial-miss wording; README
      addendum reference; ADR addendum numbering.
- [ ] CC8 — `state` + PKCE on the loopback consent, with a URL test.
- [ ] CC9 — standing-credential list entry (private registry); pointer line in the ADR.
- [ ] CC10 — `ccmail --auth` on this machine (Mike); re-check `--status`.
- [ ] CC11 — tests for the write path and the no-id part; `request()` timeout.

### Reconcile (phase 2, written 2026-09-26T21:09Z)

**What was opened, in order, after phase 1 was committed (`aa0916c`):** the sibling's
text (by message from the orchestrator); the intent record
`docs/sessions/2026-09-09-0005-…`; the three `docs/SESSIONS.md` index entries of
2026-09-09; the queue pointer 210/130; and — beyond the sibling's named record, disclosed
— `docs/sessions/2026-09-09-0257-the-credential-that-already-existed.md`, because the
index entry showed it is the session that made the re-ruling and the "proven end to end"
claim the second half of the delta rests on. No prior *verdict* on these surfaces exists
to open. Nothing above phase 1's divider or in phase 1 has been revised.

**The seeded question — cache clearing and lifetime: tool's gap, docs' gap, or design?**
Neither intent record mentions the cache's permissions, lifetime or clearing; the 0005
record's controls are paths-not-content, the repo guard and sanitised names, and stop
there. So it is an **unconsidered gap, not a design choice** — the tool's first (modes,
no clear, no retention), the docs' second (nothing to point a session at). Phase-1 CC2
already carries it, and the reconcile sharpens the evidence: the 0257 record says six
PDFs were fetched from a real message during testing on 2026-09-09, and the live cache at
review time holds one message directory and six files dated 2026-09-09 (counts only).
The test run's attachments have sat world-readable for seventeen days because nothing
says they should not. The brief-writer's own instructions noticing the gap is a second
independent sighting; CC2 stands at MODERATE.

**Author claim 1 — "the live Gmail round trip is proven end to end via the delegation
route."** Holds **as recorded on 2026-09-09**: the 0257 record lists `--status` live,
six PDFs fetched and two rendered and read. It does **not** hold at review time —
`--status` on 2026-09-26 found the delegation route lapsed and no fallback minted (CC10).
The same record predicted the lapse ("a cloud login that lapses — six transcript hits
since July") and said the stored grant "is still owed", then closed with "nothing for
the mail path — it works now, with no setup". The proof was true for its hour; the
record's own reasoning said it would not stay true, and the one action that would have
kept it true was not listed as owed. → CC13 below.

**Author claim 2 — "five defects, found by reading and by an adversarial selftest, none
by use."** Holds as recorded: `metadataHeaders`, the `unzipList` buffer and the consent
timeout by re-reading; PNG-for-every-flag and `-aa` by the selftest. The records' class
statement — every defect "in a thin layer between this code and something else" — is
also borne out by this pass in the direction the author feared: CC5 (filesystem: symlink
following, `realpath`), CC6 (filesystem: name collisions, `ENAMETOOLONG`), CC7(a) (the
argument parser) and CC4 (the OS renderer's memory) all sit in exactly those layers, and
all were found **by use** — driving the write path and the renderer with hostile inputs
— which is the method the records say the build did not apply. The 0005 record calls
the read's timing "luck rather than method"; this pass is the method.

**Per finding — anticipated by the records, or not:**

- **CC1 — stands, MAJOR; the records strengthen it.** The 0005 record recorded the case
  against domain-wide as two facts: "it can also be pointed at **any mailbox in the
  domain** and its key is a file." The 0257 record overturned the ruling on the second
  fact alone ("false here, and it was the deciding sentence") and never revisits the
  first. It also states the "stores nothing" claim in its strongest form ("adds **no**
  credential to the estate at all") without naming the cloud CLI's user credential that
  the route signs with — while quoting the principal's constraint that secrets live in
  a secret store. So the re-briefing that corrected one wrong fact left the other half
  of the original objection unweighed, and introduced an unstated dependency. Both are
  what CC1 says; the principal's re-ruling is the remedy and it is his.
- **CC2 — not anticipated** (above). Stands.
- **CC3 — not anticipated.** The nearest thing to an enumeration is the 0005 record's
  three-way access decision (personal grant / domain-wide / app password), which weighs
  *how much access* and not *who attacks the surface*. Stands.
- **CC4 — not anticipated.** The 0257 record's `ccpdf` section names the flag table
  and the filename convention; hostile PDFs are not considered. Stands.
- **CC5 — partly anticipated.** Traversal was ("a careless or hostile name cannot
  escape the directory"); symlinks, a symlinked `--dest`, and the message id were not.
  Stands.
- **CC6 — not anticipated.** Stands.
- **CC7 — not anticipated.** On (e): the 0005 record says 25 tests, the 0257 record
  says 26; the pointer and the brief inherited the stale 25. Stands.
- **CC8 — not anticipated.** Stands.
- **CC9 — partly anticipated.** Both records say the Keychain grant, once minted, is
  registered in the private registry from a session in that repo. The 0257 record then
  reasons "the delegation route creates no credential, so there is nothing new to
  register" — the same framing CC1 tests. `SECRETS.md`'s standing-credential list is
  not raised. Stands.
- **CC10 — anticipated as a possibility, then declared not owed.** See claim 1. Stands.
- **CC11 — the test gaps are anticipated and stated** (network unmocked; the two fixes
  "not easily testable"); the specific items in CC11 are not. Stands as a note.
- **CC12 — consistent with the records.** The 0257 record discloses `pdftoppm` was
  installed during testing and leaves keeping it to the principal; it is still installed
  and passes the selftest.

**CC13 — minor (record accuracy; formed at reconcile).** (a) The 0257 record's body
says the stored-grant fallback "is still owed" and predicts the delegation lapse; its
*Owed* section says "nothing for the mail path — it works now, with no setup". The
close-out contradicts the body, and the state CC10 found is the one the body foresaw.
(b) The queue pointer names the 0005 record as the sole intent record; the delta it
widened on 2026-09-09 (the two-route resolver, the plaintext-store removal, `ccpdf`) is
accounted for only in the 0257 record, which the pointer does not link. A taker
following the pointer's refs would reconcile the second half of the delta against a
record that predates it. *Counsel:* an Owed section lists every "still owed" the body
names; a widened pointer links the record that accounts for the widening.

**Overall, restated: PASS-WITH-FINDINGS — 1 MAJOR (CC1), 4 MODERATE (CC2, CC3, CC4,
CC10), 6 minor (CC5–CC9, CC13), 2 notes (CC11, CC12).** Nothing in the records lowers
a severity; CC1 and CC2 are strengthened by them. The cycle stays open on CC1.

## Deferred material — folded in at reconcile

# Deferred material — ccmail-build (open only after your findings are durably written)

Sibling of `docs/reviews/2026-09-25-0715-ccmail-build-cold.md` under REVIEW.md
rule 1's split; held by the orchestrator outside the worktree. Folded into the
brief below the verdict when the verdict lands.

## Intent records

- `docs/sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md`
  — the build session's account, including the five defects it found and how.
  **Not opened by the brief-writer.**
- The queue pointer carries two claims the author addressed to the taker: that
  the live Gmail round trip is proven end to end via the delegation route, and
  that the build's five defects were found by reading and by an adversarial
  selftest, none by use. **Read by the brief-writer** (they sit in the pointer).
  They are the author's claims; the reviewer tests them.

## Prior verdicts and barred items on the same surfaces

- `docs/sessions/2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md`
- the `docs/SESSIONS.md` entries of 2026-09-09

## The queue pointer's own lens hints — the author's seeded questions, verbatim

The pointer carries no lens paragraph — refs only.

## Brief-writer's seeded questions (a floor, never a fence)

Generate your own before reading these; a question you did not think of is a
prompt to re-read the surface, not an agenda.

1. The brief-writer's machine-local instructions say `ccmail <id> --get all`
   writes attachments to `~/.cache/ccmail/` and prints paths. Nothing there says
   how the cache is cleared or how long it keeps personal attachments. Is that
   the tool's gap, the docs' gap, or by design?
