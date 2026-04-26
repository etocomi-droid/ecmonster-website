## Wrangler Configuration

### Basic Email Worker

```jsonc
// wrangler.jsonc
{
  "name": "email-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",
  "send_email": [{ "name": "EMAIL" }]
}
```

```typescript
// src/index.ts
export default {
  async email(message, env, ctx) {
    await message.forward("destination@example.com");
  }
} satisfies ExportedHandler;
```

### With Storage Bindings

```jsonc
{
  "name": "email-processor",
  "send_email": [{ "name": "EMAIL" }],
  "kv_namespaces": [{ "binding": "KV", "id": "abc123" }],
  "r2_buckets": [{ "binding": "R2", "bucket_name": "emails" }],
  "d1_databases": [{ "binding": "DB", "database_id": "def456" }]
}
```

```typescript
interface Env {
  EMAIL: SendEmail;
  KV: KVNamespace;
  R2: R2Bucket;
  DB: D1Database;
}
```

