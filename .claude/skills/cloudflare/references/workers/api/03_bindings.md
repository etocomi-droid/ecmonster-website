## Bindings

```typescript
// KV
await env.MY_KV.get('key');
await env.MY_KV.put('key', 'value', { expirationTtl: 3600 });

// R2
const obj = await env.MY_BUCKET.get('file.txt');
await env.MY_BUCKET.put('file.txt', 'content');

// D1
const result = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(1).first();

// D1 Sessions (2024+) - read-after-write consistency
const session = env.DB.withSession();
await session.prepare('INSERT INTO users (name) VALUES (?)').bind('Alice').run();
const user = await session.prepare('SELECT * FROM users WHERE name = ?').bind('Alice').first(); // Guaranteed fresh

// Queues
await env.MY_QUEUE.send({ timestamp: Date.now() });

// Secrets/vars
const key = env.API_KEY;
```

