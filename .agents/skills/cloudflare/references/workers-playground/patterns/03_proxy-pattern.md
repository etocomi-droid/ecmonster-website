## Proxy Pattern

```javascript
export default {
  async fetch(request) {
    const url = new URL(request.url);
    url.hostname = 'api.example.com';
    return fetch(url.toString(), {
      method: request.method, headers: request.headers, body: request.body
    });
  }
};
```

