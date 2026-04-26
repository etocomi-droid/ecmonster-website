## Logging & Performance

```js
import { Log, LogLevel } from "miniflare";

new Miniflare({
  log: new Log(LogLevel.DEBUG), // DEBUG | INFO | WARN | ERROR | NONE
  scriptTimeout: 30000,         // CPU limit (ms)
  workersConcurrencyLimit: 10,  // Max concurrent workers
});
```

