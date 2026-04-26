## Middleware

```typescript
// functions/_middleware.ts
// Single
export const onRequest: PagesFunction = async (context) => {
  const response = await context.next();
  response.headers.set('X-Custom-Header', 'value');
  return response;
};

// Chained (runs in order)
const errorHandler: PagesFunction = async (context) => {
  try {
    return await context.next();
  } catch (err) {
    return new Response(err.message, { status: 500 });
  }
};

const auth: PagesFunction = async (context) => {
  const token = context.request.headers.get('Authorization');
  if (!token) return new Response('Unauthorized', { status: 401 });
  context.data.userId = await verifyToken(token);
  return context.next();
};

export const onRequest = [errorHandler, auth];
```

**Scope**: `functions/_middleware.ts` → all; `functions/api/_middleware.ts` → `/api/*` only

