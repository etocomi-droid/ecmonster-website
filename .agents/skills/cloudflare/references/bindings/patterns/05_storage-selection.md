## Storage Selection

### KV: CDN-Backed Reads

```typescript
const config = await env.MY_KV.get('app-config', { type: 'json' });
```

**Use when:** Read-heavy, <25MB, global distribution, eventual consistency OK  
**Latency:** <10ms reads (cached), writes eventually consistent (60s)

### D1: Relational Queries

```typescript
const results = await env.DB.prepare(`
  SELECT u.name, COUNT(o.id) FROM users u
  LEFT JOIN orders o ON u.id = o.user_id GROUP BY u.id
`).all();
```

**Use when:** Relational data, JOINs, ACID transactions  
**Limits:** 10GB database size, 100k rows per query

### R2: Large Objects

```typescript
const object = await env.MY_BUCKET.get('large-file.zip');
return new Response(object.body);
```

**Use when:** Files >25MB, S3-compatible API needed  
**Limits:** 5TB per object, unlimited storage

### Durable Objects: Coordination

```typescript
const id = env.COUNTER.idFromName('global');
const stub = env.COUNTER.get(id);
await stub.fetch(new Request('https://fake/increment'));
```

**Use when:** Strong consistency, real-time coordination, WebSocket state  
**Guarantees:** Single-threaded execution, transactional storage

