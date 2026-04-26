## Webhook Integration

```typescript
ctx.waitUntil(
  fetch(env.WEBHOOK_URL, {
    method: 'POST',
    body: JSON.stringify({ from: message.from, subject: message.headers.get('Subject') })
  }).catch(err => console.error(err))
);
```
