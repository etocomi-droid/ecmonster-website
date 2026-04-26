### Common Patterns

**1. Forward request to assets:**

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    return env.ASSETS.fetch(request);
  }
};
```

**2. Fetch specific asset by path:**

```typescript
const response = await env.ASSETS.fetch("https://assets.local/logo.png");
```

**3. Modify request before fetching asset:**

```typescript
const url = new URL(request.url);
url.pathname = "/index.html";
return env.ASSETS.fetch(new Request(url, request));
```

**4. Transform asset response:**

```typescript
const response = await env.ASSETS.fetch(request);
const modifiedResponse = new Response(response.body, response);
modifiedResponse.headers.set("X-Custom-Header", "value");
modifiedResponse.headers.set("Cache-Control", "public, max-age=3600");
return modifiedResponse;
```

**5. Conditional asset serving:**

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname === '/') {
      return env.ASSETS.fetch('/index.html');
    }
    return env.ASSETS.fetch(request);
  }
};
```

**6. SPA with API routes:**

Most common full-stack pattern - static SPA with backend API:

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname.startsWith('/api/')) {
      return handleAPI(request, env);
    }
    return env.ASSETS.fetch(request);
  }
};

async function handleAPI(request: Request, env: Env): Promise<Response> {
  return new Response(JSON.stringify({ status: 'ok' }), {
    headers: { 'Content-Type': 'application/json' }
  });
}
```

**Config:** Set `run_worker_first: ["/api/*"]` (see configuration.md:66-106)

**7. Auth gating for protected assets:**

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    if (url.pathname.startsWith('/admin/')) {
      const session = await validateSession(request, env);
      if (!session) {
        return Response.redirect('/login', 302);
      }
    }
    return env.ASSETS.fetch(request);
  }
};
```
