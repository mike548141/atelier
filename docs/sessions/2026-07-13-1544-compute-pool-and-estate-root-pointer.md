# 2026-07-13 · 15:44 — CI compute as a third spend pool; the estate-root pointer (Opus)

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 80+1 -->
- [2026-07-13 · CI compute as a third spend pool; the estate-root pointer (Opus)](2026-07-13-1544-compute-pool-and-estate-root-pointer.md) — Mike's GitHub-Actions cost fact (private repos meter minutes, 2000/mo free; public free) surfaced a live gap: `MODEL-ECONOMICS` named two spend pools but not the one GitHub bills, and the floor CI comments' "costs seconds, right side of the trade" reasoning was written on public/free atelier yet is the reference **private** children copy. Drafted a third-pool section; an independent un-briefed review (PASS-WITH-FINDINGS) caught real defects — the fix had patched `ci.yml` but not the `floor.yml` **template** children actually copy; the "scope a private floor to PR+default-branch" prescription reopened the never-PR'd-branch hole and undersold private CI's full-cover scan of history that publishes wholesale at go-public; per-minute-rounding, fails-open-with-billing, and standard-runner facts were off. Landed principle-only (`e9f01c1`, `4a71b7a`): the section names the pool + visibility coupling + the honest two-sided trade and **stops prescribing** — frequency and the numbers it turns on aren't atelier's to hold; precedence restated (cost never buys down safety, publication never cost-driven). Both CI comments corrected. Child doctrine block gained an **"Estate resources — point up, don't re-derive"** bullet (canonical + template byte-identical, drift green, 216 pass) so every child references the unnamed estate root for estate-wide facts. Estate half in shed: **Fin of DevSecFinOps** — financial inventory is shed's, ADR 0004 (`shed@18c6ac1`), build-out ROADMAP'd with the GitHub seed. **Owed:** shed inventory structure (2nd datum); children adopt the bullet at next pin bump.
<!-- archivecut:log-entry docs/SESSIONS.md 81+1 -->
- [2026-07-13 · addendum: second review caught a self-inflicted defect (Opus)](2026-07-13-1544-compute-pool-and-estate-root-pointer.md) — Mike asked for a fresh un-briefed pass over the *final* text before close; it found two real findings (`4eac3d3`). **(1)** The rework's "private CI scans branch history at full cover" was **false** — verified the scanners run `--root` (tree at the pushed tip), never the log; `--staged` (the hook's mode) is the only history-aware path, so per-commit cover is the hook's, not CI's. A claim stronger than its evidence, already propagated into the child template; restated as tip-tree cover (go-public argument holds: main-only leaves feature *tips* unscanned). **(2)** The estate-resources prose told a child to name the root in its onramp, but some children are *public* — a public repo naming the estate's credential/inventory root is the name↔posture reconnaissance join RECORD forbids; now a public child references it by local-path convention, never by name. Also: path-filter advice exempts the floor; "not atelier's to prescribe" narrowed to the trim-down; shed's free/2000 figure verified via `gh api user`. Lesson recorded: a review of a *reworked* draft isn't ceremony — the rework is fresh unreviewed code, and here it carried an error the first reviewer's own phrasing seeded.


Mike raised a cost fact: GitHub bills Actions minutes on **private** repos
(2000/mo on his free plan) but not on **public** ones — and asked how it fits
atelier, flagging that capacity-exhaustion should be a known issue I handle, not
alarm about. AWS/self-hosted CI noted as a parked option.

## The gap it exposed

`MODEL-ECONOMICS` named two spend pools (plan-included tokens, usage-billed
tokens) and the "know which pool" discipline — but not the pool GitHub bills:
**CI compute / Actions minutes**. And the gap was live, not academic: the floor
CI comments reasoned *"runs twice, costs seconds, right side of the trade"* —
true on public atelier where seconds are free, but those comments are the
reference children copy, and the fleet's children are **private**, where a push
is not publication and those seconds are metered minutes.

## Doctrine drafted, then reviewed (the review earned its keep)

First draft: a "compute pool" section stating a clean coupling (the same
visibility flip moves the safety rationale and the meter together) — but it
**prescribed** scoping a private floor to PR + default-branch. An independent,
un-briefed adversarial review (per the review-independence rule) came back
PASS-WITH-FINDINGS and caught real problems:

1. **Fixed the wrong file** — patched `ci.yml` (atelier's own, public) but not
   `docs/build/templates/workflows/floor.yml`, the file private children
   actually copy, which still carried the misleading line.
2. **The scope-down prescription reopened a closed hole** — a never-PR'd branch
   scanned by nothing — and undersold that private CI's full-cover secretscan
   protects history that publishes *wholesale* at go-public.
3. Factual: private Actions bill **per job rounded up to the minute** (so *run
   count*, not duration, is the lever — "zero-dep = seconds" saves nothing on
   the meter); exhaustion **fails open and bills** above a $0 limit, not only
   closed; "public free" is standard-runners-only.
4. "Make it public to save minutes" listed as a cost lever inverted this file's
   own "cost never buys down safety" precedence.

## Landed (`e9f01c1`, `4a71b7a`)

- **`MODEL-ECONOMICS` — principle-only.** Names the third pool + the visibility
  coupling + the honest two-sided trade, fixes all four factual points, and
  **stops prescribing**: floor frequency and the numbers it turns on are *not
  atelier's to hold* — they live in the operator's private estate-root repo,
  decided per repo. Precedence restated: cost never buys down safety;
  publication is never cost-driven.
- **`ci.yml` + `floor.yml` template** — both COST NOTEs corrected; the
  template's false "any branch is publication" line rewritten to split public
  (publication, primary gate, free) from private (backstop over the pre-commit
  hook, metered, history publishes at the flip).
- **Child doctrine block gained an "Estate resources — point up, don't
  re-derive" bullet** (Mike's ask: every child should know where estate-wide
  facts live). Canonical (`PROPAGATION`) + stamped template edited
  byte-identical, drift test green (216 pass). Names no repo — atelier is the
  doctrine root and holds no inventory; the estate root is the knowing-root it
  deliberately is not, named only in each child's own onramp.

## The estate half (shed, `18c6ac1`)

Mike's framing: this is the **Fin** of DevSecFinOps — shed knows the estate, so
financial inventory (plans, entitlements, free-vs-metered, one-off/licence
costs) is shed's, the same way credentials are. Confirmed and recorded there as
**ADR 0004** (mirrors shed's 0002 split: atelier holds doctrine, shed holds
inventory), ROADMAP'd as a build-out with the GitHub seed datum. Schema left to
emerge (rule of three) — charter set, structure is honest follow-on.

## Addendum (same conversation) — second review caught a self-inflicted defect (`4eac3d3`)

Mike asked for a fresh un-briefed pass over the *final* text before close (the
first review ran on the pre-rework draft). It earned its keep — two real
findings, one of them introduced *by the first fix*:

1. **False security claim, fleet-wide.** The rework said private CI "scans
   branch history at full cover." It doesn't — verified: the scanners run
   `--root repo repo` (no `--staged`), reading the working *tree at the pushed
   tip*, never the log; `--staged` (the hook's mode) is the only history-aware
   path. Per-commit cover is the hook's, not CI's. A claim stronger than its
   evidence — the exact APEX breach — and it had already propagated into the
   child template. Restated as tip-tree cover (the go-public argument still holds:
   main-only leaves feature *tips* unscanned).
2. **Name↔posture leak vector.** The bullet is clean unnamed, but the prose told
   a child to name the root in its onramp — and some children are *public*. A
   public repo naming the estate's credential/inventory root beside a catalogue
   of what it holds is the reconnaissance join RECORD forbids. Now: a public
   child references the root by local-path convention, never by name.

Also fixed: path-filter advice now exempts the floor; "not atelier's to
prescribe" narrowed to the trim-down. shed's `free/2000` figure **verified**
correct via `gh api user` (finding #5) — no change owed. Lesson: a review of a
*reworked* draft is not ceremony — the rework is fresh, unreviewed code, and here
it carried an error the reviewer's own earlier phrasing seeded.

## Owed

- shed's financial-inventory **structure** — build-out when a second provider
  datum lands (shed ROADMAP).
- Children pick up the estate-resources bullet at their next pin bump.
- Capacity-exhaustion-is-a-known-issue also captured to session memory.
