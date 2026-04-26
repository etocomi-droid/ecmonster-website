### Configure Analytics Engine

**Bind to Worker**:
```toml
# wrangler.toml
analytics_engine_datasets = [
  { binding = "ANALYTICS", dataset = "api_metrics" }
]
```

**Write Data Points**:
```typescript
export interface Env {
  ANALYTICS: AnalyticsEngineDataset;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Track metrics
    env.ANALYTICS.writeDataPoint({
      blobs: ['customer_123', 'POST', '/api/v1/users'],
      doubles: [1, 245.5], // request_count, response_time_ms
      indexes: ['customer_123'] // for efficient filtering
    });
    
    return new Response('OK');
  }
}
```

