```
refactor(auth): convert auth middleware to async/await

Rewrite the auth middleware using async/await and remove the legacy
callback-based session handler. This flattens the previous callback
nesting, makes the control flow easier to follow, and centralizes
error handling through try/catch rather than error-first callbacks.

- Replace callback-based session handler with async/await
- Propagate errors via thrown exceptions instead of callback args
```

A couple of notes in case they're useful:

- I used the Conventional Commits format (`refactor(auth): ...`) since refactors map cleanly to the `refactor` type. If your repo doesn't follow that convention, the subject line can simply be: `Refactor auth middleware to async/await`.
- If this change alters any externally observable behavior (e.g., how errors surface to callers), consider adding a `BREAKING CHANGE:` footer so downstream consumers are warned.
