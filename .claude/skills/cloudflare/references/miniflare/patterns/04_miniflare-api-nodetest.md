## Miniflare API (node:test)

```js
import assert from "node:assert";
import test, { after, before } from "node:test";
import { Miniflare } from "miniflare";

let mf;
before(() => {
  mf = new Miniflare({ scriptPath: "src/index.js", kvNamespaces: ["TEST_KV"] });
});

test("fetch", async () => {
  const res = await mf.dispatchFetch("http://localhost/");
  assert.strictEqual(await res.text(), "Hello");
});

after(() => mf.dispose());
```

