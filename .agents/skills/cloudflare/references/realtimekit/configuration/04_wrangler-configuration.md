## Wrangler Configuration

### Basic Configuration
```jsonc
// wrangler.jsonc
{
  "name": "realtimekit-app",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",  // Use current date
  "vars": {
    "CLOUDFLARE_ACCOUNT_ID": "abc123",
    "REALTIMEKIT_APP_ID": "xyz789"
  }
  // Secrets: wrangler secret put CLOUDFLARE_API_TOKEN
}
```

### With Database & Storage
```jsonc
{
  "d1_databases": [{ "binding": "DB", "database_name": "meetings", "database_id": "d1-id" }],
  "r2_buckets": [{ "binding": "RECORDINGS", "bucket_name": "recordings" }],
  "kv_namespaces": [{ "binding": "SESSIONS", "id": "kv-id" }]
}
```

### Multi-Environment
```bash
# Deploy to environments
wrangler deploy --env staging
wrangler deploy --env production
```

