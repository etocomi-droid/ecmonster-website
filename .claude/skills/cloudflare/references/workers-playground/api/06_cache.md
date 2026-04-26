## Cache

```javascript
const cache = caches.default;

// Check cache
let response = await cache.match(request);
if (!response) {
  response = await fetch(origin);
  await cache.put(request, response.clone()); // Clone before put!
}
return response;
```

