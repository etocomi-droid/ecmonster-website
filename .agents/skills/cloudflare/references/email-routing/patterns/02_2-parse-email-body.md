## 2. Parse Email Body

```typescript
import PostalMime from 'postal-mime';

export default {
  async email(message, env, ctx) {
    // CRITICAL: Consume stream immediately
    const raw = await message.raw.arrayBuffer();
    
    const parser = new PostalMime();
    const email = await parser.parse(raw);
    
    console.log({
      subject: email.subject,
      text: email.text,
      html: email.html,
      from: email.from.address,
      attachments: email.attachments.length
    });
    
    await message.forward("inbox@corp.com");
  }
} satisfies ExportedHandler;
```

