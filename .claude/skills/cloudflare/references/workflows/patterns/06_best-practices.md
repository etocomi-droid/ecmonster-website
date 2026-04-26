## Best Practices

### ✅ DO

1. **Granular steps**: One API call per step (unless proving idempotency)
2. **Idempotency**: Check-then-execute; use idempotency keys
3. **Deterministic names**: Use static or step-output-based names
4. **Return state**: Persist via step returns, not variables
5. **Always await**: `await step.do()`, avoid dangling promises
6. **Deterministic conditionals**: Base on `event.payload` or step outputs
7. **Store large data externally**: R2/KV for >1 MiB, return refs
8. **Batch creation**: `createBatch()` for multiple instances

### ❌ DON'T

1. **One giant step**: Breaks durability & retry control
2. **State outside steps**: Lost on hibernation
3. **Mutate events**: Events immutable, return new state
4. **Non-deterministic logic outside steps**: `Math.random()`, `Date.now()` must be in steps
5. **Side effects outside steps**: May duplicate on restart
6. **Non-deterministic step names**: Prevents caching
7. **Ignore timeouts**: `waitForEvent` throws, use try-catch
8. **Reuse instance IDs**: Must be unique within retention

