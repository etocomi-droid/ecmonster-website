## MySQL (mysql2)

```typescript
import { createConnection } from "mysql2/promise";  // mysql2@^3.16.2

const conn = await createConnection({
  host: env.HYPERDRIVE.host,
  user: env.HYPERDRIVE.user,
  password: env.HYPERDRIVE.password,
  database: env.HYPERDRIVE.database,
  port: env.HYPERDRIVE.port,
  disableEval: true,  // ⚠️ REQUIRED for Workers
});

const [results] = await conn.query("SELECT * FROM users WHERE active = ? LIMIT ?", [true, 10]);
ctx.waitUntil(conn.end());
```

**⚠️ MySQL support is less mature than PostgreSQL** - expect fewer optimizations and potential edge cases.

