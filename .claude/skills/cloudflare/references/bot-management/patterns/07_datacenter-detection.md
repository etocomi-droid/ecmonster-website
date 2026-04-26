## Datacenter Detection

```typescript
import type { IncomingRequestCfProperties } from '@cloudflare/workers-types';

// Low score + not corporate proxy = likely datacenter bot
export default {
  async fetch(request: Request): Promise<Response> {
    const cf = request.cf as IncomingRequestCfProperties | undefined;
    const botMgmt = cf?.botManagement;
    
    if (botMgmt?.score && botMgmt.score < 30 && 
        !botMgmt.corporateProxy && !botMgmt.verifiedBot) {
      return new Response('Datacenter traffic blocked', { status: 403 });
    }
    
    return fetch(request);
  }
};
```

