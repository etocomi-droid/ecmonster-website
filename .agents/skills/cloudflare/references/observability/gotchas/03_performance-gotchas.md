## Performance Gotchas

### Spectre Mitigation Timing

**Problem:** `Date.now()` and `performance.now()` have reduced precision (coarsened to 100μs)
**Cause:** Spectre vulnerability mitigation in V8
**Solution:** Accept reduced precision or use Workers Traces for accurate timing
```typescript
// Date.now() is coarsened - trace spans are accurate
export default {
  async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
    // For user-facing timing, Date.now() is fine
    const start = Date.now();
    const response = await processRequest(request);
    const duration = Date.now() - start;
    
    // For detailed performance analysis, use Workers Traces instead
    return response;
  }
}
```

### Analytics Engine _sample_interval Aggregation

**Problem:** Queries return incorrect totals when not multiplying by `_sample_interval`
**Cause:** Analytics Engine stores sampled data points, each representing multiple events
**Solution:** Always multiply counts/sums by `_sample_interval` in aggregations
```sql
-- WRONG: Undercounts actual events
SELECT blob1 AS customer_id, COUNT(*) AS total_calls
FROM api_usage GROUP BY customer_id;

-- CORRECT: Accounts for sampling
SELECT blob1 AS customer_id, SUM(_sample_interval) AS total_calls
FROM api_usage GROUP BY customer_id;
```

### Trace Context Propagation Limits

**Problem:** Deep call chains lose trace context after 100 spans
**Cause:** Cloudflare limits trace depth to prevent performance impact
**Solution:** Design for flatter architectures or use custom correlation IDs for deep chains
```typescript
// For deep call chains, add custom correlation ID
const correlationId = crypto.randomUUID();
console.log({ correlationId, event: 'request_start' });

// Pass correlationId through headers to downstream services
await fetch('https://api.example.com', {
  headers: { 'X-Correlation-ID': correlationId }
});
```

