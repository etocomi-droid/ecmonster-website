## Router Pattern

```javascript
const routes = {
  '/': () => new Response('Home'),
  '/api/users': () => Response.json([{ id: 1, name: 'Alice' }])
};

export default {
  async fetch(request) {
    const handler = routes[new URL(request.url).pathname];
    return handler ? handler() : new Response('Not Found', { status: 404 });
  }
};
```

