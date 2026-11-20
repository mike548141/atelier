# 2026-09-11 · 1050 UTC · The shrink refusal, and what it actually compared

**From the retired session log**, word for word; only its link paths were re-pointed for this folder:

<!-- archivecut:log-entry docs/SESSIONS.md 304+1 -->
- [2026-09-11 · 1050 UTC · The shrink refusal, and what it actually compared (Opus 5 1M, main, in place)](2026-09-11-1050-the-shrink-refusal-and-what-it-actually-compared.md) — Mike brought a live `ccarchive` run that refused six files and exited non-zero, backed the guard, and asked why a source is smaller than its archived copy at all. Filed as `210/150`, deliberately separate from `210/010`: that item asks what to do about the class, and its three options all rest on a reading ("legitimately condensed") asserted at discovery and never checked against a mirror. 🔎 **The guard compares the source against the manifest's recorded byte count while the message claims the mirror** — one number only while the two agree, which this path never verifies; so mis-pairing has a second shape, a size record that outlived the copy it described (`370`'s class). Four discriminating hypotheses recorded, all read-only, with a warning that a `--force` run destroys the evidence separating them.


**Session:** Opus 5 (1M context) · `main`, in place · one commit

A short visit. Mike brought a live `ccarchive` run that refused six files and
exited non-zero, backed the guard, and asked the question the guard does not
answer: *why is the source smaller than the archived copy in the first place?*
He named two candidates himself — a mis-pairing of two different transcripts,
or something mutating one end. Recorded, not fixed, at his direction.

## Filed as `210/150`, separately from `210/010` on purpose

`210/010` already carries this guard's non-zero exit, filed 2026-08-09 with
**two** refusals. The hand run showed **six**, every one a per-project memory
`.md` and two of them a memory index, so the class is growing rather than
static. Paths stay unnamed here for the same reason `210/010` left them out:
they identify personal projects and private repos, and this repo is public.

The two items ask different questions, and the order matters. `210/010` asks
what to do about the class, and all three of its options rest on the reading it
took at discovery — that the shrinks are legitimate condensation of whole
documents. That reading was asserted, never checked against a mirror.
`210/150` asks whether the refusal is telling the truth about what it compared.
If the pairing or the recorded size is wrong, `210/010`'s options answer a
question that does not exist.

## What the code says, read read-only at filing

`instruments/ccarchive` compares the source's size against
`manifest[rel].rawBytes` — the **manifest's recorded byte count** — while the
stderr line claims the *archived copy*. Those are one number only while the
manifest and the mirror agree, and this path never verifies that they do. So
Mike's mis-pairing candidate has a second shape he did not name: not two
transcripts confused, but a size record that outlived the copy it described.
This is `370`'s class exactly — the report can be wrong about its own evidence
while the refusal it produced is still the right call.

Pairing itself is by one relative path, used to find both the mirror and the
manifest entry, so a genuine mis-pair needs a key collision or a manifest key
orphaned by a renamed project directory. The layout-drift alarm cannot catch
the latter: it trips only when the walk yields zero sources against a non-empty
manifest, so a *partial* rename passes silently.

## Left in the item for whoever takes it

Four hypotheses to discriminate between — benign condensation,
manifest/mirror divergence, wrong pairing, post-write mutation — all
answerable read-only, plus one warning: do not clear the red with `--force`
first. The overwrite destroys the frozen mirrors, which are the only evidence
that separates those four.
