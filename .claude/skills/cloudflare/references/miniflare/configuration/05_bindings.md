## Bindings

```js
new Miniflare({
  // Environment variables
  bindings: {
    SECRET_KEY: "my-secret-value",
    API_URL: "https://api.example.com",
    DEBUG: true,
  },
  
  // Other bindings
  wasmBindings: { ADD_MODULE: "./add.wasm" },
  textBlobBindings: { TEXT: "./data.txt" },
  queueProducers: ["QUEUE"],
});
```

