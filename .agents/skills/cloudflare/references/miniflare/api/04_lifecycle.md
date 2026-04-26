## Lifecycle

**Reload:**
```js
await mf.setOptions({
  scriptPath: "worker.js",
  bindings: { VERSION: "2.0" },
});
```

**Watch (manual):**
```js
import { watch } from "fs";

const config = { scriptPath: "worker.js" };
const mf = new Miniflare(config);

watch("worker.js", async () => {
  console.log("Reloading...");
  await mf.setOptions(config);
});
```

**Cleanup:**
```js
await mf.dispose();
```

