## Core Query Methods

```typescript
// .all() - Returns all rows; .first() - First row or null; .first(col) - Single column value
// .run() - INSERT/UPDATE/DELETE; .raw() - Array of arrays (efficient)
const { results, success, meta } = await env.DB.prepare('SELECT * FROM users WHERE active = ?').bind(true).all();
const user = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first();
```

