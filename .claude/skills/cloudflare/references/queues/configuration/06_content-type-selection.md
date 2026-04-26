## Content Type Selection

Choose content type based on consumer type and data requirements:

| Content Type | Use When | Readable By | Supports | Size |
|--------------|----------|-------------|----------|------|
| `json` | Pull consumers, dashboard visibility, simple objects | All (push/pull/dashboard) | JSON-serializable types only | Medium |
| `v8` | Push consumers only, complex JS objects | Push consumers only | Date, Map, Set, BigInt, typed arrays | Small |
| `text` | String-only payloads | All | Strings only | Smallest |
| `bytes` | Binary data (images, files) | All | ArrayBuffer, Uint8Array | Variable |

**Decision tree:**
1. Need to view in dashboard or use pull consumer? → Use `json`
2. Need Date, Map, Set, or other V8 types? → Use `v8` (push consumers only)
3. Just strings? → Use `text`
4. Binary data? → Use `bytes`

```typescript
// JSON: Good for simple objects, pull consumers, dashboard visibility
await env.QUEUE.send({ id: 123, name: 'test' }, { contentType: 'json' });

// V8: Good for Date, Map, Set (push consumers only)
await env.QUEUE.send({ 
  created: new Date(), 
  tags: new Set(['a', 'b']) 
}, { contentType: 'v8' });

// Text: Simple strings
await env.QUEUE.send('process-user-123', { contentType: 'text' });

// Bytes: Binary data
await env.QUEUE.send(imageBuffer, { contentType: 'bytes' });
```

**Default behavior:** If not specified, Cloudflare auto-selects `json` for JSON-serializable objects and `v8` for complex types.

**IMPORTANT:** `v8` messages cannot be read by pull consumers or viewed in the dashboard. Use `json` if you need visibility or pull-based consumption.

