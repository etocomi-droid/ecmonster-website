## 8. Extract Attachments

```typescript
import PostalMime from 'postal-mime';

interface Env { ATTACHMENTS: R2Bucket; }

export default {
  async email(message, env, ctx) {
    const parser = new PostalMime();
    const email = await parser.parse(await message.raw.arrayBuffer());
    
    for (const att of email.attachments) {
      const key = `${Date.now()}-${att.filename}`;
      await env.ATTACHMENTS.put(key, att.content, {
        httpMetadata: { contentType: att.mimeType }
      });
    }
    
    await message.forward("inbox@corp.com");
  }
} satisfies ExportedHandler<Env>;
```

