## Workers KV (cloudflare.WorkersKvNamespace)

```typescript
const kv = new cloudflare.WorkersKvNamespace("my-kv", {
    accountId: accountId,
    title: "my-kv-namespace",
});

// Write values
const kvValue = new cloudflare.WorkersKvValue("config", {
    accountId: accountId,
    namespaceId: kv.id,
    key: "config",
    value: JSON.stringify({foo: "bar"}),
});
```

