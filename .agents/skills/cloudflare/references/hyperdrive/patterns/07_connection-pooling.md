## Connection Pooling

Operates in **transaction mode**: connection acquired per transaction, `RESET` on return.

**SET statements:**
```typescript
// ✅ Within transaction
await client.query("BEGIN");
await client.query("SET work_mem = '256MB'");
await client.query("SELECT * FROM large_table");  // Uses SET
await client.query("COMMIT");  // RESET after

// ✅ Single statement
await client.query("SET work_mem = '256MB'; SELECT * FROM large_table");

// ❌ Across queries (may get different connection)
await client.query("SET work_mem = '256MB'");
await client.query("SELECT * FROM large_table");  // SET not applied
```

**Best practices:**
```typescript
// ❌ Long transactions block pooling
await client.query("BEGIN");
await processThousands();  // Connection held entire time
await client.query("COMMIT");

// ✅ Short transactions
await client.query("BEGIN");
await client.query("UPDATE users SET status = $1 WHERE id = $2", [status, id]);
await client.query("COMMIT");

// ✅ SET LOCAL within transaction
await client.query("BEGIN");
await client.query("SET LOCAL work_mem = '256MB'");
await client.query("SELECT * FROM large_table");
await client.query("COMMIT");
```

