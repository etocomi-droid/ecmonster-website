## 4. Archive to R2

```typescript
interface Env { R2: R2Bucket; }

export default {
  async email(message, env, ctx) {
    const raw = await message.raw.arrayBuffer();
    
    const key = `${new Date().toISOString()}-${message.from}.eml`;
    await env.R2.put(key, raw, { 
      httpMetadata: { contentType: "message/rfc822" }
    });
    
    await message.forward("inbox@corp.com");
  }
} satisfies ExportedHandler<Env>;
```

