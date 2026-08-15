- [ ] **Context as a share of the window** (`477k / 1M (48%)`). Wanted — a raw
      figure doesn't say whether a session was near its ceiling. **Blocked on
      evidence, not effort:** the log records the model as `claude-opus-5` with
      no field distinguishing the 200k variant from the 1M one, so any
      denominator today is a guess, and inferring it from the measurement
      ("peak > 200k, therefore 1M") is exactly the grounding failure the
      numeric-limits rule forbids. Unblocks if a variant/window field appears in
      the log, or if a machine-local config states it per model — never by
      inference from the number being explained.

      **Re-tested 2026-07-26 against a positive control, and the block holds.**
      Previously the gap was read off the field list; it has now been checked
      the strongest way available — from inside a session *known* to be the 1M
      variant (`claude-opus-5[1m]`, stated in its own system prompt). Its
      assistant records write `"model":"claude-opus-5"`, with no suffix and no
      sibling field. A search across every log written since 2026-07-25 for any
      key matching `window`/`1m`/`context_limit`/`max_context` returned **zero
      hits**, and the full assistant-record key set (top level plus `message`
      and `usage`) carries nothing that separates the variants. So the two
      variants are **provably indistinguishable in the log**, not merely
      undistinguished — a stronger statement than the one above, and the
      difference matters: the item can't be unblocked by looking harder at what
      is already written, only by a new field or a machine-local per-model
      config. Incidental finds while looking, neither a denominator: assistant
      records carry a top-level `effort`, and `usage.cache_creation` splits
      `ephemeral_1h`/`ephemeral_5m` input tokens (cache TTL, not window size).
