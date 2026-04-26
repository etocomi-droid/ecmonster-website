## Multiple Workers

```js
new Miniflare({
  workers: [
    {
      name: "main",
      kvNamespaces: { DATA: "shared" },
      serviceBindings: { API: "api-worker" },
      script: `export default { ... }`,
    },
    {
      name: "api-worker",
      kvNamespaces: { DATA: "shared" }, // Shared storage
      script: `export default { ... }`,
    },
  ],
});
```

**With routing:**
```js
workers: [
  { name: "api", scriptPath: "./api.js", routes: ["api.example.com/*"] },
  { name: "web", scriptPath: "./web.js", routes: ["example.com/*"] },
],
```

