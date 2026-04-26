## Workers: BotManagement Interface

```typescript
interface BotManagement {
  score: number;              // 1-99 (Enterprise), 0 if not computed
  verifiedBot: boolean;       // Is verified bot
  staticResource: boolean;    // Serves static resource
  ja3Hash: string;            // JA3 fingerprint (Enterprise, HTTPS only)
  ja4: string;                // JA4 fingerprint (Enterprise, HTTPS only)
  jsDetection?: {
    passed: boolean;          // Passed JS detection (if enabled)
  };
  detectionIds: number[];     // Heuristic detection IDs
  corporateProxy?: boolean;   // From corporate proxy (Enterprise)
}

// DEPRECATED: Use botManagement.score instead
// request.cf.clientTrustScore (legacy, duplicate of botManagement.score)

// Access via request.cf
import type { IncomingRequestCfProperties } from '@cloudflare/workers-types';

export default {
  async fetch(request: Request): Promise<Response> {
    const cf = request.cf as IncomingRequestCfProperties | undefined;
    const botMgmt = cf?.botManagement;
    
    if (!botMgmt) return fetch(request);
    if (botMgmt.verifiedBot) return fetch(request); // Allow verified bots
    if (botMgmt.score === 1) return new Response('Blocked', { status: 403 });
    if (botMgmt.score < 30) return new Response('Challenge required', { status: 429 });
    
    return fetch(request);
  }
};
```

