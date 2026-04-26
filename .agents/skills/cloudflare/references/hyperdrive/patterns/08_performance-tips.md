## Performance Tips

**Enable prepared statements (required for caching):**
```typescript
const sql = postgres(connectionString, {prepare: true});  // Default, enables caching
```

**Optimize connection settings:**
```typescript
const sql = postgres(connectionString, {
  max: 5,             // Stay under Workers' 6 connection limit
  fetch_types: false, // Reduce latency if not using arrays
  idle_timeout: 60,   // Match Worker lifetime
});
```

**Write cache-friendly queries:**
```typescript
// ✅ Cacheable (deterministic)
await sql`SELECT * FROM products WHERE category = 'electronics' LIMIT 10`;

// ❌ Not cacheable (volatile NOW())
await sql`SELECT * FROM logs WHERE created_at > NOW()`;

// ✅ Cacheable (parameterized timestamp)
const ts = Date.now();
await sql`SELECT * FROM logs WHERE created_at > ${ts}`;
```

See [gotchas.md](./gotchas.md) for limits, troubleshooting.
