## Jurisdiction (Data Locality)

Specify jurisdiction at ID creation for data residency compliance:

```typescript
// EU data residency
const id = env.MY_DO.idFromName("user:123", { jurisdiction: "eu" })

// Available jurisdictions
const jurisdictions = ["eu", "fedramp"]  // More may be added

// All operations on this DO stay within jurisdiction
const stub = env.MY_DO.get(id)
await stub.someMethod()  // Data stays in EU
```

**Key points:**
- Set at ID creation time, immutable afterward
- DO instance physically located within jurisdiction
- Storage and compute guaranteed within boundary
- Use for GDPR, FedRAMP, other compliance requirements
- No cross-jurisdiction access (requests fail if DO in different jurisdiction)

