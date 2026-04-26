## TypeScript

```typescript
interface Env {
  ANALYTICS: AnalyticsEngineDataset;
}

export default {
  async fetch(request: Request, env: Env) {
    // No await - returns void, fire-and-forget
    env.ANALYTICS.writeDataPoint({
      blobs: [pathname, method, status],      // String dimensions (max 20)
      doubles: [latency, 1],                   // Numeric metrics (max 20)
      indexes: [apiKey]                        // High-cardinality filter (max 1)
    });
    return response;
  }
};
```

