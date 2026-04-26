### "False no-changes detection" - Content SHA unchanged

**Problem:** Worker code updated, Pulumi says "no changes"  
**Cause:** Content hash identical (whitespace/comment-only change)  
**Solution:** Add build timestamp or version to force update

```typescript
const version = Date.now().toString();
const worker = new cloudflare.WorkerScript("worker", {
    content: code,
    plainTextBindings: [{name: "VERSION", text: version}], // Forces new deployment
});
```

