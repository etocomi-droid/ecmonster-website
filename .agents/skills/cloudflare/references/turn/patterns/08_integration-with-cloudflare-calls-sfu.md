## Integration with Cloudflare Calls SFU

```typescript
// TURN is automatically used when needed
// Cloudflare Calls handles TURN + SFU coordination
const session = await callsClient.createSession({
  appId: 'your-app-id',
  sessionId: 'meeting-123'
});
```

