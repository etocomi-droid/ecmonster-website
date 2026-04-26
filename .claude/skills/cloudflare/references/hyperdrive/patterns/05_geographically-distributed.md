## Geographically Distributed

```typescript
// Worker runs at edge nearest user
// Connection setup at edge (fast), pooling near DB (efficient)
const sql = postgres(env.HYPERDRIVE.connectionString, {prepare: true});
const [user] = await sql`SELECT * FROM users WHERE id = ${userId}`;

return Response.json({
  user,
  serverRegion: req.cf?.colo,  // Edge location
});
```

**Benefits:** Edge setup + DB pooling = global → single-region DB without replication.

