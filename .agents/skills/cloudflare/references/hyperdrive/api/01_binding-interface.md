## Binding Interface

```typescript
interface Hyperdrive {
  connectionString: string;  // PostgreSQL
  // MySQL properties:
  host: string;
  port: number;
  user: string;
  password: string;
  database: string;
}

interface Env {
  HYPERDRIVE: Hyperdrive;
}
```

**Generate types:** `npx wrangler types` (auto-creates worker-configuration.d.ts from wrangler.jsonc)

