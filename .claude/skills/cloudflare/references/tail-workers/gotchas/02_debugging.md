## Debugging

**View logs:** `wrangler tail my-tail-worker`

**Incremental testing:**
1. Verify receipt: `console.log('Events:', events.length)`
2. Inspect structure: `console.log(JSON.stringify(events[0], null, 2))`
3. Add external call with `ctx.waitUntil()`

**Monitor dashboard:** Check invocation count (matches producer?), error rate, CPU time

