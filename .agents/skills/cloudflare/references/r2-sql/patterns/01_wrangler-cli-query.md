## Wrangler CLI Query

```bash
# Basic query
npx wrangler r2 sql query "my-bucket" "SELECT * FROM default.logs LIMIT 10"

# Multi-line query
npx wrangler r2 sql query "my-bucket" "
  SELECT status, COUNT(*), AVG(response_time)
  FROM logs.http_requests
  WHERE timestamp >= '2025-01-01T00:00:00Z'
  GROUP BY status
  ORDER BY COUNT(*) DESC
  LIMIT 100
"

# Use environment variable
export R2_SQL_WAREHOUSE="my-bucket"
npx wrangler r2 sql query "$R2_SQL_WAREHOUSE" "SELECT * FROM default.logs"
```

