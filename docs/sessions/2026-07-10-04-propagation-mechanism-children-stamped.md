**2026-07-10 — propagation mechanism built + children stamped.** Built the
load-bearing "thin anchor, fat pointer" architecture the foundation review put
ahead of all further extraction. New `method/PROPAGATION.md`: the mechanism (5
parts — SHA-as-version, standard child block, inlined floor that binds unread,
drift check riding the session-start read, human-in-the-loop pin bump), the
canonical child-block text, the **layer-override rule** (a child may
narrow/append, never silently contradict; a contradiction is a defect to
surface, and the stricter reading wins pending resolution up), and the
**enforcement clause** (read ≠ complied — the review-with-a-more-capable-model
practice is the enforcement, not the document). Versioning decided: commit SHA
*is* the version, CHANGELOG is the human index, tags reserved for milestones.
Wired into method/README + CHANGELOG; ROADMAP propagation block fully ticked.
Committed atelier at **c3676ee** (the pin). Retrofitted both children with the
stamped block: `ros` (PRIVATE, secrets+topology → publish needs scrub;
declares its `docs/PRINCIPLES.md` bearings as narrow/append) and `faves`
(PRIVATE-for-now but publication-bound). Behavioural test passed — the drift
check runs clean at HEAD and surfaces exactly the moved commit from a stale pin.
Next per ROADMAP: extraction can now begin (PRINCIPLES spine + cases, EVIDENCE
harvest A1), or rewire `create-repo` to stamp this block on new repos (the
delivery vehicle for the mechanism just built).
