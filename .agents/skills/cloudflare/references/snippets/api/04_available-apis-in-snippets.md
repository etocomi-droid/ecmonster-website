## Available APIs in Snippets

### ✅ Supported
- `fetch()` - HTTP requests (2-5 subrequests per plan)
- `Request` / `Response` - Standard Web APIs
- `URL` / `URLSearchParams` - URL manipulation
- `Headers` - Header manipulation
- `TextEncoder` / `TextDecoder` - Text encoding
- `crypto.subtle` - Web Crypto API (hashing, signing)
- `crypto.randomUUID()` - UUID generation

### ❌ Not Supported in Snippets
- `caches` API - Not available (use Workers)
- `KV`, `D1`, `R2` - Storage APIs (use Workers)
- `Durable Objects` - Stateful objects (use Workers)
- `WebSocket` - WebSocket upgrades (use Workers)
- `HTMLRewriter` - HTML parsing (use Workers)
- `import` statements - No module imports
- `addEventListener` - Use `export default { async fetch() {}` pattern

