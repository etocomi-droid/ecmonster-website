## getRequestContext (Framework SSR)

Access bindings in framework code:

```typescript
// SvelteKit
import type { RequestEvent } from '@sveltejs/kit';
export async function load({ platform }: RequestEvent) {
  const data = await platform.env.DB.prepare('SELECT * FROM users').all();
  return { users: data.results };
}

// Astro
const { DB } = Astro.locals.runtime.env;
const data = await DB.prepare('SELECT * FROM users').all();

// Solid Start (server function)
import { getRequestEvent } from 'solid-js/web';
const event = getRequestEvent();
const data = await event.locals.runtime.env.DB.prepare('SELECT * FROM users').all();
```

**✅ Supported adapters** (2026):
- **SvelteKit**: `@sveltejs/adapter-cloudflare`
- **Astro**: Built-in Cloudflare adapter
- **Nuxt**: Set `nitro.preset: 'cloudflare-pages'` in `nuxt.config.ts`
- **Qwik**: Built-in Cloudflare adapter
- **Solid Start**: `@solidjs/start-cloudflare-pages`

**❌ Deprecated/Unsupported**:
- **Next.js**: Official adapter (`@cloudflare/next-on-pages`) deprecated. Use Vercel or self-host on Workers.
- **Remix**: Official adapter (`@remix-run/cloudflare-pages`) deprecated. Migrate to supported frameworks.

See [gotchas.md](./gotchas.md#framework-specific) for migration guidance.
