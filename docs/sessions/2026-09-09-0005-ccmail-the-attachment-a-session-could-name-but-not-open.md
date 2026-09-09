# 2026-09-09 · 0005 UTC · `ccmail` — the attachment a session could name but not open

**Session:** Opus 5 (1M context) · worktree `at-ccmail`, branch
`feat/ccmail-attachments` off `origin/main` · PR #77

## What Mike asked

> "It has often been a problem that you report to me that you can access my
> gmail to collect info etc but you cant open the attachments. I want to fix
> that, I want you to create a way that any session in any repo can open
> attachments when it access my mailbox. If you see other things limiting us
> working then lets fix those too"

Two asks, and the second is open-ended: close the attachment gap, then look for
its neighbours.

## The gap, located exactly rather than assumed

The Gmail connector's `get_message` returns `attachmentIds` and an `attachments`
array carrying **filename, MIME type and an opaque id** — and the connector's
tool surface has **no call that takes that id and returns bytes**. Confirmed by
reading the tool contracts and then by one live call against a real message: the
listing came back complete, and there was nothing to fetch it with.

So the failure mode is not "Claude cannot see the mail". It is worse and more
annoying: a session reports, **accurately and uselessly**, that a message
carries a valuation PDF and that it cannot open it — leaving every question the
message was actually about unanswered.

🔎 **Grounded, not assumed.** `cctranscript --search attachment --all` over 739
sessions: **64 matched, 216 hits**. Mike's "often" is measurable.

## Shortcuts looked for, and why none existed

Checked before building, because the cheapest fix is the one already on the
machine:

| Candidate | Verdict |
|---|---|
| `RAW` message format (MIME carries attachments inline as base64) | ❌ works, and defeats the purpose — a 2.6 MB message is ~3.5 MB of base64 straight into the context window |
| Mail.app's local store (`~/Library/Mail`) | ❌ does not exist on this machine |
| Existing mail tooling in any `~/.pets` repo | ❌ none |
| `gcloud` credentials already on the machine | ❌ present but expired, and gcloud's client is not approved for Gmail's restricted scopes anyway |

## The decision Mike made

Put to him as one question — how much access, against how much setup:

- **Personal read-only key** ✅ *chosen* — his own OAuth client, one browser
  consent, `gmail.readonly` on his own mailbox only.
- Domain-wide robot account — rejected. He is the Workspace admin, so this was
  genuinely available and needs no consent and never expires; it can also be
  pointed at **any mailbox in the domain** and its key is a file. Convenience
  bought with blast radius.
- Old-style app password — rejected. No console work, but full mailbox access
  with no read-only limit, and Google is retiring them.

## What landed

**`instruments/ccmail`** — zero-dependency Node CLI, capability instrument under
ADR 0006.

- `--auth` (one-time, interactive) · `--status` · `--search <gmail-query>` ·
  `<message-id>` to list · `--get all|N|word|'*.pdf'` to fetch · `--text` ·
  `--dest` · `--json`.
- **Prints paths, never content.** The whole point is that the bytes reach a
  *file*, where the ordinary Read tool opens a PDF or an image perfectly well.
  Returning base64 into the window would recreate the problem in a new place.
- **Refuses a destination inside a git work tree** — `ccarchive`'s guard, same
  reasoning: an attachment is someone else's data and a repo is one commit from
  publication. Filenames sanitised so a careless or hostile name cannot escape
  the directory.
- **`--text`** extracts `.docx`/`.xlsx`/`.pptx` into a sidecar whose own first
  line says it is an extraction and not the document.

**ADR 0006 gains a third addendum** — this is the layer's **first instrument
holding a credential to a third-party account**. Every one before it read local
files or drove a program that already held its own sessions. The four controls
that make it acceptable are recorded there rather than left implicit.

**`docs/roadmap/210/120`** — the neighbour found while building: Drive's
`download_file_content` returns binaries as base64 into context, the same shape
`ccmail` just closed. Filed with its evidence grade stated as **read from the
tool contract, not measured**, and deliberately not probed — confirming it costs
exactly the thing the finding is about.

## Verified, and how

- ✅ 22 tests green. The Office extractors run against **genuine ZIP containers
  the test writes itself** — a fixture only our own parser accepted would prove
  nothing about the format. The network surface is **deliberately unmocked**: a
  mock of an API this thin proves only that the mock matches the code.
- ✅ `mandoc -T lint instruments/man/*.1` — clean, no output.
- ✅ Hook-plane floor exit 0, leakscan and secretscan enforced, on the real
  files.
- ✅ **Keychain round-trip proven, not assumed.** A prior session's transcript
  contained "cannot read a keychain item", which would have sunk the credential
  design, so the exact `security add-generic-password -T /usr/bin/security` /
  `find-generic-password -w` pair was run from a Claude Code shell: writes,
  reads back, no dialog. This also matches `shed` ADR 0001, which already puts
  estate secrets in the login keychain.

⚠️ **Not verified, and cannot be from here:** the live Gmail round trip. It needs
a credential that does not exist until Mike runs `--auth`, which needs a terminal
and a browser. Everything up to the API boundary is tested; the boundary itself
is honestly untested and says so in the test file's own header.

## Caught in flight

🚩 A real Gmail **message id from Mike's mailbox** went into the man page's
EXAMPLES section. atelier is public. Replaced with a placeholder before the
first commit — the scanners would not have caught it, since an opaque id trips
no term list.

## The other limits, and where they sit

Only one of the two neighbours is atelier's to fix:

- **Drive binaries** — filed as `210/120` above.
- **`gcloud` credentials expire and block non-interactive sessions** — six
  transcript hits across `shed` sessions between 2026-07-23 and 2026-08-05, and
  live again today. Estate work, not atelier's, and a Mike action
  (`gcloud auth login`). **Not filed here**, per child-repo work locality.
- **Mermaid Chart connector unauthorised** — noted, low value, since artifacts
  render mermaid natively without it.

## Owed

🎯 **Mike:** `ccmail --auth` — the console steps then one browser consent. Until
then the tool is installed and inert, and says so rather than failing obscurely.
Once the grant exists, it should be registered in `shed`'s credential map per
that repo's own doctrine — **in a `shed` session, not from here**.
