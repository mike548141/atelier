# Deferred sibling — standing checklist and test-assumption rule (160/710)

**Held under REVIEW.md rule 1's split. Open only after your phase-1 findings in
`docs/reviews/2026-10-16-1551-standing-checklist-test-rule-cold.md` are
committed.** A floor, never a fence: these questions were seeded by a brief-writer
who read the landing diffs and commit bodies, so they carry that reading's
framing. Reconcile against them; do not let them narrow what you found.

## Intent record (not opened by the brief-writer)

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md`

## Prior verdicts on the same surfaces (named, not opened)

None names the checklist section or § 15. Verdicts that touched the review-brief
skill or `REVIEW.md`'s lens text, for the reconcile:

- `docs/reviews/2026-07-21-2158-review-scope-security-lens4-cold.md`
- `docs/reviews/2026-07-22-0244-sl-application-cold.md`
- `docs/reviews/2026-08-02-2348-deferral-delta-cold.md`
- `docs/reviews/2026-07-26-2215-evidence-escalation-rung-cold.md` (`EVIDENCE.md`
  § 13, the neighbour of § 15)

## The queue pointer's own lens hints

None. The pointer is refs-only, plus the orchestrator's brief-writing claim line.

## Seeded questions (the brief-writer's, from the diffs)

1. `90c42ec`'s body names "one addition beyond the record's text, for the
   reviewer to judge": the one-line discharge clause. Is an author-flagged
   addition to principal-approved text itself a change that needed his ruling
   before landing, under rule 3?
2. The section's header says "Approved by the principal 2026-07-23, item by item"
   and "homes unamended" appears in the commit body. Does the landed text name a
   home for any check that the 2026-07-23 approval did not (for instance
   `stampscan` on V3, or "Not mechanised" on V7)?
3. "A brief need not list them" — does that sit with REVIEW.md's lifecycle step 1,
   which says what a brief contains, and with the skill's "Include:" list?
4. The skill paragraph compresses V2 to "re-run every recorded proof in scope"
   and V6 to "security & privacy", dropping the `/security-review` clause. Is that
   compression or narrowing, by the skill's own header?
5. § 15 says a wire capture is an outside authority. One grounding instance is a
   capture harness that read zero everywhere. Does the rule as written tell a
   reader how to tell a trustworthy capture from that one?
6. § 15 cites a child commit by SHA in a public repo. Is that SHA resolvable by
   anyone outside, and if not, does it ground anything for the public reader?
