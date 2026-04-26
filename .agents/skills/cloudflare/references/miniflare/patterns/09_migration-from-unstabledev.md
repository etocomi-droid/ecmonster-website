## Migration from unstable_dev

```js
// Old (deprecated)
import { unstable_dev } from "wrangler";
const worker = await unstable_dev("src/index.ts");

// New
import { Miniflare } from "miniflare";
const mf = new Miniflare({ scriptPath: "src/index.ts" });
```

