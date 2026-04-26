## Advanced Options

```jsonc
{
  // Auto-locate compute near data sources
  "placement": { "mode": "smart" },
  
  // Enable Node.js built-ins (Buffer, process, path, etc.)
  "compatibility_flags": ["nodejs_compat_v2"],
  
  // Observability (10% sampling)
  "observability": { "enabled": true, "head_sampling_rate": 0.1 }
}
```

### Node.js Compatibility

`nodejs_compat_v2` enables:
- `Buffer`, `process.env`, `path`, `stream`
- CommonJS `require()` for Node modules
- `node:` imports (e.g., `import { Buffer } from 'node:buffer'`)

**Note:** Adds ~1-2ms cold start overhead. Use Workers APIs (R2, KV) when possible

