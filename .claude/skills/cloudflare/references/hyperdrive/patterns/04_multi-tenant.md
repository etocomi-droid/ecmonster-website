## Multi-Tenant

```typescript
const tenantId = req.headers.get("X-Tenant-ID");
const sql = postgres(env.HYPERDRIVE.connectionString, {prepare: true});

// Tenant-scoped queries cached separately
const docs = await sql`
  SELECT * FROM documents 
  WHERE tenant_id = ${tenantId} AND deleted_at IS NULL
  ORDER BY updated_at DESC LIMIT 50
`;
```

**Benefits:** Per-tenant caching, shared connection pool, protects DB from multi-tenant load.

