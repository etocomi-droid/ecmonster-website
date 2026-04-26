## Hono Framework

```javascript
import { Hono } from 'https://esm.sh/hono@3';
const app = new Hono();
app.get('/', (c) => c.text('Hello'));
app.get('/api/users/:id', (c) => c.json({ id: c.req.param('id') }));
app.notFound((c) => c.json({ error: 'Not found' }, 404));
export default app;
```

