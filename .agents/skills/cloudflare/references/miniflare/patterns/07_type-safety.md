## Type Safety

```ts
import type { KVNamespace } from "@cloudflare/workers-types";

interface Env {
  KV: KVNamespace;
  API_KEY: string;
}

const env = await mf.getBindings<Env>();
await env.KV.put("key", "value"); // Typed!

export default {
  async fetch(req: Request, env: Env) {
    return new Response(await env.KV.get("key"));
  }
} satisfies ExportedHandler<Env>;
```

