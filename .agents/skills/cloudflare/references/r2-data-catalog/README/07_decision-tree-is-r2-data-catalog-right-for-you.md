## Decision Tree: Is R2 Data Catalog Right For You?

```
Start → Need analytics on object storage data?
         │
         ├─ No → Use R2 directly for object storage
         │
         └─ Yes → Dataset >1GB with structured schema?
                  │
                  ├─ No → Too small, use R2 + ad-hoc queries
                  │
                  └─ Yes → Need ACID transactions or schema evolution?
                           │
                           ├─ No → Consider simpler solutions (Parquet on R2)
                           │
                           └─ Yes → Need multi-cloud/multi-tool access?
                                    │
                                    ├─ No → D1 or external DB may be simpler
                                    │
                                    └─ Yes → ✅ Use R2 Data Catalog
```

**Quick check:** If you answer "yes" to all:
- Dataset >1GB and growing
- Structured/tabular data (logs, events, metrics)
- Multiple query tools or cloud environments
- Need versioning, schema changes, or concurrent access

→ R2 Data Catalog is a good fit.

