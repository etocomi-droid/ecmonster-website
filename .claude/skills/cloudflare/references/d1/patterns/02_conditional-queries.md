## Conditional Queries

```typescript
async function searchUsers(filters: { name?: string; email?: string; active?: boolean }, env: Env) {
  const conditions: string[] = [], params: (string | number | boolean | null)[] = [];
  if (filters.name) { conditions.push('name LIKE ?'); params.push(`%${filters.name}%`); }
  if (filters.email) { conditions.push('email = ?'); params.push(filters.email); }
  if (filters.active !== undefined) { conditions.push('active = ?'); params.push(filters.active ? 1 : 0); }
  const whereClause = conditions.length > 0 ? `WHERE ${conditions.join(' AND ')}` : '';
  return await env.DB.prepare(`SELECT * FROM users ${whereClause}`).bind(...params).all();
}
```

