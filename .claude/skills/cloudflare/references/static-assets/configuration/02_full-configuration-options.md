### Full Configuration Options

```jsonc
{
  "name": "my-worker",
  "main": "src/index.ts",
  "compatibility_date": "2025-01-01",
  "assets": {
    "directory": "./dist",
    "binding": "ASSETS",
    "not_found_handling": "single-page-application",
    "html_handling": "auto-trailing-slash",
    "run_worker_first": ["/api/*", "!/api/docs/*"]
  }
}
```

**Configuration keys:**

- `directory` (string, required): Path to assets folder (e.g. `./dist`, `./public`, `./build`)
- `binding` (string, optional): Name to access assets in Worker code (e.g. `env.ASSETS`). Default: `"ASSETS"`
- `not_found_handling` (string, optional): Behavior when asset not found
  - `"single-page-application"`: Serve `/index.html` for non-asset paths (default for SPAs)
  - `"404-page"`: Serve `/404.html` if present, otherwise 404
  - `"none"`: Return 404 for missing assets
- `html_handling` (string, optional): URL trailing slash behavior
- `run_worker_first` (boolean | string[], optional): Routes that invoke Worker before checking assets

