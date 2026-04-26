## Archive & Extract Attachments

```typescript
// Archive to KV
ctx.waitUntil(env.ARCHIVE.put(`email:${Date.now()}`, JSON.stringify({
  from: message.from, subject: email.subject
})));

// Attachments to R2
for (const att of email.attachments) {
  ctx.waitUntil(env.R2.put(`${Date.now()}-${att.filename}`, att.content));
}
```

