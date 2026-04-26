## Setup Steps

### 1. Create Tail Worker

Create a Worker with a `tail()` handler:

```typescript
export default {
  async tail(events, env, ctx) {
    // Process events from producer Worker
    ctx.waitUntil(
      fetch(env.LOG_ENDPOINT, {
        method: "POST",
        body: JSON.stringify(events),
      })
    );
  }
};
```

### 2. Configure Producer Worker

In producer's `wrangler.jsonc`:

```jsonc
{
  "name": "my-producer-worker",
  "tail_consumers": [
    {
      "service": "my-tail-worker"
    }
  ]
}
```

### 3. Deploy Both Workers

```bash
# Deploy Tail Worker first
cd tail-worker
wrangler deploy

# Then deploy producer Worker
cd ../producer-worker
wrangler deploy
```

