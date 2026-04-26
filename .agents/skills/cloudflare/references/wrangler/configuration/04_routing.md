## Routing

```jsonc
// Custom domain (recommended)
{ "routes": [{ "pattern": "api.example.com", "custom_domain": true }] }

// Zone-based
{ "routes": [{ "pattern": "api.example.com/*", "zone_name": "example.com" }] }

// workers.dev
{ "workers_dev": true }
```

