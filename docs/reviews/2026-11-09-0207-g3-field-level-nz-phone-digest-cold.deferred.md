# Sibling to the g3-field-level-nz-phone-digest cold pass — held under rule 1's split

Sibling of `docs/reviews/2026-11-09-0207-g3-field-level-nz-phone-digest-cold.md`, held under
`docs/method/REVIEW.md` rule 1's split. **Open only after the phase-1 findings in the brief are
committed.** Written 2026-11-09 UTC by the brief-writer, session `d4a0fcf3` (Opus 5.5), named in the
brief's provenance; it forms no finding and assigns no severity. Fold this file in below the
reconcile and delete it at phase 2.

## Re-run results held back from the brief

Run once by the brief-writer, 2026-11-09 UTC, from the worktree root at `b1f9499`, machine load
averages 10 to 22 throughout:

- `python3 -m unittest discover -s tools -p test_leakscan.py`: exit 0 (Ran 395 tests).
- `python3 -m unittest discover -s tools -p test_report.py`: exit 0 (Ran 102 tests).
- `python3 tools/leakscan.py --selftest`: exit 0 (selftest OK).
- Full suite, `nice -n 10 python3 -m unittest discover -s tools`, Python 3.14.6: 2,643 tests, OK,
  exit 0, 1,167 s. An earlier run on the system Python 3.9.6: 2,307 tests, 4 import errors
  (`test_floor`, `test_floorfleet`, `test_personal_data`, `test_precommit`: a module-level `str |
  None` annotation) and 1 timeout under load (`test_spellscan.BoundedMemory`, which passed alone on
  3.14).

## Prior records on nearby surfaces (named by filename, not opened unless the brief says so, not exhaustive)

- `docs/reviews/2026-10-26-0928-g3-grace-metadata-sets-cold.md`

## Seeded questions (the brief-writer's suspicions, a floor not a fence)

1. `_phone_inside_hex_digest`: a real NZ number glued to hex letters, for example in a URL or an id
   `abcd0211234567ef`. What does a 16+ hex run permit that a person's number can sit in? Option 2
   and 3 in `320/470` were not taken.
2. `_HEX_CHARS` is defined after the function. Harmless, but the function reads a module global:
   fine under an import cycle?
3. The Exif walker: endianness, offsets past the block, IFD loops, a SubIFD or the GPS IFD reached
   twice. Does a crafted file make it report a benign field while GPS sits unread, and does unread
   map to `unknown`?
4. A tag the table does not name: named `0x....` and kept by a line that lists it. Can one manifest
   line keep a GPS tag under a hex name that a human reads as harmless?
5. XMP: "one field per top-level property" with a value and its structure as one field. A property
   that nests GPS or a person's name under a benign top-level name: is the keep too wide? The
   principal's example is GPS versus camera model.
6. The XML parse: entity expansion, a packet split across APP1 and extended XMP, duplicate
   properties in two `rdf:Description`s, a namespace prefix redeclared to look like `dc:`.
   "Well-known namespaces use their usual prefix whatever the packet declares": can that make a
   hostile URI read as `dc`?
7. PNG `%XX` keywords and the `%75nknown` escape: is the encoding injective, so one field cannot
   read as another?
8. The dated flip: on 2026-12-18 type-level lines stop keeping. What happens to the children that
   hold them, and is every affected child warned by then?
9. `bare 2:090 continues the same set` and comma-merged fields: can a parse slip widen a line to
   another set?

## Facts held back from the brief

- The item cites `29021b9` for part 1. That hash is not on `main`; `2ba261b` is the landed commit
  with the same subject. The brief names `2ba261b`.
- `e269f59` (the G3 application) touched the same paths at 2026-11-09 UTC; the item predates it.
