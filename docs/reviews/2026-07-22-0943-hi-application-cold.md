# Cold pass — the applied HI-F1–F6 batch (delta `30d350c`)

- **Date/time**: 2026-07-22 0943 UTC
- **Spawn provenance (rule 4)**: taken from the ROADMAP `⏳` queue by a session
  Mike opened and pointed at the queue ("please do any review work"). This
  session authored **none** of: the sizescan/harvest-integrity doctrine deltas,
  the 2026-07-22 0819 cold pass that produced HI-F1–F6, or the application of
  Mike's accept-all ruling now under review (`30d350c`). The applier queued the
  `⏳` pointer and stopped; this brief is taker-written.
- **Named exposure**: at selection the taker read (a) the ROADMAP `⏳` pointer
  (which names the fix classes: "skip-dir bypass for stores, fence fail-safe,
  RECORD.md + template edits"), (b) `git log --oneline` subjects carrying the
  applier's and prior sessions' evaluative accounts — `30d350c`'s own subject
  ("integrity checked wherever a store lives"), the 0819 pass's finding count
  ("1M/3M/2n"), and the ruling shape ("Mike's accept-all") — (c) the file
  *names* in `git show --stat 30d350c` (no hunks), (d) `docs/method/REVIEW.md`
  in full at HEAD (needed to run the process; not an in-scope file of this
  delta), and (e) the closed SL application verdict
  (`reviews/2026-07-22-0244-sl-application-cold.md`) as the process precedent —
  a different cycle, but its shape may prime this pass's shape. Every
  evaluative claim in (a)–(b) is treated as a claim to re-run, not a fact.
  An application review cannot fully honour rule 2 — the sequence per
  REVIEW.md § Applying decisions: review the edited files at HEAD and commit
  findings *first*; open the prior verdict, decision stamps, and applier's
  intent record after. The residual exposure is named, not denied.

## What the work is (refs only)

Commit `30d350c` — the application of Mike's 2026-07-22 accept-all ruling on
the 0819 cold pass's HI-F1–F6 findings. In-scope files at HEAD:

- `tools/sizescan.py`
- `tools/test_sizescan.py`
- `docs/method/RECORD.md`
- `docs/build/templates/docs/ROADMAP.md`

**Deferred below the divider** (opened only after this reviewer's findings are
committed): the prior verdict file, the decision stamps, and the applier's
intent record.

## Ask

Run all four lenses on the applied delta; scope is the whole commitment.

1. **Approach & assumptions** — name the load-bearing assumptions first, then
   attack them. Does each applied fix discharge its finding *class*, or patch
   the instance? In particular: does whatever integrity checking the delta
   adds actually fire on the stores it claims to reach (re-drive it live, red
   leg included), and does any fail-safe genuinely fail safe — what happens on
   the malformed, the missing, and the adversarial input?
2. **Correctness & quality** — re-run every live proof in scope rather than
   reading it: the full test suite; any new test's red leg (revert the tool
   hunk → the suite must go red); sizescan itself against the live repo; the
   repo floors (linkscan, reviewscan, secretscan/leakscan via the hooks).
   Honest-labelling check: do the RECORD.md and template edits say what the
   tool now actually does — no overclaim, no silent scope-cut?
3. **Completeness / harvest** — anything the rulings required that the
   application skipped; any sibling doc or template still carrying retired
   wording; record hygiene consistent with the delta (CHANGELOG, ROADMAP,
   session index — read only after findings are committed where the record
   is evaluative).
4. **Security & privacy** — landed-delta shape: `/security-review` reads
   pending diffs, so it cannot genuinely be aimed at this work — discharge
   with grounds if that holds at run time. The lens still runs manually:
   the tool hunk is Python that walks the repo and parses files — check its
   input handling (paths, encodings, malformed frontmatter/fences), exec
   surface, and any way a crafted repo file could bypass or subvert the
   scan; design-altitude leakage in the doctrine/template text.

Cycle context: the 0819 pass returned a MAJOR, so this application inherited
rule-4 status; this pass is **terminal if it returns no MAJOR** (close rule) —
report findings either way; decisions are Mike's (rule 3: the chain is
self-authored doctrine).

---

## Deferred material (open only after findings are committed)

- `docs/reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`
- `git show cfb0ae6` (decision stamps)
- `docs/sessions/2026-07-22-0819-harvest-integrity-cold-pass.md` (+ addendum)
- The record commits `f86e6ef`, `4e6e891`, `cc0bed3`
- The author seeded no questions; there is no author-written ask anywhere in
  this file. Everything above the divider is taker-written.

---

## Verdict — PASS-WITH-FINDINGS, no MAJOR (committed before any deferred material was opened)

**Provenance restated (rule 4):** this reviewer is the Mike-spawned taker
("please do any review work"); it authored none of the sizescan doctrine,
the HI-F1–F6 findings, or their application. Everything in this section was
written without opening the prior verdict file, the decision stamps
(`cfb0ae6`), or the applier's intent record. Subject pinned at `30d350c`,
reviewed at HEAD (`b6737cc`); tree solo (no claims, no foreign edits; the
claim commit collided with nothing).

**Additional exposure incurred mid-pass, named:** reading the delta via
`git show 30d350c` put the applier's full commit message — its evaluative
account and proof claims ("suite 314→319 green; both original fail-open
repros re-driven"; the six per-finding fix summaries) — in front of this
reviewer before findings were drafted. Unavoidable for a landed-delta
review (the diff and its message travel together); every claim in it was
treated as a claim to re-run, and all were re-run below. Named, not denied.

### Attack surface (named as the first act)

- **A1 — the HI-F1 bypass actually reaches the stores it claims.**
  CONFIRMED by live re-drive: a `SESSIONS-ARCHIVE.md` carrying `- [ ]`
  under `docs/sessions/` exits 1 under `--check`; same for a store under
  `_archive/`. Red leg re-driven: with `tools/sizescan.py` reverted to
  `30d350c^` against HEAD's tests, exactly the four new HI tests go red
  (2 failures + 2 errors, `Ran 59`); restored, green. But the bypass
  over-reaches its class — HA1 below.
- **A2 — the HI-F2 fence fail-safe genuinely fails safe.** PARTIAL: the
  named repro (stray fence, marker in the swallowed tail) now counts and
  gates — re-driven, exit 1. But the invariant the comment claims ("an
  unclosed fence must surface a marker, never hide one") is falsified by
  construction — HA2 below.
- **A3 — counter parity.** CONFIRMED structurally: both counters route
  through the shared `_count_list_items`; the cold-count side carries its
  own unclosed-fence test. A `[x]` swallowed by a stray fence in a
  ROADMAP.md counts (test re-run green).
- **A4 — the recorded proofs reproduce.** Suite: **Ran 319 tests — OK**
  (claimed 314→319; the five new tests account exactly). `--selftest` OK,
  including the new store-under-`sessions/` case. Live repo scan: exit 0,
  size-advisory only (the roadmap is +124 over reference from live
  current-truth — correct non-gate). Floors green on every commit this
  pass made (secretscan, leakscan, linkscan hooks).
- **A5 — the doctrine/template edits say what the tool does.** Mostly
  confirmed: RECORD.md's new paragraph matches the implemented gate
  (stores, three live markers, investigate-then-recommend). Two wording
  defects — HA4, HA5. One surface missed — HA3.

### Lens 4 — security & privacy (run manually; scanner discharged)

Scanner discharge, grounds: landed-delta shape — nothing pending for
`/security-review` to read, and the doctrine/template hunks are markdown
its exclusions bar; a clean pass would be definitionally empty. Manual
pass: the tool remains stdlib-only, no exec/network surface; file reads
use `errors="replace"` (no decode crash on crafted bytes); all four
regexes are linear (no catastrophic backtracking shape); the adversarial
file question — can a crafted repo file *hide* a marker? — is exactly
HA2, filed under correctness where its remedy lives. Header-only marker
scanning (first 15 lines) keeps the allow-hatch a deliberate declaration.
No personal-data or leak surface in any hunk; design altitude clean.

### Findings

- **HA1 (MEDIUM, approach)** — the HI-F1 bypass conflates two skip
  classes. `SKIP_DIR_NAMES` mixes *growth stores* (`sessions`, `reviews`,
  `decisions`, `_archive`, `archive`, `intake`) with *non-content dirs*
  (`.git`, `node_modules`, `.venv`/`venv`, four caches, `.idea`,
  `.vscode`), and the bypass exempts archive-store basenames from the
  whole set. "Integrity is checked wherever a store lives" is the right
  rule for the store class; a vendored package's `ROADMAP-DONE.md` is not
  a store where *this repo's* history lives. Probed live: a `- [ ]` in
  `node_modules/somepkg/ROADMAP-DONE.md` and a `- [~]` in
  `.venv/lib/NOTES-ARCHIVE.md` both exit 1 under `--check` — a CI red on
  a file the repo owner doesn't own, with remedy prose ("flip to `[x]` …
  un-harvest to the roadmap") that cannot apply to a third-party file.
  Below MAJOR: fail-closed direction, rare trigger, and the
  `.sizescanignore` hatch works. *Counsel: split the constant into
  `STORE_DIR_NAMES` (bypass applies) and `NON_CONTENT_DIR_NAMES`
  (absolute skip, no bypass), one test per side.*
- **HA2 (MEDIUM, correctness)** — the unclosed-fence fix narrows the
  fail-open; it does not close it, and the comment overclaims. A stray
  delimiter followed by a *legitimate* fenced snippet shifts the pairing:
  a live marker between the stray delimiter and the next one is cleared
  when that "fence" closes, and if no later quoted line happens to match
  the marker shape the scan reads clean. Demonstrated: stray ``` · a
  `- [ ]` marker · a fenced shell snippet · prose tail → `live_item_count`
  = 0, silent. The code comment's invariant — "an unclosed fence must
  surface a marker, never hide one" — is falsified by that construction;
  the swallowed-tail semantics only protect the region after the *last*
  delimiter. Held at MEDIUM, stated against the incentive to grade down
  (a 0-MAJOR verdict closes this cycle): the window needs two
  co-occurring oddities in one file, the fix is strictly safer than
  pre-fix, and no fleet file exhibits the shape — blast radius, not
  rhetorical shape, sets the grade. *Counsel: when delimiters are
  unbalanced at EOF, recount the whole file with fences ignored — the
  true "as if the fence never opened" semantic; ~3 lines, false positives
  only, which the doctrine already prices as "costs a look".*
- **HA3 (LOW, completeness)** — both CI surfaces still describe `--check`
  as cold-content-only. `.github/workflows/ci.yml` ("gates on relocatable
  COLD CONTENT … never on length") and the child template
  `docs/build/templates/workflows/floor.yml` (15-line comment, same
  account, plus the step name "cold content on the hot path") predate the
  harvest-integrity gate; an adopter whose build reds on a buried live
  marker gets no warning from the surface that runs the gate. The tool's
  own output explains fully, which keeps this LOW. *Counsel: one clause
  in each comment (and the step name) at the next CI touch.*
- **HA4 (LOW, quality)** — the template legend's parenthetical
  overclaims: "(the harvest-integrity gate holds archive stores to
  exactly this grammar)" — the gate also treats a `⏳` list item as live,
  which the tri-state legend deliberately doesn't name (it is a queue
  marker, not a box state). "Exactly this grammar" is therefore not
  exact. *Counsel: soften to "holds archive stores to finished-state
  items only" or add the ⏳ clause.*
- **HA5 (LOW, quality)** — RECORD.md antecedent drift: the inserted
  harvest-integrity sentence leaves "And it carries a **trigger**"
  four subjects away from its antecedent (the signal, sizescan) — the
  nearest prior subject is now "the remedy". One-word fix ("And the
  signal carries a trigger").

**No MAJOR.** Per the close rule this pass is **terminal**: the cycle
closes, HA1–HA5 go to the principal for decision (rule 3 — the chain is
self-authored doctrine), and this application does not spawn another
ceremony.
