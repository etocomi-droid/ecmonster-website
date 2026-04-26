## CORS Handling

```javascript
export default {
  async fetch(request) {
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
          'Access-Control-Allow-Headers': 'Content-Type, Authorization'
        }
      });
    }
    const response = await fetch('https://api.example.com', request);
    const modified = new Response(response.body, response);
    modified.headers.set('Access-Control-Allow-Origin', '*');
    return modified;
  }
};
```

