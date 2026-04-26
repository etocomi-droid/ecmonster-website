## Authentication

```javascript
export default {
  async fetch(request) {
    const auth = request.headers.get('Authorization');
    if (!auth?.startsWith('Bearer ')) {
      return Response.json({ error: 'Unauthorized' }, { status: 401 });
    }
    const token = auth.substring(7);
    if (token !== 'secret-token') {
      return Response.json({ error: 'Invalid token' }, { status: 403 });
    }
    return Response.json({ message: 'Authenticated' });
  }
};
```

