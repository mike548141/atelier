- [ ] 🔎 **`ccrepo` prices the 5.5 generation wrong: Haiku 5.5 counts at $0,
      and Opus 5.5, Sonnet 5.5 and Fable 5.1 take an older model's rate by
      prefix match.** Found 2026-11-12 by the principal's session after a
      routine run; the principal asked for it on the board (his words:
      *"yes, but I suspect its on there its just a low price and I've used a
      small amount"*).
      **Measured on the operator's machine, 2026-11-12:**
      `ccrepo --model haiku -g model` printed `⚠ Unpriced model(s): haiku-5-5
      (161 msgs) — counted at $0`. His suspicion about the amount holds: at
      the published Haiku 5.5 rate the gap is about US$1, not more. His
      suspicion that it is in the table does not: `PRICING` has `haiku-4-5`
      only, and `haiku-5-5` does not start with that key.
      **The larger gap is the one nobody sees, because no ⚠ fires.**
      `priceEntry` picks the longest key that the model name starts with, so:
      | Model | `ccrepo` uses | Published (claude-api skill, cached 2026-10-06) |
      |---|---|---|
      | `opus-5-5` | `opus-5`: $5 in, $25 out, cache read 0.1× = $0.50 | $4 / $20, cache read $0.20 |
      | `sonnet-5-5` | `sonnet-5`: $3 from 2026-09-01 | $2 / $10, cache read $0.20 |
      | `fable-5-1` | `fable-5`: $10 / $50, cache read $1.00 | $10 / $50, cache read **$0.25** |
      | `haiku-5-5` | none: $0 | $0.10 / $0.50 to 100K prompt tokens; $0.50 / $2.50 above |
      So every Opus 5.5 message (most of the estate's traffic) is overstated
      by 25% on base tokens and 2.5× on cache reads, and the one multiplier
      table (`MULT.cacheRead = 0.1`) does not hold for these models. The same
      cached table lists **Sonnet 5 at $2**, where `ccrepo` moved it to $3
      from 2026-09-01; one of the two is stale, to be settled from the live
      pricing page, not from either copy.
      **Shape:** exact entries for the four models (read from the live
      pricing page the skill's `shared/live-sources.md` names); a per-model
      cache-read rate instead of one multiplier; Haiku 5.5's prompt-length
      tier; and a check that warns when a model is priced only by a shorter
      key's prefix, so the next generation surfaces the way an unpriced one
      does. Confirm with the ccusage cross-check, as the `opus-5` fix was
      (README § *`opus-5` had no price*): never fit a price to the logs.
      **Why it matters now:** atelier `440/010` (effective first, then
      efficient, real spend counted) will lean on this tool's per-job cost.
