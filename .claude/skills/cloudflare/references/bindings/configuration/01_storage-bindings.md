## Storage Bindings

```jsonc
{
  "kv_namespaces": [{ "binding": "MY_KV", "id": "..." }],
  "r2_buckets": [{ "binding": "MY_BUCKET", "bucket_name": "my-bucket" }],
  "d1_databases": [{ "binding": "DB", "database_name": "my-db", "database_id": "..." }],
  "durable_objects": { "bindings": [{ "name": "MY_DO", "class_name": "MyDO" }] },
  "vectorize": [{ "binding": "VECTORIZE", "index_name": "my-index" }],
  "queues": { "producers": [{ "binding": "MY_QUEUE", "queue": "my-queue" }] }
}
```

**Create commands:**
```bash
npx wrangler kv namespace create MY_KV
npx wrangler r2 bucket create my-bucket
npx wrangler d1 create my-db
npx wrangler vectorize create my-index --dimensions=768 --metric=cosine
npx wrangler queues create my-queue

# List existing resources
npx wrangler kv namespace list
npx wrangler r2 bucket list
npx wrangler d1 list
npx wrangler vectorize list
npx wrangler queues list
```

