# Cold pass — ADR 0008's 2026-10-16 boundary amendment and the ruleset bypass removal

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4, with a live platform read.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-17 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/820-rule-4-cold-pass-queued-adr-0008-boundary-amendment.md`.
**Why it earns a review:** it restates, in an ADR, the strength of the one control that stands
between atelier's `main` and every child's CI, and it pairs that text with a change made on the
platform rather than in git — a change no diff shows and no scanner re-reads.

## Spawn provenance

- **Author of the work under review:** the 2026-10-16 queue run that landed the commit below and
  made the platform change; its intent record is the session file dated 2026-10-16 0703 UTC that
  the pointer names (not opened by the brief-writer). The commit's trailer names an Opus model.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched on 2026-10-17 by the
  Mike-opened Fable review session working in worktree `atelier-review-1017`, on Mike's 2026-10-16
  answer that a fresh Opus session writes these briefs. Neither it nor its orchestrator authored
  the delta or was started or instructed by its author. **Off-tier for review, disclosed: it forms
  no finding and writes no severity**, and stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, passing rule 4's
  criterion. If it runs as reviewer-plus-orchestrator, the off-tier conditions of rule 4 apply and
  are disclosed in the claim, the pointer and the verdict. The reviewer repeats its own provenance
  in the verdict.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material met before writing): the four queue
  pointers it was assigned (160/820–850; refs-only), and 160/500 in full as the shape of a
  pointer's append line (its claim and its verdict summary for another pass included); the first
  lines of pointers 160/790, 160/800 and 160/860; the landing commit's subject, `--stat`, full
  message body (the author's account, with a principal quote) and diff on the delta path; the
  ADR's section headings and grep-hit lines of its 2026-08-23 amendment; single grep-hit lines
  from the commissioning board items named under *Deferred reading* — including one line from
  160/090 recording how a finding there was answered and which of its findings stand — and from
  `tools/floorfleet.py`, `CHANGELOG.md` and 115/180, met while sweeping for mirror sites; the
  `--help` text of `floorfleet` and `signscan`; filenames (not contents) of prior verdicts; the
  filenames and one append line of this run's other brief-writer (not its briefs); and its own
  harness-loaded memory index. It made no platform read. It did not open the intent record,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, `docs/method/REVIEW.md` or any
  prior verdict. What its orchestrator read is the orchestrator's to disclose; it passed the
  brief-writer an instruction file, three templates (two 2026-10-16 briefs and a sibling) and a
  list of taken prefixes, and no evaluative content. Everything evaluative the brief-writer
  formed is in the sibling.

## What the work is

Landing commit (diff it on the delta path; review the path at HEAD, `b50db0c` or later):

- `93d3a14` (2026-10-16 11:46 UTC) — decisions: ADR 0008's boundary at its true strength; main's
  admin bypass removed (140/020)

Delta, the pointer's own list:

- `docs/decisions/0008-enforcement-is-called-not-copied.md` — the appended section *Amended
  2026-10-16 — the boundary as it now stands: three legs, three strengths*; read the whole ADR at
  HEAD, because the section supersedes the 2026-08-23 amendment above it and rests on the
  *Consequences* clause.
- **The platform state:** the `bypass_actors` list of the `main` ruleset the section names, set to
  empty through the API on 2026-10-16. There is no diff for this. Read it live (re-run list), and
  if the platform exposes the ruleset's change history, read that too.

The commit also touched board items, the generated index and the intent record; those are not
the delta. No later commit touches the ADR (`git log 93d3a14..HEAD -- docs/decisions/0008*` is
empty at the time of writing); confirm at your HEAD.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs and live behaviour. The
lenses organise it; they do not bound it. Non-goals are the only narrowing and are themselves
reviewable.

Probe, at least:

- **Each factual claim against the live platform.** Every statement the section makes about the
  ruleset — its id, `enforcement`, `created_at`, each rule type, `bypass_actors`, the effective
  rules on `main` — and about commit verification ("30 of the 30 latest"), re-read live and
  recorded with the read's own time. Say which claims were true at landing, which are true at
  your HEAD, and which cannot be re-driven.
- **The three legs and their stated strengths.** For each leg (branch protection, signed commits,
  review on the registry), what the section says enforces it, and whether that enforcer exists as
  described. Name what "in force for every account" means when the owner can edit the ruleset.
- **Every path that writes `main` after the change.** Direct pushes from a session, a PR merged
  through the platform, a child's hand-up PR, any workflow or bot that commits, a revert, a
  release. For each, whether a `required_signatures` rule with no bypass actor lets it through,
  and how it would fail if not. The section claims direct-to-`main` working is untouched; test it.
- **The machine check.** The section describes what `floorfleet`'s boundary row reads, what makes
  it red, unknown or green, and that it does not read the bypass list. Check each against
  `tools/floorfleet.py` and its tests at HEAD.
- **Supersession.** How the section relates to the 2026-08-23 amendment it supersedes and to the
  *Consequences* clause: what a reader landing on the ADR now believes, in order, and whether any
  other surface still states the superseded text.
- **The principal's words.** Separate each verbatim quote or attributed ruling from the wording
  around it; say where the surrounding text narrows, widens or re-reads what is attributed.

**Non-goals:** whether the principal should have chosen to drop the bypass (recorded as his
answer). How the change is recorded, what it claims, the platform's actual state and the residual
exposure are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether an
   ADR amendment is the right carrier for a statement of live platform state, how that statement
   is kept true after landing, and what an amendment that supersedes an amendment does to the
   ADR's readability.
2. **Correctness & quality.** Diff `93d3a14` on the ADR. Check every API path, field name, rule
   type, date and count in the section against a live read and against the code it names. Check
   every cross-reference (board keys, finding IDs, `REVIEW.md` rule 4) resolves to a passage that
   says what is claimed.
3. **Completeness / harvest.** Every surface still stating the old boundary — the ADR's own
   earlier text, `tools/floorfleet.py`'s docstring and comments, `docs/method/SIGNING.md`,
   `docs/method/GUARDS.md`, `docs/method/AUTONOMY.md`'s direct-to-`main` working, the board's
   section head for the AP1 control, `CHANGELOG.md`. Is a changelog entry owed for a platform
   change?
4. **Security & privacy** — mandatory, and the centre of this pass. Model the attacker the
   section names (holder of the owner's credentials) and any it does not: a compromised session
   with push rights, a compromised signing key, a CI token, a malicious hand-up PR. For each,
   what stops arbitrary code reaching `main` and then every child, and whether the section states
   that honestly. Say what is now visible after the fact and to whom. Describe, never quote,
   anything sensitive. `/security-review` is discharged by grounds (a landed prose delta plus a
   platform setting).

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing. Every platform call is a read: never a write
method, never an edit to the ruleset, never a test push to `main`.

- `gh api repos/mike548141/atelier/rulesets/<id>` and `gh api
  repos/mike548141/atelier/rules/branches/main`, recorded with the read time
- the ruleset's history, if the platform offers a read-only endpoint for it
- commit verification over a window you choose and name (the section's "30 latest", and the
  window since the change), from the platform's commit records
- `python3 tools/floorfleet.py --selftest`, `python3 tools/signscan.py --selftest`, and
  `python3 -m unittest discover -s tools -p 'test_floorfleet.py' -v`; the parent boundary row
  live only if you can scope `floorfleet` to atelier alone (`--help` first; by default it walks
  every repo beside the checkout, which this run must not do)
- `python3 tools/linkscan.py --root . .` and `python3 tools/leakscan.py --root . .`, exit codes
  read explicitly
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-17-*` brief — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts and
  scratch trees go in a private clone under your session scratchpad, named by your prefix.
- No platform write of any kind. A probe that would need one is described in the verdict as a
  probe owed, for the principal to authorise.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds and
  do the code-altitude read by hand against the OWASP catalogue, or keep the tree clean when you
  spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/820-rule-4-cold-pass-queued-adr-0008-boundary-amendment.md`,
the sibling `docs/reviews/2026-10-17-0955-adr-0008-boundary-amendment-cold.deferred.md`, the
landing commit's message body (the author's account; read subject, stat and diff only), and:

- `docs/roadmap/140-ap1-ruled-and-half-applied-the-main-cont/` (the commissioning item and its
  section)
- `docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md`

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/820-rule-4-cold-pass-queued-adr-0008-boundary-amendment.md
--also-exclude docs/reviews/2026-10-17-0955-adr-0008-boundary-amendment-cold.deferred.md
--also-exclude docs/roadmap/140-ap1-ruled-and-half-applied-the-main-cont --also-exclude
docs/roadmap/160-doctrine-review-owed/090-rule-4-review-queued-tier-fable-pass-type-code.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `BY`: `BY1`, `BY2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands, read times and results) and a follow-up checklist. Then STOP and commit
this file before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.

---

## Verdict — phase 1 (`BY`), written 2026-10-17T23:52Z

### Provenance, repeated

- **Reviewer:** Claude Fable 5.1 (`claude-fable-5-1`), the tier the principal named (ruling
  2026-08-04), checked at selection. I formed every finding and severity below.
- **Spawn:** I was spawned by a Mike-opened Claude Code **cloud** session running
  `claude-fable-5-1` as orchestrator (it opened on `claude-opus-5` and Mike switched it to Fable
  before any claim or pass). That orchestrator authored none of the delta or this brief and was not
  started or instructed by their authors. It forms no finding and writes no severity; it holds the
  `.deferred.md` sibling outside the checkout at a path I was not given, commits this phase-1 file
  before releasing the sibling to me, and received one operational note from Mike's watching
  session (model, queue scope, container facts, merge instruction — no evaluative content about
  any delta). The claim line in the queue pointer discloses the same shape; I have not opened the
  pointer. The brief's own provenance (an Opus brief-writer, off-tier, disclosed, no finding
  formed) is repeated above and not re-litigated here.
- **Where:** the shared cloud checkout `/home/user/atelier`, branch
  `claude/review-work-briefs-adj6ad`, HEAD `0aff4d8` = `origin/main` at session open. The clone
  was **shallow** when I started (52 commits; `c824287` the graft point), so
  `git log -- docs/decisions/0008*` named `c824287` as touching the ADR — the graft, not an edit:
  `git diff 93d3a14 HEAD -- <ADR>` is empty, and the platform's newest `main` commit at
  2026-10-17T23:49Z (`fe020b1`, two board files) does not touch it either. **Addendum
  2026-10-17T23:55Z:** the orchestrator unshallowed the checkout (`git fetch --unshallow`, its act,
  not mine) and asked me to re-run any history step the graft touched; re-run on 1779 commits,
  `93d3a14..HEAD` on the ADR path is **empty** and the ADR's full history is four commits
  (2026-07-26, 2026-08-07, 2026-08-23, 2026-10-16) — the brief's "no later commit touches the ADR"
  holds at HEAD. No worktree (none exist here); scratch at `/home/user/scratch/BY/`. I edited this
  file only and ran no git command that writes.
- **Container facts, as observed — two differ from the note I was given.** (1) `gh` **is** on PATH
  (`/usr/local/bin/gh`); `gh auth status` reports the `GH_TOKEN` in the environment invalid.
  (2) **Anonymous read-only GETs to `api.github.com` succeed** through the proxy (HTTP 200 on the
  ruleset, the effective rules, the rule-suite evaluations and the commit listings), so the brief's
  live read of the `main` ruleset **was** made from here, anonymously, read times in the ledger.
  What could not be read: the ruleset's change **history** (`…/rulesets/20603641/history` → 403
  to an anonymous caller — *not re-driven here*), and GitHub's documentation pages
  (`docs.github.com` does not resolve through the proxy — *not re-driven here*). The container's
  `gpg.ssh.program` is a sign-only wrapper, so every local signature check had to override it to
  `/usr/bin/ssh-keygen`; the ledger says where. No `~/.claude/` and no leakscan term list, as the
  note said: I ran the floor's **CI plane**, not the hook plane (board `115/350`).
- **Exposure disclosed:** none beyond the brief's intended reading. The two commits whose bodies I
  avoided (`93d3a14`, `c824287`) were read as `--stat --format=%s` only. `coldsweep` ran with the
  brief's four `--also-exclude` paths and never `--include-barred`. The one slip-shaped event:
  `c824287`'s `--stat` listed the whole tree (graft artefact) — filenames only, no verdict text.
  `/security-review` was not run: the delta is a landed prose section plus a platform setting, and
  the scanner reads a pending diff (discharged by grounds; code-altitude read done by hand below).
- **Relayed, labelled:** PR #118 (the orchestrator's claim commit, SSH-signed by the cloud harness
  key, committer the harness identity) merged to `main` at 2026-10-17T23:34Z with a GitHub-minted
  merge commit. I then **observed** the same event in the platform's rule-suite listing (suite
  `4580854131`: `main`, before `b2c53da`, after `0aff4d8`, result `pass`, actor the owner account,
  pushed 2026-10-17T23:34:36Z). A merge is not evidence about `bypass_actors`; the ruleset detail
  read is.

### Lens 1 — approach and assumptions (named first, then attacked)

- **A1 — "`required_signatures` enforces signing"** in the sense the floor's signing doctrine
  means it. **False.** The rule's predicate is *GitHub-verified*, not *signed by a key in
  `allowed_signers`*. Two commits on `main` after the change prove it (BY1). The section's
  residual-exposure reasoning rests on A1.
- **A2 — an ADR amendment is a fit carrier for live platform state.** Acceptable **as a dated
  snapshot**, and the section does date its read ("Read live on 2026-10-16"). What keeps it true
  is only `floorfleet`'s boundary row, which covers two of the three rules and none of the bypass
  list (BY2) — so the signing leg, the one this amendment strengthens, has no machine tie at all.
- **A3 — "a ruleset change is a visible act."** Visible **to the owner**: the history endpoint
  refuses anonymous reads (403), the public can poll only current state, and the repo's own
  instrument does not read the fields an attacker would change. Weaker than written (BY1).
- **A4 — "the owner account is the remaining exposure."** **Correct**, and the honest spine of the
  section. The path to it is what is overstated.
- **A5 — "direct-to-`main` working is untouched."** True of `deletion` and `non_fast_forward`.
  Removing the bypass does add a condition to every direct push (GitHub-verified or refused),
  which the section implies ("the owner's included") but no session-facing doc states (BY3).
- **Readability of an amendment that supersedes an amendment:** a reader meets three states in
  sequence — the Consequences clause (control named), the 2026-08-23 section ("this clause is the
  truth of the boundary", present tense) and this one — with no forward marker at either earlier
  site. `RECORD.md`'s lifecycle has verbs for an ADR, not for an addendum, and its append-only rule
  forbids the marker inside the old section; the header is the one editable surface (BY5).
- **What "in force for every account" means when the owner can edit the ruleset** (the brief's
  question): in force for every actor at push-evaluation time, the owner included
  (`bypass_actors: []`, `current_user_can_bypass: never`), and removable by the owner in one
  authenticated API call that leaves no trace in the repo and none the public can read. The bold
  leg headings read stronger than the qualifying paragraph three paragraphs later.
- **Non-goal check:** "whether the principal should have dropped the bypass" fences off a choice,
  not a risk; the residual exposure stays in scope and is where the finding lies. Legitimate.

### Lens 2 — correctness, claim by claim against the live read and the code

Each claim, how it was re-driven, and the result:

- ruleset `20603641`, `enforcement: active`, on the default branch — live read
  2026-10-17T23:46:42Z — **true** (`conditions.ref_name.include: ~DEFAULT_BRANCH`).
- `created_at` 2026-08-09 09:58 UTC — live — **true** (`…T21:58:10+12:00`); fourteen days
  before the 2026-08-23 amendment, as the section says.
- rules `deletion`, `non_fast_forward`, `required_signatures` — live, on both endpoints —
  **true**.
- `bypass_actors` reads `[]` — live — **true**.
- "until 2026-10-16 the ruleset had one bypass actor, the admin role, `bypass_mode: always`" —
  history endpoint 403 to an anonymous caller — **not re-driven here**; the ruleset's `updated_at`
  (2026-10-16T11:46:08Z, 38 s before the landing commit's committer time 11:46:46Z) corroborates
  an edit that day, not its content.
- "30 of the 30 latest commits on `main` were verified" before the change — live, window = the 30
  commits ending at `93d3a14`'s parent — **true**: 30/30 `verified: true, reason: valid`, all SSH;
  the same 30 verify `G` locally against `allowed_signers` (unshallowed re-run, 23:55Z).
- `floorfleet` reads `rules/branches/main` whenever a plane talks to GitHub — `main()`
  1779–1780 — true (`--remote`, `--status`, `--from-github`).
- red when `deletion`/`non_fast_forward` is missing; unknown, never a pass, when unreadable; green
  otherwise — `classify_boundary` 604–636, the selftest and 118 unit tests — true.
- `--check` fails on red or unknown — `main()` 1836–1837 — true.
- `required_signatures` shown but informational — 589–601, 626 — true.
- the row does not read the bypass list — it reads only `rules/branches/main`, which carries no
  bypass field — true.
- built 2026-09-18 under `140/010` (`115/180`) — the `115/180` item — true; `140/010` itself is
  barred reading until phase 2.
- direct-to-`main` fast-forward untouched by the two rules — rule semantics — true of those two
  rules (A5 above for the third).
- "Signing now forces that attacker to hold the signing key too, or to change the ruleset first,
  which is a visible act" — live commits plus local verification — **false as stated** (BY1).
- "The platform is now the enforcing plane" — live plus `signscan` — **true of a weaker
  predicate** than the floor's (BY1).
- `signscan` stays warn-first on both planes — `ci.yml` 228–246, `floor.yml` 162–190 — true.
- cross-references `AR1`, `AR2`, `AR8`, `140/020`, `140/010` — `coldsweep` — resolve **only**
  into barred material; checked at phase 2.
- `REVIEW.md` rule 4, "queued cold pass" — rule 4 text — resolves.

Live boundary row: `floorfleet --child /home/user/atelier --remote --check` at 2026-10-17T23:44:54Z
printed `boundary:green … required-signatures: present, informational` (exit 1 is the expected
`vendored` child row the brief warned of — atelier's own `floor.yml` names scanners).

### Lens 3 — completeness and harvest

Mirror sites still carrying the superseded reading (swept with `coldsweep`; hits in the ledger):

- `tools/floorfleet.py` 61–84 and 589–601, and `tools/test_floorfleet.py` 1290–1295: the
  grounds for treating `required_signatures` as informational quote the **2026-08-23**
  amendment ("warn-first on both planes", "never names it as the ruled control"), which this
  section supersedes with "in force for every account" and "the platform is now the enforcing
  plane" (BY2).
- `docs/method/SIGNING.md`: no mention that atelier's `main` refuses unverified commits at the
  platform since 2026-10-16; its activation ladder still names the CI flip as "the remaining
  deliberate step" (211–213) (BY3).
- `CHANGELOG.md`: no entry for the bypass removal or the amendment, where the 2026-08-23 amendment
  and the `115/180` build each got one (BY4).
- `docs/roadmap/115-…/180-…`: "see the 2026-08-23 amendment" as the statement of controls in
  force — a ticked item, frozen record (BY8, note).
- `docs/method/GUARDS.md`, `AUTONOMY.md`, `tools/README.md`, `SECURITY.md`: no stale statement of
  the boundary found; `SECURITY.md` 57–60 describes floating `main` without naming the control,
  which is not a contradiction.
- Harvest from tooling the section leans on: `floorfleet` tracebacks rather than reporting
  `unknown` when the `gh` binary is absent (BY6); `signscan` reports a verifier-program failure as
  a *bad signature* (BY7).

### Lens 4 — security and privacy (the centre of this pass)

`/security-review` discharged by grounds (above). Code-altitude read by hand: the delta runs no
code; the instrument it describes (`floorfleet`) was read for input handling — `_gh_json` parses
`gh` output with `json.loads` and refuses non-list bodies (fail-closed), child-authored text is
control-stripped before rendering (C1F3), nothing here takes untrusted input into a shell. The
relevant catalogue is the supply-chain class (SLSA / the Actions hardening guidance ADR 0008
already cites), not OWASP web vectors; the design-altitude questions are below.

**Attacker models, each answered against the live state:**

- *Holder of the owner's credentials* (the one the section names). Needs **neither** the signing
  key nor a ruleset edit: the web editor, the merge button and a squash/revert all mint commits
  GitHub signs with its own key, and the platform marks them verified — one such commit
  (`0aff4d8`) landed on `main` under the no-bypass ruleset on 2026-10-17. Registering a new
  signing key on the account is the other route; a key outside `allowed_signers` (`911827f`)
  landed the same way. **The section's two "forces" alternatives are both unnecessary** (BY1).
- *Compromised session on a signing machine* (key loaded in the agent per `SIGNING.md` § Key
  handling, push rights present). The platform rule adds nothing: its commits are trust-listed
  and verified. Unmodelled by the section; the honest statement is that this attacker is bounded
  only by the floor, public visibility and review-after-landing.
- *Compromised signing key alone* (no push rights): nothing lands. The key's blast radius is
  bounded by push access, as `SIGNING.md` says.
- *A CI token*: atelier's two workflows carry `permissions: contents: read` (`ci.yml` 49–50,
  `floor.yml` 71–72). That is the control that actually stops a token writing `main`; the
  section does not name it, and a future `contents: write` would be invisible to the boundary
  row. Worth one sentence in the ADR (counsel under BY1).
- *A malicious hand-up PR*: hand-up branches are outside the ruleset (`~DEFAULT_BRANCH` only);
  CI runs on every push with a read-only token; landing on `main` is the owner's one-click merge,
  which mints a GitHub-signed commit. Review on the registry is post-hoc, as the section says.

**Every path that writes `main` after the change, and how it fails:**

- direct push of a commit signed by the trust-listed key — **passes**; 59 of the 60 commits on
  `main` since 2026-10-16 are this path, all verified.
- direct push of an unsigned or unverifiable commit — **refused at push**; *not exercised* (no
  write permitted), stated from the rule's semantics.
- direct push of a commit signed by a key GitHub verifies but `allowed_signers` lacks —
  **passes**; `911827f`: platform `valid`, local `U` "No principal matched", `signscan` **bad**.
- a PR merged on the platform — **passes**; GitHub signs the merge: `0aff4d8`, PGP, committer
  GitHub's web-flow identity, `valid`. Two older ones (`a0ef731`, `4b2cf6f`, named in `ci.yml`
  and `SIGNING.md`) are ancestors of `main` too.
- a web edit, squash or revert on the platform — **passes** by the same mechanism; *not
  exercised*.
- a workflow or bot commit — refused unless GitHub-verified; atelier's own tokens are
  `contents: read` (`ci.yml`, `floor.yml`), which is the control that actually applies.
- a local revert, rebase or cherry-pick then push — a direct push of the rewritten commits; the
  hook-plane gap is `115/340`, outside this delta.

**What is visible after the fact, and to whom:** every commit on `main` is public and its
verification record readable anonymously (I read 60). Rule-suite evaluations are readable
anonymously (actor, result, before/after). Ruleset **edits** are readable only with the owner's
authorisation (403 anonymously). The repo's own instrument reads neither the bypass list nor the
presence of `required_signatures` as a red, so the two edits an attacker would make are the two
nobody is told about.

**Privacy:** the section quotes no personal data; it names the account (a recorded exception) and
the ruleset id. Nothing in this delta widens a personal-data surface.

### Findings

**BY1 — MAJOR (security) — the signing leg's residual-exposure sentence is false in the
reassuring direction.** The section says: *"Signing now forces that attacker to hold the signing
key too, or to change the ruleset first, which is a visible act."* Re-driven: `required_signatures`
with `bypass_actors: []` requires a **GitHub-verified** signature, not one from `allowed_signers`.
On `main` since the change: `0aff4d8` (committer GitHub's web-flow identity, PGP, `verified:
true, reason: valid`) and `911827f` (committer the cloud harness identity, SSH key **absent from
`allowed_signers`**, platform `valid`; locally `U` "Good signature … No principal matched";
`signscan` with the real verifier: **bad**). Both passed the ruleset (`rule-suites` result `pass`).
So an owner-credential holder needs neither the signing key (the platform signs for anyone who
edits or merges in the web UI; a self-registered key also verifies) nor a ruleset edit — and the
edit, if made, is visible to the owner alone (history 403 anonymously) and to no instrument in the
repo. `SIGNING.md` already states the badge is "the convenience plane, not the durable one" and
"existing badges persist, including any the attacker minted" (87–96, 160–162); the amendment
contradicts the house's own signing doctrine without saying so (V5). The adjacent sentence *"The
platform is now the enforcing plane"* is true of a weaker predicate than the floor's: the
trust-list plane stays warn-first, and `main` carried a commit it rejects, surfaced as a warning
only. The section's **conclusion** (AP1 stays open; the owner account is the exposure) is correct,
which is why this is not a FAIL; the **reasoning** a reader would take as the detection hook is
wrong on the one control the ADR calls load-bearing, in doctrine that propagates. *Severity
MAJOR; recurrence-prevention step (counsel, the principal's to decide):* (i) restate the leg with
its predicate — "a GitHub-verified signature from any account, or GitHub's own; the floor's trust
list is the only *whose-key* check and it is warn-first"; (ii) decide whether the trust-list plane
blocks (the `SIGNING.md` flip) — the control that would have refused `911827f`; (iii) have the
boundary row red on `required_signatures` absent and read `bypass_actors` non-empty (AR2), the two
edits an attacker would make; (iv) name `contents: read` in the workflows as the CI-token control.

**BY2 — MODERATE — the machine check's stated grounds are the superseded text, and the check
does not cover the leg this amendment strengthens (V3, V5).** `tools/floorfleet.py` 61–84 and
589–601 and `tools/test_floorfleet.py` 1290–1295 justify treating `required_signatures` as
informational by quoting the 2026-08-23 amendment ("warn-first on both planes … never names it
as the ruled control"); the live ADR says the opposite. Behaviour is disclosed honestly in the
section ("informational … does not read the bypass list (AR2, still open)"), so this is a sweep
miss, not an overclaim — but it leaves a reader of the code believing the ADR says what it no
longer says, and it leaves the admin bypass restorable with nothing in the repo to notice. The
section names `AR2` (a finding id) and no board item; whether one exists is barred reading until
phase 2.
*Counsel:* re-ground the docstring in the 2026-10-16 section and make the row's silence on the
bypass list an explicit, dated residual.

**BY3 — MODERATE — `SIGNING.md` was not swept (V3).** Since 2026-10-16 atelier's `main` refuses
any commit the platform cannot verify, for every actor. `SIGNING.md` still says "flipping CI from
warn to block is the remaining deliberate step" (211–213), its ladder status reads "warn-first",
and no session-facing surface says what a direct push to `main` must satisfy. The two planes the
doc already describes (87–96, 119–128) now have different enforcement strengths and the doc does
not say which is blocking where. *Counsel:* one dated paragraph under *Verification* stating the
platform rule, its predicate, and that the trust-list plane remains warn-first.

**BY4 — MODERATE — no changelog entry for a change that has no diff.** `CHANGELOG.md` carries
entries for the 2026-08-23 amendment (line 334) and the `115/180` build (306) but none for the
bypass removal or this section, although it has six 2026-10-16 entries for other work. ADR 0002
makes the changelog the index; for a platform-side change the ADR and the changelog are the only
in-repo record. *Counsel:* a `Changed (2026-10-16 — main's admin bypass removed, 140/020)` entry.

**BY5 — minor — supersession leaves two misleading surfaces at the top of the ADR.** The
header's `review:` line still reads "queued — pointer owed" (unchanged since 2026-07-26, three
passes later), and the 2026-08-23 section's present-tense "Until it lands, this clause is the
truth of the boundary" is read before the section that supersedes it. The amendment's "left
above as written" is `RECORD.md`-compliant (addenda never edit accepted text), so the only
compliant fix is at the header. *Counsel:* a one-line header pointer — "boundary as of
2026-10-16: see the last amendment" — and the `review:` line brought to the pointer that exists
(`160/820`).

**BY6 — minor — `floorfleet` tracebacks instead of reporting `unknown` when `gh` is absent.**
`_gh_json`, `_gh_list` and `_read_remote_slug_result` call `subprocess.run(["gh", …])` with no
`FileNotFoundError` guard (probe: Python 3.13 raises on a missing executable); the docstring
(71–74) promises `unknown … no gh`. The section's "never a pass" survives (an uncaught exception
exits 1) but the documented contract does not, and the board does not render. Could not be
observed on `floorfleet` itself here because `gh` is present; the probe is in the ledger.

**BY7 — minor — `signscan` reports a verifier-program failure as a bad signature.** With the
container's sign-only `gpg.ssh.program`, `git verify-commit` failed on every commit and `signscan`
printed `50 bad`; with `/usr/bin/ssh-keygen` the same range is `49 good, 1 bad, 1 deferred`.
Fail-closed direction, but the class is mislabelled (error vs bad), the distinction `floorfleet`
draws between `unknown` and `red`. Harvest item on tooling the section relies on.

**BY8 — note — `115/180`'s text points at the 2026-08-23 amendment as the statement of controls
in force.** A ticked item; frozen record; recorded so the class can be counted.

### Standing checklist V1–V7

- **V1** — bitten: BY1 (one claim stronger than its evidence, the load-bearing one); BY5's
  present-tense sentence. Every platform fact in the section re-ran true.
- **V2** — every "live" claim re-run where a read exists: ruleset detail, effective rules,
  30-of-30, machine-check behaviour, selftests, 118 unit tests, floor CI plane. Not re-driven:
  ruleset history (403), the admin-role bypass's prior existence, GitHub's documentation (DNS).
- **V3** — bitten: BY2, BY3, BY4, BY8.
- **V4** — the boundary's statement lives in the ADR; `floorfleet`'s docstring restates it
  (stale copy, BY2). No new second source introduced by the delta.
- **V5** — bitten: BY1 (contradicts `SIGNING.md`'s badge paragraph; "enforcing plane" vs
  "warn-first" in the same bullet) and BY2 (code grounds vs ADR).
- **V6** — run; `/security-review` discharged by grounds; threat models above.
- **V7** — provenance stated in the brief and repeated here.

### Re-run ledger (UTC)

All on 2026-10-17, times UTC; platform reads are anonymous GETs to `api.github.com`, bodies saved
under `/home/user/scratch/BY/api/`.

- 23:39:16 — `git status`; `git rev-parse HEAD origin/main` → clean but for peer briefs; both
  `0aff4d8`.
- 23:40 — `git show --stat --format=%s 93d3a14`; `git diff 93d3a14^ 93d3a14 -- <ADR>`;
  `git diff 93d3a14 HEAD -- <ADR>` → the 51-line section; HEAD equals the landing.
- 23:41 — `git rev-parse --is-shallow-repository` → `true`; 52 commits; graft `c824287`.
- 23:44:54 — `python3 tools/floorfleet.py --child /home/user/atelier --remote --check` → parent
  row `boundary:green`, `required-signatures: present`; exit 1 on the expected `vendored` child
  row.
- 23:44:58 — GET `rules/branches/main` → 200: `deletion`, `non_fast_forward`,
  `required_signatures`, all from ruleset `20603641`.
- 23:44:58 — GET `rulesets` → 200: one ruleset, `active`, branch target.
- 23:44:59 — GET `commits?sha=main&per_page=30` → 200: 30/30 verified (29 SSH, 1 PGP).
- 23:45 — `python3 tools/floorfleet.py --selftest`; `python3 tools/signscan.py --selftest` →
  both ok, exit 0.
- 23:45 — `coldsweep` × 8 patterns with the brief's four `--also-exclude` paths → hits as in
  lens 3; 412 barred files excluded on each run; never `--include-barred`.
- 23:46:42 — GET `rulesets/20603641` → 200: `enforcement: active`, `created_at`
  2026-08-09T09:58:10Z, `updated_at` 2026-10-16T11:46:08Z, `bypass_actors: []`,
  `~DEFAULT_BRANCH`, `current_user_can_bypass: never`.
- 23:46:42 — GET `rulesets/20603641/history` → **403** "Resource not accessible by integration";
  not re-driven.
- 23:46:43 — GET `rulesets/rule-suites?ref=main&per_page=5` → 200: five `pass` evaluations,
  including the PR #118 merge push.
- 23:46:43 — GET `commits?sha=<parent of 93d3a14>&per_page=30` → 200: **30/30 verified**, all
  SSH — the section's "30 of 30".
- 23:46:43 — GET `commits?sha=main&since=2026-10-16T00:00:00Z&per_page=100` → 200: 60 commits,
  60 verified; `0aff4d8` PGP by GitHub, `911827f` SSH by the harness key.
- 23:46:52 — `signscan --boundary c824287 --warn --json` with the container's verifier →
  `50 bad, 1 deferred`: an artefact of the sign-only `gpg.ssh.program` (BY7).
- 23:47 — `git -c gpg.ssh.program=/usr/bin/ssh-keygen -c gpg.ssh.allowedSignersFile=…
  log --format='%h %G? %GF %cn' -52` → 50 `G` with the listed key; `911827f` `U` (another key);
  `0aff4d8` `E` (PGP, no keyring here).
- 23:48 — `python3 -I -c` probe of `subprocess.run(['<missing>', …])` → raises
  `FileNotFoundError` (BY6).
- 23:49:18 — GET `commits/fe020b1` → 200: verified; its files are two board paths, not the ADR.
- 23:49:26 — `signscan --boundary c824287 --warn`, verifier overridden → `49 good, 1 bad
  (911827f), 1 deferred (0aff4d8)`, exit 0; the same without `--warn` → exit 1.
- 23:49:28 — `python3 tools/floor.py --plane ci --root .` → exit 0; one warn-only `pathscan`
  finding unrelated to this delta (a stub path in the 2026-10-03 exception-register ADR).
- 23:49:4x — `python3 tools/linkscan.py --root . .`; `python3 tools/leakscan.py --root . .` →
  both exit 0; leakscan structural-only (no term list on this machine).
- 23:49:44 — `python3 -m unittest discover -s tools -p 'test_floorfleet.py'` → 118 tests OK.
- 23:49 — WebFetch of `docs.github.com` (rulesets page; signature-verification page) →
  `ENOTFOUND`; not re-driven.
- 23:55:13 — **after the orchestrator's unshallow** (its `git fetch --unshallow`, not mine):
  `git rev-parse --is-shallow-repository` → `false`, 1779 commits;
  `git log 93d3a14..HEAD -- <ADR>` → empty; `git log --follow -- <ADR>` → four commits
  (2026-07-26, 2026-08-07, 2026-08-23, 2026-10-16); local trust-list verification of the 30
  commits before `93d3a14` → 30 `G`; `93d3a14` itself `G`; `a0ef731` and `4b2cf6f` are ancestors
  of `main`, both `E` (GitHub PGP). Nothing earlier in this ledger changes.
- 23:5x — hygiene over this file: `datescan`, `spellscan`, `leakscan` (structural),
  `secretscan` clean; `reviewscan` clean over the tree; lines re-wrapped to ≤ 100 columns.

Not run: the full Python suite and the instruments suite (nothing in this delta exercises them
beyond `test_floorfleet`; the floor's CI plane ran). Never run: any platform write, any test push.

### Overall

**PASS-WITH-FINDINGS — MAJOR 1 · MODERATE 3 · minor 3 · note 1.** Every factual claim the
section makes about the platform re-ran true at 2026-10-17T23:46Z, the machine-check description
matches the code, and the conclusion (AP1 open; the owner account is the exposure) is right. The
MAJOR is one security sentence that overstates what the signing leg buys and what is visible,
contradicting the house's own signing doctrine; it stands in doctrine that propagates, so it is
the headline. Not a FAIL because the record is otherwise honest and the fix is a wording change
plus the sweep it should have carried.

### Follow-up checklist (the principal's to decide; nothing applied)

- [ ] BY1 — restate the signing leg's predicate and the visibility claim; decide the trust-list
      flip; name `contents: read` as the CI-token control.
- [ ] BY2 — re-ground `floorfleet`'s docstring/tests in the 2026-10-16 section; decide whether the
      boundary row reds on `required_signatures` absent and reads `bypass_actors` (AR2).
- [ ] BY3 — sweep `SIGNING.md` for the platform rule and the two planes' strengths.
- [ ] BY4 — changelog entry for the 2026-10-16 platform change.
- [ ] BY5 — header-level current-state pointer and `review:` line on ADR 0008.
- [ ] BY6 — guard `FileNotFoundError` in `floorfleet`'s `gh` calls; test it.
- [ ] BY7 — `signscan` distinguishes verifier error from bad signature.
- [ ] Probes owed, needing authorisation or a credential: read the ruleset's **history** with the
      owner's auth (confirms the admin-role bypass and its removal time); confirm GitHub's
      documented behaviour for web-flow signing under required signatures from a host that can
      reach the docs; exercise "unsigned push is refused" on a **scratch** repo carrying the same
      ruleset — never on atelier's `main`.
