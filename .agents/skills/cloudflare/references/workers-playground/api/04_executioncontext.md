## ExecutionContext

```javascript
// Background work (after response sent)
ctx.waitUntil(fetch('https://logs.example.com', { method: 'POST', body: '...' }));
return new Response('OK'); // Returns immediately
```

