## CI/CD Tips

```js
// In-memory storage (faster)
new Miniflare({ kvNamespaces: ["TEST"] }); // No persist = in-memory

// Use dispatchFetch (no port conflicts)
await mf.dispatchFetch("http://localhost/");
```

See [gotchas.md](./gotchas.md) for troubleshooting.
