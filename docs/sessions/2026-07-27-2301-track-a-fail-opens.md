# 2026-07-27 · 2301 UTC · Track A — the fail-opens closed, all five items

**Seat:** Opus 5 (1M context), worktree `track-a-fail-opens`.
**Ask:** *"Work Track A of the policy-as-code programme in docs/ROADMAP.md.
Bring me the EP1 and EP3 rulings first, in plain language with impacts"* —
followed mid-turn by *"There is a parallel session so take precautions"*.

Track A was the one track of five with real exposure: *the floor can report
green while checking nothing.* All five items are closed.

## The rulings, and why they were cheaper than the roadmap said

Both 🎯 items were ruled by Mike after a plain-language walk-through. The
walk-through's substance was **two measurements that contradicted the
roadmap's own statement of the cost**, and both pointed the same way — the
strong fix was affordable.

**A1/EP1 — the roadmap said the fix "reds any child whose declared scope has
drifted … an immediate blast radius".** Measured against the estate before
writing anything: of 19 repos, **2** declare `scope`/`flags` at all (atelier
and `ros`), and **all four declared paths resolve**. Of 14 repos with a floor
config, **0** lack their declared records tree. The decisive structural fact:
every scanner with no advisory form defaults to the repo **root**, which always
resolves — so the skip branch can only reach a boundary check through an
*explicit* declaration, and the three docs-scoped scanners that genuinely need
the skip are all advisory-capable. The two cases do not overlap. **Blast radius
today: zero.** It is future drift the change catches.

**A2/EP3 — the roadmap said requiring terms "fails closed on … every CI runner
by design".** Not for a hook-plane change: both workflows invoke `--plane ci`,
and the hook template is never invoked by CI. No test executed a real
hook-plane `leakscan` either. The real cost is **one** thing — a fresh clone on
a machine with no term list blocks at its first commit, with the remedy already
printed.

**Rulings:** A1 → **(a)+(c)**, report *and* refuse, with (b)'s stated-reason
requirement deferred to ride with C1's schema change. A2 → **(c)**, both halves.
On A2 Mike asked why (a) was recommended over (c) before ruling; the answer —
that (a) makes the degraded-render path unreachable on the hook plane, leaving
only CI's already-declared case — was given, and he ruled **(c) anyway, for
measurement over inference**. That is the better call and it is why the terms
reporting exists at all.

## What was built

**A1 — the scope fail-open.** An unresolvable declared path is now a hard
config error for any scanner with no advisory form, not a skip. The skip
survives for the softenable docs-scoped checks, which is the case it was
written for. Extended past the finding as written: the review described a scope
resolving to *nothing*, but the class is *any* declared path that does not
resolve — one of two paths going missing halves a boundary check's cover the
same way, so partial drift blocks too. `floorfleet` now reads `scope`, `flags`
and a non-default `docs` on the board and in `--json`.

**A3 — settled by A1, at the mechanism.** `floor.py`'s docstring claimed
`flags` was *"read out estate-wide by floorfleet"* when floorfleet read neither
key. Fixed by making it true rather than by softening the sentence, and pinned
by tests so it stays checkable instead of becoming true once and drifting back.

**A2 — the hook plane's asserted cover.** The hook template now runs
`leakscan --require-terms`. A `Scanner` may name the flag that gives it full
cover, so a plane whose template omits it renders **🟡 partial** rather than ✅
— CI's `leakscan` is structural-only permanently and now says so on every run.
`floorfleet` reports whether **this machine** carries a term list.

**A4 — five repo-local seam edges (LS1–LS5).** Actions log-command injection
through a child-authored `why` (encoded at the point of interpolation); an
executable non-Python script with no shebang crashing the floor with a
traceback (now a clean BLOCK, summary preserved); a committed symlink executing
out-of-tree code (realpath containment); unknown keys in a local declaration
read past in silence; a disabled local check losing its `local` marking.

**A5b — the parent's row.** Discovery walks children, so the repo that defines
the floor was the one repo the board never checked. Classified on whether the
parent's own workflows invoke `floor.py --plane ci`, with `floor.yml` excluded
from that search — it runs the floor over the *caller's* tree, never the
parent's, so reading it as proof would be the self-exemption A5a already was.

## Two things this surfaced that were not in the brief

**A contract test asserted the opposite of the ruling.**
`test_leakscan_never_demands_the_machine_local_term_list` banned
`--require-terms` on **both** planes. The ban is right for CI and was wrong for
the hook: it read the two planes as one and so forbade the flag on the plane
the design says carries the full cover. Narrowed to CI with its complement
added, rather than deleted — the CI half is still exactly right.

**Three pre-commit tests were passing *because* the hook was degraded, and were
env-gated in the misleading direction.** They inherited the machine's
`~/.claude/leakscan-terms.txt`, so they were green on a laptop and would have
been red on every CI runner. They now pin a term list inside the fixture. Every
suite run in this session was done **twice** — once with a term list, once with
a fake `HOME` and no term list — and the LS1 test sets `GITHUB_ACTIONS`
explicitly rather than inheriting it, because annotation mode is env-gated and
a test that merely runs the floor would pass by never entering the branch it
means to exercise.

## Verification

Every fix was driven live against the same probe the cold pass used to prove
the defect, not asserted from the diff:

| Probe | Before | After |
|---|---|---|
| Hard scanner, scope typo'd | rc 0, silently uncovered | rc 1, remedy named |
| Partial scope drift (1 of 2 paths) | rc 0, cover halved | rc 1 |
| Code-only repo, no `docs/` | ⏭ skipped | ⏭ skipped (preserved) |
| Hook plane, no term list | ✅ enforced, rc 0 | ❌ blocked, rc 1 |
| CI plane, structural-only | ✅ enforced | 🟡 partial cover |
| `why` carrying `\n::error::` | spoofed annotation emitted | inert, `%0A`-encoded |
| Executable script, no shebang | uncaught traceback | clean BLOCK, summary kept |
| Symlink to out-of-tree script | out-of-tree code executed | blocked, nothing ran |
| Unknown local keys | accepted silently | rc 1, keys named |
| Disabled local check | `local: false` | `local: true`, `· local` tag |
| Parent that drops its floor | invisible | 🛑 absent, `--check` reds |

**Tests: 694 → 720**, OK in both environments. `floorfleet --selftest` ok.
atelier's own floor green at every commit; `ros` — the one child that scopes
*and* flags `leakscan` — still green.

## Estate impact Mike should know about

The hook-plane change binds on every child the moment their `hooks.atelierTools`
resolves to an updated atelier checkout, because that is the point of the
one-registry design. This machine has a term list, so nothing breaks here. A
**new machine or a fresh clone** will block on its first commit until
`~/.claude/leakscan-terms.txt` exists — deliberate, and now documented as a
once-per-machine step in the child CONTRIBUTING template, which said only
"two lines" before.

## Concurrency

A parallel session was flagged mid-turn. Work was already isolated in a
worktree; the added precautions were explicit-path staging throughout (never
`-A`, per the nested-worktree hazard), and writing `ROADMAP.md`/`SESSIONS.md`
last, after a rebase on `origin/main`. `origin/main` carried no new commits at
merge time.

## Owed

Rule 4: each application earns a further cold pass while a MAJOR stood, so a
`⏳` is queued in the landing commit. **Not spawned by this session** — the
applier does not spawn its own review. Three MAJORs (EP1, EP2/A3, EP3) from the
ADR 0008 pass are now applied, and all five local-seam findings; EP4–EP10
remain unapplied and are untouched here.

*Corrected 2026-07-28 (TA8, Track A application cold pass): this line read "two
MAJORs (EP1, EP3) and one minor (EP2/A3)". The ADR 0008 verdict grades EP2
**MAJOR** — its reconcile narrowed EP2's blame, not its grade. Substance was
unaffected, EP2 was applied in full, but a record that demotes a MAJOR in
passing is the drift these records exist to prevent, so the correction is
stamped rather than silently swapped.*
