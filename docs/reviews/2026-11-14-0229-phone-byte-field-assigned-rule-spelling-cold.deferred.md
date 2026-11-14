# Held back — `nz-phone` passes a bracketed byte field, and secretscan's assigned-value rule takes two spellings

Opened only once the reviewer's own findings are durably written (`REVIEW.md` rule 1). A floor,
never a fence. Written by the brief-writer (`cclive` lists it as session `c8eba849`), which did not
author the delta. Nothing here is a finding: these are questions, and facts read off the machine.

## The pointer's own questions

1. Can a real number pass as a byte field?
2. Can the second spelling exempt a line it should not?

## The brief-writer's questions

3. The guard's test is that the whole bracketed run is even-length hex. The `nz-phone` regex admits
   tails of three or four digits, so it matches unseparated shapes of more than one length (fact 1).
   Is every even length it admits a real NZ number shape or not? The ten-digit exception answers one
   length only. Which numbering-plan lengths did the author check, and against what source?
4. The ten-digit exception holds only when the match IS the whole bracketed run. A real number with
   one adjoining hex byte inside the same brackets passes (fact 2). Is that shape ever how a number
   is written (a padded field, a number followed by a check byte, a pasted dump of a contact
   record)? If never, say why; if sometimes, is the exception drawn in the right place?
5. Angle brackets also wrap email addresses, URLs, markdown autolinks, and XML and HTML tags. Can any
   of them leave an even-length run of decimal digits as the whole bracketed text? A bare number in
   angle brackets in prose or a template placeholder?
6. The guard scans outward over hex characters from the match, not over digits. Does a run like a
   phone number with hex letters adjoining it inside brackets still behave as the docstring says?
   Does the digest guard, run first, already decide every case the new guard was meant for at
   sixteen characters, so the two guards overlap or leave a gap at the boundary?
7. The child reported eight-to-sixteen-digit fields from one tool's dumps. Is the fix the narrowest
   that answers it, against an exemption tied to that dump format (the property line around the
   brackets), or against the per-line markers the child already carried? What is the cost of a
   structural exemption every child inherits, against 64 markers in one child?
8. Before the delta, a marker in the short spelling exempted nothing and was counted as naming a
   rule; a marker in the long spelling exempted the line and was counted as naming no rule. The
   delta makes both exempt. Is "either way" in the filing's *Done means* satisfied by widening, when
   renaming the count's list to the long spelling would have fixed the count and widened nothing?
9. `test_allowmarker.py` used a short-spelling marker as its "real scope" case before this delta
   (fact 4): a test asserting a marker names a real rule while that marker exempted nothing. Did the
   delta re-read that test's meaning, and does any other test still encode the old split?
10. The dedupe drops an entropy finding on any line that also has a named or assigned finding, and
    the marker check runs after the dedupe (fact 6). With a scoped marker naming the assigned rule
    on a line that also carries a high-entropy token elsewhere on the line, does the entropy
    finding vanish with the assigned one? Was that true before the delta for the long spelling, and
    does the short spelling now extend it?
11. The fleet probe is "by exit code across 30 child checkouts". An exit code cannot move for a
    narrowing on a child that was already green, or on a finding that is advisory. Did the probe
    compare finding sets as well, and across which planes? Did it include the commit-message plane,
    which landed after this delta (`49f3d407`)?

## Facts read off the machine

Read 2026-11-14 UTC at `d3293d93`, by building inputs from parts in a scratch script and running
`leakscan.scan_text` over them. No phone-shaped literal is written here, by design.

1. Inside angle brackets with nothing else, an unseparated landline-prefixed shape of eight digits
   (the regex's three-digit-tail form) **passes**; the nine-digit form **flags**.
2. An unseparated ten-digit mobile-prefixed shape alone in brackets **flags**. The same shape
   followed inside the brackets by one more byte, either two digits or two hex letters, **passes**.
3. A byte field and a separate unbracketed number on the same line: the number still **flags**. A
   bracket opened and not closed before an eight-digit shape: **flags**.
4. `tools/test_allowmarker.py` line 572 at `57719bfa~1` (from `6d26b058`, the same day) uses
   `secretscan:allow:assigned: real` as the real-scope case in
   `test_each_rule_matching_scanner_counts_a_typo_and_not_a_real_scope`; it reads the same at HEAD.
5. `tools/test_leakscan.py` and `tools/test_secretscan.py` are both listed in `.leakscanignore`, so
   leakscan never reads their fixtures; secretscan's own exemption for its test file was not
   checked.
6. In `secretscan.scan_lines`, `_dedupe_same_span` runs first (an entropy finding is dropped on any
   line holding a `named` or `assigned`-kind finding), then `_scope_exempts` drops findings a marker
   covers. At the parent, the exemption test was `scope in ("", f.rule)`.
