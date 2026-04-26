### "Resumable stream not resuming"

**Cause:** Stream ID must be deterministic for resumption to work  
**Solution:** Use AIChatAgent (automatic) or ensure consistent stream IDs:
```ts
// AIChatAgent handles this automatically
export class ChatAgent extends AIChatAgent<Env> {
  // Resumption works out of the box
}
```

