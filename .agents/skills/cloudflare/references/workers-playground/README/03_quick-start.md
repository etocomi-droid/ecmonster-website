## Quick Start

Minimal Worker:

```javascript
export default {
  async fetch(request, env, ctx) {
    return new Response('Hello World');
  }
};
```

JSON API:

```javascript
export default {
  async fetch(request, env, ctx) {
    const data = { message: 'Hello', timestamp: Date.now() };
    return Response.json(data);
  }
};
```

Proxy with modification:

```javascript
export default {
  async fetch(request, env, ctx) {
    const response = await fetch('https://example.com');
    const modified = new Response(response.body, response);
    modified.headers.set('X-Custom-Header', 'added-by-worker');
    return modified;
  }
};
```

Import from CDN:

```javascript
import { Hono } from 'https://esm.sh/hono@3';

export default {
  async fetch(request) {
    const app = new Hono();
    app.get('/', (c) => c.text('Hello Hono!'));
    return app.fetch(request);
  }
};
```

