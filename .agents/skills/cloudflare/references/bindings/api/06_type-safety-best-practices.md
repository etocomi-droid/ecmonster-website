## Type Safety Best Practices

1. **Never use `any` for env:**
```typescript
// ❌ BAD
async fetch(request: Request, env: any) { }

// ✅ GOOD
async fetch(request: Request, env: Env) { }
```

2. **Run wrangler types after config changes:**
```bash
# After editing wrangler.jsonc
npx wrangler types
```

3. **Check generated types match config:**
```bash
# View generated Env interface
cat .wrangler/types/runtime.d.ts
```

