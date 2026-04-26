## Complete Example

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-app",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",
  
  "vars": { "API_URL": "https://api.example.com" },
  "kv_namespaces": [{ "binding": "CACHE", "id": "abc123" }],
  "r2_buckets": [{ "binding": "ASSETS", "bucket_name": "my-assets" }],
  "d1_databases": [{ "binding": "DB", "database_name": "my-db", "database_id": "xyz789" }],
  "services": [{ "binding": "AUTH", "service": "auth-worker" }],
  "ai": { "binding": "AI" }
}
```

