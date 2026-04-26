## Environments

```jsonc
{
  "name": "my-worker",
  "vars": { "ENV": "dev" },
  "env": {
    "production": {
      "name": "my-worker-prod",
      "vars": { "ENV": "prod" },
      "route": { "pattern": "example.com/*", "zone_name": "example.com" }
    }
  }
}
```

Deploy: `wrangler deploy --env production`

