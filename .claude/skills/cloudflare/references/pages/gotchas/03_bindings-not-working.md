## Bindings Not Working

**Problem**: `env.BINDING` undefined or errors  
**Causes**: wrangler.jsonc syntax error; wrong binding IDs; missing `.dev.vars`; out-of-sync types  
**Solution**: Validate config, verify IDs, create `.dev.vars`, run `npx wrangler types`

