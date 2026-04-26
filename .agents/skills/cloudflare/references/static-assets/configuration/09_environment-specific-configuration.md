### Environment-Specific Configuration

Use `wrangler.jsonc` environments for different configs:

```jsonc
{
  "name": "my-worker",
  "assets": { "directory": "./dist" },
  "env": {
    "staging": {
      "assets": {
        "not_found_handling": "404-page"
      }
    },
    "production": {
      "assets": {
        "not_found_handling": "single-page-application"
      }
    }
  }
}
```

Deploy with: `wrangler deploy --env staging`
