## From wrangler.toml

Miniflare doesn't auto-read `wrangler.toml`:

```toml
# wrangler.toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2026-01-01"
[[kv_namespaces]]
binding = "KV"
```

```js
// Miniflare equivalent
new Miniflare({
  scriptPath: "src/index.ts",
  compatibilityDate: "2026-01-01",
  kvNamespaces: ["KV"],
});
```
