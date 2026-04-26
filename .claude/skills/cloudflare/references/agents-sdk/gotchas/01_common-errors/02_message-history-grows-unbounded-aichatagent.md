### "Message history grows unbounded (AIChatAgent)"

**Cause:** `this.messages` in `AIChatAgent` accumulates all messages indefinitely  
**Solution:** Manually trim old messages periodically:
```ts
export class ChatAgent extends AIChatAgent<Env> {
  async onChatMessage(onFinish) {
    // Keep only last 50 messages
    if (this.messages.length > 50) {
      this.messages = this.messages.slice(-50);
    }
    
    return this.streamText({ model: openai("gpt-4"), messages: this.messages, onFinish });
  }
}
```

