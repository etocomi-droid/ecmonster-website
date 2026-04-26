## Filtering

```typescript
// Allowlist from KV
const allowList = await env.ALLOWED_SENDERS.get('list', 'json') || [];
if (!allowList.includes(message.from)) {
  message.setReject('Not allowed');
  return;
}

// Size check (avoid parsing large emails)
if (message.rawSize > 5_000_000) {
  await message.forward('inbox@example.com'); // Forward without parsing
  return;
}
```

