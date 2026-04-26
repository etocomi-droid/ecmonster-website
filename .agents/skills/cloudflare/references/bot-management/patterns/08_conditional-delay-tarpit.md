## Conditional Delay (Tarpit)

```typescript
import type { IncomingRequestCfProperties } from '@cloudflare/workers-types';

// Add delay proportional to bot suspicion
export default {
  async fetch(request: Request): Promise<Response> {
    const cf = request.cf as IncomingRequestCfProperties | undefined;
    const botMgmt = cf?.botManagement;
    
    if (botMgmt?.score && botMgmt.score < 50 && !botMgmt.verifiedBot) {
      // Delay: 0-2 seconds for scores 50-0
      const delayMs = Math.max(0, (50 - botMgmt.score) * 40);
      await new Promise(r => setTimeout(r, delayMs));
    }
    
    return fetch(request);
  }
};
```

