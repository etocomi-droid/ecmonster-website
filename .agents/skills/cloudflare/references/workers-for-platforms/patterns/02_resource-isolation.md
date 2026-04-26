## Resource Isolation

**Complete isolation:** Create unique resources per customer
- KV namespace per customer
- D1 database per customer
- R2 bucket per customer

```typescript
const bindings = [{
  type: "kv_namespace",
  name: "USER_KV",
  namespace_id: `customer-${customerId}-kv`
}];
```

