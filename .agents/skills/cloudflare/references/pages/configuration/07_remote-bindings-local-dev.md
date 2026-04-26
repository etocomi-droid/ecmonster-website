## Remote Bindings (Local Dev)

Connect local dev server to production bindings instead of local mocks:

```bash
# All bindings remote
npx wrangler pages dev ./dist --remote

# Specific bindings remote (others local)
npx wrangler pages dev ./dist --remote --kv=KV --d1=DB
```

**Use cases**:
- Test against production data (read-only operations)
- Debug binding-specific behavior
- Validate changes before deployment

**⚠️ Warning**: 
- Writes affect **real production data**
- Use only for read-heavy debugging or with non-production accounts
- Consider creating separate preview environments instead

**Requirements**: Must be logged in (`npx wrangler login`) with access to bindings.

