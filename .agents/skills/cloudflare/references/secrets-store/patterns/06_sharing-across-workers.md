## Sharing Across Workers

Same secret, different binding names:

```jsonc
// worker-1: binding="SHARED_DB", secret_name="postgres_url"
// worker-2: binding="DB_CONN", secret_name="postgres_url"
```

