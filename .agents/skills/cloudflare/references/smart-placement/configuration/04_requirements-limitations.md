## Requirements & Limitations

### Requirements
- **Wrangler version:** 2.20.0+
- **Analysis time:** Up to 15 minutes
- **Traffic requirements:** Consistent multi-location traffic
- **Workers plan:** All plans (Free, Paid, Enterprise)

### What Smart Placement Affects

**CRITICAL LIMITATION - Smart Placement ONLY Affects `fetch` Handlers:**

Smart Placement is fundamentally limited to Workers with default `fetch` handlers. This is a key architectural constraint.

- ✅ **Affects:** `fetch` event handlers ONLY (the default export's fetch method)
- ❌ **Does NOT affect:** 
  - RPC methods (Service Bindings with `WorkerEntrypoint` - see example below)
  - Named entrypoints (exports other than `default`)
  - Workers without `fetch` handlers
  - Queue consumers, scheduled handlers, or other event types

**Example - Smart Placement ONLY affects `fetch`:**
```typescript
// ✅ Smart Placement affects this:
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // This runs close to backend when Smart Placement enabled
    const data = await env.DATABASE.prepare('SELECT * FROM users').all();
    return Response.json(data);
  }
}

// ❌ Smart Placement DOES NOT affect these:
export class MyRPC extends WorkerEntrypoint {
  async myMethod() { 
    // This ALWAYS runs at edge, Smart Placement has NO EFFECT
    const data = await this.env.DATABASE.prepare('SELECT * FROM users').all();
    return data;
  }
}

export async function scheduled(event: ScheduledEvent, env: Env) {
  // NOT affected by Smart Placement
}
```

**Consequence:** If your backend logic uses RPC methods (`WorkerEntrypoint`), Smart Placement cannot optimize those calls. You must use fetch-based patterns for Smart Placement to work.

**Solution:** Convert RPC methods to fetch endpoints, or use a wrapper Worker with `fetch` handler that calls your backend RPC (though this adds latency).

### Baseline Traffic
Smart Placement automatically routes 1% of requests WITHOUT optimization as baseline for performance comparison.

### Validation Rules

**Mutually exclusive fields:**
- `mode` cannot be used with explicit placement fields (`region`, `host`, `hostname`)
- Choose either Smart Placement OR explicit placement, not both

```jsonc
// ✅ Valid - Smart Placement
{ "placement": { "mode": "smart" } }

// ✅ Valid - Explicit Placement (different feature)
{ "placement": { "region": "us-east1" } }

// ❌ Invalid - Cannot combine
{ "placement": { "mode": "smart", "region": "us-east1" } }
```

