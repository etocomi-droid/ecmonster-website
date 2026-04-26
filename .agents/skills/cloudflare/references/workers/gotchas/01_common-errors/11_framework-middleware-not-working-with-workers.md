### "Framework middleware not working with Workers"

**Cause:** Framework expects Node.js primitives (e.g., Express uses Node streams)  
**Solution:** Use Workers-native frameworks (Hono, itty-router, Worktop) or adapt middleware:

```typescript
// ✅ Hono (Workers-native)
import { Hono } from 'hono';
const app = new Hono();
app.use('*', async (c, next) => { /* middleware */ await next(); });
```

See [frameworks.md](./frameworks.md) for full patterns

