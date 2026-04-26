## Quick Start

```typescript
// 1. Create index
// npx wrangler vectorize create my-index --dimensions=768 --metric=cosine

// 2. Configure binding (wrangler.jsonc)
// { "vectorize": [{ "binding": "VECTORIZE", "index_name": "my-index" }] }

// 3. Query vectors
const matches = await env.VECTORIZE.query(queryVector, { topK: 5 });
```

