## Read Replication (Paid Plans)

```typescript
// Read from nearest replica for lower latency (automatic failover)
const user = await env.DB_REPLICA.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first();

// Writes always go to primary
await env.DB.prepare('UPDATE users SET last_login = ? WHERE id = ?').bind(Date.now(), userId).run();
```

