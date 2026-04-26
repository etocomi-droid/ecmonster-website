## Local Development

```bash
wrangler dev --persist-to=./.wrangler/state  # Persist across restarts
# Local DB: .wrangler/state/v3/d1/<database-id>.sqlite
sqlite3 .wrangler/state/v3/d1/<database-id>.sqlite  # Inspect

# Local dev uses free tier limits by default
```
