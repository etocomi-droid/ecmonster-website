## Mixed Read/Write

```typescript
interface Env {
  HYPERDRIVE_CACHED: Hyperdrive;    // max_age=120
  HYPERDRIVE_REALTIME: Hyperdrive;  // caching disabled
}

// Reads: cached
if (req.method === "GET") {
  const sql = postgres(env.HYPERDRIVE_CACHED.connectionString, {prepare: true});
  const products = await sql`SELECT * FROM products WHERE category = ${cat}`;
}

// Writes: no cache (immediate consistency)
if (req.method === "POST") {
  const sql = postgres(env.HYPERDRIVE_REALTIME.connectionString, {prepare: true});
  await sql`INSERT INTO orders ${sql(data)}`;
}
```

