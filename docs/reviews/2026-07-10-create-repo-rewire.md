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

# Verdict — PASS-WITH-FINDINGS (gate cleared on landing of the fixes)

*Reviewer: Fable, cold session 2026-07-10 — no builder context carried in.
Range as briefed (`f72031c..92c0112`; the only commit since, `cc9b886`, is this
brief itself) **plus** the machine-local skill, read in full. Reviewed deep,
driven live: floor re-run, all 18 templates re-read fresh, and the mechanism
exercised end-to-end twice (once as-written, once after the fixes). Ten
findings C1–C10; the brief's bet on its "sharpest three" paid out on two.*

## Floor (re-run, not read)

- Suite **142 OK** at review start → **145 OK** after fixes (test_templates
  added). Three scanner `--selftest`s pass.
- `leakscan docs/build/templates/` clean, structural + local, **and** with
  `--require-terms` (full cover, not degraded). Repo-wide leakscan clean;
  `licenscan --expect Apache-2.0` clean.
- Canonical block vs template block diffed mechanically: **identical today**
  (now pinned so it stays that way — C3).

## The live drive (the brief's real-world check, done as written)

Scaffolded a throwaway static-type repo per the skill's own steps: seed → 3
renames → fill → stamp → hook → planted secret → clean commit.

- **Worked as claimed:** seeding + renames clean; `.gitignore` kept
  `settings.local.json` out of the first commit; fail-closed fired live with no
  config (exit 1, 0 commits); baked config blocked a real `AKIA…` key; clean
  commit passed; the seeded CI gate (`check_links.py`) runs in the child.
- **Broke as predicted (assumption 2):** cloned the scaffold to "machine two" —
  no hook, no `hooks.atelierTools`, and the planted secret **committed with a
  green exit**. The only mention of hooks anywhere in the scaffolded repo was
  inside an HTML comment the template says to delete. → C1.
- **Broke un-predicted (assumptions 1+6 colliding):** the stamped drift check
  **fatals when run verbatim** — the house path contains spaces and the block
  stamps it unquoted (`git -C /Users/mike/Library/Mobile` → fatal). ros/faves
  survive only because they were hand-stamped `../atelier`; the skill said
  `$PP/atelier`, whose two literal readings *both* break. Session 18's "the
  stamped drift-check ran verbatim and correctly read current" is not
  reproducible under the instruction's natural reading — a recorded proof
  stronger than its procedure, the range's own B1 class. → C2.
- **Prose ambiguities hit while driving (per assumption 6, findings in
  themselves):** "set the year + holder" on a LICENSE that has no set line
  (Apache's `[yyyy]` appendix boilerplate, C8); where a *throwaway* scaffold
  may live (the skill hardcodes `$PP`); `<owner/repo>` filled before the
  remote exists (harmless — value is deterministic).

## The nine assumptions, answered

1. **Template-block drift** — was a hope, not a mechanism; the header's "a pin
   bump reviews this wording too" enforces nothing. Now mechanical:
   `tools/test_templates.py` diffs the stamped copy against PROPAGATION's
   fenced canonical on every suite run (C3), and pins the placeholder set (C4).
   Generate-at-stamp-time was considered and rejected: the copy must render in
   a repo where atelier is *absent*, so a stored copy + a mechanical diff is
   the honest shape.
2. **Fresh clone keeps protections — FALSE, proven live.** Protection quietly
   evaporated on machine two (secret committed, exit 0). Fixed at the three
   places a new clone looks (C1); honest residual: documents *instruct*,
   only CI can *enforce* on machine N, and CI scanning is the already-deferred
   scanner-distribution call — the fix closes the *silent* part of the gap.
3. **Fail-closed survives real use — holds.** The block is loud, names the
   exact repair (one command), and the repair is durable for that clone. The
   printed `--no-verify` is honest, not a defect: it's in git's own
   documentation, and hiding it would be security theatre (grounds recorded;
   no change).
4. **`ATELIER_TOOLS` env-wins — acceptable, now stated** (C9). Same trust
   class as the hook file itself (per-clone, set by whoever installs it);
   env-over-config matches git's own convention and the contract tests depend
   on it. Config-wins would break test isolation for no threat-model gain on a
   personal machine.
5. **Templates crossed the boundary clean — holds.** leakscan clean (incl.
   `--require-terms`); fresh-eyes read of all 18 found no personal/instance
   residue. Observation, not a finding: Opus/Fable + plan-vs-billed naming in
   the MODEL-ECONOMICS/reviews templates is the worked-example register
   AUTONOMY already uses; an adopter substitutes their own tiers.
6. **Prose stamp ≠ memory reborn — half-true, now shored.** The *content* now
   comes from files (the rewire's real win), but the procedure was unverified
   prose — and C2 is the proof it can silently mis-execute. Fixed by making
   the stamp self-proving (step 5 now greps for unfilled placeholders and runs
   the block's own drift command verbatim, expect-empty) — the same
   prove-it-once pattern step 6 already had. A `tools/scaffold.py` stays
   [backlog] with grounds: sizing and grounding are genuinely judgement;
   the mechanical core is now instrument-checked; build it if a stamp defect
   recurs despite C5's checks.
7. **Tests pin the contract — holds.** Test 1 *is* the permanent known-bad
   pin: the pre-fix sample fails it, so the defect class can't return
   silently; no `HEAD~1` fixture needed. The "fail closed" stderr assertion
   pins that an explanation exists — a reword must consciously update the
   test, which is the right side of brittle for a contract.
8. **Honest degradation off-machine — mostly holds, one gap.** The
   stop-and-say-so wording is strong and names the memory-reconstruction
   failure explicitly. Gap: iCloud can evict content and leave the *path*
   present — precondition now checks the templates are readable and ~19
   files, not merely that the directory exists (C10).
9. **Step 7's gate — one notch past the grant, as suspected.** "Push is
   recoverable" justifies the push, not the creation of a new outward surface.
   The honest authority is *Mike's ask itself*; rewritten so a
   standardise-existing or local-experiment invocation confirms before
   `gh repo create` (C6). The **outward step itself remains undriven** — no
   throwaway GitHub repo was spun up for this review either; it stays the
   known-owed live proof for the first keeper scaffold.

## Findings — dispositions

| ID | Sev | What | Disposition |
|---|---|---|---|
| C1 | high | Fresh clone loses hook + config silently; nothing in the scaffolded repo says to reinstall (sole mention was in a delete-me comment). Proven: machine-two clone committed a planted `AKIA…` key, exit 0. | **[fixed]** template CLAUDE.md "Hooks don't travel" bullet; CONTRIBUTING once-per-clone install block (skill fills its `<atelier-path>`); hook header + skill step 6 state per-clone scope. Verified: re-drive installed via CONTRIBUTING's own lines — secret blocked, clean passed. Residual (stated): docs instruct, only CI enforces on machine N → deferred scanner-distribution item. |
| C2 | high | Stamped drift check breaks run-verbatim: block stamps the path unquoted, house path has spaces; skill's `$PP/atelier` contradicts the `../atelier` house practice and both its readings break. Session 18's "ran verbatim, read current" claim not reproducible as instructed. | **[fixed]** canonical block + template now quote `"<atelier-path>"` (PROPAGATION + template, kept identical — C3 pins it); skill stamps sibling-relative `../atelier` with an explicit never-unquoted-absolute warning. Verified: throwaway in `$PP`, block's command run verbatim → exit 0, empty. |
| C3 | med | Nothing mechanical keeps the template's stamped block equal to PROPAGATION's canonical text; the MODEL-ECONOMICS template drift proves the class. | **[fixed]** `tools/test_templates.py` — character-for-character diff on every suite run + placeholder-set pin (suite 142→145). The test drew blood in its own build (caught a mis-anchor), i.e. it has teeth. |
| C4 | low | PROPAGATION prose said "three placeholders"; its own block carries four (`<owner/repo>` forgotten). Skill/template said four — three sources, two answers. | **[fixed]** prose corrected; count pinned by test. |
| C5 | med | The seed→rename→fill→stamp core is unverified prose executed by a model — the drift class the rewire exists to kill, alive inside its fix (C2 is the live instance). | **[fixed]** step 5 now ends in a mechanical prove-the-stamp (grep unfilled placeholders; run the block's drift command verbatim, expect empty). **[backlog]** `tools/scaffold.py` if a stamp defect recurs despite the checks — grounds: sizing/grounding are judgement work; the mechanical core is now instrument-checked. |
| C6 | low | Step 7's `gh repo create … --push` "no confirmation needed" rests on "push is recoverable" — wrong grounds for creating a new outward surface. | **[fixed]** authority anchored to Mike's ask; confirm when the invocation didn't clearly include a remote; publishing stays the floor. |
| C7 | med | "Pair it with the same scans in CI" (hook header) and tools/README's CI bullet instruct a wiring a child repo cannot do — the deferral was honest in ROADMAP but the artifacts' own text read as available. | **[fixed]** both now state the gap: child CI scanning is not wired (deferred supply-chain call); the per-clone hook is a child's only scan gate. |
| C8 | low | LICENSE seeded by copying from faves — a second source outside `templates/`, a second machine-local dependency, and "set the year + holder" had no target line (Apache appendix boilerplate). | **[fixed]** `templates/LICENSE` (Apache-2.0 verbatim); skill fills the appendix `Copyright [yyyy] …` line + NOTICE; build/README lists it. |
| C9 | low | Env-wins lets `ATELIER_TOOLS` point the hook at arbitrary code, unstated. | **[fixed]** trust note in the hook header (same trust class as the hook itself; env-wins is deliberate for test/CI redirection). Precedence judged correct — no behaviour change. |
| C10 | low | Precondition checks the atelier *path*, but iCloud eviction can leave a present path with unreadable content — stop-and-say-so wouldn't fire. | **[fixed]** precondition requires the templates dir listable and ~19 files. |

## Lens answers, compressed

**1 Approach:** delivery-vehicle-over-source is the right architecture and this
implementation genuinely delivers it — the skill re-encoded only three things,
all now closed (the placeholder list ×3 statements → pinned by test; LICENSE
sourced from faves → templates; the CI-pairing claim → honest). What it carries
is exactly the sanctioned instance-local set. **2 Correctness/honesty:** the
hook and its tests are solid work; the range's own defect class (claims
outrunning evidence) recurred three times — session 18's drift-check "verbatim"
claim (C2), the CI-pairing lines (C7), the holder-line instruction (C8) — all
corrected. **3 Harvest:** a scaffolded repo is no longer born without a
doctrine block, a licence source, clone-survival instructions, or a
self-proving stamp; it *is* still born without CI scan enforcement — known,
deferred, and now stated at every surface that previously implied otherwise.

## Close conditions — met this session

All ten findings landed [fixed] (C5 carrying its stated backlog strand) and
each fix was **re-driven, not read**: second throwaway scaffold in `$PP` —
stamp proven (no unfilled placeholders; drift check verbatim exit 0), hook via
CONTRIBUTING's own lines (secret blocked / clean passed), throwaway removed.
Suite 145 OK; leakscan (repo + templates, `--require-terms`) and
`licenscan --expect Apache-2.0` clean. **Gate cleared: create-repo may
scaffold keeper repos.** Owed beyond this review: the single outward
`gh repo create --push` live proof (first keeper run), CI scanner
distribution (existing deferred item), and the ros/faves pin bumps that will
carry the reworded block to the children.
