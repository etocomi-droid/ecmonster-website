## Type Generation Workflow

### Initial Setup

```bash
# Install wrangler
npm install -D wrangler

# Generate types from wrangler.jsonc
npx wrangler types
```

### After Changing Bindings

```bash
# Added/modified binding in wrangler.jsonc
npx wrangler types

# TypeScript now sees updated Env interface
```

**Note:** `wrangler types` outputs to `.wrangler/types/runtime.d.ts`. TypeScript picks this up automatically if `@cloudflare/workers-types` is in `tsconfig.json` `"types"` array.

