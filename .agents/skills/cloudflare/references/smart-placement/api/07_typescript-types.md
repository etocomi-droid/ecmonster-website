## TypeScript Types

```typescript
// Placement status returned by API (field may be absent)
type PlacementStatus = 
  | 'SUCCESS'
  | 'INSUFFICIENT_INVOCATIONS'
  | 'UNSUPPORTED_APPLICATION'
  | undefined;

// Placement configuration in wrangler.jsonc
type PlacementMode = 'smart' | 'off';

interface PlacementConfig {
  mode: PlacementMode;
  // Legacy fields (deprecated/removed):
  // hint?: string;  // REMOVED - no longer supported
}

// Explicit placement (separate feature from Smart Placement)
interface ExplicitPlacementConfig {
  region?: string;
  host?: string;
  hostname?: string;
  // Cannot combine with mode field
}

// Worker metadata from API response
interface WorkerMetadata {
  placement?: PlacementConfig | ExplicitPlacementConfig;
  placement_status?: PlacementStatus;
}

// Service Binding for backend Worker
interface Env {
  BACKEND_SERVICE: Fetcher;  // Service Binding to backend Worker
  DATABASE: D1Database;
}

// Example Worker with Service Binding
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Forward to backend Worker with Smart Placement enabled
    const response = await env.BACKEND_SERVICE.fetch(request);
    return response;
  }
} satisfies ExportedHandler<Env>;
```
