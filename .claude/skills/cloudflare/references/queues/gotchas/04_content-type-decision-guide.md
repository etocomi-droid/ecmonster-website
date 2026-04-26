## Content Type Decision Guide

**When to use each content type:**

| Content Type | Use When | Readable By | Supports |
|--------------|----------|-------------|----------|
| `json` (default) | Pull consumers, dashboard visibility, simple objects | All (push/pull/dashboard) | JSON-serializable types only |
| `v8` | Push consumers only, complex JS objects | Push consumers only | Date, Map, Set, BigInt, typed arrays |
| `text` | String-only payloads | All | Strings only |
| `bytes` | Binary data (images, files) | All | ArrayBuffer, Uint8Array |

**Decision tree:**
1. Need to view in dashboard or use pull consumer? → Use `json`
2. Need Date, Map, Set, or other V8 types? → Use `v8` (push consumers only)
3. Just strings? → Use `text`
4. Binary data? → Use `bytes`

```typescript
// Dashboard/pull: use json
await env.QUEUE.send({ id: 123, name: 'test' }, { contentType: 'json' });

// Complex JS types (push only): use v8
await env.QUEUE.send({ 
  created: new Date(), 
  tags: new Set(['a', 'b']) 
}, { contentType: 'v8' });
```

