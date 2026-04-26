### Configure Tail Workers

Tail Workers receive logs/traces from other Workers for filtering, transformation, or export.

**Setup**:
```toml
# wrangler.toml
name = "log-processor"
main = "src/tail.ts"

[[tail_consumers]]
service = "my-worker" # Worker to tail
```

**Tail Worker Example**:
```typescript
export default {
  async tail(events: TraceItem[], env: Env, ctx: ExecutionContext) {
    // Filter errors only
    const errors = events.filter(event => 
      event.outcome === 'exception' || event.outcome === 'exceededCpu'
    );
    
    if (errors.length > 0) {
      // Send to external monitoring
      ctx.waitUntil(
        fetch('https://monitoring.example.com/errors', {
          method: 'POST',
          body: JSON.stringify(errors)
        })
      );
    }
  }
}
```

