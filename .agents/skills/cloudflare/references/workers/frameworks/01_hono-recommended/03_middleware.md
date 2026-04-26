### Middleware

```typescript
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';

app.use('*', logger());
app.use('/api/*', cors({ origin: '*' }));

// Custom middleware
app.use('/protected/*', async (c, next) => {
  const auth = c.req.header('Authorization');
  if (!auth?.startsWith('Bearer ')) return c.text('Unauthorized', 401);
  await next();
});
```

