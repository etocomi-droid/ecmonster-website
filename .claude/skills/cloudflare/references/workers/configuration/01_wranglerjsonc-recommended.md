## wrangler.jsonc (Recommended)

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01", // Use current date for new projects
  
  // Bindings (non-inheritable)
  "vars": { "ENVIRONMENT": "production" },
  "kv_namespaces": [{ "binding": "MY_KV", "id": "abc123" }],
  "r2_buckets": [{ "binding": "MY_BUCKET", "bucket_name": "my-bucket" }],
  "d1_databases": [{ "binding": "DB", "database_name": "my-db", "database_id": "xyz789" }],
  
  // Environments
  "env": {
    "staging": {
      "vars": { "ENVIRONMENT": "staging" },
      "kv_namespaces": [{ "binding": "MY_KV", "id": "staging-id" }]
    }
  }
}
```

