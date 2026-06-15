Here are user-facing release notes for TaskPilot v2.3. I led with the breaking change (burying it is how you burn trust), then grouped the rest as New / Improved / Fixed with each line framed as what it does for the user rather than what was built. I dropped the logging-library upgrade — it has no user-visible effect, so it belongs in the developer changelog, not the user release notes.

One assumption: I treated this as **user-facing release notes** (curated, benefit-led) rather than a developer changelog (complete, every change listed). If you need the dev-facing changelog version too, say the word — that one keeps every entry, including the logging upgrade, and stays terse.

---

# TaskPilot v2.3

## ⚠️ Breaking change — action required

**The legacy `/v1/tasks` API endpoints have been removed.** If you or your team have integrations, scripts, or automations that call `/v1/tasks`, they will stop working on v2.3. Move them to the `/v2/tasks` endpoints before upgrading. [See the migration guide →](#)

> Not using the API directly? Nothing to do here — this only affects custom integrations.

---

## New

- **Bulk-edit up to 500 tasks at once.** Change status, assignee, due date, or labels across an entire batch in one action instead of one task at a time. [How bulk-edit works →](#)

## Improved

- **Exports no longer time out on large workspaces.** We rebuilt the export pipeline to stream results, so workspaces with 100,000+ tasks now export reliably instead of failing partway through.

## Fixed

- **Edits made on two devices at once are no longer dropped.** We fixed a sync issue that could quietly discard a change when you edited the same work on, say, your laptop and your phone at the same time. Your edits now reconcile correctly across devices.

---

*Questions or issues? [Contact support →](#)*

---

### A couple of notes for you (not for the published page)

- **Links** are placeholders — drop in the real migration guide, bulk-edit doc, and support URLs before publishing.
- **The `/v1/tasks` removal is the one item every user must act on**, which is why it sits at the very top with a clear "what to do." For an API-breaking change, I'd also recommend a heads-up email to workspaces that have hit `/v1/tasks` in the last 90 days, not just release notes — a deprecation users only discover when their integration breaks generates support tickets and ill will.
- If you have a real number for how big the bulk-edit or export improvement is in practice (e.g. "exports that took 8 minutes now finish in under 1"), it'll land harder than the limits alone. Happy to fold one in.
