## Read Replication Pattern (Paid Plans)

```typescript
interface Env { DB: D1Database; DB_REPLICA: D1Database; }

export default {
  async fetch(request: Request, env: Env) {
    if (request.method === 'GET') {
      // Reads: use replica for lower latency
      const users = await env.DB_REPLICA.prepare('SELECT * FROM users WHERE active = 1').all();
      return Response.json(users.results);
    }
    
    if (request.method === 'POST') {
      const { name, email } = await request.json();
      const result = await env.DB.prepare('INSERT INTO users (name, email) VALUES (?, ?)').bind(name, email).run();
      
      // Read-after-write: use primary for consistency (replication lag <100ms-2s)
      const user = await env.DB.prepare('SELECT * FROM users WHERE id = ?').bind(result.meta.last_row_id).first();
      return Response.json(user, { status: 201 });
    }
  }
}
```

**Use replicas for**: Analytics dashboards, search results, public queries (eventual consistency OK)  
**Use primary for**: Read-after-write, financial transactions, authentication (consistency required)

