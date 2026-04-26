## Batch Parallel Operations

**Problem:** Need to create multiple resources quickly.

**Solution:** Use `Promise.all()` for parallel requests (respect rate limits).

```typescript
// Create multiple DNS records in parallel
const records = ['www', 'api', 'cdn'].map(subdomain =>
  client.dns.records.create({
    zone_id: 'zone-id',
    type: 'A',
    name: `${subdomain}.example.com`,
    content: '192.0.2.1',
  })
);
await Promise.all(records);
```

**Controlled concurrency** (avoid rate limits):

```typescript
import pLimit from 'p-limit';
const limit = pLimit(10); // Max 10 concurrent

const subdomains = ['www', 'api', 'cdn', /* many more */];
const records = subdomains.map(subdomain =>
  limit(() => client.dns.records.create({
    zone_id: 'zone-id',
    type: 'A',
    name: `${subdomain}.example.com`,
    content: '192.0.2.1',
  }))
);
await Promise.all(records);
```

