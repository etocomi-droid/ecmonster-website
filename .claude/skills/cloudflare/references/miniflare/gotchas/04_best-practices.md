## Best Practices

**✓ Do:**
- Use `dispatchFetch()` for tests (no HTTP server)
- In-memory storage for CI (omit persist options)
- New instances per test for isolation
- Type-safe bindings with interfaces
- `await mf.dispose()` in cleanup

**✗ Avoid:**
- HTTP server in tests
- Shared instances without cleanup
- Old compatibility dates (use 2026+)

