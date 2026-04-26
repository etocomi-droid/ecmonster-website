## Other Frameworks

### itty-router (Minimalist)

```typescript
import { Router } from 'itty-router';

const router = Router();

router.get('/users/:id', ({ params }) => new Response(params.id));

export default { fetch: router.handle };
```

**Use case**: Tiny bundle size (~500 bytes), simple routing needs

### Worktop (Advanced)

```typescript
import { Router } from 'worktop';

const router = new Router();

router.add('GET', '/users/:id', (req, res) => {
  res.send(200, { id: req.params.id });
});

router.listen();
```

**Use case**: Advanced routing, built-in CORS/cache utilities

