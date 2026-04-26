## Static Assets

Deploy HTML/CSS/images with Workers. See [api.md](./api.md#static-assets) for upload process.

### Wrangler
```jsonc
{
  "name": "customer-site",
  "main": "./src/index.js",
  "assets": {
    "directory": "./public",
    "binding": "ASSETS"
  }
}
```

```bash
npx wrangler deploy --name customer-site --dispatch-namespace production
```

### Dashboard Deployment

Alternative to CLI:

1. Upload Worker file in dashboard
2. Add `--dispatch-namespace` flag: `wrangler deploy --dispatch-namespace production`
3. Or configure in wrangler.jsonc under `dispatch_namespaces`

See [api.md](./api.md) for programmatic deployment via REST API or SDK.

