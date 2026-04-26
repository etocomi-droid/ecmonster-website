## Framework Integration

**Supported** (2026): SvelteKit, Astro, Nuxt, Qwik, Solid Start

```bash
npm create cloudflare@latest my-app -- --framework=svelte
```

### SvelteKit
```typescript
// src/routes/+page.server.ts
export const load = async ({ platform }) => {
  const todos = await platform.env.DB.prepare('SELECT * FROM todos').all();
  return { todos: todos.results };
};
```

### Astro
```astro
---
const { DB } = Astro.locals.runtime.env;
const todos = await DB.prepare('SELECT * FROM todos').all();
---
<ul>{todos.results.map(t => <li>{t.title}</li>)}</ul>
```

### Nuxt
```typescript
// server/api/todos.get.ts
export default defineEventHandler(async (event) => {
  const { DB } = event.context.cloudflare.env;
  return await DB.prepare('SELECT * FROM todos').all();
});
```

**⚠️ Framework Status** (2026):
- ✅ **Supported**: SvelteKit, Astro, Nuxt, Qwik, Solid Start
- ❌ **Deprecated**: Next.js (`@cloudflare/next-on-pages`), Remix (`@remix-run/cloudflare-pages`)

For deprecated frameworks, see [gotchas.md](./gotchas.md#framework-specific) for migration options.

[Framework Guides](https://developers.cloudflare.com/pages/framework-guides/)

