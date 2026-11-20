- [x] **Actual spend (plan or usage) vs the API-usage estimate — BUILT
      2026-07-22** (`1711711`, merged `12613e0`): machine-local `spend`
      block (plan mode: months × fee + uncovered; usage mode: invoiced
      figures per month), reconciliation footnote with Δ $ and %, honest
      partial/unavailable degradation, JSON/CSV meta; 139 tests green;
      also fixed a pre-existing USD×rate² defect in the Actual footnote.
      Review: self-verifying class (instrument code under its test floor,
      no doctrine surface — ECONOMICS § Match the ceremony). Original item,
      for context — the money-side
      analog of the ccusage cross-check. ccrepo's cost is an API-list-price
      *estimate*; the billing model (`ccrepo-billing.json`) already apportions a
      flat plan fee into an Actual column, but Mike wants to compare **what he
      genuinely pays** — a subscription tier (e.g. Max 5x/20x) or metered usage —
      against what ccrepo computes from API usage, and see the delta. Needs a
      machine-local source of real spend (plan tier + period, or an exported
      usage/invoice figure) and a reconciliation footnote like the ccusage one but
      for dollars actually billed. Personal data ⇒ the spend source stays in
      `~/.claude`, never a repo (same boundary as `ccrepo-billing.json`).
      🎯 fill-the-config residue stays live in ROADMAP.md.
