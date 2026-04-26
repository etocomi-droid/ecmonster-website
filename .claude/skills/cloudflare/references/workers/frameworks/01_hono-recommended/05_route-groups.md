### Route Groups

```typescript
const api = new Hono().basePath('/api');

api.get('/users', (c) => c.json([]));
api.post('/users', (c) => c.json({ id: 1 }));

app.route('/', api);  // Mounts at /api/*
```

