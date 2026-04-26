## List Operations

```typescript
// List all
const keys = await env.MY_KV.list();
// { keys: [...], list_complete: boolean, cursor?: string }

// With prefix
const userKeys = await env.MY_KV.list({ prefix: "user:" });

// Pagination
let cursor: string | undefined;
let allKeys = [];
do {
  const result = await env.MY_KV.list({ cursor, limit: 1000 });
  allKeys.push(...result.keys);
  cursor = result.cursor;
} while (!result.list_complete);
```

