# Cold pass — publishscan's round-2 denylist

**Pass type:** code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection: this pass's reviewer and orchestrator are both `claude-fable-5-1`.
**Status:** BRIEF WRITTEN 2026-10-03 0357 UTC; the review runs under the
orchestration below, by a reviewer that is not the brief-writer.
**Queue pointer:** `docs/roadmap/160-doctrine-review-owed/470-rule-4-cold-pass-queued-publishscan-round-2.md`.
**Why it earns a review:** publishscan is a blocking floor scanner every child runs; a widened never-publish list changes what commits in every repo on the estate, and three private children are expected to go red at their next CI run on it.

## Spawn provenance

- **Author of the work under review:** the 2026-10-03 queue run (an Opus
  orchestrator with dispatched workers) that landed the commits named under
  *What the work is*. This brief-writer was not that session, was neither
  started nor instructed by it, and has edited none of the delta's paths.
- **Who wrote this brief:** an atelier session Mike opened on 2026-10-03 with
  the prompt "Do all cold reviews and any other work dependent on fable", on
  the Fable tier (`claude-fable-5-1`), orchestrating six rule-4 passes queued
  by that run. It wrote this brief from the queue pointer, the landing commits'
  subjects and `--stat` file lists, and the delta paths' names; it did not open
  the intent record.
- **Who takes the review:** a fresh Fable subagent (`claude-fable-5-1`) spawned
  by the brief-writer with this brief as its only framing. It is not the
  author's session and was not instructed by the author. The reviewer repeats
  its own provenance in the verdict.
- **Orchestration shape, disclosed per rule 4:** reviewer-plus-orchestrator. The
  orchestrator holds the `.deferred.md` sibling outside the worktree and
  outside the harness scratchpad (subagents can read the scratchpad), commits
  the reviewer's phase-1 findings unrevised, then releases the sibling's text by
  message; the reviewer appends a reconcile section; the orchestrator folds the
  sibling in and updates the pointer. The orchestrator forms no finding and
  writes no severity. Both seats are Fable, so the off-tier clause is not
  invoked; the shape is stated anyway so the record is auditable.
- ⚠️ **Brief-writer's exposure, disclosed** (rule-2 material it met before
  writing): the authoring run told this session over the cross-session channel
  that the pointer existed and named its subject in a phrase; nothing else from
  that run was read. Earlier in the same sitting this session commissioned
  read-only inventories of the board's open items and of every verdict in
  `docs/reviews/`, for a ruling round; the summaries it received include prior
  findings on the surfaces under review. Those summaries are author-side
  framing this pass must meet cold; every line of them that bears on this delta
  has been moved to the sibling and kept out of this brief. The brief-writer
  also read the 2026-09-25 batch's staged-plane brief as a formatting template,
  the session index entries of 2026-09-19 to 2026-10-01, and, as doctrine at
  onramp, `docs/method/REVIEW.md`, `docs/method/00-APEX.md` and
  `docs/method/COMMUNICATION.md` § *Asking for a ruling* at HEAD.

## What the work is

Landing commits (diff these; review the paths at HEAD, `17c75a9` or later):

- `a91d9b6` (2026-10-03) — merge of `a7d8fdd`: publishscan round 2, the shapes the estate survey found plus standard practice (board `260/040`)

Delta paths:

- `tools/publishscan.py` — the pattern table and any matching changes
- `tools/test_publishscan.py` — its tests
- `tools/README.md` § *publishscan*

`tools/floor.py`, the hook and the workflows did not change; the scanner floats at `main` for every child, so the new list is live for them on their next CI run without a pin bump.

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code,
tests and live behaviour. The lenses organise it; they do not bound it.
Non-goals are the only narrowing and are themselves reviewable.

Driven, not read: in a scratch repo, plant one file for every new pattern at the root, two levels deep, under a dot-directory and under a vendored directory; plant the near-misses the pattern should not catch (an `.example`, a `.md` describing the file, a directory with the file's name); run the scanner on the tree plane and the `--staged` plane, and record exit codes and listings. Compare the behaviour at the landing commit's parent and at HEAD on the same tree. **Non-goal:** the board item that commissioned round 2, and whether the three children's reds are legitimate — you may not scan other repos.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself. A denylist presumes names identify the class: find the secret-bearing file no pattern names and the harmless file a pattern does. A blocking gate that widens presumes the fleet can absorb reds: what does a child do when it is red on a file it must keep?
2. **Correctness & quality.** Read all of `tools/publishscan.py` and its tests. Run `--selftest`, `tools.test_publishscan`, the full Python suite once, and every state in *Scope*. Check every pattern matches at the depth the docstring claims.
3. **Completeness / harvest.** Every surface that lists what publishscan catches: `tools/README.md`, the module docstring, the floor registry `why`, `CHANGELOG.md`, the child workflow template. Do they agree with the code?
4. **Security & privacy** — mandatory. This is a security gate. Check the escape routes: the ignore file, the allow marker, a case or Unicode variant of a listed name, a symlink to a listed file, a listed file staged as a rename. The house scanner is discharged by grounds (landed delta; the pending diff is this brief) — say so, and deliver the code-altitude read by hand, against the OWASP catalogue.

## Re-run obligation

Re-run, do not read. A recorded proof is a claim that can be stale at the commit
that recorded it; a proof you have not re-run is not one you can close on. Lift
floor invocations from `.githooks/pre-commit`, `tools/floor.py` and
`.github/workflows/ci.yml` rather than guessing.

- `python3 tools/publishscan.py --selftest`; `python3 -m unittest tools.test_publishscan`; the full Python suite once
- the floor on both planes at HEAD
- every planted shape in *Scope*, both planes, parent and HEAD

## House rules for this run

- You work in the shared review worktree `/Users/mike/worktrees/atelier-review-430`
  (branch `review-430-1003`), read-only except for THIS brief file. Other
  reviewers are working there at the same time on their own briefs; never open
  another `docs/reviews/2026-10-03-*` file — it is another pass's framing. Run
  **no git command that writes** there (no add, commit, stash, checkout,
  worktree, reset, clean). Read-only git (`log`, `show`, `diff`, `blame`) is
  fine. Mutation probes, scratch children and checkouts of older commits go in
  your own clone: `git clone /Users/mike/worktrees/atelier-review-430
  <scratchpad>/PL/probe` under the session scratchpad, named by your
  prefix so parallel reviewers do not collide.
- One heavy process at a time on this machine: run the full suite at most once,
  in the foreground with a long timeout; if a memory-probe test times out, note
  it as environmental and re-run that test file alone before recording it.
  Never scan any tree outside the worktree or your scratch clone, and never
  point a scanner at the machine's other repos. Other sessions are live on this
  machine and in this repo's primary checkout; touch nothing there.
- `/security-review` is **discharged by grounds**: it reads the session's
  pending diff, which here is other passes' drafts and this brief, and this is a
  landed-delta review. State that line in your lens-4 answer and deliver the
  code-altitude read by hand.
- Dates in your verdict are absolute ISO-8601 from `date -u` (the hook-plane
  `datescan` reds relative words such as "yesterday" or "next week" and would
  block the orchestrator's commit). Wrap prose at ≤ 100 columns. NZ English.
  Never quote a secret, a placeholder token, an email address, a private
  repo's name or any personal detail — this repo is PUBLIC; describe, don't
  quote.
- Review deep, not fast. A finding needs a probe or a re-driven claim behind it,
  not reasoning alone; a clean lens needs the trail that earned it.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held by the orchestrator outside the worktree under the rule-1 split and released only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer
`docs/roadmap/160-doctrine-review-owed/470-rule-4-cold-pass-queued-publishscan-round-2.md`
(it carries the author's framing and this pass's claim line), and:

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md` (the
  intent record)
- the board item `docs/roadmap/260-*/040-*.md` (the commission)
- the verdicts `docs/reviews/2026-08-02-2210-publish-surface-delta-cold.md`, `2026-08-02-*-publishscan-cold.md`, `2026-08-03-*-publishscan-application-cold.md`

Sweep with `python3 tools/coldsweep.py --root
/Users/mike/worktrees/atelier-review-430 --also-exclude
docs/roadmap/160-doctrine-review-owed/470-rule-4-cold-pass-queued-publishscan-round-2.md
--also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005 <pattern>` — rule 2's
default bar plus the items above; `--include-barred` only with disclosure in
the verdict. Reading the *delta* is never barred: the code, its tests, the
README entries and the registry are the subject. What is barred is the author's
narrative of why, and the verdicts that recorded it.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list.
Then append your verdict below a `---` divider in THIS file: provenance repeated
(how you were spawned, your tier, what you read), per-lens answers, findings
with stable IDs (prefix `PL`: `PL1`, `PL2`, …) and severities
(MAJOR / MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL
line with counts, a re-run ledger with the commands and their results, and a
follow-up checklist. Then STOP and report to the orchestrator that phase 1 is
written. Do not open the sibling (it is not in the tree); do not edit the queue
pointer, the board, or any file but this one.

**Phase 2.** On receipt of the sibling's text, append `### Reconcile` beneath
your verdict: per-finding notes against the seeded questions and the intent
record, any finding formed at reconcile marked as such, and the overall line
restated. Never revise phase-1 text. The orchestrator folds the sibling in below
your reconcile.

Findings are the principal's to decide (rule 3): record all, apply nothing;
your counsel per finding is welcome, labelled as counsel and kept beneath the
finding.

---

## Verdict — phase 1 (written 2026-10-03 04:33 UTC)

**Overall: PASS-WITH-FINDINGS — 1 MAJOR · 5 MODERATE · 4 minor · 4 note (14).**
The delta's own claims hold under re-run: all 57 new globs red at the root, two
levels deep, under a dot-directory and under a vendored directory on both planes;
none of them fired at the parent; the look-alikes the tests name stay green; and
atelier's own tree is clean on both planes at `0a669e7`. The MAJOR (PL1) and the
first two MODERATEs are in the gate's live behaviour rather than in the delta's
lines, and predate it; the brief's lens 4 asked for exactly those probes, so they
are recorded here with that provenance stated.

### Provenance

- **Reviewer:** `claude-fable-5-1`, a fresh subagent spawned by the brief-writer
  with this brief as its only framing. Not the author's session (the 2026-10-03
  queue run); neither started nor instructed by it. Fable tier, so the off-tier
  clause is not invoked.
- **Read:** this brief; the delta at HEAD (`tools/publishscan.py`,
  `tools/test_publishscan.py`, `tools/README.md` § publishscan, all three byte-
  identical from `a91d9b6` through `0a669e7`); `tools/floor.py`'s registry entry;
  `.githooks/pre-commit`, `.github/workflows/ci.yml` and `floor.yml`;
  `docs/method/GUARDS.md` § the four conditions; `CHANGELOG.md` (top section);
  `docs/build/templates/gitignore` and `templates/workflows/floor.yml`; the
  landing commits' messages and `--stat`. Nothing barred was opened; the sibling
  was not opened; no other `docs/reviews/2026-10-03-*` file was opened.
- **Worktree state, disclosed:** at my first read the worktree HEAD was
  `4ff8de5`, whose history did NOT contain `a91d9b6` — the checked-out
  `publishscan.py` was the 392-line pre-round-2 file (`merge-base
  --is-ancestor` exit 1). I recovered via the scratch clone at `ca61feb`
  (`a91d9b6` an ancestor; delta paths identical to the merge). The orchestrator
  then merged `origin/main` into the worktree (HEAD now `0a669e7`); I verified
  `a91d9b6` and `5d087ec` are ancestors, that `5d087ec` touched no publishscan
  file, that no commit after `a91d9b6` touches the delta paths, and re-ran the
  floor, selftest and unit tests at `0a669e7`. Only `tools/pathscan.py` differs
  in `tools/` between `ca61feb` and `0a669e7`, so every probe at `ca61feb` stands
  at HEAD. See PL5.
- **Scratch:** clone and all fixtures under the session scratchpad `PL/`. No
  other repo on this machine was scanned. No git command that writes was run in
  the worktree.

### Lens 1 — approach & assumptions

Load-bearing assumptions, named: (a) a path's NAME identifies the class; (b) git's
listing of tracked paths is the complete, literal set the patterns see; (c) a
widened blocking gate lands by float and the fleet absorbs reds through the two
hatches (`.publishscanignore` glob with reason; `.atelier-floor.json` advisory
with `why` + `review-by`); (d) the ignore-file hatch is reviewable because a
reviewer reads the file.

- (a) fails both ways, as a denylist must, and the delta says so. The harmless
  files a pattern names are listed under PL9; the secret-bearing files no pattern
  names (24 probed, all green) are PL10.
- (b) is false under git's default `core.quotePath` — PL1.
- (c) holds mechanically: the hook plane judges only staged adds, so a child's
  existing tracked shapes do not block its commits; its CI goes red at the next
  push over the whole tracked set. There is no `--warn` transition for new
  patterns (round 1's advisory offering is per-check, not per-pattern), and the
  record a child would read to learn why — `CHANGELOG.md` — is silent (PL4).
- (d) is the assumption round 2 leans on hardest, and it is where the gate is
  weakest: an exemption is visible only to someone who opens the file, because the
  tool's own output never names it — PL2.

### Lens 2 — correctness & quality

Read all of `publishscan.py` (501 lines) and its tests. The planting matrix
(`PL/plant.py`): 57 globs × 4 locations = 228 expected reds, 228 observed on
each plane at HEAD, 0 at the parent (the parent's 3 findings were the
`.env.example`-class, round-1 behaviour); staged and tree planes agree exactly.
Every pattern matches at the depth the docstring claims. Quality notes: PL6 (one
glob reaches past the basename), PL8 (a shadowed table entry and first-match
reason attribution). The unit tests exercise `matches()` directly for round 2 and
never drive the planes with a round-2 file; the matrix above does, so the gap is
closed here but not pinned in the suite (counsel under PL8).

### Lens 3 — completeness / harvest

| Surface | Agrees with the code? |
|---|---|
| module docstring, ROUND 2 paragraph | yes; left-out list includes `*.pub` |
| `NEVER_PUBLISH` table comment | yes; left-out list adds `.vscode/extensions.json`, `.editorconfig`, defers `launch.json` |
| `tools/README.md` § publishscan | yes for the shapes; its left-out list omits `*.pub`; heading still "no machine-local config is tracked" |
| `tools/floor.py` registry `why` | stale — names only machine-local config and the allowlist |
| `CHANGELOG.md` | **no entry** for round 2; top section is dated 2026-09-20 |
| `docs/build/templates/workflows/floor.yml` | lists no shapes (transport only) — nothing to harvest |
| `docs/build/templates/gitignore` | covers `.DS_Store`, `*.swp`, the settings pair; Python/Node litter commented out; none of the key/log/db shapes |

Findings: PL4 (CHANGELOG, `why`, heading, three differing left-out lists), PL12
(template gitignore).

### Lens 4 — security & privacy

`/security-review` is **discharged by grounds**: it reads the session's pending
diff, which here is other passes' drafts and this brief, and this is a
landed-delta review. The code-altitude read was done by hand against the OWASP
catalogue: subprocess calls are list-form, no shell (A03 injection: closed); the
tool reads no file contents; every echoed string passes `_strip_controls` at both
ingest seams (verified by the suite's control-character tests); `fnmatch` globs
are fixed, so no pathological matching on a hostile path; error paths all exit 2.
Escape routes, driven (`PL/escape.py`), each in its own scratch repo:

| Route | Result | Finding |
|---|---|---|
| listed file under a directory whose name carries a macron; listed-shape file whose own name does | **green on both planes, parent and HEAD**; red with `core.quotePath=false` | PL1 |
| 8 case variants of listed names | all green | PL7 |
| homoglyph in the name (deliberate evasion) | green — outside the mistake threat model | note, lens text |
| tracked symlink NAMED like a listed file; innocent-named symlink pointing AT one | named: red; pointing: green (its content is a target path, not the key) — by design | none |
| staged rename INTO a listed name; OUT of one | into: red on the staged plane; out: green — content moved is the content scanner's layer | none |
| `.publishscanignore` with one reasoned `*` line | **exit 0, "clean — 4 tracked path(s), none in the never-publish class"**, no suppression line, JSON carries no count | PL2 |
| ignore glob `.env` against tracked `tests/fixtures/.env` | still red (pattern matches at depth, ignore glob is literal) — fails closed | PL11 |
| `.publishscanignore` in a subdirectory | not read; still red — fails closed | PL11 |
| the public record of the delta | commit body states which secret-carrier shapes the survey found tracked in the estate | PL3 |

### Findings

**PL1 — MAJOR — a non-ASCII character anywhere in the path makes the file
invisible to every pattern.** `git ls-files` and `git diff --cached --name-only`
wrap any path containing a byte above 0x7f in double quotes with octal escapes
(default `core.quotePath=true`). The scanner matches the quoted string, so a
pattern anchored at the end (`*.key`, `*/.env`, `*/id_rsa`) never sees the real
tail — the string ends in `"`. Probe 1a–1c: a listed `.env` and a listed SSH key
name under directories with macrons, and a `.key` file whose own name has one,
pass green on both planes at the parent and at HEAD; the ASCII control in the
same tree reds. Probe 1d: with `core.quotePath=false` all four red. This is a
silent fail-open in a blocking gate, reachable by ordinary use — this estate's
conventions mandate macrons on te reo Māori names, so a folder named that way is
not exotic here. Pre-existing (the `_git` seam is not in the delta); surfaced by
the lens-4 probe this brief required.
*Counsel:* pass `-z` to both git listings and split on NUL (strip controls AFTER
the split, since NUL is a C0 control), or run git with `-c core.quotePath=false`;
pin with a test that plants a macron-named directory. The fix is a few lines and
removes a whole class.

**PL2 — MODERATE — the ignore-file hatch is not principal-visible.** GUARDS.md's
third condition: a person can see the whole set of live allowances without going
looking. `leakscan`, `licenscan`, `wrapscan` and the floor's other hatched guards
print a `suppressed: … by .<tool>ignore` line and carry the count in JSON;
publishscan prints "✓ publishscan clean — N tracked path(s), none in the
never-publish class" whether zero or all N were exempted, and its JSON has no
suppressed field. Probe 6a: one reasoned `*` line exempts a tracked SSH key, a
`.env` and a log, and the floor board shows the check enforced and green. The
clean line is also literally false in that case. Pre-existing hatch; round 2
makes it load-bearing, because three children are expected red and a broad glob
is the cheapest way to go green.
*Counsel:* count exemptions and print them in the sibling scanners' `suppressed:`
grammar; add `suppressed` to the JSON (print the zero, per the comparable-fields
rule); consider refusing a bare `*` glob.

**PL3 — MODERATE — the delta's public record does what the delta's own rule
forbids.** The new docstring paragraph says a public file must not describe a
private repo's security posture, even unnamed, and files the survey's
secret-carrier finds as "standard practice and nothing more". The landing
commit's body (`a7d8fdd`, on public `main`) states which secret-carrier shapes
the survey found tracked in the estate; the table comment's `*.pem` note hedges
with "most of them", which tells a reader the remainder exists. No repo is named,
but the fact that such files sit in some estate repo's history is reconnaissance
of the kind the module docstring's own threat model describes. Pushed history
cannot be unpublished, so there is nothing to apply; the finding is for the
record and for the next commit body.
*Counsel:* a ruling that commit bodies and review verdicts on survey-derived work
carry the same "counts only, no posture" bar the source comment carries; and
drop the hedge from the `*.pem` note.

**PL4 — MODERATE — the fleet-visible behaviour change is unlogged and the
check's one-line description is stale.** `CHANGELOG.md` has no round-2 entry; the
ci.yml comment says per-gate history lives there and in the docstring, so a child
reading the changelog to understand a new red finds nothing. The registry `why`
("no machine-local config is tracked — publishing an agent's unprompted-command
allowlist…") and the README heading describe round 1's class; keys, dumps, logs
and caches are not config. The three left-out lists (docstring, table comment,
README) differ: `*.pub` is in two of three, `.vscode/extensions.json` and
`.editorconfig` in one, `launch.json` deferred in one.
*Counsel:* one CHANGELOG entry naming the widening and the hatches; reword the
`why` to the class ("no file whose publication weakens the repo is tracked");
make the left-out list live in one place and point the others at it.

**PL5 — MODERATE (process) — the review worktree did not contain the delta when
the review started.** Branch `review-430-1003` forked from `main` before
`a91d9b6`; a reviewer reading "HEAD" literally would have reviewed the 392-line
pre-round-2 file and could have passed it. The brief's "17c75a9 or later" and an
ancestry check caught it; the orchestrator has since merged `origin/main`. Also
in the same class: the brief's re-run form `python3 -m unittest
tools.test_publishscan` fails with an import error (the test imports its sibling
module bare); the working form runs from `tools/`.
*Counsel:* the brief-writer's checklist gains "worktree HEAD contains every
landing SHA (`merge-base --is-ancestor`)" and the ci.yml invocation form for the
tests.

**PL6 — minor — `.*_history` reaches past the basename.** `fnmatch`'s `*` spans
`/`, so the glob reds any extension-less path ending `_history` beneath a
leading-dot top directory: probe 7 reds `.github/release_history` and
`.ci/job_history`. `._*` has the same shape (a directory named `._x` reds
everything under it), at negligible real cost. New in round 2.
*Counsel:* match these two against the basename (`path.rsplit("/", 1)[-1]`), or
spell them `*/.*_history` with the root form kept.

**PL7 — minor — case variants pass.** Probe 2: `.ENV`, `ID_RSA`, `server.KEY`,
`App.LOG`, `Known_Hosts`, `.Npmrc`, `.Ds_Store`, `thumbs.DB` all green.
`fnmatch.fnmatch` is case-sensitive on POSIX and case-insensitive on Windows, so
the gate's answer depends on the host. Pre-existing class; the uppercase
extensions are the realistic half (files that arrived from Windows).
*Counsel:* lower-case the path before matching, or use `fnmatchcase` on a folded
path, and state the choice in the docstring.

**PL8 — minor — a dead table entry and first-match attribution.** `*.db` precedes
`Thumbs.db`, so the Windows entry can never fire and `Thumbs.db` is reported as
"a local database — measured in the 2026-10-03 survey", a provenance it does not
have. The same ordering means any specific reason placed after a generic glob is
unreachable. The round-2 unit tests drive `matches()` only; no test plants a
round-2 file and runs a plane.
*Counsel:* order specific before generic, or assert in the selftest that every
entry is reachable by its own fixture; add one plane test with a round-2 shape.

**PL9 — minor — the harmless files a pattern names.** Probe matrix overreach at
HEAD: `*.iml` (JetBrains' own guidance tracks them when not using Gradle),
`*.tfvars` holding defaults, `*.log` and `*.db` test fixtures, a public key named
`*.key`, a bare `.key`. Pre-existing from round 1 and worth stating here because
the hatch is PL2: `.env.example`, `.env.sample`, `.env.template` — the canonical
documented forms — red under `.env.*`.
*Counsel:* exclude `*.example`, `*.sample`, `*.template` tails before matching;
decide `*.iml` on the estate's actual use; leave the rest to the hatch once PL2
makes it visible.

**PL10 — note — secret-bearing shapes no pattern names, for a round 3.** All
green at HEAD: `key.pem`, `private.pem`, `server-key.pem`; `id_ed25519_sk`,
`id_ecdsa_sk`; `.ssh/config`; `secring.gpg` and `.gnupg/private-keys-v1.d/*`;
`.pgpass`, `.my.cnf`; `.vault-token`; `*.keytab`; WireGuard `wg*.conf` and
`*.ovpn` (both carry private keys inline); `.s3cfg`, `.boto`;
`service-account.json`; `.secrets`, `secrets.yaml`; `.config/gh/hosts.yml`; and
`.bak`/`.old` copies of listed names (`id_rsa.old`, `.netrc.bak`,
`known_hosts.old`, `.zsh_history.bak`). The denylist's acknowledged limit; listed
so the next survey has a seed.

**PL11 — note — ignore-glob depth asymmetry and root-only ignore file.** A
pattern matches at any depth; an ignore glob is literal, so `.env  # reason`
does not exempt `tests/fixtures/.env`, and a `.publishscanignore` below the root
is not read. Both fail closed, and the printed remedy uses the full path, so a
user following it is fine; a user writing by analogy with the table is red with
no hint why.
*Counsel:* one sentence in the remedy text and the README.

**PL12 — note — the scaffold `gitignore` template does not anticipate round 2.**
It lists `.DS_Store`, `*.swp` and the settings pair; the Python/Node litter is
commented out; no key, log, database, dump or history shape. The hook plane
catches the add, so this is friction rather than a hole.

**PL13 — note — the printed remedy echoes the path unquoted.** `git rm --cached
<path>` and the `echo … >> .gitignore` line print the tracked path with controls
stripped but shell metacharacters intact; a hostile repo could make the
copy-paste hazardous. Pre-existing; low likelihood.
*Counsel:* `shlex.quote` the path in the two remedy lines.

**PL14 — note — the selftest's `bad_green` list is the only place `.editorconfig`
and `.vscode/extensions.json` are asserted green.** They are, and the unit test
`test_round2_does_not_overreach` repeats them, so this is a cross-reference for
the harvest (PL4), not a defect.

### Re-run ledger

All commands run from the scratch clone unless stated; SHAs given per run.

| # | Command | SHA | Result |
|---|---|---|---|
| 1 | `git merge-base --is-ancestor a91d9b6 HEAD` in the worktree | `4ff8de5` | exit 1 — delta absent (PL5) |
| 2 | same, after the orchestrator's merge; also for `5d087ec` | `0a669e7` | exit 0 both; `git log a91d9b6..HEAD -- tools/publishscan.py tools/test_publishscan.py` empty |
| 3 | `git diff --stat ca61feb 0a669e7 -- tools/` | — | only `pathscan.py`, `test_pathscan.py` |
| 4 | `python3 tools/publishscan.py --selftest` | `ca61feb`, `0a669e7` | OK, exit 0, both |
| 5 | `python3 -m unittest tools.test_publishscan` (brief's form) | `ca61feb` | ImportError (PL5) |
| 6 | `cd tools && python3 -m unittest test_publishscan` | `ca61feb`, `0a669e7` | 30 tests OK (20.1 s; 51.1 s under contention) |
| 7 | `python3 -m unittest discover -s tools -p 'test_*.py'` (ci.yml line 107), once | `ca61feb` | **exit 1, failing test NOT identified**: started 04:12:46 UTC, finished 04:28:49 UTC; my capture kept the last 15 lines, which were interleaved scanner stdout rather than the unittest summary; the harness moved the run to the background at its 600 s cap despite the foreground request; a sibling reviewer's identical suite ran concurrently. Not re-run wholesale (brief: at most once). |
| 8 | the four other test files that reference publishscan, each alone: `test_allowmarker` (25), `test_mixed_root` (3), `test_floor` (137, 124 s), `test_floorfleet` (118) | `0a669e7` | all OK, exit 0 — every test file that touches publishscan passes |
| 9 | `python3 tools/floor.py --plane hook --root <clone> --tools <clone>/tools` (pre-commit line 82) | `ca61feb`, `0a669e7` | exit 0; publishscan enforced, clean, 0 staged |
| 10 | `python3 tools/floor.py --plane ci --root <clone> --tools <clone>/tools` (ci.yml line 173 form) | `ca61feb`, `0a669e7` | exit 0; publishscan enforced, clean; 896 then 901 tracked paths |
| 11 | `PL/plant.py` — 57 globs × 4 locations + 171 near-misses + 10 look-alikes + 24 unnamed shapes, parent (`1437168`) and HEAD scanners, staged then tree | HEAD scanner = `ca61feb` (identical at `0a669e7`) | parent: exit 1, 3 findings both planes; HEAD: exit 1, 248 findings both planes, identical sets; 0 expected reds missed |
| 12 | `PL/escape.py` — 10 probes (table under lens 4) | HEAD scanner = `ca61feb` | as tabled; PL1, PL2, PL7, PL11 |
| 13 | `matches()` boundary probes (escape.py § 7) | `ca61feb` | PL6, PL8, PL9 |

Residual on the ledger: row 7. Publishscan's own suite and every suite that
imports it pass alone at HEAD (rows 6, 8); the whole-suite failure is in another
file and was not characterised. A solo re-run of the full suite is owed before
anyone closes on "suite green at HEAD"; it is not a finding against this delta.

### Follow-up checklist

- [ ] PL1: NUL-delimited git listings (or `core.quotePath=false`) + a macron test
- [ ] PL2: `suppressed:` line and JSON field for the ignore-file hatch
- [ ] PL3: ruling on the "counts only" bar for commit bodies; drop the `*.pem` hedge
- [ ] PL4: CHANGELOG entry; registry `why` and README heading; one left-out list
- [ ] PL5: brief-writer checklist — landing SHA ancestry; test invocation form
- [ ] PL6–PL9: basename anchoring, case folding, table order, `*.example` tails
- [ ] PL10: seed for a round-3 survey
- [ ] PL11–PL14: remedy text, template gitignore, `shlex.quote`, harvest cross-ref
- [ ] Ledger row 7: full suite re-run alone, failing test named
- [ ] Phase 2: reconcile against the sibling when released

### Reconcile (written 2026-10-03 04:40 UTC)

Opened after phase 1 was committed: the sibling's text (released by message), the
intent record `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
§ `260/040` and § `020/150`, the board item `260/040`, the filing `020/410`, the
2026-08-02 and 2026-08-03 publishscan verdicts (PB1, PA2) and the two board
passages the search for PL1's class turned up (`160/260` BA2, `160/390` SG1).
Worktree HEAD at reconcile `c3a3a7a`; the three delta paths are byte-identical
from `a91d9b6` to it. Phase-1 text above is unrevised.

**Against the seeded questions.**

1. *Every new pattern obeys the PB1 depth rule?* Yes — 228 of 228 planted
   reds, both planes (ledger row 11). Two qualifications the rule's mechanism
   carries: the `*`-spans-`/` behaviour PB1's fix relies on is what makes
   `.*_history` overreach (PL6), and the depth rule has a blind spot PB1 did
   not name — a quoted path (PL1).
2. *False-positive surface stated?* Partly. The left-out list and the
   look-alike tests state the considered half; `*.iml`, `*.tfvars` defaults,
   and log/database fixtures (PL9's round-2 half) are not stated anywhere a
   child reads. The `.env.example` half of PL9 is PA2, which the principal
   ruled deliberate on 2026-08-03; my counsel there is a re-raise of a ruled
   matter, marked as such, and carries no new severity.
3. *Fleet consequence stated on a surface a child reads?* No. It is stated,
   and corrected (pin bump → next CI run), in the board item and the intent
   record — both author-side. `CHANGELOG.md`, the README section and the
   scanner's own output are silent (PL4 confirmed). The correction's own
   lesson — the claim was reasoned, not checked against `floor.yml` — is the
   same shape as my ledger row 7 residual, so I hold it to the same bar.
4. *Documented path for a child that must keep a listed file?* Yes, two: the
   reasoned `.publishscanignore` glob (printed in the remedy) and the
   per-check advisory declaration (registry comment). `020/410`'s gap — a
   guard with no advisory form cannot adopt advisory-first — does not bite
   here, because publishscan has one. What qualifies the yes is PL2: the
   per-path route is invisible in the output, so the fleet's cheapest green
   is also its least reviewed.

**Against the intent record.** The record says the orchestrator rewrote the
worker's commit before merge so the public source carries no measured counts
for secret-carrier shapes and no vendor-specific filename, naming the exact
rule PL3 cites. That sweep reached the source and missed two surfaces: the
commit body (`a7d8fdd`) still describes the shapes, and the `*.pem` comment
keeps its hedge. PL3 stands at MODERATE with its cause now known — a privacy
rewrite with no checklist of the surfaces a landing commit publishes. The
record's blast-radius figures (3 private repos, 23 files) are outside this
pass's non-goal and were not checked; its "atelier stays clean (884 paths)"
is consistent with my 896 and 901 at later SHAs.

**Against prior findings.** PB1 (fixed) holds for every round-2 entry. PA2
(rejected as deliberate) is cross-referenced above. PS1[pub] and `260/060` P4
do not touch this delta. Neither prior publishscan verdict probed path
quoting, case, or hatch visibility, so PL1, PL2 and PL7 are first findings on
this guard.

**Findings formed at reconcile** (marked as such; severities are notes
because each sharpens a phase-1 finding rather than adding a defect):

**PL15 — note, formed at reconcile — PL1 is a recurring class, open twice
already on another guard.** `160/260` BA2 (MODERATE) and `160/390` SG1
(MODERATE) record that a staged item whose filename carries a macron is
C-quoted by `git ls-files` and silently dropped by the `board` guard's index
plane. Same seam, same cause, third sighting, second guard; neither prior
finding was fixed at the seam. For publishscan the cost is a silent pass on a
tracked private key rather than a stale index, which is why PL1 is MAJOR
where BA2 and SG1 were MODERATE.
*Counsel:* close the class once — one NUL-delimited git-listing helper shared
by every guard that reads `git ls-files` or `git diff --cached`, the natural
companion to `115/080` part 2's single-sourced ignore loader — and sweep the
other guards for the same call.

**PL16 — note, formed at reconcile — the pre-merge privacy rewrite had no
surface list.** Sharpens PL3; no new severity. *Counsel:* the brief-writer's
and the orchestrator's checklists both gain "surfaces a landing publishes:
source, tests, docs, commit body, PR body, board item, session record".

**Ledger row 7, restated on the orchestrator's instruction:** the full suite
ran once at `ca61feb` and exited 1 with the failing test unread (the capture
kept interleaved scanner output, not the unittest summary); it is recorded as
*run-result-unread*, not re-run now because two sibling passes are running
theirs, and the solo re-run stays an owed step on the checklist. Every test
file that imports publishscan passes alone at `0a669e7` (ledger rows 6, 8).

**Overall, restated: PASS-WITH-FINDINGS — 1 MAJOR · 5 MODERATE · 4 minor ·
6 note (16).** The delta does what it says; the gate it widens carries a
pre-existing fail-open (PL1) that the estate has now met three times and
closed nowhere, and an exemption hatch (PL2) that round 2 makes load-bearing
while leaving it invisible. Findings are the principal's to decide (rule 3);
nothing was applied.

## Folded sibling — released after the phase-1 findings were committed

The `.deferred.md` sibling the orchestrator held outside the worktree, folded in
verbatim at close; the reviewer met it only in phase 2.

# Deferred sibling — publishscan's round-2 denylist (PL)

Held by the orchestrator outside the worktree and outside the harness
scratchpad. Released to the reviewer only after its phase-1 findings are
committed. Folded into the verdict file at close.

## 1. The queue pointer's own framing (author's words)

> - ⏳ **Rule-4 cold pass queued: publishscan's round-2 denylist
> (`260/040`).** The run authored this itself (its dispatched workers'
> output counts as the run's authorship). It was queued at landing, and
> the run neither takes it nor spawns a reviewer for it. *Tier:* Fable,
> the principal-named review tier, checked at selection. *Pass type:*
> code cold pass, per `method/REVIEW.md` rule 4. *Delta, scoped to
> paths:* `tools/publishscan.py`, `tools/test_publishscan.py` and
> publishscan's section of `tools/README.md`. It landed on `main` on
> 2026-10-03, in merge `a91d9b6`.
> *Intent record:*
> `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`.

## 2. Intent record and commissioning item (read in phase 2)

- `docs/sessions/2026-10-03-0144-queue-run-handups-and-tool-defects.md`
- the board item named in the pointer

## 3. What the authoring run said to the orchestrator (channel, verbatim)

> a fifth refs-only pointer of mine is on main, docs/roadmap/160-doctrine-review-owed/470-rule-4-cold-pass-queued-publishscan-round-2.md. (Plus the two gate-stricter notices quoted in § 4.)

Nothing else from that run was read by the orchestrator.

## 4. Prior findings and seeded questions (the orchestrator's, labelled)

Prior findings on this scanner (all ruled by the principal, 2026-08-02/03):

- PB1 (MAJOR, fixed): `fnmatch` patterns were depth-blind for most entries, so a
  nested `.npmrc`, `.env.production` or `.mcp.json` passed green; fixed to match
  dotfiles by basename at any depth and directory pairs by suffix.
- PA2 (rejected as deliberate): `.env.example` false positives widened to every
  depth as a side effect of PB1's fix.
- PS1[pub] (MAJOR, fixed): REPO-STANDARD's standardise step still told children to
  commit `.claude/settings.json`.
- 260/060 P4 (open): the CI plane calls leakscan without `--require-terms`.

What the authoring run said over the channel (verbatim, two messages):

> Gate-stricter notice: publishscan's never-publish list grew (cadcf4e). atelier
> itself stays clean. Three private children will newly red when they next bump
> their pin. That only affects sessions that run publishscan on another repo.

> correcting what I sent earlier: publishscan round 2 does NOT wait for a pin bump.
> Children call floor.yml@main and their scanners float at main, so the 3 private
> children go red at their NEXT CI RUN. That's the floor working as designed on
> latent findings; I'd reasoned it instead of checking the workflow. It's corrected
> in 260/040 (f2b84e3).

Seeded questions (the orchestrator's): (1) Does every new pattern obey the PB1
depth rule? (2) What is the false-positive surface of the new entries, and is it
stated? (3) Is the fleet consequence (reds at next CI run, no pin bump) stated on
any surface a child reads? (4) Is there a documented path for a child that must
keep a listed file?
