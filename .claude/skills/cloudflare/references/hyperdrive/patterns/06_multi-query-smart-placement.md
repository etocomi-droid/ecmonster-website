## Multi-Query + Smart Placement

For Workers making **multiple queries** per request, enable Smart Placement to execute near DB:

```jsonc
// wrangler.jsonc
{
  "placement": {"mode": "smart"},
  "hyperdrive": [{"binding": "HYPERDRIVE", "id": "<ID>"}]
}
```

```typescript
const sql = postgres(env.HYPERDRIVE.connectionString, {prepare: true});

// Multiple queries benefit from Smart Placement
const [user] = await sql`SELECT * FROM users WHERE id = ${userId}`;
const orders = await sql`SELECT * FROM orders WHERE user_id = ${userId} ORDER BY created_at DESC LIMIT 10`;
const stats = await sql`SELECT COUNT(*) as total, SUM(amount) as spent FROM orders WHERE user_id = ${userId}`;

return Response.json({user, orders, stats});
```

**Benefits:** Worker executes near DB → reduces latency for each query. Without Smart Placement, each query round-trips from edge.

