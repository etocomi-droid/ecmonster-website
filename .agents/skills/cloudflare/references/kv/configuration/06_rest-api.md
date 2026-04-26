## REST API

### Single Operations

```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({
  apiEmail: process.env.CLOUDFLARE_EMAIL,
  apiKey: process.env.CLOUDFLARE_API_KEY
});

// Single key operations
await client.kv.namespaces.values.update(namespaceId, 'key', {
  account_id: accountId,
  value: 'value',
  expiration_ttl: 3600
});
```

### Bulk Operations

```typescript
// Bulk update (up to 10,000 keys, max 100MB total)
await client.kv.namespaces.bulkUpdate(namespaceId, {
  account_id: accountId,
  body: [
    { key: "key1", value: "value1", expiration_ttl: 3600 },
    { key: "key2", value: "value2", metadata: { version: 1 } },
    { key: "key3", value: "value3" }
  ]
});

// Bulk get (up to 100 keys)
const results = await client.kv.namespaces.bulkGet(namespaceId, {
  account_id: accountId,
  keys: ["key1", "key2", "key3"]
});

// Bulk delete (up to 10,000 keys)
await client.kv.namespaces.bulkDelete(namespaceId, {
  account_id: accountId,
  keys: ["key1", "key2", "key3"]
});
```
