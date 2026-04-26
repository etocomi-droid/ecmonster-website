## HTTP Server & Request.cf

```js
new Miniflare({
  port: 8787,              // Default: 8787
  host: "127.0.0.1",
  https: true,             // Self-signed cert
  liveReload: true,        // Auto-reload HTML
  
  cf: true,                // Fetch live Request.cf data (cached)
  // cf: "./cf.json",      // Or load from file
  // cf: { colo: "DFW" },  // Or inline mock
});
```

**Note:** For tests, use `dispatchFetch()` (no port conflicts).

