## Common Errors

### "Cannot find module"
**Cause:** Module path wrong or `modulesRules` not configured  
**Solution:**
```js
new Miniflare({
  modules: true,
  modulesRules: [{ type: "ESModule", include: ["**/*.js"] }],
});
```

### "Data not persisting"
**Cause:** Persist paths are files, not directories  
**Solution:**
```js
kvPersist: "./data/kv",  // Directory, not file
```

### "Cannot run TypeScript"
**Cause:** Miniflare doesn't transpile TypeScript  
**Solution:** Build first with esbuild/tsc, then run compiled JS

### "`request.cf` is undefined"
**Cause:** CF data not configured  
**Solution:**
```js
new Miniflare({ cf: true }); // Or cf: "./cf.json"
```

### "EADDRINUSE" port conflict
**Cause:** Multiple instances using same port  
**Solution:** Use `dispatchFetch()` (no HTTP server) or `port: 0` for auto-assign

### "Durable Object not found"
**Cause:** Class export doesn't match config name  
**Solution:**
```js
export class Counter {} // Must match
new Miniflare({ durableObjects: { COUNTER: "Counter" } });
```

