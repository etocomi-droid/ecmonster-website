## Framework Integration

### Hono
```javascript
import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => c.text('Hello Hono!'));
app.get('/api/:id', async (c) => {
  const id = c.req.param('id');
  const data = await c.env.KV.get(id);
  return c.json({ id, data });
});

export default app;
```

### itty-router
```javascript
import { Router } from 'itty-router';

const router = Router();

router.get('/', () => new Response('Hello itty!'));
router.get('/api/:id', async (request, env) => {
  const { id } = request.params;
  const data = await env.KV.get(id);
  return Response.json({ id, data });
});

export default {
  fetch: (request, env, ctx) => router.handle(request, env, ctx)
};
```

