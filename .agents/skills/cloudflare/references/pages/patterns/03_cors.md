## CORS

```typescript
// functions/api/_middleware.ts
const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type, Authorization'
};

export const onRequest: PagesFunction = async (context) => {
  if (context.request.method === 'OPTIONS') {
    return new Response(null, {headers: corsHeaders});
  }
  const response = await context.next();
  Object.entries(corsHeaders).forEach(([k, v]) => response.headers.set(k, v));
  return response;
};
```

