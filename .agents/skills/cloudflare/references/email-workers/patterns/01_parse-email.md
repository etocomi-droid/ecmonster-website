## Parse Email

```typescript
import PostalMime from 'postal-mime';

export default {
  async email(message, env, ctx) {
    const buffer = await new Response(message.raw).arrayBuffer();
    const email = await PostalMime.parse(buffer);
    console.log(email.from, email.subject, email.text, email.attachments.length);
    await message.forward('inbox@example.com');
  }
};
```

