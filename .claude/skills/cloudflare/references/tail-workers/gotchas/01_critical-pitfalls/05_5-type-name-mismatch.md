### 5. Type Name Mismatch

**Problem:** Using `TailItem` type  
**Cause:** Old docs used `TailItem`, SDK uses `TraceItem`

```typescript
import type { TraceItem } from '@cloudflare/workers-types';
export default {
  async tail(events: TraceItem[], env, ctx) { /* ... */ }
};
```

