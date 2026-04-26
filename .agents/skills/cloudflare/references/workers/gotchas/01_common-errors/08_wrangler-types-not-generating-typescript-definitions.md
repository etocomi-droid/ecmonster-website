### "wrangler types not generating TypeScript definitions"

**Cause:** Type generation not configured or outdated  
**Solution:** Run `npx wrangler types` after changing bindings in wrangler.jsonc:

```bash
npx wrangler types  # Generates .wrangler/types/runtime.d.ts
```

Add to `tsconfig.json`: `"include": [".wrangler/types/**/*.ts"]`

Then import: `import type { Env } from './.wrangler/types/runtime';`

