## Advanced Mode

Full Workers API, bypasses file-based routing:

```javascript
// functions/_worker.js
export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    
    // Custom routing
    if (url.pathname.startsWith('/api/')) {
      return new Response('API response');
    }
    
    // REQUIRED: Serve static assets
    return env.ASSETS.fetch(request);
  }
};
```

**When to use**: WebSockets, complex routing, scheduled handlers, email handlers.

