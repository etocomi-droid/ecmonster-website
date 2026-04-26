## Verify Setup

Test configuration by querying system tables:

```bash
# List namespaces
npx wrangler r2 sql query "my-bucket" "SHOW DATABASES"

# List tables in namespace
npx wrangler r2 sql query "my-bucket" "SHOW TABLES IN default"
```

If successful, returns JSON array of results.

