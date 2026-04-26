## Token Permission Errors (403)

**Problem:** API returns 403 Forbidden despite valid token.

**Cause:** Token lacks required permissions (scope).

**Scopes Required:**

| Operation | Required Scope |
|-----------|----------------|
| List zones | Zone:Read (zone-level or account-level) |
| Create zone | Zone:Edit (account-level) |
| Edit DNS | DNS:Edit (zone-level) |
| Deploy Worker | Workers Script:Edit (account-level) |
| Read KV | Workers KV Storage:Read |
| Write KV | Workers KV Storage:Edit |

**Solution:** Re-create token with correct permissions in Dashboard → My Profile → API Tokens.

