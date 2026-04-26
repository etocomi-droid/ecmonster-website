## Platform Bindings

```jsonc
{
  "analytics_engine_datasets": [{ "binding": "ANALYTICS" }],
  "mtls_certificates": [{ "binding": "MY_CERT", "certificate_id": "..." }],
  "hyperdrive": [{ "binding": "HYPERDRIVE", "id": "..." }],
  "unsafe": {
    "bindings": [{ "name": "RATE_LIMITER", "type": "ratelimit", "namespace_id": "..." }]
  }
}
```

