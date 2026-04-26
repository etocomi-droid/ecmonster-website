## Connection String Format

For quick reference:

```
Catalog URI:  https://<account-id>.r2.cloudflarestorage.com/iceberg/<bucket>
Warehouse:    <bucket-name>
Token:        <r2-api-token>
```

**Where to find values:**

| Value | Source |
|-------|--------|
| `<account-id>` | Dashboard URL or `wrangler whoami` |
| `<bucket>` | R2 bucket name |
| Catalog URI | Output from `wrangler r2 bucket catalog enable` |
| Token | R2 API Token creation page |

