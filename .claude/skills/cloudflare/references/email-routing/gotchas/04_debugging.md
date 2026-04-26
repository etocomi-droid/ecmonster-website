## Debugging

### Local

```bash
npx wrangler dev

curl -X POST 'http://localhost:8787/__email' \
  --header 'content-type: message/rfc822' \
  --data 'From: test@example.com
To: you@yourdomain.com
Subject: Test

Body'
```

### Production

```bash
npx wrangler tail
```

### Pattern

```typescript
export default {
  async email(message, env, ctx) {
    try {
      console.log("From:", message.from);
      await process(message, env);
    } catch (err) {
      console.error(err);
      message.setReject(err.message);
    }
  }
} satisfies ExportedHandler;
```

