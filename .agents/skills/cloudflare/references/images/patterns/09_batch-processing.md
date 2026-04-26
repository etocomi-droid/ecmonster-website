## Batch Processing

```typescript
const results = await Promise.all(images.map(buffer =>
  env.IMAGES.input(buffer).transform({ width: 800, fit: 'cover', format: 'avif' }).output()
));
```

