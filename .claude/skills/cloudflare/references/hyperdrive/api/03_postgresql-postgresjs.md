## PostgreSQL (postgres.js)

```typescript
import postgres from "postgres";  // postgres@^3.4.8

const sql = postgres(env.HYPERDRIVE.connectionString, {
  max: 5,             // Limit per Worker (Workers max: 6)
  prepare: true,      // Enabled by default, required for caching
  fetch_types: false, // Reduce latency if not using arrays
});

const users = await sql`SELECT * FROM users WHERE active = ${true} LIMIT 10`;
```

**⚠️ `prepare: true` is enabled by default and required for Hyperdrive caching.** Setting to `false` disables prepared statements + cache.

