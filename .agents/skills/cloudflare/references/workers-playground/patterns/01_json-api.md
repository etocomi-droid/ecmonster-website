## JSON API

```javascript
export default {
  async fetch(request) {
    const url = new URL(request.url);
    if (url.pathname === '/api/hello') return Response.json({ message: 'Hello' });
    if (url.pathname === '/api/echo' && request.method === 'POST') {
      return Response.json({ received: await request.json() });
    }
    return Response.json({ error: 'Not found' }, { status: 404 });
  }
};
```

