## Bindings

```jsonc
{
  // Environment variables - access via env.VAR_NAME
  "vars": { "ENVIRONMENT": "production" },
  
  // KV (key-value storage)
  "kv_namespaces": [{ "binding": "MY_KV", "id": "abc123" }],
  
  // R2 (object storage)
  "r2_buckets": [{ "binding": "MY_BUCKET", "bucket_name": "my-bucket" }],
  
  // D1 (SQL database)
  "d1_databases": [{ "binding": "DB", "database_name": "my-db", "database_id": "xyz789" }],
  
  // Durable Objects (stateful coordination)
  "durable_objects": {
    "bindings": [{ "name": "COUNTER", "class_name": "Counter" }]
  },
  
  // Queues (message queues)
  "queues": {
    "producers": [{ "binding": "MY_QUEUE", "queue": "my-queue" }],
    "consumers": [{ "queue": "my-queue", "max_batch_size": 10 }]
  },
  
  // Service bindings (worker-to-worker RPC)
  "services": [{ "binding": "SERVICE_B", "service": "service-b" }],
  
  // Analytics Engine
  "analytics_engine_datasets": [{ "binding": "ANALYTICS" }]
}
```

### Secrets

Set via CLI (never in config):

```bash
npx wrangler secret put API_KEY
```

Access: `env.API_KEY`

### Automatic Provisioning (Beta)

Bindings without IDs are auto-created:

```jsonc
{ "kv_namespaces": [{ "binding": "MY_KV" }] }  // ID added on deploy
```

