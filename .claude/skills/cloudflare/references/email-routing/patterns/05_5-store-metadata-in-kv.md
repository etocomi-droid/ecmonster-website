## 5. Store Metadata in KV

```typescript
import PostalMime from 'postal-mime';

interface Env { KV: KVNamespace; }

export default {
  async email(message, env, ctx) {
    const raw = await message.raw.arrayBuffer();
    const parser = new PostalMime();
    const email = await parser.parse(raw);
    
    const metadata = {
      from: email.from.address,
      subject: email.subject,
      timestamp: new Date().toISOString(),
      size: raw.byteLength
    };
    
    await env.KV.put(`email:${Date.now()}`, JSON.stringify(metadata));
    await message.forward("inbox@corp.com");
  }
} satisfies ExportedHandler<Env>;
```

