# Observability of the collaboration itself (2026-07-30)

*`review:` refs + open work, not doctrine — the doctrine candidate below queues
its own `⏳` when and if it lands. Account:
[`sessions/2026-07-30-0301-context-atlas-and-trust-window-analysis.md`](../../sessions/2026-07-30-0301-context-atlas-and-trust-window-analysis.md).*

**Where this came from.** A session-telemetry analysis across all 470 priced
sessions found that context size does **not** degrade the work (tool-failure
rate flat from 28k to 934k, ρ = −0.05; the apparent link is a length effect at
ρ = 0.85 against message count), and that what context genuinely causes —
overflow and forced compaction — is confined to the deepest handful of sessions.
Then the same instrument was pointed at three days the principal named as
trust-damaging, and reported them **cleaner than baseline**.
