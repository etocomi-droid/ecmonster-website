## Advanced Usage

### Modifying Responses

```typescript
const response = await env.ASSETS.fetch(request);

// Clone and modify
return new Response(response.body, {
  status: response.status,
  headers: {
    ...Object.fromEntries(response.headers),
    'Cache-Control': 'public, max-age=31536000',
    'X-Custom': 'value'
  }
});
```

See patterns.md:27-35 for full example.

### Error Handling

```typescript
const response = await env.ASSETS.fetch(request);

if (!response.ok) {
  // Asset not found or error
  return new Response('Custom error page', { status: 404 });
}

return response;
```

### Conditional Serving

```typescript
const url = new URL(request.url);

// Serve different assets based on conditions
if (url.pathname === '/') {
  return env.ASSETS.fetch('/index.html');
}

return env.ASSETS.fetch(request);
```

See patterns.md for complete patterns.
