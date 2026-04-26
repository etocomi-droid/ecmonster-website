### "@callable method returns undefined"

**Cause:** Method doesn't return JSON-serializable value, or has non-serializable types  
**Solution:** Ensure return values are plain objects/arrays/primitives:
```ts
// ❌ Returns class instance
@callable()
async getData() { return new Date(); }

// ✅ Returns serializable object
@callable()
async getData() { return { timestamp: Date.now() }; }
```

