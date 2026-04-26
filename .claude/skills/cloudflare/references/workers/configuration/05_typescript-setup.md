## TypeScript Setup

### Automatic Type Generation (Recommended)

```bash
npm install -D @cloudflare/workers-types
npx wrangler types  # Generates .wrangler/types/runtime.d.ts from wrangler.jsonc
```

`tsconfig.json`:

```jsonc
{
  "compilerOptions": {
    "target": "ES2022",
    "lib": ["ES2022"],
    "types": ["@cloudflare/workers-types"]
  },
  "include": [".wrangler/types/**/*.ts", "src/**/*"]
}
```

Import generated types:

```typescript
import type { Env } from './.wrangler/types/runtime';

export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    await env.MY_KV.get('key');  // Fully typed, autocomplete works
    return new Response('OK');
  },
};
```

Re-run `npx wrangler types` after changing bindings in wrangler.jsonc

### Manual Type Definition (Legacy)

```typescript
interface Env {
  MY_KV: KVNamespace;
  DB: D1Database;
  API_KEY: string;
}
```

