## Storage Bindings

```js
new Miniflare({
  // KV
  kvNamespaces: ["TEST_NAMESPACE", "CACHE"],
  kvPersist: "./kv-data", // Optional: persist to disk
  
  // R2
  r2Buckets: ["BUCKET", "IMAGES"],
  r2Persist: "./r2-data",
  
  // Durable Objects
  modules: true,
  durableObjects: {
    COUNTER: "Counter", // className
    API_OBJECT: { className: "ApiObject", scriptName: "api-worker" },
  },
  durableObjectsPersist: "./do-data",
  
  // D1
  d1Databases: ["DB"],
  d1Persist: "./d1-data",
  
  // Cache
  cache: true, // Default
  cachePersist: "./cache-data",
});
```

