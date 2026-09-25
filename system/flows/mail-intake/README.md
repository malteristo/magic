# Flow: Mail Intake

Read new practice-relevant email into the private workshop without making the
Mage copy and paste it.

**Invocation:** `@mail-intake`  
**Automatic reader:** professional arrival (`.` / `. craft` / named craft-lane), when `desk/config/mail_intake.json` exists  
**Full procedure:** `cast_mail_intake.md`

The flow is deliberately read-only. It discovers candidates from exact grants
and a Mage-controlled Gmail label, reads only unseen individual messages as
plain text, and routes attributed deltas into private intention artifacts.
It never sends, drafts, labels, trashes, follows links, or reads attachments.

Instance-specific addresses, thread IDs, routes, and checkpoint state belong in
`desk/config/`. The public template is
`system/config/mail_intake.json.template`.
