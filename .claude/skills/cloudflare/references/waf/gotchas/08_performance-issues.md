## Performance Issues

**Problem:** Increased latency
**Cause:** Complex expressions, excessive rules
**Solution:**

1. Skip static assets early: `action: 'skip'` for `\\.(jpg|css|js)$`
2. Path-based deployment: Only run managed on `/api` or `/admin`
3. Disable unused categories: `{ category: 'wordpress', enabled: false }`
4. Prefer string operators over regex: `starts_with` vs `matches`

