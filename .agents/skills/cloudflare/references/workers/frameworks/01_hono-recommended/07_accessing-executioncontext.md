### Accessing ExecutionContext

```typescript
export default {
  fetch(request: Request, env: Env, ctx: ExecutionContext) {
    return app.fetch(request, env, ctx);
  },
};

// In route handlers:
app.get('/log', (c) => {
  c.executionCtx.waitUntil(logRequest(c.req));
  return c.text('OK');
});
```

