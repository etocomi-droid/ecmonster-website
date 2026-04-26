## Web Platform APIs

### Fetch
- `fetch()`, `Request`, `Response`, `Headers`
- `AbortController`, `AbortSignal`

### Streams
- `ReadableStream`, `WritableStream`, `TransformStream`
- Byte streams, BYOB readers

### Web Crypto
- `crypto.subtle` (encrypt/decrypt/sign/verify)
- `crypto.randomUUID()`, `crypto.getRandomValues()`

### Encoding
- `TextEncoder`, `TextDecoder`
- `atob()`, `btoa()`

### Web Standards
- `URL`, `URLSearchParams`
- `Blob`, `File`, `FormData`
- `WebSocket`

### Server-Sent Events (EventSource)
```javascript
// Server-side SSE
const { readable, writable } = new TransformStream();
const writer = writable.getWriter();
writer.write(new TextEncoder().encode('data: Hello\n\n'));
return new Response(readable, {headers: {'Content-Type': 'text/event-stream'}});
```

### HTMLRewriter (HTML Parsing/Transformation)
```javascript
const response = await fetch('https://example.com');
return new HTMLRewriter()
  .on('a[href]', {
    element(el) {
      el.setAttribute('href', `/proxy?url=${encodeURIComponent(el.getAttribute('href'))}`);
    }
  })
  .on('script', { element(el) { el.remove(); } })
  .transform(response);
```

### TCP Sockets (Experimental)
```javascript
const socket = await connect({ hostname: 'example.com', port: 80 });
const writer = socket.writable.getWriter();
await writer.write(new TextEncoder().encode('GET / HTTP/1.1\r\n\r\n'));
const reader = socket.readable.getReader();
const { value } = await reader.read();
return new Response(value);
```

### Performance
- `performance.now()`, `performance.timeOrigin`
- `setTimeout()`, `setInterval()`, `queueMicrotask()`

### Console
- `console.log()`, `console.error()`, `console.warn()`

### Node.js Compat (`nodejs_compat` flag)
```javascript
import { Buffer } from 'node:buffer';
import { randomBytes } from 'node:crypto';

const buf = Buffer.from('Hello');
const random = randomBytes(16);
```

**Available:** `node:buffer`, `node:crypto`, `node:stream`, `node:util`, `node:events`, `node:assert`, `node:path`, `node:querystring`, `node:url`
**NOT available:** `node:fs`, `node:http`, `node:net`, `node:child_process`

