### "startWorker doesn't match production"

**Cause:** Using local mode when remote resources needed
**Solution:** Use `remote` option:
```typescript
const worker = await startWorker({ 
  config: "wrangler.jsonc",
  remote: true  // or "minimal" for faster tests
});
```

