## Auth Middleware

```typescript
// functions/_middleware.ts
const auth: PagesFunction<Env> = async (context) => {
  if (context.request.url.includes('/public/')) return context.next();
  const authHeader = context.request.headers.get('Authorization');
  if (!authHeader?.startsWith('Bearer ')) {
    return new Response('Unauthorized', { status: 401 });
  }
  
  try {
    const payload = await verifyJWT(authHeader.substring(7), context.env.JWT_SECRET);
    context.data.user = payload;
    return context.next();
  } catch (err) {
    return new Response('Invalid token', { status: 401 });
  }
};
export const onRequest = [auth];
```

