### Testing with Hono

```typescript
import { describe, it, expect } from 'vitest';
import app from '../src/index';

describe('API', () => {
  it('GET /', async () => {
    const res = await app.request('/');
    expect(res.status).toBe(200);
    expect(await res.text()).toBe('Hello World!');
  });
});
```

