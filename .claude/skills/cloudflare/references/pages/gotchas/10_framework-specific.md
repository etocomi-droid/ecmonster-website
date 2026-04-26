## Framework-Specific

### ⚠️ Deprecated Frameworks

**Next.js**: Official adapter (`@cloudflare/next-on-pages`) **deprecated** and unmaintained.
- **Problem**: No updates since 2024; incompatible with Next.js 15+; missing App Router features
- **Cause**: Cloudflare discontinued official support; community fork exists but limited
- **Solutions**:
  1. **Recommended**: Use Vercel (official Next.js host)
  2. **Advanced**: Self-host on Workers using custom adapter (complex, unsupported)
  3. **Migration**: Switch to SvelteKit/Nuxt (similar DX, full Pages support)

**Remix**: Official adapter (`@remix-run/cloudflare-pages`) **deprecated**.
- **Problem**: No maintenance from Remix team; compatibility issues with Remix v2+
- **Cause**: Remix team deprecated all framework adapters
- **Solutions**:
  1. **Recommended**: Migrate to SvelteKit (similar file-based routing, better DX)
  2. **Alternative**: Use Astro (static-first with optional SSR)
  3. **Workaround**: Continue using deprecated adapter (no future support)

### ✅ Supported Frameworks

**SvelteKit**:
- Use `@sveltejs/adapter-cloudflare`
- Access bindings via `platform.env` in server load functions
- Set `platform: 'cloudflare'` in `svelte.config.js`

**Astro**:
- Built-in Cloudflare adapter
- Access bindings via `Astro.locals.runtime.env`

**Nuxt**:
- Set `nitro.preset: 'cloudflare-pages'` in `nuxt.config.ts`
- Access bindings via `event.context.cloudflare.env`

**Qwik, Solid Start**:
- Built-in or official Cloudflare adapters available
- Check respective framework docs for binding access

