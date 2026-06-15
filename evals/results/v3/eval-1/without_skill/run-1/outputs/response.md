# TaskPilot v2.3 Release Notes

Hi everyone — TaskPilot v2.3 is here. This release is all about working at scale and trusting your data: bulk editing, faster exports for big workspaces, and a fix for a rare sync issue. There's also one breaking change for teams using our oldest API — details below.

---

## ⚠️ Action required: legacy v1 Tasks API removed

We've removed the legacy `/v1/tasks` API endpoints. If you have integrations, scripts, or automations that still call `/v1/tasks`, they will stop working as of this release.

**What to do:** Migrate to the v2 Tasks API, which covers everything v1 did and more. See the [v1 → v2 migration guide] in our developer docs, or contact support if you need help identifying which of your integrations are affected.

*If you only use TaskPilot through the app — no custom integrations — no action is needed.*

---

## ✨ New: Bulk-edit up to 500 tasks at once

Cleaning up a sprint backlog or reassigning work just got a lot faster. Select up to 500 tasks and update them in one go — change assignees, due dates, statuses, labels, and more — instead of editing tasks one at a time.

**Try it:** Select multiple tasks in any list view, then choose **Bulk edit** from the toolbar.

---

## 🚀 Improved: Exports that handle your biggest workspaces

Exports now stream data as they run instead of building the entire file up front. If you've ever had an export time out on a large workspace (we're looking at you, 100k+ task teams), this fixes it — exports of any size now complete reliably, and large ones start downloading sooner.

---

## 🛠️ Fixed: Rare sync issue with simultaneous edits

We fixed a rare bug where edits made on two devices at nearly the same moment — say, your laptop and your phone — could conflict, and one of the edits could be lost. Sync now handles simultaneous edits correctly, so changes from all your devices are preserved.

---

## Under the hood

We also upgraded our internal logging tooling, which helps us diagnose and fix issues faster. No visible changes, just a healthier app behind the scenes.

---

**Questions or feedback?** Reach us at support@taskpilot.example or through in-app chat. As always, thanks for building with TaskPilot.

---

*Note for the team before publishing: I assumed the v2 API already exists and has a migration guide — swap in the real doc link. Also confirm where the bulk-edit entry point lives in the UI (I described it as a toolbar action in list views) and adjust the support email/link to the real ones.*
