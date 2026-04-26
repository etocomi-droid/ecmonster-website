## Error Handling

```typescript
try {
  return (await env.IMAGES.input(buffer).transform({ width: 800 }).output()).response();
} catch (error) {
  console.error('Transform failed:', error);
  return new Response('Image processing failed', { status: 500 });
}
```
