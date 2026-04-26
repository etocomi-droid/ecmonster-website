## Testing

**Unit tests** (Vitest + cloudflare:test):
```typescript
import { env } from 'cloudflare:test';
import { it, expect } from 'vitest';
import { onRequest } from '../functions/api';

it('returns JSON', async () => {
  const req = new Request('http://localhost/api');
  const ctx = { request: req, env, params: {}, data: {} } as EventContext;
  const res = await onRequest(ctx);
  expect(res.status).toBe(200);
});
```

**Integration:** `wrangler pages dev` + Playwright/Cypress

