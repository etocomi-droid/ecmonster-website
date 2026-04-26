### Vite Plugin Integration

For Vite-based projects, use `@cloudflare/vite-plugin`:

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import { cloudflare } from '@cloudflare/vite-plugin';

export default defineConfig({
  plugins: [
    cloudflare({
      assets: {
        directory: './dist',
        binding: 'ASSETS'
      }
    })
  ]
});
```

**Features:**

- Automatic asset detection during dev
- Hot module replacement for assets
- Production build integration
- Requires: Wrangler 4.0.0+, `@cloudflare/vite-plugin` 1.0.0+

