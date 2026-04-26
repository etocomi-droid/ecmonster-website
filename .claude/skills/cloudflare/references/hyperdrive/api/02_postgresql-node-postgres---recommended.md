## PostgreSQL (node-postgres) - RECOMMENDED

```typescript
import { Client } from "pg";  // pg@^8.17.2

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const client = new Client({connectionString: env.HYPERDRIVE.connectionString});
    try {
      await client.connect();
      const result = await client.query("SELECT * FROM users WHERE id = $1", [123]);
      return Response.json(result.rows);
    } finally {
      await client.end();
    }
  },
};
```

**⚠️ Workers connection limit: 6 per Worker invocation** - use connection pooling wisely.

