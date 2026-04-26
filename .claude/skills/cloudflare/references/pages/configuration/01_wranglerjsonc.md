## wrangler.jsonc

```jsonc
{
  "name": "my-pages-project",
  "pages_build_output_dir": "./dist",
  "compatibility_date": "2026-01-01", // Use current date for new projects
  "compatibility_flags": ["nodejs_compat"],
  "placement": {
    "mode": "smart"  // Optional: Enable Smart Placement
  },
  "kv_namespaces": [{"binding": "KV", "id": "abcd1234..."}],
  "d1_databases": [{"binding": "DB", "database_id": "xxxx-xxxx", "database_name": "production-db"}],
  "r2_buckets": [{"binding": "BUCKET", "bucket_name": "my-bucket"}],
  "durable_objects": {"bindings": [{"name": "COUNTER", "class_name": "Counter", "script_name": "counter-worker"}]},
  "services": [{"binding": "API", "service": "api-worker"}],
  "queues": {"producers": [{"binding": "QUEUE", "queue": "my-queue"}]},
  "vectorize": [{"binding": "VECTORIZE", "index_name": "my-index"}],
  "ai": {"binding": "AI"},
  "analytics_engine_datasets": [{"binding": "ANALYTICS"}],
  "vars": {"API_URL": "https://api.example.com", "ENVIRONMENT": "production"},
  "env": {
    "preview": {
      "vars": {"API_URL": "https://staging-api.example.com"},
      "kv_namespaces": [{"binding": "KV", "id": "preview-namespace-id"}]
    }
  }
}
```

