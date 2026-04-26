## Location Control

```typescript
// Jurisdiction (GDPR/FedRAMP)
const euNamespace = env.MY_DO.jurisdiction("eu");
const id = euNamespace.newUniqueId();
const stub = euNamespace.get(id);

// Location hint (best effort)
const stub = env.MY_DO.get(id, { locationHint: "enam" });
// Hints: wnam, enam, sam, weur, eeur, apac, oc, afr, me
```

