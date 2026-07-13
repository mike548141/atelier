# 2026-07-13 · 15:44 — CI compute as a third spend pool; the estate-root pointer (Opus)

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

## Owed

- shed's financial-inventory **structure** — build-out when a second provider
  datum lands (shed ROADMAP).
- Children pick up the estate-resources bullet at their next pin bump.
- Capacity-exhaustion-is-a-known-issue also captured to session memory.
