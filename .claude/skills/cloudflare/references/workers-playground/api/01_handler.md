## Handler

```javascript
export default {
  async fetch(request, env, ctx) {
    // request: Request, env: {} (empty in playground), ctx: ExecutionContext
    return new Response('Hello');
  }
};
```

