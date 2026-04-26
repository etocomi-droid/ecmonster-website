### OpenAPI/Swagger (Hono OpenAPI)

```typescript
import { OpenAPIHono, createRoute, z } from '@hono/zod-openapi';

const app = new OpenAPIHono();

const route = createRoute({
  method: 'get',
  path: '/users/{id}',
  request: { params: z.object({ id: z.string() }) },
  responses: {
    200: { description: 'User found', content: { 'application/json': { schema: z.object({ id: z.string() }) } } },
  },
});

app.openapi(route, (c) => {
  const { id } = c.req.valid('param');
  return c.json({ id });
});

app.doc('/openapi.json', { openapi: '3.0.0', info: { version: '1.0.0', title: 'API' } });
```

