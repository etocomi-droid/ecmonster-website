## Format Negotiation

```typescript
async fetch(request: Request, env: Env): Promise<Response> {
  const accept = request.headers.get('Accept') || '';
  const format = /image\/avif/.test(accept) ? 'avif' : /image\/webp/.test(accept) ? 'webp' : 'jpeg';
  return env.IMAGES.input(buffer).transform({ format, quality: 85 }).output().response();
}
```

