# 2026-07-10 · atelier's own CI — the floor, dogfooded (Opus)

The natural next build off going-public (session 22): the CI-scan gap didn't just
survive publication, it *dissolved* into a buildable. atelier's tools are zero-dep
stdlib Python, so a public runner needs nothing but Python to run the exact floor
every review had been asserting by hand. Built atelier's **own** CI first — the
self-contained half, and the reference the child-CI half will copy.

## What landed

`.github/workflows/ci.yml`, one job `floor`, on push-to-main + every PR:

1. three scanner `--selftest`s (leakscan/secretscan/licenscan)
2. the tool test suite — `unittest discover -s tools` (145 tests)
3. the scan triad over the whole tree — secretscan, leakscan, `licenscan
   --expect Apache-2.0`

Least-privilege (`contents: read`), concurrency-cancel-in-progress for cost
hygiene.

## The one honest scope call

leakscan in CI runs **structural-only, deliberately without `--require-terms`**.
Its literal person/estate term list is machine-local by design (`~/.claude`, never
in any repo) — so CI *can't* hold it, and *must not* (that list is itself a thing
we keep out of repos). A degraded structural pass is therefore the correct, honest
CI cover; full leakscan cover stays where the term list lives, the pre-commit hook
on a real machine. This is the B5/B7 residual made explicit, not papered over: the
workflow header states it plainly so a green CI badge is never mistaken for full
person-data cover. secretscan and licenscan, by contrast, run at full cover in CI
— they carry no machine-local state.

## Grounded before claimed, watched not assumed

Ran the exact CI command set locally first — 3 selftests OK, 145 tests OK, triad
clean — including a **simulated bare runner** (`env -u HOME GIT_CONFIG_GLOBAL=
/dev/null GIT_CONFIG_SYSTEM=/dev/null`) to prove the git-touching tests
(test_precommit's real `git commit`s, test_worktree) self-configure identity and
don't lean on ambient config. Still 145 OK.

Then the REVIEW re-run-live-proven rule (session 21) applied to a claim I was
about to record: **CI works** is a live claim, so I watched the GitHub run rather
than assume it. First run green in 11s under Python 3.12 — but annotated the
Node-20 deprecation on `checkout@v4`/`setup-python@v5`. Bumped to `checkout@v5` +
`setup-python@v6` (current majors, Node 24), re-ran: green in 7s, 11/11 steps, no
annotation. A warning-free floor keeps the signal honest — a habitually-yellow
badge trains you to ignore it.

## Still open (deliberately not stacked)

- **Child-CI half**: a child's CI checks out `mike548141/atelier` and runs its
  public `tools/` (no secret, no vendored copy, no drift). `ci.yml` is the
  reference to adapt — swap the in-repo tool steps for an atelier checkout.
- **Markdown internal-link check**: the whole pointer/propagation architecture
  depends on links resolving, so this is genuinely wanted — but it's net-new
  tooling that wants its own review, so it was consciously *not* bolted onto this
  CI change (don't-stack-on-unreviewed, applied to tooling).

## Now true for every future session

- atelier has a green `floor` CI on push + PR. A red floor is now a first-class
  signal, not something a reviewer has to reconstruct by hand.
- CI's leakscan is structural-only by design — do not "fix" it with
  `--require-terms`; that would either fail CI or demand the machine-local term
  list enter the repo, which is the exact boundary the tool exists to hold.
