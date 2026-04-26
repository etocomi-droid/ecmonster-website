## CORS

```typescript
const corsHeaders = { 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS' };
if (request.method === 'OPTIONS') return new Response(null, { headers: corsHeaders });
```

