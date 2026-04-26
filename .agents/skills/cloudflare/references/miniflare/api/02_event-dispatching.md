## Event Dispatching

**Fetch (no HTTP server):**
```js
const res = await mf.dispatchFetch("http://localhost:8787/path", {
  method: "POST",
  headers: { "Authorization": "Bearer token" },
  body: JSON.stringify({ data: "value" }),
});
```

**Custom Host routing:**
```js
const res = await mf.dispatchFetch("http://localhost:8787/", {
  headers: { "Host": "api.example.com" },
});
```

**Scheduled:**
```js
const worker = await mf.getWorker();
const result = await worker.scheduled({ cron: "30 * * * *" });
// result: { outcome: "ok", noRetry: false }
```

**Queue:**
```js
const worker = await mf.getWorker();
const result = await worker.queue("queue-name", [
  { id: "msg1", timestamp: new Date(), body: "data", attempts: 1 },
]);
// result: { outcome: "ok", retryAll: false, ackAll: false, ... }
```

