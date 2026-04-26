### "D1 read-after-write inconsistency"

**Cause:** D1 is eventually consistent; reads may not reflect recent writes  
**Solution:** Use D1 Sessions (2024+) to guarantee read-after-write consistency within a session:

```typescript
const session = env.DB.withSession();
await session.prepare('INSERT INTO users (name) VALUES (?)').bind('Alice').run();
const user = await session.prepare('SELECT * FROM users WHERE name = ?').bind('Alice').first(); // Guaranteed to see Alice
```

**When to use sessions:** Write → Read patterns, transactions requiring consistency

