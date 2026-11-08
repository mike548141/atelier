# tools/ — atelier's mechanical controls

<!-- indexscan:maps dir=. match=*.py exclude=test_*.py -->
<!-- indexscan:allow: allowmarker.py its catalogue entry is owed as AM5 (the shared allow-marker grammar cold pass), open on that review's checklist; this marker goes stale and is reported the day the entry lands. Added 2026-10-05 by session 5e3f68f1 (agent, queue run 200/010) -->

Doctrine informs; a *check* enforces. These are the checks. Zero third-party
dependencies — run them with the system `python3`.

**A scanner's `--selftest` prints one verdict line and nothing else**
(`320/690`). It proves the engine against deliberate fixtures, whose findings
are not the floor's: a passing run prints `selftest OK — <scanner>`, a failing
one prints `selftest FAILED — <scanner>` and then what it captured, each line
prefixed `selftest (<scanner>):`. So a CI log never holds a fixture's
`✗ <scanner>: N finding(s)` beside a real one.

## What these scans cannot see (read this before trusting a clean run)

A clean scan means **"no known shape matched"**, not "safe to publish". Per
EVIDENCE §14, an instrument states what it dropped — this is the triad's
standing residual, the classes each scan *structurally* cannot catch:

- **All three** scan line-by-line and text-only: anything **split across
  lines** (a concatenated secret, a PEM body pasted without its header, a
  folded YAML scalar) and anything inside a **binary container** (docx, PDF,
  sqlite, images — skipped silently on the first NUL byte) is invisible.
- **leakscan** matches literal terms and NZ-tuned structural shapes: a
  **paraphrased** personal fact ("the dog", "the house we bought last year"),
  a term not on the machine-local list, or a non-NZ address/phone shape sails
  through. The term list is only as good as its curation.
- **secretscan** no longer trades single-case hex away entirely — since E6b
  (2026-08-06) a **hex-encoded token outside a secret-named assignment** is
  REPORTED as an advisory finding rather than passing in silence. It still does
  not *block* on one, so the residual is now about response rather than
  blindness. Still uncaught in either tier: a novel vendor format that is
  neither assignment-anchored nor high-entropy-mixed-class, a literal secret
  that *begins* like an indirection (`$uperS3cret…` reads as `$VAR`), and a
  context-free credential shorter than 32 characters.
- **licenscan** sees SPDX-tagged headers and metadata declarations only: a
  vendored file carrying the **traditional prose licence header** with no
  `SPDX-License-Identifier` tag — the commonest real-world copyleft shape — is
  invisible. Dual-licence (`A OR B`) and `LicenseRef-` ids degrade to an
  *unknown-declaration* warn (friction, never a silent pass). A legitimately
  bundled copyleft component (the NOTICE case) **will block**; the
  allow-marker/ignore hatch, reason recorded, is the sanctioned way to say
  "bundled, not relicensed".

**conflictscan** is anchored-line-based, so a conflict marker without its own
line — one folded mid-paragraph, or split by a hard line-wrap — is invisible,
same residual as the triad above. Its `--staged` (hook) mode reads only the
**added lines** of the staged diff, matching `secretscan`'s/`leakscan`'s own
hot-path shape: a marker that predates this scanner's adoption, or one that
enters a file by some route other than `git commit` on this machine, is not
in that diff and is caught only by the CI plane's whole-tree pass.

**linkscan** (a doc-integrity check, not a leak scan) is line-based too: it reads
inline `[text](path)` links and Markdown (ATX `#` + setext underline) headings
only. **Reference-style links** (`[text][ref]` + a `[ref]: …` definition), links
inside raw **HTML**, and a link whose `](…)` **spans two lines** are invisible to
it — as is any anchor slug where atelier's simplified slugger diverges from
GitHub's full CommonMark render (an exotic heading). Anchors minted by raw HTML
(`<a id=…>`, `<h2>`) aren't seen either, so a valid link into one **false
positives** (one `linkscan:allow` fixes it); the same goes for a link-shaped
example inside an **indented (4-space) code block**, which linkscan reads as
live text (GitHub renders it as code — fixing that would risk missing real
links in indented list items, the worse trade). It never touches the network,
so it says nothing about whether an external URL is alive.

Where the replacement path is **computable**, linkscan prints it (`↳ did you
mean: ../../tools/x.py`). Two cases qualify, both requiring a *unique* answer:
the path resolves from the **repository root** — the commonest break by far, a
root-relative path written inside a file two levels down — or exactly **one**
file in the tree carries that basename, the moved-or-renamed case. Two
candidates means guessing which, so it stays silent; a confident wrong
suggestion costs more than none. Suggestions are **advisory text only**: they
never change a verdict or an exit code, and nothing is rewritten for you.

**sizescan** (a hygiene check, not a safety scan) gates on **relocatable cold
content** — a completed `[x]` item on a checkbox-worklog file, whose fix is a
lossless move to the history store — and on live state in an archive store. It
has **no size check**: a file is never reported for its length (Mike's ruling,
2026-10-05; the old length advisory was removed 2026-10-16). Cost is
size × read-frequency, so the enemy is cold content sitting on the hot path,
never fulsomeness: a roadmap that is long purely from a genuine list of *open*
items is not mentioned at all. The judgement of whether a long all-open file is
hiding resolved narrative stays human, caught at review.

**board** (a records-hygiene check, board-store ADR 2026-08-15) guards the one
derived file the split board keeps: `ROADMAP.md` is generated from the per-item
files under `docs/roadmap/`, and a commit whose index is stale against them
fails with the remedy printed (`board.py rebuild`; after a merge conflict on
the index, rebuilding *is* the resolution). CI checks the worktree against
itself — a CI checkout has no staged-vs-unstaged distinction to get wrong, the
checkout already *is* the committed tree. The hook checks the **staged plane**
instead (`--staged`; harvestscan's HV4 shape, reused rather than reinvented):
it builds the wanted index from the item files as staged (`git show :path`)
and compares it against `ROADMAP.md` as staged, so it answers "does what's
about to be committed already agree with itself" — never "does the working
directory agree with itself", which is the weaker question the hook used to
ask and which let two slips through unnoticed until CI (BS1, 2026-08-15): an
index rebuilt on disk but never `git add`ed, and a rebuild that read a
**sibling's** dirty, unstaged item edit straight off the worktree and baked it
into the committed index. `rebuild --from-index` is the matching write-side
fix — it regenerates from the same staged plane, so a claimer at a dirty
primary checkout (`CONCURRENCY.md` § Claiming work) never absorbs a sibling's
unstaged line into the file they are about to stage; it is the remedy the
hook now prints on a staged-plane failure. Done items render `✅` in the index
— never `[x]`, so sizescan's cold-content gate cannot fire on a generated line.
A repo with no `docs/roadmap/` directory (worktree plane) or none tracked in
the index (staged plane) is out of scope and passes saying so.
Every string the generator writes into the index has to be true in a repo that
is **not** this one — children call the floor's tools and never vendor them, so
the rebuild instruction is resolved per root (repo-relative here, the hook's
`$ATELIER_TOOLS` spelling in a child, never an absolute path) and the banner
names no path at all. Remaining stated residual: the index cannot pass a
repo-wide `wrapscan` — its item lines are markdown links that cannot be
wrapped without ceasing to be links — so a child either scopes `wrapscan` off
the index or waits on the generated-file exemption question (board item
`010/070`, unruled).

Each index line is projected from the item's **logical first paragraph** (board
`010/170`): the state line plus the indented lines that continue it, up to a
blank line, an unindented line or a line that opens a new block. A bold title
that wraps renders whole and a `(claimed …)` fragment wrapped onto line two
shows; flags still read the state line alone, and a code span is read across the
joined paragraph, so an odd backtick pairs with one on a later line. **Until
2026-11-18 (UTC)** `--check` also accepts an index in the previous first-line
form. It prints a ⚠️ notice, and a `board advisory: 1 finding(s)` line that
`floor.py` shows as `🟡 board` on its summary, so the notice survives a green
run. From that date the old form is stale like any other mismatch. The date is
firm and no flag moves it; the removal list is the `LEGACY` comment in
`board.py`.

**reviewscan** (a records-hygiene check) proves only **presence**: a decision
record carries *a* review line. Whether "not warranted" was the honest call —
or a queued pointer was ever taken — is exactly the judgement a validator
can't make; the review practice owns it. Roadmap sections aren't scanned at
all (deliberate — see the tool's docstring), so a design entry there rests on
convention alone.

**publishscan** judges the **path, never the contents** — the one scanner here
that does. It cannot tell you a tracked `.env` is empty or a tracked allowlist
is harmless; it says the file should not be in the repo at all. It is a
denylist, so it knows only the shapes it was taught, and it deliberately
*allows* the guard declarations (`.atelier-floor.json`, the `.<scanner>ignore`
files) that also map where the defences are weak — they must travel for the
floor to run, so that exposure is accepted and mitigated by requiring a stated
reason for every exemption, not by hiding the files.

The scans are the mechanical floor, not the whole boundary: the human
pre-publish scrub (and the review practice) owns the residual above.

## `--root` and path arguments — one root, and it means one thing

Almost every scan takes `--root <repo>` plus an optional list of paths. **A
relative path argument resolves against `--root`, never against your current
directory** (since 2026-08-23, roadmap `010/110`). So from atelier:

```sh
python3 tools/wrapscan.py --root ~/code/child docs/method   # child's docs
python3 tools/wrapscan.py --root ~/code/child               # the whole child
```

Before that fix the target resolved against **cwd** while everything else the
run depends on — the `.<scanner>ignore` lookup, the repo-relative anchors, the
`docs/` default — resolved against `--root`, so the run read one repo's file
under another repo's rules and said nothing about it. That shape lost a child
session a full round of readings. Two consequences worth knowing:

- **`--root repo repo` now means `repo/repo`** and exits 2. Say `--root repo`
  (or `--root repo .`) instead. Exiting loudly on a path that is not there is
  the design — a scan covering nothing must never read as a clean pass.
- **An absolute target is taken as given**, `--root` or not. Naming a path in
  full is an explicit act; only the silent mis-resolution was the defect.

## Supply chain — zero-dep *is* the control, and its residual

These tools take **zero third-party dependencies** (stdlib Python, and Node's
built-in `node:test` for `instruments/`), and that is a deliberate
**supply-chain control**, not merely a convenience: a dependency you do not have
is a dependency that cannot ship a vulnerability into the build
(`method/PRINCIPLES.md` §8, *design out the work* — depending on nothing designs
out the whole class of dependency-vulnerability screening). It is the reason this
repo runs no SCA scanner, no Dependabot, no lockfile audit: there is almost
nothing to screen. **"Almost"** is the honest word — the control shrinks the
surface to near-zero, it does not zero it, and the residual is named here rather
than pretended away:

- **CI actions are SHA-pinned, not tag-pinned.** The floor and CI workflows
  consume a few third-party GitHub Actions (`actions/checkout`,
  `actions/setup-python`, `actions/setup-node`). A version *tag* (`@v5`) is
  mutable — its owner can repoint it at new code — so every such action is pinned
  to a **full commit SHA** with the tag kept as a trailing comment
  (`@<sha> # v5`), in `.github/workflows/ci.yml` and in the child
  `docs/build/templates/workflows/` a child copies. A pin is bumped
  deliberately, re-resolving the SHA (`gh api repos/<owner>/<repo>/git/ref/tags/<tag>`
  — checking `.object.type` first: an **annotated** tag returns a *tag object*,
  not a commit, so dereference it
  (`gh api repos/<owner>/<repo>/git/tags/<sha> --jq .object.sha`, or
  `git ls-remote --tags <url> '<tag>^{}'`) before pinning;
  a moved tag can no longer ship code into a trusted build silently. (Grounded:
  the 2026-07-22 security-canon gap map; SC3, 2026-07-23.)
- **The toolchain is a trusted, unpinned dependency — stated, not hidden.** The
  scanners still trust the runner's `python3`, `node`, `git`, and `gh`, the OS,
  and the runner image itself. These are dependencies even though no manifest
  lists them; the floor pins the *actions* but not the interpreter builds
  (`setup-python`/`setup-node` request a version line, not a SHA of the
  toolchain). That is an accepted residual for a zero-dep doctrine repo, named
  here so it is a known limit rather than an invisible one.
- **No SBOM / artefact signing yet — deferred with a stated trigger.** There is
  no software bill of materials at rest and no release-artefact signing; both are
  deferred to the first published *artefact* (`method/SIGNING.md`, layer 2 — the
  trigger is a package or binary someone else installs). Until an artefact
  exists there is nothing to bill or sign, and standing the machinery up would be
  ceremony.
- **Scanner distribution to children is decided — fetch at CI.** A child's CI
  floor checks atelier out beside the repo and runs these scanners from that
  checkout (`docs/build/templates/workflows/floor.yml` — one source, no
  vendored copy); the per-clone hook covers the local clone. (SC2 sweep,
  2026-07-23 — the earlier "deferred call" wording predated floor.yml.)
- **Child CI trusts `atelier@main` for scanner code — by design.** The floor
  template fetches the scanners at floating `main` (newest detection is
  safest — rationale in floor.yml's header) while the *trust list* and
  doctrine are read at the child's pinned SHA. Detection floats, trust roots
  pin — the asymmetry is deliberate, named here where the residuals live
  (SC5, 2026-07-23). Stated at strength: the float is also a standing grant —
  a write to atelier's `main` runs code in every child's floor job, bounded
  by the job's `contents: read` permissions and no step secrets; a child
  wanting the opposite trade pins `ref:` exactly as the trust list pins
  (SCA1, 2026-07-23).

## `leakscan.py` — catch the shape of personal/estate data before it is committed

A repo holds personal data only for a purpose, with every exception recorded
(`docs/build/REPO-STANDARD.md` § Personal data); a public repo holds only a
closed list its principal has granted (atelier's is `docs/PERSONAL-DATA.md`).
`leakscan` is the machine behind that rule, so a leak fails the commit instead of
reaching the remote. It reads shapes and listed terms, not purpose, and an
allow-marker on a line is not a grant of an exception.

### Two layers (why the scanner itself leaks nothing)

| Layer | Where it lives | What it catches |
|---|---|---|
| **Structural patterns** | in `leakscan.py` (shareable) | the *shape* of sensitive data — emails, IPv4/IPv6, MACs, private-key headers, AWS keys, JWTs, NZ address/phone shapes, coordinates. Names no real value. **Always runs.** |
| **Literal terms** | `~/.claude/leakscan-terms.txt` (**machine-local, never in a repo**) | the actual names, addresses, medications, device IDs, deal figures of one estate. This list *is* the leak if committed, so it stays outside every repo. |

If no local list is found, the scan runs structural-only and **says so loudly** —
partial cover, never silently weaker. For automation that only reads exit codes,
loud isn't enough: pass **`--require-terms`** on a hook/CI line that *expects*
full cover and the scan fails closed (exit 2) when the list is absent, instead
of reporting a degraded pass a script can't tell from a full one.

### Usage

```sh
python3 tools/leakscan.py                 # scan the whole repo
python3 tools/leakscan.py --staged        # scan only staged additions (the hook)
python3 tools/leakscan.py path/to/file    # scan specific paths
python3 tools/leakscan.py --json          # machine-readable, for CI/composition
python3 tools/leakscan.py --binary-entries  # print .leakscanbinaries lines to review (G3)
python3 tools/leakscan.py --selftest      # prove the engine on this box
```

Exit codes follow the shared contract (`report.py`, below): `0` includes report-only
findings, and `1` blocks the commit.

### Rules that are off report, and never block (115/090)

A rule that is off still runs. Its hits are listed in a `🟡 REPORT-ONLY
FINDINGS` block, counted on a line printed on every run, zero included
(`leakscan advisory: N finding(s) — reported, not blocking.`), and carried on
the floor board as `🟡 leakscan enforced`. None of them moves the exit code.
Two kinds of rule are off:

- **A rule a repo turns off** with `--disable` (in a child, the `flags` entry
  in `.atelier-floor.json`). Before this, its hits were dropped unseen.
- **A withdrawn rule**, taken out of the blocking set for noise:
  `diagnosis-key`, the diagnosis/diagnoses key G1 tried and withdrew. It has
  no blocking form, so `--disable` refuses its name.

Nothing that blocks stops blocking: no rule that blocked is demoted, and
`test_leakscan.BlockingSetPinned` pins every one. This narrows the EI6 ruling
(leakscan gains no advisory form) for rules that are off only, on Mike's
answer of 2026-10-16 (`SECRETS.md` § *The boundary's posture*). An allow-marker
or a `.leakscanignore` glob exempts a report-only hit as it does a blocking
one. `--json` keeps `clean` and `findings` for blocking findings, as before,
and adds `blocked`, `counts` and `advisory`. Design and residuals:
`leakscan.off-rules.design.md`.

### The local term list

Point the scanner at your literal terms one of three ways (first that exists
wins): `--terms <path>`, `$ATELIER_LEAKSCAN_TERMS`, or the default
`~/.claude/leakscan-terms.txt`. Format — one per line, `#` comments, blank lines
ignored:

```
# literal, matched case-insensitively on whole words
Some Person
23 Example Road                     # leakscan:allow: doc example
# a raw pattern for families of identifiers
regex:ACME-\d{4}
```

See `leakscan-terms.example.txt` for a fuller template. **Never commit your real
list** — it belongs in `~/.claude/`, which travels with you, not with any repo.

### Exempting a false positive

A leak-scanner over-flags on purpose (a false positive costs a comment; a false
negative costs a leak). Two escape hatches, both visible and greppable:

- **Per line** — append `# leakscan:allow: <reason>` (or `<!-- leakscan:allow:
  … -->` in Markdown) to the offending line.
- **Per path** — add a glob to `.leakscanignore` at the repo root. Keep it short;
  every entry is a hole in the boundary.

A binary file has its own hatch, below. It can't carry a line marker, and a
glob is the wrong tool for it.

### Binary files (G3): blocked until a person has looked

leakscan can't read the body of a binary file: the pixels of an image, a
PDF, an archive, a font. Until G3 it skipped them in silence. Now a **tracked**
binary blocks (Mike ruled this 2026-08-04, funded 2026-08-09). It passes once
a reasoned entry in **`.leakscanbinaries`** at the repo root accepts its exact
bytes, and a reasoned line keeps each metadata set it carries:

```
# Project logo and a docs diagram, drawn for this repo. Looked at: no
# people, screenshots or personal data.
3f1c9a0d5e7b2a64  docs/img/logo.png
9b04e6d1c2a8f357  docs/img/flow.webp

c81d07a2e4f9b613  docs/img/site.jpg  # our own photo of the product; looked at
c81d07a2e4f9b613:icc  docs/img/site.jpg  # keeps the brand colours true on wide-gamut screens
```

- **Format.** A file line is the first 16 or more hex characters of the
  file's SHA-256, then the repo-relative path. A set line is the same digest,
  `:<scope>`, then the path; the scope names the sets and fields it keeps
  (below). The reason uses the same grammar
  as `.leakscanignore` (`allowmarker.read_reasoned_parts`): a comment stanza
  above the line, or a trailing `# reason`. A line with no reason is a config
  error (exit 2). So is a malformed line, an unknown set, a path or set listed
  twice, a path that is absolute or climbs out with `..` (it could match no
  file, so it would sit in the inventory doing nothing), and a set line with
  no file line or a different digest. A path can't contain `#`.
- **Who allowed it, and when.** Mike, 2026-10-03, on every exception: it is
  to be *"recorded so that its clear that the exception exists, why it is
  necessary, who created it (e.g. session transcript ID, did I rule or did
  you do it automatically etc), when the exception was granted"*, and on
  2026-11-08 he answered that each manifest line records who and when, not a
  reason alone. So each line's comment, trailing or in its stanza, also
  carries `by=<principal-ruled|principal-answer|agent> session=<id|human>
  on=<YYYY-MM-DD>`. `principal-ruled` is his own words, `principal-answer` a
  pick he made from a session's options, `agent` a session's own judgement; the
  session is the transcript id (`$CLAUDE_CODE_SESSION_ID`) or `human`. These
  are not a reason: a line that holds only them is still unreasoned, and a
  stanza of them over lines needing their own reason still counts as one
  blanket. A `by=` that doesn't read as the whole form, an unknown kind or a
  bad date is a config error, never a quiet pass. `--binary-entries` prints
  the note on every line (`by=agent` with the session id inside a Claude
  session; `by=CHOOSE` otherwise, which is refused until a person picks).
  **A line written before this, with a reason and no who/when, still loads and
  prints a warning that names its line and never blocks.** No date turns that
  warning into a block: whether and when it should is Mike's to rule. It is the
  minimum his answer needed; the held exception register (`110/100`) would
  carry the same three fields as `file` entries.
- **One-time, because the entry is tied to the hash.** If the file changes it
  blocks again as `binary-changed`, and whoever re-lists it is looking at the
  new bytes. 16 hex characters (64 bits) is the printed form because
  secretscan's entropy net reports every 32+ character run as advisory, which
  would add one advisory per listed binary. A full 64-character digest also
  parses (sha256sum's ` *path` binary-mode form too).
- **Metadata, set by set.** Read for PNG, JPEG and WebP using only the
  standard library, with every read size-capped. Each segment found belongs to
  one named set:

  | Set | What it is |
  |---|---|
  | `exif` | Exif (camera, time, place): PNG `eXIf`, JPEG APP1 Exif, WebP `EXIF`, ImageMagick's raw exif profile |
  | `iptc` | IPTC / Photoshop resources: JPEG APP13, ImageMagick's raw iptc/8bim profile |
  | `xmp` | XMP packet: JPEG APP1 (and extended), WebP `XMP `, PNG `XML:com.adobe.xmp` |
  | `icc` | ICC colour profile: PNG `iCCP`, JPEG APP2 `ICC_PROFILE`, WebP `ICCP` |
  | `png-text` | PNG `tEXt`/`zTXt`/`iTXt` text chunks other than XMP |
  | `jpeg-comment` | JPEG `COM` segments |
  | `unknown` | what the walker can't identify or read: an unrecognised APP1, a segment over the 1 MiB cap or undecodable, a structure it can't walk |

  Mike, 2026-10-18: *"that reason for the image metadata must be specific to
  the sets of metadata it wants to keep. It should only keep the metadata it
  has a need for"*. And, 2026-10-19: *"I am fine with one reason applying
  to multiple fields of metadata, but it should be specific e.g. fields A,
  B, and C allowed because of X"*. These sets are **data types** (Exif, XMP,
  and so on), not the fields he meant; the field-level keep he asked for, GPS
  versus the camera model, is the next bullet (`020/450`). So every set present
  in the file blocks as `binary-metadata`, naming the set, until a line names it. One line may
  name one set (`<digest>:icc  path`) or several (`<digest>:icc,xmp  path`)
  under one reason, the need for exactly those sets. There is no wildcard.
  Keeping `icc` never keeps the `exif` beside it. A set line's reason may not
  repeat the file line's own reason, so one comment over a file and its sets
  (a blanket) does not load. Strip
  what you don't need (for example `exiftool -all= file`, or
  `exiftool -all= -tagsfromfile @ -icc_profile file` to keep only the colour
  profile). A set line for a set the file doesn't carry is stale and blocks:
  the hash binds the bytes, so the line was wrong when it was written.
- **Fields, for Exif, GPS, IPTC, XMP and PNG text.** Mike, 2026-10-19: *"I did mean fields as in
  GPS versus the camera model. Things like exif, iptc, xmp are data types,
  nto fields"*. So each of these blocks is read field by field (names only,
  never the values), and a line keeps named fields, not the whole set:

  ```
  c81d07a2e4f9b613:exif:Make,Model,LensModel  docs/img/site.jpg  # the shop shows which camera
  c81d07a2e4f9b613:gps:GPSLatitude,GPSLongitude  docs/img/site.jpg  # the venue pin on the map
  ```

  A field is `exif:<TagName>` or `gps:<TagName>`, with the tag names of the
  Exif / TIFF / GPS specifications (`exif:Model`, `exif:DateTimeOriginal`,
  `gps:GPSLatitude`). After one `set:Field`, bare names continue the same
  set, so `exif:Make,Model` keeps two fields. One reason may cover several
  fields, so long as the line lists each. Rules: no wildcard; `gps` alone is
  refused, because it would keep every GPS tag under a reason that names none
  (list them); a name that is not a real tag is refused as a typo; a tag the
  table does not name is written by its number, `exif:0x9999`; and a set and
  its own fields (`exif` with `exif:Model`) cannot both be named. Any field
  present and not named blocks as `binary-metadata`, naming it. A field the
  file lacks is a stale line. A block the reader cannot walk (a short header,
  an offset outside the block, more than 16 directories) is the field
  `exif:unknown`, which blocks until it is named. `MakerNote` is one field:
  naming it keeps the camera maker's whole opaque block, so say so in the
  reason.

  The other three sets follow the same rules, and each has an `unknown` field
  for what the reader cannot walk, which blocks until it is named:

  ```
  c81d07a2e4f9b613:iptc:By-line,Credit  photo.jpg  # the credit line the licence needs
  c81d07a2e4f9b613:xmp:dc:creator,xmp:dc:rights  photo.jpg  # same, in the XMP copy
  c81d07a2e4f9b613:png-text:Author,Creation%20Time  chart.png  # the tool's own stamp
  ```

  - **IPTC**: `iptc:<dataset>`, the IPTC IIM names of the Photoshop 8BIM
    resource 0x0404 (`iptc:By-line`, `iptc:City`, `iptc:Caption-Abstract`). A
    dataset the table does not name is `iptc:<record>:<number>`
    (`iptc:2:250`); another Photoshop resource in the same APP13 is
    `iptc:8BIM-0x03ED`. Bare `2:090` continues the same set; names are
    case-sensitive.
  - **XMP**: `xmp:<prefix>:<Property>` (`xmp:dc:creator`,
    `xmp:exif:GPSLatitude`), one field per top-level property of the packet's
    `rdf:Description` elements, attribute or element form. A property's value,
    structure included, is one field. Well-known namespaces use their usual
    prefix whatever the packet declares; another uses the prefix it declares.
    Write every XMP field in full: `xmp:dc:creator,xmp:dc:rights`, not
    `xmp:dc:creator,dc:rights` (a prefix could be a set's name, and
    `xmp:dc:creator,exif:Make` keeps the Exif field `Make`). A packet with a
    DOCTYPE or entity, an element outside the xmpmeta / RDF / Description
    skeleton, a property with no prefix, or over 1,024 properties is
    `xmp:unknown`. JPEG extended XMP is joined before it is read.
  - **PNG text**: `png-text:<keyword>` for a tEXt, zTXt or iTXt chunk (XMP in
    iTXt is XMP). A byte outside `A-Z a-z 0-9 _ . -` is written `%XX`, so
    `Creation Time` is `png-text:Creation%20Time`. A keyword that is itself
    `unknown` is `png-text:%75nknown`; an empty or over-long keyword is
    `png-text:unknown`.

  A set with over 1,024 distinct fields adds `<set>:unknown`. JPEG comments
  and ICC profiles have no fields to name and stay kept by set.
- **Type-level lines, accepted with a warning until 2026-12-18.** A line
  written before fields were read (`<digest>:exif  path`, or `:iptc`, `:xmp`,
  `:png-text`) keeps the whole set, GPS included for Exif. Until
  `TYPE_LEVEL_UNTIL` (2026-12-18, UTC) it still does, and each scan prints a
  warning that names the fields the file carries and asks for field-level
  lines. From that day it keeps nothing: the set blocks as `binary-metadata`
  until fields are named. A month after the grace ends, so a child that listed
  by type before 2026-11-18 has until 2026-12-18 to move to field-level lines.
  `icc`, `jpeg-comment` and `unknown` have no fields and are unaffected. Like
  the grace, no flag or setting moves the date.
- **Text sets are still scanned.** `png-text`, `xmp` and `jpeg-comment` are
  decoded and run through the normal rules and term list, kept or not.
  Keeping a set states a need; it doesn't stop the scan. Allow-markers
  inside metadata are ignored, because nobody reviews text hidden in a
  binary. That includes XMP in ImageMagick's `Raw profile type xmp` PNG chunk,
  which is a hex dump of the packet: it is decoded and scanned like XMP in a
  JPEG or WebP. A raw `exif`, `iptc` or `xmp` profile that doesn't decode is
  reported as **UNREADABLE** and blocks as `<set>:unknown`; it is never
  clean.
- **What it can't see.** The pixels: no OCR, so the reason *is* the human
  check. Metadata in any other format (GIF, TIFF, HEIC/AVIF, PDF, Office files,
  fonts, archives), where the file line accepts the whole file, metadata
  included. Two guards are weaker than they may read: a set line's reason may
  not repeat the file line's, but that is textual equality, so a one-character
  difference loads, and whether a reason is specific stays the person's call;
  and the JPEG walker's cost is linear in a run of degenerate markers (a
  million RST markers took 0.5 s), bounded by the file's size and not
  budgeted. The values of Exif and IPTC fields, which are named and never read
  (the human who writes the reason reads them in the file); XMP and PNG text
  values are matched by the text rules, which do not understand them. The
  contents of an ICC block, which are named by presence and never read. JPEG segments after the first start-of-scan, JPEG
  APPn segments other than APP1, APP2 (ICC) and APP13, and bytes after a
  format's end marker.
- **Which files are gated.** In a git work tree, a whole-tree scan gates the
  files `git ls-files` lists. It counts untracked binaries such as `.DS_Store`
  as "not gated" in the summary. Outside git, every binary is gated. The
  staged hook gates every binary the commit adds, modifies or renames. It reads
  the index copy, not the working tree, and so does it read
  `.leakscanbinaries`: the manifest the commit holds, and none when the commit
  holds none, whatever the working copy says (it prints a note when the two
  differ, so a hook and CI cannot disagree about the same commit). It also now path-scans the names of
  binaries, empty new files and pure renames, which the added-lines diff never
  showed. A file git marks `binary` that is really text is read in full.
- **Deleted or renamed.** An entry that accepts nothing blocks as
  `binary-stale-entry`. That covers a file that's gone, untracked, read as
  text, or removed or renamed by the staged commit. A renamed file's finding
  names its old entry ("same bytes as the entry for …"), so the fix is
  re-pathing its lines.
- **`.leakscanignore` does not skip the gate.** For a binary the gate runs
  *before* the ignore file (Mike's answer, 2026-11-08): a glob is path-wide
  and blind to content, so it can't be the hatch for an image, and a reasoned
  `docs/img/` glob would otherwise pass every present and future image unread.
  A tracked binary under a glob is gated like any other and needs its
  hash-bound entry; the glob still skips text, and still skips an untracked
  file. `--disable` can't turn the gate off, because the binary rules aren't
  structural rules. Every accepted binary is counted in the `suppressed:`
  line.

**The adoption grace, until 2026-11-18, and it is firm.** On roadmap `020/150`
(2026-10-18) Mike chose, through the decision device, the option labelled
*"Grace period (Recommended)"*. The option's own text was the queue run's, not
his words: *unlisted files print a warning naming a cut-off date (~30 days),
then start blocking; no child goes red today; each lists its files when
convenient*. So until `BINARY_GRACE_UNTIL` (2026-11-18, UTC) the four gate
findings, `binary-unlisted`, `binary-changed`, `binary-metadata` and
`binary-stale-entry`, print as warnings. Each names the date and its remedy,
and none fails the exit code. From that date they block exactly as above.
The day was the queue run's pick on "~30 days"; Mike made it firm on
2026-11-08 (*"Firm; queue fixes now"*): **2026-11-18 stands for every child.**
Each child that would fail gets an item on its own board to strip or list
before then, and a child not worked by the date goes red until it is. In
`GUARDS.md`'s terms it is a mandate, not a default: a child may list or strip
earlier, or argue an exemption through its parent, and none can move the
date. Nothing else is graced: every other rule, including a hit in an image's
text metadata, blocks today. This is the one exception to leakscan having no
advisory form for a rule that blocks (E6a; rules that are off report, above).
It is dated and has no flag, env var or config key, so nothing can move it.
floor.py refuses any `flags` argument that is, or abbreviates, a mode flag
(`--binary-entries`, `--selftest`, `--warn`, `--json`, `--check`) or one that
re-aims the check (`--root`, `--terms`, `--staged`), and any `scope` path
starting with `-`. Those were the only *unrecorded* ways to skip the gate: a
reasoned floor `scope` that leaves a tree out is still on the record, and
declared, not quiet. (A `.leakscanignore` glob used to be a second one; it no
longer is, above.) leakscan's floor entry still has no advisory form.

**Adopting it: one commit, before the cut-off.**

```sh
python3 <atelier>/tools/leakscan.py --root . --binary-entries   # prints the lines
```

`--binary-entries` prints a file line for every tracked binary that no entry
accepts yet (new, or changed since listed), and one `<digest>:<set>` line for
each metadata set it carries that no line keeps, or one `<digest>:<set>:<Field>`
line for each Exif, GPS, IPTC, XMP or PNG text field. A type-level line on one
of those sets is listed again as its field lines, with a note that it is replaced. Merge the fields that share
one need into one line. Each line ends with the who/when note
(`# by=… session=… on=…`, above). It writes **no reason**, and
the scan refuses the lines until a person adds one. Its notes go to stderr:
which entries replace a changed line, and which sets each file carries. Look
at each file. Strip every set you have no need for, then re-run, because
stripping changes the bytes. Append the lines with a true reason per file and
a need-specific reason per set kept, and commit.

### Networking repos & scanning a subtree

A networking codebase is *full* of IPs and MACs by nature — scanning it whole
buries the real signal (leaked names, addresses, subnets) under thousands of
legitimate structural hits. Two levers handle this:

- **`--disable ipv4,ipv6,mac-address`** stops the network-shape rules blocking
  while keeping the PII/secret catches (email, address, coordinates, private
  keys, AWS keys) and *all* local-term matching blocking. Their hits still
  report, counted and listed, without blocking (115/090). Unknown rule names
  are a usage error.
- **Positional paths in `--staged` mode** restrict the scan to a subtree — so a
  mostly-private repo can guard only its shareable part. `leakscan --staged
  tiki/` scans only staged additions under `tiki/`; the private inventory/secrets
  are left alone (they hold real data by design).

Together they give the pattern for a private repo with an open-sourceable
subtree — scan the new lines of that subtree only, minus the network noise:

```sh
leakscan --staged --disable ipv4,ipv6,mac-address tiki/
```

### Wiring it in

- **Pre-commit hook** — copy `tools/pre-commit.sample` to
  `.git/hooks/pre-commit` (`chmod +x`). It names no scanner (ADR 0008): it hands
  the commit to `floor.py`, which runs the registry's checks (`secretscan` and
  `leakscan` over the staged diff, `linkscan` over the **whole tree**, and the
  rest) and aborts the commit on any finding. This is the primary control.
  (linkscan is whole-tree, not staged, on purpose: a link breaks when a
  *different* file is renamed or deleted, so the file that goes stale is usually
  not the one in your diff — see `linkscan.py` below.) To scope a check to a
  subtree (a networking repo, a private repo with a shareable `tiki/`), declare
  it in the repo's `.atelier-floor.json`, never in the hook: `"scope":
  {"leakscan": {"paths": ["tiki/"], "why": "..."}}`, and `flags` for
  `--disable`. The floor renders the paths as the guard's staged positionals.
  A staged positional is a repo-root-relative path in git's own spelling and
  case: the guard lets git say what it names and exits 2 for one git does not
  know (a typo, `Docs` for `docs`), never a clean pass over nothing.
  - **In a repo that doesn't carry the scanners** (any create-repo child — the
    scanners live only here), point the hook up:
    `git config hooks.atelierTools <atelier-path>/tools` (or `ATELIER_TOOLS`
    env, which wins). The hook **fails closed**: if a scanner it's asked to run
    can't be resolved, the commit is *blocked with an explanation*, never
    silently skipped — the pre-fix hook skipped silently and committed a planted
    secret (2026-07-10, the create-repo exercise). Contract pinned by
    `tools/test_precommit.py`.
  - **Merges.** Git does not run `pre-commit` for a clean `git merge --no-ff`;
    copy `tools/pre-merge-commit.sample` to `pre-merge-commit` beside it and the
    same checks run over the merged tree (it hands over to the sibling
    `pre-commit` and names no scanner). `cherry-pick`, `revert` and `rebase` have
    no hook that can refuse, so CI is the only plane that reads those commits
    (`docs/method/GUARDS.md` § *Which commits the hook plane reaches*).
- **CI** — in a repo that carries the scanners (atelier itself), run both with
  `--json` on every push (belt and braces; a hook only protects the clone that
  has it installed). A child repo runs the same scanners through its **CI
  floor**, which checks atelier out beside the repo and fetches them at CI
  time (`docs/build/templates/workflows/floor.yml`); the per-clone hook still
  guards local commits. (Swept 2026-07-23, SC2 — this note predated floor.yml.)

## `secretscan.py` — keep plaintext credentials out of git history

leakscan guards the *public* boundary; `secretscan` guards one that exists in
**every** repo, private ones included: a credential committed in plaintext is
burned the moment it lands in history — history is forever and a private repo can
be shared or leaked later. So this runs everywhere, and pairs with the SECRETS
doctrine's other half: **detect → rotate immediately → the burn cost is minutes.**

### Two detector classes

| Class | Catches | Confidence |
|---|---|---|
| **Named credentials** | vendor formats that are a secret by construction — private-key/PGP headers, AWS/GitHub/Slack/Google/Stripe/Anthropic/OpenAI/Twilio/SendGrid/npm tokens, JWTs, `user:pass@host` URLs | high; flags on shape alone |
| **Assigned + entropy** | a key that *names* a credential (`password`, `api_key`, `token`, `client_secret`…) assigned a long, high-entropy value that isn't a placeholder or indirection; plus a conservative context-free high-entropy net | medium; the workhorse for home-grown secrets matching no vendor format |

### Two responses (E6b, 2026-08-06)

A finding carries a **response** as well as a rule, and only one of them touches
the exit code:

| Response | Rules | Exit code |
|---|---|---|
| **block** | every named format, `assigned-secret`, and `high-entropy` — unchanged, byte for byte, from before the tier existed | `1` |
| **advisory** | `low-variety-entropy` — an unbroken 32+ character run with no credential-named key beside it (hex digests, single-case blobs) | `0` |
| **advisory** | `exempt-private-key` — real private-key material in a file a `.secretscanignore` glob skips (below) | `0` |

The blocking set never shrinks; the advisory tier is coverage that did not exist
before, opened on the path `HIGH_ENTROPY_RX`'s mixed-class requirement had shut.
An advisory finding nobody reads is cover rather than coverage, so it ships with
its consumers: the pre-commit hook prints them at the commit that would introduce
them, every CI push re-prints **all** of them tree-wide, and `floor.py`'s board
carries a `🟡 N advisory finding(s)` count read from that run's output — no state
file, so nothing to go stale and nothing to quietly vanish.

It deliberately does **not** flag the safe indirections — `!secret foo` (tiki),
`${VAR}`, `$(cmd)`, `<placeholder>` — those are the *correct* way to reference a
secret. It skips variable/attribute/call values (`password=admin_password`),
public-key material (`ssh-ed25519 …`, `public_key:`), **public-key fingerprints**
(`SHA256:…`, colon-joined hex — public by definition, matched whole-shape so a
near-miss still flags), and a token in a **published URL's scheme+host+path**
(320/290, 2026-09-18, tightened same day) — which are the dominant false
positives in real source, including hyphenated documentation links that
otherwise read as one long high-entropy run. The exclusion stops at the URL's
first `?` or `#`: a query string or fragment is exactly where a signed-URL
credential lives in practice, so it is scored as a live entropy candidate
throughout, on top of the assigned-secret rule already catching a named key
there (`?token=…`, `?api_key=…`) regardless of URL shape. A bare `http://`
glued to a real secret with no host/path shape buys no suppression either.
The report prints only a redacted
fingerprint (length + entropy), never the secret value.

### A public certificate's body (320/790)

A PEM `-----BEGIN CERTIFICATE-----` or `-----BEGIN PUBLIC KEY-----` block is a
run of base64 lines with no keyword, and a comment cannot go inside it, so
the per-line public-key rule used to exempt only the BEGIN line and flag every
body line under it. The block is now exempt from the **entropy** rule as a unit,
counted in the existing `by public-key line` field (the summary line's field set
does not change). Nothing else is widened: named and assigned rules still run on
every line of the block. It fails closed, each condition pinned by a test in
`tools/test_secretscan.py` (`PublicPemBody*`):

| Condition | Why |
|---|---|
| The label is exactly `CERTIFICATE` or `PUBLIC KEY` | a `PRIVATE KEY` block of any prefix (`RSA`, `EC`, `OPENSSH`, `ENCRYPTED`) is never covered, and its header still flags |
| The matching END line must be found, within 2048 body lines | an unclosed BEGIN suppresses nothing rather than running to end of file. 2048 lines is 96 KiB of DER at openssl's 64 characters a line, about twice the largest certificate in current use (an SLH-DSA-256f signature, about 50 KB) |
| Every line between is pure base64 (`A-Za-z0-9+/=`), at most 76 characters, on consecutive file lines | RFC 7468. One stray line (a `password=...`, a blank, a private-key header, a gap in a staged diff's line numbers) voids the **whole** block, so a half-valid block is flagged in full |
| The decoded body is one DER `SEQUENCE` that accounts for every byte and whose **first element is itself a `SEQUENCE`** | the shape a certificate (its `tbsCertificate`) and a public-key record (its `AlgorithmIdentifier`) share, and which no private-key DER form has: PKCS#8, PKCS#1 and SEC1 all open with an `INTEGER` version. So a private key's body under a certificate header (a mislabel, or an editor gluing one there) is still flagged, as is a random secret wrapped in forged headers. A check on shape from tags and lengths, stdlib only, not a certificate parse |

Each certificate in a chain is judged on its own. In `--staged` mode a diff that
only adds body lines carries no BEGIN, so the block is read from the **index
copy** of the file and a line is exempt only if that whole block is valid there;
a file with no long base64 line among its added lines never reads a blob. Not
covered, deliberately: other PEM labels (`RSA PUBLIC KEY`, `CERTIFICATE REQUEST`,
`TRUSTED CERTIFICATE`) and a certificate escaped inside a one-line string.

### What an exemption still checks (115/380)

A glob in `.secretscanignore` skips a file for every rule. The scanners' own
test files are skipped on the stated ground that their fixtures are fictional,
and nothing held them to it: on 2026-11-06 a worker put four working private
keys into `tools/test_secretscan.py`, every check passed, and only a human read
caught it. So an exempt file keeps **one** narrow check, for what "fictional"
is meant to exclude: real private-key material. Every other rule stays skipped,
so a reasoned glob works as it always did.

It is **advisory**: a hit is reported and counted in the `secretscan advisory:`
line (so `floor.py`'s board carries it), and the exit code does not move. A
later item may make it blocking once the estate reads clean. The summary line
keeps its field set; `N file(s) by .secretscanignore` still counts the files
skipped, and a hit is a finding, not a new counter. `--disable
exempt-private-key` turns it off, and then the exempt file is not read at all.

Two shapes, both judged on the **decoded bytes**, so a fictional header, a
placeholder body, a certificate or a public key cannot trip it:

| Shape | A hit when |
|---|---|
| A PEM block | any `-----BEGIN ... PRIVATE KEY-----` label, a body of pure base64 on consecutive lines (raw, or quoted fragments), and the decoded bytes are a private key's DER outline. `OPENSSH PRIVATE KEY` needs a body that opens `openssh-key-v1\0`; `ENCRYPTED PRIVATE KEY` needs the encrypted PKCS#8 outline. A header alone, a truncated or random body, a Proc-Type (traditional encrypted) block and a closed `CERTIFICATE` are not hits |
| A bare base64 run | at least 100 decoded bytes (the floor is a cost bound; the outline is what excludes false positives) that decode to a `SEQUENCE` opening with `INTEGER` 0 or 1, then PKCS#8 (`SEQUENCE{OID..}`, `OCTET STRING`), PKCS#1 or DSA (five or more `INTEGER`s) or SEC1 (`OCTET STRING`, optional `[0]`/`[1]`), the children filling the `SEQUENCE` exactly. A certificate or public key opens with a `SEQUENCE` and matches none |

**Joined fragments.** A Python test writes a key as adjacent quoted strings, one
per line, so no single line is long enough to judge. A quoted base64 fragment is
joined to the lines straight after it until a line that is not a fragment, a
line ending `,` or `)`, or a padded `=`. It is worth the small state machine
because it is the shape the 2026-11-06 keys were committed in. A comma ends the
literal, so a list of separate strings is never read as one key. A PEM block
and the same body read as a bare run are reported once.

**Known gaps, stated.** A joined run is judged from its first character, so a
key that does not begin at a fragment is missed. A bare run under 100 decoded
bytes (an Ed25519 key) is missed, though its PEM form is caught. Base64url
(`-` `_`) runs, PGP private-key blocks, and a key split over comma-separated
literals are not read. In `--staged` mode only the **added lines** are read (no
blob), so a key is seen if its lines were added together; the CI run reads the
whole file and prints anything the hook missed. Cost: the file is streamed
through the 020/370 reader, a joined run is capped at the PEM bound (about 150
KiB), and a hit is held as a redacted finding under the findings cap, so
memory stays bounded. An excerpt names the form and the decoded length and
never the key. Tests: `tools/test_secretscan.py` (`Exempt*`); the key shapes in
them are **built at test time** by `synthetic_private_der`, never written down.

### Bounded memory (020/370)

Peak memory is bounded by a fixed constant, independent of how large the tree
or any one file is — an estate probe once pushed this scanner to ~9 GB RSS
over a large repo and thrashed the machine running it; Mike's ruling: *"it
should not matter how much it scans it should no have this affect."* Three
mechanisms, each a fixed size chosen once (see the constants and comments
beside `_iter_numbered_lines`/`Tally.take_finding_slot` in the source):

- the file walk streams (`filewalk.py`: a streamed `git ls-files` inside a git
  work tree, else `os.walk` pruned in place) instead of building the whole
  tree's file list before scanning a byte;
- a file is read and decoded in fixed-size chunks, never held whole as bytes
  **and** a decoded `str` **and** a `splitlines()` list at once (the old
  shape); an overlong single line (no `\n` in sight) is scanned in
  overlapping windows instead of being buffered whole;
- the number of findings actually held in memory is capped
  (`MAX_MATERIALIZED_FINDINGS`, 50,000) — every finding past the cap is still
  **counted** (the exit code, the advisory count, and `--json`'s `counts`
  block all read the true total) but not built as an object, so pathological
  content can't make the findings list itself grow without bound. Hitting the
  cap prints how many more there were; it is never silent.

`tools/memprobe.py` measures a scanner's real (whole-process) peak RSS from
outside it; `tools/test_secretscan.py::BoundedMemory` is the regression guard
built on it, and the template every guard in `020/380` reuses.

### Usage

```sh
python3 tools/secretscan.py                 # scan the whole repo
python3 tools/secretscan.py --staged        # scan only staged additions (the hook)
python3 tools/secretscan.py path/to/file    # scan specific paths
python3 tools/secretscan.py --json          # machine-readable, for CI/composition
python3 tools/secretscan.py --selftest      # prove the engine on this box
```

Exit codes follow the shared contract (`report.py`, below): `0` includes
advisory-only findings. Escape hatches mirror leakscan's: `# secretscan:allow:
<reason>` per line, a glob in `.secretscanignore` per path, and `--disable
<rule>` to quiet a noisy rule (a named rule, `assigned`, `high-entropy`, or
`low-variety-entropy`) while keeping the rest. A true positive is never just
exempted — **remove it, move it to the secret store, and rotate it.**

## `licenscan.py` — the pre-publish licence gate

The third member of the publish triad. leakscan keeps personal data out;
secretscan keeps credentials out; both guard *content*. `licenscan` guards the
licence story: publish a repo whose licence is missing, self-contradictory, or
carries someone else's copyleft code and you grant the wrong rights (or, with no
LICENSE, none — the default is all-rights-reserved). Unlike the other two it is a
**pre-publish** check, not an every-commit one: a private repo carries licence
mess harmlessly; it only bites at the public boundary that `AUTONOMY` already
gates.

### Three checks, rising specificity

| Check | Catches | Severity |
|---|---|---|
| **LICENSE present + recognised** | an open repo with no LICENSE (all-rights-reserved by default), or a LICENSE body no known SPDX licence matches (read as a declared custom licence since 2026-08-05 — the per-file header checks keep running; only declaration comparison is skipped) | high (no LICENSE, blocks) / medium (unrecognised, advisory) |
| **Declarations agree** | metadata that names a *different* licence than LICENSE — `pyproject.toml`, `package.json`, `Cargo.toml`, `*.gemspec`, `setup.cfg`, a README shields.io badge — i.e. the repo contradicting itself; or a declaration that is not a recognised SPDX id at all | high (contradiction, blocks) / medium (unknown id, advisory) |
| **No incompatible header** | a file with an `SPDX-License-Identifier` differing from the repo licence — copyleft (GPL/AGPL/LGPL/MPL) into a permissive repo is a **block** (can't be relicensed on publish); permissive-into-permissive is a warn, reported without blocking | high (blocks) / medium (advisory) |

The compatibility judgement is deliberately **conservative** — it flags for a
human, it is not legal advice, and it does not encode the deep cases (e.g.
Apache-2.0/GPLv2). It encodes the one that bites in practice:
copyleft-into-permissive.

### Two responses (115/290, 2026-10-16)

A finding carries a **response** as well as a kind, derived from its severity,
and only one response touches the exit code:

| Response | Severity | Findings | Exit code |
|---|---|---|---|
| **block** | `high` | no LICENSE, a declaration contradicting it, a copyleft header in a permissive (or custom) repo, a failed `--expect` | `1` |
| **advisory** | `medium` | a permissive header differing from the repo licence, a LICENSE or declaration the scan cannot read as a known SPDX id | `0` |

Until 2026-10-16 the docstring and this section called the `medium` findings a
*warn* ("friction, never a silent pass") while the code counted every one toward
exit 1, so a warn blocked a publish. Mike ruled 2026-10-16: *make the warning
real.* The blocking set did not move; the `medium` findings are now shown in a
`🟡 ADVISORY FINDINGS` block of their own, which shares no wording with the
blocking block. A severity the tool does not know as advisory blocks. The tier
ships with its consumer, the way `secretscan`'s does: `licenscan` prints
`licenscan advisory: N finding(s)` on **every** run, zero included, and
`floor.py`'s board reads it into a `🟡 N advisory finding(s)` count from that
run's output (no state file). `--json` carries `blocked`, `counts` (`blocking`,
`advisory`) and a `response` on each finding; `clean` keeps its meaning of
nothing found at all.

### Usage

```sh
python3 tools/licenscan.py                      # scan the repo in cwd
python3 tools/licenscan.py path/to/repo         # scan a specific repo root
python3 tools/licenscan.py --expect Apache-2.0  # assert the licence (CI); fail if LICENSE differs
python3 tools/licenscan.py --json               # machine-readable, for CI/composition
python3 tools/licenscan.py --selftest           # prove the engine on this box
```

Exit codes follow the shared contract (`report.py`, below): `0` includes
advisory-only findings and `1` means publish blocked. Escape hatches mirror the
others': `# licenscan:allow: <reason>` per line (a deliberately dual-licensed
file, or a header in test data), a glob in `.licenscanignore` per path. `#
licenscan:allow:<kind>: <reason>` exempts one kind only (`mismatch`,
`incompatible`, `unknown-declaration`, `unknown-license`), so a marker written
for a permissive mismatch no longer covers a copyleft header (`115/080`). A
scope naming none of the kinds still exempts the whole line, as it always did.
Because it's a publish gate, wire it into the **pre-publish** scrub (alongside
the leak/secret pass) and CI's release job — not the per-commit hook.

## `conflictscan.py` — no unresolved merge-conflict marker reaches history

The fourth check with `advisory=None`: a committed conflict marker is never
correct, at any repo's stage of adopting the check, so it has no soft form —
the same severity class as `secretscan`, not the first-of-kind advisory
rollout `datescan`/`wrapscan`/`spellscan` used. Grounded in a real incident
(roadmap `320/200`): a bad merge fenced two records inside `<<<<<<< HEAD` /
`=======` / `>>>>>>> <sha>` in a **public** repo, the floor was green on
every commit, and nothing mechanical read a line as a conflict marker until
a human happened to open the file a day later.

### Four marker shapes, two of them gated

| Marker | Shape | Flagged |
|---|---|---|
| **opener** | `^<<<<<<< ` | always |
| **closer** | `^>>>>>>> ` | always |
| **base** (diff3) | `^\|\|\|\|\|\|\| ` | only inside an OPEN region |
| **separator** | `^=======$` (exactly seven `=`) | only inside an OPEN region |

A bare `=======` line is also a valid Markdown/RST setext heading underline —
`wrapscan`'s own doctrine files use exactly this shape. The separator (and
the diff3 base marker) is a finding only when an earlier, still-unclosed
`<<<<<<< ` opener has been seen in the SAME file — a standalone heading,
however wide, never sits after one. Combined with requiring the separator's
length be exactly seven characters (not "three or more"), the two checks
close the gap either leaves alone on its own. Stated residual: an opener with
no matching closer before end-of-file leaves the REST of that file read as
still-open, so a later, otherwise-innocent separator downstream also flags —
the opposite direction from `wrapscan`'s own "unclosed fence" residual, and
accepted here because a file that opens a conflict and never closes it is
already the failure this check exists to catch.

Unlike the Markdown-only doc scanners, this one runs over **every tracked
file type** (matching `secretscan`'s/`leakscan`'s own whole-tree shape,
binary skipped on the first NUL byte) — a bad merge can fence a marker into
source or config just as easily as a doc. It also carries no fenced-code
exemption: a doc that legitimately quotes a marker at the START of a line
needs the ordinary allow-marker, the same route this scanner's own grounding
item needs for the lines it quotes.

### A fifth shape, advisory: tool-call markup saved into a file (`320/490`)

Files written with the harness's file-write tool sometimes end in the call's
own closing markup (a last line of just the content tag's closer, then the
invoke block's), saved into the body. It silently corrupts a record, a doc or
an agent memory, and no scanner saw it. A line at column 0 that is exactly
either closing tag (an allow-marker may trail it), or that starts with an
opening `invoke name=` or `parameter name=` tag, is a `tool-markup` finding.

It uses the **advisory tier** `secretscan` and `licenscan` already have, not
the blocking one: it is reported (`🟡 ADVISORY FINDINGS`), counted on the
always-printed line `conflictscan advisory: N finding(s) — reported, not
blocking.`, carried onto the `floor.py` board, and never moves the exit code.
Why advisory: the estate holds frozen instances this scan had not met, and
a blocking rule would red a child on its next CI run for a file it may not
touch. The flip to blocking is one edit once the estate is clean. Escape
hatches are the shared two: `conflictscan:allow: <reason>` on the line (a
comment after the tag, for a doc that quotes it on purpose) and a reasoned
glob in `.conflictscanignore` (this repo exempts its two frozen session
records that carry the leak; a record is history and is not rewritten).

### Usage

```sh
python3 tools/conflictscan.py                 # scan the whole repo
python3 tools/conflictscan.py --staged        # scan only staged additions (the hook)
python3 tools/conflictscan.py path/to/file    # scan specific paths
python3 tools/conflictscan.py --json          # machine-readable, for CI/composition
python3 tools/conflictscan.py --selftest      # prove the engine on this box
```

Exit codes: `0` clean, or advisory tool-markup findings only · `1` conflict-marker
findings, commit blocked · `2` usage/config error — no `--warn`, since the
conflict markers have no soft form. Escape hatches mirror
the others: `# conflictscan:allow: <reason>` per line (a doc quoting the
markers at line start) and a glob in `.conflictscanignore` per path.

## `worktree.py` — one worktree per line of work

`method/CONCURRENCY.md` says every independent line of work gets its own git
worktree — own checkout, own branch, **outside iCloud** (a live `.git` index in
iCloud corrupts under sync) — reconciling on `main` via PR/merge. Said once
that's easy; at 11pm it's the forgotten rule. This makes the right thing the
one-liner and bakes the guards in.

| Command | Does | Guard it encodes |
|---|---|---|
| `worktree start <feature>` | checkout at `~/worktrees/<repo>-<feature>`, branch `<feature>` | **refuses an iCloud base**; branches off the integration branch so a line never inherits a half-done branch |
| `worktree list` | every worktree + ahead/behind, dirty, age | flags **stale** (diverged for days = merge hazard) and **dirty** (leaked file handle) trees |
| `worktree land [<feature>]` | push the branch + open a PR back to `main` | refuses to land `main` onto itself or with uncommitted changes; falls back to a local-merge instruction when there's no remote |
| `worktree remove <feature>` | `git worktree remove`, guarded | **refuses to delete uncommitted or unmerged work** without `--force` — losing work is the failure mode the whole doctrine exists to prevent |

### Usage

```sh
python3 tools/worktree.py start perf-harness   # fork a line of work
python3 tools/worktree.py list                 # hygiene view (--json for tooling)
python3 tools/worktree.py list --check         # exit 1 if any tree is stale/dirty (CI/hooks)
python3 tools/worktree.py land perf-harness    # push + PR back to main
python3 tools/worktree.py remove perf-harness --delete-branch
python3 tools/worktree.py --selftest           # prove the guard logic offline
```

Zero-dep, `--json` on every command (the orchestrator seam), fail-safe exit
codes (0 ok · 1 a guard tripped · 2 environment error). Real-world side-effects
stay serialised: this forks *build-time* lines only — applying a change to a live
device is still one-at-a-time and announced (CONCURRENCY "the safety rail").

## `pins.py` — the fleet view of who is stale on the doctrine

`method/PROPAGATION.md` makes staleness observable one repo at a time: each
child's `CLAUDE.md` carries a pin (`atelier@<SHA>`) and a session-start drift
check. That is per-child and pull-based — a child only shows it's behind when a
session opens in it. `pins` is the roll-up: stand in atelier, get one answer to
"across the whole fleet, who is behind, and by how much?".

It is deliberately **read-only**. Bumping a pin stays a per-repo
human-in-the-loop act (PROPAGATION §5 — read the delta, judge it bears on that
repo, then move the pin). This tool never edits a child; it turns per-child
observability into a fleet view and nothing more.

| Status | Means | Mark |
|---|---|---|
| `current` | pin == atelier HEAD | ✓ |
| `behind` | pin is an ancestor of HEAD — N house commits since | → |
| `ahead` | HEAD is an ancestor of pin — child pinned newer (atelier not pulled here?) | ! |
| `diverged` | neither is an ancestor — pin on a different history | ✗ |
| `unknown` | atelier has no such object — bad/rewritten pin, or unfetched | ? |
| `no-pin` | `CLAUDE.md` exists but names no atelier pin | · |

### Usage

```sh
python3 tools/pins.py                    # discover children under atelier's parent, report
python3 tools/pins.py --log              # also print the commits each stale child would inspect
python3 tools/pins.py --child ../ros     # report only named repo(s) (repeatable; skips discovery)
python3 tools/pins.py --root ~/code      # search a different root (repeatable)
python3 tools/pins.py --json             # machine-readable, for a dashboard / CI gate
python3 tools/pins.py --check            # exit 1 if any child is not current (CI/hooks)
python3 tools/pins.py --selftest         # prove the parse + classification offline
```

Discovery walks one level under each search root (default: atelier's parent dir)
for git repos whose `CLAUDE.md` carries a pin; atelier itself is excluded. An
unreadable root degrades to a warning, not a crash (fail-safe). Exit codes match
the others: `0` every child current · `1` at least one not current · `2`
environment error (not an atelier repo, HEAD unreadable, a named child missing) —
so a fleet it *couldn't* verify never reports green.

## `linkscan.py` — keep the doctrine's internal pointers resolving

atelier's architecture is **"thin anchor, fat pointer"** (`method/PROPAGATION.md`):
a child inlines a safety floor and *points up* to canonical doctrine; a doc states
a bearing and *points* to its case-law. The whole graph is only as sound as its
links. A relative link that 404s — a renamed file, a moved doc, a typo'd `#anchor`
— is a silent hole: the reader is told "see X" and X isn't there. `linkscan` is the
machine that catches it before a reader (or an adopter) does.

Scope is deliberately narrow — a sharp honest check beats a broad flaky one:

- **Internal links only.** `[text](path)` / `![alt](path)` with a relative or
  root-relative (`/…`) destination. External schemes (`http`, `https`, `mailto`,
  `tel`, …) and protocol-relative `//host` are **skipped** — verifying them means
  the network, which is a different, flakier tool's job.
- **File existence** — the path must resolve (relative to the linking file, or the
  repo root for a leading `/` — GitHub resolves those against the repository root
  too), to a real file *or* directory, with the **on-disk casing matched exactly**
  (a case-insensitive local disk hides a mismatch GitHub 404s) and the target
  **inside the repo root** (GitHub serves nothing above it — a `../…` that
  resolves on this machine is still a 404 for every reader).
- **Anchor existence** — a `#fragment` into a Markdown target (or same-file) must
  match a heading anchor **exactly** (GitHub fragment matching is exact —
  `#A-Section` never reaches `#a-section`; the report says what to write
  instead). ATX (`#`) and setext (underline) headings both mint anchors. `#L42`
  line anchors are line references, not headings, and are skipped; anchors into
  non-Markdown targets aren't validated (nothing to validate against).

Links inside fenced (` ``` `) or inline (`` `…` ``) code are ignored — they're
examples, not live pointers. Wiki-style `[[name]]` memory links aren't Markdown
links and are out of scope by design. A deliberately dangling pointer is exempted
with `<!-- linkscan:allow: <reason> -->` on the line, or a glob in
`.linkscanignore`.

**A child's inlined floor is not scanned** (`320/610`): in a repo that does not
hold `docs/method/PROPAGATION.md`, the text between `stamp:begin
source=docs/method/PROPAGATION.md region=floor` and `stamp:end` is atelier's
floor copied word for word. `stampscan` checks it against the canonical copy;
the child's tree cannot resolve the atelier-relative paths it names
(`method/TOOLBOX.md`), and the child cannot add an allow-marker without
drifting from the canonical text. So `pathscan` skips that block there. The
same path anywhere else in the file still reports, and where the canonical
source is in the tree (atelier itself) the stamped copy is scanned as before.

**Bounded on any single file** (`110/120`): a file is streamed line by line, not
held whole; no more than `MAX_MATERIALIZED_FINDINGS` (50,000) findings are built,
and every one past that is **counted** and printed (`…and N more broken link(s)`,
plus `--json`'s `findings_over_cap`), so the headline total and the exit code
stay true. The count prints on every run, a known `0` included, as in the other
guards' summaries. Each distinct
`(directory, link path)` is resolved against the disk once per scan.

### Usage

```sh
python3 tools/linkscan.py                 # scan the whole repo
python3 tools/linkscan.py docs/method      # scan a subtree / named files
python3 tools/linkscan.py --root . .       # explicit root for /… links + .linkscanignore
python3 tools/linkscan.py --json           # machine-readable, for CI
python3 tools/linkscan.py --selftest       # prove the engine offline
```

Exit codes follow the shared contract (`report.py`, below): `1` is at least one
broken link, and a scan it *couldn't* complete is `2`, never green. See the
residual note at the top for what it structurally cannot catch.

**Wiring** — unlike the licence gate, linkscan runs on both the **pre-commit
hook** and **CI**, always over the **whole tree** (not `--staged`): a link goes
stale when a *different* file is renamed or deleted, so the file to re-check is
rarely the one in the diff. It is cheap (stdlib, no network) so the hot-path cost
is negligible, and it is the one gate that catches a 404 *before* a push
publishes it. A repo that keeps its tree link-clean pays nothing; a deliberately
dangling pointer uses `linkscan:allow` / `.linkscanignore`.

## `sizescan.py` — keep cold content off the always-loaded files

A session resumes cold by reading a handful of files at the start — the roadmap
(what's open), the session index (where the last one stopped), the README, the
architecture note. `RECORD.md` prescribes the fix for when they bloat — the
**current-truth / history split** (open items stay; completed detail moves to
`ROADMAP-DONE.md`; a flat session log becomes an index + `docs/sessions/`). The
split works, but nothing *triggered* it: it got done once by hand and the
discipline decayed silently — a sibling roadmap reached 3000+ lines, each
finished item accreting a running log of how it got done, no signal firing.
`sizescan` is that missing signal.

**Cost is size × read-frequency (2026-07-20 ruling)**, so the enemy is never
fulsomeness — it is **cold content on the hot path**: content that is finished
(no longer live current-truth) yet still loaded every session. `sizescan` fires
on exactly that, and only where the fix is mechanical and lossless:

- **The cold-content gate** fires on **relocatable cold content** — a completed
  `[x]` item on a checkbox-worklog file (`ROADMAP.md`), whose whole remedy is a
  lossless move to `ROADMAP-DONE.md` (the current-truth/history split). The gate
  can never demand a reword: it fires only when a machine can name the fix as a
  move. It never fires on length.
- **The harvest-integrity gate** fires on a live state marker (`[ ]`, `[~]`, `⏳`)
  in a named archive store (`*-DONE.md`, `*-ARCHIVE.md`), which records finished
  history only.

**There is no size check.** sizescan once also reported a hot file's length
against a class reference point (`ROADMAP` ~300 lines, `SESSIONS`/`README`/
`ARCHITECTURE` ~250, `CLAUDE` ~200) as an advisory that never failed a build,
with a `sizescan:budget=N` marker to override it. Mike's ruling: "I specifically
do not want artibuary limits like a fixed kb or line count as limits because
that is contrary to the purpose", and asked what the advisory was for, he
answered "Remove it" (`115/270` c). The reference points, the marker and the
advisory output are gone. What that gave up, stated plainly: the advisory was
the only pointer to **prose-shaped cold content** (resolved narrative under an
*open* item) and to thinness, which a machine cannot name without guessing. They
stay **caught at review, not measured**, with nothing in the tool pointing at
them. A finding still prints its file's line count as context, never as a
trigger.

Scope, in two deliberate directions:

- **Cold content is looked for in `ROADMAP.md` only**, wherever it lives. The
  other current-truth names (`SESSIONS.md`, `ARCHITECTURE.md`, the root
  `README.md` and `CLAUDE.md`) are no longer measured for anything; their first
  15 lines are still read, so that a hatch left in them is named as inert (below)
  rather than silently accepted. A nested `tools/README.md` is a reference index
  and is not read.
- **It ignores the append-only stores** — `ROADMAP-DONE.md`, `CHANGELOG.md`,
  `SPECS.md`, and anything under `sessions/`, `reviews/`, `decisions/`, or archive
  dirs — for cold content. Those are the *destinations* the split moves detail
  into. A named archive store inside one is still integrity-checked.

**Nothing silences the cold-content gate** (`115/270`, Mike's ruling: no repo
keeps a flat running log; the board is a list of work and its state, and the
detail lives in a standalone file). An unscoped `sizescan:allow`, a
`sizescan:allow:cold-content` scope and a `.sizescanignore` glob all leave a
file's completed `[x]` items gated; a glob no longer skips the file.

**Two hatches still do something, only on an archive store.** An unscoped (or
`harvest-integrity`-scoped) `sizescan:allow: <reason>` header exempts the store's
integrity check, and a glob in `.sizescanignore` skips it. They are counted on
the `suppressed:` line.

**Every other hatch is present and inert, and the report names it.** With the
size advisory gone, a `sizescan:allow` on any other hot-path file (it only ever
quieted that advisory), a scope that does not cover the file's own kind
(`size-advisory`, `cold-content`, or `harvest-integrity` on a roadmap), a
`.sizescanignore` glob over a hot-path file and a leftover `sizescan:budget=N`
exempt nothing. Each is listed under "Inert hatches" with its path (on a roadmap
that carries cold content, under that finding instead: `note: sizescan:allow
header (unscoped) present and inert — it cannot exempt cold content`), counted on
the `suppressed:` line as `N inert hatch(es) (exempt nothing)`, and carried in
`--json` as `inert_hatches`. They change no verdict and no exit code: remove
them. No new exemption exists. `size-advisory` stays a recognised, retired scope
name so a stale `sizescan:allow:size-advisory:` marker is not mistaken for the
unscoped form, which *would* exempt an archive store (`115/080`).

**The gate names what it counted.** Each flagged file lists every completed item
(`line 12: the item's text`, text capped at 60 characters), so the move to
`ROADMAP-DONE.md` is a lookup, not an inference. The listing is capped
run-wide at `MAX_MATERIALIZED_FINDINGS` (50,000, the cap every scanner uses);
items past it are counted, never dropped silently: the report prints
`…and N more completed item(s), counted but not listed`, the `suppressed:` line
carries `N beyond the 50000-finding cap`, and `--json` carries each file's
`cold_listed` (`line`, `title`), its `cold_hatches` and two top-level fields,
`cold_items_over_cap` and `inert_hatches`.

### Usage

```sh
python3 tools/sizescan.py                  # report over the whole repo (cold content, archive integrity, inert hatches)
python3 tools/sizescan.py --root repo      # scan a child from atelier
python3 tools/sizescan.py --check          # gate: exit 1 on relocatable cold content or a live archive marker
python3 tools/sizescan.py --json           # machine-readable
python3 tools/sizescan.py --check --staged # the hook plane: staged copy of each roadmap / archive store the commit touches
python3 tools/sizescan.py --selftest       # prove the engine offline
```

**On the hook plane it reads the index** (`320/600`). Cold content and live
state are properties of a whole file, so `--staged` judges the **whole staged
copy** of each hot-path file or archive store the commit touches, not just the
lines it adds, and a deletion-only edit is judged too (it adds no line, yet it
can unbalance a fence). A file the commit does not touch is not read at the
hook: its state is CI's whole-tree read, which is unchanged.

**The gate has a narrow bite.** Cold content is a recoverable hygiene threshold
with a lossless fix — harvest the `[x]` item aside — so a bare `sizescan`
**reports and exits 0** (drop it in CI to surface findings without breaking a
build); `--check` gives it teeth, but **only on cold content and archive
integrity, never on length** (length is not reported at all). Exit codes: `0`
clean, or findings without `--check` (inert hatches are named but never change
it) · `1` cold content or a live archive marker present **and** `--check` · `2`
usage/config error (a scan that read nothing is never green — fail-loud, not
fail-open).

**Wired into the gate (2026-07-20).** `sizescan --check` runs in atelier's
`ci.yml` and the child `floor.yml` in cold-content mode. Because it gates only on
a lossless move, it is safe to stack: it can red a build only when the fix is
`git mv`-shaped, never when it would demand a reword.

## `reviewscan.py` — decision records state their review judgement

`REVIEW.md`'s remedy made *declining* a review an act: every durable design
record carries a `review:` line — a queued pointer or an explicit
`not warranted — <grounds>` — because a reader can disagree with a stated
judgement but not with a blank. This is the structural half of that rule: it
reds any record under a `docs/decisions/` directory, named on the
coordination-free `YYYY-MM-DD[-HHMM]-slug.md` scheme and dated on or after
**2026-07-21** (the day the templates began prompting for the field — frozen
records are append-only and never flagged), that carries no review line.
Presence only, by design; scope deliberately excludes roadmap headings (a lint
there fires on prose — the `2026-07-18-0820` record's grounds). Exemption
hatch: `reviewscan:allow: <reason>` on any line. Deliberation:
`docs/decisions/2026-07-21-0744-review-line-artefact.md`.

```sh
python3 tools/reviewscan.py --root . .        # scan a repo
python3 tools/reviewscan.py --root . docs/decisions   # a decisions dir directly
python3 tools/reviewscan.py --staged --root .  # the hook plane: staged copy of each record / brief the commit touches
python3 tools/reviewscan.py --selftest        # prove it against fixtures
```

**On the hook plane it reads the index** (`320/600`). Both checks are
properties of a whole file (does the record carry a review line; does the brief
carry a deferred section with no verdict), so `--staged` judges the **whole
staged copy** of each decision record and review brief the commit touches. A
deletion-only edit that drops a record's review line is judged, which an
added-lines filter would miss. A record or brief the commit does not touch is
left to CI's whole-tree read.

A path arg may be a tree, a `docs/decisions/` dir itself, or a single record
file — an explicitly-named path is scanned, never silently matched by nothing
(the 2026-07-21 cold pass's RS1). The review line must carry a non-empty
value, and a `review:` quoted inside a code fence doesn't count (RS2/RS3).

## `publishscan.py` — no machine-local config is tracked

Every other scanner here asks *does this file contain something private?* This
one asks *does publishing this file, whatever it holds, help someone attack the
repo?* They come apart: `rpi`'s committed `.claude/settings.json` published the
exact list of commands an AI session runs **unprompted** — while going public
opened untrusted inbound (issues, PRs) into those sessions — and both content
scanners passed it correctly, because it holds no credential and no personal
fact. **The exposure was the file's presence, not its contents** (rpi F1,
2026-07-29; Mike ruled the same day that the allowlist is untracked
*everywhere*, not only on public repos, because a visibility-conditional rule
becomes wrong at the moment of the flip).

Patterns carry their provenance in the source: the `.claude/settings*.json`
pair is grounded in that finding; `.mcp.json`, `.env*`, `.envrc`, `.netrc`,
`.npmrc`, `.pypirc` and editor-local config are standard practice, named as
such rather than dressed up as findings. A second round (2026-10-03) added the
shapes a survey of the estate's tracked files found (runtime logs, local
databases, compiled-Python caches), plus standard-practice key, keystore,
history, dump, capture, tool-cache and OS-cruft shapes. Each entry says which
tier it is. Generic `*.pem`, `credentials*.json`,
`*.rsc`, archives and `*.jsonl` were considered and left out, because
legitimate files wear those names. Hatch: a glob in
`.publishscanignore` — there is deliberately **no line marker**, because a
reason written inside a file that should not exist is an exemption no reviewer
would ever see.

```sh
python3 tools/publishscan.py --root .            # the tracked set (CI plane)
python3 tools/publishscan.py --root . --staged   # what this commit adds (hook)
python3 tools/publishscan.py --root . --warn     # advisory while a repo cleans up
python3 tools/publishscan.py --root . --history  # every path ever added (pre-flip)
python3 tools/publishscan.py --selftest          # prove it against fixtures
```

**`--history` is the pre-flip plane, and it is opt-in.** The default planes
read the current tree, but a flip publishes every path ever pushed. The
history plane applies the same rules and the same ignore file to every path
added on any branch, tag or remote-tracking ref. It reports each hit with the
oldest commit that added it, and says whether the tip still tracks it or it
lives in history only. A history-only hit cannot be untracked away; removing it
takes a history rewrite or a fresh history, and that is the owner's call before
the flip. It reads `git log --name-only -z` and not `rev-list --objects`,
because the blob walk prints one name per blob and drops every other path with
the same bytes. Its output is streamed, and only the hits are held. A shallow
clone is a broken scan (exit 2). `--history` and `--staged` are separate
planes and cannot be combined. The floor registry does not run it. It was added
with round 3's single shape, `*.egg-info/`, from the harvest of a flip's
transcripts (`260/090`); that shape was tracked at the tip of no sibling repo
when it landed.

A tree with no git skips visibly at exit 0 — not a fail-open, since nothing is
tracked and so nothing can be published from it. Every *other* git failure (git
absent, repo corrupt) is exit 2: a broken scan is not a pass.

## `datescan.py` — absolute-UTC dating discipline (enforced; shipped first-of-kind)

Seam S3 (2026-07-22 invariant-candidates review): a dated record states
ISO-8601 absolute dates stamped from `date -u`, never a relative-time word
("today", "yesterday", "last week") whose meaning drifts with the reader's
"now" — grounded in a real miss, the standing correction that cost a
five-file sweep when a record was stamped from local NZ time instead of UTC.
Two checks over `docs/**` Markdown by default: a **relative-time-word
denylist**, and an **ISO/UTC shape check** (a non-ISO absolute date like
`23/07/2026` or `July 23, 2026`; an ISO-*shaped* date that isn't a real
calendar day, e.g. `2026-13-40`).

**Wiring: enforced.** The floor registry (`tools/floor.py`) runs it blocking
on both the pre-commit hook and CI, and `floor.py --list` prints it
`enforced`. It shipped first-of-kind and advisory-only (CI in `--warn`, kept
out of the hook until it had an independent review); the flip to blocking in
CI was Mike's ruling in `d24caec` (2026-07-23), after the cold review passed
and the docs re-baselined to zero genuine breaches, and the registry
(`40c7a22`, 2026-07-25) then put it on the hook plane too. On the hook plane it
runs `--staged` (`320/600`), exactly as `spellscan` and `wrapscan` do: the
staged copy is read from the index, whole, and only findings on lines the
commit **adds** are kept. CI keeps the whole-tree read.

Exemptions, deliberately generous (a false positive costs a comment; a noisy
scanner trains itself away): a fenced code block or blockquoted line (quoted
external text; a blockquoted line now reports, below), an inline
`` `code span` ``, and — the hard case — a
relative-time word immediately flanked by a matching quote pair (`"today"`)
is read as a MENTION (prose *about* the word) rather than a USE, exactly the
shape the rule's own worked examples use. This is a punctuation heuristic,
not a parser: unquoted prose about relative time still false-positives, and
is meant to be closed with `datescan:allow`. The rule's third clause — "a
dated maintenance edit carries its date" — is **not** mechanically checked;
naming an edit's intent isn't a shape a text scanner can see honestly, so
that clause stays caught at review, same honesty as sizescan's
prose-cold-content residual.

```sh
python3 tools/datescan.py                 # scan docs/** (default scope)
python3 tools/datescan.py --root . docs    # explicit — the CI invocation
python3 tools/datescan.py --warn           # report findings, always exit 0
python3 tools/datescan.py --json           # machine-readable
python3 tools/datescan.py --selftest       # prove the engine offline
```

Exit codes follow the shared contract (`report.py`, below): `0` includes
report-only findings and `--warn`; `1` is blocking findings without it. Escape
hatches mirror the sibling scanners: `<!-- datescan:allow: <reason> -->` per
line, a glob in `.datescanignore` per path.

### Blockquoted lines report, and never block (115/090)

A blockquoted (`>`) line never blocks, because it may be a quoted source's own
words. It is also the house's own callout style, so its dating used to pass
unseen. Now every check runs on it; each hit is listed in a `🟡 REPORT-ONLY
FINDINGS` block, counted on a line printed on every run, zero included
(`datescan advisory: N finding(s) — reported, not blocking.`), and carried on
the floor board as `🟡 datescan enforced`. None of them moves the exit code.
Code inside or beside a blockquote stays exempt, and an allow-marker or a
`.datescanignore` glob exempts a report-only hit as it does a blocking one.

Nothing that blocks stops blocking: `test_datescan.BlockingSetPinned` pins
every check that blocked. A bare "today" with no date cue still passes
unreported: across the estate it is about 2,650 hits, nearly all the
"currently" sense, so a report of it would be a flood. `--json` keeps `clean`
and `findings` for blocking findings and adds `blocked`, `counts` and
`advisory`. Built on Mike's answer of 2026-11-03 ("Carry on to datescan").
Design and residuals: `datescan.off-rules.design.md`.

## `wrapscan.py` — line-wrap / column hygiene (enforced; shipped first-of-kind)

Seam S1 (2026-07-22 invariant-candidates review): Markdown prose under
`docs/**` wraps at the house width; a line **materially over** it reds —
concretely at or beyond `LINE_LIMIT + 1` (86 cols at the shipped limit of 85).
Grounded in a real repeat: the same over-wide-line class shipped **three
cycles running** (`SL7` → `AC1` at 122 cols → `IR3`), each fix re-introducing
the next, because nothing mechanical caught a judgement the reviewer kept
re-making. This scanner is that column count.

**Wiring: enforced.** The floor registry runs it blocking on both the
pre-commit hook and CI, and `floor.py --list` prints it `enforced`. It shipped
advisory-only (CI in `--warn`, not in the hook, until reviewed); Mike's ruling
flipped it to blocking in CI in `4f1c10c` (2026-07-23), once the
doctrine-surface scope scanned clean, and the registry (`40c7a22`, 2026-07-25)
then put it on the hook plane too. On the hook plane it runs `--staged`
(`320/600`): it reads each staged Markdown file from the git **index**, whole,
so fence state is right, and reports only the lines the commit **adds**. An
unstaged draft on disk can no longer block someone else's commit, and a staged
over-long line cannot pass because its disk copy was fixed after `git add`. CI
keeps the whole-tree read.

Column length is a character count, honest for the house's ASCII prose but not
a true display-width measure (a stated Unicode caveat). Four exemptions,
each with its honest limit documented in-header: **fenced/indented code**
(the indented rule is per-line, so it also exempts some wrappable indented
prose — a false negative accepted over a false positive inside real code);
**table rows** (any `|`-bearing line — a bare heuristic, not a table parser);
**ATX headings**; **reference-style link definitions**; and **single
unbreakable-token overflow** (a URL/path/long identifier with no legal wrap
point in the overflow — this *will* let through prose that merely ends in one
long word, the accepted line-local trade-off). Setext underlines are correctly
not special-cased.

```sh
python3 tools/wrapscan.py                  # scan docs/** (default scope)
python3 tools/wrapscan.py --root . docs     # explicit — the CI invocation
python3 tools/wrapscan.py --warn            # report findings, always exit 0
python3 tools/wrapscan.py --limit 100       # tune the column limit
python3 tools/wrapscan.py --json            # machine-readable
python3 tools/wrapscan.py --staged --root . docs   # the hook plane: staged copy, added lines
python3 tools/wrapscan.py --selftest        # prove the engine offline
```

Exit codes follow the shared contract (`report.py`, below): `1` is findings
without `--warn`. Escape hatches mirror the sibling scanners:
`<!-- wrapscan:allow: <reason> -->` per line, a glob in `.wrapscanignore` per
path.

## `spellscan.py` — NZ-English spelling (enforced; shipped first-of-kind)

Seam S5 (2026-07-22 invariant-candidates review): `docs/**` uses NZ-English
spelling (artefact, organise, colour, behaviour…). The premise is that a
scanner catches the convention the eye skips — the mining found `artifact`
used 15+ times across `method/` despite the rule, caught as a finding only
twice; the class is **under-detected, not rare**.

**Wiring: enforced.** The floor registry runs it blocking on both the
pre-commit hook and CI, and `floor.py --list` prints it `enforced`. It shipped
advisory-only (CI in `--warn`, not in the hook, until reviewed); Mike's ruling
flipped it to blocking in CI in `4f1c10c` (2026-07-23), with the frozen record
stores netted by `.spellscanignore` rather than retro-spelled, and the
registry (`40c7a22`, 2026-07-25) then put it on the hook plane too. On the
hook plane it runs `--staged` (`320/600`): it reads each staged Markdown file
from the git **index**, whole, so fence state is right, and reports only the
lines the commit **adds**. An unstaged draft on disk can no longer block
someone else's commit, and a staged US spelling cannot pass because its disk
copy was fixed after `git add`. CI keeps the whole-tree read.

The denylist is generated from stem lists, one source of truth: an
`-ize/-ise` + `-yze/-yse` verb family (with a smaller `-ization/-isation`
subset that **excludes** stems whose noun is irregular — `recognize` →
`recognition`, not `recognization` — so it never invents a word), plus
hand-listed irregulars (artifact, the colour/behaviour/defence/centre
families, catalogue, favour, honour, fulfil). Matched case-insensitively as
whole words. **`license`/`practice` are deliberately excluded**: they are
US/NZ noun-verb homographs (NZ `licence`/`license`, `practice`/`practise`)
that need part-of-speech tagging to call correctly, and a bare heuristic would
false-flag every `LICENSE` heading and `SPDX-License-Identifier` — the honest
call is to leave them to review, documented in-header.

Exemptions mirror datescan (fenced/inline code, blockquotes, quote-flanked
MENTION) plus two this class needs: URL/path tokens (slash-detected, so
`actions/upload-artifact` is exempt for free) and a small `ALLOWLIST_PHRASES`
for bare-prose API terms (`artifact attestations`, `upload-artifact`…);
ALL-CAPS tokens read as identifiers/filenames. Honest limit: a legitimate
API term in bare prose still false-positives and is meant to be closed with an
inline-code span, the allowlist, or `spellscan:allow`.

```sh
python3 tools/spellscan.py                 # scan docs/** (default scope)
python3 tools/spellscan.py --root . docs    # explicit — the CI invocation
python3 tools/spellscan.py --warn           # report findings, always exit 0
python3 tools/spellscan.py --json           # machine-readable
python3 tools/spellscan.py --staged --root . docs   # the hook plane: staged copy, added lines
python3 tools/spellscan.py --selftest       # prove the engine offline
```

Exit codes follow the shared contract (`report.py`, below): `1` is findings
without `--warn`. Escape hatches mirror the sibling scanners:
`<!-- spellscan:allow: <reason> -->` per line, a glob in `.spellscanignore` per
path.

## `harvestscan.py` — a removed roadmap item arrived somewhere (advisory only)

The third member of `sizescan`'s family, and the only one that loses work: an
item **removed** from `ROADMAP.md` that arrives nowhere. Every other check reads
a file as it stands; this failure exists only as a difference between two
versions. It fingerprints an item's *content*, never its title — a healthy
roadmap retitles and re-homes constantly, and title-matching was measured at a
near-total false-positive rate.

**Scoped, and the scope is why it is wired at all.** Unscoped it fired on one
roadmap commit in four and was shelved on its author's own counsel. Its cold
pass measured the variant the shelving never did, and the principal overturned
the verdict on that measurement (HV1, 2026-07-29): scoped to
`--only-bulk-deletes` — a change shedding ≥ 50 **net** lines from `ROADMAP.md` —
the whole history holds 6 in-scope commits, of which 3 warn, including the
incident that motivated it. Net, not delete-only: that incident was +48/−184.

**Bucketed, not quadratic (020/400).** The similarity pass used to compare
every candidate item against every survivor — O(items × survivors) in item
count, and past useful at estate scale (measured: 500 items ~21s, 5,000 did
not finish inside a 120s ceiling). It now builds an inverted word index over
the survivor set once per call and, for each candidate, only checks the
survivors its own rarest words could possibly reach at the survival
threshold — an exact prefix filter for a set-overlap join, not an
approximation, so it cannot change a verdict. Worst case is bounded by the
buckets a candidate's own vocabulary touches, not by the corpus size.

```sh
python3 tools/harvestscan.py --root . --staged --only-bulk-deletes  # the hook plane
python3 tools/harvestscan.py --root . .        # working tree vs HEAD, no gate
python3 tools/harvestscan.py --against <rev>   # against another revision
python3 tools/harvestscan.py --replay          # re-measure over the whole history
python3 tools/harvestscan.py --selftest        # prove the matching logic offline
```

Exit codes: `0` always for findings — **warn-only, never blocking**, because its
similarity threshold is honestly ungrounded and a check that cannot ground its
constant may not red a build · `2` usage/config error.

## `pointerscan.py` — the queued-review pointer, refs-only and true (advisory only)

Three detectors on one parse of `ROADMAP.md`'s queued-review pointers:

- **grammar** — a pointer that seeds the reviewer's first question steers the
  pass it is queuing, against the ceiling `ROADMAP.md` and `REVIEW.md` both
  state. Fires on a question inside a pointer, plus a short list of
  reviewer-direction forms. Pass type and tier are **lawful** fields: they route
  the review; they say nothing about the delta's merits.
- **cycle state** — an item asserting a review is owed while carrying the verdict
  of the review that ran, with the state it is *actually* in named (reviewed,
  ruled, applied) rather than only the contradiction.
- **queue state** (`state`, added by `130/020`) — whether the state line counts
  true. Fires on a pointer whose own pass has run while it still wears the
  queued glyph, and on a queued review written as an ordinary open item with no
  glyph, which a count of the glyph misses.

The scope decision — **what makes an item a queued-review pointer** — is settled
in the module docstring on the four recorded specimens, and it is the load-bearing
part: the marker glyph alone misses the specimen that was still live when this
shipped. `harvestscan` imports that decision rather than keeping a second copy.

It lints **no field into existence** anywhere — the 2026-07-18-0820 record
rejected a lint demanding a review line under every roadmap heading, and
`reviewscan` honours that refusal. This forbids content in one narrow,
self-identifying item type instead, which is a different rung.

```sh
python3 tools/pointerscan.py --root . docs   # explicit — the floor's invocation
python3 tools/pointerscan.py --json          # machine-readable
python3 tools/pointerscan.py --selftest      # prove the rules on the specimens
```

Exit codes: `0` always for findings — **warn-only**; a pointer is fixable in the
commit that writes it, which is the one moment the fix costs nothing · `2`
usage/config error. Escape hatch: `pointerscan:allow: <reason>` anywhere in the
item, or on a board file's first line for the whole file. Scoped to one detector,
`pointerscan:allow:<detector>: <reason>` (`grammar`, `cycle` or `state`) exempts
that detector only (`115/080`); a scope naming none of them exempts everything,
as it always did.

## `plainscan.py` — removed 2026-09-18

Removed on the principal's ruling (2026-09-18): the reply hook
(`tools/hooks/plain-reply.py`) was already unwired, and the repo-plane gate was
warn-only in every child and printed ~6,050 findings on every commit — judged
more dangerous as noise than beneficial as a guard. Both the engine and its
tests are archived, not deleted, at git tag `archive/plainscan-2026-09-18`
(retrieve with `git show archive/plainscan-2026-09-18:tools/plainscan.py`).

## `pathscan.py` — a repo path named in prose still resolves (advisory only)

A file rename breaks every **named** path reference outside the diff that
caused it — bare prose (`docs/method/REVIEW.md`) and backtick spans alike,
which `linkscan` cannot see because they are not Markdown links. `pathscan`
finds those references and confirms each resolves, trying repo-root-relative,
relative to the referencing file, and relative to its enclosing `docs/`, with
`.md`/`.markdown` appended under the directory-index convention.

Registry-promoted 2026-08-05 (PS5): it runs warn-only on every child's hook
and CI through the floor — the `--warn` sits in the registry template as one
visible argument, because dropping it *is* the estate-wide flip to blocking
and must never happen as a side effect. **Records are excluded by default**
(FR2, ruled 2026-08-23): `docs/reviews`, `docs/sessions`, `docs/SESSIONS.md`,
`docs/ROADMAP-DONE.md` and `CHANGELOG.md` name the tree as it stood when they
were written and can never come clean without falsifying the record —
`--include-records` widens deliberately, and a records file named explicitly
as a path argument is always scanned.

**Bounded on any single file** (`110/120`): a file is streamed line by line, not
held whole, and an overlong line is scanned in overlapping windows. No more than
`MAX_MATERIALIZED_FINDINGS` (50,000) findings are built; every one past that is
**counted** and printed (`…and N more finding(s)`, plus `--json`'s
`findings_over_cap`), so the headline total and the exit code stay true. The
count prints on every run, a known `0` included, as in the other guards'
summaries. **Named residual**: on a line
longer than 16 KiB the placeholder/URL/link-destination blanking is applied in one
pass per pattern rather than re-run after each blanked span, which differs only
for adversarial nesting such as `<a <b> c>`.

### Usage

```bash
python3 tools/pathscan.py --root . docs      # the floor's shape
python3 tools/pathscan.py --include-records  # widen into the records
python3 tools/pathscan.py --selftest
```

Exit codes: `0` clean · `1` findings (suppressed by `--warn`, the registry
default) · `2` usage/config error. Escape hatches: `pathscan:allow: <reason>`
on the line, or a reasoned glob in `.pathscanignore`. **What it cannot see**:
prose that names a path without its extension or in a reworded form; a path
that resolves to the *wrong* file after a swap; see the module docstring for
the reviewed false-positive/false-negative modes.

## `indexscan.py` — a hand-maintained index names every file it maps (warn-only)

A hand-maintained index — a decisions index, a session log kept as an index
plus detail files, a tool or instrument catalogue — can drift from the
directory it maps in three ways. **Listed but missing** was already
guarded and is not re-checked here: `linkscan` fails a Markdown link to a file
that is not there, and `pathscan` reports a backtick-named path that does not
resolve. **Unlisted** was guarded by nothing: a file committed into the
directory that the index never names is invisible to every session that reads
only the index, and a link checker has nothing to fire on when there is no
link. `indexscan` adds that direction (board `200/010`, option C as ruled; the
census found 22 such indexes of 7 kinds across 14 repos, none guarded against
it; `320/430` is the same class filed from a child).

**Opt-in, per index.** An index declares what it maps in one whole-line HTML
comment near its head, invisible when rendered:

```markdown
<!-- indexscan:maps dir=sessions match=*.md before=2026-07-11 -->
<!-- indexscan:maps dir=. match=*.py exclude=test_*.py -->
```

`dir=` is relative to the index file (`.` for an index inside the directory it
maps) and must stay inside `--root`. `match=` and `exclude=` are
comma-separated globs on each **entry's name**; an entry is a file or a
subdirectory directly inside `dir`, so an instrument that is a folder is one
entry. `before=` is the frozen-record precedent: an entry whose name starts
with an ISO date earlier than it is blameless. The index file itself is always
excluded. A file with no declaration is never checked, so the scanner cannot
red a repo that has not declared one — an undeclared tree prints that it
checked nothing and exits 0.

**Listed** means a Markdown link (inline or a reference definition) resolving
to the entry or into it, or an inline code span (whole, or its first word)
naming it relative to the mapped directory, the index's directory or the root.
Fenced code is skipped: a usage example is not a catalogue entry.

**Exemptions** are counted on every run, known zeros included. An allow marker
lives **in the index**, where its readers see it: an HTML comment carrying
`indexscan:allow:` then the entry's name then a reason. One marker exempts one
entry; with no reason after the name it exempts nothing. A marker that exempts
nothing — its entry is now listed, gone, or outside every `match=` — is
reported as `stale-allow`, so a deferment written as "entry owed by finding X"
announces itself the day the entry lands. `.indexscanignore` exempts a file
from being read for declarations (a fixture tree quoting the syntax raw), each
glob with its reason. atelier's own two markers are of that deferment kind:
the shared file-walk and allow-marker helpers have catalogue entries owed by
two open review findings (FW2, AM5).

**The date rule (`date-mismatch`, `320/430`'s second residual).** An index
line whose date disagrees with the file it links passes `linkscan`, because the
link resolves. For a declaring index, `indexscan` reads the *leading* link of
each list item whose text opens with an ISO date (optionally `· HHMM UTC`) and
whose target is a date-named entry of a declared directory, and flags the line
if it is dated **earlier** than the file: an entry cannot predate the file it
describes. On the same date, an exact time earlier than the file's `-HHMM-`
start fires too; an approximate `~HHMM` is never compared. An index whose lines
carry no dates is never touched.

It checks "not earlier", not "equal", on evidence: atelier's session index has
many lines legitimately *later* than their file — addendum lines appended after
a later ruling, and entries stamped at session close — so an equality rule
fires on all of them. **The slug is not checked at all**: link text is free
prose with nothing crisp to compare against the filename, and a heuristic there
would cry wolf. Also unseen: a line dated too *late* (it reads as an addendum),
a link that is not the item's leading token, and table rows.

A deliberate exception is marked **on the offending line**, the narrowest unit,
in its own scoped form: `<!-- indexscan:allow:date-mismatch: <entry> <reason> -->`
with the entry's name. Anywhere else, or naming another entry, it exempts
nothing and is reported `stale-allow`. The earlier unscoped marker still
exempts an *unlisted* entry only; it never silences a date finding.

**Fourth requirement — declared: makes the failure cheap.** It forbids
nothing: an unlisted file still commits, and whether a file belongs in an index
is the index-keeper's call. It names the drift at the commit that causes it,
when the fix is one line.

**Wiring.** In the floor registry, **warn-only on both planes**, whole tree
(`--warn` is in the template, as `pathscan`'s is; dropping it is the flip to
blocking and is a separate ruling). Children float on `floor.py@main`, so the
registry line reaches every child's next run — where it checks nothing until
that child declares an index. atelier declares four: the decisions index, this
catalogue, the instruments catalogue and the session log index.

```sh
python3 tools/indexscan.py --root . .        # the floor's shape, without --warn
python3 tools/indexscan.py --json --root . .
python3 tools/indexscan.py --selftest
```

Exit codes: `0` clean, or findings under `--warn` · `1` an `unlisted` entry, a
`missing-dir` (the declared directory is gone), a `date-mismatch` or a
`stale-allow` · `2` a
malformed or unknown-key declaration, a `dir=` escaping the root, a bad
`before=` date, an unreasoned ignore glob, a path that does not exist — never
downgraded by `--warn`. **What it cannot see**: whether a listed entry's line
is *true* about it beyond the date rule above (a line's slug, or a date that is
wrong in the later direction, passes); an index that is not Markdown (a YAML
manifest); a name mentioned only in bare prose without a link or code span.
The converse is loose by design: **any** link or code span naming an entry
counts as listing it, wherever it sits in the index — a passing mention is
indistinguishable from an entry.

## `stampscan.py` — an inlined copy still equals its canonical parent (advisory)

Where a child repo or a template **inlines** a floor or a pull-quote of canonical
doctrine, the copy must equal its parent — or *legitimately narrow* it, declared
— never silently drop or contradict an item. The corpus paid for this class three
times before there was a scanner: `create-repo` C3 (nothing kept the stamped block
equal to PROPAGATION's canonical text), `method-layer` P1 (an inlined floor
silently dropped "new trust surfaces"), `foundation` Q2 (a pull-quote listed 4 of
6 floor items) — each caught by a human reading two files side by side.

The mechanism is a marker pair. The parent names a **region** with
`<region>:begin` / `<region>:end` HTML comments; the copy wraps itself in
`stamp:begin source=<path> region=<name>` / `stamp:end`. Both are HTML comments,
so stamping changes nothing visible. The convention itself is doctrine and lives
in [`docs/method/PROPAGATION.md`](../docs/method/PROPAGATION.md), beside the one
region it declares — including who may declare a `narrow=` (the child, with a
written reason) and the rule that **narrowing to nothing is drift**, not a narrow.

**Markers are recognised only outside fenced code and inline code spans**, like
every sibling scanner. That is not a nicety: a stray marker is a config error,
`--warn` never downgrades one, and before the fix any document that merely
*documented* this syntax reddened the whole floor — which is why the scanner sat
unwired for two weeks (2026-07-26 cold pass ST1). The named residual is a raw,
line-start marker in bare prose, which is indistinguishable from a real one;
rendered Markdown hides raw HTML comments, so genuine documentation uses a code
span anyway, and `.stampscanignore` nets the stores that quote probe material raw.

```sh
python3 tools/stampscan.py --warn --root . .   # the advisory CI invocation
python3 tools/stampscan.py --root . docs       # docs only, gating
python3 tools/stampscan.py --json              # machine-readable
python3 tools/stampscan.py --require-stamps --root . .   # fail if nothing was verified
python3 tools/stampscan.py --require-floor-stamp --root . .   # fail unless the floor stamp was
python3 tools/stampscan.py --selftest          # prove the engine offline
```

`--require-stamps` is the cover switch, modelled on `leakscan --require-terms`.
Without it a tree with no stamped block prints
`✓ stampscan clean — no stamped blocks found.` and exits 0, which a reader cannot
tell from "checked and clean". With it, a run that verified no stamped block
(none found, or only allow-marker skips) exits `2` with a stderr message naming
what was missing. **What it certifies is "at least one stamped block of any kind
was compared", not "the floor is stamped"**: a tree whose floor copy carries no
marker passes it while any unrelated stamp is present (cold pass `160/430`,
CU1). `--require-floor-stamp` is the switch for that claim: it exits `2` unless
a compared block names the floor pair (`source=docs/method/PROPAGATION.md
region=floor`), so an unrelated stamp cannot stand in for it. It fails closed
and is deliberately literal: a floor stamp spelling the source path another way
reads as no floor stamp. Under `--json` an unmet demand still prints the
document, with `clean: false` and `require_stamps_unmet` set to
`no-stamped-block` or `no-floor-stamp` (`null` otherwise). Drift (`1`) and
config errors (`2`) are reported as before. Both switches are off by default,
so the advisory invocation is unchanged, and nothing wired passes either of
them yet.

Exit codes: `0` clean, or `--warn` with drift findings only · `1` drift, without
`--warn` · `2` usage/config error — a malformed stamp, an unresolvable source or
region, or a `source=` resolving **outside** `--root` (traversal and absolute
paths both escaped before; a crafted stamp could aim the scanner at any file on
the machine and get a line of it echoed in the drift hint). A config error is
**never** downgraded by `--warn`. Escape hatches: `stampscan:allow: <reason>`
anywhere inside a stamped block exempts that block; a path glob in
`.stampscanignore` exempts a file from being scanned for stamps of its own
(it stays usable as a canonical `source=` target).

**Wired advisory in atelier's own `ci.yml` only** — deliberately *not* in the
`floor.py` registry, which would reach every child at once (ADR 0008). The
template ships a stamp pinned at `source=docs/method/PROPAGATION.md`, a path that
exists only here, so a scaffolded child running it would exit 2; the child-side
resolution story also has to be **pin-aware**, since a child pinned at
`atelier@<SHA>` may lawfully differ from atelier@main. That is ST3, still open.

## `memprobe.py` — measuring a guard's real peak memory from outside it

Not a floor check, not a scanner — a small harness (020/370) other tests build
on. `tracemalloc` only sees Python-heap allocations, missing C buffers,
`mmap`'d regex tables, and OS baseline — none of which is the number that
matters when a guard is thrashing a real machine. `run_and_measure(argv, …)`
runs a guard as a **subprocess** and reads its peak RSS back from the kernel
via `os.wait4`, the same number `/usr/bin/time -l`/`-v` reports, normalised to
bytes across macOS (`ru_maxrss` in bytes) and Linux (`ru_maxrss` in KiB).
Optional `timeout` and `rss_limit_bytes` kill a runaway child rather than
letting a bad measurement become a repeat of the incident that motivated
building this. **By default the measurement runs one level down**, in a fresh
minimal interpreter: a forked child inherits its parent's page accounting on
Linux until it `exec`s, so measuring from a fat caller read the *caller's*
footprint back as the child's — `python -c pass` measured 187 MB on a CI
runner, and a test that wrote a large input grew its own baseline with the
input size, which is exactly the signal being measured. macOS spawns rather
than forks, so none of this showed locally. `isolated=False` measures from
the calling process and is kept for testing this module's own mechanics. See `tools/test_secretscan.py::BoundedMemory` for the pattern
every guard in `020/380` is meant to reuse: build a small and a larger
synthetic input, measure both, assert the growth is under a bound derived
from the guard's own design (never from today's measurement).

## `blockscan.py` — a ruling that moves doctrine moves the child block too (advisory, atelier-only)

`stampscan` checks a **child's** inlined copy of the floor block against
atelier's own region — drift once the block has already moved. Nothing checked
the other direction: does atelier's *own* region still say what the method docs
it summarises actually say, right now. A 2026 ruling reworded the ask rule in
`COMMUNICATION.md`; the floor region and the scaffold template both kept the
overturned wording for weeks and copied it into every child at pin bump.
`blockscan` is the check that closes that gap (board `320/300`, Mike's ruling
2026-09-19: *"Build the check"*).

**The map, not a stored hash.** [`tools/blockscan_map.json`](blockscan_map.json)
is a small, hand-maintained table: each floor-region bullet that cites a source
doc gets a stable id, its own bold lead-in text (the `anchor`, used to find the
*same* bullet in both `PROPAGATION.md`'s region and the template's stamped
copy), and the exact heading(s) it summarises. Six of the floor's nine bullets
are mapped; the other three (**Source & drift**, **Estate resources**, **This
repo's visibility**) cite no doc section at all in their own prose, so mapping
them would be inventing a citation, not checking one — see the map's own header
comment and the module docstring for the full accounting.

**The rule (staged plane, no hashes, no section-text diff against a stored
baseline):** if a commit changes lines inside a mapped section, it must ALSO
change the corresponding bullet in *both* the region and the template, or carry
`<!-- blockscan:allow: <reason> -->` somewhere in the changed section or either
bullet. A section is **non-recursive** — it stops at the *next heading of any
level*, not just the same or a shallower one, so (say) `00-APEX.md`'s `##
Honesty is absolute` and its own `### The principal's authority...` subsection
are two separate mapped targets, each answering to the one bullet that actually
cites it, rather than one edit echoing onto every bullet in the file.

Three run modes:

```sh
python3 tools/blockscan.py --staged --root .        # the hook plane: HEAD vs the index
python3 tools/blockscan.py --against HEAD^ --root . # the CI plane: HEAD vs its parent
python3 tools/blockscan.py --check --root .         # map-integrity only, no git needed
python3 tools/blockscan.py --selftest
```

`--check` (also the default with none of the three given) verifies ONLY that
the map still resolves — every mapped heading to exactly one line, every bullet
anchor to exactly one bullet in both files — and is what a renamed or duplicated
heading reds against: a `stale-heading`/`missing-bullet` finding is a **config
error**, never suppressible by the allow marker, because a map that cannot find
what it claims to map must fail loudly, not quietly pass on a wrong assumption.

**Unmapped headings (board `320/340`, advisory).** Sections are extracted
non-recursively, so an edit to a *subsection* of a mapped section is invisible
to the co-change rule. `--check` therefore also lists every `##`-or-deeper
heading, code fences excluded, in a doc the map names as a source that no map
entry accounts for, labelled `under mapped <heading>` when it sits beneath a
mapped section (the sharp case). Human output lists only those in full and
collapses the rest to one count line (`+ N other heading(s) no bullet cites
(--json lists them)`; it counts every other unmapped heading, including a `###`
under an unmapped `##`); `--json` keeps every finding. It is a report
only: exit code, the `clean` field in `--json` and the `--staged`/`--against`
planes are unchanged (it appears as `unmapped` findings in `--json`), and it is
skipped while the map is stale. Mapping or leaving a heading is still a
human call. **What it does not see** (160/430, CU5): the body under a doc's `#`
title (every mapped doc has one, a few non-blank lines, and the co-change rule
cannot see it either), a fenced presentation of the floor in `PROPAGATION.md`,
setext or indented headings, and a second `#`; and it runs under `--check`
only, so a subsection-only edit passes `--staged` and `--against` unremarked.
Fences pair by the shared rule (a bare closer of the same character, at least as
long), and heading text and map paths are printed with control and bidi
characters escaped. A map `path` that resolves outside `--root` is a config
error (exit `2`).

Exit codes: `0` clean, or `--warn` with violation findings only · `1` a
co-change violation, without `--warn` · `2` usage/config error — a malformed
map, an unresolvable region/template/source file (or one resolving outside
`--root`), a stale heading, a missing bullet anchor, a `git show` failure (never
downgraded by `--warn`).

**Deliberately NOT in `tools/floor.py`'s registry — the same ST3 class as
`stampscan`, and worse: every path this map names exists only in atelier**
(`00-APEX.md`, `COMMUNICATION.md`, `CONCURRENCY.md`, `ECONOMICS.md`,
`RECORD.md`, `PROPAGATION.md`, the scaffold template). A registry line would
reach every child's hook and CI (they run atelier's own `floor.py`, not a
vendored copy) and exit 2 — fail-safe, never downgraded by `--warn` — on their
very first mapped path, from the commit this merged. What's wired instead is
two bespoke steps in atelier's own `ci.yml`, `--check` and `--against HEAD^`,
matching `stampscan`'s precedent exactly. **One residual, named rather than
hidden:** neither of those runs from this repo's actual pre-commit hook —
`.githooks/pre-commit` deliberately names no scanner (ADR 0008) and calls only
the shared registry, so a co-change violation is caught one push later by CI
(`--against HEAD^`), reported but not blocking, rather than at commit time.
Closing that gap needs a hook-plane, atelier-only, not-in-the-shared-registry
seam that `floor.py` does not offer today — see the module docstring, WIRING
RESIDUAL, for the two ways to close it and why this build takes neither
unilaterally.

## `signscan.py`, `signfleet.py`, `floorfleet.py` — the signing gate and the fleet views

Three tools whose doctrine lives elsewhere, listed here so this catalogue is
complete. Each module's docstring is its full manual.

- **`signscan.py`** verifies git commit signatures over a range against a trust
  list. It is the CI and hook half of `docs/method/SIGNING.md` (ADR 0007), and it
  runs `--warn` fleet-wide.
- **`signfleet.py`** answers for the whole fleet whether the signing gate would
  pass if it were enforcing. It runs `signscan` in blocking mode against every
  child, each resolved the way that child's own CI resolves it.
- **`floorfleet.py`** answers whether every repo in the estate is actually
  running atelier's floor. It enumerates conformance rather than assuming it
  (ADR 0008; `docs/method/PROPAGATION.md`).

## `local` in `.atelier-floor.json` — a repo adds a check of its own

The hook set is atelier's, and that reads as "a child cannot add one". It can: a
`local` block in the repo's `.atelier-floor.json` names a script the repo ships,
and the floor runs it on the planes you choose, in the same hook and the same CI
that already run the shared checks. Reach for it before filing a hand-up for
"wire my checker into the hook" (the seam is older than most such requests).

```json
{
  "local": {
    "config-loads": {
      "run": "tools/check_config.py",
      "why": "a duplicate key in the service config must never be committed",
      "planes": ["hook"],
      "args": ["--staged", "--root", "{root}"],
      "scope": ["config"]
    }
  }
}
```

- **Keys.** `run` (repo-relative, inside the repo, invoked directly, never
  through a shell) and `why` (one line) are required. `planes` defaults to both
  `hook` and `ci`; hook-only is legitimate for a check CI cannot run, such as one
  that needs a machine-local list or a library CI does not install. `args` takes
  the same `{root}` templates as the shared checks, and `scope` narrows the tree.
- **It only adds.** A local name that collides with a shared scanner is a config
  error, so the seam cannot replace or weaken a fleet check. Softening one of your
  own checks uses the ordinary `advisory` / `disabled` keys.
- **It fails closed.** A declared script that is missing blocks, as a missing
  shared scanner does.
- **It is visible.** Local checks show in `floor.py --list`, in `--json`, in the
  render (tagged `local`) and on the `floorfleet` board.

The full contract is the docstring of `tools/floor.py` (§ *The repo-local seam*)
and the `.atelier-floor.json` bullet in `docs/build/REPO-STANDARD.md`. Check the
hook with `python3 tools/floor.py --list --plane hook`, then stage a deliberate
defect and watch the commit block.

## `report.py` — the shared exit-code contract and report lines

Not a check. Fourteen floor scanners import it for the parts of their output
that were the same everywhere (`115/080`, part 3). It holds the exit codes (0
nothing blocking, 1 blocking findings, 2 the scan itself is broken), the
wrapper that turns a config error into exit 2, and the exit-2 stderr lines (a
missing root, a missing path, an unreadable file, a failed `git diff`, an
absolute `--staged` path). It also holds the `✓ <name> clean — …` and
`✗ <name>: N …` heads, the `suppressed:` tally line with its allow-marker
breakdown, the finding-cap lines, and the `(--warn: advisory only …)` notice.

<!-- exitcodes:begin -->
**The exit-code contract, stated once** (`160/730` RT10; the per-scanner
sections below point here and add only what is theirs). `0`: nothing blocking,
meaning clean, only advisory or report-only findings, or `--warn` given. `1`:
blocking findings. `2`: the scan itself is broken and cannot be trusted, meaning
a usage or config error, a missing root or path, a file it could not read, a
failed `git diff`, an ignore glob with no reason, or a crash. `--warn` turns `1`
into `0` and never touches `2`: a broken scan is not a pass.
<!-- exitcodes:end -->

Every difference between scanners is a parameter: the scanner's name, its
tally fields in its own order, the finding noun, the tail of a head line. None
is a shared default. Lines that genuinely differ stay in their scanner:
`leakscan`'s clean head, `indexscan`'s over-cap line, and the `⚠` heads of the
advisory checks. `pointerscan.py` and `board.py` keep their own copies for now.

It also reads git's path output (`115/260`). git C-quotes a path holding a
non-ASCII byte, tab, newline, double quote or backslash, so a parser that
expects a bare path misses the file. `nul_paths` reads `-z` output (the raw
path; `board.py`, `harvestscan.py`). `diff_header_path` and `unquote_c` read
the `+++` header of a staged diff, which has no `-z` form.

The same three guards read the staged diff through one function,
`staged_added` (`115/280`). It follows the diff's structure, not its look: a
file header is only what git writes between `diff --git` and a file's first
`@@`, and a hunk's `@@ -a,b +c,d @@` counts say where its body ends. An added
line whose own text begins `++ ` prints as `+++ …`, and used to pass for a
header, moving the lines after it to a posed file name. It fails closed: a
diff that does not fit its counts is exit 2, never a guess. Each added line
comes with its real line number in the file the commit produces, and all three
guards report a finding at that line (`115/300`): a marker staged on line 5 of
a file whose lines 1-4 are unchanged is reported at 5, not at its position
among the added lines.

The staged guards read their positionals through one function too (the three
boundary guards, plus `datescan`, `sizescan`, `spellscan`, `reviewscan` and
`wrapscan`): `resolve_staged_scope` (`115/360`, `160/950`). `.` is the whole
diff, `./docs` and `docs//` mean `docs`, and `docs` is the `docs/` subtree,
never `docs-extra/`. Git decides what a positional names (`git ls-files` for
the index, plus the paths the commit removes), so a spelling the filesystem
forgives and git does not (a different case, a decomposed Unicode name) cannot
make the scan cover nothing. These exit 2: an absolute path, one that climbs
out with `..`, one git does not know (a typo, a glob, an unexpanded `~`, a
directory the repo lacks), and a `--root` that is not the repo the process runs
in (the staged diff is always the current directory's). A tracked directory the
commit does not touch is not refused: that is a commit outside the scope.
`leakscan` judges its positionals once and cuts all three of its path lists by
the answer.
`test_report.py` tests each helper and pins each converted scanner's lines as
literals. What a scanner prints reaches every child's CI at its next run, so a
shared edit that changes one of those lines fails the suite first.

**Finding IDs.** Nine scanners end each finding line with a namespaced ID,
`<scanner>:<kind>`, and give each `--json` finding an `id` field (`sizescan`,
one finding per file with up to two kinds, gives an `ids` list). The kind is
exactly the scope that scanner's allow-marker accepts, so the ID copies into
the narrowest marker there is:

```text
  a.txt:1  [high/structural] email → a.b…nz (17 chars)  [leakscan:email]
  a.md:1  [us-spelling] 'color' → 'colour'  [spellscan:color]
```

`leakscan:email` becomes `# leakscan:allow:email: <reason>`. The kind is a
rule name in `secretscan` and `leakscan`, the word in `spellscan`, and the
finding's kind in `linkscan`, `datescan`, `pathscan`, `licenscan`, `sizescan`
and `pointerscan`. A finding with no line to carry a marker (a hit in a path
name, a missing LICENSE, an `--expect` mismatch) still gets an ID. The rest of
each line, and every exit code, is unchanged (`115/080`). `conflictscan`,
`wrapscan` and `indexscan` print none: their marker takes no scope, so there
is no kind a marker could name. `reviewscan`, `publishscan` and `harvestscan`
have no per-finding kind either.

## `anchoredrx.py` — linear-time stand-ins for three greedy-run regexes

Not a check. Three rules each open with a greedy character class that must be
followed by a literal: `leakscan`'s `email` (`[A-Za-z0-9._%+-]+@…`),
`secretscan`'s `basic-auth-url` and its `URL_RX` carve-out
(`[A-Za-z][A-Za-z0-9+.-]*://…`). The regex engine restarts the class run at every
word boundary and scans to the end of the run before it fails on the literal, so
a line of short boundary-rich runs (`1-1-1-`, `sk-`, `eyJ.`) cost O(n²): about
twenty-two minutes for a 1 MiB line, in a blocking hook (cold pass `160/720`,
GT1). The gates skip the rules on lines without the literal; one trailing `@` or
`://` reopened the path.

`AnchoredRx` keeps the original compiled pattern as the single statement of
what matches, and tries it once per maximal run, at the first position that
satisfies the pattern's own start condition (`\b`, or `\b` plus a letter) at or
after the previous match. It yields the same match objects in the same order;
`test_anchoredrx.py` proves that against the originals on a fuzzed corpus
including adjacent matches, and proves the cost grows 4x for 4x the line. It is
the stand-in for a possessive quantifier that the Python 3.9 floor does not
have, and would not be enough anyway: the restarts, not the backtracking, are
the cost.

**A gate is declared on its rule.** `Pattern.gate` in `leakscan` and
`secretscan` is the rule's cheap necessary condition (`110/130`, lever 4),
written beside the regex it conditions, so widening the regex and re-reading the
gate are one diff hunk. `GATES` / `NAMED_GATES` are derived from the rules and
are the one table the scan loop and the shadow spans read. The suites prove
every gate necessary against a corpus **generated from each rule's own regex**
(`test_support_regex.py`: one line per alternative of every alternation), not
only against a hand-kept list; and that no gated rule is case-insensitive unless
its gate is flag-aware. `test_scanner_rules.py` pins the three rules the two
scanners copy (`private-key-header`, `aws-access-key-id`, `jwt`) to each other,
declaring the one intended difference, and runs every rule table through
boundary-rich lines at two sizes: the control shape for this defect class, which
had been found three times by hand. A regex known to be quadratic and not yet
fixed is listed with its reason (`pathscan`'s scheme-URL pattern, `BP9`), and the
test fails when the entry has become linear.

The speed figures in `CHANGELOG.md` for the gates (about 3x for `leakscan`, 4.6x
for `secretscan` on a 50 MB corpus) were measured once on a corpus that is not in
the repository; the equivalence claim re-runs, the speed figure does not. A
future figure names its corpus shape or ships a generator.

## `filewalk.py` — the one file walk every scanner shares

Not a check. Every tree-walking scanner calls `walk_files(base, skip_dir_names)`
for the files it reads (`115/080` part 1, `110/110`). **Inside a git work tree
it streams `git ls-files -z -t --cached --others --exclude-standard`**: tracked
files plus untracked files that are not ignored, which is everything that could
be committed. A gitignored file can never be committed, so not reading it loses
no protection (one repository went from 15.8 GB walked to its 132 MB tracked).
Anywhere else (no repository, the root itself ignored, git missing or failing)
it falls back to `os.walk`, pruning in place. Each scanner passes its own
skip-name set, and a directory whose `.git` is a file (a linked worktree or an
initialised submodule) is always pruned. A nested plain clone is walked with
`os.walk`, so its content is still read.

What the walk guarantees, and what it does not (cold pass `160/600`):

- **Tracked files are read even under a skip name, for the three boundary
  guards** (GW1). `secretscan`, `leakscan` and `conflictscan` pass
  `read_tracked_under_skip=True`, so a credential committed at `.vscode/…`,
  `venv/…` or `node_modules/…` no longer passes the whole-tree plane while the
  staged plane catches it. The skip names then apply to untracked entries and
  nested walks only. Every other scanner keeps its skip contract unchanged: a
  prose or licence check has no business reading vendored output.
- **A yielded path never has a symlinked parent directory** (GW4). Git can index
  `d/f.txt` while the worktree has `d` replaced by a link out of the root; that
  file is not read.
- **Scanning does not run what the tree names** (GW5). Every git call runs with
  `core.fsmonitor=false`, because a repository's own `.git/config` can name a
  command for it and `ls-files` would run it. Git itself still parses that
  tree's index and config.
- **A fallback that hides a failure says so** (GW2). Git reporting "no
  repository" is the ordinary case and is silent. Git failing for a tree that
  carries a `.git` entry (dubious ownership, a corrupt `HEAD`) prints one stderr
  line and records `os.walk:git-failed` in `LAST_MODE`, because the wide walk
  reads the ignored files again and the result would otherwise change with the
  machine.
- **No git call has a timeout** (GW8). A hung git hangs the guard; it stops, it
  does not pass.
- **It answers "which paths", not "which content"** (GW10). At the hook a
  staged-then-deleted file is committed unread and a file whose worktree copy
  differs from its staged copy is read in the worktree version. The boundary
  guards avoid this with `--staged`.
- **A nested clone's own ignored files are read** (GW9), deliberately.

The per-scanner ignore files (`.leakscanignore` and its siblings) may still
carry globs for nested worktrees that git mode already drops; they are harmless.
`linkscan`, `reviewscan` and `pointerscan` still walk with their own code, so
"guards stop reading ignored trees" is not yet true of them (GW7, tracked on the
board with the earlier `FW7`).

`test_filewalk.py` holds a shape matrix: one repository with every shape the
modes could differ on (tracked, untracked, ignored, force-added past an ignore
rule, deleted but cached, symlinks, a nested clone, a linked worktree, skip
names) and the expected set written out.

## Tests

```sh
cd tools && python3 -m unittest      # stdlib only, no pytest — covers every tool here
```

The tools themselves run on Python 3.9 and later, but the **tests need 3.11 or
later**: the G3 git-plane tests (`BinaryGitTracking`) use `contextlib.chdir`,
`test_allowmarker` uses `Path.write_text(newline=)` (3.10), and `test_floor`
uses 3.10 type syntax. CI pins 3.12. Under macOS's system `python3` (3.9) those error,
which is the interpreter and not a bug in the tools.

## `coldsweep.py` — the cold reviewer's tree search, with rule 2's bar built in

**Not a floor check and deliberately not in the registry.** It gates no commit
and returns no verdict — it is a reviewer's instrument, and its value is being
the easiest way to search at the moment a reviewer wants to.

`REVIEW.md` rule 2 bars a cold reviewer from the author's records: the session
log, the session records, the harvested board, prior verdicts. Reviewers were
told to exclude those paths and tried to. **Three recorded times the exclusion
silently did not apply** — most often a pattern assuming a `./` prefix that
`grep -r <dir>` does not emit, so the exclusion matched nothing and the sweep
ran wide open. In the worst instance a reviewer held a prior verdict's findings
before writing its own. The rule was restated after each instance; three
instances in, the principal ruled for a guard instead (2026-08-17).

**Why it does not shell out to `grep`.** The defect was never in the reviewer's
care — it was in matching a path by string prefix against output whose prefix is
a platform detail. This walks the tree with `pathlib` and filters on the
relative path **parts**, so `./docs/sessions`, `docs/sessions`, `docs/sessions/`
and `docs//sessions` all bar the same files, and `docs/sessions-archive/` is not
swept up by any of them. Both directions are pinned by tests.

Every run prints the exclusion set it used, in a form that pastes straight into
a verdict's provenance. `--include-barred` is the exception and prints a banner:
under rule 2 a wide sweep is not forbidden, an **undisclosed** one is.

```sh
python3 tools/coldsweep.py 'PATTERN'                     # barred set excluded
python3 tools/coldsweep.py -i 'pattern'                  # case-insensitive
python3 tools/coldsweep.py --also-exclude docs/roadmap/160-x 'PAT'
python3 tools/coldsweep.py --list-barred                 # what it would exclude
python3 tools/coldsweep.py --include-barred 'PAT'        # the exception, loudly
python3 tools/coldsweep.py --selftest
```

Exit codes follow `grep` so it drops into a pipeline: **0** matched, **1** no
match, **2** the search itself failed. A broken sweep is not a clean one.
