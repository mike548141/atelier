# 2026-09-09 · 0257 UTC · The credential that already existed, and the PDF that still would not open

**Session:** Opus 5 (1M context) · worktree `at-ccmail2`, branch
`feat/ccmail-delegation` off `origin/main` · continues
[the ccmail build](2026-09-09-0005-ccmail-the-attachment-a-session-could-name-but-not-open.md)

## What Mike said

He ran `ccmail --auth` and stopped at the first prompt:

> "I ran this and its asking for details you should either already have
> accessible in the shed repo or be able to access using credentials in the
> shed repo"

He was right, and the check that would have found it was **reading the estate
registry before offering to build**. The earlier session went straight from
"the connector cannot fetch attachments" to "here is how to mint a credential",
and never asked what the estate already held.

## What was already there

| Fact | Evidence |
|---|---|
| A Workspace identity with `gmail.readonly` | 9 read-only scopes, delegation registered **2026-07-29**, verified end to end at the time |
| It is **keyless** | No key exists; reached by impersonation. Built that way *because* a key file had gone wrong on this estate before |
| The Gmail API is already enabled | On the estate automation project |
| Tooling to reach it already written | The estate's own delegate module |

So the console work was **entirely unnecessary**. Choosing this route grants
nothing that was not already granted on 29 July.

## The ruling this corrects

The earlier choice was put to Mike as personal-grant *versus* domain-wide, and
the case against domain-wide included *"its password is a file sitting on your
Mac"*. That was **false here**, and it was the deciding sentence. Re-briefed on
the real picture, he ruled for **both, delegation first**, and added a standing
constraint in his own words:

> "credentials, secrets etc must be stored in the shed repo which uses things
> like Apple keychain, [SOPS]+age, openbao etc"

⚖️ **The method lesson is the load-bearing one, not the fact.** The wrong option
was nearly taken because the *brief* was wrong, not because the ruling was. An
approval extracted on a wrong fact still stands as the principal's word — it is
challenged by **re-briefing**, never voided quietly — and raising that challenge
is the agent's job.

## What landed

**`ccmail` now has two routes, tried in order.** Delegation first — impersonate,
`signJwt`, jwt-bearer exchange, a token that lives in memory for one run and
adds **no credential to the estate at all**. The stored grant is the fallback,
and it is still owed: the delegation depends on a cloud login that lapses (six
transcript hits since July), and an instrument promising "any session, any repo"
cannot be dark for a day.

- **The plaintext-file fallback is removed**, not deprioritised — a fallback
  that lowers the bar is reached exactly when something else has already gone
  wrong. Off macOS `ccmail` refuses to store and names the estate's real stores.
- **When both routes fail, both reasons are reported.** "Not set up" and "your
  cloud login lapsed" need different hands.
- **`--status` reports every route**, live or not, because a preferred route
  that has quietly stopped answering is the state that ends in a surprise.
- Estate identifiers live in machine-local config, never in this public repo.

**`ccpdf` — because the attachment still would not open.** Six valuation PDFs
fetched from a real message, all valid, and **every read failed**: Claude Code's
file reader renders PDF pages through poppler's `pdftoppm`, and this machine has
no package manager and so no poppler. A file downloaded and still unopenable is
the *same* gap one step further along. `ccpdf` is ~120 lines of Swift on macOS's
own PDFKit — no runtime dependency — installed as `pdftoppm` because that is the
name the reader looks up. Its `setup` refuses to shadow a real poppler and
prints its own uninstall.

## Verified end to end, not inferred

- ✅ `--status` live via the delegation route, reading the real mailbox.
- ✅ Six PDFs fetched from a real message; `file` confirms all valid.
- ✅ **Two of them rendered and actually read** — the first time this session
  could open an attachment rather than name it. That is the whole commission,
  discharged.
- ✅ 26 tests, `mandoc` lint clean, hook-plane floor exit 0.

## Two more defects, both silent, both caught by a selftest

🔎 `ccpdf` emitted **PNG for every format flag**, so it wrote `page-1.png` while
the reader looked for `page-1.jpg`, found nothing, and reported *the document* as
invalid. Everything about that failure pointed at the PDF instead of the tool.
The selftest now asserts on the **filename**, not on "some output appeared", and
the call shape it tests was **observed** from the reader rather than guessed.

🔎 poppler's `-aa` **takes a value**; treating it as a bare switch left `yes`
loose to be read as the input filename, so the renderer reported "could not open
yes as a PDF". Value-taking flags are now an explicit list.

⚖️ That is **five defects across this commission, none found by using the tool**
— three by re-reading, two by a selftest written to be adversarial about
filenames. The standing pattern from the first session holds and has now
extended: every one sat in a thin layer between this code and something else —
a URL, a subprocess, an event loop, a filename convention, a flag table.

## Also captured this session, at Mike's request

The `ccgrab` webinar-capture work from a parallel session was checked and is
**properly captured**: board item `210/140`, its own session record, and a
detailed machine-local memory. One real gap found and closed — that memory sits
in a *single project's* memory directory, so no session in any other repo could
see it, which defeats the "use it from any repo" intent. A pointer now lives in
the machine-local global instructions alongside `ccmail`'s. `ffmpeg`, `ffprobe`
and `yt-dlp` verified present and working.

## Owed

🎯 **Mike:** nothing for the mail path — it works now, with no setup. Two things
remain his call: whether to keep `ccpdf`'s `pdftoppm` (installed during testing,
disclosed rather than assumed), and `gcloud auth login` whenever the delegation
route reports a lapsed login.

📋 **Not done here, deliberately:** no `shed` edit. The delegation route creates
**no** credential, so there is nothing new to register; if the Keychain fallback
is ever minted, that registration belongs in a `shed` session, not this one.
