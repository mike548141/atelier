# Binary kinds the estate tracks: what each hides, what a guard costs

Board item `115/390`. Run 2026-11-16 (UTC) by a worker of queue run 78ca. This
is a measurement record and a recommendation to rule on. It changes no rule and
builds no guard.

## The question

No guard reads a binary's contents beyond image metadata. So a secret or a
personal detail inside a PDF, an Office file or an archive is unseen, and an
exemption over a binary can only cover the whole file. The principal's answer
to the exception-register redraft's Q4 was *"Separate investigation"* (an
answer to options offered, not a ruling). This note is that investigation:
which binary kinds the estate tracks, what each could hide, what reading it
would cost, and which are worth a guard first by the value ranking of `020/240`
(*written always, checker by value*; a check not built is a recorded decision).

## What already reads binaries

- **G3** (`leakscan`, ruled blocking 2026-08-04) gates every **tracked** binary.
  It blocks until a reasoned, hash-bound `.leakscanbinaries` entry accepts the
  exact bytes. For PNG, JPEG and WebP it also walks the metadata (Exif, IPTC,
  XMP, ICC, text chunks, comments) and runs the text sets through the ordinary
  rules. Its adoption grace ends 2026-11-18.
- **Everything else is accepted whole.** For PDF, Office, archives, fonts, TIFF,
  GIF and the rest, a G3 entry records that a person looked. Nothing reads the
  bytes. The pixels of any image are never read (no OCR); the entry's reason is
  the human check.
- **`secretscan`, `leakscan`'s line rules and `namescan` read no binary.** A
  file with a NUL byte in its first chunk is skipped.
- **Constraint on any new reader:** atelier's tools take zero third-party
  dependencies (`tools/README.md` § *Supply chain*; `PRINCIPLES.md` §8). So a
  reader here is stdlib only: `zipfile`, `zlib`, `gzip`, `lzma`, `re`, `struct`.
  That rules out OCR and a full PDF library.

## Method

For this repo and every sibling git repo under the estate's working directory
(29 siblings), tracked paths only: `git ls-files -s -z` for the list,
`git check-attr filter` for LFS, `file --mime-type` per tracked file for the
kind, `lstat` for size. Where a probe needed bytes (a PDF's `/Author`, a zip's
member names, an image's metadata marker) it read the tracked file and kept
only a count. Nothing in the tree outside the tracked list was opened, and no
path, name or content appears here or in any committed file. "Binary" means
`file` reports a type that is not `text/*`, JSON, XML, SVG or empty.

Limits, stated: sibling counts come from their working trees, so a tracked
file edited but not committed is measured as it stands. A byte probe (the
image metadata markers) is a crude upper bound, not a walk. One text format
(`.dxf`, ASCII CAD) is counted as binary because `file` types it so.

## Census

**This repo (atelier): 0 tracked binaries**, out of 1,418 tracked files. It
holds no `.leakscanbinaries`. Its own tests make their binaries at run time.
The 29 siblings together:

- 11,697 tracked files (plus 13 symlinks); 0 Git LFS files; 0 submodules.
- **633 binary files (5.4% of files), 204.7 MB (46% of tracked bytes).**
- 11 of the 29 siblings track at least one binary. 9 siblings hold a
  `.leakscanbinaries` (974 entries in all: file lines and metadata-set lines),
  8 of them among the 11. The other 3 of the 11 hold 18 binaries between them
  and no manifest. That is outside this note's question, but it is the first
  thing G3 will block when its grace ends.

| Kind | Files | Size | Siblings | Existing read |
|---|---:|---:|---:|---|
| JPEG | 286 | 121.5 MB | 5 | G3 walks metadata; pixels human |
| Opaque data: `age`-encrypted | 88 | (in the 14.4 MB line below) | 2 | whole-file entry only |
| Opaque data: headerless `.bin`/`.enc` | 26 | (as above) | 1 | whole-file entry only |
| PNG | 97 | 16.7 MB | 9 | G3 walks metadata; pixels human |
| PDF | 27 | 41.1 MB | 2 | whole-file entry only |
| WebP | 42 | 1.3 MB | 1 | G3 walks metadata (ICC only here) |
| Office (OOXML: 10 xlsx, 2 docx) | 12 | 3.0 MB | 1 | whole-file entry only |
| Gzip / xz (`.gz`, `.snap`, `.dss`) | 11 | 1.8 MB | 1 | whole-file entry only |
| Legacy Word (`.doc`, OLE) | 7 | 0.3 MB | 1 | whole-file entry only |
| Zip | 2 | 2.8 MB | 2 | whole-file entry only |
| Network captures (`.pcap`, `.pcapng`) | 4 | in the opaque line | 1 | whole-file entry only |
| Other: fonts 5, icons 5, Mach-O 3, script bundles 4, TIFF, audio, CAD, 3D, 1 unidentified | 22 | about 2 MB | 1 to 3 each | none |

The opaque line (`octet-stream` by `file`) is 135 files and 14.4 MB in all:
the 88 + 26 above, the 4 captures, 8 that sit in the "Other" row, and 9
one-byte `.md` stubs that are not content (so they sit in no row of their own).
No tracked SQLite file,
keystore (`.p12`, `.jks`), disk image or Git LFS pointer exists in the estate
today. Those kinds are recorded as absent, not as safe.

Two cross-cutting facts:

1. **Images are 67% of the binary files and 68% of the binary bytes, and are
   the only kind a guard reads.** The unread remainder is 208 files.
2. **Archives hide members from the image walker.** The 2 zips hold JPEGs, a
   CAD file and captures as members. G3 sees one opaque zip and walks no
   member, so a geotagged JPEG inside a zip passes where the same JPEG
   alongside it would block.

## What each kind can carry, and what a read would cost

Costs are estimates from the stdlib reads tried here, not builds. Timing:
inflating every Flate stream in all 27 PDFs (41 MB) took about 1 s, so runtime
is not the constraint on any kind below; the cost is writing, reviewing and
tuning a reader. False-positive risk is the second cost: a reader that fires on
compressed noise gets bypassed or switched off.

### PDF: 27 files, 41 MB, 2 siblings

- **Can carry:** a text layer (names, account numbers, addresses, tax and
  statement detail); Info and XMP metadata (author, producer, creation and
  modification dates, sometimes a file path or the template's origin); form
  fields (4 files have an AcroForm); annotations (5); embedded files and
  JavaScript (none seen in this population, absent by byte probe); embedded
  images (21 files carry image streams, so a scan of a document is a picture of
  it).
- **Measured:** 14 carry an XMP `/Metadata` stream; 6 have a non-empty
  `/Author`; 19 name a `/Creator`; 8 show no font object in plain bytes, 6 of
  them with Flate streams, so likely image-only scans whose text no byte read
  will recover.
- **Cheapest read that sees the main risk:** the **metadata slice**. Read the
  trailer and Info dictionary and the XMP packet (inflating object streams
  where the file uses them, `zlib`), then run the decoded strings through the
  ordinary rule set exactly as G3 does for image XMP. Also flag `/Encrypt`,
  `/EmbeddedFile`, `/JavaScript`, `/Launch`. About 150 to 250 lines.
- **The text-layer slice is the hard half.** Simple-font `Tj`/`TJ` strings come
  out of a content stream with `zlib` and `re`. Subset fonts need their
  `ToUnicode` CMap parsed, and a scan has no text. Expect partial recall and a
  real maintenance tail. It earns its own ruling after the metadata slice has
  run against the 27.
- **False positives:** low for metadata (short, structured strings); moderate
  for body text (hyphenation, ligatures, stray numeric runs trip phone and
  number shapes).

### Office (OOXML): 12 files, 3.0 MB, 1 sibling

- **Can carry:** the full document or workbook text (cell values, formulas,
  comments, tracked changes), the author and last-modified-by names in
  `docProps/core.xml`, a company and template in `app.xml`, custom properties
  (`custom.xml`), embedded files and macros (`vbaProject`), external links,
  and images in `media/`.
- **Measured:** all 12 carry `core.xml` and `app.xml`; 9 carry `custom.xml`;
  2 carry embedded media. No macro project, embedded object, comment part or
  external link seen.
- **Cheapest read:** an OOXML file is a zip of XML, so this is the best ratio of
  all. `zipfile` lists members; the properties parts and the text parts are read
  with a size cap per member and a total-expansion cap, tags stripped, and the
  text run through the ordinary rules. Member names also flag `vbaProject`,
  `embeddings/`, `externalLinks/`. Must not use `xml.etree` on untrusted XML
  without refusing a DOCTYPE (entity expansion); a regex strip avoids the
  question. About 120 to 200 lines.
- **False positives:** low to moderate. The text is real prose or numbers, which
  is what the rules were tuned on.

### Archives: 13 files, 4.6 MB (gzip, xz, zip)

- **Can carry:** anything, one level down: members that are themselves
  JPEGs, PDFs, captures or text, which every other guard then never reaches.
  A `.gz` or `.xz` is one member; a zip is many.
- **Cheapest read:** decompress under a hard size, ratio and depth cap
  (`gzip`, `lzma`, `zipfile`), then feed each member back through the same
  gate as a tracked file of that kind (image walker, text rules, and the
  PDF/Office readers if they exist). Reject encryption, nesting past a small
  depth, and any member whose expansion breaks the cap, as findings, never as
  clean. About 100 to 150 lines, and its value is derivative: it multiplies the
  reach of the other readers.
- **Risk of the reader itself:** it is the attack surface in this list (zip
  bombs, path-traversal names). Caps are the design, not a refinement.

### Printable-string pass (a generic fallback for formats with no reader)

Applies to legacy `.doc` (7, OLE), network captures (4, plus the 4 inside zips),
Mach-O and compiled-script files (about 7), and any unknown kind. Extract
ASCII and UTF-16LE runs of a minimum length and run only the **shape** rules
(named token shapes such as key headers and provider key prefixes), not the
entropy net.
`.doc` text is usually stored as plain 8-bit or UTF-16 text, so a strings pass
sees most of it; the `.doc` summary properties (author) are UTF-16 strings in
the same pass.

- **Can carry:** in a capture, credentials, hostnames, addresses and cleartext
  payloads; in a `.doc`, document text and author; in a compiled binary, a
  baked-in token.
- **Cost:** about 40 to 80 lines. **False positives are the problem:** compiled
  code and compressed streams produce random runs that look like keys, so it
  needs the shape rules only, a length floor, and a cap on findings per file.
  Without that, a Mach-O file reports noise and the guard gets exempted.

### Opaque encrypted data: 114 files

- **88 `.age` files** all begin with the `age` header, so they are real age
  ciphertext, which is the design: the secret is not readable by anything.
  A guard cannot read inside and should not try. The cheap check is the
  header: a file named `.age` that does not begin with it is plaintext in a
  costume. About 10 lines.
- **26 headerless `.bin` and `.enc`** are unidentified. A Shannon-entropy
  probe over the first block separates ciphertext (near 8 bits per byte) from
  plaintext secrets and structured data. About 20 lines. False positives:
  compressed or media data also scores high, so it can only say "plausible
  ciphertext", never "clean".

### Images beyond what G3 reads

- **Residual:** TIFF (1) and ICO/ICNS (5) have metadata no walker reads; the
  pixels of every image are unread. A screenshot of a statement is the
  historic case G3 was built for, and the entry's reason is the human attesting
  to it.
- **Measured (crude probes):** 191 of 287 `.jpg` files show an Exif or APP1
  segment marker, 185 of them with bytes consistent with a GPS pointer, 7 an
  XMP packet. These are already walked and blocked unless kept by a named,
  reasoned set. 10 PNGs carry text chunks, 3 `eXIf`. The probes over-count (a
  marker byte pair occurs by chance), so read them as an upper bound that says
  location metadata is common in this population, not as a count of leaks.
- **Cost of more:** OCR needs a third-party engine and is out of reach under the
  zero-dependency rule. A TIFF walker is a modest extension of the existing
  one for one file. Low value.

### Fonts, icons, Mach-O, audio, CAD, 3D, script bundles: 22 files

Metadata in a font is name and licence strings; an icon carries pixels only; an
audio file may carry tags and a recording location; a compiled-script bundle
may carry source and an author. Each is 1 to 6 files in at most 3 siblings.
Not worth a reader on count alone. The strings pass would cover the strings in
them for free if it is built.

## Value ranking (by `020/240`)

Value here is the chance a breach is real, how bad it would be, and whether a
person's attestation would plausibly miss it, set against build, review and
tuning cost, and the false-positive cost that gets a guard switched off. Every
population is small and already passed a human at G3 time, so the gain is a
second line for the cases a person misreads, and for the day a child is
public.

| Rank | Read | Files it sees | Value | Cost | Why |
|---:|---|---:|---|---|---|
| 1 | OOXML text and properties | 12 | high | low | full text recoverable with no fuzzy decode; author names present in all 12; spreadsheets are where financial detail lives |
| 2 | PDF metadata slice | 27 | high | low to medium | the largest unread document population (41 MB); author or producer in 6 to 23 of 27; scanned pages mean the text layer is no help, so metadata is the part a read can see |
| 3 | Archive descent (gz, xz, zip) | 13 | medium, derivative | medium (own attack surface) | closes the hole that hides geotagged JPEGs and captures inside a zip; pays only once there are readers to descend into |
| 4 | Printable-string pass | about 20 | medium | low, high false-positive risk | covers `.doc`, captures and compiled files in one go, but needs tuning to stay quiet |
| 5 | `age` header check and entropy probe | 114 | low to medium | very low | stops plaintext in an encrypted file's name; cannot see content |
| 6 | PDF text layer | 27 | medium | high | partial recall, heavy upkeep; rule on it after rank 2 has run |
| 7 | Pixels (OCR), TIFF, fonts, icons, audio | 425 images, 22 other | low | high or third-party | OCR is blocked by the dependency rule; the rest is a few files |

Absent today, so unranked and recorded: SQLite, keystores, disk images, Git LFS.
If one appears, G3's whole-file entry is its only guard.

## Recommendation (for the principal to rule on, not a decision)

🎯 **Build the Office read first (rank 1), then the PDF metadata slice
(rank 2), as one small container-reader unit under `leakscan`'s G3 gate.**

- **Why these two.** They are the only kinds where a stdlib read sees the real
  risk (the text of a workbook; the author and producer of a document) at low
  cost and low false-positive risk. Between them they cover 39 files, 44 MB,
  and every unread personal-name field the census found in a document. They
  also share one shape: decode a bounded set of strings, run the existing
  rules, report under G3's `binary-metadata` or a sibling rule.
- **Keep the gate as it is.** A reader does not replace the whole-file entry.
  What it adds is a block for text the person who wrote the entry did not see,
  the way G3 already treats image XMP: naming a set states a need, it does not
  stop the scan.
- **Not first, and why.** Archive descent has value only once there are readers
  to descend into, and brings its own attack surface, so it follows. The strings
  pass is cheap to write and costly to keep quiet, so it follows too. The `age`
  header check is tiny and could ride along. OCR is out under the
  zero-dependency rule.
- **The alternative is a legitimate ruling.** Under `020/240` a check not built
  is a recorded decision. The case for accepting the gap is that all 633
  files passed a human at G3 time, the Office and PDF populations are 39 files
  in 2 repos, and atelier itself tracks none. The case for building is that the
  floor gives every child the guard when it lands, a child that goes public
  would turn this from a private gap into a published one, and the Office and
  PDF reads are the cheap end of the list.
- **Sizing for the ruling.** Estimated 300 to 450 lines of stdlib Python plus
  tests and a man-page paragraph, and a cold pass because it adds a rule that
  blocks (a reader that fails open reads as clean). Run against the real 39
  files before it lands, to count its false positives first.

## What this does not say

- It reads no pixels and no text layer, so it says nothing about whether any
  specific binary leaks. It counts kinds and what a kind can hold.
- The metadata probes are crude byte checks, an upper bound. A walk of the
  images with G3's own reader would give exact figures; those images are
  already walked by G3 where it is adopted, so that count was not needed here.
- Sibling counts are a snapshot of 2026-11-16. A population that grows (the
  JPEGs are the likeliest) changes the ranking only for images.
