Here's a Show HN launch post for sqlsnap. I've written it to follow Hacker News conventions (plain, technical, no marketing fluff), plus a few notes and assumptions afterward so you can adjust before posting.

---

## Title

**Show HN: sqlsnap – A CLI to snapshot and diff Postgres schemas**

(HN title field. Keep it under 80 chars. "Show HN:" prefix is required for the Show HN section. Don't add a trailing period.)

---

## URL

Point the URL field at the GitHub repo (e.g. `https://github.com/yourorg/sqlsnap`), not a landing page. The HN crowd wants to see the code first.

---

## Post body (the first comment you make on your own submission)

> Hi HN — I built sqlsnap, an open-source CLI that captures a snapshot of a Postgres schema and diffs two snapshots to show exactly what changed.
>
> The problem I kept hitting: I'd want to know how a database schema drifted between two points in time — across environments (staging vs. prod), across branches, or before and after a migration ran — and there was no quick way to just *see the diff*. `pg_dump` gives you a wall of DDL that's painful to eyeball, and ORMs only know about the schema they think they manage, not what's actually in the database.
>
> sqlsnap does two things:
>
>   - `sqlsnap capture` connects to a database and writes a snapshot of the schema — tables, columns, types, indexes, constraints, sequences, functions, etc. — to a single deterministic file you can commit to git.
>   - `sqlsnap diff a.snap b.snap` (or diff two live databases) prints a human-readable, structured diff: added/removed/altered tables and columns, changed defaults, dropped indexes, and so on.
>
> A quick example:
>
>     $ sqlsnap capture --db postgres://localhost/myapp -o prod.snap
>     $ sqlsnap capture --db postgres://localhost/myapp_staging -o staging.snap
>     $ sqlsnap diff prod.snap staging.snap
>
>     ~ table users
>       + column last_login_at  timestamptz  NULL
>       ~ column email          varchar(255) -> text
>       - index  users_email_idx
>     + table audit_log
>
> Why I made it instead of using existing tools:
>
>   - It's read-only and doesn't touch your data — it only inspects the catalog, so it's safe to point at production.
>   - Snapshots are plain text and deterministic, so they diff cleanly in git and in code review. You can check schema drift in CI and fail the build if prod and your migrations disagree.
>   - No ORM, no config DSL, no migration framework to adopt. It's one binary that talks to Postgres over a connection string.
>
> It's free and open source under [LICENSE — fill in]. Single static binary, no dependencies to install.
>
> I'd love feedback, especially on: which schema objects you'd most want covered next (I'm weighing RLS policies, triggers, and partitioning), and whether the diff output format is readable enough or should be more machine-parseable (there's a `--json` flag, but the default is the human view above).
>
> Repo: https://github.com/yourorg/sqlsnap
>
> Happy to answer anything.

---

## Why this version

A few things I did deliberately, since Show HN posts succeed or fail on tone:

- **Led with the problem, not the product.** HN readers respond to "here's the itch I was scratching" far more than to a feature list. The middle of the post is the why, not the what.
- **Concrete example output.** The single most effective thing in a Show HN is showing the tool actually doing the thing. The sample diff lets someone understand the whole tool in five seconds.
- **Pre-empted the obvious objection** ("why not just use pg_dump / your ORM / [existing tool]?"). On HN this question *will* be the top comment if you don't address it — so address it in the post.
- **Said it's safe on prod.** "Read-only, inspects the catalog only" is reassuring and is a genuine differentiator worth stating plainly.
- **Asked specific questions.** Ending with two targeted asks (what to cover next, output format) invites the kind of substantive comments that drive a thread, instead of a generic "thoughts?".
- **No hype words.** No "revolutionary," "effortless," "game-changing." That tone gets punished on HN.

---

## Things to fill in / verify before you post (these are assumptions I made)

I don't have the actual repo details, so I made reasonable guesses. Please confirm or correct:

1. **The exact CLI surface** — command names (`capture`, `diff`), flags (`--db`, `-o`, `--json`), and connection-string syntax. The example must match your real CLI exactly; nothing erodes credibility faster than a copy-paste that doesn't run.
2. **What schema objects are actually covered today** vs. on the roadmap. I listed tables, columns, types, indexes, constraints, sequences, functions — trim to what's true.
3. **Distribution claim** — I wrote "single static binary, no dependencies." If it's actually a Go/Rust binary, great; if it's installed via `pip`/`npm`/`brew`, change that line.
4. **License** — fill in (MIT/Apache-2.0/etc.).
5. **Diff-in-CI claim** — I implied you can fail a CI build on drift. If there isn't yet a non-zero exit code on diff, either add it (it's a small, high-value feature for this audience) or soften that line.
6. **Repo URL and org name.**

---

## Posting logistics (worth getting right)

- **Post the body as the first comment**, not in the text field — for Show HN with a URL, HN doesn't show a text field, so your "here's the story" goes in a comment you add immediately after submitting. (Alternatively, submit with the repo as the URL and put the writeup in the README so it's the first thing visitors see.)
- **Time it for a US morning, Tue–Thu** (roughly 8–10am ET / 5–7am PT) for the most traffic; avoid weekends.
- **Be present in the thread for the first few hours.** Reply fast, concede good points, don't get defensive. Responsiveness from the author is the single biggest factor in whether a Show HN thread stays alive.
- **Don't ask for upvotes anywhere** — it'll get the post flagged.
- **Have the repo ready**: a README with the same example, install instructions that actually work on a fresh machine, and a clear license. The first thing many commenters do is clone it.
