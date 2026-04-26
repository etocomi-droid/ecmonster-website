### "unstable_startWorker not found"

**Cause:** Using outdated API
**Solution:** Use stable `startWorker` instead:
```typescript
import { startWorker } from "wrangler";  // Not unstable_startWorker
```

