## TypeScript SDK

Install: `npm install cloudflare`

```typescript
import Cloudflare from 'cloudflare';

const cf = new Cloudflare({
  apiToken: process.env.CF_API_TOKEN,
});

const accountId = process.env.CF_ACCOUNT_ID;
```

