## Smart Placement for Database Apps

Enable Smart Placement for apps with D1 or centralized data sources:

```jsonc
// wrangler.jsonc
{
  "name": "global-app",
  "placement": {
    "mode": "smart"
  },
  "d1_databases": [{
    "binding": "DB",
    "database_id": "your-db-id"
  }]
}
```

```typescript
// functions/api/data.ts
export const onRequestGet: PagesFunction<Env> = async ({ env }) => {
  // Smart Placement optimizes execution location over time
  // Balances user location vs database location
  const data = await env.DB.prepare('SELECT * FROM products LIMIT 10').all();
  return Response.json(data);
};
```

**Best for**: Read-heavy apps with D1/Durable Objects in specific regions.  
**Not needed**: Apps without data locality constraints or with evenly distributed traffic.

