## Bindings

```jsonc
// Variables
{ "vars": { "API_URL": "https://api.example.com" } }

// KV
{ "kv_namespaces": [{ "binding": "CACHE", "id": "abc123" }] }

// D1
{ "d1_databases": [{ "binding": "DB", "database_id": "abc-123" }] }

// R2
{ "r2_buckets": [{ "binding": "ASSETS", "bucket_name": "my-assets" }] }

// Durable Objects
{ "durable_objects": { 
  "bindings": [{ 
    "name": "COUNTER", 
    "class_name": "Counter",
    "script_name": "my-worker"  // Required for external DOs
  }] 
} }
{ "migrations": [{ "tag": "v1", "new_sqlite_classes": ["Counter"] }] }

// Service Bindings
{ "services": [{ "binding": "AUTH", "service": "auth-worker" }] }

// Queues
{ "queues": {
  "producers": [{ "binding": "TASKS", "queue": "task-queue" }],
  "consumers": [{ "queue": "task-queue", "max_batch_size": 10 }]
} }

// Vectorize
{ "vectorize": [{ "binding": "VECTORS", "index_name": "embeddings" }] }

// Hyperdrive (requires nodejs_compat_v2 for pg/postgres)
{ "hyperdrive": [{ "binding": "HYPERDRIVE", "id": "hyper-id" }] }
{ "compatibility_flags": ["nodejs_compat_v2"] }  // For pg/postgres

// Workers AI
{ "ai": { "binding": "AI" } }

// Workflows
{ "workflows": [{ "binding": "WORKFLOW", "name": "my-workflow", "class_name": "MyWorkflow" }] }

// Secrets Store (centralized secrets)
{ "secrets_store": [{ "binding": "SECRETS", "id": "store-id" }] }

// Constellation (AI inference)
{ "constellation": [{ "binding": "MODEL", "project_id": "proj-id" }] }
```

