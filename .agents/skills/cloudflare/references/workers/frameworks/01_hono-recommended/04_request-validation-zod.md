### Request Validation (Zod)

```typescript
import { zValidator } from '@hono/zod-validator';
import { z } from 'zod';

const schema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
});

app.post('/users', zValidator('json', schema), async (c) => {
  const validated = c.req.valid('json');  // Type-safe, validated data
  return c.json({ id: 1, ...validated });
});
```

**Error handling**: Automatic 400 response with validation errors

