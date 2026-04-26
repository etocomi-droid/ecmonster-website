## Session Management

```typescript
// List sessions
await puppeteer.sessions(env.MYBROWSER);

// Connect to existing
await puppeteer.connect(env.MYBROWSER, sessionId);

// Check limits
await puppeteer.limits(env.MYBROWSER);
// { remaining: ms, total: ms, concurrent: n }
```

