## Type Safety Gotchas

### Missing @cloudflare/workers-types

**Error:** `Cannot find name 'Request'`  
**Solution:** `npm install -D @cloudflare/workers-types`, add to tsconfig.json `"types"`

### Binding Type Mismatches

```typescript
// ❌ Wrong - KV returns string | null
const value: string = await env.MY_KV.get('key');

// ✅ Handle null
const value = await env.MY_KV.get('key');
if (!value) return new Response('Not found', { status: 404 });
```

