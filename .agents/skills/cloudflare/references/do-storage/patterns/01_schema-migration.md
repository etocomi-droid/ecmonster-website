## Schema Migration

**Note:** `PRAGMA user_version` is **not supported** in Durable Objects SQLite storage. Use a `_sql_schema_migrations` table instead:

```typescript
export class MyDurableObject extends DurableObject {
  constructor(ctx: DurableObjectState, env: Env) {
    super(ctx, env);
    this.sql = ctx.storage.sql;

    this.sql.exec(`
      CREATE TABLE IF NOT EXISTS _sql_schema_migrations (
        id INTEGER PRIMARY KEY,
        applied_at TEXT NOT NULL DEFAULT (datetime('now'))
      )
    `);

    const ver = this.sql
      .exec<{ version: number }>("SELECT COALESCE(MAX(id), 0) as version FROM _sql_schema_migrations")
      .one().version;

    if (ver < 1) {
      this.sql.exec(`CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT)`);
      this.sql.exec("INSERT INTO _sql_schema_migrations (id) VALUES (1)");
    }
    if (ver < 2) {
      this.sql.exec(`ALTER TABLE users ADD COLUMN email TEXT`);
      this.sql.exec("INSERT INTO _sql_schema_migrations (id) VALUES (2)");
    }
  }
}
```

For production apps, consider [`durable-utils`](https://github.com/lambrospetrou/durable-utils#sqlite-schema-migrations) — provides a `SQLSchemaMigrations` class that tracks executed migrations both in memory and in storage. Also see [`@cloudflare/actors` storage utilities](https://github.com/cloudflare/actors/blob/main/packages/storage/src/sql-schema-migrations.ts) — a reference implementation of the same pattern used by the Cloudflare Actors framework.

