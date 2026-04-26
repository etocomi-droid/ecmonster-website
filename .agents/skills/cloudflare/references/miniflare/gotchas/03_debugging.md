## Debugging

**Enable verbose logging:**
```js
import { Log, LogLevel } from "miniflare";
new Miniflare({ log: new Log(LogLevel.DEBUG) });
```

**Chrome DevTools:**
```js
const url = await mf.getInspectorURL();
console.log(`DevTools: ${url}`); // Open in Chrome
```

**Inspect bindings:**
```js
const env = await mf.getBindings();
console.log(Object.keys(env));
```

**Verify storage:**
```js
const ns = await mf.getKVNamespace("TEST");
const { keys } = await ns.list();
```

