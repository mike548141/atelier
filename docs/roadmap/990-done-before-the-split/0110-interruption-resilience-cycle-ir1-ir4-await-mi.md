- [x] **Interruption-resilience cycle — IR1–IR4 await Mike's ruling** —
  the rule-4 cold pass on `9c11525` returned **PASS-WITH-FINDINGS
  0 MAJOR · 3 MEDIUM · 2 LOW**, so the cycle is closed terminal (close
  rule); the findings are decided into this backlog item (rule 3 — Mike's).
  Verdict + counsel per finding:
  [`reviews/2026-07-22-0257-interruption-resilience-cold.md`](../../reviews/2026-07-22-0257-interruption-resilience-cold.md).
  IR1 (M): the CLAUDE.md onramp tell overclaims — "no closing entry means
  died mid-flight" also matches a live sibling (live-proven); counsel:
  one-line reword to "died or still live — sweep read-first before assuming
  either". IR2 (M, the author's flagged sub-question): the child CLAUDE.md
  template onramp carries no firing pointer; counsel: propagate one
  sentence via `<atelier-path>`, worded per IR1's correction, at next pin
  bump. IR3 (L): two lines over-wrap (~153-col aside, ~109-col table row).
  IR4 (L): the resume-breadcrumb grammar isn't in the ROADMAP legend.
  IR5 (M, records hygiene) is already **[fixed]** — the authoring session
  left an un-harvested `[x]` redding the shared floor on `main` for three
  pushes; harvested by the reviewing session (this commit), floor re-proven
  green. *review: not warranted — applying the rulings is line-level
  mechanical; the cold pass just reviewed the surrounding text.*
  **RULED 2026-07-22 (Mike): "I take your recommendations on these" —
  IR1–IR4 [fixed]** as counselled, applied + re-proven same day; decision
  stamps in `reviews/2026-07-22-0257-interruption-resilience-cold.md`.
