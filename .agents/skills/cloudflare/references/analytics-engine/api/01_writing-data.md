## Writing Data

### `writeDataPoint()`

Fire-and-forget (returns `void`, not Promise). Writes happen asynchronously.

```typescript
interface AnalyticsEngineDataPoint {
  blobs?: string[];      // Up to 20 strings (dimensions), 16KB each
  doubles?: number[];    // Up to 20 numbers (metrics)
  indexes?: string[];    // 1 indexed string for high-cardinality filtering
}

env.ANALYTICS.writeDataPoint({
  blobs: ["/api/users", "GET", "200"],
  doubles: [145.2, 1],  // latency_ms, count
  indexes: ["customer_abc123"]
});
```

**Behaviors:** No await needed, no error thrown (check tail logs), auto-sampled at high volumes, auto-timestamped.

**Blob vs Index:** Blob for GROUP BY (<100k unique), Index for filter-only (millions unique).

### Full Example

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const start = Date.now();
    const url = new URL(request.url);
    try {
      const response = await handleRequest(request);
      env.ANALYTICS.writeDataPoint({
        blobs: [url.pathname, request.method, response.status.toString()],
        doubles: [Date.now() - start, 1],
        indexes: [request.headers.get("x-api-key") || "anonymous"]
      });
      return response;
    } catch (error) {
      env.ANALYTICS.writeDataPoint({
        blobs: [url.pathname, request.method, "500"],
        doubles: [Date.now() - start, 1, 0],
      });
      throw error;
    }
  }
};
```

