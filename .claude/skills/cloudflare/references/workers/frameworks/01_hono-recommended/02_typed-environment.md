### Typed Environment

```typescript
import type { Env } from './.wrangler/types/runtime';

const app = new Hono<{ Bindings: Env }>();

app.get('/data', async (c) => {
  const value = await c.env.MY_KV.get('key');  // Fully typed
  return c.text(value || 'Not found');
});
```

