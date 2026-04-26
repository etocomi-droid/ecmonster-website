## Key Concepts

### Envelope vs Headers

- **Envelope addresses** (`message.from`, `message.to`): SMTP transport addresses (trusted)
- **Header addresses** (parsed from body): Display addresses (can be spoofed)

Use envelope addresses for security decisions.

### Single-Use Streams

`message.raw` is a ReadableStream that can only be read once. Buffer to ArrayBuffer for multiple uses.

```typescript
// Buffer first
const buffer = await new Response(message.raw).arrayBuffer();
const email = await PostalMime.parse(buffer);
```

See [gotchas.md](./gotchas.md#readablestream-can-only-be-consumed-once) for details.

### Verified Destinations

`forward()` only works with addresses verified in the Cloudflare Email Routing dashboard. Add destinations before deployment.

