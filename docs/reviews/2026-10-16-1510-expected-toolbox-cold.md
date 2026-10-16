# Cold pass — the expected toolbox and its install rule

**Pass type:** doctrine cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at selection by
whoever takes this pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus brief-writer;
the pass waits for a further cold Fable session that neither the delta's author nor this
brief-writer (nor its orchestrator) started or instructed; tier checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/500-rule-4-cold-pass-queued-the-expected-toolbox.md`.
**Why it earns a review:** it rewrites which tools a session may install without asking, publishes
the estate's expected tool list in a public repo, adds an "ask, but routine" class beside the
floor, and changes the floor block every child stamps.

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
  line); the landing commit's subject, `--stat`, full message body (the author's account, with
  principal quotes) and diff on the delta paths; `docs/method/REVIEW.md` in full; the ask halves
  of two 2026-10-04 briefs as templates; HEAD text of the neighbouring surfaces named in *Scope*;
  single grep-hit lines from the commissioning board items named under *Deferred reading*, from
  one north-star board item and from old `CHANGELOG.md` entries, met while sweeping for mirror
  sites; filenames (not contents) of prior verdicts; and its own cross-session memory index. It
  did not open the intent record, `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md` or
  any prior verdict. Its orchestrator read the `docs/SESSIONS.md` index tail (entries through
  2026-10-16, including the authoring run's one-paragraph summary) and the 2026-10-16 session
  record's close section, and passed no evaluative content beyond the pointer list. Everything
  evaluative the brief-writer formed is in the sibling.

## What the work is

Landing commit (diff it on the delta paths; review the paths at HEAD, `2e2da81` or later):

- `55572b1` (2026-10-03) — toolbox: the expected tools live in atelier, with how to find each one

Delta paths (the pointer's own list):

- `docs/method/TOOLBOX.md` — most of the file was rewritten; read it whole at HEAD
- `docs/method/AUTONOMY.md` — the install bullet under *Always proceed*
- `docs/method/PROPAGATION.md` — the floor region's *Estate resources* bullet
- `docs/build/templates/CLAUDE.md` — the same bullet, the stamped copy

The commit also touched board items and the intent record; those are not the delta. Two later
commits touch delta files outside the delta's hunks: `1ffefc7` (the template, another pass's
subject) and `89ff0d8` (AUTONOMY, not the install bullet). Check that neither moved the delta.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs and live behaviour. The
lenses organise it; they do not bound it. Non-goals are the only narrowing and are themselves
reviewable.

Probe, at least:

- **Who may add a row, and what a row then permits.** Trace TOOLBOX's "a session … updates this
  list" through "Listed and missing → install it" and AUTONOMY's floor (*Widening your own
  authority*, *New trust surfaces*, the unapproved-tool stop). Cases: a session adds a row and
  installs in one commit; a child-repo session needing a tool atelier does not list; an adopter
  who replaces the table; a row whose route is a user-level pip install, a global npm install, a
  vendor installer or a `.pkg`.
- **The vocabulary.** "Approved", "unapproved", "listed", "expected", "manifest": find every site
  that names the install set (AUTONOMY's intro and floor, `00-APEX.md`, the PROPAGATION floor
  region and template, `skills/session-onramp/SKILL.md`, `docs/method/README.md`, TOOLBOX's own
  opening and allowlist sections) and say whether each still names one set.
- **The new class.** "Upgrading is a routine ask, not a floor stop": does AUTONOMY define a class
  between *Always proceed* and *Always confirm*? What does an unattended run do with it?
- **The table against the rule.** Which *Get* routes need an admin password, and does the table
  flag each one the install rule says Mike must run?
- **The finding method, live.** Run steps 1–3 read-only on your machine for a sample of rows and
  record which commands work as written on macOS and which assume a layout.
- **The principal's words.** Separate each verbatim quote from the wording around it; say where
  the surrounding text narrows, widens or re-reads what is quoted.
- **The stamped pair.** PROPAGATION's floor region and the template must stay identical; say how
  and when a child receives the change.

**Non-goals:** the principal's decision to keep the list in atelier (quoted in the delta) and
which tool groups are listed (recorded as an answer). Placement, the wording around them,
internal consistency and security of the rows are in scope.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first. Ask whether a
   public, extensible list is the right carrier for an install grant, and whether the old
   practice/instance layering (the heading *Two things, kept separate* survives) still holds.
2. **Correctness & quality.** Diff `55572b1` on the four paths. Check every cross-reference in the
   new text resolves to a passage that says what is claimed. Record the case table from *Scope*.
3. **Completeness / harvest.** Every surface still stating the old manifest rule or the old home
   for the list: the sites above, `README.md`, the create-repo skill, the person-context
   north-star item on the board, the plugin's skills. Is a template stamp or changelog owed?
4. **Security & privacy** — mandatory. The same file argues the command allowlist must stay
   unpublished because it maps unattended reach. Test the published table and its install grant
   against that argument. Check for any row or note naming an estate-specific repo, host, account
   or service. At install: what "trusted package manager" covers, and pinning. Describe, never
   quote, anything sensitive. `/security-review` is discharged by grounds (a landed prose delta).

## Re-run obligation

Re-run, do not read. Lift invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/stampscan.py --warn --root . .` and `python3 tools/blockscan.py --check --warn
  --root .` — the stamped floor region against the template
- `python3 tools/leakscan.py --root . .` and `python3 tools/pathscan.py --root . .`, exit codes
  read explicitly
- the finding method's read-only commands for a sample of rows, recorded per row
- the floor on both planes at HEAD (`python3 tools/floor.py --plane ci --root .`)

## House rules for this run

- Name your own review worktree in the verdict; it is read-only to you except for THIS file. Other
  sessions may be live on this machine: touch nothing outside your worktree and your scratch
  clone. Never open another `docs/reviews/2026-10-16-1510-*` file — it is another pass's framing.
- No git command that writes in the worktree, beyond committing this one file at the end of each
  phase (or handing it to your orchestrator to commit). Read-only git is fine. Older checkouts and
  scratch trees go in a private clone under your session scratchpad, named by your prefix.
- One heavy process at a time: the full Python suite at most once, in the foreground; never point
  a scanner at another repo on the machine.
- `/security-review` reads the session's pending diff, not this delta. Discharge it by grounds and
  do the code-altitude read by hand against the OWASP catalogue, or keep the tree clean when you
  spawn it — never with this brief or its sibling dirty.
- Absolute ISO 8601 dates from `date -u`; prose wrapped at ≤ 100 columns; NZ English. Never quote
  a secret, a placeholder token, an email address or a personal detail — this repo is PUBLIC.
- Review deep, not fast: a finding needs a probe or a re-driven claim behind it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md under the rule-1 split, opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`, `docs/sessions/`, every
prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/500-rule-4-cold-pass-queued-the-expected-toolbox.md`, the
sibling `docs/reviews/2026-10-16-1510-expected-toolbox-cold.deferred.md`, the landing commit's
message body (the author's account; read subject, stat and diff only), and:

- `docs/roadmap/320-child-filed-findings-via-pointing-up/500-sessions-cannot-find-installed-tools-toolbox-has-no-locator.md`
- `docs/roadmap/320-child-filed-findings-via-pointing-up/510-sessions-credited-mike-with-a-private-tool-list.md`
- `docs/roadmap/420-when-to-ask-mike-commissioned/020-an-answer-is-not-a-ruling.md`

Sweep with `python3 tools/coldsweep.py --root <your-worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/500-rule-4-cold-pass-queued-the-expected-toolbox.md
--also-exclude docs/reviews/2026-10-16-1510-expected-toolbox-cold.deferred.md --also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up/500-sessions-cannot-find-installed-tools-toolbox-has-no-locator.md
--also-exclude
docs/roadmap/320-child-filed-findings-via-pointing-up/510-sessions-credited-mike-with-a-private-tool-list.md
--also-exclude docs/roadmap/420-when-to-ask-mike-commissioned/020-an-answer-is-not-a-ruling.md
<pattern>`; `--include-barred` only with disclosure in the verdict. Reading the delta is never
barred; the author's narrative of why, and the verdicts that recorded it, are.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Append your verdict
below a `---` divider in THIS file: provenance repeated (how you were spawned, your tier, what you
read), per-lens answers, findings with stable IDs (prefix `TB`: `TB1`, `TB2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with counts, a
re-run ledger (commands and results) and a follow-up checklist. Then STOP and commit this file
before opening the sibling. Edit no other file.

**Phase 2.** Open the sibling. Append `### Reconcile` beneath your verdict: per-finding notes
against its seeded questions and the intent record, any finding formed at reconcile marked as
such, and the overall line restated. Never revise phase-1 text. Fold the sibling in below the
reconcile and delete it.

Findings on doctrine are the principal's to decide (rule 3): record all, apply nothing; counsel
per finding is welcome, labelled as counsel.
