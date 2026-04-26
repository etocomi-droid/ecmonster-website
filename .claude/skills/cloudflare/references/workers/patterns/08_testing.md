## Testing

```typescript
import { describe, it, expect } from 'vitest';
import worker from '../src/index';

describe('Worker', () => {
  it('returns 200', async () => {
    const req = new Request('http://localhost/');
    const env = { MY_VAR: 'test' };
    const ctx = { waitUntil: () => {}, passThroughOnException: () => {} };
    expect((await worker.fetch(req, env, ctx)).status).toBe(200);
  });
});
```

