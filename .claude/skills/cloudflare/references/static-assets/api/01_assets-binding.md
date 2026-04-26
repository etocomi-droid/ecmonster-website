## ASSETS Binding

The `ASSETS` binding provides access to static assets via the `Fetcher` interface.

### Type Definition

```typescript
interface Env {
  ASSETS: Fetcher;
}

interface Fetcher {
  fetch(input: RequestInfo | URL, init?: RequestInit): Promise<Response>;
}
```

### Method Signatures

```typescript
// 1. Forward entire request
await env.ASSETS.fetch(request);

// 2. String path (hostname ignored, only path matters)
await env.ASSETS.fetch("https://any-host/path/to/asset.png");

// 3. URL object
await env.ASSETS.fetch(new URL("/index.html", request.url));

// 4. Constructed Request object
await env.ASSETS.fetch(new Request(new URL("/logo.png", request.url), {
  method: "GET",
  headers: request.headers
}));
```

**Key behaviors:**

- Host/origin is ignored for string/URL inputs (only path is used)
- Method must be GET (others return 405)
- Request headers pass through (affects response)
- Returns standard `Response` object

