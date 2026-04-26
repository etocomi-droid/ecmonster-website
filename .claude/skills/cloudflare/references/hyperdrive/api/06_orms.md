## ORMs

**Drizzle:**
```typescript
import { drizzle } from "drizzle-orm/postgres-js";  // drizzle-orm@^0.45.1
import postgres from "postgres";

const client = postgres(env.HYPERDRIVE.connectionString, {max: 5, prepare: true});
const db = drizzle(client);
const users = await db.select().from(users).where(eq(users.active, true)).limit(10);
```

**Kysely:**
```typescript
import { Kysely, PostgresDialect } from "kysely";  // kysely@^0.27+
import postgres from "postgres";

const db = new Kysely({
  dialect: new PostgresDialect({
    postgres: postgres(env.HYPERDRIVE.connectionString, {max: 5, prepare: true}),
  }),
});
const users = await db.selectFrom("users").selectAll().where("active", "=", true).execute();
```

See [patterns.md](./patterns.md) for use cases, [gotchas.md](./gotchas.md) for limits.
