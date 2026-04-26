### Basic Setup

```typescript
import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => c.text('Hello World!'));
app.post('/api/users', async (c) => {
  const body = await c.req.json();
  return c.json({ id: 1, ...body }, 201);
});

export default app;
```

