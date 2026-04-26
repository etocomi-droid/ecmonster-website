## Script Loading

```js
// Inline
new Miniflare({ modules: true, script: `export default { ... }` });

// File-based
new Miniflare({ scriptPath: "worker.js" });

// Multi-module
new Miniflare({
  scriptPath: "src/index.js",
  modules: true,
  modulesRules: [
    { type: "ESModule", include: ["**/*.js"] },
    { type: "Text", include: ["**/*.txt"] },
  ],
});
```

