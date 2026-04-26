## Common Patterns

### Error Handling
```javascript
export default {
  async fetch(request, env, ctx) {
    try {
      return await handleRequest(request, env);
    } catch (error) {
      console.error("Request failed", error);
      return new Response("Internal Error", {status: 500});
    }
  }
};
```

### Background Tasks
```javascript
export default {
  async fetch(request, env, ctx) {
    const response = new Response("OK");
    
    // Fire-and-forget background work
    ctx.waitUntil(
      env.ANALYTICS.put(request.url, Date.now())
    );
    
    return response;
  }
};
```

See [configuration.md](./configuration.md) for config syntax, [api.md](./api.md) for runtime APIs, [gotchas.md](./gotchas.md) for common errors.
