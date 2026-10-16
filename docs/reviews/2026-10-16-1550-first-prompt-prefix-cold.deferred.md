# Deferred sibling — cctranscript's first-prompt prefix read

**Held under rule 1's split** (`docs/method/REVIEW.md`). Open only after your
phase-1 findings are committed to the brief
`docs/reviews/2026-10-16-1550-first-prompt-prefix-cold.md`. At verdict, fold this
file in below your reconcile and delete it.

Written 2026-10-16 UTC by the Opus brief-writer named in the brief, which authored
none of the delta and forms no finding: the questions below are seeds, a floor
and never a fence.

## Intent record

- `docs/sessions/2026-10-05-1120-queue-run-closes-and-builds.md` — **not opened
  by the brief-writer**. The follow-up commit `72bc6d3` appended to it.

## Prior verdicts on the same surface (named, not opened)

Path greps over `docs/reviews/` for `instruments/cctranscript` name these; none
was opened by the brief-writer:

- `docs/reviews/2026-08-15-1032-cctranscript-search-cold.md`
- `docs/reviews/2026-08-17-1321-plain-reply-repurpose-design.md`
- `docs/reviews/2026-10-03-0357-archive-pool-speedup-cold.md` — by its name, the
  likeliest review of the change that introduced `gunzipHead`

## The pointer's own lens hints

None. The pointer is refs-only (delta, intent record, tier, pass type). Note for
V7 and rule 4's landing = queuing: the pointer was added by `78cc660`, after the
close commit `72bc6d3`, not in the commit that landed the work; that commit's
message says so itself.

## Seeded questions

1. The code comment says the bound "can never change an answer"; the commit
   message discloses that a corrupt mirror whose prompt sits in the intact prefix
   now lists instead of aborting the listing. Both cannot be true as written. Is
   the comment an overclaim (V1), and is the new behaviour the one the tool
   wants?
2. `gunzipHead` inflates with `Z_SYNC_FLUSH` and returns as soon as it has at
   least `want` bytes — it can return far more. For a highly compressible log, how
   large is the buffer the prefix path decodes and then converts to a string, and
   is that ever worse than the whole-file read it replaced?
3. Is a `Z_SYNC_FLUSH` partial inflate always a byte-exact prefix of the full
   decompression — including multi-member files and files with trailing bytes —
   which the "first match is final" argument needs?
4. The 64 KB bound and its justification come from a census of the principal's
   own archive, recorded in a code comment. Is a number fitted to one machine's
   current data a sound basis even for a speed-only bound, and does the comment
   publish anything about the private archive (its size, its shape) that should
   not be in a public file?
5. Do the new tests actually fail against the parent, or do they pass on both
   (pinning only output equality, which the parent already had)?
