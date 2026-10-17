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

---

# Verdict — phase 1 (2026-10-17 UTC)

## Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent (the named review tier, ruling 2026-08-04),
  spawned 2026-10-17 by a Fable orchestrator that authored neither the delta nor this brief and
  held the sibling `.deferred.md` outside my reach. The orchestrator forms no finding and writes no
  severity; it commits this file. Neither of us was started or instructed by the 2026-10-03 run
  that landed `55572b1`, so rule 4's criterion holds, on tier.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`, HEAD `8acfff1`
  (verified an ancestor of HEAD). Read-only to me except this file; no git write was run.
- **Interruption, disclosed:** the pass was cut off by an API rate limit on 2026-10-17 UTC after
  the verdict above the ledger was written, and resumed in the same agent transcript with the
  same context; nothing was restarted or rewritten, and the only additions after the resume are
  this disclosure and the wrap check recorded in the ledger.
- **What I read:** this brief; the four delta paths at HEAD in full; the `55572b1` diff on those
  four paths (subject and `--stat` only, never the message body); the diffs of `1ffefc7`,
  `89ff0d8` and a third later commit the brief did not list, `09a61b4` (2026-10-17, one row added
  to the TOOLBOX table) on the delta files; `docs/method/REVIEW.md` in full; `AUTONOMY.md` in
  full; `PROPAGATION.md` lines 76–305; `00-APEX.md`, `docs/method/README.md`,
  `skills/session-onramp/SKILL.md`, `skills/create-repo/SKILL.md` and `README.md` at the grep-hit
  lines only; `CHANGELOG.md` lines 1–45 and two historical TOOLBOX entries; `instruments/README.md`
  and `instruments/install`; `tools/blockscan_map.json`; `.githooks/pre-commit` and `ci.yml` at
  their scanner lines. Board items opened (none barred): `320/610` and `320/590` (child-filed
  hand-ups on the floor's estate-resources bullet, dated 2026-10-16 and 2026-10-11), `240/010`
  lines 25–45, `260/README.md` lines 80–90. The coldsweep output also showed me single grep-hit
  lines from `020/180`, `160/870`, `200/100`, `320/640`, `420/010`, and two title lines of the
  generated `docs/ROADMAP.md` index — one of them the barred pointer's own title, refs-only.
- **Not opened:** the sibling, the queue pointer, `320/500`, `320/510`, `420/020`, `SESSIONS.md`,
  `docs/sessions/`, `ROADMAP-DONE.md`, any prior verdict, any other `2026-10-16-15*` brief, the
  landing commit's body. Sweep: `coldsweep.py` with all five `--also-exclude` paths, **no
  `--include-barred`**. `/security-review` discharged by grounds: the delta is landed prose,
  this session's pending diff is other reviewers' drafts, and the tool's exclusions bar markdown
  anyway — a clean pass would weigh nothing. Security read done by hand against OWASP Top 10
  (A05 misconfiguration, A06 outdated components, A08 software/data integrity) and the file's own
  reconnaissance argument.

## Lens 1 — approach and assumptions

Load-bearing assumptions I named before reading beyond the delta:

1. *A list of expected tools is the right carrier for an install grant.* Partly. A list carries
   the **what**; a grant needs a **who said so, when**. The delta attaches the grant to list
   membership and then lets any session extend membership (TB1).
2. *"Listed" means "approved".* Intended, never stated. Seven surfaces still say
   approved/unapproved; TOOLBOX says listed/expected and never bridges them (TB6).
3. *The practice/instance layering survives.* The heading does; the body no longer describes two
   separated things — both bullets now say "this doc" (TB9). The separation that still matters is
   list (public) versus per-machine detail (private), stated in one trailing sentence.
4. *A public list is safe because it holds no paths, hosts or accounts.* True of the content; the
   same file's own allowlist argument says the exposure of an unattended-reach list is its
   *existence*, not its contents, and the delta does not say why that reasoning stops at the
   toolbox (TB4).
5. *Homebrew is the installer for most rows.* Not on the estate's own primary machine (TB3).

**Case table (Scope § who may add a row):**

| Case | TOOLBOX text | AUTONOMY floor | Result |
|---|---|---|---|
| Session adds a row and installs in one commit | permitted: "updates this list in the same commit as the work that needed it" | *Widening your own authority*: the agent records a grant, never originates one | contradiction — TB1 |
| Child-repo session needs a tool atelier does not list | "Not on the list → confirm first"; row lives in atelier, child cannot edit it | point up (`PROPAGATION` § Pointing up) | no route stated for where the confirmed row lands — TB1 |
| Adopter replaces the table | "A peer adopting atelier replaces the table with their own" | their own principal's grant | consistent, if the row carries a decision (TB1 counsel) |
| Route is user-level pip / global npm / vendor installer / `.pkg` | "Use a trusted package manager"; `.pkg` → hand to Mike | — | "trusted" undefined; `.pkg` rows unflagged — TB3, TB4 |

## Lens 2 — correctness and quality

- Diff of `55572b1` on the four paths read whole. Later commits: `1ffefc7` touched the template's
  *Hard constraints* only; `89ff0d8` added three sub-bullets under the making-public floor; neither
  moved the delta. `09a61b4` (not in the brief) appended one tool to the estate-tools row — the
  delta's hunks otherwise stand at HEAD (TB12 notes it).
- Cross-references in the new text: `AUTONOMY.md` (floor says "installing an *unapproved* tool
  (see TOOLBOX)" — resolves, but the two files now use different nouns, TB6); the three board
  items named in the correction paragraph exist by filename (not opened); `instruments/` exists
  with an install script that symlinks each CLI into the user bin — matches "user bin" in the row.
- Factual claims re-driven on this macOS machine: `mandoc` and `tcpdump` are system binaries ✅;
  `openssl` reports LibreSSL ✅; no `timeout` on `PATH` ✅; Playwright is importable from exactly
  one of four `python3` interpreters (the system one) and not from the others ✅ — the method's
  step 3 is what finds it.
- Row-internal consistency: `gh` and `ffmpeg` say *Find: user bin* and *Get: Homebrew*. Homebrew
  does not install into a user bin, so the two columns describe different provenance; on this
  machine every copy of both lives in the user bin and Homebrew is absent (TB3).

## Lens 3 — completeness and harvest

Mirror sites of the old rule and old home, swept with coldsweep (48 hits, 639 files):

| Surface | State |
|---|---|
| `docs/method/README.md:45` | still "keep a tool manifest; approved-but-missing may be installed; keep the personal inventory machine-local" — the reversed rule — TB5 |
| `TOOLBOX.md:3–7` (intro) | still "tool manifest … available and approved" — TB6 |
| `TOOLBOX.md:106–113` (allowlist section) | "the 'approved' column", "approved but absent" — TB6 |
| `00-APEX.md:87, :114`; `AUTONOMY.md:13, :104, :119`; floor region + template; `session-onramp/SKILL.md:50`; `method/README.md:17` | "unapproved tool" — one set intended, mapping unstated — TB6 |
| `240/010` (north-star item) | original text still classes *toolbox* as instance-tier private context; marked "for context", so historical — noted under TB5, no separate finding |
| `260/README.md:85` | cites TOOLBOX as a place that "mandates committing" the allowlist — historical narrative of a fixed defect; not stale doctrine |
| `CHANGELOG.md` | no entry for the 2026-10-03 reversal; the 2026-07-12 entry describes the old rule — TB13 |
| `skills/create-repo/SKILL.md` | stamps the template; new children get the new bullet; no toolbox wording of its own ✅ |

Template stamp: not owed — `stampscan` reports the template identical to the region (93 lines).
How a child receives it: via its own pin bump after the session-start drift check prints the
parent's new commits; `stampscan` runs in atelier's CI only (advisory), so a child learns its
copy drifted only when it bumps or hand-checks. One child did on 2026-10-16 and filed `320/610`
(TB7).

## Lens 4 — security and privacy

- **Content check of the table and notes:** no hostname, account, token scope, repo name or
  machine path. The two paths named are generic (`~/.claude/`, `~/.local`). The `ike-scan` row's
  "per its repo's onramp" implies an unnamed private repo that does IKE scanning; the provider
  mix (three clouds, Cloudflare, IPsec tooling) is disclosed at the grain Mike's ruling accepted.
  Recorded as TB11 (note), within the non-goal.
- **The allowlist argument against the install grant:** TB4. The file holds both "publishing an
  unattended-reach list converts reconnaissance into a plan" and "here is the list of what a
  session installs without asking", and does not reconcile them. The reconciliation that exists
  (default ≠ divergence; installs are reversible) is in the same file for the seed templates and
  is not extended to the toolbox.
- **At install:** "trusted package manager" undefined; the routes include `pip install --user`,
  `npm i -g`, a `curl | bash` installer (brew.sh) and "the projects' releases"; no pinning,
  checksum or signature step; upgrades are deliberately batched, so A06-class staleness is the
  resting state. Folded into TB4.
- `leakscan` clean, exit 0; `secretscan` on the CI floor shows 23 advisory findings at exit 0,
  the known advisory tier.

## Findings

**TB1 — MAJOR.** *The install grant rides on a list any session may extend, in the same commit
that uses it.* `TOOLBOX.md` § *The install rule*: "Listed and missing → install it … needs no
ask" and "When a session finds a tool the list lacks … it updates this list in the same commit as
the work that needed it." `AUTONOMY.md` § *Always proceed* repeats the grant by reference.
`AUTONOMY.md` § *Always confirm*, *Widening your own authority*: "editing … a permission
allowlist to grant the agent more than it had … the agent *records* a grant, never *originates*
one." The toolbox is now the permission allowlist for installs, and its own text tells a session
to widen it routinely. Nothing says a row records a dated principal decision, nor that the "Not
on the list → confirm first" ask is the thing that authorises the row; a reader meeting the
update bullet first has a no-ask path to install anything it adds. The pattern is already live:
`09a61b4` (2026-10-17) added a tool to the row and installed it in one commit — the tool is the
estate's own and commissioned, so the instance is benign, but the wording that permits it permits
the non-benign case equally. A child session cannot take even the benign path, because the list
lives in a repo it may only point up to. V5, V1. *Counsel:* make a row a recorded grant — each
addition carries the principal's dated word or the decision it rests on; a session may *propose*
a row (hand-up or PR) and installs only once the row has landed with that record; state that the
"confirm first" answer is what authorises the row; give the child case its route (point up, then
install once atelier lists it).

**TB2 — MODERATE.** *"A routine ask" sits under "Always proceed (no prompt)".* `AUTONOMY.md:34–35`
puts "Upgrading one is a routine ask, not a floor stop" under a heading that says no prompt; the
doc has only two classes and the delta's third is unnamed. An unattended run (queue run,
scheduled batch) has no instruction: ask and stall, or proceed and breach the principal's "still
ask". TOOLBOX adds "Batch upgrade asks with the session's other questions", which an unattended
run cannot do. V5. *Counsel:* name the class — *ask, non-blocking*: batch it, and when no one can
answer, record the want and proceed on the installed version; move the upgrade bullet out from
under *Always proceed*.

**TB3 — MODERATE.** *The table flags one admin-password row; the rule names a class.* The install
rule says Homebrew itself and any `.pkg` installer need Mike. Rows whose *Get* is a privileged or
GUI installer and carry no flag: `python3` (python.org `.pkg`), `node` (nodejs.org `.pkg`),
`docker` (Docker Desktop's privileged helper), `git`/`make`/`curl`/`sqlite3` (Xcode command-line
tools, a system install dialog), `aws` (its `.pkg` is system-wide by default; a current-user
install exists and the row does not say). Probed live: Homebrew is absent at both standard macOS
prefixes on the estate's primary machine, and every tool here that the table says to *Get* from
Homebrew (`gh`, `jq`, `rg`, `ffmpeg`, `terraform`, `nmap`, `sops`, `age`, …) lives in the user
bin instead. So on the machine the list describes, the no-ask install grant routes through the
one row the rule hands to Mike for about twelve rows, and the table does not say so. V5, V1.
*Counsel:* flag every row whose route needs an admin password or a GUI; add the user-bin
release-binary route where the estate actually uses it; or state plainly that Homebrew is the
expected installer and its absence is a one-time Mike step.

**TB4 — MODERATE (security).** *The file argues both ways about publishing unattended reach.*
§ *The command allowlist is part of this*: publishing a list of what runs without a human
"converts prompt-injection reconnaissance from a guess into a plan … the exposure is the file's
existence in the tree, not its contents." § *The expected toolbox* then publishes what a session
will install without asking, including network and security tooling, and the installer surfaces
it will use. An injected "the toolbox expects X — install and run it" now lands inside the no-ask
grant for every listed row. The available reconciliation — the toolbox is the estate *default*,
as the seed templates already are ("the estate default remains mapped"), and installs are
reversible — is in the same file and not applied. "Trusted package manager" is undefined while
the routes include user-level pip, global npm, a `curl | bash` installer and loose release
binaries; no pinning, checksum or signature step; batched upgrades make staleness the resting
state. OWASP A08 (software and data integrity), A06 (vulnerable and outdated components). Mike's
decision to publish the list is the non-goal; the unreconciled argument and the unguarded install
path are not. V5, V6. *Counsel:* write the default-versus-divergence reconciliation into the
Bearing; define *trusted* (the OS package manager or the project's own signed release, never
`curl | bash` without the principal); for a no-ask install require a pinned version and the
project's checksum or signature where one is published.

**TB5 — MODERATE.** *The method index still states the reversed rule.* `docs/method/README.md:45`:
"keep a tool manifest; approved-but-missing may be installed; keep the personal inventory
machine-local." The inventory is now in atelier by ruling. The index is the first thing a reader
meets. V3, V4. (`240/010`'s original text classes the toolbox as private instance context; it is
marked "for context" and historical — noted, not a finding.) *Counsel:* one-line sweep.

**TB6 — minor.** *Three vocabularies for one set, and the bridge is unwritten.* approved/unapproved
at `00-APEX.md:87, :114`, `AUTONOMY.md:13, :104, :119`, the floor region and template,
`session-onramp/SKILL.md:50`, `method/README.md:17`; listed/expected in TOOLBOX's table, install
rule and `AUTONOMY.md:34`; manifest in TOOLBOX's intro and allowlist section. Each site still
names one set; no site says *unapproved = not on the expected toolbox*. V5. *Counsel:* one
sentence in TOOLBOX's intro, and retire "manifest" there or keep it as the practice's name.

**TB7 — MODERATE.** *The floor region names a path no child can resolve.* The bullet reads
`method/TOOLBOX.md`; `pathscan` resolves it in atelier by docs-relative shorthand (0 findings on
the delta files here), and reports `[missing-path]` on a scratch copy of the template used as a
child's `CLAUDE.md` (reproduced: exit 1, the TOOLBOX line flagged). A child cannot allow-mark the
line without drifting from the verbatim floor. Already filed by a public child as `320/610`
(2026-10-16) and verified by a worker; recorded here as corroboration with my own reproduction,
not a new item. The repair is a floor change, so it re-enters the pin-bump cycle. V3, V5.
*Counsel:* spell it as prose a child's scanner does not read as a local path, or carry the
allow-marker in the canonical text so every copy inherits it.

**TB8 — minor.** *The principal's words and the wording around them.* (i) Quote 1 asks for "a list
of tools to expect … and how (a method) to find them", and hedges "does not *necessarily* mean
paths need to be published". The text hardens the hedge into "never a machine's paths, hostnames,
accounts or token scopes" and adds "install routes" — the *Get* column and the install grant are
the session's design, not his words; label them so. (ii) The Bearing says the list is "published
by ruling" while the correction paragraph says which groups are on it "was Mike's answer … not a
ruling (`420/020`)" — the ruling covers the home, the answer covers the content; say which.
(iii) Quote 2 ("still ask … a normal action") → "Batch upgrade asks" is the session's addition.
V1. *Counsel:* keep each quote, mark each inference as the session's.

**TB9 — minor.** *"Two things, kept separate" no longer describes its body.* Both bullets now say
"this doc"; the separation that matters (public list / machine-local detail) is one trailing
sentence plus the Bearing. The correction paragraph (history of a mis-attribution) sits inside
the layering section rather than beside the Bearing. Lens 1. *Counsel:* rename the heading to the
split it now makes, and move the correction under the Bearing.

**TB10 — minor.** *The finding method asks the installer where it is, which needs the installer on
`PATH`.* Step 2: `$(brew --prefix)/bin` and `$(npm prefix -g)/bin`. When the tool is off `PATH`
because the installer's own bin is off `PATH`, the question cannot be asked; a careless shell
substitution then yields `/bin`, which exists, and reads as success — I made that error once in
this pass before re-checking. Here Homebrew is absent so the line yields nothing; the venv line
(`*venv*/bin` under `~/.local`) found one venv and not `az`, which is correctly reported missing.
Steps 1 and 3 worked as written. *Counsel:* add the fallback for each installer (the two standard
macOS Homebrew prefixes; `npm`'s default global prefix) and "if the installer is itself on `PATH`".

**TB11 — note (security).** The table discloses the estate's provider mix and, via "per its
repo's onramp", that an unnamed private repo runs IKE scanning. No host, account, path or repo
name. Within the grain Mike ruled public; recorded so the reader has seen it.

**TB12 — note.** `ccpdf` is an atelier instrument absent from the estate-tools row (the
`instruments/` README says it installs as `pdftoppm`), while `pdftotext` via poppler is listed —
a "keep the list current" gap. `09a61b4` (2026-10-17) is a third later commit on a delta file the
brief did not name; it appended one tool to that row and moved nothing else.

**TB13 — minor.** No `CHANGELOG.md` entry for the 2026-10-03 reversal; the changelog records
doctrine changes (its 2026-07-12 entry introduced TOOLBOX with the rule this delta reverses).
V3. *Counsel:* one *Changed* entry under *Unreleased*.

## Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 5 MODERATE · 5 minor · 2 note.**

The list and the finding method are sound and reproduce live; the grant attached to the list is
the defect, and it contradicts the floor the same doctrine inlines into every child.

## Standing checklist

- **V1** — TB1 (grant stronger than its authority), TB3 (table under-states the Mike-run class),
  TB8 (inferences presented beside quotes). Five factual claims in the delta re-driven ✅.
- **V2** — ledger below; every re-run reproduced.
- **V3** — TB5, TB6, TB7, TB13.
- **V4** — list has one home ✅; stamped copy identical ✅; README restates the rule (TB5).
- **V5** — TB1, TB2, TB3, TB4, TB8(ii).
- **V6** — TB4, TB11; `/security-review` discharged by grounds above.
- **V7** — provenance in the brief and repeated above ✅.

## Re-run ledger

| Command (from the worktree root, `nice -n 10`) | Result |
|---|---|
| `git merge-base --is-ancestor 8acfff1 HEAD` | ancestor ✅ |
| `git show --format='%h %s' --stat 55572b1`; diffs on the four paths; `1ffefc7`, `89ff0d8`, `09a61b4` on delta files | read; delta unmoved except one row (TB12) |
| `python3 tools/coldsweep.py --root <wt> --also-exclude ×5 -i '<vocabulary pattern>'` | 48 hits / 639 files; 398 barred; no `--include-barred` |
| `python3 tools/stampscan.py --warn --root . .` | clean, exit 0; template `[identical]` to region, 93 lines |
| `python3 tools/blockscan.py --check --warn --root .` | clean, exit 0; estate-resources bullet is unmapped by design (map comment) |
| `python3 tools/leakscan.py --root . .` | clean, exit 0 (structural + local; `local-term×3` expected) |
| `python3 tools/pathscan.py --root . .` | exit 1, 70 findings, **0 on the delta files**; pre-existing elsewhere |
| `pathscan` on a scratch copy of the template as a child `CLAUDE.md` (scratchpad `TB-childrepro/`) | exit 1; `method/TOOLBOX.md` flagged — TB7 reproduced |
| `python3 tools/floor.py --plane ci --root .` | exit 0; secretscan 23 advisory, leakscan cover-not-guaranteed, 4 warn-only, rest ✅ |
| Finding method step 1 (`command -v`, `which -a`) over all 48 listed names + `tshark`, `ccpdf` | 33 on `PATH`; off: `az`, `ruff`, `mypy`, `pytest`, `pre-commit`, `pipx`, `brew`, `gtimeout`, `gtac`, `groff`, `pdftotext`, `docker`, `cloudflared`, `ike-scan`, `tiki`, `ccpdf` |
| Step 2: `python3 -m site --user-base` per interpreter; `npm prefix -g`; `brew --prefix`; `*venv*/bin` under `~/.local`; Homebrew at both standard prefixes | user-base bins exist ×4; npm global bin exists (holds `wrangler`); no Homebrew anywhere (TB3, TB10); one venv, not `az` |
| Step 3: `python3 -m playwright --version` per interpreter | works from the system interpreter only ✅ |
| macOS claims: `mandoc`, `tcpdump` system; `openssl version`; `timeout` | LibreSSL ✅; no `timeout` ✅; both system ✅ |
| Full Python suite, `node --test` | not run — no code in the delta; nothing they exercise changed |
| After the resume: `wrapscan.py` and `datescan.py` on this file only | both clean, exit 0 (the reviews directory is wrapscan-ignored by `.wrapscanignore`) |

## Follow-up checklist (for the principal's decision; nothing applied)

- [ ] TB1 — decide what a row *is*: a recorded grant (who, when) or a mere expectation; give the
      child case its route.
- [ ] TB2 — name the ask-non-blocking class and say what an unattended run does.
- [ ] TB3 — flag every admin/GUI route; say whether Homebrew is expected on the estate's machines.
- [ ] TB4 — write the default-versus-divergence reconciliation; define *trusted*; pin and verify.
- [ ] TB5, TB6, TB13 — sweep `method/README.md`, TOOLBOX's intro vocabulary, the changelog.
- [ ] TB7 — already on the board as `320/610`; the fix is a floor change (pin-bump cycle).
- [ ] TB8, TB9 — label inferences as the session's; retitle the layering section.
- [ ] TB10 — fallbacks in the finding method.
- [ ] TB12 — `ccpdf` row, or a reason it is not expected.

### Reconcile

Phase 1 committed as `c824287`; the sibling's text was then passed to me by the orchestrator, and
I opened the intent record (`docs/sessions/2026-10-03-0144-…`, the toolbox passages), the queue
pointer, `320/500`, `320/510`, `420/020`, and the toolbox-related passages of the four prior
verdicts the sibling names. The landing commit's body was read as the sibling describes it.
Phase-1 text above is unrevised.

**Against the seven seeded questions.** Each one lands on a finding formed before I opened the
sibling: Q1 → TB4; Q2 → TB1; Q3 → TB6; Q4 → TB2; Q5 → TB9; Q6 → TB8; Q7 → TB3 and TB4. Full
overlap is recorded, not claimed as corroboration of either side (REVIEW § *What review is not*):
the brief-writer and I read the same delta with different context, and both arrived at the same
seven seams; what it does show is that none of them needed the author's framing to find.

**Against the intent record and the commissioning items, per finding:**

- **TB1 (MAJOR) — stands, sharpened.** Mike's 2026-10-03 words in `320/500` are wider than what
  TOOLBOX quotes: *"If the tool is on the list and its not installed (or needs an update) then
  claude should expect that its approved to use that tool, upgrade it to keep it working etc."*
  So the grant for a **listed** tool is his, verbatim, and the doc leaves that sentence out. What
  no record carries is a word from him on who adds a row afterwards: he asked the session to
  *propose* candidates ("Any others you can think of … that I should be including?") and then
  picked groups — an answer, as `320/500` itself labels it. The standing "a session updates this
  list" bullet has no ruling behind it and is the session's rule; the contradiction with
  AUTONOMY's *Widening your own authority* stands. The record's own account — "An unlisted tool
  still stops at the floor" — is true only until the session lists it.
- **TB2 (MODERATE) — stands.** The record says "Upgrades are a routine ask, in his words"; his
  words settle the *weight* of the ask, not where it sits in AUTONOMY's two classes nor what an
  unattended run does. No record addresses that.
- **TB3 (MODERATE) — stands.** `320/500`'s one-machine probe and the record's "this Mac's
  inventory" are the same machine I probed: Homebrew absent, tools in the user bin. The table's
  *Get* column was not grounded in that inventory; the *Find* column was.
- **TB4 (MODERATE) — stands, with precedent.** The 2026-08-02 and 2026-08-03 verdicts (PS2,
  PSA1) had Mike rule *accept + name it* for exactly this class — the seed templates stay
  published and TOOLBOX names the residual ("the estate default remains mapped"). The toolbox
  table is the same class and the residual is not extended to it. The counsel in TB4 is that
  precedent applied; the decision remains his.
- **TB5, TB13 (MODERATE, minor) — stand.** The record lists the surfaces it fixed (TOOLBOX's
  scaffold text, the floor bullet, a child's record); `docs/method/README.md` and the changelog
  are not among them.
- **TB6 (minor) — stands, reframed.** The bridge *listed = approved* exists in his words (above);
  it is only unwritten in the doctrine. The repair is a quotation, not a new rule.
- **TB7 (MODERATE) — stands.** The record and `320/510` both say the floor change "reaches each
  child when it re-stamps"; `320/610` is what the first re-stamp found. The intent record did not
  anticipate it, and nothing in the delta's records tested the bullet from a child's tree.
- **TB8 (minor) — (i) corrected at reconcile.** I wrote that "the install grant [is] the
  session's design, not his words"; the grant for listed tools is his (the sentence quoted under
  TB1). What remains the session's is the hardening of "not necessarily … paths" into "never …
  paths, hostnames, accounts or token scopes", the *Get* column as a published artefact, and
  "Batch upgrade asks". (ii) stands: `420/020` is the commissioning item for exactly the
  answer/ruling distinction the Bearing blurs, and the record says the run "relabelled" its
  records to match — the Bearing was missed. (iii) stands.
- **TB9 (minor) — stands.** The 2026-07-10 foundation verdict (A5) held the TOOLBOX
  practice/instance split up as the model for restructuring AUTONOMY and STORAGE; the delta
  changed the model without saying so at the sites that cite it. See TB14.
- **TB10 (minor) — stands.** `320/500`'s option C (a probe reporting present / off-`PATH` /
  missing by name) was ruled "B, then C" on 2026-09-28 and the record says C "is not built …
  whether to build it is open". A built probe is where the method's fallbacks would live.
- **TB11, TB12 (notes) — stand.** `320/500`'s probe lists `sshd`, `pwsh`, `kubectl`, `tofu` as
  seen or missing; none is in the table, which is consistent with the groups he picked. `ccpdf`
  remains the one atelier instrument unlisted.

**Formed at reconcile:**

- **TB14 — note.** `docs/method/COMMUNICATION.md:16` reads "The same split as `TOOLBOX.md`,
  applied to communication" — pattern in the repo, values in the person-level context. That is
  the *old* TOOLBOX split; the new TOOLBOX publishes the instance. The analogy now points at a
  shape TOOLBOX no longer has. Seen as a grep hit in the phase-1 sweep, not written up then; a
  mirror site for TB9 (V3). *Counsel:* "the split `TOOLBOX.md` used to make" or point at the
  Bearing's list/detail split instead.

**Prior verdicts, otherwise.** Foundation H3 recorded TOOLBOX once carrying a fabricated AUTONOMY
quotation (2026-07-10, fixed); TB8's attention to what is quoted versus inferred is in that class.
The 2026-10-04 pii-by-purpose verdict touches the template's *Hard constraints* only, outside this
delta, as the sibling says.

**Overall, restated:** **PASS-WITH-FINDINGS — 1 MAJOR · 5 MODERATE · 5 minor · 3 note** (TB14
added at reconcile; no phase-1 severity changed).

## Deferred material — folded in at reconcile

# Sibling to the expected-toolbox cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-10-16-1510-expected-toolbox-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-10-16 UTC by the Opus brief-writer named in the brief's provenance; it
forms no finding. Fold this file in below the reconcile and delete it at phase 2.

## Intent and commissioning records

- Intent record: `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` —
  **not opened by the brief-writer**.
- Commissioning board items (single grep lines seen, never read whole):
  `320/500` (sessions cannot find installed tools), `320/510` (sessions credited Mike with a
  private tool list), `420/020` (an answer is not a ruling).
- The landing commit's message body (read by the brief-writer): it quotes the principal, says the
  floor change reaches each child when it re-stamps, and records that `320/510` and `420/020` were
  applied in the same change.

## Prior verdicts on these surfaces (named by filename grep, not opened, not exhaustive)

- `docs/reviews/2026-07-10-atelier-foundation.md`
- `docs/reviews/2026-08-02-2210-publish-surface-delta-cold.md`
- `docs/reviews/2026-08-03-0653-publish-surface-application-cold.md`
- `docs/reviews/2026-10-04-2215-pii-by-purpose-cold.md` — same template file, a later commit

## The pointer's own lens hints

None. The pointer is refs-only; its last sub-bullet is the brief-writer's orchestrator's claim.

## Overlap with sibling passes of this batch

No other 2026-10-16 pass touches TOOLBOX, AUTONOMY or the floor region. The template
`docs/build/templates/CLAUDE.md` was also changed by `1ffefc7` (the 2026-10-04 pii-by-purpose
pass's subject), so a runner should read that region at HEAD, not at `55572b1`.

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. TOOLBOX's allowlist section argues that publishing what runs unattended turns reconnaissance
   into a plan. The new table publishes the expected tools — including network and security
   tooling and the estate's own CLIs — together with a grant to install any of them unasked. Is
   that the same exposure in a different shape, and does the closing *Bearing* line reconcile it?
2. "When a session finds a tool the list lacks … it updates this list", plus "Listed and missing
   → install it", lets a session list a tool and install it in one commit. Does that collide with
   AUTONOMY's floor that an agent records a grant and never originates one?
3. "Unapproved tool" survives in AUTONOMY's intro and floor, the apex, the floor region, the
   template, the onramp skill and `docs/method/README.md`; TOOLBOX's own opening still says
   "approved". Is "approved" now "listed", and who approves a row?
4. "Upgrading is a routine ask, not a floor stop": AUTONOMY has two classes. Is a third defined
   anywhere a session would find it, and what does an unattended run do with a stale tool?
5. The heading *Two things, kept separate* now introduces two bullets that both say "this doc".
   Did the practice/instance layering survive, or collapse silently into one public instance?
6. The surrounding text turns the quoted "does not necessarily mean paths need to be published"
   into "never a machine's paths, hostnames, accounts or token scopes" — a stronger rule than the
   quote. Whose rule is the stronger one?
7. Several *Get* routes are `.pkg` or vendor installers that need admin rights, but only Homebrew
   is flagged as Mike's to run; user-level pip and global npm routes pull unpinned packages. Does
   "a trusted package manager" cover them?
