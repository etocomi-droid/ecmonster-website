### TypeScript SDK

```bash
npm install cloudflare
```

```typescript
import Cloudflare from 'cloudflare';

const client = new Cloudflare({
  apiToken: process.env.CLOUDFLARE_API_TOKEN,
});

// Enable Cache Reserve
await client.cache.cacheReserve.edit({
  zone_id: 'abc123',
  value: 'on',
});

// Get Cache Reserve status
const status = await client.cache.cacheReserve.get({
  zone_id: 'abc123',
});
console.log(status.value); // 'on' or 'off'
```

