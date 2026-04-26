## Outbound Workers

Control external fetch from user Workers:

### Configure
```typescript
const userWorker = env.DISPATCHER.get(
  workerName, {},
  { outbound: { customer_context: { customer_name: workerName, url: request.url } } }
);
```

### Implement
```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const customerName = env.customer_name;
    const url = new URL(request.url);
    
    // Block domains
    if (["malicious.com"].some(d => url.hostname.includes(d))) {
      return new Response("Blocked", { status: 403 });
    }
    
    // Inject auth
    if (url.hostname === "api.example.com") {
      const headers = new Headers(request.headers);
      headers.set("Authorization", `Bearer ${generateJWT(customerName)}`);
      return fetch(new Request(request, { headers }));
    }
    
    return fetch(request);
  },
};
```

**Note:** Doesn't intercept DO/mTLS fetch.

See [README.md](./README.md), [configuration.md](./configuration.md), [patterns.md](./patterns.md), [gotchas.md](./gotchas.md)
