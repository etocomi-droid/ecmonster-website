## Wrangler Configuration

### Basic Setup

TCP Sockets are available by default in Workers runtime. No special configuration required in `wrangler.jsonc`:

```jsonc
{
  "name": "private-network-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01"
}
```

### Environment Variables

Store connection details as env vars:

```jsonc
{
  "vars": { "DB_HOST": "10.0.1.50", "DB_PORT": "5432" }
}
```

```typescript
interface Env { DB_HOST: string; DB_PORT: string; }

export default {
  async fetch(req: Request, env: Env): Promise<Response> {
    const socket = connect({ hostname: env.DB_HOST, port: parseInt(env.DB_PORT) });
  }
};
```

### Per-Environment Configuration

```jsonc
{
  "vars": { "DB_HOST": "localhost" },
  "env": {
    "staging": { "vars": { "DB_HOST": "staging-db.internal.net" } },
    "production": { "vars": { "DB_HOST": "prod-db.internal.net" } }
  }
}
```

Deploy: `wrangler deploy --env staging` or `wrangler deploy --env production`

