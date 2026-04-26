## Bypassing Redaction

```typescript
export default {
  async tail(events, env, ctx) {
    for (const event of events) {
      // ⚠️ Use with extreme caution
      const unredacted = event.event?.request?.getUnredacted();
      // unredacted.url and unredacted.headers contain raw values
    }
  }
};
```

**Best practices:**
- Only call `getUnredacted()` when absolutely necessary
- Never log unredacted sensitive data
- Implement additional filtering before external transmission
- Use environment variables for API keys, never hardcode

