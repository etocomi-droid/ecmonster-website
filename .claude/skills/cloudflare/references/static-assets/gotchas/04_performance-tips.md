## Performance Tips

### 1. Use Hashed Filenames

Enable long-term caching with content-hashed filenames:

```
app.a3b2c1d4.js
styles.e5f6g7h8.css
```

Most bundlers (Vite, Webpack, Parcel) do this automatically.

### 2. Minimize Worker Invocations

Serve assets directly when possible:

```jsonc
{
  "assets": {
    // Only invoke Worker for dynamic routes
    "run_worker_first": ["/api/*", "/auth/*"]
  }
}
```

### 3. Leverage Browser Cache

Set appropriate `Cache-Control` headers:

```typescript
// Versioned assets
'Cache-Control': 'public, max-age=31536000, immutable'

// HTML (revalidate often)
'Cache-Control': 'public, max-age=0, must-revalidate'
```

See patterns.md:169-189 for implementation.

### 4. Use .assetsignore

Reduce upload time by excluding unnecessary files:

```
*.map
*.md
.DS_Store
node_modules/
```

See configuration.md:107-126 for details.
