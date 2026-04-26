## 7. Auto-Reply

```typescript
interface Env {
  EMAIL: SendEmail;
  REPLIED: KVNamespace;
}

export default {
  async email(message, env, ctx) {
    const msgId = message.headers.get("message-id");
    
    if (msgId && await env.REPLIED.get(msgId)) {
      await message.forward("archive@corp.com");
      return;
    }
    
    ctx.waitUntil((async () => {
      await env.EMAIL.send({
        from: "noreply@yourdomain.com",
        to: message.from,
        subject: "Re: " + (message.headers.get("subject") || ""),
        text: "Thank you. We'll respond within 24h."
      });
      if (msgId) await env.REPLIED.put(msgId, "1", { expirationTtl: 604800 });
    })());
    
    await message.forward("support@corp.com");
  }
} satisfies ExportedHandler<Env>;
```

