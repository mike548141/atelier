**2026-07-10 (Opus) — MODEL-ECONOMICS.md: stub → canonical.** The extraction
item after the P2 pin view, same session. The stub already carried the *shape*
(match-model-to-job, know-which-pool self-check, one-doctrine/tiered-authority,
inline-vs-batched review triggering, cost-lowest-precedence); what it lacked to
be canonical was the **general session-hygiene mechanics + cache economics**,
which sit in the ros source but had never been generalised up. Extracted those:
per-model prompt cache (a mid-session model switch re-processes the whole context
at full input price), TTL churn as the expensive pattern, output>input, one-task-
per-session, heavy-skills-are-episodic, point-don't-paste, and keep-the-hot-path-
lean (bulk stays off the every-session read path). **Generalised, not copied** —
the estate-specific numbers (per-token prices, the exact model roster, the
measured ~35k session overhead) stay person-local in ros; a foot-pointer names
the split explicitly so a reader knows where the numbers live. This follows the
extraction rule (keep the bearings, drop the person-local values) and EVIDENCE's
store-the-rule-not-the-value.

Lockstep sweep in the same commit (RECORD): dropped the stub/TODO markers;
`README.md` + `docs/method/README.md` entries swept off "extraction in progress"
to "canonical here, numbers person-local"; ROADMAP item ticked; CHANGELOG gains a
Changed entry and loses the MODEL-ECONOMICS line from Pending. leakscan clean.

Extraction remaining after this: A6 (source-acquisition ladder) + A7
(honest-instrument) into method/, then the build/ layer (create-repo standard +
rewire-to-inherit). **Model note:** Opus, plan-included — a doc extraction, not
token-heavy; no flag.
