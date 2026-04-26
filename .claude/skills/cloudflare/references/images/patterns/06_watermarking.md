## Watermarking

```typescript
const watermark = await env.ASSETS.fetch(new URL('/watermark.png', request.url));
const result = await env.IMAGES
  .input(await image.arrayBuffer())
  .draw(env.IMAGES.input(watermark.body).transform({ width: 100 }), { bottom: 20, right: 20, opacity: 0.7 })
  .transform({ format: 'avif' })
  .output();
return result.response();
```

