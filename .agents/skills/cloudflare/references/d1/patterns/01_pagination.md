## Pagination

```typescript
async function getUsers({ page, pageSize }: { page: number; pageSize: number }, env: Env) {
  const offset = (page - 1) * pageSize;
  const [countResult, dataResult] = await env.DB.batch([
    env.DB.prepare('SELECT COUNT(*) as total FROM users'),
    env.DB.prepare('SELECT * FROM users ORDER BY created_at DESC LIMIT ? OFFSET ?').bind(pageSize, offset)
  ]);
  return { data: dataResult.results, total: countResult.results[0].total, page, pageSize, totalPages: Math.ceil(countResult.results[0].total / pageSize) };
}
```

