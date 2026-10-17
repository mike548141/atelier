# Cold pass — the pre-flip gate learns from the first flip; publishscan --history

**Pass type:** doctrine and code cold pass, per `docs/method/REVIEW.md` rule 4.
**Tier:** Fable (the principal-named review tier, ruling 2026-08-04), checked at
selection by whoever takes the pass.
**Status:** BRIEF ONLY — the review has NOT run. Written 2026-10-16 UTC by an Opus
brief-writer; the pass waits for a further cold Fable session that neither the
delta's author nor this brief-writer (nor its orchestrator) started or instructed.
Tier is checked at selection (rule 4).
**Queue pointer:**
`docs/roadmap/160-doctrine-review-owed/740-rule-4-cold-pass-queued-the-pre-flip-gate.md`.
**Why it earns a review:** making a repository public cannot be undone. This delta
adds three binding steps to the one doctrine home of the gate run before that
moment, and a new mode of the guard the gate relies on to see what the flip will
publish; a gap in either is found only after the publication it was meant to stop.

## Spawn provenance

- **Author of the work under review:** the queue run whose intent record is dated
  2026-10-05 11:20 UTC (an Opus orchestrator with dispatched workers; the pointer
  counts the workers' output as the run's authorship). Not opened here.
- **Who wrote this brief:** an Opus subagent (`claude-opus-5-5`) dispatched by a
  Mike-opened Opus queue-run session (id prefix `abe96d8d`) on 2026-10-16 UTC, on
  Mike's answer that day that a fresh Opus session writes these briefs. It
  authored none of the delta. It is **off-tier for review, disclosed: it forms no
  finding and writes no severity**, and it stops after this brief and its sibling.
- **Who takes the review:** a further cold Fable session, not yet started, that
  passes rule 4's criterion. The reviewer repeats its own provenance in its
  verdict.
- ⚠️ **Exposure, disclosed** (rule-2 material met before writing). This
  brief-writer read: the queue pointer in full; the landing commit's subject,
  `--stat`, the `AUTONOMY.md` and `CHANGELOG.md` diffs, a keyword skim of the
  `publishscan.py` diff, **and the message body** (the author's own account); the
  subjects and `--stat` of later commits on the same files; `REVIEW.md` rules 1–4,
  the four lenses, the checklist and the lifecycle; the ask halves of two
  2026-10-04 briefs as templates; `docs/reviews/` filenames and filename-level
  greps (no prior verdict opened); the names, not contents, of the commissioning
  board items; and its harness-loaded memory index. Its orchestrator read the
  `docs/SESSIONS.md` index tail through 2026-10-16 (including the authoring run's
  one-paragraph summary) and the 2026-10-16 session record's close section, and
  passed on no evaluative content beyond the pointer list. Everything evaluative
  is in the sibling.

## What the work is

Landing commit (diff it; review the paths at HEAD):

- `89ff0d8` (2026-10-05 18:41 UTC) — publish: the pre-flip gate learns from the
  first flip (260/110); landed in merge `ce3f776` (2026-10-05 18:42 UTC)

Delta paths: `docs/method/AUTONOMY.md` (three new sub-bullets under the
making-public clause), `tools/publishscan.py` (`--history`, `history_findings`,
`run_history`, the streamed NUL reader, round-3 pattern `*.egg-info/`),
`tools/test_publishscan.py`, `tools/README.md` (publishscan section),
`CHANGELOG.md` (the 2026-10-05 entry).

**Later commits on the same files — not this delta; do not attribute them to
it.** `c1cef10` (2026-10-05 18:56 UTC) — publishscan reads the tip and staged
planes NUL-delimited (260/120; its own pass is 160/760); `CHANGELOG.md` and
`tools/README.md` have many later entries. Earlier, `ffabef3` had already moved
publishscan onto the shared report contract (160/730).

## Scope

Widest the work admits: intent, decisions, assumptions, design, docs, code, tests
and live behaviour. The lenses organise it; they do not bound it. Non-goals are the
only narrowing and are themselves reviewable.

**The doctrine.** Whether each new bullet is executable by a session holding only
`AUTONOMY.md`: "the scrub runs last, over the gate's own records" — is there a
point at which the gate's records are final, or does writing the scrub's own
record reopen it? "A planted canary is reconciled shape by shape" — where are the
shapes listed, and what is the gate's state when one does not fire? "The doctrine
pin is current at the flip" — which tool or procedure is "the drift check
(PROPAGATION)", does it exist and run as named, and what is "the inlined floor"?
Whether the three bullets agree with `RECORD.md` § *The record is public*,
`PROPAGATION.md`, ADR 0005 and any repo-creation or publication skill that walks
the same moment. **The tool.** Whether `--history` sees every path a visibility
flip publishes. Build repos in a scratch area and test: a path added and deleted
on a branch merged long ago; a path added only on a side branch later merged; a
path added in a merge commit's own diff; a rename (with `--no-renames`); a path
on a pushed branch whose local remote-tracking ref was pruned; tags pointing at
non-commit objects; a path only in a stash; refs the hosting service publishes
that a clone does not fetch by default (pull-request refs, unreachable commits by
hash); submodule entries; names with newlines, non-ASCII bytes and leading dashes;
a commit message whose text looks like a path list. Whether the shallow-clone
refusal and the "not a git repository" path give the right exit code for a gate
that must not pass blind. **Non-goal:** the principal's choice to build all four
harvest items before the next flip.

## The four lenses

1. **Approach & assumptions.** Name the load-bearing assumptions yourself first.
   Among them: that local branches, tags and remote-tracking refs approximate what
   the host will publish; that path names are the right unit (not content) for a
   history check; that opt-in is safe when the gate doctrine says the gate "runs"
   it — what enforces that it runs?
2. **Correctness & quality.** Read the three bullets in context and
   `publishscan.py`'s history mode and tests whole; diff `89ff0d8`. Record a table
   for the history cases above: published by a flip? reported? Check the
   streamed reader's parsing of git's `-z` header-and-names layout, the stderr
   drain and non-zero-exit path, and the "oldest adding commit" and "still
   tracked" fields.
3. **Completeness / harvest.** Every surface that describes the pre-flip gate or
   publishscan: `tools/README.md`, `docs/method/GUARDS.md`, `SECURITY.md`, ADR
   0005, `skills/` that cover creating or publishing a repo, and the child
   templates. Does each mention `--history` where it should, and does any still
   describe the gate without the three new steps? Is the changelog entry true?
4. **Security & privacy** — mandatory. The history mode shells out to git on a
   repo about to be published; check argument construction, repository-local
   config that could alter `git log` output or run commands, and whether output
   or findings can echo a private repo's name next to its scan state — the very
   join the first new bullet forbids. Never quote any such name in the verdict.
   `/security-review` is discharged by grounds (a landed delta; the pending diff
   is not the work) — say so, and deliver the code-altitude read by hand against
   the OWASP catalogue.

## Re-run obligation

Re-run, do not read. Lift floor invocations from `.githooks/pre-commit`,
`tools/floor.py` and `.github/workflows/ci.yml` rather than guessing.

- `python3 -m unittest tools.test_publishscan -v`; `python3 tools/publishscan.py
  --selftest`; `--help` shows `--history` and its refusal with `--staged`
- `python3 tools/publishscan.py --history --root .` on this repo and on your
  scratch fixture repos; a shallow clone of a fixture must exit 2
- the "default output byte-identical" claim, re-driven at landing on this repo
  and your fixtures only: `89ff0d8^` against `89ff0d8`, stdout, stderr and exit
  code (the commit's 29-repo measurement is not re-run — never point a scanner
  at other repos on the machine; say so)
- the floor on both planes at HEAD; the full Python suite once, foreground

## House rules for this run

- Name the worktree you work in. Run no git command that writes there; read-only
  git is fine. Fixture repos, shallow clones and older checkouts go in a private
  area under your session scratchpad, named by your prefix.
- One heavy process at a time on a shared machine: the full suite at most once, in
  the foreground. Never point a scanner at any other repo on the machine.
- `/security-review` reads the session's pending diff: discharge it by grounds for
  this landed delta, or keep the tree clean whenever you spawn it.
- Dates absolute ISO 8601 from `date -u`. Prose wrapped at ≤ 100 columns. NZ
  English. Never quote a secret, placeholder token, email address, private repo
  name or personal detail — this repo is PUBLIC; describe and locate instead.

## Deferred reading — do not open before your findings are durably written
<!-- reviewscan:allow:deferral: this section BARS reading and carries no deferred content — the deferred material lives in the sibling .deferred.md, held apart under the rule-1 split and opened only after the reviewer's phase-1 findings are committed -->

Rule 2 bars until phase 2: `docs/ROADMAP-DONE.md`, `docs/SESSIONS.md`,
`docs/sessions/`, every prior verdict in `docs/reviews/`, the queue pointer, this
brief's sibling `docs/reviews/2026-10-16-1551-pre-flip-gate-history-cold.deferred.md`,
and the commissioning items `090`, `110` and `120` in
`docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005/` (barred as a
section; `090` holds the harvest the bullets cite as evidence).

Sweep with `python3 tools/coldsweep.py --root <your worktree> --also-exclude
docs/roadmap/160-doctrine-review-owed/740-rule-4-cold-pass-queued-the-pre-flip-gate.md
--also-exclude docs/reviews/2026-10-16-1551-pre-flip-gate-history-cold.deferred.md
--also-exclude docs/roadmap/260-sharing-public-since-2026-07-10-adr-0005
<pattern>`; `--include-barred` only with disclosure. Reading the delta is never
barred.

## Process

**Phase 1.** Reproduce the floor first; work the lenses and the re-run list. Then
append your verdict below a `---` divider in THIS file: provenance repeated (how
you were spawned, your tier, what you read), per-lens answers, the standing
checklist V1–V7 each answered or discharged with grounds, the history-case table,
findings with stable IDs (prefix `PF`: `PF1`, `PF2`, …) and severities (MAJOR /
MODERATE / minor / note), an overall PASS / PASS-WITH-FINDINGS / FAIL line with
counts, a re-run ledger, and a follow-up checklist. Then STOP and commit phase 1
unrevised before opening the sibling.

**Phase 2.** Open the sibling; append `### Reconcile` beneath your verdict:
per-finding notes against the seeded questions and the intent record, any finding
formed at reconcile marked as such, and the overall line restated. Never revise
phase-1 text. Then fold the sibling in below the reconcile and delete it.

Findings on self-authored doctrine are the principal's to decide (rule 3): record
all, apply nothing; counsel per finding is welcome, labelled and kept beneath it.

---

## Verdict — phase 1 (2026-10-17 UTC)

### Provenance, repeated

- **Reviewer:** a fresh `claude-fable-5-1` subagent (Fable, the principal-named
  review tier; checked at claim) spawned 2026-10-17 UTC by a Fable orchestrator
  that authored none of the delta and none of this brief, and that holds the
  sibling `.deferred.md` outside this reviewer's reach until these findings are
  committed. The orchestrator forms no finding and writes no severity. The
  reviewer's session is one the delta's author (the 2026-10-05 queue run) neither
  started nor instructed; the brief-writer (an Opus subagent, 2026-10-16) is a
  third party to both. Rule 4's criterion and the reviewer-plus-orchestrator
  disclosure both hold.
- **Worktree:** `/Users/mike/worktrees/atelier-review-1017`, branch `review-1017`,
  HEAD `7d06d9d` (carries `8acfff1`, verified with `merge-base --is-ancestor`).
  No git command that writes was run there. Fixture repos, bare "host" repos,
  clones and the extracted `89ff0d8^`/`89ff0d8` copies of the tool live under
  the session scratchpad in a `PF/` directory.
- **What was read:** this brief; `git show 89ff0d8` (stat, message body and every
  file diff) and `c1cef10`'s stat and `publishscan.py` diff (to separate the two);
  `tools/publishscan.py`, `tools/test_publishscan.py`, `tools/report.py` and the
  publishscan section of `tools/README.md` at HEAD; `docs/method/AUTONOMY.md`,
  `REVIEW.md` whole; the named sections of `RECORD.md`, `PROPAGATION.md`,
  `GUARDS.md`, `PRINCIPLES.md` §6; ADR 0005; `SECURITY.md`; `skills/create-repo`
  steps 5–7, the floor lines of `session-onramp`; `docs/build/templates/CLAUDE.md`
  and `SECURITY.md`; the hook, `ci.yml` and `floor.py`'s registry entry; the
  `CHANGELOG.md` entry; board item `320/550` (not barred). The GitHub guidance
  page on removing sensitive data was fetched once, for PF1's host behaviour.
- **Sweeps:** `tools/coldsweep.py` with the three `--also-exclude` paths the brief
  lists, never `--include-barred`. **Not opened:** the sibling, any prior verdict,
  `docs/SESSIONS.md`, `docs/sessions/`, `docs/ROADMAP-DONE.md`, the queue pointer,
  the `260/…` items. No other `docs/reviews/2026-10-16-15*` file was opened and no
  `.deferred.md` path was shown or checked out.
- `/security-review` **discharged by grounds:** the work is a landed delta
  (`89ff0d8`, 2026-10-05); the session's pending diff is other reviewers' drafts
  and the orchestrator's partition, not the work. The code-altitude security read
  was done by hand against the OWASP Top 10 (lens 4 below).

### Lens 1 — approach and assumptions (named by the reviewer first)

1. **A clone's branches, tags and remote-tracking refs approximate what the host
   publishes.** False in one direction that matters. A flip publishes the host's
   objects and refs; the walk reads the clone's. The two differ by exactly the
   shapes a clean-up leaves behind: a branch deleted on the host after a push, a
   pull request closed unmerged or squash-merged (the host keeps `refs/pull/N/head`,
   which no default fetch brings), and a commit force-pushed over. Each stayed on a
   bare host in the probes (`cat-file -t` = `commit`) and was reported by nothing;
   GitHub's own guidance on removing sensitive data says such commits remain
   reachable by SHA in cached views and through pull requests until Support purges
   them. "Fetch first" (docstring) does not close this. → **PF1**.
2. **Path names are the right unit.** Right for this tool's question (presence,
   not contents), and the docstring says so. It leaves the content half of "every
   path ever pushed" to tools that have no history plane (secretscan and leakscan
   take `--staged` only; `320/550` records that nothing reads a message body). The
   gate bullet names only `publishscan --history`. → **PF12** (note; outside the
   non-goal's four items).
3. **Opt-in is safe because the gate "runs" it.** Nothing enforces that. The
   floor registry does not run `--history` (README says so, correctly); no skill,
   template or checklist walks the flip; the gate's three steps exist only as
   prose under AUTONOMY's making-public clause, and the two surfaces a session at
   the flip is most likely to be holding — the child's inlined floor and
   `create-repo` step 7 — say "stop and confirm" without pointing at the gate. The
   honest PROPAGATION caveat applies (observable, not enforced) but is not stated
   for the gate. → **PF11** (note).
4. **`git log` reports what the host would publish.** Not when a repo-local
   `refs/replace` ref is present: `log` honours it, the host does not, and the hit
   vanished in the probe. → **PF2**.
5. **"Not a git repository" is a complete scan of nothing.** Sound for the floor
   planes (fixture trees), unsound at a gate whose operator typed `--root` by
   hand. → **PF3**.
6. **The three bullets are executable by a session holding only AUTONOMY.** Two
   of the three are not: bullet 1 names a scrub no live surface defines and asks
   it to catch the one line RECORD says no scanner can; bullet 2 governs the form
   of a canary proof for a step no doctrine states. Bullet 3 is executable with
   one gap (which tool compares the floor, and that it must run gating). →
   **PF4, PF5, PF6**.
7. **The brief's framing.** Its account of the delta matches the diff; its
   non-goal (the principal's choice to build all four items) fences off a
   decision, not a risk, and is accepted. One brief defect: its verbatim re-run
   line for the unit tests does not run from the repo root → **PF10**.

### Lens 2 — correctness and quality

**The doctrine bullets, read in context.** They sit as sub-bullets of the
making-public floor item, after the existing "know your visibility" and "the
confirmation includes the pre-flip scrub" lines, each citing `260/090`. Bullet 1
("the scrub runs last, over the gate's own records") carries a second, unrelated
instruction in its last sentence (run `publishscan --history`) — a structural
nit, folded into PF5. Bullet 2 is a rule about the proof's form with no statement
of the act it qualifies (PF4). Bullet 3 names "the drift check (PROPAGATION)",
which exists (PROPAGATION point 4, the verbatim command in the child block), and
"compare the inlined floor with the canonical one", which is `tools/stampscan.py`
unnamed (PF6).

**The tool, read whole and re-driven.** `history_findings` parses the
`--format=%x01%H %ct` / `--name-only -z` layout correctly for git's actual
output: the raw bytes (C19) are `\x01<sha> <ct>\0\n<name>\0<name>\0…`, so the
header is a NUL-terminated token and the first name carries one leading `\n`,
which the `first` flag strips. Commits with no addition print nothing at all
(C19b, C15), so `commits` counts commits with an addition, as the docstring says
(the clean line's "across N commit(s) of history" reads wider — PF13). The
chunked NUL reader reassembles across edges (unit test, chunk sizes 1–64). The
stderr drain and non-zero path work: a shallow clone exits 2 with the fetch
remedy on stderr and no JSON on stdout (C13a). Oldest-adding-commit selection is
right for add/remove/re-add (unit test), for a rename into a never-publish name
(C4: the rename commit) and for a side-branch add later merged (C1, C2: the
side commit, not the merge). "Still tracked" is read from the checked-out
index, not a branch tip (PF8). Two 0x01-leading names in one commit crash the
parser (PF7). `--remotes` imports every remote's history (PF9).

**Claims re-driven.** Default output byte-identical between `89ff0d8^` and
`89ff0d8`: **8 of 8** (four flag sets × this repo and one fixture; stdout, stderr
and exit code compared), both selftests OK. The commit's 120-of-120 figure over
29 repos is **not re-run** — never point a scanner at another repo on this
machine. `*.egg-info/*` is in `NEVER_PUBLISH` with the selftest's two red and two
green shapes. `--history` on this repo: exit 1, two history-only hits (the
allowlist first added 2026-07-10 and a nested-worktree gitlink first added
2026-07-22), both long published — atelier is public and the docstring already
says its historic copies are published for good; no new exposure.

**The history-case table** (probe IDs are the scratchpad fixture names;
"published" means the host still holds the object after the routine clean-up).

| Case | Published by a flip? | Reported? | Probe |
|---|---|---|---|
| Added and deleted on a branch merged long ago (merge commit, branch deleted) | yes (merge's 2nd parent) | yes, at the side commit | C1 |
| Added only on a side branch later merged (merge commit) | yes | yes, still tracked | C2 |
| Same, **squash**-merged, branch deleted (the `--delete-branch-on-merge` shape) | yes, via the host's `refs/pull/N/head` | **no** | C2b, C8 |
| Added in a merge commit's own diff | yes | yes, at the merge | C3 |
| Rename into / out of a never-publish name (`--no-renames`) | yes | yes, both names | C4 |
| Pushed branch; local branch deleted; remote-tracking ref still present | yes | yes | C5a |
| …then deleted on the host and pruned locally (host keeps the object) | yes, by SHA | **no** | C5b, C5c |
| Branch force-pushed over a commit (host keeps the object) | yes, by SHA | **no** | C8b |
| Tag pointing at a blob; tag at a tree; annotated tag | n/a | no crash; walk unaffected | C6 |
| Commit reachable only from a tag | yes | yes | C6b |
| Path only in the stash | no | no (correct) | C7 |
| Submodule: inner history | no (gitlink only) | no (correct) | C9 |
| Submodule gitlink at a never-publish path | yes (the gitlink) | yes | C9 |
| Invalid-UTF-8 dir, `-/`, `--rf/`, newline dir, each holding `.env`/`.envrc` | yes | yes (newline stripped from the printed name) | C10a |
| One top-level name beginning 0x01 | yes | yes (sorts first, so it wears the `\n`) | C10b |
| Two top-level names beginning 0x01 | yes | **crash**, exit 1, no JSON | C10d |
| Commit message shaped like a path list and a header | n/a | clean; message never read | C11 |
| `refs/replace` rewriting the adding commit | yes (host ignores replace) | **no** (exit 0); yes with `--no-replace-objects` | C12, C12c |
| Shallow clone | — | exit 2 | C13a |
| Blobless / treeless partial clone (local promisor) | — | exit 1, lazy fetch succeeded | C13b, C13c |
| `--root` not a git repo | — | **exit 0** with a tick | C14a |
| `--root` inside the repo | — | rebased to the top, reported | C14b |
| Second remote (`upstream`) holding `up/.env` | no (origin flips) | yes (over-report) | C16 |
| Orphan branch | yes | yes | C17 |
| Checkout parked on an older branch; `main` tracks the hit | — | "history only" (index read) | C18 |
| `git rm --cached` staged, not committed | — | "history only" while HEAD tracks it | C18b |

### Lens 3 — completeness and harvest

- `tools/README.md`: names `--history`, its scope, the rev-list rationale, exit 2
  on shallow, "the floor registry does not run it". ✓. Its "a flip publishes
  every path ever pushed" line is the overclaim PF1 names.
- `docs/method/GUARDS.md`: frames publishscan as the boundary the allowance
  inventory sits inside; no plane detail. Nothing stale.
- `SECURITY.md`: no mention; its scope clause makes an *undocumented* miss a
  vulnerability and a documented one a pointer — which is why PF1 is counsel to
  document first.
- ADR 0005: historic record of the first flip; untouched by design (no-edit
  rule). Its "secretscan clean over all 44 commits" is the content-history check
  the gate bullet does not carry forward (PF12).
- `skills/create-repo` step 7, `skills/session-onramp` §2, the child template's
  inlined floor: each says publishing is a floor stop; none points at the gate
  (PF11). `docs/build/templates/SECURITY.md` is a publish-time artefact with its
  own flip-time step (enable Private Vulnerability Reporting) that the gate does
  not list (PF11). The child block's visibility-fact line must change at the
  flip; not listed either (PF11).
- `CHANGELOG.md` entry: true to the delta line by line; the 120/29 figures are
  the commit's and were not re-run here.

### Lens 4 — security and privacy (OWASP Top 10, by hand)

- **Injection (A03):** every git call is an argv list with `-C <root>`, no shell;
  paths arrive on stdout and are matched, never re-used as arguments; history mode
  prints no remediation command carrying a path. Terminal injection closed at the
  ingest seam (`_strip_controls`; C10a's newline name printed flat). ✓
- **Integrity failures / misconfiguration (A05, A08):** a repo-local
  `refs/replace` alters the walk and not the publication (PF2). `.git/info/grafts`
  is the same class, untested. Repo-local `diff.renames`, `log.diffMerges`,
  `core.quotePath` are all overridden by explicit flags. `core.fsmonitor` (a
  command git runs on index reads) would run during `ls-files`; that is the
  owner's own config on a repo they are flipping — noted, not charged.
- **Logging / fail-closed (A09):** broken scans exit 2 ✓, except the non-repo
  root (PF3) and the parser crash (PF7, exit 1 with a traceback).
- **Data exposure (A01/A02):** a finding line is `path — first added <sha> (<date>),
  <state>: <why>`; on the repo being flipped it names nothing the flip will not
  publish. The rebase notice prints the absolute repo path on stderr (C14b) — the
  directory name is usually the repo's name, so a captured gate transcript holds
  the join RECORD forbids; that is what bullet 1's scrub exists to catch, and PF5
  is about whether it can. No private name is quoted in this verdict.
- **Resource use:** streamed reader, hits-only memory ✓; `_git_stream` reads
  stderr after stdout EOF, so a git that fills its stderr pipe before finishing
  stdout would deadlock (PF14, theoretical). A treeless partial clone lazily
  fetched over the network with no notice (C13c) — acceptable, noted.
- **Supply chain:** stdlib only ✓. **Design altitude:** the threat the work
  answers (a path published by history, not the tip) is named in the docstring;
  the threat it does not answer (host-side residue) is not — PF1's design half.

### The standing checklist

- **V1** — the tool's banner and README say "every path ever pushed"; the walk
  covers every path on a *present* ref (PF1). The docstring says no reported path
  can carry the header byte; the parser tests the raw token (PF7).
- **V2** — re-run ledger below; every in-scope claim reproduced except the
  29-repo figure, deliberately not re-run.
- **V3** — mirror sites swept per PRINCIPLES §6 (docs, skills, templates): no
  stale restatement of the gate exists because none exists at all (PF11).
- **V4** — AUTONOMY is the gate's one home ✓; README and docstring restate the
  rev-list rationale in two wordings — the house pattern for every scanner,
  not charged.
- **V5** — bullet 1 asks the scrub to catch the name-to-posture join; RECORD
  § *The record is public* says no scanner can hold that rule (PF5).
- **V6** — lens 4 above; `/security-review` discharged with grounds.
- **V7** — provenance stated in the brief and repeated above ✓.

### Findings

Doctrine findings (PF4, PF5, PF6, PF11, PF12) are the principal's to decide
(rule 3); nothing is applied. Counsel is labelled.

**PF1 — MAJOR — `--history` walks the clone; the flip publishes the host, and
the gap is undocumented.** Squash-merged or closed pull-request branches
(`refs/pull/N/head`, kept by the host, never fetched by default), branches
deleted on the host after a push, and commits force-pushed over all survived on a
bare host in the probes and were reported by nothing (C2b, C5b, C5c, C8, C8b).
GitHub's sensitive-data guidance says exactly these stay reachable by SHA, in
cached views and through pull requests until Support purges them. Under the
house's own `--delete-branch-on-merge` standard the squash-merged PR branch is
the routine shape, not an edge. Nothing in the docstring, README, CHANGELOG or
the AUTONOMY bullet names the limit, and the tool's own banner ("A flip publishes
every path ever pushed, not only the tip") states the wider scope the walk does
not reach. By `SECURITY.md`'s own scope clause an undocumented miss in a scanner
is a vulnerability; a documented one is a pointer. *Counsel:* (a) document the
limit in the docstring and README now; (b) have history mode run `git ls-remote
<remote>` and refuse (exit 2, like shallow) when the host holds refs the clone
lacks, naming the fetch refspec for `refs/pull/*` — a clone that cannot see what
the host serves is a broken scan; (c) have bullet 1 say what `--history` covers
and that host-side residue is the host's own purge path or a fresh history.
Severity rests on the gate's one purpose: a green here reads as "nothing in
history", and on the routine shape it is not.

**PF2 — MODERATE — a `refs/replace` ref blinds the walk.** With a replace ref
pointing the adding commit at a clean twin, the scan exits 0; without it, 1;
`git --no-replace-objects` restores the hit (C12, C12b, C12c). Replace refs are
repo-local, not pushed by default, and never applied by the host, so this is the
brief's "repository-local state that alters `git log` output" made concrete.
*Counsel:* run the history and `ls-files` calls with `--no-replace-objects` (or
`GIT_NO_REPLACE_OBJECTS=1`); grafts are the same class and worth one test.

**PF3 — MODERATE — `--history` on a non-repository exits 0 with a tick.** The
floor planes' reasoning (fixture trees are plain directories) does not transfer
to a gate run by hand on one repo about to flip; a mistyped `--root` passes the
gate blind (C14a). *Counsel:* in history mode, `NotARepo` is a broken scan
(exit 2); keep the exit-0 skip for the floor planes only.

**PF4 — MODERATE (doctrine) — bullet 2 governs a proof for a step no doctrine
states.** "A planted canary is reconciled shape by shape" presumes the gate
plants shapes and proves a scanner fires; no surface says which scanner, which
shapes, who plants them, or what the gate's state is when a shape stays quiet
("a finding to explain" — to whom, and does the flip wait?). The practice lives
in `260/090`, barred and not doctrine. *Counsel:* write the step the bullet
qualifies (plant the suite's shapes, run the scrub, list each with fired/quiet)
and that a quiet shape holds the flip until the principal has the explanation.

**PF5 — MODERATE (doctrine) — bullet 1's "scrub" is undefined, and the line it
must catch is one RECORD says no scanner can.** `docs/method` uses "scrub" only
in these bullets, in RECORD (scrub of HEAD is not remediation), SECRETS (never
scrub history) and PROPAGATION (forward-only): no surface names the tools or hand
reads that constitute it. The bullet points at RECORD § *The record is public* for
the name-to-scan-state join, and that section says in terms that the join binds
through write-time discipline and review sweeps because no scanner can hold it.
The fixed point is also unstated: the scrub's own clean line is a gate record
written after the scrub ran. The bullet's last sentence (`publishscan --history`)
is a different step riding inside this one. *Counsel:* name the scrub (secretscan
and leakscan with the local term list over the whole tree, plus a hand read of
the gate's records and of the final commit's message body — `320/550` — for the
join); state that the final commit is the one before the flip and that its
clean line carries no name, so writing it reopens nothing; give `--history` its
own bullet.

**PF6 — minor (doctrine) — bullet 3 names the drift check but not the floor
comparison, and not that it runs gating.** The drift check is PROPAGATION point
4's verbatim command ✓. "Compare the inlined floor with the canonical one" is
`tools/stampscan.py`, run advisory (`--warn`) in CI; at the flip it must run
gating with `--require-stamps` or its clean line proves nothing (README: a run
that found no stamps also prints clean). "Current" is undefined (empty drift
output, or pin at `origin/main`?). For atelier itself the bullet is void (no
pin). *Counsel:* name stampscan, the gating form, and "current = the drift
command prints nothing".

**PF7 — minor — two names beginning with 0x01 in one commit crash the parser.**
`IndexError` traceback, exit 1, no JSON (C10d). The header test runs on the raw
token before `_strip_controls`, so the docstring's "a byte no path the tool
reports can carry once controls are stripped" is true of the report and false
of the parse; the same path makes a name spelled `\x01<40 hex> <digits>` in
second position a header, misattributing the names after it. *Counsel:* accept a
header only when the token matches `\x01[0-9a-f]{40} \d+` exactly, else treat it
as a name; add the two-name fixture to the suite.

**PF8 — minor — "still tracked" is the checked-out index, not a tip.** Parked on
an older branch, a path `main` tracks reports "history only" (C18); a staged
`git rm --cached` does the same while HEAD tracks it (C18b). Detection is
unaffected; the remediation label is wrong, and the house works in worktrees by
default. *Counsel:* read `ls-tree -r -z --name-only <branch>` for the branch the
flip publishes, or say "tracked in this checkout" in the line.

**PF9 — minor — `--remotes` walks every remote.** A fork's `upstream` remote
imports the upstream project's history; `up/.env` was reported as a history-only
hit no rewrite of this repo can remove (C16). Over-reporting is the safe
direction, but the remediation text then prescribes a history rewrite for a path
this repo never held. *Counsel:* say so in the README, or take `--remote <name>`
defaulting to all.

**PF10 — note (brief) — the unit-test re-run line does not run from the repo
root.** `python3 -m unittest tools.test_publishscan -v` fails with
`ModuleNotFoundError: publishscan` (the tests import the tool bare); CI and this
pass use `python3 -m unittest discover -s tools -p test_publishscan.py -v`
(46 tests OK). A brief defect, not the delta's.

**PF11 — note (harvest) — the flip's other surfaces do not point at the gate.**
`create-repo` step 7, `session-onramp` §2 and the child template's inlined floor
each say "stop and confirm"; none says where the gate's steps are. Two flip-time
acts the gate does not list: seeding `SECURITY.md` and enabling Private
Vulnerability Reporting (the template's own comment), and changing the child
block's visibility-fact line. *Counsel:* one pointer from the floor's
making-public line to AUTONOMY's gate; list the two acts there.

**PF12 — note (harvest) — history content has no scanner.** The first flip's
audit ran secretscan over every commit (ADR 0005); neither secretscan nor
leakscan has a history plane today, and `320/550` records that no scanner reads
a commit message. The gate bullet carries forward only `publishscan --history`.
Outside the brief's non-goal (the four harvest items), so counsel only: the gate
should say the content half of history is a hand job until a tool exists.

**PF13 — note — the clean line's "across N commit(s) of history"** counts
commits with an addition (C15: three commits, one addition → "1 commit(s)"),
matching the docstring but reading as the whole history. *Counsel:* "N commit(s)
that added a path".

**PF14 — note — possible stderr deadlock in `_git_stream`.** stderr is read only
after stdout reaches EOF; a git that writes more than the pipe buffer to stderr
mid-walk would block. Theoretical, untested, bounded by git's usual quietness.
*Counsel:* `communicate()`-style draining, or redirect stderr to a temp file.

### Overall

**PASS-WITH-FINDINGS — 1 MAJOR · 4 MODERATE · 4 minor · 5 note.** The tool does
what its docstring says it does, cleanly, with tests that hold and a default
plane proven byte-identical; the three bullets land in the right home. What it
does not do — see the host's view of history — is the one thing a pre-flip gate
is for, and no surface says so (PF1). The cycle stays open on that count.

### Re-run ledger

| Step | Result |
|---|---|
| `python3 tools/publishscan.py --help` | `--history` listed with its help text ✓ |
| `--history --staged` | exit 2, "two different planes" ✓ |
| `python3 tools/publishscan.py --selftest` | OK, exit 0 ✓ (also OK for the extracted `89ff0d8^` and `89ff0d8` copies) |
| `python3 -m unittest discover -s tools -p test_publishscan.py -v` | 46 tests, OK, 39 s under `nice -n 10` ✓ (the brief's `tools.test_publishscan` form fails to import — PF10) |
| `--history --root .` on this worktree | exit 1, 2 history-only hits, 1675 additions over 701 commits; JSON parses ✓ |
| `--history` on scratch fixtures | 29 probes, table above |
| Shallow clone of a fixture | exit 2, remedy on stderr ✓ |
| Byte-identical default output, `89ff0d8^` vs `89ff0d8` | 8 of 8 (none / `--staged` / `--warn` / `--json` × this repo and one fixture): stdout, stderr, exit equal ✓; the 29-repo measurement **not re-run** by rule |
| `python3 tools/floor.py --plane hook --root .` at HEAD | exit 0 ✓ (pathscan and the other warn-only guards report, never block) |
| `python3 tools/floor.py --plane ci --root .` at HEAD | exit 0 ✓ (secretscan 23 advisory, leakscan structural-only, as designed) |
| Full Python suite, once, foreground, `nice -n 10` | 1916 tests, OK, exit 0, 708 s wall under load (no `BoundedMemory` time-out occurred) ✓ |
| `node --test instruments/*.test.js` | not run — the delta touches no instrument and the brief's list does not name it |

Machine load during the run: 1-minute averages between 9 and 30 from other
sessions' test runs; every heavy step ran one at a time under `nice -n 10`.

### Follow-up checklist

- [ ] PF1 — document the host-side limit; add the `ls-remote` refusal; reword
      bullet 1's coverage claim (principal's call on the doctrine half)
- [ ] PF2 — `--no-replace-objects` on the history and `ls-files` calls; test
- [ ] PF3 — `--history` + not-a-repo → exit 2
- [ ] PF4, PF5, PF6, PF11, PF12 — doctrine wording: the principal decides
- [ ] PF7 — strict header match; two-name fixture
- [ ] PF8 — tip read from the publishing branch, or relabel
- [ ] PF9 — README line or `--remote`
- [ ] PF10 — fix the re-run line in the brief template the 2026-10-16 briefs copy
- [ ] PF13, PF14 — wording and drain, at leisure
