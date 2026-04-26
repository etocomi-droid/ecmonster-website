## Common Errors

### CPU Time Exceeded

**Cause:** Heavy parsing, large emails

**Solution:**
```typescript
const size = parseInt(message.headers.get("content-length") || "0") / 1024 / 1024;
if (size > 20) {
  message.setReject("Too large");
  return;
}

ctx.waitUntil(expensiveWork());
await message.forward("dest@example.com");
```

### Rule Not Triggering

**Causes:** Priority conflict, matcher error, catch-all override

**Solution:** Check priority (lower=first), verify exact match, confirm destination verified

### Undefined Property

**Cause:** Missing header

**Solution:**
```typescript
// ❌ WRONG
const subj = message.headers.get("subject").toLowerCase();

// ✅ CORRECT
const subj = message.headers.get("subject")?.toLowerCase() || "";
```

