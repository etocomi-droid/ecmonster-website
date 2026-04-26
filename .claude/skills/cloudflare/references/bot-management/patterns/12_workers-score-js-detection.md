## Workers: Score + JS Detection

```typescript
import type { IncomingRequestCfProperties } from '@cloudflare/workers-types';

export default {
  async fetch(request: Request): Promise<Response> {
    const cf = request.cf as IncomingRequestCfProperties | undefined;
    const botMgmt = cf?.botManagement;
    const url = new URL(request.url);
    
    if (botMgmt?.staticResource) return fetch(request); // Skip static
    
    // API endpoints: require JS detection + good score
    if (url.pathname.startsWith('/api/')) {
      const jsDetectionPassed = botMgmt?.jsDetection?.passed ?? false;
      const score = botMgmt?.score ?? 100;
      
      if (!jsDetectionPassed || score < 30) {
        return new Response('Unauthorized', { status: 401 });
      }
    }
    
    return fetch(request);
  }
};
```

