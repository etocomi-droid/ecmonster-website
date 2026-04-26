## 9. Log to D1

```typescript
import PostalMime from 'postal-mime';

interface Env { DB: D1Database; }

export default {
  async email(message, env, ctx) {
    const parser = new PostalMime();
    const email = await parser.parse(await message.raw.arrayBuffer());
    
    ctx.waitUntil(
      env.DB.prepare("INSERT INTO log (ts, from_addr, subj) VALUES (?, ?, ?)")
        .bind(new Date().toISOString(), email.from.address, email.subject || "")
        .run()
    );
    
    await message.forward("inbox@corp.com");
  }
} satisfies ExportedHandler<Env>;
```

