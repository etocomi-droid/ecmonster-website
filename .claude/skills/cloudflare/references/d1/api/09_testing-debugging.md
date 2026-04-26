## Testing & Debugging

```typescript
// Vitest with unstable_dev
import { unstable_dev } from 'wrangler';
describe('D1', () => {
  let worker: Awaited<ReturnType<typeof unstable_dev>>;
  beforeAll(async () => { worker = await unstable_dev('src/index.ts'); });
  afterAll(async () => { await worker.stop(); });
  it('queries users', async () => { expect((await worker.fetch('/users')).status).toBe(200); });
});

// Debug query performance
const result = await env.DB.prepare('SELECT * FROM users').all();
console.log('Duration:', result.meta.duration, 'ms');

// Query plan analysis
const plan = await env.DB.prepare('EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = ?').bind(email).all();
```

```bash
# Inspect local database
sqlite3 .wrangler/state/v3/d1/<database-id>.sqlite
.tables; .schema users; PRAGMA table_info(users);
```
