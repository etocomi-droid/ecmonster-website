## Debugging

**Inspector URL for DevTools:**
```js
const url = await mf.getInspectorURL();
console.log(`DevTools: ${url}`);
// Open in Chrome DevTools for breakpoints, profiling
```

**Wait for server ready:**
```js
const mf = new Miniflare({ scriptPath: "worker.js" });
const url = await mf.ready; // Promise<URL>
console.log(`Server running at ${url}`); // http://127.0.0.1:8787

// Note: dispatchFetch() waits automatically, no need to await ready
const res = await mf.dispatchFetch("http://localhost/"); // Works immediately
```

See [configuration.md](./configuration.md) for all constructor options.
