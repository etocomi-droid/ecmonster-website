## Binding API

### Basic Access

**CRITICAL**: Async `.get()` required - secrets NOT directly available.

**`.get()` throws on error** - does NOT return null. Always use try/catch.

```typescript
interface Env {
  API_KEY: { get(): Promise<string> };
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const apiKey = await env.API_KEY.get();
    return fetch("https://api.example.com", {
      headers: { "Authorization": `Bearer ${apiKey}` }
    });
  }
}
```

### Error Handling

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    try {
      const apiKey = await env.API_KEY.get();
      return fetch("https://api.example.com", {
        headers: { "Authorization": `Bearer ${apiKey}` }
      });
    } catch (error) {
      console.error("Secret access failed:", error);
      return new Response("Configuration error", { status: 500 });
    }
  }
}
```

### Multiple Secrets & Patterns

```typescript
// Parallel fetch
const [stripeKey, sendgridKey] = await Promise.all([
  env.STRIPE_KEY.get(),
  env.SENDGRID_KEY.get()
]);

// ❌ Missing .get()
const key = env.API_KEY;

// ❌ Module-level cache
const CACHED_KEY = await env.API_KEY.get(); // Fails

// ✅ Request-scope cache
const key = await env.API_KEY.get(); // OK - reuse within request
```

