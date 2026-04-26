## GET (Download)

```typescript
const object = await env.MY_BUCKET.get(key);
if (!object) return new Response('Not found', { status: 404 });

// Body: arrayBuffer(), text(), json(), blob(), body (ReadableStream)

// Ranged reads
const object = await env.MY_BUCKET.get(key, { range: { offset: 0, length: 1024 } });

// Conditional GET
const object = await env.MY_BUCKET.get(key, { onlyIf: { etagMatches: '"abc123"' } });
```

