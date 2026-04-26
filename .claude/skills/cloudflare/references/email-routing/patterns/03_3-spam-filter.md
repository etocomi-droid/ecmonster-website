## 3. Spam Filter

```typescript
const score = parseFloat(message.headers.get("x-cf-spamh-score") || "0");
if (score > 5) {
  message.setReject("Spam detected");
  return;
}
await message.forward("inbox@corp.com");
```

