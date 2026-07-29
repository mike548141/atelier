# Review brief — B2+B3 `floorfleet --status` cold pass

- **Date:** 2026-07-29 1251 UTC
- **Subject:** commits `79c8992` (`--status` — the board answers *wired* AND
  *passing*; B3 folded in as the same defect one level down) and `fb13b71`
  (`--from-github` — enumerate the estate, not one laptop's directories).
  Files: `tools/floorfleet.py`, `tools/test_floorfleet.py`. The estate-root
  consumer workflow is in scope as a consumer; per this repo's own boundary
  it is referenced by convention, never named.
- **Spawn provenance (rule 4):** same Mike-spawned taker session as the E6
  pass (Fable 5), author of nothing in the Track B chain; claim on `main`
  (`f127c5f`) precedes this worktree. The brief is the taker's own.
- **Deferral discipline:** the intent record
  (`sessions/2026-07-28-1233-track-b-enumerator.md`) and the Track B harvest
  in `ROADMAP-DONE.md` stay unopened until findings are committed; commit
  messages and the roadmap's live Track B summary are treated as the work's
  claims — a floor of questions, never a fence.
- **Scanner reach:** `/security-review` reads pending changes; this is a
  landed delta with nothing in flight — discharged with grounds. The
  mechanical floor here is the test suite plus live read-only runs.

## Scope — four lenses

1. **Approach:** is *wired AND passing AND current* the right definition of
   green for a conformance board, and is inference-with-declared-authority
   the right answer to the Actions-disabled blind spot (vs the admin-scope
   endpoint it deliberately refused)?
2. **Correctness:** does the code do what the commit claims — fail-safe on
   every path, exit-code compatibility for `--check` without `--status`,
   behind-head success not green?
3. **Completeness:** what the board still cannot see; whether the
   enumeration claim ("both listings unioned") is complete at every token
   altitude, not just this laptop's.
4. **Security & privacy:** token scope (the refused Administration
   permission), injection surface in the `gh` plumbing, read-only claim,
   and what the board's output may reveal and where.

## Load-bearing assumptions to attack (the reviewer's own, first act)

- **A1 — "only a passing run counts as green; an unread answer counts as
  red" holds on *every* path.** Walk every `classify_run` branch: API
  error, no workflow, empty run list, `in_progress`, `cancelled`/`skipped`,
  success-behind-head. Verify the selftest genuinely drives each branch
  offline, and that `--check` without `--status` byte-for-byte keeps its
  old meaning.
- **A2 — the run being read is the right run.** Default branch only, or can
  a green feature-branch run masquerade? Keyed to the floor workflow
  identity or to any workflow? Event filtering (push vs schedule vs PR)?
- **A3 — enumeration is complete at every token altitude.** The
  public-only bug was fixed by unioning two listings — which two, and what
  happens on a token that cannot see private repos? Does the tool *declare*
  its enumeration authority the way B3 declares run-reading authority, or
  does the same quietly-enumerated-a-quarter failure recur one level up?
  Forks/archived repos: counted, skipped, or undeclared?
- **A4 — inferred Actions-disabled is honest.** A new repo whose floor
  landed but never ran reads the same as one with Actions off. Does the
  board say *which authority answered* per row, as claimed? Does the
  inference have a false-green direction anywhere?
- **A5 — n/a is not green and not red.** In `--from-github` mode the hook
  column is n/a (no working copy). Verify n/a can neither satisfy nor fail
  `ChildFloor.green` — a board where n/a reds every remote row is useless,
  one where it greens is worse.
- **A6 — the plumbing is safe.** `_gh_json`/`_gh_list`: how arguments reach
  `gh` (injection via owner/repo names), the bare-string `--jq` bug's fix
  and its test, rate-limit behaviour over ~20 repos, and that the whole
  mode is read-only.
- **A7 — the tests bite.** `RunStatusTest`, `RemoteDiscoveryTest`,
  `GhReadTest`: known-failure legs for the two found-while-building bugs
  (public-only listing, bare-string jq), suite counts 759→771→779 re-run
  at HEAD.
- **A8 — the live claims re-run.** The board runs today, read-only, and
  reports coherent statuses; the parent's own row exists; the historical
  5-of-14 figure is treated as the work's claim about its first run, not
  re-provable — say so rather than pretend.
- **A9 — the refused permission was the right refusal.** B3 declined
  GitHub's Administration scope for one boolean — verify nothing in the
  delta requests it, and the degradation path is declared, not silent.

## Security lens (by hand)

**T1** — token altitude: a scheduled consumer running this with a
narrow token must not read as a *cleaner* board (fewer repos, fewer reds).
**T2** — argument injection from repo/owner strings into the `gh` calls.
**T3** — output disclosure: what a board row reveals and which plane it
prints on. **T4** — the board itself as a false-confidence instrument: any
state it renders green without having read evidence.

---

# Verdict — PASS-WITH-FINDINGS (1 MAJOR / 2 minor / 2 notes)

- **Date:** 2026-07-29 (UTC) · **Reviewer:** Fable 5, cold
- **Provenance repeated (rule 4):** Mike-spawned taker session, author of
  nothing in the Track B chain. The intent record and the `ROADMAP-DONE`
  harvest were not opened before these findings were committed; reconcile
  follows.
- **Scanner line:** `/security-review` discharged — landed delta, nothing
  in flight for it to read. Mechanical floor: the suite (795 tests, green
  at HEAD) plus four live runs.
- **Overall:** B2+B3 are well built. The core is genuinely fail-safe: the
  classifier is pure with every branch selftested, only `passing` is green,
  the refused Administration permission is the right least-privilege call
  and its degradation is *declared* on the board. The MAJOR is the same
  defect class the work itself hunts — an absence that cannot raise its
  hand — surviving one level up, in discovery.

## Re-run and verified

- **Suite:** 795 tests green at HEAD (landing claims of 771/779 are
  mid-chain records; the suite has since grown — re-run, not read).
  `floorfleet --selftest` ok, 0 failures.
- **Fail-safe contract:** every `classify_run` branch selftested offline,
  including the three that used to read green (actions-off, never-ran,
  behind-head success); `green()` selftested `False` for all eight
  non-passing states and for unwired+passing.
- **`--check` compatibility:** live run, `--check` without `--status`
  exits 0 on today's estate (all 13 wired) *while four floors are red* —
  the old meaning preserved exactly, and `--status` is what surfaces the
  reds. With `--status`: exit 1.
- **Live board (local discovery):** runs clean; 4 of 14 not proven green
  today (docker-heap, faves, homenetwork, nova — the work's first-run
  figure was 5; one has since cleared). The historical 5-of-14 is treated
  as the work's claim about its first run; the class reproduces today.
- **Live board (consumer mode):** `--from-github <owner> --status --check`
  run end-to-end from this machine: 13 children + parent enumerated, all
  14 run rows read, 6 unenrolled repos declared, exit 1 on the four reds —
  failing for the right reason. 13 children + 6 outsiders + atelier = the
  account's 20 repos: enumeration complete *with this token*.
- **Authority declaration:** with a token that can read the Actions
  switch, no caveat is advertised (correct — the stronger authority
  answered); the estate-root job's first production run printed the
  INFERRED footer for all 14 (recorded in the roadmap). Both directions
  observed.
- **B3's refused permission:** nothing in the delta requests
  Administration; the `actions/permissions` 403 path falls through to
  inference and says so. Verified in code and in both live runs.
- **The two build-time bugs have known-failure tests:** the public-only
  listing (union test) and the bare-string `--jq` parse (GhReadTest).
- **Injection surface:** all `gh`/`git` calls are list-argv, no shell;
  slugs are owner-filtered and regex-constrained on the local plane.

## Findings

- **FS1 (MAJOR) — discovery declares no authority, and a refused read is
  misreported as a scope decision.** Two legs, one defect:
  (a) the empty-estate guard fires only when *zero* children are found —
  a token that sees some-but-not-all repos (selected-repos grant,
  wrong-account, partial fine-grained grant) proceeds silently and renders
  a smaller, cleaner board with no line saying which listings answered or
  how many repos each returned (T1);
  (b) a child whose `CLAUDE.md` read *fails* (per-repo 403, rate-limit,
  transient error) is indistinguishable from one with no pin — it lands in
  the "carry no atelier pin … not red, not counted, not scanned" list, a
  *confident wrong claim*, and `RemoteDiscoveryTest` (the outsider leg)
  bakes the conflation in by asserting `None` ⇒ outsider. The tool's own
  posture — *"a read we could not make must never become a pass"*
  (`_gh_json`) — is violated here, where the read that could not be made
  becomes a scope decision. Mitigation today: the live token is granted
  all-repos until 2026-10-27, so leg (a)'s likeliest trigger is currently
  closed — but rotation is a human step, the consumer workflow's token
  spec comment does not state the grant scope, and this board is the
  instrument that is supposed to outlive that. **Counsel:** declare
  discovery authority in the footer exactly as run-authority is declared
  (which endpoints answered, counts per listing, a warning when the
  private-capable listing returns nothing); separate unreadable from
  unpinned (an unreadable child is an `unknown` row, not an outsider);
  state the token's grant scope beside its permissions in the consumer's
  token spec.
- **FS2 (minor) — the headline list miscounts unwired repos as "wired".**
  `unproven` filters `run != "passing"` over *all* rows, so a repo that is
  `absent`/`vendored` (run: `unregistered`) is counted under
  *"N repo(s) are wired but NOT PROVEN GREEN"*. The sentence built to be
  read first misdescribes exactly the worst rows. Counsel: filter on
  `i.ok`, or reword to drop "wired".
- **FS3 (minor) — an archived child vanishes without a word.** Archived
  repos are skipped before the pin check (deliberate, tested) — but a
  decommissioned-but-still-pinned child leaves the board with no line, on
  the board whose doctrine is that absences raise their hands. One
  footer line ("skipped N archived repo(s)") keeps it a decision.
- **FS4 (note) — `read_run` is annotated `tuple[str, str]` and returns a
  3-tuple** on every path. Cosmetic; fix with the next touch.
- **FS5 (note) — `green()`'s docstring overclaims.** "Every state that is
  not literally `passing` is not green" is false for the `""` sentinel
  (no `--status`), which is green-by-collapse to `ok` — by design,
  documented at the field, unpinned by any selftest leg. Fold the
  sentinel into the docstring and add `green("") == ok` to the selftest,
  so the compatibility contract is pinned, not remembered.

## Reconcile (written after the findings above were committed)

Opened after the findings commit: the intent record
(`sessions/2026-07-28-1233-track-b-enumerator.md`) and the Track B harvest
in `ROADMAP-DONE.md`.

- **No contradiction, and no pre-emption:** FS1 appears nowhere in the
  author's account — the union fix addressed the *endpoint* under-
  enumeration; the *token-altitude* recurrence and the unreadable-vs-
  unpinned conflation were not seen. FS2–FS5 likewise unclaimed.
- **The author's own honesty notes check out:** the union bug and the
  bare-`--jq` bug are recorded as found-in-building with the fixture
  mea-culpa ("the unit test had agreed with the defect"), which matches
  the tests as they now stand; the degraded-authority footer's production
  proof is quoted in the roadmap and both directions were observed live
  by this pass.
- **Worth carrying to the B4 pass (queued next):** the intent record's
  addendum documents the B4 pointer's refs-only breach and its
  correction — the pointer this taker reads is the corrected one; the
  breach history itself is already tracked as the third-instance finding.

## Decision — Mike's (rule 3 reach: the board is enforcement doctrine by
function; its author also wrote the tests that judge it)

FS1–FS5 await rulings; the reviewer applied nothing. Cycle stays open
(1 MAJOR): rulings → application (own rule-4 pointer) → terminal pass.

## Rulings (Mike, 2026-07-29, plain-language walk-through with per-option
impacts; recorded verbatim by the reviewer, applied by no one yet)

- **FS1 — RULED: accept both legs.** floorfleet gains a
  discovery-authority footer (which listings answered, per-listing
  counts, a warning when the private-capable listing returns nothing);
  a child whose `CLAUDE.md` read fails renders as an `unknown` row,
  never as an outsider; the consumer's token spec states the all-repos
  grant requirement beside its permissions.
- **FS2 — RULED: accept.** The not-proven-green headline filters on
  wired-ness (or drops the word "wired").
- **FS3 — RULED: accept.** A footer line declares skipped archived
  repos by count.
- **FS4 — RULED: accept.** `read_run`'s annotation corrected to the
  3-tuple it returns.
- **FS5 — RULED: accept.** `green()`'s docstring names the no-`--status`
  sentinel, and a selftest leg pins `green("") == ok`.

**Application owed:** all five land together as one build item; the
applier queues its rule-4 pointer in the landing commit. FS1 changes
board behaviour, so its application is code + tests, reviewable on the
same footing as B2+B3 were.

