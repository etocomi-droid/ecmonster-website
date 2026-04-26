## Best Practices

### 1. Always Enable Tiered Cache

```typescript
// Cache Reserve is designed for use WITH Tiered Cache
const configuration = {
  tieredCache: 'enabled',    // Required for optimal performance
  cacheReserve: 'enabled',   // Works best with Tiered Cache
  
  hierarchy: [
    'Lower-Tier Cache (visitor)',
    'Upper-Tier Cache (origin region)',
    'Cache Reserve (persistent)',
    'Origin'
  ]
};
```

### 2. Set Appropriate Cache-Control Headers

```typescript
// Origin response headers for Cache Reserve eligibility
const originHeaders = {
  'Cache-Control': 'public, max-age=86400', // 24hr (minimum 10hr)
  'Content-Length': '1024000', // Required
  'Cache-Tag': 'images,product-123', // Optional: purging
  'ETag': '"abc123"', // Optional: revalidation
  // Avoid: 'Set-Cookie' and 'Vary: *' prevent caching
};
```

### 3. Use Cache Rules for Fine-Grained Control

```typescript
// Different TTLs for different content types
const cacheRules = [
  {
    description: 'Long-term cache for immutable assets',
    expression: '(http.request.uri.path matches "^/static/.*\\.[a-f0-9]{8}\\.")',
    action_parameters: {
      cache_reserve: { eligible: true },
      edge_ttl: { mode: 'override_origin', default: 2592000 }, // 30 days
      cache: true
    }
  },
  {
    description: 'Moderate cache for regular images',
    expression: '(http.request.uri.path matches "\\.(jpg|png|webp)$")',
    action_parameters: {
      cache_reserve: { eligible: true },
      edge_ttl: { mode: 'override_origin', default: 86400 }, // 24 hours
      cache: true
    }
  },
  {
    description: 'Exclude API from Cache Reserve',
    expression: '(http.request.uri.path matches "^/api/")',
    action_parameters: { cache_reserve: { eligible: false }, cache: false }
  }
];
```

### 4. Making Assets Cache Reserve Eligible from Workers

**Note**: This modifies response headers to meet eligibility criteria but does NOT directly control Cache Reserve storage (which is zone-level automatic).

```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const response = await fetch(request);
    if (!response.ok) return response;
    
    const headers = new Headers(response.headers);
    headers.set('Cache-Control', 'public, max-age=36000'); // 10hr minimum
    headers.delete('Set-Cookie'); // Blocks caching
    
    // Ensure Content-Length present
    if (!headers.has('Content-Length')) {
      const blob = await response.blob();
      headers.set('Content-Length', blob.size.toString());
      return new Response(blob, { status: response.status, headers });
    }
    
    return new Response(response.body, { status: response.status, headers });
  }
};
```

### 5. Hostname Best Practices

Use Worker's hostname for efficient caching - avoid overriding hostname unnecessarily.

