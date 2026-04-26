## Multi-Tenancy Strategy

```
How many tenants?
├─ < 50K tenants → Use namespaces (recommended)
│   ├─ Fastest (filter before vector search)
│   └─ Strict isolation
├─ > 50K tenants → Use metadata filtering
│   ├─ Slower (post-filter after vector search)
│   └─ Requires metadata index
└─ Per-tenant indexes → Only if compliance mandated
    └─ 50K index limit per account (paid plan)
```

