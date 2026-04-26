## wrangler.jsonc

```jsonc
{
  "$schema": "./node_modules/wrangler/config-schema.json",
  "name": "my-pages-app",
  "pages_build_output_dir": "./dist",
  "compatibility_date": "2025-01-01",
  "compatibility_flags": ["nodejs_compat"],
  
  "vars": { "API_URL": "https://api.example.com" },
  "kv_namespaces": [{ "binding": "KV", "id": "abc123" }],
  "d1_databases": [{ "binding": "DB", "database_name": "prod-db", "database_id": "xyz789" }],
  "r2_buckets": [{ "binding": "BUCKET", "bucket_name": "my-bucket" }],
  "durable_objects": { "bindings": [{ "name": "COUNTER", "class_name": "Counter", "script_name": "counter-worker" }] },
  "services": [{ "binding": "AUTH", "service": "auth-worker" }],
  "ai": { "binding": "AI" },
  "vectorize": [{ "binding": "VECTORIZE", "index_name": "my-index" }],
  "analytics_engine_datasets": [{ "binding": "ANALYTICS" }]
}
```

