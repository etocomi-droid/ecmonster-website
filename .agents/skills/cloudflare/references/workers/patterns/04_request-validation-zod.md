## Request Validation (Zod)

```typescript
import { z } from 'zod';

const userSchema = z.object({
  name: z.string().min(1).max(100),
  email: z.string().email(),
  age: z.number().int().positive().optional(),
});

async function handleCreateUser(request: Request) {
  try {
    const body = await request.json();
    const validated = userSchema.parse(body);  // Throws on invalid data
    return new Response(JSON.stringify({ id: 1, ...validated }), {
      status: 201,
      headers: { 'Content-Type': 'application/json' },
    });
  } catch (err) {
    if (err instanceof z.ZodError) {
      return new Response(JSON.stringify({ errors: err.errors }), { status: 400 });
    }
    throw err;
  }
}
```

**With Hono**: Use `@hono/zod-validator` for automatic validation (see [frameworks.md](./frameworks.md))

