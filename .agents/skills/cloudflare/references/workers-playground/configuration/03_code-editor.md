## Code Editor

### Syntax Requirements

Must export default object with `fetch` handler:

```javascript
export default {
  async fetch(request, env, ctx) {
    return new Response('Hello World');
  }
};
```

**Key Points:**
- Must use ES modules (`export default`)
- `fetch` method receives `(request, env, ctx)`
- Must return `Response` object
- TypeScript not supported (use plain JavaScript)

### Multi-Module Code

Import from external URLs or inline modules:

```javascript
// Import from CDN
import { Hono } from 'https://esm.sh/hono@3';

// Or paste library code and import relatively
// (See patterns.md for multi-module examples)

export default {
  async fetch(request) {
    const app = new Hono();
    app.get('/', (c) => c.text('Hello'));
    return app.fetch(request);
  }
};
```

