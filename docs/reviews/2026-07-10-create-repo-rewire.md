# Fable review — the create-repo delivery mechanism (rewire + templates + the scan-hook fix)

**Status:** brief (ask on top). Verdict appended below the divider after the
review runs. **Run this cold** — a fresh session, not the window that built it
(`REVIEW.md`: independence is about context, not just model tier; the builder's
reasoning must not ride along).

Range under review: **`f72031c..92c0112`** (atelier HEAD at brief time), plus
one artifact *outside* the repo: the machine-local skill at
`~/.claude/skills/create-repo/SKILL.md` — it is half of the mechanism and has
never been reviewed in its rewired form. Review deep, not fast: this is the
**birth canal for every future repo**. A defect here doesn't stay here — it is
stamped into each new repo at the one moment installation is cheapest and
scrutiny is lowest. The batch review's sharpest findings (B1, B14) were both
claims that quietly outran their evidence; this batch already yielded one of
the same class (the fail-open hook), found only when the mechanism was finally
*driven*. Assume there are more.

## What the work is (context for the reviewer)

Read first: `docs/build/REPO-STANDARD.md`, `docs/method/PROPAGATION.md`,
`docs/SESSIONS.md` tail (sessions 18–19 + their detail files), the prior
verdict (`docs/reviews/2026-07-10-post-method-review-batch.md`), and the skill
itself at `~/.claude/skills/create-repo/SKILL.md`.

- **The rewire (session 18).** `create-repo` was a second source of the repo
  standard (re-encoded file set/sizing/processes + a private `templates/`
  copy). Now it is a pure *delivery vehicle*: points up to
  REPO-STANDARD/REPO-BOUNDARY/PROPAGATION, seeds from
  `docs/build/templates/` (18 files, moved from the skill), hard-depends on
  atelier being present, fails honestly if absent. Carries only
  instance-local specifics (exemplars, git identity, `gh` account, `$PP`,
  copyright holder, locale).
- **The keystone template.** `docs/build/templates/CLAUDE.md` — previously the
  skill had *no* CLAUDE.md template, so scaffolded repos were born without the
  doctrine block (PROPAGATION bypassed at birth). The template carries a
  **stamped copy** of the standard block (canonical text: PROPAGATION.md) with
  four placeholders the skill fills at scaffold time.
- **The scan-hook fix (session 19).** Exercising the mechanism on a real local
  scaffold surfaced `tools/pre-commit.sample` **failing open**: it pointed at
  `$repo_root/tools/`, and a child repo has no scanners (they live only in
  atelier) — so both scans were silently skipped and a planted `AKIA…` key
  committed with a green exit. Fixed: resolution chain `ATELIER_TOOLS` env →
  `git config hooks.atelierTools` → in-repo fallback, and **fail closed**
  (unresolvable scanner ⇒ commit blocked with an explanation). Step 6 of the
  skill bakes the config.
- **The contract tests.** `tools/test_precommit.py` — 5 stdlib tests driving
  real `git commit`s in throwaway repos (fail-closed; config-resolution
  blocks/passes; env-wins; in-repo fallback). Known-failure was proven once
  against the `HEAD~1` sample. Suite 137→142.

Out of scope (note, don't spend budget): everything verdicted at the two prior
reviews; `worktree.py`/`pins.py`; the deferred CI-scan-wiring question is
*known* open — judge whether it's honestly stated, not whether it's built.

## Scope — three lenses, run all three

1. **Approach & assumptions** (most important): is delivery-vehicle-over-source
   the right architecture, and does this implementation actually deliver it —
   or does the skill still quietly re-encode anything atelier owns?
2. **Correctness & honesty**: does each piece do what it claims; any claim
   stronger than its evidence; anything that *reads* enforced but is manual.
3. **Completeness / harvest**: what the mechanism should cover and doesn't;
   what a scaffolded repo is still born without.

## Load-bearing assumptions to attack

If any is false, the mechanism is mis-built no matter how clean the prose.

1. **The stamped CLAUDE.md copy cannot silently drift from PROPAGATION's
   canonical block.** The template's header says a pin bump "reviews this
   wording too". Is that a mechanism or a hope? Nothing mechanical diffs
   template-block against canonical-block (pins.py watches child *pins*, not
   template *text*). The rewire itself caught the MODEL-ECONOMICS template
   still naming ros canonical — proof this class of drift *happens*. Should
   the block be generated at stamp time from PROPAGATION rather than stored as
   a copy — or is the copy + review-at-bump honest enough if stated?
2. **A fresh clone of a scaffolded repo keeps its protections.** Git hooks and
   `git config` are **per-clone and never travel**. Machine two clones a child
   repo: no pre-commit hook, no `hooks.atelierTools`, possibly no atelier at
   all. Does *anything* in the scaffolded repo (doctrine block? README? session
   onramp?) tell that clone to reinstall the hook — or does protection quietly
   evaporate on every machine after the first? If unstated, that's the same
   silent-gap class as the fail-open hook, one hop later.
3. **Fail-closed will survive contact with real use.** A missing-scanner block
   on every commit in a misconfigured repo is high-friction; the bypass
   (`--no-verify`) is printed in the hook's own output. Does the design price
   the alarm-fatigue → habitual-bypass path (the method-review's drift-check
   alarm-fatigue guard, same logic), or does fail-closed become
   fail-open-with-extra-steps in practice?
4. **`ATELIER_TOOLS` env-wins is safe.** The hook executes
   `python3 "$tools_dir/…"` from an env-controlled path — an environment
   variable can point the hook at *arbitrary code* that runs on every commit.
   Is env-wins the right precedence (vs config-wins-env-fallback), and is the
   trust surface acceptable for a personal-machine tool, stated or unstated?
5. **The templates crossed the personal→shareable boundary clean.** 18 files
   moved from a machine-local skill into the shareable repo; the scrub was
   grep + leakscan. Re-scan with fresh eyes for instance residue the greps
   didn't name (paths, names, entity hints, NZ-specific fragments that read as
   personal context rather than locale convention).
6. **The stamp step is mechanically reliable, not model-memory reborn.** Steps
   3–5 (seed, rename, fill four placeholders, stamp) are *prose instructions to
   a model*, not a script. The rewire's whole thesis was "re-encoding from
   memory drifts". Is a prose procedure executed by a model at scaffold time
   meaningfully different — or should the seed/rename/stamp core be a house
   tool (`tools/scaffold.py`) with the skill as its wrapper? If prose-is-fine
   is the position, what makes *this* prose immune to the drift the rewire
   just killed?
7. **The contract tests pin the contract, not the wording.** `test_precommit`
   asserts on the "fail closed" stderr string in one test — brittle against a
   reword that keeps the behaviour, and conversely a reworded hook could pass
   tests while losing the explanation. And the known-failure proof was a
   one-off against `HEAD~1`, not a fixture — B1's lesson is that one-time
   proofs go stale. Should the fail-open shape live as a permanent known-bad
   fixture the suite exercises?
8. **The skill degrades honestly on machines that aren't this one.** It
   hard-depends on `$PP/atelier` (an iCloud path) and stops if absent. On any
   other machine or a future layout change, does "stop and say so" actually
   happen, or does the skill's framing let a capable model reconstruct the
   standard from training-memory — the exact failure the precondition exists
   to kill? Is the precondition's wording strong enough to bind a model that
   *thinks it knows* the standard?
9. **Step 7's outward action is correctly gated.** The skill's process ends in
   `gh repo create --private --push` labelled "no confirmation needed". Check
   this against AUTONOMY's actual floor: creating a *new* GitHub repo is a new
   outward surface, not just a push to an existing remote. Is the skill's
   confidence aligned with the grant, or one notch past it?

## The real-world check (per `REVIEW.md` — don't skip it)

- **Run** `python3 -m unittest discover -s tools -p 'test_*.py'` and report
  the count + result. Run the three scanner `--selftest`s.
- **Re-run every "live-proven" claim in scope** (the B1 rule, now doctrine-
  recommended): scaffold a throwaway repo per the skill's own steps in scratch
  — seed, rename, stamp, hook, planted secret, clean commit. Report what the
  drive actually did, including any step where the prose was ambiguous enough
  that you had to guess (that ambiguity is a finding in itself, per
  assumption 6).
- **leakscan** the template tree fresh (`docs/build/templates/`), structural +
  local.
- **Read the machine-local skill in full** — it's outside the repo, so no
  other review will ever catch it by accident.

## Disposition & close (reminder)

Findings get stable IDs (**C1…Cn**); each tagged **[fixed]** / **[backlog]** /
**[rejected: grounds]**; a finding closes only when its fix is itself verified.
Then tick the ROADMAP pointer and add a SESSIONS entry.

---
