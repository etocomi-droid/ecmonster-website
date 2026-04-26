## WebSocket Testing

```js
const res = await mf.dispatchFetch("http://localhost/ws", {
  headers: { Upgrade: "websocket" },
});
assert.strictEqual(res.status, 101);
```

