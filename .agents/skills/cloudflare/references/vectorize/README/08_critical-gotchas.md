## Critical Gotchas

See `gotchas.md` for details. Most important:

1. **Async mutations**: Inserts take 5-10s to be queryable
2. **500 batch limit**: Workers API enforces 500 vectors per call (undocumented)
3. **Metadata truncation**: `"indexed"` returns first 64 bytes only
4. **topK with metadata**: Max 20 (not 100) when using returnValues or returnMetadata: "all"
5. **Metadata indexes first**: Must create before inserting vectors

