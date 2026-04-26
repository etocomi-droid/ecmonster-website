## Quick Start

```bash
# 1. Enable R2 Data Catalog on bucket
npx wrangler r2 bucket catalog enable my-bucket

# 2. Create API token (Admin Read & Write)
# Dashboard: R2 → Manage API tokens → Create API token

# 3. Set environment variable
export WRANGLER_R2_SQL_AUTH_TOKEN=<your-token>

# 4. Run query
npx wrangler r2 sql query "my-bucket" "SELECT * FROM default.my_table LIMIT 10"
```

