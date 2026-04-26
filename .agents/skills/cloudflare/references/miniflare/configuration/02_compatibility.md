## Compatibility

```js
new Miniflare({
  compatibilityDate: "2026-01-01", // Use recent date for latest features
  compatibilityFlags: [
    "nodejs_compat",        // Node.js APIs (process, Buffer, etc)
    "streams_enable_constructors", // Stream constructors
  ],
  upstream: "https://example.com", // Fallback for unhandled requests
});
```

**Critical:** Use `compatibilityDate: "2026-01-01"` or latest to match production runtime. Old dates limit available APIs.

