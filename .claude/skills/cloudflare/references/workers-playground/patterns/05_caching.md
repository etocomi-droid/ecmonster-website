## Caching

```javascript
export default {
  async fetch(request) {
    if (request.method !== 'GET') return fetch(request);
    const cache = caches.default;
    let response = await cache.match(request);
    if (!response) {
      response = await fetch('https://api.example.com');
      if (response.status === 200) await cache.put(request, response.clone());
    }
    return response;
  }
};
```

