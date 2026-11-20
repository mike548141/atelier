# 2026-07-10 · child CI scanner floor — the public scanners now gate child repos (Opus)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 49+1 -->
- [2026-07-10 · child CI scanner floor — the public scanners now gate child repos (Opus)](2026-07-10-27-child-ci-scanner-floor.md) — took the standing-open half of the CI story (sessions 23 + 26 both left it): **wire the public scanners into child CI**, unblocked by the public flip (ADR 0005). `docs/build/templates/workflows/floor.yml` — a language-agnostic scanner floor any doctrine-inheriting child drops in *beside* its `ci.yml` (correctness vs publish-safety, two files). It sibling-checks-out `mike548141/atelier` and runs its public secretscan/leakscan/linkscan against the child's own tree (`repo/`) on every push + PR — the CI backstop to the hook, which only guards its own clone. Design calls in the header not buried: **floats `atelier@main`** (a security floor wants newest; and avoids a second stamped-SHA drift surface — CLAUDE.md's pin stays the sole doctrine-version truth; `ref:` commented for reproducible-CI wanters), **leakscan structural-only** (machine-local term list — same honest scope as atelier's own `ci.yml`), **licenscan commented** (no-LICENSE hard-fails it → it's a *publish* gate, wrong to default-on for a private child like numen). Scoping to `repo/` is load-bearing (a whole-workspace scan false-positives on atelier's own fake-secret fixtures — proven). Known-failure driven (EVIDENCE §14): clean child 0/0/0, damaged child (real `AKIA…` + broken link) blocks — after a self-caught false start using the whitelisted AWS *example* secret. Wired into create-repo (seed step 3; step 6 "not wired yet" retired), REPO-STANDARD file set, pinned by 5 `test_templates.py` tests (one-source · repo-scoped · structural-only · licenscan-commented · least-priv; suite 190→195). **Left open:** not yet run on a real child (numen predates it); review-owed (net-new CI tooling).


Took the standing-open half of the CI story that sessions 23 and 26 both left as
their explicit "left open": **wire the public scanners into child CI**. It was
blocked until session 22 flipped atelier public (ADR 0005) — a child's CI can
now `git checkout mike548141/atelier` and run its public `tools/` with no secret,
no vendored copy, no drift. The build is one new template file plus its wiring;
the substance was in the design calls, each proven before claimed.

## The deliverable

`docs/build/templates/workflows/floor.yml` — a language-agnostic **scanner
floor** any doctrine-inheriting child drops in *beside* its `ci.yml`. Two
concerns, two files: `ci.yml` gates **correctness** (sized to the repo type),
`floor.yml` gates **publish-safety** (identical for every repo). It sibling-
checks-out atelier and runs its public secretscan/leakscan/linkscan against the
child's tree on every push + PR — the CI backstop to the pre-commit hook, which
only guards the clone it's installed in (git transports neither hooks nor config,
so a fresh clone, a teammate's machine, or a web edit commits unscanned).

## The design calls (in the header, not buried)

- **Floats `atelier@main`, no pinned SHA.** A security *floor* wants the newest
  scanner: a tightened scanner that newly flags the child has found a latent
  issue that was always there, not spooky drift. And pinning here would create a
  **second stamped-SHA drift surface** — the CLAUDE.md doctrine pin stays the
  *only* SHA to keep in sync, which the whole keystone lesson (sessions 18/20)
  says to minimise. A commented `ref:` is there for anyone who wants reproducible
  CI instead. This is the deliberate opposite of the doctrine pin's reproducible-
  by-SHA stance, and the header says why the two differ.
- **leakscan structural-only** — no `--require-terms`. The literal person/estate
  term list is machine-local by design (`~/.claude`, never in a repo), so CI
  cannot hold it and must not. Identical honest scope to atelier's own `ci.yml`;
  full leakscan cover lives on the real-machine hook.
- **licenscan commented, not default-on.** Driven the question rather than
  assuming: with no LICENSE, licenscan hard-fails ("all-rights-reserved,
  publish blocked") — correct before going public, *wrong* for a private/pre-
  licence child (e.g. numen), which it would red on every push. So it's a
  *publish* gate: present but commented, with an enable-note.

## Grounded, not assumed

- **Cross-directory scan works.** Ran each scanner as the workflow does
  (`python3 atelier/tools/X.py --root repo repo`) against a scratch child — clean
  tree passes, a missing link fails. Confirmed the scanners take a target tree
  that isn't their own repo.
- **Scoping to `repo/` is load-bearing, proven.** Sibling layout (child at
  `repo/`, atelier at `atelier/`), scan pointed at `repo/` only → isolated and
  clean. Scanning the *whole workspace* `.` instead → exit 1, because atelier's
  own tree carries deliberate fake-secret **test fixtures** that false-positive.
  So the scoping is a correctness requirement, not cosmetics — stated in the
  header.
- **Known-failure discipline (EVIDENCE §14).** Proved the floor *catches*, not
  just passes: clean child → secretscan/leakscan/linkscan all 0; damaged child
  (a real `AKIA…` access-key-id + a broken link) → secretscan and linkscan both
  block. A false start here was instructive: my first "damaged" fixture used the
  literal AWS *documentation example* secret (`…EXAMPLEKEY`), which secretscan
  correctly whitelists as a placeholder — my bad input, not a scanner miss;
  re-proven with a genuine key shape.
- Full local floor before commit: 195 tests OK, four selftests OK, the whole-tree
  triad + linkscan all clean over atelier.

## Wiring + the contract pin

- **create-repo** (machine-local skill): step 3 now seeds
  `workflows/floor.yml`→`.github/workflows/floor.yml`; step 6's "CI scanning for
  child repos is **not wired yet**" note is **retired** — replaced by "the hook
  is the local gate, floor.yml is the CI backstop."
- **`docs/build/REPO-STANDARD.md`** — floor.yml added to the standard file set,
  distinguished from `ci.yml` (correctness vs publish-safety).
- **`tools/test_templates.py`** — 5 new tests pin floor.yml's load-bearing
  invariants against an innocent edit: fetches the one source
  (`mike548141/atelier`), every active scan scoped to `repo/` (not `.`), leakscan
  has no `--require-terms` (asserted on the run line, since the header prose names
  the flag to explain its absence), licenscan stays commented, least-privilege.
  Suite **190→195**.

## Left open

- **The remaining CI edge:** atelier's own `ci.yml` runs the tool test suite +
  scanner selftests (it *owns* the tools); child `floor.yml` deliberately does
  **not** (it trusts atelier's own gate that the tools work) — a child that
  wanted belt-and-braces could add a selftest line, noted but not built.
- **Not yet exercised on a real child.** numen predates this and has no
  `floor.yml`; the next real scaffold (or a numen pin bump) is where floor.yml
  first runs on GitHub for real. Proven locally end-to-end; the live-on-GitHub
  proof is owed, same as any template until a child uses it.
- **Review-owed.** This is net-new CI-facing tooling; per the don't-stack rule it
  hasn't been reviewed. A future Fable sweep candidate (the sharpest assumptions
  to attack: does the sibling checkout actually isolate on a real runner? does
  `atelier@main` floating surprise a child mid-work? is the `contents: read`
  token enough to check out a second public repo?).
