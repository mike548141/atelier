# 2026-07-22 · 0819 UTC · Harvest-integrity gate cold pass — PASS-WITH-FINDINGS, 1 MAJOR; HI-F1–F6 to Mike (Fable, main)

## Provenance and sequence

The queue's one `⏳` — the rule-4 cold pass on delta `0bdccf3` — taken by a
session Mike opened and pointed at the queue ("Please do any review work").
This session authored none of the gate, its tests, the legend, or the records.
Sequence held: taker-written brief → work reviewed at HEAD → live claims
re-run → verdict committed (`0ce23e1`) → only then the intent record and
`2cd4730` opened → reconcile note (`074fa42`, nothing overturned). Verdict:
[`reviews/2026-07-22-0819-harvest-integrity-gate-cold.md`](../reviews/2026-07-22-0819-harvest-integrity-gate-cold.md).

## What reproduced (lens 2 — all of it)

Suite 314 OK; `--selftest` OK including the archive cases; live repo
`--check` exit 0 (one ROADMAP size-advisory, which never gates — "green" is
honest); all four taxonomy situations tested and behaving; the
state-coherence-only bound held in code; tri-state coherent across all four
surfaces; hatches can't silence the gate.

## Findings (decisions are Mike's — rule 3)

- **HI-F1 (MAJOR)** — archive stores inside `SKIP_DIR_NAMES` dirs
  (`sessions/`, `_archive/`, `archive/`, …) are never integrity-checked, and
  the clean banner still claims "archive stores hold no live markers".
  Reproduced with buried `[ ]` items under `docs/sessions/` and
  `docs/_archive/` → exit 0. The skip list's rationale is size-metering,
  written pre-gate; the gate inherited it unexamined — the same fail-open
  class the tool's own F1 lesson forbids. Latent: the fleet keeps every store
  directly in `docs/` (verified across five repos). Counsel: archive-store
  basenames bypass the skip-dir filter; tests for both locations.
- **HI-F2 (MINOR)** — an unclosed code fence swallows all live markers after
  it (reproduced; fail-open, silent; class shared with `cold_item_count`).
- **HI-F3 (MINOR)** — `RECORD.md`'s account of sizescan still says
  cold-content-only; the second gated condition isn't mentioned.
- **HI-F4 (MINOR)** — the child ROADMAP template carries no checkbox legend,
  so children meet the tri-state grammar only via the gate's failure text.
- **HI-F5/F6 (notes)** — blockquote skipping is correct-but-undocumented;
  unfenced indented code false-positives are an inherent, acceptable
  trade-off (remedy is investigative, so a false positive costs a look).

Lens 4: `/security-review` discharged with grounds (landed delta, markdown +
stdlib Python — nothing it can be aimed at); manual pass clean (no content
echoed, fail-safe exit codes, no network/secrets).

## State at close

Verdict + reconcile + records on `main`, pushed; suite 314 green; floors
green. The `⏳` queue is empty. 🎯 **HI-F1–F6 await Mike's ruling** — the
MAJOR keeps this cycle open (ruling → application → application's own `⏳`).
