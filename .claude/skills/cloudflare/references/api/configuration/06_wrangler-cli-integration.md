## Wrangler CLI Integration

```bash
# Configure authentication
wrangler login
# Or
export CLOUDFLARE_API_TOKEN='token'

# Common commands that use API
wrangler deploy              # Uploads worker via API
wrangler kv:key put          # KV operations
wrangler r2 bucket create    # R2 operations
wrangler d1 execute          # D1 operations
wrangler pages deploy        # Pages operations

# Get API configuration
wrangler whoami              # Shows authenticated user
```

### wrangler.toml

```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"
account_id = "your-account-id"

# Can also use env vars:
# CLOUDFLARE_ACCOUNT_ID
# CLOUDFLARE_API_TOKEN
```

