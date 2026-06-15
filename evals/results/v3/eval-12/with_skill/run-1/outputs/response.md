Here's a commit message following the Conventional Commits format:

```
refactor(auth): convert session middleware to async/await

Rewrote the auth middleware to use async/await instead of callbacks
and removed the callback-based session handler. This flattens the
control flow, improves error propagation via try/catch, and removes
the now-unused callback path.
```

If your project doesn't use Conventional Commits, a simpler version works too:

```
Refactor auth middleware to async/await

Replace callback-based session handler with async/await for clearer
control flow and error handling.
```

A couple of notes:
- I used the `refactor` type since this is a behavior-preserving internal change. If the refactor also fixes a bug or changes behavior, consider `fix` or `feat` instead.
- If removing the callback-based session handler is a breaking change for anything that imported it, add a `BREAKING CHANGE:` footer describing the migration.
