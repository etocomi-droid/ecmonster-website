## High-Traffic Read-Heavy

```typescript
const sql = postgres(env.HYPERDRIVE.connectionString, {max: 5, prepare: true});

// Cacheable: popular content
const posts = await sql`SELECT * FROM posts WHERE published = true ORDER BY views DESC LIMIT 20`;

// Cacheable: user profiles
const [user] = await sql`SELECT id, username, bio FROM users WHERE id = ${userId}`;
```

**Benefits:** Trending/profiles cached (60s), connection pooling handles spikes.

