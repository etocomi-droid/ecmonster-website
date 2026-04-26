## TypeScript Types

```typescript
interface Env { MY_BUCKET: R2Bucket; }

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const object = await env.MY_BUCKET.get('file.txt');
    return new Response(object?.body);
  }
}
```

