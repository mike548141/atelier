# Repo relationships beyond the parent/child tree (Mike commissioned, 2026-09-12)

Two related asks landed in the same message, neither answered by existing
doctrine, both about relationships **atelier's tree doesn't model**.

`PROPAGATION.md` models exactly one relationship: atelier is the parent, a
repo that adopts its doctrine is a child. That is not the only real
relationship in the estate. His words: *"Better ways to manage groups of
repos and relationships between repos. That could be other repos using the
credentials in shed, child repos of atelier, or the group of repos that
relate to a common subject like my estate (including shed, docker-heap,
homenetwork etc) or home automation (can't remember there names but hac,
numen, kahuranga etc)."* Three distinct shapes are tangled in that one
sentence, kept separate below rather than collapsed into one item:

1. **Consumer-of-asset** — a repo using a credential `shed` holds is not a
   doctrine relationship at all; it is a dependency with no doctrine home.
2. **Subject/domain clustering** — repos grouped by what they're *for*
   (estate infrastructure; home automation) rather than by who they inherit
   doctrine from. Mike named the home-automation repos tentatively and
   flagged his own uncertainty about their exact names — carried here as his
   hedge, not corrected or firmed up.
3. **Authorized-access protection**, item `020` below — a related but
   separate ask about `shed` and client-data repos specifically never
   reaching unauthorized people, which is about *who may act*, not about
   what a repo's relationship to another repo *is*.

No mechanism chosen for any of the three. This section exists so the three
shapes are visible together without pretending they are one problem.
