## Transactions (via batch)

```typescript
// D1 executes batch() as atomic transaction - all succeed or all fail
const results = await env.DB.batch([
  env.DB.prepare('INSERT INTO accounts (id, balance) VALUES (?, ?)').bind(1, 100),
  env.DB.prepare('INSERT INTO accounts (id, balance) VALUES (?, ?)').bind(2, 200),
  env.DB.prepare('UPDATE accounts SET balance = balance - ? WHERE id = ?').bind(50, 1),
  env.DB.prepare('UPDATE accounts SET balance = balance + ? WHERE id = ?').bind(50, 2)
]);
```

