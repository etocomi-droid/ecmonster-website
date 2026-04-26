## Batch Operations

```typescript
// Execute multiple queries in single round trip (atomic transaction)
const results = await env.DB.batch([
  env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(1),
  env.DB.prepare('SELECT * FROM posts WHERE author_id = ?').bind(1),
  env.DB.prepare('UPDATE users SET last_access = ? WHERE id = ?').bind(Date.now(), 1)
]);
// results is array: [result1, result2, result3]

// Batch with same prepared statement, different params
const userIds = [1, 2, 3];
const stmt = env.DB.prepare('SELECT * FROM users WHERE id = ?');
const results = await env.DB.batch(userIds.map(id => stmt.bind(id)));
```

