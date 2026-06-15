Assuming the audience is HN's developer crowd (Postgres users, backend/platform engineers, DBAs) and the goal is trials → GitHub stars/first installs, not signups; adjust if wrong. A Show HN is you talking to peers, so this is written plain, in your voice, with limitations stated up front — no marketing-speak, because that gets shredded on HN. I've left two `[BRACKETED]` spots where a real number makes the post much stronger; drop in the truth or cut the line.

---

## Title

The HN title field is the single most important thing — most readers decide from it alone, and "Show HN:" is required. Keep it concrete and under ~80 chars. Three options, different angles:

1. **Direct / descriptive (recommended):**
   `Show HN: sqlsnap – snapshot and diff Postgres schemas from the CLI`

2. **Problem-led:**
   `Show HN: sqlsnap – git diff for your Postgres schema`

3. **Capability-led:**
   `Show HN: sqlsnap – catch unintended schema changes before they ship`

I'd ship #1. It says exactly what it is, names Postgres (the qualifier HN's audience filters on), and makes no claim the tool can't back up. #2 is catchier but "git diff for X" is a worn HN trope and invites "why not just use pg_dump | git diff?" in the first comment — which you'd rather answer in the body than concede in the title.

---

## Body (the post text)

> Hi HN — I built sqlsnap, an open-source CLI that takes a snapshot of a Postgres schema and shows you a readable diff between any two snapshots.
>
> The problem I kept hitting: schema drift. The schema in staging didn't match prod, a migration did something slightly different than the PR implied, or someone added an index by hand months ago and nobody remembered. `pg_dump` gives you the full DDL, but diffing two dumps by hand is noisy — output ordering changes, comments move, and you end up squinting at a 2,000-line diff to find the one column that actually changed.
>
> sqlsnap does three things:
>
> - `sqlsnap snapshot` — captures a schema (tables, columns, indexes, constraints, sequences, [enums/functions/views — list exactly what's covered]) into a single stable file. Same schema in, same file out, so the snapshots diff cleanly.
> - `sqlsnap diff a.snap b.snap` — shows what changed, grouped by object: added/dropped tables, column type and nullability changes, new/removed indexes and constraints. Exits non-zero when there's a difference, so you can drop it into CI as a guardrail.
> - Snapshots are plain text and meant to be committed, so your schema history lives next to your code.
>
> What it's for: catching drift between environments, reviewing what a migration *actually* did vs. what the PR said, and failing CI when the live schema diverges from what's checked in.
>
> What it's **not**: it's not a migration tool and doesn't generate `ALTER` statements — it tells you what differs, not how to fix it. Postgres only right now. It reads the schema, not data. [If there are known gaps — partitioned tables, large catalogs, specific PG versions — say so here. Honesty about limits earns more trials on HN than it costs.]
>
> Install: `[exact install line — e.g. brew install sqlsnap / go install ... / cargo install sqlsnap]`
> Repo (MIT/[your license]): `[github.com/you/sqlsnap]`
> It's written in `[language]`, runs as a single binary with no dependencies beyond a Postgres connection.
>
> I'd genuinely like feedback on the diff output and the CI workflow — does the grouping match how you'd want to read a schema change, and what's missing that would make you actually put this in a pipeline? Happy to answer anything.

---

### Why it's built this way (notes you can ignore)

- **No hype, limitations stated early.** The HN audience punishes superlatives and rewards candor; the "what it's not" paragraph will do more for credibility than any adjective. I deliberately cut words like "powerful," "seamless," and "effortless."
- **Show, don't claim.** The three bulleted commands *are* the pitch — a reader can see exactly what they'd run. If you have a 20–30 second asciinema/terminal recording of a real diff, link it; for a dev CLI a recording outperforms any paragraph.
- **The CI angle is the hook.** "Exits non-zero, drop it into CI" is the line that turns this from a curiosity into something people adopt, because it names a concrete job. I led the feature list with snapshot but made sure CI landed before the limitations.
- **One real number would lift it.** If you have anything true and concrete — `[diffs a 500-table schema in under a second]`, or `[we caught N drift incidents in our own infra with it]` — add one line. One honest number beats three adjectives. Don't invent one; an unbacked stat is worse than none on this audience.
- **Fill the brackets before posting.** The install line, repo URL, language, license, and exact object coverage are the things HN readers check first — vagueness there reads as concealment. Precision is the whole game with this crowd.

**First-comment prep:** have a ready, non-defensive answer to "why not `pg_dump | diff`?" (stable ordering, object-grouped output, non-zero exit for CI) and to "what about [Flyway/Liquibase/Atlas/migra]?" (you're a read-only drift detector, not a migration engine — name where you overlap and where you don't). The thread lives or dies on how you handle the first three comments.

**Timing:** Show HNs do best posted weekday mornings US Eastern (roughly 8–10am ET). Post when you can sit with it for the next 3–4 hours to reply quickly — engagement in the first hour drives the rest.
