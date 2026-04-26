## API Auth Header Injection

```javascript
export default {
  async fetch(request) {
    if (new URL(request.url).pathname.startsWith("/api/")) {
      const req = new Request(request);
      req.headers.set("X-Internal-Auth", "secret_token");
      req.headers.delete("Authorization");
      return fetch(req);
    }
    return fetch(request);
  }
}
```

