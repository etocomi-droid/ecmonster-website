## Read Replication (Paid Plans)

Routes queries to nearest replica for lower latency. Writes always go to primary.

```typescript
interface Env {
  DB: D1Database;          // Primary (writes)
  DB_REPLICA: D1Database;  // Replica (reads)
}

// Reads: use replica
const user = await env.DB_REPLICA.prepare('SELECT * FROM users WHERE id = ?').bind(userId).first();

// Writes: use primary
await env.DB.prepare('UPDATE users SET last_login = ? WHERE id = ?').bind(Date.now(), userId).run();

// Read-after-write: use primary for consistency (replication lag <100ms-2s)
await env.DB.prepare('INSERT INTO posts (title) VALUES (?)').bind(title).run();
const post = await env.DB.prepare('SELECT * FROM posts WHERE title = ?').bind(title).first(); // Primary
```

