## Conditional Operations

```typescript
// Precondition failure returns object WITHOUT body
const object = await env.MY_BUCKET.get(key, {
  onlyIf: { etagMatches: '"wrong"' }
});

// Check for body, not just null
if (!object) return new Response('Not found', { status: 404 });
if (!object.body) return new Response(null, { status: 304 }); // Precondition failed
```

