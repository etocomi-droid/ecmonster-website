## Response

```javascript
// Text
return new Response('Hello', { status: 200 });

// JSON
return Response.json({ data }, { status: 200, headers: {...} });

// Redirect
return Response.redirect('/new-path', 301);

// Modify existing
const modified = new Response(response.body, response);
modified.headers.set('X-Custom', 'value');
```

