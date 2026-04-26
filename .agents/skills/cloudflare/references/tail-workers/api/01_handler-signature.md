## Handler Signature

```typescript
export default {
  async tail(
    events: TraceItem[],
    env: Env,
    ctx: ExecutionContext
  ): Promise<void> {
    // Process events
  }
} satisfies ExportedHandler<Env>;
```

**Parameters:**
- `events`: Array of `TraceItem` objects (one per producer invocation)
- `env`: Bindings (KV, D1, R2, env vars, etc.)
- `ctx`: Context with `waitUntil()` for async work

**CRITICAL:** Tail handlers don't return values. Use `ctx.waitUntil()` for async operations.

