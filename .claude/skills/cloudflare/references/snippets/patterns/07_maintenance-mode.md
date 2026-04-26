## Maintenance Mode

```javascript
export default {
  async fetch(request) {
    if (request.headers.get("X-Bypass-Token") === "admin") return fetch(request);
    return new Response("<h1>Maintenance</h1>", {
      status: 503,
      headers: { "Content-Type": "text/html", "Retry-After": "3600" }
    });
  }
}
```

