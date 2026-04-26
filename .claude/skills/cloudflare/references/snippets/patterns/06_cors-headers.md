## CORS Headers

```javascript
export default {
  async fetch(request) {
    if (request.method === "OPTIONS") {
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE",
          "Access-Control-Allow-Headers": "Content-Type, Authorization"
        }
      });
    }
    const response = await fetch(request);
    const newResponse = new Response(response.body, response);
    newResponse.headers.set("Access-Control-Allow-Origin", "*");
    return newResponse;
  }
}
```

