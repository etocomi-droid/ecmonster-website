## Test Isolation & Mocking

```js
// Per-test isolation
beforeEach(() => { mf = new Miniflare({ kvNamespaces: ["TEST"] }); });
afterEach(() => mf.dispose());

// Mock external APIs
new Miniflare({
  workers: [
    { name: "main", serviceBindings: { API: "mock-api" }, script: `...` },
    { name: "mock-api", script: `export default { async fetch() { return Response.json({mock: true}); } }` },
  ],
});
```

