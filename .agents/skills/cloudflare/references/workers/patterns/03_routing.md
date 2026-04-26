## Routing

```typescript
const router = { 'GET /api/users': handleGetUsers, 'POST /api/users': handleCreateUser };

const handler = router[`${request.method} ${url.pathname}`];
return handler ? handler(request, env) : new Response('Not Found', { status: 404 });
```

**Production**: Use Hono, itty-router, or Worktop (see [frameworks.md](./frameworks.md))

