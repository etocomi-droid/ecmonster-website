## Dependencies

```bash
npm install postal-mime
```

```typescript
import PostalMime from 'postal-mime';

export default {
  async email(message, env, ctx) {
    const parser = new PostalMime();
    const email = await parser.parse(await message.raw.arrayBuffer());
    console.log(email.subject);
    await message.forward("inbox@corp.com");
  }
} satisfies ExportedHandler;
```

