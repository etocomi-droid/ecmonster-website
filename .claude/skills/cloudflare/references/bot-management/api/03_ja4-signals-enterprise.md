## JA4 Signals (Enterprise)

```typescript
import type { IncomingRequestCfProperties } from '@cloudflare/workers-types';

interface JA4Signals {
  // Ratios (0.0-1.0)
  heuristic_ratio_1h?: number;  // Fraction flagged by heuristics
  browser_ratio_1h?: number;    // Fraction from real browsers  
  cache_ratio_1h?: number;      // Fraction hitting cache
  h2h3_ratio_1h?: number;       // Fraction using HTTP/2 or HTTP/3
  // Ranks (relative position in distribution)
  uas_rank_1h?: number;         // User-Agent diversity rank
  paths_rank_1h?: number;       // Path diversity rank
  reqs_rank_1h?: number;        // Request volume rank
  ips_rank_1h?: number;         // IP diversity rank
  // Quantiles (0.0-1.0, percentile in distribution)
  reqs_quantile_1h?: number;    // Request volume quantile
  ips_quantile_1h?: number;     // IP count quantile
}

export default {
  async fetch(request: Request): Promise<Response> {
    const cf = request.cf as IncomingRequestCfProperties | undefined;
    const ja4Signals = cf?.ja4Signals as JA4Signals | undefined;
    
    if (!ja4Signals) return fetch(request); // Not available for HTTP or Worker routing
    
    // Check for anomalous behavior
    // High heuristic_ratio or low browser_ratio = suspicious
    const heuristicRatio = ja4Signals.heuristic_ratio_1h ?? 0;
    const browserRatio = ja4Signals.browser_ratio_1h ?? 0;
    
    if (heuristicRatio > 0.5 || browserRatio < 0.3) {
      return new Response('Suspicious traffic', { status: 403 });
    }
    
    return fetch(request);
  }
};
```

