## Device-Based Transforms

```typescript
const ua = request.headers.get('User-Agent') || '';
const isMobile = /Mobile|Android|iPhone/i.test(ua);
return env.IMAGES.input(buffer)
  .transform({ width: isMobile ? 400 : 1200, quality: isMobile ? 75 : 85, format: 'avif' })
  .output().response();
```

