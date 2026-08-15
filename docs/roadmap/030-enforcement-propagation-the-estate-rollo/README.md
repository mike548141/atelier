# Enforcement propagation — the estate rollout (ADR 0008, 2026-07-25)

**Rolled out 2026-07-25.** All 13 children call the floor; `floorfleet --remote
--check` exits 0 against GitHub's default branches. Proven live in CI, not just
locally: one child's floor run passed, another failed on a real `leakscan`
finding — the workflow itself ran clean in both, which is the end-to-end proof
the mechanism works.

> 📦 **2 completed items** in this section → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
>   (the 13-repo wiring, and the repo-specific scoping preserved with it).

- 🎯 **EP1–EP10 — RULED 2026-08-04 and the application DELIVERED
      2026-08-06** (wt: ep-application-0806): EP1(b)'s `flags` half built —
      the `scope` half was found already landed 2026-07-28 in C1 phase 1's
      A1(b), so the ruling entry's "verified absent at HEAD" was itself the
      cycle-state residue class, corrected from the tree — and EP4–EP10 all
      applied as counselled; EP1(a)/(c), EP2 and EP3 verified present
      rather than redone. Blast radius measured, not estimated: zero repos
      red at their next push. The deferral surfaced at close —
      the legacy-spelling exemption postponing the forcing function to C1
      phase 2 — was **RULED 2026-08-09 (Mike): bite now**, and applied
      the same day: on a never-softened scanner the legacy `scope`/`flags`
      spelling is a config error naming the reasoned form; softenable
      checks keep it until C1 phase 2. One declaration estate-wide moves
      from exempt to blocked. Verdict:
      [ADR 0008 cold pass](../../reviews/2026-07-26-2215-adr0008-enforcement-propagation-cold.md);
      detail + the withdrawn-Opus-pass history →
      [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *The EP application*. The
      MAJORs keep the cycle open — the application's rule-4 pointer is
      queued in § *Doctrine — review-owed*.

### Boundary findings surfaced by the measurement — triage separately

These are **real findings the guards were never run to catch**, not rollout
blockers to wave through. Each needs eyes before its repo can go green.


Deliberately generic here: atelier is public, so naming which private repo holds
committed credentials — and in which file — is reconnaissance, not a record. The
per-repo detail belongs in the operator's private estate-root repo, and the
triage list lives there. Only the *classes* are named below, because the classes
are what generalise to any adopter.

> 📦 **1 completed item** in this section → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)
>   (the tracked data export — ruled, executed, and the three things its triage
>   surfaced that the original entry could not have known).

- **Two clock times read as an IPv6 address — FIXED 2026-08-06** (found
      2026-07-26; ruled 2026-08-04 via E7's D2; one landing with E4): the
      rule now requires `::` or four-plus groups, must-flag/must-pass tests
      both directions. → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md) § *E7 built*.

### Candidate invariant — the public-record join, breached three times


### To be considered — the ranked residual after the rollout (Mike, 2026-07-25)

What is *not* covered now that policy propagates by call. Ranked by how much
real protection each would add. Item 1 has its own section below with four
costed options; the rest are recorded here with their reasoning so the next
session inherits the thinking rather than re-deriving it.

**1. Nothing runs `floorfleet` automatically** — the biggest structural gap. The
enumerator exists and was never scheduled. Fully specified in the section
immediately below (four options, one of them explicitly rejected).

**2. A red CI does not actually stop anything — and the obvious fix is wrong.**
The instinctive answer is branch protection with required status checks. Two
findings, one of them a reversal worth recording:

- The **private children cannot have branch protection at all** — GitHub gates
  it behind Pro for private repos. So this is a *spending* decision before it is
  a technical one.
- **atelier can, free, and currently has none.**

  🚩 **Recommendation reversed after thinking it through: do NOT enable it on
  atelier.** Required status checks block direct pushes to `main` until CI
  passes, and this estate deliberately runs commit-small-push-fast to main. It
  would mean waiting on a runner for every commit, or routing one-line doc fixes
  through PRs — a large, permanent tax on the working rhythm to catch a case the
  pre-commit hook already catches earlier, at commit time.

  **The honest framing to carry forward:** the floor is enforced *at commit time*
  by the hook; CI is the backstop, not the gate. That is a defensible design, and
  it should be stated rather than left implicit — because its corollary is that
  **`--no-verify` is the real hole**, and it was used twice during the rollout
  itself (both times deliberately, both times recorded in the commit message).
  Anyone revisiting this should decide whether that hole is acceptable, not
  assume it away.

**3. Three PUBLIC repos in the account have no scanning at all** —
`cel-web-hosting`, `fpx`, `homelablabelmaker`. They were never atelier children
(no `CLAUDE.md`, no pin), so `floorfleet` correctly does not report them: it
reports children, and these are not. Naming them here is not the private-repo ×
posture join — they are public, so the absence of a workflow file is already
visible to anyone. **Whether to adopt them is a scope decision, not a defect
fix.** The relevant question is not "are they tidy" but "is anything in a public
repo that should not be public", which is exactly what the scanners answer.

**4. A blind spot worth closing cheaply.** **CLOSED 2026-07-28 as B3** — and
the proposed shape was costlier than it needed to be. The suggestion was one
`gh api repos/{owner}/{repo}/actions/permissions` call per child; that endpoint
requires GitHub's **Administration** permission, which is the repo-*settings*
permission, so taking it would have widened the scheduled check's token across
the whole private estate for one boolean. It is used when the token happens to
carry it and inferred from run history when it does not — a floor that has never
run is the same practical absence whatever switched it off — and the board
declares which authority answered. Detail →
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

**5. `advisory` needs a stated reason and an expiry.** `disabled` requires a
reason; `advisory` does not, and neither carries a review date. So an advisory
declaration can sit indefinitely — **the "honour it manually" decay in a new
costume**, which is the precise failure ADR 0008 exists to end. Fix shape: make
`advisory` take `{scanner: reason}` like `disabled`, add an optional
`review-by` date, and have `floorfleet` flag any advisory past its date (or with
no date) so the board ages them rather than accumulating them silently.

### 🎯 Schedule the conformance check — the last structural gap (Mike, 2026-07-25)

**The gap, stated plainly:** `floorfleet` is the instrument that turns "I hope
the policy propagated" into "I know it did" — and nothing runs it. It only knows
when a human types the command. That is the same shape as the defect this whole
change fixed: a guard that exists, works, and is pointed at nothing.

**What it would catch that nothing else does.** A child's `floor.yml` edited back
into a copy or deleted · a fresh clone (or a new laptop) where nobody ran
`git config core.hooksPath` · a child that pins `@<sha>` and quietly freezes
propagation · a new repo that never adopted the floor at all. Every one of those
is an *absence*, and an absence never raises its hand.

**The constraint that makes this a decision rather than a task.** atelier's CI
runs on a GitHub runner with no access to the private children. Reading their
default branches needs a token — a fine-grained, read-only (`contents` +
`metadata`), expiring PAT scoped to exactly those repos. That is a new credential
and a new trust surface: **an always-confirm floor action, and the minting is
Mike's, never the agent's.**

Four ways, same goal, very different blast radius:

**RULED AND BUILT 2026-07-28 — Mike chose B**, the scheduled workflow in the
private estate-root repo. A (token in atelier's public CI) and C (local cron)
closed unchosen; D (the session-close ritual) stayed rejected. All four options
are preserved verbatim with their dispositions in
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md), because a decision is only legible beside
what it was chosen over.

**B1 IS LIVE — token minted and the job PROVEN end to end (2026-07-28).** Mike
minted `FLOORFLEET_TOKEN` (fine-grained, read-only, expires 2026-10-27, all
repos, read on actions + code + metadata, no user permissions, **no
Administration**) and set it in the estate-root repo's secret store. A
`workflow_dispatch` run then proved the whole path on a runner with **no local
clones**: 13 children plus the parent enumerated from GitHub, every run status
read, exit 1 on the five red floors — failing for the right reason, which is the
only kind of red worth having. Detail →
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

> 🔎 **The degraded-authority path proved itself in production, not just in
> tests.** The board printed *"Actions-off was INFERRED (not read) for 14
> repo(s)"* — the token deliberately lacks `Administration: read`, so the check
> fell back to run history **and said so on the board** rather than letting a
> reader assume the stronger authority. That was the design argument for
> declining the wider permission; it is now a demonstrated fact.

**What the item got wrong, worth keeping.** It costed the work as "small: the
schedule, `--check` wiring, and a failure message". The premise was that
`--remote` was remote end-to-end. It was not: `--remote` read each repo's
*content* from GitHub and still *discovered* children by listing directories
beside the atelier checkout, so on a GitHub runner it would have found nothing
and exited 2 — fail-safe, but not a check. That is the same class as everything
else this programme keeps finding, one level further out: **the estate this
board could see was the estate that happened to be cloned on one laptop.**
`--from-github` was the real work, and it closes the tool's own documented
blind spot as a side effect.

### Licence gate — ENABLED estate-wide (Mike ruled 2026-07-25)

Mike overruled an earlier deferral of mine, and was right to: I had weighed the
gate as *tidiness* for private repos. His framing — **"I want the licence gate
enabled so those repos are ready to publish"** — is protection, not
housekeeping. Publish-readiness is the whole point of the gate; deferring it
until a repo is already public is backwards.

**Landed on 11 of 13.** 10 declare `Apache-2.0` and pass; 3 are `disabled` with
a stated reason (below); one needed a false-positive marker.

> 📦 **2 completed items** in this section → [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md)


### For your consideration — ideas raised this session, not yet decided (2026-07-25)


Suggestions the rollout surfaced that were never queued. None is urgent; each is
recorded so it is a **choice** rather than something that quietly evaporates.



The **tracked-shim check** landed 2026-07-26 — `floorfleet` now reports
`shim:` (a repo fact, so `--remote` carries it estate-wide; all 13 children
`current`) separately from `hook:` (still machine-local, since
`core.hooksPath` never travels) → detail in
[`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).

The **suggested-fix** strand closed 2026-07-26: `linkscan` now prints the
replacement path where it is uniquely computable, advisory-only (`b89a306`)
→ detail in [`ROADMAP-DONE.md`](../../ROADMAP-DONE.md).
