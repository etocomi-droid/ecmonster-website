## Bindings Access

**Environment variables:**
```js
// Basic usage
const bindings = await mf.getBindings();
console.log(bindings.SECRET_KEY);

// With type safety (recommended):
interface Env {
  SECRET_KEY: string;
  API_URL: string;
  KV: KVNamespace;
}
const env = await mf.getBindings<Env>();
env.SECRET_KEY; // string (typed!)
env.KV.get("key"); // KVNamespace methods available
```

**Request.cf object:**
```js
const cf = await mf.getCf();
console.log(cf?.colo); // "DFW"
console.log(cf?.country); // "US"
```

**KV:**
```js
const ns = await mf.getKVNamespace("TEST_NAMESPACE");
await ns.put("key", "value");
const value = await ns.get("key");
```

**R2:**
```js
const bucket = await mf.getR2Bucket("BUCKET");
await bucket.put("file.txt", "content");
const object = await bucket.get("file.txt");
```

**Durable Objects:**
```js
const ns = await mf.getDurableObjectNamespace("COUNTER");
const id = ns.idFromName("test");
const stub = ns.get(id);
const res = await stub.fetch("http://localhost/");

// Access storage directly:
const storage = await mf.getDurableObjectStorage(id);
await storage.put("key", "value");
```

**D1:**
```js
const db = await mf.getD1Database("DB");
await db.exec(`CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT)`);
await db.prepare("INSERT INTO users (name) VALUES (?)").bind("Alice").run();
```

**Cache:**
```js
const caches = await mf.getCaches();
const defaultCache = caches.default;
await defaultCache.put("http://example.com", new Response("cached"));
```

**Queue producer:**
```js
const producer = await mf.getQueueProducer("QUEUE");
await producer.send({ body: "message data" });
```

