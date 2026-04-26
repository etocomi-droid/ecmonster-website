## 1. Allowlist/Blocklist

```typescript
// Allowlist
const allowed = ["user@example.com", "trusted@corp.com"];
if (!allowed.includes(message.from)) {
  message.setReject("Not allowed");
  return;
}
await message.forward("inbox@corp.com");
```

