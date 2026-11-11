- [x] 🔧 **`ccmail` gains a headers-only read: a message's transport headers (Received, authentication results, DKIM-Signature) fetched without its body, so a mail route can be measured from a mailbox without reading anyone's mail.**

      **Why.** A session measuring an outbound mail route (which hops a
      message crossed, the TLS on each, which domain signed it) needs only the
      headers a receiving server writes. The mailbox connector sessions talk
      to returns whole messages, bodies included; `ccmail` talks to the Gmail
      API directly and can ask for `format=metadata` with a named header list,
      which returns no body at all. Same grant (`gmail.readonly`), no new
      scope, no new credential.

      **Shape.** `ccmail <id> --headers` and `ccmail --search <q> --headers`
      write one private file of transport headers per message and print only
      paths; subjects are not fetched in this mode. Same work-tree refusal as
      `--get`.

      **Done 2026-11-11.** `transportRequest`, `transportText`, `cmdHeaders`
      and `searchIds` in `instruments/ccmail`; three tests (metadata only and
      no subject in the request; hops kept in order and unrequested headers
      dropped; control and bidirectional characters neutralised, so a planted
      line break cannot forge a header); man page and README. Live run: 26
      messages read, every file holding only the seven named headers.
      🚩 **Not reviewed.** It changes no scope and no credential, but it is a
      new read mode on a credentialled instrument; a cold pass waits on the
      principal's Fable approval like the two already queued for `ccmail`.
