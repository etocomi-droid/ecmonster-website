### "Binding name mismatch"

**Problem:** Worker fails with "env.MY_KV is undefined"  
**Cause:** Binding name in Pulumi != name in Worker code  
**Solution:** Match exactly (case-sensitive)

```typescript
// Pulumi
kvNamespaceBindings: [{name: "MY_KV", namespaceId: kv.id}]

// Worker code
export default { async fetch(request, env) { await env.MY_KV.get("key"); }}
```

