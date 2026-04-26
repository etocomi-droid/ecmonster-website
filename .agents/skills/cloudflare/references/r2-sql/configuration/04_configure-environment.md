## Configure Environment

### Wrangler CLI

Set environment variable for Wrangler to use:

```bash
export WRANGLER_R2_SQL_AUTH_TOKEN=<your-token>
```

Or create `.env` file in project directory:

```
WRANGLER_R2_SQL_AUTH_TOKEN=<your-token>
```

Wrangler automatically loads `.env` file when running commands.

### HTTP API

For programmatic access (non-Wrangler), pass token in Authorization header:

```bash
curl -X POST https://api.cloudflare.com/client/v4/accounts/{account_id}/r2/sql/query \
  -H "Authorization: Bearer <your-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "warehouse": "my-bucket",
    "query": "SELECT * FROM default.my_table LIMIT 10"
  }'
```

**Note:** HTTP API endpoint URL may vary - see [patterns.md](patterns.md#http-api-query) for current endpoint.

