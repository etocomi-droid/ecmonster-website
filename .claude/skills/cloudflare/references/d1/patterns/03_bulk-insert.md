## Bulk Insert

```typescript
async function bulkInsertUsers(users: Array<{ name: string; email: string }>, env: Env) {
  const stmt = env.DB.prepare('INSERT INTO users (name, email) VALUES (?, ?)');
  const batch = users.map(user => stmt.bind(user.name, user.email));
  return await env.DB.batch(batch);
}
```

