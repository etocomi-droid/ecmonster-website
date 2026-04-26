## Query Caching

**Cacheable:**
```sql
SELECT * FROM posts WHERE published = true;
SELECT COUNT(*) FROM users;
```

**NOT cacheable:**
```sql
-- Writes
INSERT/UPDATE/DELETE

-- Volatile functions
SELECT NOW();
SELECT random();
SELECT LASTVAL();  -- PostgreSQL
SELECT UUID();     -- MySQL
```

**Cache config:**
- Default: `max_age=60s`, `swr=15s`
- Max `max_age`: 3600s
- Disable: `--caching-disabled=true`

**Multiple configs pattern:**
```typescript
// Reads: cached
const sqlCached = postgres(env.HYPERDRIVE_CACHED.connectionString);
const posts = await sqlCached`SELECT * FROM posts ORDER BY views DESC LIMIT 10`;

// Writes/time-sensitive: no cache
const sqlNoCache = postgres(env.HYPERDRIVE_NO_CACHE.connectionString);
const orders = await sqlNoCache`SELECT * FROM orders WHERE created_at > NOW() - INTERVAL 5 MINUTE`;
```

