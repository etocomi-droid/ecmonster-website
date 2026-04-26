## Security Headers

```javascript
export default {
  async fetch(request) {
    const response = await fetch(request);
    const newResponse = new Response(response.body, response);
    newResponse.headers.set("X-Frame-Options", "DENY");
    newResponse.headers.set("X-Content-Type-Options", "nosniff");
    newResponse.headers.delete("X-Powered-By");
    return newResponse;
  }
}
```

**Rule:** `true` (all requests)

