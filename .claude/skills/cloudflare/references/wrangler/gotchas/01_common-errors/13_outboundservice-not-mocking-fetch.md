### "outboundService not mocking fetch"

**Cause:** Mock function not returning Response
**Solution:** Always return Response, use `fetch(req)` for passthrough:
```typescript
const worker = await startWorker({
  outboundService: (req) => {
    if (shouldMock(req)) {
      return new Response("mocked");
    }
    return fetch(req);  // Required for non-mocked requests
  }
});
```

